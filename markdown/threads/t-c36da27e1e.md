[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL: It's Everywhere

_79 messages · 16 participants · 2009-09 → 2009-10_

---

### COBOL: It's Everywhere

- **From:** rick.malek@microfocus.com
- **Date:** 2009-09-03T12:38:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com>`

```
For those of you who haven't seen it or heard about it, there are new
COBOL articles being published on the C#Corner (http://www.c-
sharpcorner.com) dealing with COBOL and .NET integration. Look for
'COBOL.NET' in the left navigation pane.

Also there is a new COBOL blog at http://itsacobolworld.blogspot.com/.
Check it out and leave a comment!
```

#### ↳ Re: COBOL: It's Everywhere

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-04T13:30:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7rnje01nqi@news5.newsguy.com>`
- **In-Reply-To:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com>`

```
rick.malek@microfocus.com wrote:
> For those of you who haven't seen it or heard about it, there are new
> COBOL articles being published on the C#Corner (http://www.c-
> sharpcorner.com) dealing with COBOL and .NET integration. Look for
> 'COBOL.NET' in the left navigation pane.

Love that word-wrapped URL. I guess G2 doesn't know to skip URLs when
it applies its word-wrapping algorithm. (You can also use
"csharpcorner.com" without the hyphen, by the way; apparently they've
grabbed that as a CNAME.)

Looks like there's some interesting material here. Unfortunately
csharpcorner.com isn't what you'd call a well-designed site (over 400
SGML validation errors per page, doesn't work without scripting
enabled, etc), but it could be worth checking out if you're willing to
put up with that sort of thing.

> Also there is a new COBOL blog at http://itsacobolworld.blogspot.com/.

... which is much easier to read, thanks to its clean design.

Anyway, thanks for posting these, Rick. After reading Atwood's sad
can't-be-bothered-to-learn-about-my-subject COBOL piece on Coding
Horror, it's nice to think that there might be a few informed blog
posts on the subject out there for the casual reader to stumble across.
```

##### ↳ ↳ Re: COBOL: It's Everywhere

- **From:** Louis Krupp <lkrupp_nospam@indra.com.invalid>
- **Date:** 2009-09-05T02:52:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U-6dnTaz4LVGuz_XnZ2dnUVZ_oednZ2d@indra.net>`
- **In-Reply-To:** `<h7rnje01nqi@news5.newsguy.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <h7rnje01nqi@news5.newsguy.com>`

```
Michael Wojcik wrote:
> rick.malek@microfocus.com wrote:
<snip>
>> Also there is a new COBOL blog at http://itsacobolworld.blogspot.com/.
> 
…[6 more quoted lines elided]…
> 

I posted a comment clarifying (to the best of my knowledge) the state of 
standardization for other languages mentioned in the blog.

Louis
```

#### ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-06T06:30:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gfp1jF2pfqolU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com>`

```
rick.malek@microfocus.com wrote:
> For those of you who haven't seen it or heard about it, there are new
> COBOL articles being published on the C#Corner (http://www.c-
…[4 more quoted lines elided]…
> Check it out and leave a comment!

I frequent C# corner but haven't been there for a while.

Can anyone explain to me what the point of COBOL.NET is?

It allows people to perpetuate the travesties of procedural code into a 
modern OO environment. The code I've seen in it is verbose compared to C#, 
(or even VB.NET), it doesn't buy me anything (apart from an expensive 
compiler, when the .NET languages are free...), I just don't get it.

I was thinking about this a couple of days ago when a Client told me he'd 
bought Fujitsu NetCOBOL for .NET. I asked him what he planned to do with it 
and he wasn't sure but "thought it would be useful".

"I need to run some Legacy in the .NET environment..."

"You can do that with the compiler you already have."

"Really? The rep told me I should get 2 copies of this before the price goes 
up next month..."

(Fujitsu NetCOBOL runs extremely well as native code under InterOp services. 
It isn't essential, but it is advisable to wrap it as COM to standardise the 
interface, just as we demonstrated with the cobdata tool on 
http://primacomputing.co.nz/cobol21  I had a look at the figures for that 
site the other day and over 100 people have downloaded the tool, but less 
than 40 have downloaded the source... I guess that says that people want 
results more than they want enlightenment :-). That being the case, you'd 
wonder why they want to wade through COBOL when writing for .NET... I guess 
if you know no different you do what you can.)

This is a place with a longer term goal to move away from COBOL, so why 
would they invest thousands of dollars into a compiler and environment they 
simply don't need?

He isn't very happy at the moment and I suspect he'll be even more unhappy 
after talking to Alchemy...

Is COBOL Land so absolutely bewildered by change that they are now doing 
what reps tell them?

It's really pretty simple:  If you want to use the .NET Framework, use a 
.NET language. They're easy to learn, fast to write, efficient, and free. 
Furthermore, they integrate perfectly into the environment they were 
invented for. You don't have to hobble around like Jake the Peg with his 
extra leg (Object Orientation bolted onto COBOL), even though the actual 
bolting was a fantastic feat, it is still an extra leg and COBOL is never 
entirely comfortable with OO. I've been using it for 12 years and I still 
like C# better.

I have a theory about .NET COBOL...

Some years back some of the vendors who were vulnerable to the demise of 
COBOL  realized they had to modernize the product if it was to have any show 
of being around and continung to generate revenue. The obvious "future 
platform" at the time was .NET, so they targeted that and decided to provide 
COBOL compilers that could generate CLR.

The COBOL world was just starting to realize how seriously they missed the 
boat with OO Design and Programming  and were seeing their jobs evaporate 
and their systems being replaced by a new breed who grew up with computers 
and were not constrained by 1960s programming practices for computer system 
development.

It wasn't too hard for the COBOL vendors to blow the horn and say: "Over 
here! YOU can be a part of the Brave New World! Look! We can compile COBOL 
for .NET!!!

Nobody seemed to stop and ask: "Why?"

Why would I pay several thousand dollars for a compiler I don't need, when I 
can download a free one in minutes, along with a far superior IDE ?
(Just compare Fujitsu's NetCOBOL Project Manager with VS 2008... It is no 
coincidence that .NET COBOL ships with VS, but it doesn't integrate properly 
with it from what I hear...still, that's hearsay and may not be true for 
everybody.)

Why would I perpetuate a programming paradigm that is well past its "sell 
by" date into an environment that is completely foreign to it? So I can tell 
people "we moved our legacy to .NET" (even if said legacy DOES degrade every 
other system we try and run...)

The only possible justification I can see for the existence of .NET COBOL is 
to generate revenue for vendors.

I have some empathy with people who refactor COBOL, wrap it as objects, 
while they get their staff trained in the new environments and languages. 
That makes sense. At least the legacy is being transformed to fit the new 
environment, not just recompiled as it stands.

A growing number of people (and I am doing business with some of them) are 
becoming disullusioned with being held over a barrel for maintenance of a 
compiler that shows no significant changes each year, that can't implement a 
standard already 7 years old (with 17 years for the standard before that), 
and that implements a paradigm intended for centralized mainframes back in 
the middle of the last century.

Fortunately, despite what you are led to believe in certain quarters, it 
ISN'T hard (or expensive even) to migrate away from COBOL. There are tools 
available now that can automate the whole task of moving off your indexed 
file system, and can generate a complete OO data access layer that runs in 
.NET, that can work with COBOL (while you're in transition) and with 
anything you like after that, without change. Simple tools that don't 
require complex mappings and data analysis to build a normalized Relational 
DB from your COBOL data definitions.

I guess it might be useful to write some .NET components in COBOL, but I 
can't think of any off-hand that couldn't be just as easily written in C#, 
VB, or C++.

I was offered a .NET COBOL license by someone who had no further use for it 
and I politely declined.

5 years ago, I would have grabbed it; today, I simply don't want or need it.

Despite the desperate talk and ridiculously inflated and outdated figures, 
COBOL simply isn't going anywhere. And that includes .NET COBOL.

The role of COBOL will be batch processing and legacy maintenance until 
legacy can be replaced. It'll take a few years, but no-one planning a career 
can be seriously looking at COBOL.

That is no reflection on COBOL. The world changed. Dramatically, and in a 
relatively short space of time (say, 30 years...)

It lasted over half a century and it is fun to learn and write, but it is 
simply not viable in the modern world.

My advice:  Spend your money on training and upskilling, not on pointless 
compilers and non-visible maintenance for them .

Pete.
```

##### ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-09-05T16:54:16-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u6g5a59nfgpibdm6b2557k500dngv69ak4@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net>`

```
Note: top posted

Can you always get the same results in arithmetic calculations with C#
that you can in COBOL where inputs and outputs are defined the same?
Are there exact equivalents to the S9(n)V9(n) COBOL field descriptions
where n stands for any legal number in C#?  If I were going to be
consulting or programming where I would need C# I would look it up but
I am spending my time these days research rail and other passenger
transportation.

/End all new posting 
Clark

On Sun, 6 Sep 2009 06:30:18 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>rick.malek@microfocus.com wrote:
>> For those of you who haven't seen it or heard about it, there are new
…[137 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-06T12:05:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ggcl6F2pt41sU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <u6g5a59nfgpibdm6b2557k500dngv69ak4@4ax.com>`

```
Clark F Morris wrote:
> Note: top posted
>
> Can you always get the same results in arithmetic calculations with C#
> that you can in COBOL where inputs and outputs are defined the same?

Yes. Decimal classes have been implemented for years.

> Are there exact equivalents to the S9(n)V9(n) COBOL field descriptions
> where n stands for any legal number in C#?  If I were going to be
> consulting or programming where I would need C# I would look it up but
> I am spending my time these days research rail and other passenger
> transportation.

Small world... so am I :-)

Not researching it but providing services for it.

No more below.

Pete.
>
> /End all new posting
…[153 more quoted lines elided]…
>> Pete.
```

##### ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2009-09-05T16:04:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FiBom.161394$0e4.43780@newsfe19.iad>`
- **In-Reply-To:** `<7gfp1jF2pfqolU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net>`

```
Our Resident Expert wrote :
> rick.malek@microfocus.com wrote:
> 
…[16 more quoted lines elided]…
> compiler, when the .NET languages are free...), I just don't get it.

<snipped>

You do recall the name Tesco from your UK days ?

Jack Cohen, (later Sir Jack), started in the East End of London just 
after WWII selling damaged cans of food from a wheelbarrow. I visited 
their HQ back in mid-70s before I designed our FoodHall system for 
Debenhams. (The Tesco name has been around since about 1929).

1. "Tesco expands into China

Tesco has signed a joint venture deal with China's largest food company, 
Ting Hsin, representing the first move into China by Britain's biggest 
supermarket chain. Tesco is to buy 50% of Ting Hsin's hypermarket 
division (Hymall) for ï¿½140 million.

Tesco currently has a presence in 12 countries, including Hungary, 
Poland, South Korea, Taiwan and Japan. "China is one of the largest 
economies in the world with tremendous forecast growth," said Tesco's 
Sir Terry Leahy.

Source: The Grocer [sub req], Reuters, BBC"

2. "The top 10 most valuable retail brands in the UK are:

1. Tesco ï¿½8.6bn (Primarily food)
2. Sainsbury's ï¿½4.9bn (primarily food)
3. Marks & Spencer ï¿½3.9bn (fashion and food)
4. Asda ï¿½3.6bn (WalMart - primarily food)
5. Morrisons ï¿½2.6bn (Primarily food)
6. Boots ï¿½1.9bn (Pharmacy)
7. Argos ï¿½1.4bn (?? - probably food)
8. Co-operative ï¿½1.4bn (Food and fashion)
9. Waitrose ï¿½1.2bn (Primarily food)
10. John Lewis ï¿½1.1bn (Deparmtment stores)

Source : Sky News"

3. And then :-

Tesco and Micro Focus :

http://www.microfocus.com/AboutMicroFocus/pressroom/releases/pr20070312123456.asp
http://www.computerworlduk.com/management/it-business/it-department/news/index.cfm?newsid=2191

4. From your perspective, I guess the IT Department at Tesco must have 
got it all wrong ?
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-05T22:35:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7up35$mms$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad>`

```
In article <FiBom.161394$0e4.43780@newsfe19.iad>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:

[snip]

>1. "Tesco expands into China
>
…[14 more quoted lines elided]…
>1. Tesco ?8.6bn (Primarily food)

[snip]

>Source : Sky News"
>
…[8 more quoted lines elided]…
>got it all wrong ?

Mr Gavan, are you attempting to say that something of value might be 
learned from the actual processes and practises employed by an 
international company which uses DP/IS/IT as a tool (not as a primary 
focus) and operates in a business where razor-thin margins can make or 
break an organisation?

What folly... next thing you know you'll be questioning whether I am the 
King of England... God Save the Me!

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-06T12:33:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ggea4F2pgfcjU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad>`

```
James J. Gavan wrote:
> Our Resident Expert wrote :
>> rick.malek@microfocus.com wrote:
…[23 more quoted lines elided]…
> You do recall the name Tesco from your UK days ?

Yes, though I preferred to shop at Sainsburys.
>
> Jack Cohen, (later Sir Jack), started in the East End of London just
…[31 more quoted lines elided]…
> Source : Sky News"

The grocery industry is currently the biggest rip-off on the planet. They 
don't care about recessions or hard times they just continue ripping off 
suppliers and consumers alike...
>
> 3. And then :-
…[3 more quoted lines elided]…
> http://www.microfocus.com/AboutMicroFocus/pressroom/releases/pr20070312123456.asp

A press release from Micro Focus with the word COBOL in it once. And that is 
to say they are porting a mainframe application to Unix.

So that's OK then; COBOL is safe. Sigh of relief and round of applause for 
Tesco.


> http://www.computerworlduk.com/management/it-business/it-department/news/index.cfm?newsid=2191
>
So, Tesco are moving their supply chain software to Unix. They have an 
application into which they have made considerable investment and it does 
what they want (for now, at least...)  Generally, Unix does not run .NET.

> 4. From your perspective, I guess the IT Department at Tesco must have
> got it all wrong ?

Not at all. If what they are doing works, good luck to 'em. Have they been 
advertising recently for COBOL progammers? Your sources make much of Micro 
Focus "modernisation expertise"... (I'm wondering exactly what that 
entails... does it mean: "We've done a few COBOL migrations and are getting 
pretty good at it..." ?)

I have never at any time questioned the expertise or efficacy of Micro Focus 
products and personnel. However, despite Stephen Kelly's titanic struggle to 
re-kindle the embers of COBOL, I don't believe the company will be using 
COBOL as it's primary product in 10 years time. If it still exists at all. 
It already has a history of takeovers. There is certainly money to be made 
in moving people off mainframes or facilitating network acess to mainframe 
data, but that will not be providing jobs for COBOL programmers.

My question was about the need for a .NET COBOL compiler.  Nothing you have 
posted addresses that. I repeat: Unix, generally, does not run .NET.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-09-07T18:11:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net>`

```
>
> My question was about the need for a .NET COBOL compiler.  Nothing you have
…[3 more quoted lines elided]…
>

Inter-operability Pete. Cobol uses it to inter-operate with
'other' .NET languages and of course code-managed cloud computing
technologies. Eventually they (MF) could not abadon any technology
that is lying around. Every IT terminology (SaaS, .NET, cloud
computing) should be looked into by whom? Apparently by all software
companies. No man is an island... and it is advantageous to all.

What can I see here is the maintenance cost. It's all about cost is
it? So sometimes other people think the other product is better than
what is at hand. But hey, it is a free world. Anybody chooses what is
best for their interest.

It reminds me of what my University thought me... we're graduating
then when my instructor told us that what we are heading is NOT for
getting ourselves riches of the world, it is that we are going out of
school to reach out for others and 'inter-operate' within the
community. It's not "go out there and be better than other and be
rich!!" but working every single day for a common good.

I hope it is similar out there in the playing field (for IT
companies).
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-08T16:25:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gm4mkF2q04rhU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com>`

```
Rene_Surop wrote:
>> My question was about the need for a .NET COBOL compiler. Nothing
>> you have posted addresses that. I repeat: Unix, generally, does not
…[7 more quoted lines elided]…
> technologies.

I'm all in favour of interoperability. So is .NET. That's why they have a 
special class that can wrap stuff and make it work in the .NET environment; 
it's called InterOP services.

You can run your existing applications (COBOL, VB, other native code 
applications) in .NET as unmanaged code (it is actually more efficieint than 
managed CLR code), simply by wrapping them as InterOP services.

Certainly, it helps if they are OO, and it helps even more if they are COM 
objects, but you DON'T need a .NET COBOL compiler to run COBOL in .NET.

Robert Wagner and I spent a couple of weeks showing how this can be done 
easily. A full explanation and full source code is downloadable from 
cobol21.

People are simply buying these compilers without any clear idea of what to 
do with them or whether they need them. Usually because it is being promoted 
to them by vendors. "You need our tools but they won't run without .NET 
COBOL, so you need that too..."

If you are committed to COBOL for the long haul (and that is a very risky 
committment for any company to make nowadays) THEN you might find a use for 
a .NET COBOL compiler.

What happens instead is that people start writing .NET COBOL, find what an 
amazing environment it is, and want to do more, more quickly. Eventually, as 
the concepts start to gel, they realize that COBOL is not ideal for this 
environment and they change. In particular, data access technology is far 
advanced "outside" of COBOL. Once you start realizing the power of LINQ and 
Lambdas you don't want to be tied back to ESQL because that's what COBOL 
needs.

It's like a cuddle blanket that people are afraid to let go of.

Learn a .NET language and let COBOL go.


> Eventually they (MF) could not abadon any technology
> that is lying around. Every IT terminology (SaaS, .NET, cloud
…[6 more quoted lines elided]…
> best for their interest.

No, they don't. If that were actually the case, I wouldn't be writing here. 
They are being told to buy what is in the interest of the vendor, not their 
own interest.  You can argue that if they can't make an informed choice then 
they deserve to be shafted, but that is kind of an unfriendly approach.

New technology is confusing for everybody at first. People need unbiased 
information and explanation. In the last 6 months I have responded to dozens 
of requests for information (WITHOUT trying to sell my own products; in 
fact, PRIMA supports and helps people doing data and code migrations, 
whether they use our toolset or they don't...), and it was these requests 
that prompted me to set up the cobol21 web site in the first place. Most 
COBOL people are unfamiliar with the concepts of objects and layers and why 
these things are important. Today I have referral sites who are absolutely 
thrilled with the help and support they received (much of it without ever 
being charged), and they are good ambassadors who spread the word to others.

I see a real need to leverage the investment in COBOL into a modern 
environment. (Whether there are trillions of lines in existence, or only 
billions, nobody can deny there is still a lot of it about. It simply 
doesn't make sense to throw it all away and start from scratch. (At least, 
it doesn't always make sense; there are times when that is probably the best 
option.))   Something needs to be done about it.

I have looked at, and thought about at length, the pros and cons of 
different approaches for doing this. I am a small business with a large 
investment in COBOL who was treated shabbily because of that. The perception 
seemed to be: "You're a COBOL shop; we sell COBOL. You're not going 
anywhere, and you're not a big business, so just shut up while we shaft you, 
with stupid licenses, inflated prices for products and "maintenance", shabby 
"support", and an attitude that says; "we don't really want your business, 
but if you beg us to, we might sell you something.""

I determined to get out from under. Along the way, I wrote hundreds of 
thousands of lines of code, generated millions of lines more, and learned 
much about things that are not immediately obvious. Today PRIMA is fast 
becoming a centre of competence for things COBOL, and moving away from it. 
(I am finding more and more people without COBOL experience, but very 
computer competent in other areas, looking for assistance in moving someone 
else's COBOL... and I learn something from each one of them...)

Rene, if somebody is a COBOL shop and feels comfortable with that, and has 
no concern about the future or the viability of maintaining a huge codebase 
that NEEDS maintaining, then, maybe there is a place for a .NET COBOL 
compiler, for such a shop. They are probably wasting so much on IT it is 
just a drop in the ocean...

But for smaller businesses, where an expenditure of several thousand dollars 
needs to be questioned, (and that is the bulk of the market I am looking at) 
I cannot see this product being justified.

These are the people wanting to move to .NET and that means moving off 
COBOL.

Sooner or later, you're going to have to let COBOL go. The sooner you do it, 
the longer you have to get acquainted with the new environment, and the more 
financial reward you reap from cutting your "COBOL services" bill...

Migration costs are "one-off"; COBOL costs are ongoing...

When we had no option, COBOL costs were just a necessary part of doing 
business. Now there are options and you don't HAVE to incur COBOL costs. If 
I have a C# query I can get instantaneous 24 hour help from a community of 
around 60 million people... at NO charge. Those nice people at Microsoft 
will upgrade my IDE and compiler every couple of years, for NOTHING! (OK, if 
I want the whole nine yards I can pay a bit and get it... I did, and I 
wasn't sorry. VS 2008 alone is the best value software I have ever bought, 
never mind the C# compiler...


> It reminds me of what my University thought me... we're graduating
> then when my instructor told us that what we are heading is NOT for
…[4 more quoted lines elided]…
>
That sounds like a good school with a noble mind set. Unfortunately, not 
everybody went there...

> I hope it is similar out there in the playing field (for IT
> companies).

What are you actually finding?

Most of us are happy to help people if we can. (Mainly because most of us 
have had occasion to be thankful for the kindness of strangers at some point 
in our lives).

But we need to make a living too. It is much better if you can do so 
honestly. I've sometimes wondered about guys who sell completely worthless 
products (Sodastream, cigarettes, etc.)... Do they have trouble sleeping? 
Why not?... I know I would...

I guess that's why I never wrote a COBOL compiler for .NET... :-)

Pete
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-08T13:16:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h85lej$784$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com>`

```
In article <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com>,
Rene_Surop  <infodynamics_ph@yahoo.com> wrote:

[snip]

>It reminds me of what my University thought me... we're graduating
>then when my instructor told us that what we are heading is NOT for
…[6 more quoted lines elided]…
>companies).

Not from what I have seen... and, evidently, not from what others have 
seen, as well.  From 'Beyond Computing' Magazine, May, 1996, pg. 51, 
sidebar entitled 'Cultural Contradictions' (caps original):

--begin quoted text:

WE MUST WORK AS A TEAM.

But you get rewarded for standing out.

--end quoted text

(note that what constitutes 'rewarded' is not specified... it could be 
money, true, but it could also be training, a better parking-space or the 
ability to put one's skills to use in order to make Things Better all 
around)

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-09T03:13:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gnalkF2pq6b7U1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com> <h85lej$784$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com>,
…[30 more quoted lines elided]…
> around)

I worked in London and found parking to be an absolute nightmare.(In the end 
I used public transport and when Winter came and I found myself standing in 
snow on the platform at Rayner's Lane, waiting for a series of cancelled 
trains, I decided it was maybe time I left the U.K... Madrid was a lot more 
salubrious and I could walk to work... :-) Company spaces in London were 
more highly prized than annual salary increments. In fact one guy had his 
space taken for a new executive (who had negotiated a car park into his 
contract) and he quit over it...

On the other hand, in Dueselldorf, every single person who attended work had 
an allocated space, including the contractors.

Rewards and motivations can be widely varying as you noted, often depending 
on perceptions like status...

The whole business of how you reward people is a much more complex one than 
you might think.

I worked with an Egyptian contractor who worked day and night with me to 
rewrite an entire system to meet a deadline. He did it out of 
professionalism, pride and amazing loyalty because he knew I was on the line 
if it wasn't delivered, and I had shown him kindness in the past. I paid for 
his wife to come from Egypt for a holiday with him at the end of a previous 
phase of the contract, as a token of my appreciation for his very hard work. 
He repaid me many fold, when the chips were down.

One place I worked at on contract was so pleased with the work another 
contractor and myself did that they gave us a 2 week holiday anywhere on 
Earth... (We went to Thailand and spent a fortnight enjoying Pattaya...) 
Needless to say, when we came back, we worked many hours that were never 
billed, on the next phase of the contract... Another place I worked for paid 
for my London flat for 6 weeks while I went home for Xmas, on the 
understandng I would resume there in the New Year... Another company paid 
for my wife and I to have a weekend at a top hotel in Madrid, just because I 
gave them some free advice that saved them a large sum of money. I found all 
of these things to be highly motivating, partly because they were just not 
usual (most of us like to feel "special"), and partly because they showed 
imagination and were tax free... :-)

Now that I'm much older and value the quiet life, I find I am highly 
motivated by the need to feed and clothe myself :-) I want to be able to 
stay in NZ but I still can't quite afford to (without working). Writing 
software at home is an ideal solution (as long as it continues to generate 
revenue...)

These days when I work, at least I have a comfortable chair, can put my feet 
up, and never need to worry about a car park... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-08T15:47:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h85uaa$m5h$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com> <h85lej$784$1@reader1.panix.com> <7gnalkF2pq6b7U1@mid.individual.net>`

```
In article <7gnalkF2pq6b7U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article
…[30 more quoted lines elided]…
>> all around)

[snip]

>Rewards and motivations can be widely varying as you noted, often depending 
>on perceptions like status...
>
>The whole business of how you reward people is a much more complex one than 
>you might think.

If that second-person singular in the second sentence ('... you might 
think') has the same object as the second-person singular in the first 
sentence ('... as you noted') then - in as much as I can know what I 
think, of course - I'd have to respond with a measured, well-considered 
and yet still hearty 'Nope!'

I've noticed that those human-being type people can get surprisingly 
complex; it stands to reason that motivating them can, as well, get 
surprisingly complex.  A few decades back I read Sun T'zu's 'The Art of 
War' and I recall one of the commentators saying that different people 
needed to be motivated by different things... the lazy are motivated by 
the opportunity of doing Some Work so that they won't have to do More 
Work, the greedy are motivated by the possibility of gain, the intelligent 
are motivated by being the ability to demonstrate their worth to others 
and the General is motivated by the chance to sweep his army to victory.

I summed it up a while back by a simple 'Find the WIIFM gene - the one 
that responds to 'What's In It For Me?' and scratch it.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-08T11:22:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vi4da5p6sgp69rrj2vh0lq9ncms25e3rn9@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com> <h85lej$784$1@reader1.panix.com> <7gnalkF2pq6b7U1@mid.individual.net> <h85uaa$m5h$1@reader1.panix.com>`

```
On Tue, 8 Sep 2009 15:47:22 +0000 (UTC), docdwarf@panix.com () wrote:

>I've noticed that those human-being type people can get surprisingly 
>complex; it stands to reason that motivating them can, as well, get 
…[6 more quoted lines elided]…
>and the General is motivated by the chance to sweep his army to victory.

And sometimes a person is primarily lazy or greedy or intelligent, or
a General...    But more often our characteristics are more complex
and conditional.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-08T11:18:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j74da5t6um4smg73kd377gr0voqrelulob@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <33b104be-e894-434e-a30d-ac30cccfc92a@12g2000pri.googlegroups.com> <h85lej$784$1@reader1.panix.com>`

```
On Tue, 8 Sep 2009 13:16:03 +0000 (UTC), docdwarf@panix.com () wrote:

>--begin quoted text:
>
…[9 more quoted lines elided]…
>around)

Of course, different ways of standing out provide different "rewards".

It's a lifetime process adjusting back and forth between conforming
and not.   Teens have an especially hard time with it (being different
by being the same).    We have a long history of punishing people for
being different - but reward those who stand out "the right way".
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-09T10:01:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h88e1a1q29@news5.newsguy.com>`
- **In-Reply-To:** `<7ggea4F2pgfcjU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> I have never at any time questioned the expertise or efficacy of Micro Focus 
…[3 more quoted lines elided]…
> It already has a history of takeovers.

Micro Focus has never been taken over.

After Micro Focus acquired INTERSOLV (not the other way around), the
merged company was renamed MERANT. Some time later, the business unit
that owned most of the pre-merger Micro Focus assets was purchased
from MERANT and reestablished as an independent company.

The remains of MERANT were later acquired by Serena. MERANT was taken
over, but Micro Focus never was.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-10T03:54:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gq1d6F2qpkf8U1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <h88e1a1q29@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[15 more quoted lines elided]…
> over, but Micro Focus never was.

My point was that there has been a fairly unstable history at Micro Focus.

I remember the large redundancies and knew some of the people. I was also 
(indirectly) one of the victims of the Visoc fiasco (that was what caused me 
to move to Fujitsu; prior to that I had been uing Micro Focus and was 
perfectly satisfied.)

Nevertheless, I stand corrected on your point Michael. Thank you for the 
clarification.

And, like Fujitsu, I believe the MicroFocus product quality is excellent.

Having said all of that, I still don't see a long term future in COBOL for 
Micro Focus, or anyone else. (with the possible exception of IBM... their 
preference will be to drop it, but their user base will make it hard for 
them to do so.  Again, that will be a derivative of what was once the 
"mainframe market", until such time as it fades away through attrition of 
hardware and personnel.

I imagine that Micro Focus will either be absorbed by a larger competitor, 
or they will carve out a niche market in "modernisation" as Jimmy mentioned 
recently.

I'll be surprised if that future involves .NET; I see more Java and Unix...

Time as always will reveal all... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-10T09:38:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8b0u8018hg@news3.newsguy.com>`
- **In-Reply-To:** `<7gq1d6F2qpkf8U1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <h88e1a1q29@news5.newsguy.com> <7gq1d6F2qpkf8U1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[8 more quoted lines elided]…
> My point was that there has been a fairly unstable history at Micro Focus.

That's a subjective evaluation. There are only a handful of software
firms that, like Micro Focus, have existed for over 30 years, so it's
difficult to determine what would constitute a "stable" history for
that duration in this industry.

> Having said all of that, I still don't see a long term future in COBOL for 
> Micro Focus, or anyone else.

Understood. And I sympathize with your argument that there are better
ways to develop software - though even the best languages in
widespread mainstream use are still woefully behind the state of the
art in academia.

I just don't think most large organizations have the resources to
discard their legacy software assets.

> I imagine that Micro Focus will either be absorbed by a larger competitor, 
> or they will carve out a niche market in "modernisation" as Jimmy mentioned 
> recently.

It's a comfy niche.

> I'll be surprised if that future involves .NET; I see more Java and Unix...

You could be right, but for this race I'm putting my money on
Microsoft. (It's only fair, since they gave me that money in the first
place...) Not that I think our Java and Unix markets will go away - I
think .Net will come alongside them as a significant market.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** invalid@domain.invalid
- **Date:** 2009-09-10T14:31:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrnhai3ef.s9n.invalid@invalid.org>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <h88e1a1q29@news5.newsguy.com> <7gq1d6F2qpkf8U1@mid.individual.net> <h8b0u8018hg@news3.newsguy.com>`

```
On 2009-09-10, Michael Wojcik <mwojcik@newsguy.com> wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
>>> Pete Dashwood wrote:

>> Having said all of that, I still don't see a long term future in COBOL
>> for Micro Focus, or anyone else. 

How long is long? It's the 2nd oldest HLL in common use and it doesn't show
any signs of going away. I just came off a project recently at a large bank
where they implemented a new system in COBOL. In traditional applications
COBOL is still far and away the best choice and doesn't have any contenders.

> Understood. And I sympathize with your argument that there are better
> ways to develop software - though even the best languages in
> widespread mainstream use are still woefully behind the state of the
> art in academia.

And so? Academia has always been out of touch with practical software
engineering and large systems. People like Wirth and Dijkstra have done more
damage to programming than any other two people I can think of. The vast
majority of coders I run in to have no idea of what kind of load module gets
generated as a result of their horrific coding practices. Stroustrup bless
his heart is about the only "academic" I've ever seen with his head on his
shoulders.

> I just don't think most large organizations have the resources to
> discard their legacy software assets.

Nor should they. Business isn't about legacy or doing something new but
about what works. Let them concentrate on their business and leave the
technical decisions to qualified people- if they can find any.

>> I'll be surprised if that future involves .NET; I see more Java and
>>Unix...

Java is a more natural fit with MVS COBOL. Write the GUI in Java and let
COBOL handle transaction processing. UNIX? They're not anywhere near the
level of reliability and performance of an MVS box and there's no movement
in that direction.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-12T15:05:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8grfr22fer@news2.newsguy.com>`
- **In-Reply-To:** `<slrnhai3ef.s9n.invalid@invalid.org>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad> <7ggea4F2pgfcjU1@mid.individual.net> <h88e1a1q29@news5.newsguy.com> <7gq1d6F2qpkf8U1@mid.individual.net> <h8b0u8018hg@news3.newsguy.com> <slrnhai3ef.s9n.invalid@invalid.org>`

```
invalid@domain.invalid wrote:
> On 2009-09-10, Michael Wojcik <mwojcik@newsguy.com> wrote:
> 
…[6 more quoted lines elided]…
> engineering and large systems.

Practical software engineering and large systems have always been out
of touch with academia. Practitioners who disdain academic research
frequently have no idea whatsoever what that research consists of, or
how extensively it contributed to what they do on a daily basis.

> People like Wirth and Dijkstra have done more
> damage to programming than any other two people I can think of.

That's a ridiculous assertion. Care to back it up?

(Of course, this is the sort of argument one expects from an anonymous
poster.)
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2009-09-06T09:27:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f10dc020-1345-4bd1-b07a-df0f8e78aafe@y21g2000yqn.googlegroups.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <FiBom.161394$0e4.43780@newsfe19.iad>`

```
On Sep 5, 6:04 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Our Resident Expert wrote :
>
…[70 more quoted lines elided]…
> - Show quoted text -

You forgot to mention that one pound in every 8 spent in the UK is
spent in Tesco.
```

##### ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-09-05T17:14:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net>`

```
Pete,
  I don't know the "motivation" for various compiler vendors, but there is a 
fact that you seem to miss (or not include in your thoughts), BOTH "major" 
vendors how now offer ".NET COBOLs" (managed code version) introduced "OO COBOL 
versions" *many* years before they offered .NET versions.

For Windows (and to a lesser extent Unix/Linux) "OO COBOL compilers have been 
available for over a decade now.  To the best of my knowledge, all Windows OO 
COBOL compilers "interact" (easily) with Java, C++, C#, and/or Visual Basic 
(methods and classes).

There are certainly reasons why neither "OO COBOL" nor ".NET COBOLs" have 
"caught on" and I would certainly raise questions to any customers/user who was 
"just now" planning a migration to them.  On the other hand, having "timely 
tools" (compilers and application building tools) does not (to me) seem to be 
the reason.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-06T12:51:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ggfc6F2phkjoU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com>`

```
William M. Klein wrote:
> Pete,
>  I don't know the "motivation" for various compiler vendors, but
…[3 more quoted lines elided]…
> offered .NET versions.

Bill, I don't miss that; I said as much in my post. I have been using OO 
COBOL ever since it became widely avialable and i have been very thankful 
for it. If I hadn't learned about objects and layers the migration of my own 
COBOL investment would have been much more painful and expensive than it 
was. I'm not sure what your point is here. The fact that OO COBOL is 
available and can be wrapped to run in .NET, is one plank in my argument 
against .NET COBOL. I can;t see the need for it and I can't understand why 
anyone would pay considerable sums of money to develop for .NET when there 
are really good FREE tools to do it with. That's the nub of my argument.
>
> For Windows (and to a lesser extent Unix/Linux) "OO COBOL compilers
> have been available for over a decade now.  To the best of my
> knowledge, all Windows OO COBOL compilers "interact" (easily) with
> Java, C++, C#, and/or Visual Basic (methods and classes).

Precisely. So why COBOL for .NET?

>
> There are certainly reasons why neither "OO COBOL" nor ".NET COBOLs"
…[3 more quoted lines elided]…
> building tools) does not (to me) seem to be the reason.

Some time ago I was quite staggered by the number of hits the cobol21 site 
is taking on using embedded SQL in COBOL. I had assumed that everybody was 
familiar with this and posted the stuff there just as a matter of record and 
on the off chance some hobbyist might be interested. It has taken hundreds 
of hits... the point is that NOT "everyone" is up with the state of the 
play. (To me, embedded SQL is already obsolete, but that is certainly not 
the case for many people. I was swearing yesterday at SQL Server for some of 
the primitive ways it does stuff, then I realised, that it is actually 
pretty good as far as implementing SQL goes. In 10 years time people will be 
leaving ESQL and coming to Lambdas and LINQ (or equivalent) and you'll be 
reminding me that these facilities were available years ago :-))

I am helping people to migrate into an OO world after decades in COBOL. I 
see nothing wrong with them doing this "just now" (or any time...) and 
neither do they. I'd be interested to see some of the questions you might 
raise to such a person, and even more interested in providing answers to 
them.

Cheers,

Pete.

>
>> rick.malek@microfocus.com wrote:
…[138 more quoted lines elided]…
>> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-08T09:07:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net>`

```
On Sun, 6 Sep 2009 12:51:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Bill, I don't miss that; I said as much in my post. I have been using OO 
>COBOL ever since it became widely avialable and i have been very thankful 
…[6 more quoted lines elided]…
>are really good FREE tools to do it with. That's the nub of my argument.

Especially since the market doesn't seem to be there to buy even OO
COBOL, much less .NET COBOL when there are cheaper alternatives
available for new development.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-09T21:17:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gpa5oF2os8igU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net> <9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com>`

```
Howard Brazee wrote:
> On Sun, 6 Sep 2009 12:51:24 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> available for new development.

Absolutely, Howard.

However, most of the people I'm helping migrate, already have an OO COBOL 
compiler, usually Micro Focus or Fujitsu. My point is that if you already 
have a compiler that can generate code to run your legacy in .NET, then it 
is just senseless to spend more money on another one that allows you to 
generate managed code. If you NEED managed code (and if you commit to the 
.NET platform it makes sense to create new applications as managed code) you 
can generate it for free...

BUT, both managed and unmanaged code can interact and run in the 
environment, so legacy is really not a problem.

The advantages to running managed (as opposed to unmanaged) code are so 
minimal it doesn't justify it. If you have had a legacy application running 
for years without abending due to storage violations, it is probably safe to 
run it as unmanaged code.

I fail to be persuaded by the argument for .NET COBOL.

It's like arguing that a paddle steamer is better for bringing people to the 
new world than a cruise liner... Sure, the paddle steamer will get there but 
it will take longer and the fare is many times the fare on the cruise liner 
(did I mention that the cruise liner is FREE! You might need a few bucks for 
drinks and entertainment, but there aren't any drinks or entertainment when 
you go with the paddle steamer, and you may end up burning the fixtures and 
fittings to make the last leg into harbour...)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-09T10:10:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h88e1b2q29@news5.newsguy.com>`
- **In-Reply-To:** `<9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net> <9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com>`

```
Howard Brazee wrote:
> 
> Especially since the market doesn't seem to be there to buy even OO
> COBOL, much less .NET COBOL when there are cheaper alternatives
> available for new development.

We're selling both native-mode OO COBOL and .Net COBOL, and people are
building applications with them.

It's true the markets for both products are currently significantly
smaller than the market for traditional, procedural, native-mode
COBOL. But they exist, and they're a significant revenue stream.

Mainframe emulation for .Net COBOL is a much bigger market, judging by
the interest we're already seeing from prospective customers.
Microsoft thinks it's a big market, too; and while Microsoft often
gets these things wrong, it has a good long-term average.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-09T08:56:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<82gfa5571csmiueb0re8j7pu5aa4r5ndl7@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net> <9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com> <h88e1b2q29@news5.newsguy.com>`

```
On Wed, 09 Sep 2009 10:10:24 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>Mainframe emulation for .Net COBOL is a much bigger market, judging by
>the interest we're already seeing from prospective customers.
>Microsoft thinks it's a big market, too; and while Microsoft often
>gets these things wrong, it has a good long-term average.

Interesting.   Is this all mainframes, or just IBM?     (Microsoft has
been trying to get into that market for a while without much success)

How do you see mainframe computers using .Net COBOL?

I see IBM mainframe computers typically used in one of these
environments:
1.   Run batch programs using CoBOL (or another old language).
2.   Run on-line programs using either CoBOL and CICS or something
like ADS/O (IDMS).
3.   Running a database which is accessed via SQL and SQL based tools
on other computers.

I don't see individual sites changing too much unless they are buying
a package that was designed with a different paradigm.   I would be
quite pleased if I was missing something here.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-10T10:02:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8b0ua118hg@news3.newsguy.com>`
- **In-Reply-To:** `<82gfa5571csmiueb0re8j7pu5aa4r5ndl7@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net> <9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com> <h88e1b2q29@news5.newsguy.com> <82gfa5571csmiueb0re8j7pu5aa4r5ndl7@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 09 Sep 2009 10:10:24 -0400, Michael Wojcik
> <mwojcik@newsguy.com> wrote:
…[6 more quoted lines elided]…
> Interesting.   Is this all mainframes, or just IBM?

I was referring to IBM zOS systems, running batch, CICS, and IMS. We
have partners who provide emulation for some other mainframe
platforms, such as Unisys A-series.

> (Microsoft has
> been trying to get into that market for a while without much success)

I'm not sure what you're thinking of. Microsoft has certainly sold a
goodly number of Windows licenses (and SQL Server, etc) for
native-mode mainframe migrations. There are case studies on the Micro
Focus website.

Microsoft themselves don't currently have a mainframe emulation
solution for .Net. There's the Alchemy (formerly Fujitsu) product set,
NetCOBOL plus NeoKicks, which transforms mainframe COBOL application
source to run under .Net; and Microsoft is happy to sell Windows
licenses for Alchemy migrations. But there isn't any product currently
on the market, from Microsoft or anyone else, that emulates zOS batch
or CICS on .Net.

> How do you see mainframe computers using .Net COBOL?

I don't. I see mainframe COBOL applications migrated to .Net. The
process works like this:

1. Download COBOL application source.
2. Compile with the managed-code generation option.
3. Configure mainframe emulation regions and resources (CICS PCTs, etc).
4. Run.

5. (Optional) Extend, enhance, refactor, and/or update applications by
integrating with and/or rewriting using .Net COBOL features, other
.Net languages, .Net framework facilities, etc.

> I see IBM mainframe computers typically used in one of these
> environments:
…[4 more quoted lines elided]…
> on other computers.

Yes, though 1 and 2 often include 3 - those aren't orthogonal.

Those are the sorts of applications our customers migrate off IBM
mainframes onto Windows and Unix.

> I don't see individual sites changing too much unless they are buying
> a package that was designed with a different paradigm.

I do. I see customers moving applications off mainframes into our
current emulation environments (MFE EE for development, ES/MSS for
development and production) every day. There are large cost savings
for a relatively small investment, and CIOs like to save money.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-10T04:01:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gq1puF2pbubjU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <2pBom.632077$op1.339822@en-nntp-05.dc1.easynews.com> <7ggfc6F2phkjoU1@mid.individual.net> <9msca5t67g4r10c590kvunljo55kfjjlv5@4ax.com> <h88e1b2q29@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Howard Brazee wrote:
>>
…[14 more quoted lines elided]…
> gets these things wrong, it has a good long-term average.

Yes, that would be my feeling too. It is mainframe technology that is 
keeping COBOL alive, but there is still a swell of desire to get off it. As 
the network becomes more robust and powerful it is eroding the traditional 
mainframe role of "heavy duty processing".

 I didn't think the mainframe people would be opting for .NET and am 
surprised by that. (Generally, it is a good choice...).

Pete.
```

##### ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2009-09-06T00:36:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4aa30403$0$27575$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net>`

```
Pete Dashwood wrote:

> You don't have to hobble around like Jake the
> Peg with his extra leg (Object Orientation bolted onto COBOL), 

 ROFLOL (or should that be ROLF-OL?)
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-06T13:14:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gggoaF2pd0dpU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <4aa30403$0$27575$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`

```
Paul Richards wrote:
> Pete Dashwood wrote:
>
…[3 more quoted lines elided]…
> ROFLOL (or should that be ROLF-OL?)

Good one Paul! (It made me chuckle... and I like the actual wit in it.. 
:-)). Bless him, he's a National treasure... :-)

Pete.
```

##### ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-09T09:56:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h88e1a0q29@news5.newsguy.com>`
- **In-Reply-To:** `<7gfp1jF2pfqolU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> Can anyone explain to me what the point of COBOL.NET is?

Well, we can try.

There's an enormous codebase of running COBOL applications. Many of
the people who control those applications are interested in migrating
them to new platforms. They don't have the huge resources
(particularly time) required to rewrite those applications in another
language.

COBOL.NET gives those people the option of migrating those
applications to .Net. For a lot of them, that's attractive, judging by
the tremendous interest we're seeing.

And once those applications are migrated, it's easy to gradually
replace them with more modern, OO code, using OO COBOL or any other
.Net language.

If you have a huge codebase of COBOL CICS apps, say, and you migrate
them to .Net, it's trivial to front-end them with WPF. It's trivial to
expose them as WCF services, or have them invoke WCF client proxies.
It's trivial to have .Net code in other languages instantiate and
invoke them.

It's even trivial to mix .Net OO code into those CICS apps as you
maintain them. The other day I needed a quick & dirty CICS app that'd
show the name of the machine it was running on. In .Net COBOL with
CICS support, it was as simple as taking a skeleton CICS app and
adding a few .Net invokes:

-----
      * Show name of host where this program is run
      $set ilusing "System"
      $set ilusing "System.Text"

       identification division.
       program-id. showhost.

       data division.
       working-storage section.
       77  ws-netbios-name                   string.
       77  ws-decoder                        type "ASCIIEncoding".
       77  ws-byte                           binary-char unsigned.

       01  ws-nbn-buf                        pic x(40) value spaces.
       01  ws-nbn-bytes                      binary-char unsigned
                                             occurs 40
                                             redefines ws-nbn-buf.

       77  ws-buf-pos                        pic x(4) comp-5.
       77  ws-output                         pic x(80).
       77  ws-blank                          pic x value space.

       procedure division.

      * Get the NetBIOS machine name
           set ws-netbios-name to type "Environment"::"MachineName"

      * Convert to ASCII
           set ws-decoder to new "ASCIIEncoding"
           move 1 to ws-buf-pos
           perform varying ws-byte through
                           ws-decoder::"GetBytes"(ws-netbios-name)
               move ws-byte to ws-nbn-bytes(ws-buf-pos)
               add 1 to ws-buf-pos
           end-perform

      * Display it
           string
               " NetBIOS machine name: " delimited size
               ws-nbn-buf delimited space
               into ws-output
           end-string
           exec cics send text
               from(ws-output)
               freekb
           end-exec

      * Done
           exec cics return end-exec
           stop run.
-----

Now there are certainly some infelicities there, particularly the
hoops in getting the ASCII encoding of the name into a pic x(n) buffer
in order to display it with exec cics send text. That's a limitation
of CICS and TN3270, though, not of COBOL .Net per se.

The important thing is that I can take an existing CICS program, and
do all the OO stuff with it: invoke static methods (like
Environment::MachineName), instantiate objects and invoke methods on
them (like ASCIIEncoder::GetBytes), iterate through containers
(perform varying through), etc. I didn't need to do anything more in
this trivial program, but I can wrap CICS apps as objects. I can wrap
them as delegate methods. I can invoke them as event handlers.

None of that requires recapturing the business logic (and all the risk
that involves) so I can reimplement it in another language. Which
would be a project that, even if it's completely successful, gets me
no further than I was before; at the end I have exactly the same
applications.

> It allows people to perpetuate the travesties of procedural code into a 
> modern OO environment.

So does any other .Net language. I can write horrible procedural code
in VB.Net, C#, F# - you name it.

> The code I've seen in it is verbose compared to C#, 
> (or even VB.NET), it doesn't buy me anything (apart from an expensive 
> compiler, when the .NET languages are free...), I just don't get it.

No, it doesn't buy *you* anything. But it's worth a lot to a lot of
other people - people who have a huge investment in COBOL and lack the
resources to discard all of it and start from scratch.

> (Fujitsu NetCOBOL runs extremely well as native code under InterOp services. 

For many people, running unmanaged code isn't satisfactory. If they're
moving to .Net, they're going to move to managed code.

> My advice:  Spend your money on training and upskilling, not on pointless 
> compilers and non-visible maintenance for them .

We have plenty of customers with thousands of COBOL applications,
containing millions of lines of source. There are no independent
specifications of what those programs do. They embody business rules,
data formats, and other information that's critical to the daily
functioning of the enterprise. The effort just to analyze all of that
so it could be replicated precisely by a completely new implementation
in some other language would be hugely costly - far more than the
organization can justify.

That's not a training issue. No amount of training can reduce the
effort required to distill critical information from that large a
codebase to something practical.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-10T04:14:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gq2jdF2ohsbvU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[9 more quoted lines elided]…
>

They don't need to rewrite their legacy in a different language to run it on 
.NET. All they have to do is wrap it. BUT, they are bing TOLD that they have 
to recompile for .NET.

It simply isn't true.

Most of them are not familiar enough with the details of the environment to 
know about the services available in it, so they are guided by the vendors 
(well, actually the vendors Sales reps...) who are certainly not going to 
tell them they don't need a product that pays good commisision and ensures 
an ongoing revenue stream for maintenance, support, and upgrades.

I have encountered several instances of this; it is not just an isolated 
thing.

> COBOL.NET gives those people the option of migrating those
> applications to .Net. For a lot of them, that's attractive, judging by
> the tremendous interest we're seeing.

No argument. I'm seeing it too. The difference is I try to keep their costs 
as low as possible and don't let them buy things they don't need (not even 
my own products...)
>
> And once those applications are migrated, it's easy to gradually
> replace them with more modern, OO code, using OO COBOL or any other
> .Net language.

Yep. Completely agree. The only thing I take issue with is your statement 
that migration is predicated on a .NET COBOL compiler. It isn't.
I already have a number of sites who are NOT using .NET COBOL but ARE 
migrating to .NET.

>
> If you have a huge codebase of COBOL CICS apps, say, and you migrate
…[117 more quoted lines elided]…
> codebase to something practical.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-10T05:52:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gq8aiF2qjbmcU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net>`

```
Sorry, some finger trouble meant my response was prematurely posted...:-)

Completion is made below...


Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[109 more quoted lines elided]…
>> -----

>>
>> Now there are certainly some infelicities there, particularly the
…[11 more quoted lines elided]…
>>

Yes, I can see there is a use as far as CICS goes.

>> None of that requires recapturing the business logic (and all the
>> risk that involves) so I can reimplement it in another language.
>> Which would be a project that, even if it's completely successful,
>> gets me no further than I was before; at the end I have exactly the
>> same applications.

I am not advocating rewriting legacy in another language.
>>
>>> It allows people to perpetuate the travesties of procedural code
…[4 more quoted lines elided]…
>>

You could, but you would be less likely to...


>>> The code I've seen in it is verbose compared to C#,
>>> (or even VB.NET), it doesn't buy me anything (apart from an
…[5 more quoted lines elided]…
>> the resources to discard all of it and start from scratch.

Without wishing to sound petulant, I've been saying that for some time.

The last time was 2 days ago in this thread...

I had a pretty hefty investment in COBOL myself when I first decided to move 
off it. Certainly, rewriting from scratch was not an option, and it hasn't 
been for the people using my tools to migrate their COBOL. Howard made the 
point that some Management will want to restart and I think he's probably 
right, but for most people even salvaging 50% makes the whole exercise 
worthwhile. (On my own stuff I salvaged over 90% and on other people's we 
expect no less than 80%. The refactoring is still a manual process although 
standard procedures for doing it are evolving and we have learned what NOT 
to do :-) I still plan to automate some or all of it as soon as I can 
possibly get time.
>>
>>> (Fujitsu NetCOBOL runs extremely well as native code under InterOp
…[3 more quoted lines elided]…
>> they're moving to .Net, they're going to move to managed code.

Certainly, in the long run. But running legacy during transition under 
InterOP services is no problem. And even doing it for several years (given 
stable code that has been stable for years) is not a problem either.

>>
>>> My advice:  Spend your money on training and upskilling, not on
…[9 more quoted lines elided]…
>> more than the organization can justify.

I know. I'm not advocating that.
>>
>> That's not a training issue. No amount of training can reduce the
>> effort required to distill critical information from that large a
>> codebase to something practical.

That is an argument that Howard might be interested in. He could also argue 
that that is a very good reason to get rid of it and start over using modern 
practices and approaches. It cuts both ways... Instead of trying to analyse 
what your legacy code does, you could be analysing what your people are 
doing and how you can help them do it better.

After reading this response, I think your most powerful argument is in the 
CICS arena. The precompile of COBOL which translates the CICS commands is 
all nicely integrated. I could rewrite your sample code in many fewer lines 
using C#  (I'm pretty siure you could too :-)) but I can't (easily) 
integrate the CICS calls. So for people with CICS legacy there may be a case 
for using .NET COBOL, provided CICS calls are supported, as yours appear to 
be.

Personally, I'd be more interested in refactoring the code into objects and 
leave the presentation layer to the very last. I wouldn't need .NET COBOL to 
do that, but I accept that many people will be less concerned about 
converting their COBOL into objects and layers than I am. (Or "was"... it's 
all done now.)

The automated generation of objects for a Data Access Layer is proving 
popular and generating quite a bit of interest. Everybody likes the idea of 
an OO DAL coming out of Standard COBOL, and being generated by tools, but 
the same people are less concerned about their own code being converted to 
objects and layers... I guess it takes time :-) Most people can instantly 
see the advantages of separation between Business, Presentation, and Data 
layers, but it's a bit like: "Yeah, that'd be really cool, but we don't want 
to do any work..."   Hence my strong desire to get some or all of this 
automated as soon as I can. They see the data layer being 100% generated, 
with their existing applications modified to invoke the data objects instead 
of using COBOL indexed file access verbs, and that is all pretty trouble 
free and fully automated. They want the same ease of conversion for the 
Business and Presentation layers. That isn't there yet. As you noted, the 
Presentation layer is pretty easy. Most people are looking at going to the 
Web for it.

This being the case, I have been working with a tool which generates a web 
based interface for your database (Iron Speed) and I'm finding it a bit like 
the curate's egg... (good in parts...) To be fair, I am using a free version 
that doesn't do everything so I have to keep writing C# code-behinds to 
manually do stuff that would be a few mouse clicks in the Enterprise 
Edition. I have been very impressed with the speed of getting stuff done, 
especially basic table maintenance and it is a very slick web user 
interface.  I have alkways been suspicious of bound controls and this is the 
first time I have done any extensive work with them. I should have done it 
sooner... this is really good. There is an Arts magazine here that I write 
for regularly and they have asked me to take over the finances and manage 
the subscriptions etc. The existing system is totally paper based and things 
like a monthly Bank Reconciliation could take a full working day.I decided 
to build them an admin. system using Iron Speed. I expect to complete it 
next week which, considering what it does, is pretty impressive. There are 
around 30 web pages involved and it handles names and addresses, 
subscribers, receipts, payments, renewal notices, and a number of different 
Marketing options, plus a feed to MYOB for the actual accounting. I've 
cancelled the paper statements and moved to online Banking and I'll be 
writing the Bank Reconciliation program over the weekend :-)

What this exercise is bringing home to me is the power of modern tools and 
approaches. I can knock this out in a little over 12 days, without a single 
line of COBOL. It would have been a 6 month project back in the 60s. Where 
previously, things were locked onto a single spreadsheet on a single 
person's machine, now there is a true database with much richer information, 
that can be accessed by authorized people from all over NZ. A Poetry Editor 
in the South Island can communicate to the Production manager 600 miles away 
in Northland, which poems have been accepted, from whom, and payents are 
raised automatically for me to approve. The Fiction Editor can offload to 
the Prose Editor if there is a large number of stories so people can help 
each other, and the system updates related tables automatically. (It's 
actually a lot of fun... :-)) New subscribers can be processed by any of the 
committee members from their homes, instead of one person carrying the whole 
load because the spreadsheet happens to be on their computer...

Summing up, I believe there are more points of agreement than disagreement 
in our posts, Michael.

I could see people with CICS legacy deriving benefit from .NET COBOL, so 
thank you, that has answered my question. It isn't a totally worthless 
product and I have to withdraw that statement.

The people I'm dealing with, who are NOT mainframe sites, can't really get 
any benefit from it at all, however, and it is shabby, to say the least, 
when Sales people exploit the lack of knowledge that some of their prospects 
will necessarily have, about a new and unfamiliar environment.

I would expect people to be able to return the product and get a refund. 
Apparently, that is not an option...

Neither can a licence be traded for a different product.

I'm just glad I don't have these hassles any more...

Thanks for a thought provoking response, as usual, Michael.

Pete
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-09T13:19:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7lvfa5hui20uh6cp5i6sgebbgchaq6safj@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net>`

```
On Thu, 10 Sep 2009 05:52:17 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>>> That's not a training issue. No amount of training can reduce the
>>> effort required to distill critical information from that large a
…[6 more quoted lines elided]…
>doing and how you can help them do it better.

You're right - it cuts both ways.    I believe the solution picked
will more likely be based upon the bosses' career goals, than in the
enterprise's long term benefit.   Maybe not to the degree that
politicians do, but close.

>After reading this response, I think your most powerful argument is in the 
>CICS arena. The precompile of COBOL which translates the CICS commands is 
…[4 more quoted lines elided]…
>be.

I agree.   It's better than screen scraping for moving existing
applications off of terminal emulators and onto Web pages.

>Personally, I'd be more interested in refactoring the code into objects and 
>leave the presentation layer to the very last. I wouldn't need .NET COBOL to 
>do that, but I accept that many people will be less concerned about 
>converting their COBOL into objects and layers than I am. (Or "was"... it's 
>all done now.)

If it could be done in maintenance mode, it would be useful.   
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-09T13:20:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<000ga5pppu1lk7j9rq82a2tbbl7jcgpd1q@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <7lvfa5hui20uh6cp5i6sgebbgchaq6safj@4ax.com>`

```
On Wed, 09 Sep 2009 13:19:12 -0600, Howard Brazee <howard@brazee.net>
wrote:

>>After reading this response, I think your most powerful argument is in the 
>>CICS arena. The precompile of COBOL which translates the CICS commands is 
…[7 more quoted lines elided]…
>applications off of terminal emulators and onto Web pages.

The big selling point here might be to have the same applications -
but no CICS fee.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-10T13:30:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8av0r$1er$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net>`

```
In article <7gq8aiF2qjbmcU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Sorry, some finger trouble meant my response was prematurely posted...:-)
>
…[4 more quoted lines elided]…
>> Michael Wojcik wrote:

[snip - I hope I got the attributions right]

>>> That's not a training issue. No amount of training can reduce the
>>> effort required to distill critical information from that large a
…[6 more quoted lines elided]…
>doing and how you can help them do it better.

The more things change... I recall reading, a while back (only a few 
decades but pre-dating DB2 by a fair amount), a consultant's Letter to the 
Editor of some now-defunct computing magazine; he had been retained by an 
accounting-firm to 'computerise' their system.

In his mind this translated into studying the business processes and then 
combining/deleting/adding/changing functions so as to be able to take full 
advantage of the kind of stuff that computers can do with greater speed, 
ease, efficiency and accuracy than human beings.

The client's idea was a bit... different; the client wanted their current 
pencil/form/review/sign-off system reproduced, as precisely as possible, 
on a computer platform.  When it was pointed out that the new platform 
offered possibilities that could not be accomplished under the older 
methods and with less effort the Standard Reply was 'Our People are used 
to it this way'.

In other words... the client wanted a paper-and-pencil system duplicated 
on a computer.  To the consultant writing the letter (and possibly a few 
other folks, as well) This Makes Almost No Sense... except for theone bit 
of sense of 'it caused the person with the authority to sign checks for 
the system to smile'.

'... analyse what your people are doing'?  Leaving aside the antipathy 
generated by the Time-and-Motion Men encouraged by Frederick Winslow 
Taylor's theories of Scientific Management... what gets found out, at 
times, is that folks spend years coming to their desks, going through the 
sheets in their In-box one at a time, skimming them for obvious errors, 
putting some initials on the appropriate 'Reviewed By' line and putting 
the sheets over into the Out-box.

I have seen it happen that folks who suggest that things might be done 
otherwise get labelled as malcontents, troublemakers or (*gasp!*) Not Team 
Players and be transferred to the mail-room, the branch office in Outer 
Lithuania or 'rightsized' into the unemployment-line... but as I have said 
before, the nature of my work puts me into what I call 'sick shops'.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-10T07:57:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n41ia5h5lvrmf7kotj4t263c85mkoad9np@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8av0r$1er$1@reader1.panix.com>`

```
On Thu, 10 Sep 2009 13:30:03 +0000 (UTC), docdwarf@panix.com () wrote:

>In other words... the client wanted a paper-and-pencil system duplicated 
>on a computer.  To the consultant writing the letter (and possibly a few 
>other folks, as well) This Makes Almost No Sense... except for theone bit 
>of sense of 'it caused the person with the authority to sign checks for 
>the system to smile'.


The way around this was when the users went around the system.    The
big example of this was when managers discovered spreadsheets.   

Expectations also changed when people discovered how easy it was to
get data on their laptop computers at coffee houses near their
clients' sites.  

While this still isn't analyzing from scratch, at least the
expectations aren't quite for the same old reports, but for a report
that is deliverable on a spreadsheet remotely, in their desired
format.

I see lots of users accessing a company's data warehouse with report
generators that automatically download into spreadsheets (if that's
the desired format).    That kind of data retrieval doesn't use the
old business logic in the CoBOL programs unless we recreate that logic
in accessible queries.    But it does require new security and privacy
rules.

The decision makers aren't so interested in data entry - they are into
data retrieval and manipulation being done Their Way.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-10T14:21:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8b21k$8rf$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gq8aiF2qjbmcU1@mid.individual.net> <h8av0r$1er$1@reader1.panix.com> <n41ia5h5lvrmf7kotj4t263c85mkoad9np@4ax.com>`

```
In article <n41ia5h5lvrmf7kotj4t263c85mkoad9np@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 10 Sep 2009 13:30:03 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[8 more quoted lines elided]…
>big example of this was when managers discovered spreadsheets.   

Our memories are different, Mr Brazee... as I recall it the working 
accountants discovered spreadsheets and brought their own machines into 
the office - at times, against company policy - because the managers would 
not allocate budget for the equipment/software.

(that was also a while after the letter I wrote about was written, as 
well)

>
>Expectations also changed when people discovered how easy it was to
>get data on their laptop computers at coffee houses near their
>clients' sites.  

Once again, I find myself in 'sick shops'... but if a manager cannot count 
nostrils and recta nor can hear the clattering of a keyboard then 'work 
isn't getting done!' and some talking-to is needed.

>
>While this still isn't analyzing from scratch, at least the
>expectations aren't quite for the same old reports, but for a report
>that is deliverable on a spreadsheet remotely, in their desired
>format.

It may just be my tin ear, Mr Brazee... but it sounds like 'Change the 
wrapping-paper and the delivery-address but make sure the contents of the 
package are the same'.

>
>I see lots of users accessing a company's data warehouse with report
…[4 more quoted lines elided]…
>rules.

What... you mean that Social Security Number can no longer be used as the 
universal file key?  But... We've Always Done It That Way!

>The decision makers aren't so interested in data entry - they are into
>data retrieval and manipulation being done Their Way.

Different groups are interested in different things, Mr Brazee, and 
likewise their decision makers.  Data Entry groups are interested in data 
entry, Inventory Management groups are interested in inventory management, 
Routing/Delivery groups are interested in routing and delivery... and so 
on.  Have you ever heard the story about L L Bean's order-picking 
strategy?

The intricacies arise when the functions of the groups are at odds... 
getting large quantities of data into a database or file system is best 
accomplished with an architecture that is completely different from one 
which is good at retrieving and analysing historical data... and DASD 
costs money and networking it costs money and monitoring/optimising data 
costs money and people to code for new circumstances cost money and 
*anything* that costs money can result in less of a bonus for someone 
else.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-10T08:58:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t4ia5doak25vn2pjbmgjk8tp5rka00o76@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gq8aiF2qjbmcU1@mid.individual.net> <h8av0r$1er$1@reader1.panix.com> <n41ia5h5lvrmf7kotj4t263c85mkoad9np@4ax.com> <h8b21k$8rf$1@reader1.panix.com>`

```
On Thu, 10 Sep 2009 14:21:40 +0000 (UTC), docdwarf@panix.com () wrote:

>Different groups are interested in different things, Mr Brazee, and 
>likewise their decision makers.  Data Entry groups are interested in data 
>entry, Inventory Management groups are interested in inventory management, 
>Routing/Delivery groups are interested in routing and delivery... and so 
>on.  

While Data Entry groups are interested in keeping their jobs stable -
they don't write the checks.

>Have you ever heard the story about L L Bean's order-picking 
>strategy?

I'm not thinking of it - could you share it?
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-10T15:50:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8b78d$ltc$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <n41ia5h5lvrmf7kotj4t263c85mkoad9np@4ax.com> <h8b21k$8rf$1@reader1.panix.com> <7t4ia5doak25vn2pjbmgjk8tp5rka00o76@4ax.com>`

```
In article <7t4ia5doak25vn2pjbmgjk8tp5rka00o76@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 10 Sep 2009 14:21:40 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>they don't write the checks.

I have seen managers of Data Entry groups commission and pay for systems, 
Mr Brazee... just as I've seen the same for Inventory Management, 
Routing/Delivery and the like.

>
>>Have you ever heard the story about L L Bean's order-picking 
>>strategy?
>
>I'm not thinking of it - could you share it?

A wonderful bit of simplicity.  The DDP (Director of Data Processing... 
this was a while ago) of another company in a different line of business 
(ie, not in competeition with Bean's) was talking with the DDP of Beans 
and bemoaning the problems they had in translating orders - which arrived 
randomly - into pick-lists for the stock crew.  There was constant 
Managerial in-fighting about this, Manager A wanted things to be in 
alphabetical order (so items could be easily looked up on his particular 
list), Manager B wanted things in stock-number order for a similar reason, 
everyone wanted things Just His Own Way.

(intentional use of masculine form here... this was a while ago)

The DDP at Bean's mentioned that when they generated their pick-lists they 
didn't pay attention to what the various other Managers wanted.  They had 
the folks in Warehousing number their bins in geographic sequence (Row A, 
bins 001 - 999, Row B, 001 - 999, etc) and then the folks in DP created a 
pick-list with the bin-location number on it and as the primary sort.

Sure, the pick-list wasn't in alphabetical order, as Manager A liked to 
see things, or stock-number order, as per Manager B... *and* it required 
another set of lists to be printed up and That Costs MONEY!...

... but the increased speed and accuracy of picked orders more than made 
up for the costs incurred.

DP worked with the department involved (Warehousing) for its unique needs, 
incurred an extra cost in order to accomodate those needs... and yet Made 
Things Easier for people *and* Saved Money at the same time.  

That, I believe, is How Things Should Be Done... and I cannot count the 
times I have encountered resistance, hostility and the usual 'Well, it 
*might* make sense but, you know... Things Are Different Here' when I've 
seen similar suggestions offered.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-11T18:13:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8grdu02fer@news2.newsguy.com>`
- **In-Reply-To:** `<7gq8aiF2qjbmcU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net>`

```
Pete Dashwood wrote:
>>> That's not a training issue. No amount of training can reduce the
>>> effort required to distill critical information from that large a
…[6 more quoted lines elided]…
> doing and how you can help them do it better.

For some organizations, that's simply not practical.

We have a number of customers in the financial sector, for example,
who operate under very strict regulatory regimes. They have to produce
large, complex reports every day. The form and content of those
reports are dictated by a labyrinth of regulatory statutes and rules
issued by government agencies.

Today, they have large, complicated COBOL applications that produce
those reports. The reports they currently produce satisfy the regulators.

Replacing those programs would be a huge risk. Get a report wrong, or
fail to produce one, and the organization is facing investigation,
fines, and suspension of their business activities. That can kill a
business in short order; even if the costs don't do it outright, they
have a very touchy customer base with little loyalty. Even delaying
transactions a few minutes because of a hiccup in the reporting
mechanism could cost them customers.

The potential benefits - already nebulous - of rewriting those
applications are nowhere near large enough to even consider doing it.

It's true that many business applications primarily capture employee
workflow, and that many of them have a decent margin for error, which
can accommodate the inevitable glitches of a transition to a new code
base. But others capture specific, esoteric knowledge that's very
difficult to reliably reconstruct, and have very little tolerance for
failure.

> Personally, I'd be more interested in refactoring the code into objects and 
> leave the presentation layer to the very last. I wouldn't need .NET COBOL to 
> do that, but I accept that many people will be less concerned about 
> converting their COBOL into objects and layers than I am. (Or "was"... it's 
> all done now.)

You'd need .Net COBOL if you wanted managed code for those objects,
and you want to keep them COBOL. If you want to get rid of the COBOL
entirely - which is certainly an option - you'd need to replace CICS
with another transaction manager, as well as whatever other CICS
features you were using. All of that is doable, but it's usually not
simple.

Drag and drop migration, on the other hand, is simple. Our PDC demo
was IBM's ACCT CICS demo app from the mid-80s. We just compiled it as
managed code and ran it. No source changes at all. That's a powerful
value proposition for the CIO, because it means almost no new
development costs (just training developers to use Visual Studio,
basically, and how to deploy to the new environment). So there's very
little impact on the existing development schedule.

And it means that proof-of-concept demos using actual customer apps
can be done very quickly. That's also important to CIOs and
development managers, because it means they don't have to make a major
investment just to find out if the solution is usable.

Those aren't simply psychological factors; it's not selling the
product based solely on management's desire to stick with the known.
They're real costs.

> Summing up, I believe there are more points of agreement than disagreement 
> in our posts, Michael.

I'd say that's a fair assessment. Certainly, I'm not opposed to people
trying new approaches, and I believe in using an appropriate tool for
the job. I think I am just more pessimistic than you are about the
costs of moving away from a lot of legacy code. (And, of course, I
have a vested interest in that, which no doubt contributes to my
perception.)
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-13T13:04:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h2upeF2qtpgqU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>>> That's not a training issue. No amount of training can reduce the
…[47 more quoted lines elided]…
> and you want to keep them COBOL.

Just a quick comment on this, I take no issue with the rest of your post...

I have apps now that are legacy COBOL running under .NET They have been 
running that way for nearly 3 years and there has never been a problem with 
them. Certainly, I have rewritten some of them in C#, but that was driven by 
application requirement and my own desire to get out from under COBOL, not 
by problems running unmanaged code under InterOP services.

There is no need for legacy to be managed code and there is no need for a 
.NET COBOL compiler, at least in my environment, and the people I am working 
with are realizing the same. However, as we discussed earlier, these are not 
sites where CICS is being used.

Managed code is good and it gives people peace of mind, but desire for it 
stems more from paranoia than any real threat. If an application has run 
stably for years in your present environment, there is no reason for it not 
to in a .NET environment, whether it is managed or not.



> If you want to get rid of the COBOL
> entirely - which is certainly an option - you'd need to replace CICS
…[29 more quoted lines elided]…
> perception.)

My company charges a fraction of what yours does for doing that, so I don't 
see the costs as being a problem. :-)

Pete
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-16T12:16:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8r72e01d46@news2.newsguy.com>`
- **In-Reply-To:** `<7h2upeF2qtpgqU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <7h2upeF2qtpgqU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> There is no need for legacy to be managed code

Perhaps not for you. Other people do have that need.

> and there is no need for a
> .NET COBOL compiler, at least in my environment, and the people I am working 
> with are realizing the same.

There are other environments. Some of them do not permit unmanaged code.

> Managed code is good and it gives people peace of mind, but desire for it 
> stems more from paranoia than any real threat.

Other organizations have threat models which are different from yours.
To dismiss them as "paranoia" is insulting and short-sighted.

> If an application has run 
> stably for years in your present environment, there is no reason for it not 
> to in a .NET environment, whether it is managed or not.

There's can be vast differences between running as native code on a
mainframe and running as native code on a Windows server. There are
plenty of reasons why an application which is safe (in terms of the
threat model) in the former is not safe in the latter.

Different organizations have different requirements. Some of them
cannot be wished away.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-14T10:56:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com>`

```
On Fri, 11 Sep 2009 18:13:56 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>Today, they have large, complicated COBOL applications that produce
>those reports. The reports they currently produce satisfy the regulators.

There are several reasons that so many companies have moved away from
hiring their own janitors.   Many of those reasons are on the order of
"it's hard to fire our employees", or "contractual obligations require
we spend so much on insurance".   So they contract out for janitorial
services.

I see the same thing happening for many types of regulatory reports,
collections processing, payroll, taxes, etc.     Contract out these
pieces that aren't really core business - but which are more
constrained by regulations than by particular business needs.   

And as with janitorial services - one isn't stuck with a particular
contractor.    The flexibility gained is worth the cost of giving
someone else a profit (within that other company's area of expertise).

I see large companies doing this - I also see restaurants doing it.

It's a variation on "modular computing".
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-09-14T12:44:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jhvrm.35065$u76.20247@newsfe10.iad>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com>`

```

You know, having followed this thread and become bored by it, because the
same people are playing the same tape over again - I begin to wonder if it's
worth discussing.  Cobol is decreasing in importance - true.  It's behind
the times - true.  it's unfashionable - true.  It works perfectly well when
it's used properly (just like any other tool) - true.  It is used in
zillions (generic number for whatever you want to ubstitute)  of
installations for important  and mission-critical applications - true.  It
will continue to be used for the foreseeable future - true.

 It will continue to decline in relevance: impossible to say.  Radio would
kill newspapers.  TV would kill radio & movies.  Interent will kill them
all.  Well, let's wait 20 years or so and see.  None of us are legitimate
prophets and nobody knows what the next revolution will be.  (As a small
example of this: who would have predicted ten years ago that ringtones would
be a billion-dollar business??)   Some compelling reason may (I say MAY)
force a change.

I'll also add that many things touted as brand-new & important look from a
distance to be revamping old things as new ideas.  Remember RISC?  The very
first computers had 32 or so instructions.  IBM's FBA?  the first disks had
fixed-length architecture.  Cloud computing?  Can you say tarted-up and
invisible service bureau?

Who knows?  But at least let's not evangelize on the decline of this or
that.

PL
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-14T12:42:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lc3ta5l7d68kanshuahpjjqdb1kbh7u6mg@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com> <Jhvrm.35065$u76.20247@newsfe10.iad>`

```
On Mon, 14 Sep 2009 12:44:22 -0500, "tlmfru" <lacey@mts.net> wrote:

>Who knows?  But at least let's not evangelize on the decline of this or
>that.

Agreed.    Evangelizing implies True Belief, and it's silly to do that
about a tool.    

It is important to recognize the possibility of guessing wrong and
making sure we have side doors in the event that we discover that the
highway we're on leads to a dead-end.    And that "we" is all of us,
no matter where we stand in the argument at hand.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-15T11:45:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h82t2F2rdb9tU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com> <Jhvrm.35065$u76.20247@newsfe10.iad>`

```
tlmfru wrote:
> You know, having followed this thread and become bored by it, because
> the same people are playing the same tape over again - I begin to
> wonder if it's worth discussing.

Well, Gee, Peter, sorry if we're keeping you awake... :-)

If you don't think it is worth discussing then don't discuss it.

Like all conversations, if you find it boring, just move on to a different 
group.

I have to admit, I'm finding it less fun than it used to be. The frequency 
of my posts has declined as a result.

>Cobol is decreasing in importance -
> true.  It's behind the times - true.  it's unfashionable - true.  It
…[4 more quoted lines elided]…
> for the foreseeable future - true.

I disagree with your last statement, but perhaps I see further than you do.
>
> It will continue to decline in relevance: impossible to say.  Radio
…[5 more quoted lines elided]…
> compelling reason may (I say MAY) force a change.

Or the evolution of a new ways of doing things. Some of what is currently in 
labs will have far reaching effects on how we see and use computers in the 
not-too-distant future.

Perhaps you could dispel some of your ennui by reading Kurtzweil's "The 
Singularity is Near"?

There are some exciting ideas there.

>
> I'll also add that many things touted as brand-new & important look
…[4 more quoted lines elided]…
>

Or you could just say ITSA to everything and keep it limited to your own 
experience, when you should be saying ITSLIKE and recognizing the 
differences...

> Who knows?  But at least let's not evangelize on the decline of this
> or that.

The whole purpose of an unmoderated public forum is so that people can say 
what's on their mind. Inevitably some people won't like it, others will feel 
it doesn't go far enough, some will see passion as evangelism, others will 
see a chance to indulge rhetoric and pedantry, and some will be bored by it. 
It is a hugely diverse universe of posters and readers.

But it isn't going away and whether you like it or not, it will be here for 
"the foreseeable future"... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-16T12:21:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8r72i01d4b@news2.newsguy.com>`
- **In-Reply-To:** `<q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 11 Sep 2009 18:13:56 -0400, Michael Wojcik
> <mwojcik@newsguy.com> wrote:
…[7 more quoted lines elided]…
> constrained by regulations than by particular business needs.   

That doesn't apply to the kind of customer I'm talking about.
Regulation *is* core. A failure in the regulatory realm can destroy
these firms.

At MF DevForum 2006, we had a presentation by NYSE Arca (formerly
Pacific Exchange). They're a stock exchange, and under US law they're
a Self-Regulating Organization (SRO). That means very strict, complex,
daily reporting requirements. They *cannot* fail to meet those
requirements for any significant length of time and remain in
business. That was one of their major requirements in their migration;
they talked about it at length in their presentation.

For organizations like that, complying with regulation is like
monitoring the assembly line in a factory. Outsourcing that kind of
processing would be a tremendous risk.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-16T12:08:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qr92b5h994mfkjsviilbjlphei6224pcr2@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <7gq8aiF2qjbmcU1@mid.individual.net> <h8grdu02fer@news2.newsguy.com> <q2tsa5p5o1itfugbt7mqrsj3rgp89kornk@4ax.com> <h8r72i01d4b@news2.newsguy.com>`

```
On Wed, 16 Sep 2009 12:21:20 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>> I see the same thing happening for many types of regulatory reports,
>> collections processing, payroll, taxes, etc.     Contract out these
…[5 more quoted lines elided]…
>these firms.

Sure there are such examples.   Obviously some businesses have these
as their core business.    Whatever your core business is, that's what
you need to work on.    

Tool makers can make money by producing special purpose tools for
relatively small numbers of businesses - losing some economy of scale.
I just think packaging up existing complicated regulations in code
that should not be reanalyzed is a niche need.    Most companies are
better off letting specialists do that work.

Maybe my experience is atypical - but I see companies starting over
when they replace their core systems.   I also see companies
outsourcing various subsets of their business IS - stuff like taxes
and billing and collection - when they aren't in the tax and billing
or collection business.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-09T13:13:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqufa5pa0778qghg14s6cofnjetpa56ra4@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net>`

```
On Thu, 10 Sep 2009 04:14:36 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>They don't need to rewrite their legacy in a different language to run it on 
>.NET. All they have to do is wrap it. BUT, they are bing TOLD that they have 
…[11 more quoted lines elided]…
>thing.

Those making the decisions to spend the money often find a harder sell
in trying to persuade their bosses that wrapping their current code to
make it more accessible is worth much, career wise.    Sure it's nice
to keep current business rules - but the larger the change, the more
important it is to do a complete analysis which is likely to result in
a major rebuild.    The major rebuild is more visible to the powers
that give promotions and money.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 4)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-09-12T15:06:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8grft32fer@news2.newsguy.com>`
- **In-Reply-To:** `<7gq2jdF2ohsbvU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[13 more quoted lines elided]…
> It simply isn't true.

If they want to run applications built from legacy source as managed
code, they certainly do have to recompile it. And there are excellent
reasons to run fully managed.

>> And once those applications are migrated, it's easy to gradually
>> replace them with more modern, OO code, using OO COBOL or any other
…[5 more quoted lines elided]…
> migrating to .NET.

Again, a .Net COBOL compiler is absolutely required to run COBOL
programs as managed code. There's no way around that. That's the
definition of a .Net COBOL compiler.

There are .Net environments - SQL Server, IIS managed app pools, WAS,
Azure - where native code is a second-class citizen or simply not
allowed. And there are a lot of benefits to managed code, like much
more robust runtime type checking, safer exception handling,
verification, etc.

We have plenty of customers who continue to run COBOL apps as native
code. Some interoperate with .Net through PInvoke or by wrapping them
as COM services. That's fine.

But for many people, that's simply not satisfactory. They want managed
COBOL, and for that they need a .Net COBOL compiler.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-13T13:38:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h30oeF2pakqpU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gfp1jF2pfqolU1@mid.individual.net> <h88e1a0q29@news5.newsguy.com> <7gq2jdF2ohsbvU1@mid.individual.net> <h8grft32fer@news2.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
…[18 more quoted lines elided]…
> reasons to run fully managed.

No there aren't. Those reasons are very arguable and nowhere near as 
important as someone selling a .NET compiler would have you believe.

I've been running unmanaged legacy code for some years now without a single 
incident. But I am an informed user who knows what I'm doing and I don't get 
panicked by threats of dire consequences from vendors.

It is a paper tiger.

You can run legacy perfectly safely as unmanaged code provided you debug it 
properly and test it properly. (If you don't do that, even managed code will 
fail...) Fortunately, most legacy code that is runnig every day has already 
been tested and debugged.

New development is going to be managed code and that's fine too.

The proof of the pudding is in the eating.

I've eaten it and it is delicious. :-)

Best of both worlds, and no need to shell out for an expensive product for a 
language I've phased out.


>
>>> And once those applications are migrated, it's easy to gradually
…[11 more quoted lines elided]…
> definition of a .Net COBOL compiler.

But you keep saying it as if it were a mantra.

Yes, you need a .NET COBOL compiler to run COBOL as managed code, but there 
is NO need to run legacy COBOL as managed code at all. It runs fine as 
unmanaged. (In fact, it's actually more efficient because it isn't 
interpreting CLR...) Those nice people at Microsoft provided InterOP 
services for exactly that scenario. So that applications written in 
languages for which there may not be a .NET compiler (and there wasn't 
always one for COBOL...) can enjoy the benefits of the platform just like 
everybody else.
>
> There are .Net environments - SQL Server, IIS managed app pools, WAS,
> Azure - where native code is a second-class citizen or simply not
> allowed.

Michael that is demonstrably untrue. You seem to be uncharacteristically 
misinformed here. I am running SQL server apps under InterOP services 
(unmangaed code), I am running IIS ASP.NET apps that use unmanaged code in 
C# code behind pages under Interop services, and I have no doubt whatsoever 
that these same components will run in the cloud or Azure without problem 
too.

>And there are a lot of benefits to managed code, like much
> more robust runtime type checking, safer exception handling,
> verification, etc.

But even under managed code, if it fails, then it has failed. There is no 
danger of it running rogue and affecting other applications, but there is no 
danger of that anyway if the code is properly debugged. (or compiled with 
BOUNDS checking)
>
> We have plenty of customers who continue to run COBOL apps as native
> code. Some interoperate with .Net through PInvoke or by wrapping them
> as COM services. That's fine.

Yes, that would be the way I do it for most of the legacy. PInvoke is pretty 
much old hat now but InterOP services and COM function perfectly well.

>
> But for many people, that's simply not satisfactory. They want managed
> COBOL, and for that they need a .Net COBOL compiler.

And why do they "want managed COBOL"?... because someone who just happens to 
have a compiler costing thousands of dollars has told them that they need 
it, and there are severe risks in running unmanaged and you don't want to be 
a "a second class citizen" do you...? :-)

(Most of my life I have dreamed of aspiring to be second class...) :-)

I can see people who are spending a fortune on IT not being worried about 
it. It is a small amount in the overall scheme of things, and they can look 
on it as an insurance policy. But for small businesses like mine and the 
people I'm talking to, it just isn't justifiable, UNLESS you are planning to 
stay with COBOL long term. Nobody I know is.(Most of us simply can't afford 
to...)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-14T12:53:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8lecv$bmk$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gq2jdF2ohsbvU1@mid.individual.net> <h8grft32fer@news2.newsguy.com> <7h30oeF2pakqpU1@mid.individual.net>`

```
In article <7h30oeF2pakqpU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I've been running unmanaged legacy code for some years now without a single 
>incident. But I am an informed user who knows what I'm doing and I don't get 
>panicked by threats of dire consequences from vendors.

Mr Dashwood, to be, simultaneously, 'an uninformed used who knows what 
(he's) doing' and a data-processing professional with decades of 
experience across various platforms and businesses seems a pretty neat 
trick.

I also do not know how many of the systems you currently manage must take 
into account the labyrinthine regulations which are required in such 
industries as banking, insurance, finance, human resources and government 
contracting, systems where hundreds of millions of transactions per day 
are commonplace and a table of 60,000,000 rows is considered one of 
fair-to-middling size... but that's neither here nor there.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-15T01:35:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h6v5sF4dla6U1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7gq2jdF2ohsbvU1@mid.individual.net> <h8grft32fer@news2.newsguy.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7h30oeF2pakqpU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> trick.

It would be extremely unlikely. I never said that and you seem to have 
misread what I DID say...
>
> I also do not know how many of the systems you currently manage must
…[5 more quoted lines elided]…
> nor there.

Most industries have regulations; some are indeed labryinthine. Large 
industries have no monopoly on red tape.

Personally, I would not design a table to contain 60,000,000 rows and if I 
had a normalized table with that kind of volume I'd split it physically 
across a number of servers. So no, I am unlikley to ever process 60,000,000 
rows in a single table, from a single thread. (I might well process 
10,000,000 rows on six threads simultaneously... but, as you observed, 
that's neither here nor there...)

But volume isn't everything.

I HAVE worked for Banks and Governments where their processing was batch 
oriented and their systems were primitive by modern standards. I seem to 
recall some of them even used that archaic procedural paradigm implemented 
by ... let me see now... was it SNOBOL? (pronounced "snowball", apparently), 
or JOVIAL (Jules own version of the international algorithmic language)?... 
no, I remember ... it was COBOL.

Not much call for it these days, apparently.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-14T14:51:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8llab$6bj$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net>`

```
In article <7h6v5sF4dla6U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7h30oeF2pakqpU1@mid.individual.net>,
…[15 more quoted lines elided]…
>misread what I DID say...

My apologies, Mr Dashwood.  So you are not a data-processing professional 
with decades of experience across various platforms and businesses?  That 
might explains a few things, then.

>>
>> I also do not know how many of the systems you currently manage must
…[17 more quoted lines elided]…
>But volume isn't everything.

When there is a drop-dead time for the processing of a set of transactions 
entered during a given period (remember 'batch windows') it comes fairly 
close, aye.

>
>I HAVE worked for Banks and Governments where their processing was batch 
>oriented and their systems were primitive by modern standards.

I've no idea what you believe to constitute a 'modern standard', Mr 
Dashwood... but I know that here, in the United States of America, if a 
deposit is made under certain conditions the funds of said deposit MUST BE 
AVAILABLE TO THE ACCOUNT HOLDER BY THE OPEN OF THE NEXT BUSINESS DAY.  
This is not a courtesy or a nice thing to do... it is The Law.

Primitive or not, it is usually a Good Idea if a business' processes are 
in accord with The Law... unpleasant situations might result were they 
not.

>I seem to 
>recall some of them even used that archaic procedural paradigm implemented 
…[4 more quoted lines elided]…
>Not much call for it these days, apparently.

COBOL, SNOBOL, JOVIAL, ADA, PL/I... the path is of secondary importance, 
Mr Dashwood.  Of primary importance is compliance with The Law.  Secondary 
importance might be given to satisfying users as unsatisfied users tend to 
find other organisations with which to do business.

Tertiary importance could be assigned to 'keeping the one who signs the 
checks for the systems smiling'... because chances are pretty good that an 
organisation that doesn't comply with The Law and keep its customers happy 
won't have sufficient funds in its accounts to sign checks.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-15T09:45:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h7rs8F2qk6dmU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7h6v5sF4dla6U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[21 more quoted lines elided]…
> businesses?  That might explains a few things, then.

Why don't you just accept you got it wrong, Doc? You read "uninformed" where 
I wrote "informed".

As for being a "data-processing professional with decades of experience 
across various platforms and
businesses"  that is just a matter of record.

Explain a few things?  Like Mary Poppins, I never explain anything...


>
>>>
…[23 more quoted lines elided]…
> it comes fairly close, aye.

No, the volume has nothing to do with the time available.

The time available is fixed.

The volume must be processed in that time. You and I have different 
approaches for achieving that.
>
>>
…[8 more quoted lines elided]…
> The Law.

Perhaps you might look around and realise that the World is not encompassed 
by the United States of America?

Most countries would meet the criterion you expressed, whether it is the law 
or not.

In NZ fund deposits are available within 15 minutes in most cases.

But then, we are not limited by laws passed years ago...
>
> Primitive or not, it is usually a Good Idea if a business' processes
> are in accord with The Law... unpleasant situations might result were
> they not.
>

It is possible to be law abiding and still eschew primitive processes...


>> I seem to
>> recall some of them even used that archaic procedural paradigm
…[12 more quoted lines elided]…
>

You are struggling to find something to argue about. I never disagreed with 
any of your deflections regarding the Law or satisfying customers.

> Tertiary importance could be assigned to 'keeping the one who signs
> the checks for the systems smiling'... because chances are pretty
…[3 more quoted lines elided]…
>

Sure. No argument.

Pete.
> DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-14T23:12:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8mik2$4le$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net>`

```
In article <7h7rs8F2qk6dmU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7h6v5sF4dla6U1@mid.individual.net>,
…[25 more quoted lines elided]…
>I wrote "informed".

Mr Dashwood, I quoted 'uninformed' where you posted 'informed'... and I 
quoted 'used' where you posted 'user'.  Some might see it interesting that 
you chose to emphasise one instead of the other.

>
>As for being a "data-processing professional with decades of experience 
>across various platforms and
>businesses"  that is just a matter of record.

On the UseNet nobody knows you're a record... me, I'm a 106-rpm Edison 
Celluloid 'Napkin Sleeve'.

[snip]

>> I've no idea what you believe to constitute a 'modern standard', Mr
>> Dashwood... but I know that here, in the United States of America, if
…[6 more quoted lines elided]…
>by the United States of America?

Were I unaware of that fact, Mr Dashwood, it might have been unlikely that 
I would have specified it as I did.

>
>Most countries would meet the criterion you expressed, whether it is the law 
>or not.

Mr Dashwood, perhaps you might want to look at the United States of 
America, where that condition (availability by next business day) is only 
one of a subset of a variety of conditions.

>
>In NZ fund deposits are available within 15 minutes in most cases.
>
>But then, we are not limited by laws passed years ago...

You are also not limited by seven time zones, three hundred million people 
and a few delicate balances between local, state and federal 
requirements... it is so much easier having a Monarch's dictates so much 
closer in one's past, perhaps.

[snip]

>> COBOL, SNOBOL, JOVIAL, ADA, PL/I... the path is of secondary
>> importance, Mr Dashwood.  Of primary importance is compliance with
…[5 more quoted lines elided]…
>You are struggling to find something to argue about.

Only in the same fashion as you might be trying to find something to 
Managerially dismiss, Mr Dashwood... and this, at least for me, is *far* 
from a struggle.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-15T07:37:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net>`

```
On Tue, 15 Sep 2009 09:45:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>But then, we are not limited by laws passed years ago...

Interesting statement.    I'm picturing a legal defense pointing out
that a law is years old...
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-16T02:36:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h9n2mF2t37tdU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 15 Sep 2009 09:45:42 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[4 more quoted lines elided]…
> that a law is years old...

Laws that don't work generally get changed here. We are in the middle of 
that process at the moment over whether it should be legal to smack 
children.

A Law was passed by the previous "nanny State" (sometimes, for a small 
country, we really try too hard...) Government that it is illegal for 
parents to smack children. The idea was to stop violence against children 
and there have been some dreadful cases of it so everyone wanted something 
done...

The new law doesn't work, is virtually unenforceable, and when it is 
enforced, it is not enforced consistently, so they had a referendum (non 
binding on the Government) on whether it should be revoked. It was a 
landslide against it and more people voted than in the general election...

Government wanted to remind everyone that they call the shots, and that the 
law in any of its incarnations is not to be taken lightly, so they were 
reluctant to change the legislation, despite the referendum.

That was a couple of months ago. Government decided to have the whole 
situation investigated by a Parliamentary commission. Then they can change 
it wthout losing face... ("Commission recommended it be changed...")

It is kind of amusing sometimes to see the law being an ass.

The only saving feature is that at least things do get changed.

So, for the most part, our laws are relevant to the world in which we live 
and the views of current society, rather than society as it was 200 years 
ago. Our laws are also a unique blend of Pacific island communal culture and 
British justice. It seems to work pretty well and I'm not planning on 
emigrating...

Corporate legislation, which is what this conversation started about, is 
also subject to the same kind of pressure for change, although not 
necessarily through a national referendum. There are legal requirements on 
companies, just as there are on individuals... and, as a Company Director, I 
am familiar with the salient ones. None of them are unreasonable, onerous, 
or "labryinthine", in my opinion and I have no trouble paying someone to 
make sure I comply with them... :-) Joking aside, it really isn't that bad 
and honest people would have no problem with compliance.

It is the nature of Antipodeans (the Australians are very much the same as 
us in this regard) to resent being governed and to tolerate only what is 
really necessary... :-) As the people in Government are generally from the 
same culture, they recognise this and know that if they want to be 
re-elected, it is best not to try imposing too much control.

Here in NZ these lessons were hard learned. For many years (right up until 
the 1980s really) we had a controlling and regulatory Government that was 
very Right wing, and reactionary.  Shops traded in restrive hours, 
restaurants could not sell liquour, the pubs shut at 6.00 pm, looking back 
on it, I don't know how we survived. As the values in society changed, the 
call for change in the laws and government intensified and finally, we came 
kicking and screaming into the modern world, after living in the Victorian 
one for much longer than we needed to or should have.

Today, the laws we live under are neither onerous nor convoluted. It is 
better than it used to be...

Now, if you want to talk about labrynthine red tape, you should see the 
rules set by the committee of the local golf club... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-15T15:48:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8od16$45q$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net>`

```
In article <7h9n2mF2t37tdU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>It is the nature of Antipodeans (the Australians are very much the same as 
>us in this regard) to resent being governed and to tolerate only what is 
…[8 more quoted lines elided]…
>on it, I don't know how we survived.

Readily answered... given the first paragraph as true then a logical 
conclusion is that New Zealanders weren't Antipodeans until the 1980s.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-16T11:48:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hanedF2rdq8qU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <h8od16$45q$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7h9n2mF2t37tdU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[19 more quoted lines elided]…
> DD

There's a lot of truth in that.

You could argue we were Victorian British colonials struggling to find our 
own identity, for around 150 years.

That struggle still continues, but it is heading in the right direction and 
we have a diverse and multicultural society which, largely, works.

I wish I could be here in another 50 years, because I believe something 
unique and valuable is emerging.

Never mind, the sun is shining and there are some native bellbirds (they're 
called "tuis") enjoying the nectar on the native trees in front of my house, 
and singing their hearts out. It is like the boys going out and getting 
drunk then forming a midnight chorus (except it is midday). A salutary 
reminder for me of two things:

1. No matter how much money I make, I can never make that bird sing for me.
2. Life is fleeting and should be enjoyed.

I think I can take a coupleof hours off and go to the beach... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-16T07:47:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nsq1b5p3knl6smeechv9od3lilh915k3b8@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <h8od16$45q$1@reader1.panix.com> <7hanedF2rdq8qU1@mid.individual.net>`

```
On Wed, 16 Sep 2009 11:48:28 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I wish I could be here in another 50 years, because I believe something 
>unique and valuable is emerging.

I've seen (and read) enough history to suspect that in 50 years you
would find some stuff you like - and others which you were hoping
would be gone.

It seems particularly unlikely that a society that is based upon
change won't change itself into a society that likes things
unchanging.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 12)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-09-15T11:56:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zGPrm.4914$tG1.2492@newsfe22.iad>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
news:7h9n2mF2t37tdU1@mid.individual.net...
> Howard Brazee wrote:
> > On Tue, 15 Sep 2009 09:45:42 +1200, "Pete Dashwood"
…[10 more quoted lines elided]…
>
<snip>
>
> So, for the most part, our laws are relevant to the world in which we live
> and the views of current society, rather than society as it was 200 years
> ago. Our laws are also a unique blend of Pacific island communal culture
and
> British justice. It seems to work pretty well and I'm not planning on
> emigrating...
>

Actually, there's more to it than that.  There is the Law - the exisitng
body of legislation and statutes and practice which is available in the
Legislative Library, which is what you're referring to; and there is legal
history and precedent.  The latter, referred to as Common Law if I have my
details correct,  is orders of magnitude greater in volume than the Law -
recognizing in England at least experience that goes back to about 900AD in
bulk, and specific cases before that.

I'd bet a beer that there remain on the books any number of silly laws -
such as the classic one that a car must be preceded by a man with a bell and
a red flag (I jest but you know what I mean).  Unless there's a specific
agency to review old statutes, I'd hazard a guess that many laws simply are
forgotten since they no longer apply.

The spanking debate is in progress in Canada also, although at the moment it
seems to be quiet.  The question to be resolved apparently is whether
children know why they're being spanked or if they perceive it as a sudden
and reasonless attack on them.

PL
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-15T11:53:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q6kva5l67lvoot7am0cda9cvstomoav549@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad>`

```
On Tue, 15 Sep 2009 11:56:11 -0500, "tlmfru" <lacey@mts.net> wrote:

>Actually, there's more to it than that.  There is the Law - the exisitng
>body of legislation and statutes and practice which is available in the
…[4 more quoted lines elided]…
>bulk, and specific cases before that.

...

>The spanking debate is in progress in Canada also, although at the moment it
>seems to be quiet.  The question to be resolved apparently is whether
>children know why they're being spanked or if they perceive it as a sudden
>and reasonless attack on them.

So much of this is subjective and even fashion.   We have
"fashionable" crimes which get more or less attention depending upon
what society is interested in.    (Of course our values today are the
Right ones - the ones God intended us to have from the time of
creation).

An odd one I read about a couple of weeks ago was when someone got
arrested and charged with cruelty to animals when he hired someone to
kill his dog and make a belt out of his skin.     Replace "dog" with
"cow" in that accusation and nobody would have been arrested.    The
law doesn't define a dog as being the type of animal we can't kill and
a cow as the type we can kill - that's apparently up to society to
decide.

With spanking, we really don't need to have children have a rational
reason to avoid playing on a hot stove.    "Mommy will be angry" is
sufficient reason.   Understanding won't increase that child's
survivability.    If yelling works as well as spanking, great.   But
if explaining doesn't work as well - do what keeps the child from
getting burned.

Many of the regulations and standards we follow in our computer
programming are useful in that they exist at all.   If we know that
banks will have our deposits available at 8:00, we can use that money
at that time.   Or if we know it will be available in 2 hours.    
```

###### ↳ ↳ ↳ OT: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-16T13:14:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hasg0F2scldsU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad>`

```
tlmfru wrote:
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
> news:7h9n2mF2t37tdU1@mid.individual.net...
…[35 more quoted lines elided]…
> that many laws simply are forgotten since they no longer apply.

I'd gladly share the beer with you, Peter, but I believe you'd lose your 
bet.

Our legislation simply doesn't have 1000 years of history and was rewritten 
from scratch in the 20th century. (Well, to be fair, it was reviewed from 
British Statutes and other appropiate laws for the culture were added. It 
would have been during that process that the law which requires London taxi 
drivers to carry a bale of hay in the back of their diesel taxis, (and 
similar anachronisms) were removed.)

> The spanking debate is in progress in Canada also, although at the
> moment it seems to be quiet.  The question to be resolved apparently
> is whether children know why they're being spanked or if they
> perceive it as a sudden and reasonless attack on them.
>

It's like we never learn: you cannot legislate effectively against the 
mindset of the community.

If you're concerned about Race Relations, don't try and introduce positive 
discrimination; change people's minds about being Racist. (You won't do it 
overnight but we have seen here that it can be done. Young people, 
particularly, here are far less bigoted than their grandparents were and the 
community view is different than it was even 50 years ago. I have seen it 
change in my lifetime.)

Start in schools and teach kids that race, colour, and creed all deserve 
respect, and that differences in culture contribute to an overall culture 
that we can all be proud of.

If you're concerned at child (or parent) abuse, you will never change it by 
making it illegal. You need to persuade the people who do it that it is not 
a good thing to do.

Some of them can't be reached due to booze, drugs, and apathy, so what can 
you do?

I recently wrote a guest Editorial in the local paper here, and it was 
picked up and syndicated throughout NZ.

It's only a few hundred words so I'll take the liberty of including it here:

[quoted editorial]

In August there is going to be a 23 hour telethon. You can phone in and 
pledge support for KidsCan.

The primary objective is to buy raincoats and shoes for little feet.

Very few of us would find it acceptable for kids to go to school wet and 
cold, but I got to thinking about this.

I have a couple of friends who are single Mums. It isn't easy but they have 
learned to keep an eye out for bargains and to "shop clever".
One of them tells me she bought two raincoats on sale for her little one for 
$10. ($5 each - one is a larger size for him to grow into)
A pair of gumboots for around $4 in a Warehouse Sale. Hat and scarf from the 
$2 shop.

So, for around the same price as a packet of fags, you can ensure your 
toddler is protected against the weather.

Obviously, as kids get older and bigger, there is more cost involved, but 
the principles still apply. I guess what's bothering me
about this is the acceptance by the community that it is necessary to step 
in and fix it, without actually considering what it is
that needs fixing...

If the community takes responsibility for what should really be a parental 
obligation, is it any wonder that kids are being neglected
and mistreated?

Why aren't we getting parents of "at risk" kids to take responsibility for 
their kids? If a weak parent knows that their child will
be cared for on humanitarian grounds, by people who can feel warm and fuzzy 
because they "did good", without actually thinking through
the implications of their actions, then we are not building a community to 
be proud of.

I know there are some genuine cases of real hardship. That is why we have 
WINZ. Also, I am not a mean or ungenerous man and I don't
want kids to suffer. But I DO want to see more action on getting parenting 
right.

Instead of handing out raincoats to "lower decile" schoolchildren, why can't 
we fund parent/teacher interviews, encourage parents to
take responsibility for their children, run parenting classes for parents 
who are not good at it, provide help and advice lines for
parents who want to do better? Practical advice like how to clothe kids on a 
limited budget (It CAN be done, but it requires perseverence
and effort.) I could see handouts being dependent on attendance by the 
parents at parenting seminars and parent/teacher meetings, with
raincoats being dispensed to the parents, not directly to the children.

Kids should perceive their parents caring for them, not the community.

Assistance should be earned. If you haven't got anything and are truly on 
the poverty line, at least show willing...If you truly cannot
clothe your kids then you should expect to receive help and advice, not just 
a handout.

New Zealand is a blend of many cultures and some of those cultures 
traditionally consider the child to be the responsibility of the
community. That is not a bad thing, but it needs to be tempered with the 
fact that the PRIMARY RESPONSIBILITY for children is with the parents.

If you'd rather drink, gamble, or smoke your kid's allowance away, in the 
certain knowledge that other, more responsible, people will
try and paper over the cracks for you, it is time you woke up.

If you really don't care about your kids and see them as a hindrance and a 
nuisance, seek help.

Being poor is not a crime; being irresponsible with your children, certainly 
is.

[/guest editorial]

One of the effects of the above was that I received a phone call from the 
head of a group called "KiwiCan" .(His name is Dan and he is a remarkable 
man...:-)). He invited me to come and see what they were doing in 7 local 
schools, so I did. It was incredible.

When most of us think about schools, we are thinking about academic 
achievement, and most parents experience anxiety, realising that how their 
kids do at school can have a significant effect on the opportunities 
available to them in later life. Sometimes we get so focused on the academic 
side we forget that equally important (probably even more so...) are the 
"life skills". Dan told me there are some parents who can never be reached. 
I disagreed. I believe EVERYBODY can be reached if communiication is carried 
out effectively. After 30 minutes he changed my mind.  His arguments, 
(backed by actual cases) were compelling. I then asked the question which I 
noted above:

So, what do we do?

Dan's solution is, if you can't reach the parents, do it through the kids.

I sat in on a session at a local Primary school (KiwiCan targets kids aged 8 
to 13) and spoke with some of the children. They were all eager and 
enthusiastic about the KiwiCan sessions. The whole class attends (they don't 
just target certain kids) they have fun activities and role playing and they 
learn ethics and values "in passing" without being preached at or having a 
particular value set rammed down their throats. These sessions teach 
personal responsibility, and the importance of honesty and moral courage. 
They are acquiring skills which will set them up for life.

Kids from homes where parents are doing a good job simply have what their 
parents have been telling them reinforced; other kids come to realise that 
how life is at their place is not necessarily how it HAS to be.

The Principal of the school told me he was delighted with the program and 
bullying had dropped by 80% since it was introduced.

KiwiCan gets NO Government assistance, it is funded from local sponsorship 
by businesses and public donations. Schools contribute $1200 a year to have 
the program on their site. For $2 per child, per week, the program is doing 
incredible work and is a very worthwile investment in the future of the 
local community. The "overheads" (administration costs and small payments to 
volunteers who implement the program) are 8%. No-one is getting rich off 
KiwiCan (least of all Dan, who is also a parent with kids at local schools), 
and yet the community as a whole is benefitting in ways yet to become 
apparent. The program has been running for 6 years and some of the kids have 
gone on to a teenage program (called "Project K") that gets them involved in 
the outdoors and teaches leadership and confidence. (This was instigated by 
Graeme Dingle, an explorer, mountaineer, and close personal friend of Sir 
Edmund Hillary, mainly known for his circumnavigation of the Arctic, and for 
climbing all the major peaks in Europe in a single season. Despite several 
Himalayan expeditions he has never made the summit of Everest; I didn't like 
to ask him if that bothered him... :-)I met him a few nights ago and spent 5 
minutes chatting to him. He is a very interesting man... :-)).

At the same function, after Graeme had explained how and why he set up 
"Project K", a 17 year old from this program told us what it had meant to 
him. It was very impressive. Both Project K and KiwiCan are programs 
implemented through an umbrella trust set up by Graeme Dingle. I chatted 
with some young women who had also been through Project K and were now 
enrolling as mentors for the program.

Sometimes, when you pick up a newspaper, it is easy to despair and think the 
world is going to Hell in a handcart.

There are people out there who are determined to stop it and they deserve 
our support.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-16T07:52:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5r1b5tif7qdvb85um7k39g77jv6649m3f@4ax.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad> <7hasg0F2scldsU1@mid.individual.net>`

```
On Wed, 16 Sep 2009 13:14:40 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>There are people out there who are determined to stop it and they deserve 
>our support.

It's a great battle that should continue to be fought.   But don't
fool yourself into thinking the war will ever be won.

Discrimination isn't about race or class or whatever except that these
are where we can see that those other people aren't us and don't do
nor think things the Right way.   My team is better.   My family is
better.   My race is better.   My diet is better.   My indoctrination
is better.   My religion is better (we are Good, and you will be
tortured for not believing that).    If I can use rational methods of
teaching you to think the way I do - I will take that effort, it's
bound to win because obviously my way is Right.
```

###### ↳ ↳ ↳ Re: OT: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-16T14:49:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8qtt4$ood$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad> <7hasg0F2scldsU1@mid.individual.net>`

```
In article <7hasg0F2scldsU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>Start in schools and teach kids that race, colour, and creed all deserve 
>respect, and that differences in culture contribute to an overall culture 
>that we can all be proud of.

You've got to be taught
To hate and fear,
You've got to be taught
From year to year,
It's got to be drummed in your dear little ear,
You've got to be carefully taught.

You've got to be taught to be afraid
Of people whose eyes are oddly made,
And people whose skin is a different shade,
You've got to be carefully taught.

You've got to be taught before it's too late,
Before you are six or seven or eight,
To hate all the people your relatives hate,
You've got to be carefully taught.

- from South Pacific (lyrics: Rodgers, music: Hammerstein), 1949.

Of course, there are those who will recall that a fear or distrust of The 
Other is an ancient human tendency... while conveniently forgetting that 
children need to be dragged away from joyous play with the intoning of 
'You don't play with kids like that, y'hear?  They're not Like Us, you 
just stay away'.

DD
```

###### ↳ ↳ ↳ Re: OT: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-17T11:12:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hd9n4F2tsd8gU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad> <7hasg0F2scldsU1@mid.individual.net> <h8qtt4$ood$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7hasg0F2scldsU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[24 more quoted lines elided]…
> - from South Pacific (lyrics: Rodgers, music: Hammerstein), 1949.

Wow! I never knew that was in South Pacific. Seen the show several times 
over the years and it never registered.

And in 1949 that was just years ahead of the prevailing attitudes.

Thanks Doc.

>
> Of course, there are those who will recall that a fear or distrust of
…[4 more quoted lines elided]…
>

And the sad thing is that until that happens kids will play together happily 
without any thought to the "differences"...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-17T13:11:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tci3$fra$1@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7hasg0F2scldsU1@mid.individual.net> <h8qtt4$ood$1@reader1.panix.com> <7hd9n4F2tsd8gU1@mid.individual.net>`

```
In article <7hd9n4F2tsd8gU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7hasg0F2scldsU1@mid.individual.net>,
…[6 more quoted lines elided]…
>>> overall culture that we can all be proud of.

[snip]

>> You've got to be taught before it's too late,
>> Before you are six or seven or eight,
…[6 more quoted lines elided]…
>over the years and it never registered.

As the decades pass, Mr Dashwood, I find more and more odd things get kept 
in core... errrrr, RAM... and even odder things show up once they get 
archived in... errrrr, brought online from near-line storage.

>
>And in 1949 that was just years ahead of the prevailing attitudes.

Art imitates Life imitates Life imitates Art imitates Life and the wheels 
within the wheels go 'round and 'round.  If you think the abovegiven 
example shows 'progress'... do a bit of searching on Aimee Semple 
Macpherson and you might find that things stagnate, as well.

>
>Thanks Doc.

Anytime, old boy.

>
>>
…[8 more quoted lines elided]…
>without any thought to the "differences"...

That's the point I tried to make, aye... for the children there are no 
'differences' until They Are Carefully Taught.  

On the other hand, though... 'to see the world as a child' is said, at 
times, to be a valuable thing, to be devoid of the rote learnings and 
prejudices picked up over the decades so that the Wonder Of It All is more 
readily apparent.  On the other hand... to 'see the world as a child' can 
also mean that there's a miniature orchestra playing inside the radio and 
that there's no need to pay attention to that little cut on your foot you 
got from stepping on a rusty nail.

Perhaps I should wait until I retire until I begin to philosophise (from 
'The Tall Blonde Man with One Black Shoe').
DD
```

###### ↳ ↳ ↳ Re: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 14)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-09-16T21:09:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vTgsm.194642$0e4.169834@newsfe19.iad>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad> <7hasg0F2scldsU1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
news:7hasg0F2scldsU1@mid.individual.net...

> > I'd bet a beer that there remain on the books any number of silly
> > laws - such as the classic one that a car must be preceded by a man
…[7 more quoted lines elided]…
> Our legislation simply doesn't have 1000 years of history and was
rewritten
> from scratch in the 20th century. (Well, to be fair, it was reviewed from
> British Statutes and other appropiate laws for the culture were added. It
> would have been during that process that the law which requires London
taxi
> drivers to carry a bale of hay in the back of their diesel taxis, (and
> similar anachronisms) were removed.)
>

Neat!

Obviously you know your country's system better than I do - but I'll leave
the bet in.  It's a guarantee that there will arise situations that the
framers of the legislations did not foresee - and they willl either have put
the case over until a law is made to handle it - or make up something on the
spot - or appeal to legal history for guidance.  Given NZ's history I
imagine that you would examine British Common Law first.  Easy to settle -
ask a lawyer of your acquaintance.  If I'm wrong, your legal system is at an
advantage over ours from the litigants' points of view - researching the law
& precedents will be a much quicker process - 1/5 of the time under
consideration.

PL
>
```

###### ↳ ↳ ↳ Re: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-09-17T22:54:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7heiqvF2s5g1hU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <7h7rs8F2qk6dmU1@mid.individual.net> <tv5va5tp5s2ib1oumlg4q4ecuov56qvki5@4ax.com> <7h9n2mF2t37tdU1@mid.individual.net> <zGPrm.4914$tG1.2492@newsfe22.iad> <7hasg0F2scldsU1@mid.individual.net> <vTgsm.194642$0e4.169834@newsfe19.iad>`

```
tlmfru wrote:
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
> news:7hasg0F2scldsU1@mid.individual.net...
…[27 more quoted lines elided]…
> British Common Law first.

Yes, that is exactly the process. It was only recently, because of a 
controversial murder case which cost the country millions, that the right to 
appeal to the Law Lords in London has been revoked. Instead, a similar 
Authoritative body is being set up locally. Obviously, laws are drawn by 
senior members of the Legal profession, in conjunction with members of 
Parliament and Ministers of the Government, and must be ratified by 
Paliament before coming Law.

As we are seeing with the smacking legislation, once that process is 
complete it can be very difficult to reverse it.


> Easy to settle - ask a lawyer of your
> acquaintance.

What?! And pay $180 an hour for the privelege...?!!! I think not...

> If I'm wrong, your legal system is at an advantage
> over ours from the litigants' points of view - researching the law &
> precedents will be a much quicker process - 1/5 of the time under
> consideration.

I don't think our system is perfect, but it is largely rational and 
reasonable. That's why it is kind of amusing when it makes an ass of itself. 
We all love to see Politicians embarrassed... it's part of the resenting 
being governed thing... :-)

Precedents are all searched by (networked :-)) computers (the entire legal 
system here is fully computerized) and typically take seconds. (I assisted a 
Local Lawyer with some computer stuff a little while back and I was 
impressed with how good the systems were.)

To give you an idea, here's the Sale of Goods Act 1909...(Strongly based on 
British Common Law...)

http://www.legislation.govt.nz/act/public/1908/0168/latest/DLM173958.html

Note it was amended and simplified in the 1980s and 1990s...

Here's a typical amendment to it, made in the light of conditions and 
technology changing...

http://www.legislation.govt.nz/act/public/1993/0091/latest/DLM311053.html

You can see that the language used is generally free of jargon, terms are 
carefully defined, it is intended for a wider audience than the Legal 
Profession...

Most of the actual Laws have Summaries in plain English available online as 
well. These summaries are available in 27 languages and ignorance of the law 
is not considered an excuse.

We tried to learn from the USA and NOT become a nation of litigants.

There are certain things here that you cannot sue for. If you have an 
accident, for example, it is covered by something called the Accident 
Compensation Corporation (ACC). (When I first knew it it was a Parliamentary 
Commission, but apparently they changed its name in 1992...)

http://en.wikipedia.org/wiki/Accident_Compensation_Corporation

 They have a standard list of damage and payouts, so it doesn't matter if 
you can afford to employ Perry Mason or not, ACC says a broken arm is worth, 
say, $5000 (the cost of getting it repaired is also met by the ACC, and 
there will be a payout if you are off work or lose income because of it.) If 
criminal negligence is involved, there will be punitive fines that go to the 
Government, and in extreme cases there may be a prison sentence.

The idea was to ensure that the person with the best lawyer doesn't always 
win...and to deter people from bringing frivolous lawsuits.

It seems to work quite well.

You can't sue MacDonalds for several million because you burned your mouth 
on the coffee, or for mental anguish because your fries were cold...

I can honestly say I have never had cause in business or personal life to 
bring a lawsuit against anyone and no-one ever has against me, either. 
Disputes are settled by discussion over a beer (or coffee), and, in the rare 
event that that doesn't work, with baseball bats or four by twos. We 
generally don't use guns, although the use of knives (particularly amongst 
gang members) is increasing. (We blame the influence of American 
television... :-))

Seriously, there obviously ARE occasions where legal opinion is required 
(corporates arguing company law over who has the right to what,  neighbours 
and families in dispute over land, property, etc. etc.) but it is not 
possible to sue just anybody for just anything.

The police are empowered to confiscate stereo equipment on the spot if you 
are disturbing the neighbours and don't respond to reasonable requests. 
(This has the unusual side effect of ensuring that the neighbours are 
invited to parties, were they often end up too drunk to care about the 
noise...:-))

I don't think there is a perfect legal system on the planet, but, obviously 
it is easier if you have 4 million people than lf you have 400 million...

Pete.
```

###### ↳ ↳ ↳ Re: Engineering society WAS: Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-17T13:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tcrr$fra$2@reader1.panix.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7hasg0F2scldsU1@mid.individual.net> <vTgsm.194642$0e4.169834@newsfe19.iad> <7heiqvF2s5g1hU1@mid.individual.net>`

```
In article <7heiqvF2s5g1hU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>tlmfru wrote:

[snip]

>> Easy to settle - ask a lawyer of your
>> acquaintance.
>
>What?! And pay $180 an hour for the privelege...?!!! I think not...

Where's your Mind for Business, Mr Dashwood?  Be patient... and begin to 
barter when a lawyer of your acquaintance asks you for a bit of 'computer 
advice'.

[snip]

>(I assisted a 
>Local Lawyer with some computer stuff a little while back and I was 
>impressed with how good the systems were.)

See?  A missed chance, perhaps another will come around.

DD
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 9)_

- **From:** Emerson <emersonlopes@gmail.com>
- **Date:** 2009-10-01T11:13:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ac80b3cf-f68f-4ccb-b064-a3472b17a7e1@33g2000vbe.googlegroups.com>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com>`

```
Come on, Pete...admit, you miss that time when you had happiness
coding nice things that no one have seen before in Cobol. The very
first time that you created a Window in character mode, the first time
that you added mouse support to your apps, the frustrating windows API
study, being ahead of time, until you saw OO in Cobol and said, this
is great, but I do not want to code thousands of lines to get GUI
(Fujitsu here I come). I know exactly what you feel, I was a beta
tester for VISOC back in middle 90's, after being happy with MF and
realize that VISOC wasn't the answer I went to Fujitsu too, and
finally I left Cobol for ASP, Java, C# and other stuff. I also spent a
lot of time feeling angry about the laziness of Cobol's developers
everywhere (they simply seems like frogs that don't try to escape even
when the water temp raises until boiling point). Now I know that this
community is formed by people that only common attribute is being
target of prejudice everywhere, and to be honest many of them will
never understand OO, nor appreciate the elegance of design patterns,
but so what? Out of 1000 there are 1 or 2 people that understand it,
and these are the people that will make the difference.

Resistance is futile. You will be (re)assimilated, soon or later. If
not, why are you still flying around this "dead body"? ;)

Emerson


On Sep 14, 10:51 am, docdw...@panix.com () wrote:
> In article <7h6v5sF4dla...@mid.individual.net>,
>
…[95 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-02T14:22:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7il2ubF31u7vaU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <ac80b3cf-f68f-4ccb-b064-a3472b17a7e1@33g2000vbe.googlegroups.com>`

```
Emerson wrote:
> Come on, Pete...admit, you miss that time when you had happiness
> coding nice things that no one have seen before in Cobol.

I responded on this very point before I read your post... :-)


>The very
> first time that you created a Window in character mode,

That was under Windows 3.1 using Micro Focus COBOL. I used a Screen section 
and have never used it since... I can't think when it was and  the pentium 3 
laptop with it all on is packed away in storage, but I would estimate late 
eighties. I moved to Panels and Dialog very quickly. Then switched to 
Fujitsu (after the VISOC debacle) and PowerCOBOL (which was infinitely 
better).



> the first time
> that you added mouse support to your apps, the frustrating windows API
> study,

I LOVED winAPI ! (Not that I would get emotional about computer software, 
you understand... :-))  I started programming in 1965 in very low level 
assembler (on various "mini-computers" and mainframes) and spent the first 
couple of years of my career writing low-level code. WinAPI was natural for 
me.

> being ahead of time, until you saw OO in Cobol and said, this
> is great, but I do not want to code thousands of lines to get GUI
…[3 more quoted lines elided]…
> finally I left Cobol for ASP, Java, C# and other stuff.

I'm sure many people followed a similar path to both of us.


> I also spent a
> lot of time feeling angry about the laziness of Cobol's developers
> everywhere (they simply seems like frogs that don't try to escape even
> when the water temp raises until boiling point).

I got angry with the Standards committee when it took 17 years to produce 
COBOL 2002, and I got annoyed and frustrated with people in this group who 
seemed to pour scorn and ridicule on new ideas, but I soon got over it. I 
came to realize that people who say: "Everything I want to do I can do in 
COBOL..." simply have very limited viewpoints... I also became quite excited 
by stuff I was doing myself using OO COBOL components and started to realize 
the fantastic implications of component based systems.


>Now I know that this
> community is formed by people that only common attribute is being
> target of prejudice everywhere,

I'm not sure that's fair... I found much more interest and courtesy from 
non-COBOL people when I discussed what COBOL could do with them, than I 
found in this COBOL group when I tried to discuss new concepts and ideas. I 
think the prejudice is two way, not one way. It is also fair to say, that 
with the passage of time, we have all grown, and things are much better here 
now as people are realising from experience in their workplaces that "new 
technology" isn't going to go away and the days of COBOL being the "Only 
game in town" are long gone. I'm also more mature and (hopefully...) less 
brash than I once was so I think it all helps... :-) (It took 20 years, but 
I guess I'm a slow learner... :-))


> and to be honest many of them will
> never understand OO, nor appreciate the elegance of design patterns,
> but so what?

I agree, it doesn't matter. But the sad reality is that it doesn't matter 
because COBOL doesn't matter.


>Out of 1000 there are 1 or 2 people that understand it,
> and these are the people that will make the difference.

...or not. :-)

>
> Resistance is futile. You will be (re)assimilated, soon or later. If
> not, why are you still flying around this "dead body"? ;)

You make a good point, but I have worked with COBOL for so long I wouldn't 
just not be interested overnight. COBOL was good to me. It fed me, clothed 
me, and took me all over the planet, where I had some amazing experiences. I 
am not so shallow as to fail to give recognition to a seminal influence in 
making me what I am. For most of us, our work is a very important part of 
our lives (in fact, it takes many years for some people to realize that they 
are NOT defined by their work, and are just as "important" as people, 
whether they are working or not), and it shapes and helps to make us 
whatever we become.

I'm quite sure I would be a completely different person, if I had followed a 
completely different career. Perhaps the underlying traits and attitudes are 
there anyway, but work experience and interactions in the workplace DO have 
effects on most of us.

So, it is natural I would retain an interest in COBOL, even though I don't 
personally write much of it any more.

More importantly (for me at least) is the fact that this is an unmoderated 
Newsgroup. That makes it one of the last bastions of Free Speech on our 
planet. No vested interests (sponsors), no political affiliations, just 
people saying what they think. It never ceases to amaze me and you have no 
idea how much I appreciate this. Sometimes it is tedious and pedantic, 
sometimes it is abusive, sometimes it is just silly, but there are pearls of 
wit and wisdom that come out of comp.lang.cobol, which make me keep coming 
here. I've always said I'd be posting as long as it is fun and it is still 
fun.

Over the years sacred cows like religion and politics have been debated at 
length here; minds may not have been changed but insights have certainly 
been gained. It is a privelege to have a community of generally bright, 
thinking people, giving their views on the world. For that reason I often 
enjoy the OT posts more than the other ones, although I have tried to 
contribute to both.

A small community of people all tied together by a shared interest in COBOL.

If COBOL never did anything else, it could justify its existence by that 
alone. :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 11)_

- **From:** Robert Doerfler <rocrash@gmx.de>
- **Date:** 2009-10-02T07:25:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ilo7jF321useU1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <ac80b3cf-f68f-4ccb-b064-a3472b17a7e1@33g2000vbe.googlegroups.com> <7il2ubF31u7vaU1@mid.individual.net>`

```
> I LOVED winAPI ! (Not that I would get emotional about computer
> software, you understand... :-))  I started programming in 1965 in very
> low level assembler (on various "mini-computers" and mainframes) and
> spent the first couple of years of my career writing low-level code.
> WinAPI was natural for me.

Oh, my goodness! How could WinAPI be natural to someone even assembler
(ibm/370, pdp) is more comfortable than WinAPI.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-03T03:26:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7imgsdF32m6b6U1@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <ac80b3cf-f68f-4ccb-b064-a3472b17a7e1@33g2000vbe.googlegroups.com> <7il2ubF31u7vaU1@mid.individual.net> <7ilo7jF321useU1@mid.individual.net>`

```
Robert Doerfler wrote:
>> I LOVED winAPI ! (Not that I would get emotional about computer
>> software, you understand... :-))  I started programming in 1965 in
…[5 more quoted lines elided]…
> (ibm/370, pdp) is more comfortable than WinAPI.

I learned and wrote Autocoder for IBM 1401s, BAL for 360, PLAN for ICL 1900, 
COMPASS for CDC Cybers, NEAT for NCR 315 (the original NEAT before it became 
NEAT 3 for Century series),  Burroughs B500 Assembler, and both Motorola 
(not much of this) and Intel 8086 Assembler (tons of it before COBOL became 
readily available for PCs). Using Macros in these facilities (when Macros 
became available) was a very good grounding for interfacing to WinAPI.  When 
you've hooked interrupt vectors and written TSRs for PCs, interfacing to 
WinAPI is a doddle. I never said WinAPI was more comfortable than the 
Assemblers, I simply observed that WinAPI was not a problem for me.

YMMV.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL: It's Everywhere... but going Nowhere....

_(reply depth: 13)_

- **From:** Robert Doerfler <rocrash@gmx.de>
- **Date:** 2009-10-04T12:47:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7irjrtF323ivbU3@mid.individual.net>`
- **References:** `<edeaf1d5-12b1-4bbb-b52d-069c49ef40ea@r33g2000vbp.googlegroups.com> <7h30oeF2pakqpU1@mid.individual.net> <h8lecv$bmk$1@reader1.panix.com> <7h6v5sF4dla6U1@mid.individual.net> <h8llab$6bj$1@reader1.panix.com> <ac80b3cf-f68f-4ccb-b064-a3472b17a7e1@33g2000vbe.googlegroups.com> <7il2ubF31u7vaU1@mid.individual.net> <7ilo7jF321useU1@mid.individual.net> <7imgsdF32m6b6U1@mid.individual.net>`

```
> Robert Doerfler wrote:

> (...)
> I never said WinAPI was
> more comfortable than the Assemblers, I simply observed that WinAPI was
> not a problem for me.

... ok, ok. But "loving" it sounds quite extrem ;)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
