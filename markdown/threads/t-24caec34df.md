[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# News for COBOL Migrations

_11 messages · 4 participants · 2021-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### News for COBOL Migrations

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-01-07T21:43:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5pv77FbpiU1@mid.individual.net>`

```
With the beginning of a new year and very little happening on the
Migration front during the last one, I decided to knock down the PRIMA
site and move to some other things I have been thinking about.

I'm not happy with the information I can get from Google analytics so I
decided to write my own web traffic analysis for
https://primacomputing.co.nz

This was a fun thing to do (and I am enjoying it immensely as it goes on
and each day brings a new facility I suddenly realized I wanted... :-))
but some of the information it revealed has made me think again.
(I'm writing it in C# with SQL Server and it targets .NET 4+)

I was seriously underestimating traffic to the site and not even
bothering to check the overall visits. Last time I looked it was around
20,000 hits; today it is 61014 with 250 hits in the last 4 days...
I usually expect about 15 hits a day, so this is very interesting.
I have no idea why there has been a surge; I haven't DONE anything.
Maybe Covid lockdown has got people bored and they are visiting sites
that they normally wouldn't... :-)

I can now get the information I want, instantly, and it is going to a
SQL Server DB so I can dice and slice it any way I want.

How many hits on any given page or overall during any given period?

What are people most interested in looking at?

Which pages are trending and which declining?

Am I investing effort into things that no-one is interested in?

As a result, I'm going to attend to the site and streamline and focus it
much better.

It will take me a few months to do this, but when it is finished there
will be better videos showing the Migration of Standard COBOL away from
indexed files to an optimized RDB with a tiered architecture for running
on the network, and the capability to operate with other modern
languages, layers and objects.

The old (legacy) COBOL is automatically transformed into OO COBOL and
the new Classes can run as objects for other languages if required. 100%
salvage of legacy code is guaranteed and it can be automatically
refactored into objects that will require minimum maintenance, (so the
impact of decreasing COBOL skill availability is lessened). Both old and
new technology can share the same databases using a generated DAL layer
or direct ESQL, and eliminating the need for overnight batch runs to
synchronize files between old and new technologies and languages.

PowerCOBOL migration is even more urgent for many people and we can do
it. Use our tools yourself or outsource the migration to us. We can
salvage 100% of your existing PowerCOBOL codebase, the sheets and the
scriptlets, and turn it into a standard .NET Windows Forms application.
Dependency on PowerCOBOL is completely removed and you get OO COBOL
Classes that are maintained in the usual way, and PowerCOBOL Forms that
recognize the same controls and events as your old PowerCOBOL sheets.
(You maintain them as Windows Forms with Visual Studio just like the
rest of the World does; you're no longer out on a limb...)

We are also considering the conversion of mainframe CICS and IMS/DC 3270
screens to WinForms in very much the same way. I'd be interested in
talking to anyone on a mainframe site about this.

BOTTOM LINE:

Fully automated migration of legacy COBOL (all flavors, mainframe, mini,
PC) and Fujitsu PowerCOBOL to .NET, is now possible with over 90%
automated tools and 100% of the legacy salvaged and modernized.

Keep an eye on the PRIMA web site for further developments...

Pete.
I used to write *COBOL*; now I can do *anything*...
```

#### ↳ Re: News for COBOL Migrations

- **From:** "vbcoen" <ua-author-14501880@usenetarchives.gap>
- **Date:** 2021-01-08T07:49:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p2@usenetarchives.gap>`
- **In-Reply-To:** `<i5pv77FbpiU1@mid.individual.net>`
- **References:** `<i5pv77FbpiU1@mid.individual.net>`

```
Hello pete!

Friday January 08 2021 02:43, pete dashwood wrote to All:

> With the beginning of a new year and very little happening on the
> Migration front during the last one, I decided to knock down the PRIMA
> site and move to some other things I have been thinking about.

> I'm not happy with the information I can get from Google analytics so
> I decided to write my own web traffic analysis for
> https://primacomputing.co.nz


.....


> I was seriously underestimating traffic to the site and not even
> bothering to check the overall visits. Last time I looked it was
…[4 more quoted lines elided]…
> visiting sites that they normally wouldn't... :-)


If you look at the logs you may well find it is search engines taking a
look at site content. I get it on a regular basis although I have reduced
it as now using robots.txt at various points traffic has reduced for the
one's doing it hourly.


Vincent
```

##### ↳ ↳ Re: News for COBOL Migrations

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-01-08T17:26:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p2@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p2@usenetarchives.gap>`

```
On 9/01/2021 01:49, Vincent Coen wrote:
› Hello pete!
› 
…[31 more quoted lines elided]…
› 
Thanks Vince.

I did look over the logs and some of it is definitely that.

I'm going to continue and refurbish the site anyway, though.

Pete.

I used to write *COBOL*; now I can do *anything*...
```

#### ↳ Re: News for COBOL Migrations

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2021-01-08T13:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p4@usenetarchives.gap>`
- **In-Reply-To:** `<i5pv77FbpiU1@mid.individual.net>`
- **References:** `<i5pv77FbpiU1@mid.individual.net>`

```
In article ,
pete dashwood wrote:

[snip]

› The old (legacy) COBOL is automatically transformed into OO COBOL and 
› the new Classes can run as objects for other languages if required. 100% 
› salvage of legacy code is guaranteed and it can be automatically 
› refactored into objects that will require minimum maintenance, (so the 
› impact of decreasing COBOL skill availability is lessened).

Has anyone beside me had the joy of sitting in on conference-calls for
'lift and shift' and having to explain what match/merge processing is?

'Why didn't they use SQL?'

'It wasn't widely available then.'

'So where do I find a description of the table?'

'There aren't any tables. It's all done with files.'

'So how do you get the name and address for an employee-number?'

'In this application it's done by match/merge procesing.'

'You need to be more specific.'

'The concepts are fairly simple but it usually takes a week or two to get
comfortable with the concepts.'

'We don't have that much time.'

'Your schedule isn't my responsibility.'

'So... how are you going to help us?'

'By suggesting you learn more, first, and then ask questions.'

'That's not very helpful.'

'It is to people who understand the necessity of time and education.'

... and it goes downhill from there... but what do I know, I was only
doing this - and more! - before their parents met.

DD
```

##### ↳ ↳ Re: News for COBOL Migrations

- **From:** "vbcoen" <ua-author-14501880@usenetarchives.gap>
- **Date:** 2021-01-08T16:13:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p4@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap>`

```
Hello docdwarf!

Friday January 08 2021 18:11, you wrote to All:

> In article ,
> pete dashwood wrote:

> [snip]

>> The old (legacy) COBOL is automatically transformed into OO COBOL and
>> the new Classes can run as objects for other languages if required.
>> 100% salvage of legacy code is guaranteed and it can be automatically
>> refactored into objects that will require minimum maintenance, (so
>> the impact of decreasing COBOL skill availability is lessened).

> Has anyone beside me had the joy of sitting in on conference-calls for
> 'lift and shift' and having to explain what match/merge processing
> is?


snip....

> 'It is to people who understand the necessity of time and education.'

> .... and it goes downhill from there... but what do I know, I was only
> doing this - and more! - before their parents met.

This is the generation of the university education that was never geared
for the 'real' world.

It hasn't change since the 70's and when going fo the odd interview in the
80's got the odd - 'so why have you NOT got a degree.

Despite my CV showing I was in at the sharp end from 1963 full time and 61
PT.

Mind you the saying sucking eggs comes to my attention :)


Vincent
```

###### ↳ ↳ ↳ Re: News for COBOL Migrations

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2021-01-08T22:12:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p5@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap> <gap-24caec34df-p5@usenetarchives.gap>`

```
In article <161··6@f1.··t.ftn>,
Vincent Coen wrote:
› Hello docdwarf!
› 
› Friday January 08 2021 18:11, you wrote to All:
 
› [snip]
 
›› 'It is to people who understand the necessity of time and education.'
› 
…[4 more quoted lines elided]…
› for the 'real' world.

I was taught that a university education was for the learning and a
technical school was for a trade... but maybe things have changed.

› It hasn't change since the 70's and when going fo the odd interview in the
› 80's got the odd - 'so why have you NOT got a degree.
› 
› Despite my CV showing I was in at the sharp end from 1963 full time and 61
› PT.

My own BA is in Liberal Arts from a tiny, toy school that took the Trivium
and the Quadrivium rather seriously. I remember waking up one morning,
rolling over and firing up a cigarette... and I looked through the
tendrils of smoke at the volumes on my college-kid cot, Descartes,
Maxwell, Newton, Rousseau...

... and thought 'I've shared my bed with some of the greatest minds the
world has seen.'

Learning is difficult, joyful work.

DD
```

###### ↳ ↳ ↳ Re: News for COBOL Migrations

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2021-01-10T09:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p6@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap> <gap-24caec34df-p5@usenetarchives.gap> <gap-24caec34df-p6@usenetarchives.gap>`

```
On 1/8/21 10:12 PM, doc··f@pa··x.com wrote:
› In article <161··6@f1.··t.ftn>,
› Vincent Coen  wrote:
…[15 more quoted lines elided]…
› technical school was for a trade... but maybe things have changed.

They have been arguing this since the early 19th century. I used to
work at a Jesuit University. we had a "self evaluation" done once. A
certain Jesuit who was on the investigative committee argued that we
should not be teaching Computer Science because that belonged in a
trade school. He came from Georgetown where they turn out 10 times
as many lawyers as we did computer scientists.


› 
›› It hasn't change since the 70's and when going fo the odd interview in the
…[14 more quoted lines elided]…
› Learning is difficult, joyful work.

I also went to a Liberal Arts College. And my degree is in Liberal
Studies. But, it is still quite useful. My concentrations were
German, Theology and Computer Science. And, it turns out, I have
one course short of a Theology Major. More German Credits than a
German Major. And more Computer Science Credits than a CS Major.
As well as all the Liberal Arts Courses like Philosophy, English,
Literature, etc.

Go figure.

bill
```

###### ↳ ↳ ↳ Re: News for COBOL Migrations

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2021-01-10T11:18:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p7@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap> <gap-24caec34df-p5@usenetarchives.gap> <gap-24caec34df-p6@usenetarchives.gap> <gap-24caec34df-p7@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:
› On 1/8/21 10:12 PM, doc··f@pa··x.com wrote:
›› In article <161··6@f1.··t.ftn>,
…[18 more quoted lines elided]…
› They  have been arguing this since the early 19th century.

Not only did the They argue this, Mr Gunshannon... They built it into the
English language. In order to go to school one needs leisure (L.,
scholium).

› I used to
› work at a Jesuit University.  we had a "self evaluation" done once.  A
…[3 more quoted lines elided]…
› as many lawyers as we did computer scientists.

Jesuits are a... frightening crew. (long ago it ocurred to me that
Benedictines reminded me of Jesuits in their devotion to learning... but
the Benedictines did not have the Certainty of Righteousness held by God's
Soldiers). That said... I'm guilty, here, of using the language
established in the conversation and neglecting specifics.

In the Oldene Dayse a baccalaureate degree was earned in a college and a
university was for more advanced studies, producing Masters and Doctors.
(technical schools stay where they are).

Lawyers that you mention above are doctors (in that they earn a degree of
Juris Doctor) after a baccalaureate degree.

Computer science is a new field and a broad term... folks designing new
languages, operating systems and architectures need a lot of groundwork
before they can start t make really good Professionam Mistakes while
slinging COBOL well enough to change a column in a report need less.

(yes, there are folks who say 'I wrote a new compiler over the weekend';
these are exceptions)

So perhaps as a Bachelor of Science in Chemistry candidate is required to
duplicate old, established experiments in order to understand the work to
come - how do you determine the atomic weight of sulfur? - so a Computer
Science candidate need to learn machine language, Assembley, what sort
should be used for what kinds of data and disorganisation... but neither
should neglect grammar, rhetoric, logic, arithmetic, geometry, music and
astronomy.

*Especially* music.

(oh... and the Georgetown Jesuit you mention was probably sent out on the
evaluation team because they didnt want him being a nuisance at the Home
Office)

› 
› 
…[26 more quoted lines elided]…
› Go figure.

If it all made sense already, Mr Gunshannon, there'd be less to learn and
love. Happy New Year!

DD
```

##### ↳ ↳ Re: News for COBOL Migrations

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-01-08T17:58:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p4@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap>`

```
On 9/01/2021 07:11, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[45 more quoted lines elided]…
› 
Thanks Doc,

I enjoyed the transcript... :-)

I've encountered similar lack of understanding when they want to move to
RDB.

They don't understand the new technology and they either don't have the
time or inclination to learn about it, but they want it.

Gently ask them why they want it and the response is usually that their
competitors have it or "everybody knows" RDB is "better" than flat
files. (It isn't always, of course, and there have been a few rare
occasions where we deliberately did not migrate certain files during a
large migration.)

Basically people don't like change and resist it vehemently. But they
don't like being seeing to be archaic either, so they want the latest.

There is seldom a judgement based on the innate advantages of a new
technology; the reasons for adopting are mostly fashion and social
pressure, often driven by sales conferences.

We had one client who wanted to migrate and eventually move off COBOL
altogether. You might think they had done some investigations and
decided a technical road map to a better future.

Not a bit of it. The salesman had got sick of being embarrassed by
answering the questions: "What's your package written in?" (COBOL), and,
"What database are you using? (indexed files). The opposition invariably
had an RDB and wrote in Java, Python, or C#... His prospects looked down
their noses at him and the sale was lost.

It's like no-one cared about the functionality (and the package was
really very good functionally); they were losing sales because of
fashion and buzzwords.

We did some POCs (Proof of concept) for them and when they realized the
amount of effort that would be involved and the pressure that migration
would put on their limited tech resources (even with the tools), they
decided to wait. We discussed them outsourcing the job to us, but even
spreading the cost and keeping it low for them, it is a big commitment
for a small business.

Currently, they are trying to get cloud based. For no good technical
reason. (again it is about keeping up with the Joneses.) The cost of a
VM in the cloud for each of their clients is too prohibitive, so I
looked at using Cloud based containers which cost less to run. We could
have converted their COBOL package to .NET and run it in the cloud.
Unfortunately, because you can't run a Windows Forms application in a
Docker container, this is currently non-viable. So they are waiting
until the cost of cloud VMs comes down or Docker Containers receive
support for Win Forms applications...

There are some very good reasons to migrate from COBOL, but there are a
lot of very bad reasons too.

Pete.

I used to write *COBOL*; now I can do *anything*...
```

###### ↳ ↳ ↳ Re: News for COBOL Migrations

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2021-01-08T18:24:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p9@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap> <gap-24caec34df-p9@usenetarchives.gap>`

```
On 1/8/21 5:58 PM, pete dashwood wrote:
› On 9/01/2021 07:11, doc··f@pa··x.com wrote:
›› In article ,
…[64 more quoted lines elided]…
› don't like being seeing to be archaic either, so they want the latest.

This looks like a good place to throw in one of my (many) examples
along this line.

I was hired to maintain and make updates to some COBOL programs.
After the updates were caught up I had some time to actually look
thru some of the other COBOL programs.

Realize, this place was really proud of the project that had moved
them from flat files to a real database. They thought the people
who had done all this walked on water.

Imagine my surprise when I found a couple of the programs modifications
consisted of reading the database, writing the data to a flat file and
then using the previous code to process the flat file. My peers there
used to wonder why I spent so much time laughing in my cubicle.

And we won't even go into what happens when all your calculations are
done using unsigned intermediate variables.

bill
```

###### ↳ ↳ ↳ Re: News for COBOL Migrations

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-01-08T21:43:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24caec34df-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24caec34df-p10@usenetarchives.gap>`
- **References:** `<i5pv77FbpiU1@mid.individual.net> <gap-24caec34df-p4@usenetarchives.gap> <gap-24caec34df-p9@usenetarchives.gap> <gap-24caec34df-p10@usenetarchives.gap>`

```
On 9/01/2021 12:24, Bill Gunshannon wrote:
› On 1/8/21 5:58 PM, pete dashwood wrote:
›› On 9/01/2021 07:11, doc··f@pa··x.com wrote:
…[90 more quoted lines elided]…
› 
Thanks Bill,

Has to be one of the best "war stories" I ever heard. :-)

I tried to imagine WHY they would do that and I could only think that
the existing code was such a mess they DARE not try and sort it out.

I'm pleased to say that our tools could have refactored this for them
AND replaced all the IO code with invokes of methods in a generated DAL
layer. No need for "double dipping" and all existing logic processing
100% as before.

I'm a big fan of separation (especially for data access)...
[https://primacomputing.co.nz/primametro/ObjectsandLayers2.aspx]

Pete.
I used to write *COBOL*; now I can do *anything*...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
