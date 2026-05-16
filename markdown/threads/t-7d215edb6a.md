[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Conversion of Spaghetti cobol code to Structured COBOL code....

_25 messages · 12 participants · 2002-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** satyam_satyam@hotmail.com (Satyam)
- **Date:** 2002-07-11T04:24:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
Has anybody used any conversion tool to make the Spaghetti COBOL code
to a Structured COBOL code (on IBM OS/390)? I heard that there is tool
from CA called VISION:Recode. Are there any other similar tools
available? What are the merits & demerits of these tools? What level
of testing is needed after conversion? Does the conversion code need
any manual intervention? Does it increase the performance of the
programs and savings interms of CPU time etc., How much of effort is
required to carry on this task?
Please help. Thanks a lot in advance.

Best Regards, Satyam.
```

#### ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** "Larry Kahm" <lkahm@bellatlantic.net>
- **Date:** 2002-07-11T12:39:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o0fX8.31536$5f3.12998@nwrddc01.gnilink.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
If you were interested in an IBM solution, you could have used the COBOL
Structuring Facility.

It would revamp existing code to a structured format - you would set the
guidelines by which it operated.  Manual changes would still probably be
required in some instances.

Advantage - code that is standardized is easier to maintain (provided the
developers understand and adhere to the guidelines).

Disadvantage - if anyone clearly understood the old, unformatted code, they were
usually not likely to be happy with the results.

Any change to any program requires a degree of testing - this is certainly no
exception.

http://www2.ibmlink.ibm.com/cgi-bin/master?xh=J3tobiLEPDrGd42USenGnN9332&request
=salesmanual&parms=H%5f5696%2d737&xhi=usa%2emain%7csalesmanual%5e&xfr=N

It seems that this product is no longer available - no replacement seems to be
evident.

Larry Kahm
```

#### ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** docdwarf@panix.com
- **Date:** 2002-07-11T08:59:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agjvg3$mtq$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
In article <fd149d96.0207110324.1165aaca@posting.google.com>,
Satyam <satyam_satyam@hotmail.com> wrote:
>Has anybody used any conversion tool to make the Spaghetti COBOL code
>to a Structured COBOL code (on IBM OS/390)? I heard that there is tool
…[6 more quoted lines elided]…
>Please help. Thanks a lot in advance.

Please do your own job.

DD
```

##### ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2002-07-12T05:23:59+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2DDB4F.E0CA429A@melbpc.org.au>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> In article <fd149d96.0207110324.1165aaca@posting.google.com>,
…[13 more quoted lines elided]…
> DD

IMHO that was a perfectly reasonable question.

My 2c worth... I have found these tools to be not useful. Minor format fixing
programs (beautifiers) are very useful, but restructuring spaghetti code
automatically seems to result in hard to follow code. 

Tim Josling
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** docdwarf@panix.com
- **Date:** 2002-07-11T16:02:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agko8o$6en$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au>`

```
In article <3D2DDB4F.E0CA429A@melbpc.org.au>,
Tim Josling  <tej@melbpc.org.au> wrote:
>docdwarf@panix.com wrote:
>> 
…[16 more quoted lines elided]…
>IMHO that was a perfectly reasonable question.

Well... 'reasonable' is, quite obviously, open to interpretation... and my 
Drill Sergeant taught me something about comparing opinions and a certain 
body part... but hey, if I want only agreement then I would speak only 
with my mirror.

It sounded to me like a 'do my homework for me' question involving some 
rather intricate issues; there is no indication whatsoever that the 
inquirer has expended any effort on his own, even to the point of 
contacting the company to verify 'what I heard'.

What restructuring tools are available?  A few, here and there.  What kind 
of system needs restructuring? How large a staff supports it?  What's the 
technical expertise available in-house?  'Savings in terms of CPU time 
etc.'... smells like a fishing-expedition.

>
>My 2c worth... I have found these tools to be not useful. Minor format fixing
>programs (beautifiers) are very useful, but restructuring spaghetti code
>automatically seems to result in hard to follow code. 

What... you mean that paragraph names like 
A751269-C5100-REFORMAT-GL600-REC aren't intuitively obvious?

DD
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 4)_

- **From:** "Larry Kahm" <lkahm@bellatlantic.net>
- **Date:** 2002-07-11T21:09:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xumX8.32767$5f3.4003@nwrddc01.gnilink.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com>`

```
<<It sounded to me like a 'do my homework for me' question >>

That's fair.  Although, I thought it sounded like preparation for a job
interview question.

Needless to say, asking for immediate help to a vast topic - without explaining
the reasons why - seems to be prevalent this summer...

Larry Kahm
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-07-11T22:26:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agleo6$l1q$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net>`

```
In article <xumX8.32767$5f3.4003@nwrddc01.gnilink.net>,
Larry Kahm <lkahm@bellatlantic.net> wrote:
><<It sounded to me like a 'do my homework for me' question >>
>
>That's fair.  Although, I thought it sounded like preparation for a job
>interview question.

Also a possibility... if that were the case then it might have better to 
change 'please do your own job' to 'please study for your own job'.

>
>Needless to say, asking for immediate help to a vast topic - without explaining
>the reasons why - seems to be prevalent this summer...

That it does... speaking of which, can you tell me how light can be both a 
particle and a wave simultaneously?  How might this effect the measurement 
of small phenomena?  I have heard that a fellow named Heisenberg was 
uncertain about this; can anyone clarify this for me?

But... I'll tell you the reason why; it has nothing to do with work or 
jobs or anything like that... I'm just naturally curious about such 
things...

... oh, and I am the King of England, too.

DD
```

###### ↳ ↳ ↳ Re: [OT] Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-07-12T03:59:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CusX8.89962$p85.2446433@twister.austin.rr.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net> <agleo6$l1q$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:agleo6$l1q$1@panix1.panix.com...
> That it does... speaking of which, can you tell me how light can be both a
> particle and a wave simultaneously?  How might this effect the measurement
> of small phenomena?  I have heard that a fellow named Heisenberg was
> uncertain about this; can anyone clarify this for me?
>

Well, there are several good books out that provide popular explanations of string theory,
explanations without the math. It comes pretty darn close. And it is even starting to show
experimental results - they teleported a laser beam in Australia last month. :)

> But... I'll tell you the reason why; it has nothing to do with work or
> jobs or anything like that... I'm just naturally curious about such
…[3 more quoted lines elided]…
>

Stay curious, but stay out of the Tower of London then...
-Paul


> DD
>
>
```

###### ↳ ↳ ↳ Re: [OT] Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2002-07-12T05:56:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agm94h$laj$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net> <agleo6$l1q$1@panix1.panix.com> <CusX8.89962$p85.2446433@twister.austin.rr.com>`

```
In article <CusX8.89962$p85.2446433@twister.austin.rr.com>,
Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote:
>
><docdwarf@panix.com> wrote in message news:agleo6$l1q$1@panix1.panix.com...
…[8 more quoted lines elided]…
>experimental results - they teleported a laser beam in Australia last month. :)

Miracles of modern technology!  But tell me... is it my imagination or 
does the response of 'there are several good books out that provide... 
explanations' approximate at least the spirit - of not the entire practise 
- of 'please do your own homework/job'?

>
>> But... I'll tell you the reason why; it has nothing to do with work or
…[6 more quoted lines elided]…
>Stay curious, but stay out of the Tower of London then...

God save the Me!

DD
```

###### ↳ ↳ ↳ Re: [OT] Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 8)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-07-12T12:42:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2F06FA.9010300@optonline.NOSPAM.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net> <agleo6$l1q$1@panix1.panix.com> <CusX8.89962$p85.2446433@twister.austin.rr.com> <agm94h$laj$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <CusX8.89962$p85.2446433@twister.austin.rr.com>,
> Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote:
…[30 more quoted lines elided]…
> God save the Me!

Wouldn't that be "God Save My Majesty"?

PS: We are not amused.
```

###### ↳ ↳ ↳ Re: [OT] Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2002-07-12T13:56:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agn57k$mhb$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <CusX8.89962$p85.2446433@twister.austin.rr.com> <agm94h$laj$1@panix1.panix.com> <3D2F06FA.9010300@optonline.NOSPAM.net>`

```
In article <3D2F06FA.9010300@optonline.NOSPAM.net>,
Liam Devlin  <LiamD@optonline.NOSPAM.net> wrote:
>docdwarf@panix.com wrote:
>> In article <CusX8.89962$p85.2446433@twister.austin.rr.com>,
>> Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote:

[snippage]

>>>Stay curious, but stay out of the Tower of London then...
>> 
…[3 more quoted lines elided]…
>Wouldn't that be "God Save My Majesty"?

Not if We wanted the line to scan, no... and in order for My Majesty to be 
saved the whole of Me - or at least the part containing My Majesty - would 
have to be saved, as well.

>
>PS: We are not amused.

Hey, ain't nobody said that Life is Always a Bowl O' Chuckles... and if 
they did, they lied.

DD
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 5)_

- **From:** satyam_satyam@hotmail.com (Satyam)
- **Date:** 2002-07-11T21:40:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fd149d96.0207112040.2fa0d96c@posting.google.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net>`

```
"Larry Kahm" <lkahm@bellatlantic.net> wrote in message news:<xumX8.32767$5f3.4003@nwrddc01.gnilink.net>...
> <<It sounded to me like a 'do my homework for me' question >>
> 
…[6 more quoted lines elided]…
> Larry Kahm

Larry,

Sorry for my wordings... after I saw all your comments I realised what
I wrote. I was actually frustrated with the search and calls made to
differenet vendors on this topic. Nobody is aware of these kind of
tools except CA's VISION:Recode. CA is yet to respond to my queries. I
am trying to find out if there any other competitive tools available
in the market. The whole purpose of this is to make the existing code
a structured and easy maintainable. The programs has become so complex
to understand as for the past 15 years many had laid hands on it and
played with it. Now I am finding out ways to make it maintainable. It
is a huge task to take it up manually (instead we can develop a new
code..:-). Hope you understand my situation.

-Satyam.
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 6)_

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-07-12T22:44:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2F5BC0.DAD3A7BD@boeing.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <xumX8.32767$5f3.4003@nwrddc01.gnilink.net> <fd149d96.0207112040.2fa0d96c@posting.google.com>`

```


Satyam wrote:
> in the market. The whole purpose of this is to make the existing code
> a structured and easy maintainable. The programs has become so complex
…[3 more quoted lines elided]…
> code..:-). Hope you understand my situation.


You will get a much better product with a thoughtful review of the code
you have, develop your rules and standards and hire (1 or more)
experienced programmers to do it properly - a really good analyst will
also be of enormous assistance as will a committed customer.

Old code may have useless processes, patches in the wrong location in
the data stream, work arounds for new rules; out dated rules; code best
used in a table; code better used out of a table and so forth.

In your case, manual will be far better then any conversion routine, as
you must get the logical structure functioning cleanly.  The one time I
saw conversion code it failed to identify duplicate logical routines
and  other obvious code inefficiencies (it was structured); it failed to
address a code 'fall through' and replicated some unwanted structures.


	Susan A
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 4)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2002-07-13T05:35:18+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2F2F76.C0588FA0@melbpc.org.au>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> >IMHO that was a perfectly reasonable question.
…[10 more quoted lines elided]…
> 

It may well be someone trying to get us to do their homework for them. But it
may not (in July?). I am more conservative than others in my view of the
extent to which I can read others' minds. 

I thought in any case it was a question of general interest regardless of the
possible motives of the author.

My own experience in this regard is in translating programs from one language
to another, which tends also to produce unless and unreadable code.

Tim Josling
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-07-12T16:07:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agncu8$mi5$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <3D2F2F76.C0588FA0@melbpc.org.au>`

```
In article <3D2F2F76.C0588FA0@melbpc.org.au>,
Tim Josling  <tej@melbpc.org.au> wrote:
>docdwarf@panix.com wrote:
>> 
…[14 more quoted lines elided]…
>may not (in July?).

Homework is not always the result of academic assignments; it may be 
work-related... hence the request of 'Please do your own job'.

>I am more conservative than others in my view of the
>extent to which I can read others' minds. 

I made no claim of mindreading abilities... note the use of 'it sounded to 
me'.

>
>I thought in any case it was a question of general interest regardless of the
>possible motives of the author.

You had, of course, your own reasons or coming to your conclusions... as I 
had in coming to mine.

>
>My own experience in this regard is in translating programs from one language
>to another, which tends also to produce unless and unreadable code.

My own experience is in writing useless and unreadable code from the 
ground up... who needs structuring programs?

DD
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 6)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2002-07-13T06:19:05+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2F39B9.7A817A67@melbpc.org.au>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3D2DDB4F.E0CA429A@melbpc.org.au> <agko8o$6en$1@panix1.panix.com> <3D2F2F76.C0588FA0@melbpc.org.au> <agncu8$mi5$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> I made no claim of mindreading abilities... note the use of 'it sounded to
> me'.

Not in your original response. That was pretty black and white.

Tim Josling
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2002-07-12T21:46:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ago0pb$irl$1@panix1.panix.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3D2F2F76.C0588FA0@melbpc.org.au> <agncu8$mi5$1@panix1.panix.com> <3D2F39B9.7A817A67@melbpc.org.au>`

```
In article <3D2F39B9.7A817A67@melbpc.org.au>,
Tim Josling  <tej@melbpc.org.au> wrote:
>docdwarf@panix.com wrote:
>> 
…[3 more quoted lines elided]…
>Not in your original response. That was pretty black and white.

My original response was, if I recall correctly, 'Please do your own job'.  
If a claim of mindreading can be interpreted from this it might be 
interesting to see the methodology behind it.

DD
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-07-12T03:56:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2E5351.81ADC8D8@worldnet.att.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <agjvg3$mtq$1@panix1.panix.com> <3D2DDB4F.E0CA429A@melbpc.org.au>`

```
Tim Josling wrote:
> (snip) 
> My 2c worth... I have found these tools to be not useful. Minor format fixing
…[3 more quoted lines elided]…
> Tim Josling

I had some experience with IBM's mainframe CSF (COBOL Structuring
Facility).  I would have to say I was a little disappointed.  The
product worked very well at eliminating GO TO and ALTER statements,
which has some value.  For very bad cases of PERFORM...THRU it would
generate working-storage flags to control PERFORM branching in the
generated program.  "Performed by..." comments could be automatically
generated.  CSF could also do some "beautification" and enforce
standard alignment.

I used it convert a couple of real stinkers and installed them into
production.  In general, there would be fewer paragraph names in the
generated program than in the original spaghetti code source file. 
Paragraph names that were eliminated could optionally be propogated as
comments in the target program.  And quite often CSF found large
chucks of dead code in the procedure division that it could not
propogate to the target program.

The biggest difficulty was that uninformative data names and procedure
names were still uninformative in the target program.  The generated
program could be improved even more by an experienced programmer. 

Naturally, I tested every program I converted, and never found a bug
caused by the automated restructuring itself.  My shop eventually
stopped paying for CSF because we weren't using it enough.  But it was
very good at getting rid of GO TO's and ALTER's.
```

#### ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** Alistair Maclean <ld50macca@ld50macca.demon.co.uk>
- **Date:** 2002-07-11T15:11:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rd9N9AAgIZL9EwG4@ld50macca.demon.co.uk>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
a LONG TIME AGO I looked at this problem and found that CSF (IBM's
product) produced a result that I considered to be poor (personal
preference). Compuware (Namics I think they are now) produced a program
(the name of which escapes me but it began with X) which came up with
better results. However, it was damnably expensive.

In article <fd149d96.0207110324.1165aaca@posting.google.com>, Satyam
<satyam_satyam@hotmail.com> writes
>Has anybody used any conversion tool to make the Spaghetti COBOL code
>to a Structured COBOL code (on IBM OS/390)? I heard that there is tool
…[8 more quoted lines elided]…
>Best Regards, Satyam.
```

#### ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-07-11T20:42:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2E25F2.7040206@optonline.NOSPAM.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
Satyam wrote:
> Has anybody used any conversion tool to make the Spaghetti COBOL code
> to a Structured COBOL code (on IBM OS/390)? I heard that there is tool
…[8 more quoted lines elided]…
> Best Regards, Satyam.

I did a lot of work restructuring COBOL pgms in 1989-90. The best tool 
in my experience was RETOOL from CDSI in Rockville, MD. I just did a 
little Google search and it seems CDSI is now known as: ACS Government 
Solutions Group, Inc.

HTH
```

#### ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** "Deborah Torrekens" <deborah@phidani.be>
- **Date:** 2002-07-26T17:43:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d416ecc$0$30453$afc38c87@sisyphus.news.be.easynet.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com>`

```
Satyam,

RainCode http://www.raincode.com has a very efficient COBOL refactoring
technology.
RainCode's approach is to take the COBOL code and renovate it through the
application of automatic improvements.
The re-structuring of the code is done by applying a sequence of passes on
the source, among which:

- Replacing GO TO's by equivalent, but structured constructs.
- Removal of dead components.
- Loop detection and transformation into PERFORM statements.
- Cosmetic enhancements such as: systematic indentation, adding the optional
reserved words (THEN, END-IF, etc.).

Each step can take advantage of the result of the other steps, incrementally
rising the "abstraction level'' of the code.

This method proves to be advantageous in many ways.
- Executability is guaranteed. The risk of error is quite low. If an error
were made, it would be infinitely repeated through the automatic process,
which means that the probability of not catching it is close to null.
- Semantic equivalence between the initial code and the renovated code is
guaranteed.
- The process can be applied at will, even after potential manual changes
were made; improvements can be made incrementally.
- There is no eclipse effect: the program continues to run during the
renovation process, and can be tested at any time.

As of today RainCode offers the renovation as a service, and not as a tool.

Please, don't hesitate to contact me if you need more information.
Best regards,

Deborah Torrekens
PS: check out DVV Insurance's story at: http://www.raincode.com/dvv.htm

"Satyam" <satyam_satyam@hotmail.com> wrote in message
news:fd149d96.0207110324.1165aaca@posting.google.com...
> Has anybody used any conversion tool to make the Spaghetti COBOL code
> to a Structured COBOL code (on IBM OS/390)? I heard that there is tool
…[8 more quoted lines elided]…
> Best Regards, Satyam.
```

##### ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** _computer_consultant_@_mindspring_._com_ (nospam)
- **Date:** 2002-07-26T19:21:28+00:00
- **Newsgroups:** comp.lang.cobol,us.issues.occupations.computer-programmers
- **Message-ID:** `<3d41a043.11522274@nntp.mindspring.com>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3d416ecc$0$30453$afc38c87@sisyphus.news.be.easynet.net>`

```
In responce to the post:
 On Fri, 26 Jul 2002 17:43:38 +0200, "Deborah Torrekens"
<deborah@phidani.be> stated...and I replied:

>Satyam,
>
…[49 more quoted lines elided]…
>
Does anyone else see a problem here?  Spaghetti code is a result of
inexperienced programmers writing code that may work but does not
incorporate structured programming techniques.  RainCode would
probably not be needed if programmers used structured programming
standards.

I've had to unravel code written first with a lack of understanding
for database currency and retrieval, and after 26 other programmers
(the source code included fix reports) tried to fix it and (without
fixing the root DB retrival problem) failed.

Now I'm not saying that any specific race is at fault, but this shop
had a high percentage of Indian cobol programmers on the H1B visa
program.  This group was trained and sent to fill positions in IT
departments as low cost, inexperienced, resources.

It was this group that had spent 26 programmers, to fail at fixing
this problem (remember, there was a log of the fixes, with
programmer's name, in the source code).  This State agency got what
they paid for.

As a parting comment...if you write code where the base functionality
is flawed, no effort of "automated recoding" will result in code that
will perform without flaws.

-
One of many Computer Consultants in the USA
http://drshell.home.mindspring.com/
30 years in the computer field, 20 with Unisys.
-
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** Anonymous <Nobody>
- **Date:** 2002-07-26T16:07:37-04:00
- **Newsgroups:** comp.lang.cobol,us.issues.occupations.computer-programmers
- **Message-ID:** `<3d41001e_1@anonymous>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3d416ecc$0$30453$afc38c87@sisyphus.news.be.easynet.net> <3d41a043.11522274@nntp.mindspring.com>`

```

> Does anyone else see a problem here?  Spaghetti code is a result of
> inexperienced programmers writing code that may work but does not
…[22 more quoted lines elided]…
>

HEAR!  HEAR!  My experience exactly!

No speaka da English + no coda da COBOL = Serves you right you greedy US
corporate drone!





-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-26T19:42:50-05:00
- **Newsgroups:** comp.lang.cobol,us.issues.occupations.computer-programmers
- **Message-ID:** `<ahsqad$t9i$1@slb0.atl.mindspring.net>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3d416ecc$0$30453$afc38c87@sisyphus.news.be.easynet.net> <3d41a043.11522274@nntp.mindspring.com>`

```
see below
```

###### ↳ ↳ ↳ Re: Conversion of Spaghetti cobol code to Structured COBOL code....

_(reply depth: 4)_

- **From:** "Steve Gomori" <sgomori@no.spam.yahoo.com>
- **Date:** 2002-07-30T08:44:55-04:00
- **Newsgroups:** comp.lang.cobol,us.issues.occupations.computer-programmers
- **Message-ID:** `<ai61o8$q3t$1@news.cis.ohio-state.edu>`
- **References:** `<fd149d96.0207110324.1165aaca@posting.google.com> <3d416ecc$0$30453$afc38c87@sisyphus.news.be.easynet.net> <3d41a043.11522274@nntp.mindspring.com> <ahsqad$t9i$1@slb0.atl.mindspring.net>`

```
Thanks, William. All the money and years of therapy to forget "ALTER GO TO"s
and you just undid it all ...


<snip>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
