[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is one period per paragraph a good idea?

_151 messages · 30 participants · 1998-11 → 1998-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Is one period per paragraph a good idea?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
I have been thinking about the concept of 'one period per paragraph'.
Thane Hubbell first introduced me to the idea and I didn't like it,
too different from what I'm used to.  But I can see the advantages.
Have there been any suggestions to the standards committees to relax
the requirement that there be at least one period before a paragraph
name?  Might be tricky syntax, especially since they are working on
removing column restrictions.  I would be a bit more comfortable with
the idea if we could eliminate periods altogether in the Procedure
Division.  I don't relish the thought of 'occasional' periods.  Use
'em or don't.  Wow!  Would that be COBOL?  I'm also a little uneasy
about no statement terminators at all.  Would developing this habit
make us highly 'period error prone' when maintaining old code?  Any
comments?
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365bdc27.24978094@news.enteract.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
I missed out on commenting about the one period idea.  Though I never
read Thane's original post about this, my opinion is that this is a
side affect of good programming practice.

I learned to write paragraphs to be specialized and only do one thing.
As your coding, if you find you are doing too much in a paragraph, you
split it into two specialized paragraphs, and thusly down the line
until each paragraph does only what it's tile implies.  THis rule is
very nice for being able to re-use code.

OTOH, maybee the one period per paragraph rule is geared towards the
same goal.  The more periods you have, the more you are doing in the
paragraph, and the more that can be broken out into seperate
paragraphs.

Just my 2 cents,

Paul

On Tue, 24 Nov 1998 17:05:24 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>I have been thinking about the concept of 'one period per paragraph'.

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b6975.2402798@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365bdc27.24978094@news.enteract.com>`

```
On Mon, 23 Nov 1998 22:11:40 GMT, pduboisREMOVETHIS@enteract.com
(PAL3000) wrote:

>I missed out on commenting about the one period idea.  Though I never
>read Thane's original post about this, my opinion is that this is a
>side affect of good programming practice.
>

I've not said much about it publicly.  There is now some source code
on my home page, http://www.geocities.com/Eureka/2006/ 
on the downloads page - I use that technique in the code you can find
there.  One of the programs is more complex, with some interesting
validations - showing actually where an Exit Paragraph would be a good
thing.
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365aeee4.0@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```

Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
>too different from what I'm used to.  But I can see the advantages.

progress...

>Have there been any suggestions to the standards committees to relax
>the requirement that there be at least one period before a paragraph
…[3 more quoted lines elided]…
>Division.

this would be the ideal

>  I don't relish the thought of 'occasional' periods.  Use
>'em or don't.  Wow!  Would that be COBOL?

a long time ago (ca. 1964) people used commas, semi-colons, and
periods as you would in normal text. They did not try to make the
program look like a Hemingway shortstory with only one statement
sentences.

>  I'm also a little uneasy
>about no statement terminators at all.  Would developing this habit
>make us highly 'period error prone' when maintaining old code?  Any
>comments?

when you maintain old code, you must scrupouesly foloow the
existing style so you will have to adapt anyway. There are,
of course, programs that have no style or are a mixture of several.
Ain't much you can do there...


>--
>Judson McClendon      judmc123@bellsouth.net  (remove numbers)
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365AF041.9E2F640F@bdssoftware.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
After coding with one period for the last few years I have no problems
with it, never did.  There were far more errors with missing periods
when they were required, with IF statement occasionally running amuck. 
I'm unsure how you could eliminate them entirely and still reliably
detect a paragraph header.  I suppose the compiler could simply say
"Well this variable name, or whatever it is, makes no sense, it's one
word on a line by itself, what the hell, must be a paragraph name" or
something similar.  On the other hand, if the supposed paragraph name
was identical to a variable name, and the last statement in the previous
paragraph were a MOVE, well then. . .  Or simply, if the last statement
in the previous paragraph were a MOVE how would the compiler know this
unknown name were either a new paragraph or an incorrectly spelled
variable name.  God forbid, I don't think we need an END-MOVE terminator
to deal with this situation when a period is here now. There are times
when I omit a period at the end of a paragraph and MF Cobol always comes
up with some sort of error and the problem is easily recognizable.  If
periods can be eliminated entirely I wouldn't mind it at all, on the
other hand, one period per paragraph isn't burdensome or inducive of
errors. Period.

Judson McClendon wrote:
> 
> I have been thinking about the concept of 'one period per paragraph'.
…[16 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ekfnm7$F#GA.210@upnetnews03>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365AF041.9E2F640F@bdssoftware.com>`

```

Scott Ramey wrote in message <365AF041.9E2F640F@bdssoftware.com>...
>After coding with one period for the last few years I have no problems
>with it, never did.  There were far more errors with missing periods
…[5 more quoted lines elided]…
>something similar.

This should not be a problem as long as we still have A and B margins
defined.
A "name" in the A margin of the PD is a paragraph name, and a "name" in the
B margin is a dataname.

On the other hand, if the supposed paragraph name
>was identical to a variable name, and the last statement in the previous
>paragraph were a MOVE, well then. . .  Or simply, if the last statement
>in the previous paragraph were a MOVE how would the compiler know this
>unknown name were either a new paragraph or an incorrectly spelled
>variable name.

Still just an A or B margin determination.

>God forbid, I don't think we need an END-MOVE terminator
>to deal with this situation when a period is here now. There are times
…[25 more quoted lines elided]…
>> whoever believes in Him should not perish but have everlasting life."
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#0CAO4$F#GA.256@upnetnews03>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365AF041.9E2F640F@bdssoftware.com>`

```

Scott Ramey wrote in message <365AF041.9E2F640F@bdssoftware.com>...
>After coding with one period for the last few years I have no problems
>with it, never did.  There were far more errors with missing periods
…[5 more quoted lines elided]…
>something similar.

This should not be a problem as long as we still have A and B margins
defined.
A "name" in the A margin of the PD is a paragraph name, and a "name" in the
B margin is a dataname.

On the other hand, if the supposed paragraph name
>was identical to a variable name, and the last statement in the previous
>paragraph were a MOVE, well then. . .  Or simply, if the last statement
>in the previous paragraph were a MOVE how would the compiler know this
>unknown name were either a new paragraph or an incorrectly spelled
>variable name.

Still just an A or B margin determination.

>God forbid, I don't think we need an END-MOVE terminator
>to deal with this situation when a period is here now. There are times
…[25 more quoted lines elided]…
>> whoever believes in Him should not perish but have everlasting life."
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TlC62.164$Q91.449116@news.rdc1.on.wave.home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
I am a big believer in the 'one period per paragraph' style. It forces me to
think about the code I am writing which reduces the 'hacker factor'
considerably.

If I feel a strong urge to put in another period, then it is an indicator
that the paragraph is too complex and should be decomposed into two or more
simpler routines.

Discussions of style usually devolve into religious wars. Steve McConnell's
book, 'Code Complete', has some good ideas on the topics of style and
layout. He argues that a good layout should meet 4 objectives, namely:

1. Accurately represent the logical structure of the code.
2. Consistently represent the logical structure of the code.
3. Improve readability.
4. Withstand modifications.

Any style which holds up to all those criteria probably has merit. If you
can define your objectives, then it should be possible to decide the merit
of any coding *rule*.


Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365AFB33.37E61F96@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com>`

```
Karl Wagner wrote:
> 
> I am a big believer in the 'one period per paragraph' style. It forces me to
> think about the code I am writing which reduces the 'hacker factor'
> considerably.

I guess I probably do the same thing, without thinking of "one period
per paragraph", probably because I still use a variety of old compilers.

But it does look kind of silly to have a single period at the end of the
paragraph, countering the early mandate of English-type syntax.

What I do though is have lots of tiny paragraphs, which basically do
only one thing.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "david scott" <david.scott@gtedc.gte.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f30c$j5m$2@news-1.news.gte.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com>`

```
The original concept of English-like programming was good only as far as
English was like a programming language.  COBOL started out trying to make
the computer accept English, but to make the most of a computer's
capabilities, and to adhere to truly optimal programming methods,
programmers needed to have a dialect that shared more of the computer's
nature than the programmer's.

As for having lots of tiny paragraphs that justdo one thing each, I have
always observed that it was really only valuable to create a paragraph (or
SECTION, if that's your bent) when there was some need for functionality
that was use multiple times and from different locations (and always via
PERFORM, not GOTO).  If a programmer has to break his segment of activity
into too many little paragraphs, then maybe his major paragraph needs it
function more narrowly defined from the next higher calling paragraph.

Howard Brazee <NOSPAMbrazee@home.com> wrote in article 
> But it does look kind of silly to have a single period at the end of the
> paragraph, countering the early mandate of English-type syntax.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b7490.5245939@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net>`

```
On 24 Nov 1998 19:55:56 GMT, "david scott" <david.scott@gtedc.gte.com>
wrote:


>As for having lots of tiny paragraphs that justdo one thing each, I have
>always observed that it was really only valuable to create a paragraph (or
…[4 more quoted lines elided]…
>function more narrowly defined from the next higher calling paragraph.


While this is true - only needing a paragraph if the code is to be
performed multiple times- I still prefer this type of construct:

Perform Open-Files
Perform Initialize-Data
Perform Process-Files
Perform Report-Results
Perform Close-Files

Separating by functionality leads to easier maintenance later on.  In
this example, only process-files may have repetitive logic, but it
makes it easy to see the program structure.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "david scott" <david.scott@gtedc.gte.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73h3n6$7k2$1@news-1.news.gte.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net>`

```
And I agree with this approach, but I still wouldn't create a new paragraph
for just one or two commands.  A thorough application of this idea could
lead to dozens of paragraphs where one properly commented main paragraph
would make a simpler and cleaner program.

>>If a programmer has to break his segment of activity
> >into too many little paragraphs, then maybe his major paragraph needs it
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CAB0B.5922@swbell.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net> <73h3n6$7k2$1@news-1.news.gte.net>`

```
david scott wrote:
> 
> And I agree with this approach, but I still wouldn't create a new paragraph
> for just one or two commands.  A thorough application of this idea could
> lead to dozens of paragraphs where one properly commented main paragraph
> would make a simpler and cleaner program.

The size of a paragraph is less important than its cohesiveness as
a modular unit.  It may make sense to put even a single statement
in a paragraph by itself, if doing so raises the level of abstraction
for the code which performs it.

For example, at the close of your programs you might routinely perform
3600-RELEASE-RESOURCES.  Each program may have a different collection
of resources to release -- files to close, memory to deallocate, 
database transactions to commit, whatever -- but the abstract notion
of releasing resources packages them into a tidy unit.  A given 
program might have nothing to do in this paragraph but close a single
file, but it would still be reasonable to keep the CLOSE in a separate
paragraph.

If you package your code according to modularity rather than size or
syntax, it's not likely that you'll have dozens of tiny paragraphs.
Generally you'll have a few tiny ones, maybe one or two large ones
(mainly for stereotyped and repetitive code), and the rest in between.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73idjs$ch6$1@news.igs.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net> <73h3n6$7k2$1@news-1.news.gte.net> <365CAB0B.5922@swbell.net>`

```
Michael C. Kasten wrote in message <365CAB0B.5922@swbell.net>...

If you read a lot of my code, you would not find
the following code segment rare.

    close-out.
        exit.


>For example, at the close of your programs you might routinely perform
>3600-RELEASE-RESOURCES.  Each program may have a different collection
…[5 more quoted lines elided]…
>paragraph.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7u72.6105$Sf1.4253047@news3.mia>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net> <73h3n6$7k2$1@news-1.news.gte.net> <365CAB0B.5922@swbell.net>`

```
Michael C. Kasten wrote:
>
>The size of a paragraph is less important than its cohesiveness as
>a modular unit.  It may make sense to put even a single statement
>in a paragraph by itself, if doing so raises the level of abstraction
>for the code which performs it.

Good point.  I have, on occasion, actually written empty paragraphs
because it was consistent with a particular structure pattern within
a given system, and the particular program did not currently use the
specific code, but might possibly do so in the future.  The idea was
to make the whole logical structure pattern clear, even though not all
of it existed in that program.  Don't do it often, though.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662C777.61046599@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net> <73h3n6$7k2$1@news-1.news.gte.net> <365CAB0B.5922@swbell.net>`

```
> The size of a paragraph is less important than its cohesiveness as
> a modular unit.  It may make sense to put even a single statement
…[10 more quoted lines elided]…
> paragraph.

And one can expand 3600-RELEASE-RESOURCES to perform another paragraph
if a maintenance need requires a new complicated procedure to release,
say a database record.  Without changing the ease of reading the
program.

Keeping the CLOSE separate is thinking ahead for maintenance.  You may
code your program  with only a need to close at one place, but if
someone wants to add an error routine which requires closing the files,
the code is ready for them.
 
> If you package your code according to modularity rather than size or
> syntax, it's not likely that you'll have dozens of tiny paragraphs.
> Generally you'll have a few tiny ones, maybe one or two large ones
> (mainly for stereotyped and repetitive code), and the rest in between.

The many tiny paragaphs come in with logic branches.  If condition-a
perform this, else perform that.   Maybe this is only a couple of lines,
but when maintenance wants to expand on it, the entry-level maintenance
programmer does not need to enter code witihin your if statement.  It is
a lot easier to add safe code within a paragraph of statements than
within a logical construct.

Think of who will be doing maintenance when developing your coding
style!
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C2215.FADEB444@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365AFB33.37E61F96@home.com> <73f30c$j5m$2@news-1.news.gte.net> <365b7490.5245939@news1.ibm.net> <73h3n6$7k2$1@news-1.news.gte.net>`

```
david scott wrote:
> 
> And I agree with this approach, but I still wouldn't create a new paragraph
> for just one or two commands.  A thorough application of this idea could
> lead to dozens of paragraphs where one properly commented main paragraph
> would make a simpler and cleaner program.

Obviously any sequential commands designed to print headings, etc would
be grouped together.

What you want to do is to branch different functions into different
paragraphs.  People will be looking at your program on-line and need to
see the logic of your paragraph easily without a lot of scrolling.  Well
named paragraphs can do this.
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CBC13.86C0F5C9@att.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com>`

```
Karl Wagner wrote:
> 
> I am a big believer in the 'one period per paragraph' style. It forces me to
…[5 more quoted lines elided]…
> simpler routines.

Under what circumstances do you feel an urge to put in another period?
I'm a long time advocate of completely structured COBOL, e.g., simple
PERFORMs, no GOTOs, etc. (14 years); and a more recent convert to
treating the period as a verb and coding it only where necessary (12-15
months). I'm having trouble conjuring up a scenario in which I'm tempted
to add another period.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CDE90.391@swbell.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net>`

```
William Lynch wrote:
> 
> Karl Wagner wrote:

[snip]

> > If I feel a strong urge to put in another period, then it is an indicator
> > that the paragraph is too complex and should be decomposed into two or more
…[7 more quoted lines elided]…
> to add another period.

I can't speak for Mr. Wagner, but I feel an urge to put in a period
whenever the alternative is to have three or more END-IFs in a row,
unwinding from a series of nested IFs.  There might be other scope 
terminators mixed in, but END-IF is the most common one.

Formally it may be possible to recast nested IFs into EVALUATE TRUE,
but I prefer to reserve EVALUATE for true case structures, where
the branches are mutually exclusive.  Using it as a torturous device
to avoid END-IF misleads the reader.

There are also cases where EVALUATE doesn't do the job.  You can
artificially reduce the nesting by pulling chunks of code into
separate paragraphs, but that decision should be driven by 
considerations of modularity, not by awkward syntax.

Sooner or later you reach a point where none of the alternatives
is very appealing.  In that case you might as well just go for
consistency.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E1417.1898FE22@att.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net> <365CDE90.391@swbell.net>`

```
"Michael C. Kasten" wrote:
>
(snip)
> > > If I feel a strong urge to put in another period, then it is an indicator
> > > that the paragraph is too complex and should be decomposed into two or more
> > > simpler routines.
> >
> > Under what circumstances do you feel an urge to put in another period?

(snip)
> 
> I can't speak for Mr. Wagner, but I feel an urge to put in a period
> whenever the alternative is to have three or more END-IFs in a row,
> unwinding from a series of nested IFs.  There might be other scope
> terminators mixed in, but END-IF is the most common one.

I'm happier with the three END-IF's (properly indented, of course),
rather than the period. What don't you like about the three END-IF's?
Colour me different, I guess. <g>

I certainly agree on not using EVALUATE where it doesn't apply.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365EAE47.64A4@swbell.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net> <365CDE90.391@swbell.net> <365E1417.1898FE22@att.net>`

```
William Lynch wrote:
> 
> "Michael C. Kasten" wrote:
…[7 more quoted lines elided]…
> rather than the period. What don't you like about the three END-IF's?

They're a nuisance to type and a nuisance to align properly.  They
take up space, crowding more interesting code off the page or screen.
They make it difficult to tell what your level of nesting is, unless
you're willing to trust the indentation -- which is most likely to
become inconsistent in deeply nested logic, precisely when you have 
the most difficulty keeping track of the levels.

The worst case is when I'm using a long chain of IF ELSE to implement
a case structure, instead of using EVALUATE for one reason or another.
In that situation I generally align the ELSEs and IFs vertically
rather than indenting them.  Then all the END-IFs are aligned
vertically as well.  Besides looking silly, this arrangement forces
me to count my IFs carefully to make sure I have the right number
of END-IFs, since indentation gives no clue.

In practice, in any given program I use either the traditional style
or a rigorous 1-period-per-paragraph style.  In the latter case if
I need a long chain of END-IFs I'll code it that way, but not without
grumbling.

No matter what your stylistic conventions are, sooner or later you'll
find a case where they are more awkward to preserve than to break.
Then you have to make a judgement call.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365ece08.0@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net> <365CDE90.391@swbell.net> <365E1417.1898FE22@att.net> <365EAE47.64A4@swbell.net>`

```
Michael C. Kasten wrote in message <365EAE47.64A4@swbell.net>...
>William Lynch wrote:
>> "Michael C. Kasten" wrote:
…[16 more quoted lines elided]…
>grumbling.


As with any stylistic issue the rules are never absolute. the only thing
that really counts is:  does the chosen code make it easier to maintain
the program. Not, does it look good?, do I like it?, does it satisfy the
rigorous rules?

The question is not: 'Is one period per para a good idea?', but
'are extraneous periods a good idea?' If you  have periods
that serve a purpose and help making the code more readable
(like when emulating the evaluate), then they have a place.

My personal 'crusade' against periods is against those *extra*
periods that serve no purpose, like a period after a move
statement , after an end-if, etc.  I have even heard people
complain that I'm trying to 'separate the period from the statement
it belongs to' . The period does not 'belong' to every statement;
it does not, like in C, Algol, Ada, PL/1, Java, etc serve as a statement
delimiter. Instead it is a SENTENCE delimiter that signals the end
of a related group of statements. It was unfortunate that it was also
used as an IF-clause delimiter; that has now been rectified by the
scope delimiters.

If you use a period after every statement, you are writing
one-statement sentences; if you use only one period per
paragraph, you are writing one-sentence paragraphs.
Both are extremes.  It seems perfectly appropriate the
break a long paragraph into several sentences if it
improves readability.

Personally, I prefer short paragraphs (the long-winding
paragraphs in this post not withstanding!!). One reason
is (in this is where the analogy between Cobol and normal
English text breaks down) that paragraphs in Cobol are
*named* and therefore can be *re-used* in other places
simply by *performing*. The longer the paragraph, the
lesser its re-usability, hence: the shorter paragraphs as
a means to increase potential re-usability.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uSv7pMxG#GA.237@upnetnews03>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net> <365CDE90.391@swbell.net> <365E1417.1898FE22@att.net> <365EAE47.64A4@swbell.net> <365ece08.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <365ece08.0@news1.ibm.net>...
>Michael C. Kasten wrote in message <365EAE47.64A4@swbell.net>...
>>William Lynch wrote:
…[56 more quoted lines elided]…
>


Using shorter paragraphs definitely improves readability (and therefor, I
think, maintainability) but that, in and of itself, does not necessarily
increase potential for reusability.  One might just get that impression from
the number of "reused" paragraphs that are in fact relatively short.  IMO,
reusability derives more from a limiting a paragraph's functionality rather
than it's relative length.  But then, limiting a paragraph to a single
function does tend to keep it short.

For example, I try to isolate all IO functions to separate paragraphs.  I
initially create a separate paragraph for READ file NEXT for each file
sequentially accessed, a separate READ file for each file randomly accessed,
etc.  Then, when I need to do another READ-whatever, I just code a PERFORM
READ-filename-NEXT, PERFORM READ-filename, etc. as needed.  There is then no
need to clutter up the processing flow (wasting vertical bandwidth!) with AT
END / NOT AT END or INVALID KEY / NOT INVALID KEY clauses.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366069e4.0@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net> <365CDE90.391@swbell.net> <365E1417.1898FE22@att.net> <365EAE47.64A4@swbell.net> <365ece08.0@news1.ibm.net> <uSv7pMxG#GA.237@upnetnews03>`

```
Dennis,

I agree completely. I made the (unwarranted?) ASSumption that a paragraph
only does one thing and that is what keeps it short.

Dennis J. Minette wrote in message ...
>
>Leif Svalgaard wrote in message <365ece08.0@news1.ibm.net>...
…[63 more quoted lines elided]…
>increase potential for reusability.  One might just get that impression
from
>the number of "reused" paragraphs that are in fact relatively short.  IMO,
>reusability derives more from a limiting a paragraph's functionality rather
…[5 more quoted lines elided]…
>sequentially accessed, a separate READ file for each file randomly
accessed,
>etc.  Then, when I need to do another READ-whatever, I just code a PERFORM
>READ-filename-NEXT, PERFORM READ-filename, etc. as needed.  There is then
no
>need to clutter up the processing flow (wasting vertical bandwidth!) with
AT
>END / NOT AT END or INVALID KEY / NOT INVALID KEY clauses.
>
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981127221812.23446.00001715@ng153.aol.com>`
- **References:** `<365EAE47.64A4@swbell.net>`

```
I would like to add to this discussion the possibility of an ELSE-IF construct.
Not as a proposal, just as a discussion point. In a way all we are dealing with
in part of this thread's discussion is the fact that most of us would agree to
repeatedly indent as we code the IF statement within an ELSE clause.

This leads in some cases to severe indentation.  Many such expressions are
really dealing with a prioritized interrogation of mutually exclusive
conditions.  They do not really represent structural depth, just priority (the
upper IFs first, lower IFs later), and exclusivity (successful upper tests
short ciruit lower tests).

Thus in some of these cases (not all), the indentation is a misleading
graphical indicator.

Most languages _lack_ an ELSE-IF construct. When present in a language it is
sometimes encoded as a four-character symbol, ELIF, ... in COBOL statements it
would look like

IF condition-a
  PERFORM A100-dispatcher
ELIF condition-b
  PERFORM B200-dispatcher
ELIF condition-c
  PERFORM C300-dispatcher
END-IF.

Keep in mind that each of those PERFORMs could be sequences of statements which
could include other conditional expressions.

But the people who build the compilere front-end parser get into deep trouble
when language users insist upon allowing a genuine ELSE in there somewhere.

When you encounter the first true ELSE does it glue back to the most recent
nested IF or back to the ELIF.

This could be solved by yet another language reserved word, (I'll make up an
exagerated one), ELIF-ELSE, which would not look like a simple ELSE. 

This would aid in nesting various kinds of conditions, just as each of the
tokens  EVALUATE / WHEN / OTHER / END-EVALUATE are distinct form IF / ELSE /
END-IF.

With the COBOL language as it is, and as it may likely remain, lacking an ELIF
construct, I think that these situations actually argue for breaking the more
difficult ones into their own procedure.  And there, in relative isolation, a
suspension of the indentation convention becomes a lot more acceptable.

And I would say that the trailing END-IF dragon should be shot dead before it
is coded. A period on the end of such a structure is perfectly clear. And it
becomes feasible only if you have isolated the entire expression into its own
procedure.

So when do you break off part of an IF statement into a separate paragraph? 
One criteria could be, if part of the IF is dealing with structural depth, and
another is just dealing with a check-off list of mutually exclusive coditions
examined in a priority sequence, then it may be easier to read, and the END-IF
dragon may be easier to slay, if you place the parts into different paragraphs.


If this is not considered, then we pay people to code what in many cases are
useless END-IF scope terminators.  We pay maintainers to puzzle over  how to
insert new levels in the portion of the expression that is structural, and to
figure out the placement of the inserted END-IF.

And as several postors (my koine, you saw it here first!) have clearly
indicated we will then pay college graduates with decades of high-tech
experience to chase indented clauses and their retinue of contentless END-IFs
left and right as they over the years add and delete coditional levels.

You can hear this stuff in the office when it happens, there is a certain
cadence to the keyboard when people, we are talking some of the very best paid
folks in our society, repeatedly move to a new line and indent a completely
unchanged line x number of spaces.

You can not hear the money drain out for that staff time, however. Nor can you
hear the management salaries go down the drain as earnest project managers and
lead analyst try to extract from a SuperC (comparison) list, the few lines that
actually changed and decide if they believe the umpteen listed changed lines
are really not changes. Of course, only college grads can do this kind of
thing.

You can hear the keyboards, but you can not hear the loss of reliability as
people chase indented code around under production down pressure. 

For ELIF type IF statements, there is no more justification for indentation
then there is for EVALUATE WHEN segments.  That is, there is none. And although
this _is_ hard to see because they look a lot like other IF statements, it is
not really hard to grasp that priority evaluation is distinct from structural
condition testing.

I think the two call for different graphic support on the screen. We talk of
indentation, but actually we use line break and indentation.  In the case of
priority evaluations, coded either as EVALUATE stements or ELIF structures, it
seems to me that line breakage is sufficient.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365fd17b.1265870@news3.ibm.net>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com>`

```
On 28 Nov 1998 03:18:12 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:

>I would like to add to this discussion the possibility of an ELSE-IF construct.

>IF condition-a
>  PERFORM A100-dispatcher
…[4 more quoted lines elided]…
>END-IF.


EVALUATE TRUE
    WHEN condition-a
	PERFORM A100-dispatcher
   WHEN condition-b
	PERFORM B200-dispatcher
   WHEN condition-c
	PERFORM C300-dispatcher
   WHEN OTHER
               PEFFORM HUH
END-EVALUATE
	
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365FDF6A.4C00@swbell.net>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com>`

```
RKRayhawk wrote:

[snip -- proposing a syntax for case structures which would not
 require multiple END-IFs, such as: ] 

> IF condition-a
>   PERFORM A100-dispatcher
…[4 more quoted lines elided]…
> END-IF.

[snip]
 
> But the people who build the compilere front-end parser get into deep trouble
> when language users insist upon allowing a genuine ELSE in there somewhere.
> 
> When you encounter the first true ELSE does it glue back to the most recent
> nested IF or back to the ELIF.

[snip]

I don't see any parsing problem here.  The ELSE would match the most 
recent un-ELSEd IF, provided that there is one between the ELSE and 
the previous ELIF.  If there is no such IF, then the ELSE is a
syntax error.

In other words, between ELIFs, the parser would work exactly the way 
it works now between WHENs in an EVALUATE.  If language users insist
on something more ambiguous then they will deserve whatever mess
they get.

I've used a construct like this in PL/SQL (Oracle's extension of SQL),
which requires an END IF for every IF.  Using ELSIF cuts down on the
use of END IF.

On the other hand, PL/SQL doesn't have a construct for a true case
structure, i.e. one which branches on multiple values of a single
expression.  COBOL has EVALUATE, which can be used either for true
case structures or (in the form of EVALUATE TRUE) as the exact 
equivalent of the proposed ELIF construct.  What would be the
advantage of adding a redundant construct?

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fYS72.11541$Gy.4796826@news4.mia>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com> <365FDF6A.4C00@swbell.net>`

```
Michael C. Kasten wrote:
>RKRayhawk wrote:
>
…[14 more quoted lines elided]…
>syntax error.

I use that construct fairly often in COBOL 74 (no EVALUATE), with each
IF immediately below the preceding ELSE.  I have had a few instances
when compilers blew the stack on a particularly long series of them.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3660cff4.32520762@netnews>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com>`

```
'Twas 28 Nov 1998 03:18:12 GMT, when rkrayhawk@aol.com (RKRayhawk)
illuminated comp.lang.cobol thusly:

>Most languages _lack_ an ELSE-IF construct. When present in a language it is
>sometimes encoded as a four-character symbol, ELIF, ... in COBOL statements it
>would look like

IMO, most of the modern languages have it.  In Fortran there's an explicit
ELSIF (I think that's how it's spelled), in COBOL-85 it's implemented by
the slightly obtuse EVALUTATE statement, and in C, Algol, and Pascal
there's no need for a special construct, because ELSE followed immediately
by IF is semantically identical to an ELSE-IF.

Judson mentions he's strung so many ELSE IFs together that the compiler
blew it's stack.  In COBOL-85 this is just a fact of life, because the
compiler has to know how many END-IFs can follow (though a really cleaver
compiler could just have a counter of nested ELSEs); but in a competently
written COBOL-74 compiler, ELSE IF should not increase the nesting level.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JPb82.8802$w_6.5401276@news2.mia>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com> <3660cff4.32520762@netnews>`

```
Randall Bart wrote:
>
>Judson mentions he's strung so many ELSE IFs together that the compiler
…[3 more quoted lines elided]…
>written COBOL-74 compiler, ELSE IF should not increase the nesting level.

As I recall, it was Medium Systems COBOL 74.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36665ac0.85096840@netnews>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com> <3660cff4.32520762@netnews> <JPb82.8802$w_6.5401276@news2.mia>`

```
'Twas Sun, 29 Nov 1998 13:17:29 GMT, when "Judson McClendon"
<judmc123@bellsouth.net> illuminated comp.lang.cobol thusly:

>Randall Bart wrote:
>>
…[6 more quoted lines elided]…
>As I recall, it was Medium Systems COBOL 74.

Most of our applications (all our big programs) were in COBOLV (68).  I
wrote a user-coded DMPALL in COBOL 74, and it had a big ELSE IF cascade.
It probably wasn't bigger than 15 levels.  Before COBOL-85, I was a heavy
user of ELSE IF and I've never hit an ELSE IF nesting limit in any
compiler, though I did have one where I could tell each ELSE IF increased
the nesting, and nesting was limitted.

How deep were your ELSE IFs?
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wFA92.1001$Jl.230064@news3.mia>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com> <3660cff4.32520762@netnews> <JPb82.8802$w_6.5401276@news2.mia> <36665ac0.85096840@netnews>`

```
Randall Bart wrote:
>
>How deep were your ELSE IFs?

It's been a long time, but there were quite a few, perhaps fifty or
more.  It happened at least twice, as I recall.  This was during the
time I was trying to abandon GO TO completely.  Once I started using
PERFORM/EXIT and GO TO EXIT there was no problem. :-)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3661624b.71240289@news1.ibm.net>`
- **References:** `<365EAE47.64A4@swbell.net> <19981127221812.23446.00001715@ng153.aol.com> <3660cff4.32520762@netnews>`

```
On 29 Nov 1998 06:47:11 GMT, Barticus@att.spam.net (Randall Bart)
wrote:


>
>Judson mentions he's strung so many ELSE IFs together that the compiler
…[3 more quoted lines elided]…
>written COBOL-74 compiler, ELSE IF should not increase the nesting level.

I support of this -- someone at my shop recently ported an Ansi '74
COBOL program (Compiled with RM COBOL on an MVS mainframe No less)  to
VMS - with an Ansi '85 compiler.  It had too many levels of IF ELSE
and would not compile.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pz572.757$Pc1.881859@news.rdc1.on.wave.home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net>`

```
My point exactly.

William Lynch wrote in message <365CBC13.86C0F5C9@att.net>...
>Karl Wagner wrote:
>>
>> I am a big believer in the 'one period per paragraph' style. It forces me
to
>> think about the code I am writing which reduces the 'hacker factor'
>> considerably.
>>
>> If I feel a strong urge to put in another period, then it is an indicator
>> that the paragraph is too complex and should be decomposed into two or
more
>> simpler routines.
>
…[7 more quoted lines elided]…
>Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365d3294.60216296@news3.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net>`

```
On 26 Nov 1998 02:24:30 GMT, William Lynch <wblynch@att.net> wrote:


>
>Under what circumstances do you feel an urge to put in another period?


When you have COPY in open code.In CICS programs I often have things like

	EXEC CICS RECEIVE MAP('ABCMAP') NOHANDLE END-EXEC
	COPY mrgfield REPLACING ==(field)== BY ==VAR1==.
	COPY mrgfield REPLACING ==(field)== BY ==VAR2==.
	COPY mrgfield REPLACING ==(field)== BY ==VAR3==.
	COPY mrgfield REPLACING ==(field)== BY ==VAR4==.
	COPY mrgfield REPLACING ==(field)== BY ==VAR5==.

where mrgfield is a copy book doing the simple (but repetitive) task of merging
screen-variables into commarea

Agreed, this is a pathological case, and the only "." I can think of that would be
required before the end of a paragraph



with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662C7E6.2BD0216C@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <TlC62.164$Q91.449116@news.rdc1.on.wave.home.com> <365CBC13.86C0F5C9@att.net>`

```
> Under what circumstances do you feel an urge to put in another period?
> I'm a long time advocate of completely structured COBOL, e.g., simple
…[5 more quoted lines elided]…
> Bill Lynch

Certainly using older compilers without END-IF statements.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981130132528.16775.00000176@ng131.aol.com>`
- **References:** `<3662C7E6.2BD0216C@home.com>`

```
Howard Brazee <NOSPAMbrazee@home.com>
Date: Mon, 30 Nov 1998 09:29:26 -0700

<<
I'm having trouble conjuring up a scenario in which I'm tempted
to add another period.
>>

While doing maintenance I frequently add periods to existing code and retest,
just to see if it really is true that the trailing statements are occuring at
depth zero (that is, is the code truely invariant).

Real code in real production programs has been messed with by so many real
people with realy different styles that it can be real difficult to determine
if all necessary explicit scope terminators were included.  Even where
possible, it can actually be quicker to just point blank terminate it with the
implicit code terminator and see if all the statements that follow are executed
by both versions of the program.

Furthermore, if I am inserting a standalone conditional statement in a portion
of a procedure that is supposed to be at depth zero.  I will put a period
before and after it (assuming the one after is what should be done). 

One interesting thing about production bugs is that people learn to kill them
dead. An implicit implicit scope terminator is not nearly as deadly a weapon as
an explicit implicit scope teminator. 

One thing is for certain, the compiler tends to be able to see the explicit
implicit scope terminator, where as it can sometimes have vision problems when
we present it with an implicit implicit scope terminator. This has to do with
the look-ahead logic of the grammatical portion of a compiler. There isn't any
reason in the world to be reluctant to latch onto that available strength.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365AF6C6.1FD5@compaq.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
Judson McClendon wrote:
> 
> I have been thinking about the concept of 'one period per paragraph'.
…[5 more quoted lines elided]…
> removing column restrictions.

It is syntactically ambiguous if you eliminage periods.  No matter 
what other comentors say, all situations cannot be handled.  
Especially when one uses free-form syntax (no area A and such).  One 
needs a separator other than space before a procedure-name.  Of 
course, we could use some strange thing like other languages do, but 
we have to have compatibility.

> I would be a bit more comfortable with
> the idea if we could eliminate periods altogether in the Procedure
> Division.

You can write a program with just one at the end if you don't use any 
procedure-names.  With nested programs, in-line PERFORMs, and other 
modular things it is not all that difficult to avoid procedure-names 
(with the current standard you need one at the front - in the proposed 
standard you don't need any at all.)

> I don't relish the thought of 'occasional' periods.  Use
> 'em or don't.  Wow!  Would that be COBOL?  I'm also a little uneasy
…[3 more quoted lines elided]…
> --

Not sure what you mean here.  Using structured stuff catches misplaced 
periods.
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TuE62.218$7a.223@news1.atlantic.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365AF6C6.1FD5@compaq.com>`

```

Don Nelson wrote in message <365AF6C6.1FD5@compaq.com>...
>Judson McClendon wrote:
>>
>> I have been thinking about the concept of 'one period per paragraph'.
[...]
>
>> I would be a bit more comfortable with
…[8 more quoted lines elided]…
>
In fact, with the one-level nested program I just completed, there are
no procedure-names and no periods within any of the procedural
code. Nor is there a STOP RUN or EXIT PROGRAM statement in
either the containing program or the 15 contained programs. Other than
a procedure name after the procedure division header, which
procedure name is optional with Micro Focus, I could find nothing to
tell me they were required and the program runs fine without them.
(NOTE: This is not production code.)
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f9n8$t1v@dfw-ixnews6.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365AF6C6.1FD5@compaq.com> <TuE62.218$7a.223@news1.atlantic.net>`

```
You are using a BUNCH of Micro Focus extensions (some of which will be in
the next Standard and others that won't).

1) Omitting an EXIT PROGRAM is Standard and OK - as long as you really WANT
to "fall thru" the source code (and do an implicit EXIT PROGRAM at the
physical - not logical - end of each nested program).

2) Omitting the STOP RUN (or GoBack) in the main program is NOT something
that you should do.  Although the syntax may work, the program as explicitly
(even under Micro Focus) "undefined" behavior that MAY change with some
future maintenance or release level of the compiler.

3) Not using any procedure names WILL be allowed in the next Standard (as I
recall the latest draft). This is fine for relatively small programs (like
your nested ones) where you have a single "mainline" logic with no PERFORMs,
GO TOs or other explicit "transfer of controls" - but instead do everything
in "inline" code.

4) Not having a period at the end of each Procedure Division is an extension
(and I think actually documented as "illegal" even in MF COBOL).  I would
NOT rely on this working for ever.  A single period (possibly on a source
line of its own) before each END PROGRAM header (or marker as it will soon
be known) would be a good idea.

Rick Smith wrote in message ...
>
>Don Nelson wrote in message <365AF6C6.1FD5@compaq.com>...
…[27 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c%G62.224$7a.336@news1.atlantic.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365AF6C6.1FD5@compaq.com> <TuE62.218$7a.223@news1.atlantic.net> <73f9n8$t1v@dfw-ixnews6.ix.netcom.com>`

```

William M. Klein wrote in message <73f9n8$t1v@dfw-ixnews6.ix.netcom.com>...
>You are using a BUNCH of Micro Focus extensions (some of which will be in
>the next Standard and others that won't).
…[3 more quoted lines elided]…
>physical - not logical - end of each nested program).

I choose to be explicit for production programs. I created the condition
by accident and found it on purpose! (If that makes sense!)

>2) Omitting the STOP RUN (or GoBack) in the main program is NOT something
>that you should do.  Although the syntax may work, the program as
explicitly
>(even under Micro Focus) "undefined" behavior that MAY change with some
>future maintenance or release level of the compiler.

Fair enough!

>3) Not using any procedure names WILL be allowed in the next Standard (as I
>recall the latest draft). This is fine for relatively small programs (like
>your nested ones) where you have a single "mainline" logic with no
PERFORMs,
>GO TOs or other explicit "transfer of controls" - but instead do everything
>in "inline" code.

Ok! But, there are "explicit transfers of control" that are accomplished
entirely with CALLs which use program-names rather than procedure
names. (I am sure you understood that but others may not have.)

>4) Not having a period at the end of each Procedure Division is an
extension
>(and I think actually documented as "illegal" even in MF COBOL).  I would
>NOT rely on this working for ever.  A single period (possibly on a source
>line of its own) before each END PROGRAM header (or marker as it will soon
>be known) would be a good idea.

After searching further, I dd find a definition of (COBOL) sentence as:
one or more statements terminated by a period followed by a space.
This agrees with your comments and shows I was not reading in the
right part of the manual. I was relying on text which stated, in part, the
(procedure) division ends at the identification division header of the
next program, the END PROGRAM header, or the end of the source
program.

I think the change to marker is a good idea. It does not seem right
to call something that trails -- a header.

Thank You!
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >

>Rick Smith wrote in message ...
>>>
…[8 more quoted lines elided]…
>>-------------------------------
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UuE62.219$7a.223@news1.atlantic.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```

Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
>too different from what I'm used to.  But I can see the advantages.


To get used to other styles, one must practice those styles.
As you have stated elsewhere, you have clients that require
COBOL 74. This reduces the opportunity for you to become
accustomed to "one period per paragraph." I saw it, I liked
it, but I still occasionally delete a period that I add from habit.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f4b1$7np@dfw-ixnews5.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
I remember there being a discussion on this point - but as you indicated, it
would be impossible (or nearly so) to remove BOTH the A-margin/B-margin
rules and the Period rule.

Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3659d9f0.24411390@news.enteract.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4b1$7np@dfw-ixnews5.ix.netcom.com>`

```
Didn't read anyone elses comments because lack of time.  My opinion is
that certain syntax rules are there in order to speed up compilation.
Since processors are so much faster, maybee we don't need any more of
these rules.  OTOH, code is much easier to use when there are rules
adhered to from program to program, so know matter what coding
conventions you are ALLOWED to use, it is better to be consistent.  
For example, we use all capatalized letters in ALL our cobol programs
because it keeps them consistent.

C has no paragraph restrictions, but you delinate functions using
curly braces { and }. 

Paul



On Tue, 24 Nov 1998 00:17:55 -0800, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>I remember there being a discussion on this point - but as you indicated, it
>would be impossible (or nearly so) to remove BOTH the A-margin/B-margin
…[24 more quoted lines elided]…
>

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365B19B7.3E724361@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4b1$7np@dfw-ixnews5.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I remember there being a discussion on this point - but as you indicated, it
> would be impossible (or nearly so) to remove BOTH the A-margin/B-margin
> rules and the Period rule.

I have converted COBOL from a version which allowed wide lines without
A-margins, to standard COBOL, and it is a pain.  But on the other hand,
it has been a while since I have had to put a program through the sorter
after I dropped it!


Actually though, with copymembers, etc, I often sequence my code just to
make it easier to find which line my compiler says is wrong.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b36fb.0@news2.uswest.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4b1$7np@dfw-ixnews5.ix.netcom.com> <365B19B7.3E724361@home.com>`

```
I could easily live with the death of the period.

"Period delanda est".


Howard Brazee wrote in message <365B19B7.3E724361@home.com>...
>William M. Klein wrote:
>>
>> I remember there being a discussion on this point - but as you indicated,
it
>> would be impossible (or nearly so) to remove BOTH the A-margin/B-margin
>> rules and the Period rule.
…[8 more quoted lines elided]…
>make it easier to find which line my compiler says is wrong.
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f4ig$808@dfw-ixnews5.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
Judson,
  As someone who "likes" the one period per paragraph style, I do need to
say that it is critical that you use the full set of '85 Standard "scope
terminators" (and NOT conditionals) when using this style.  From things that
you have written in the past, aren't many of your customers still stuck on
'74 compilers.  If so, I think you will find the one-period per paragraph
style possible but pretty clumsy.

Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
>too different from what I'm used to.  But I can see the advantages.
   <much snippage>
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b6a50.2622056@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4ig$808@dfw-ixnews5.ix.netcom.com>`

```
On Tue, 24 Nov 1998 00:21:56 -0800, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>Judson,
>  As someone who "likes" the one period per paragraph style, I do need to
…[5 more quoted lines elided]…
>

Just a small area of disagreement here - I agree that you must use the
explicit scope terminators - but with condition.

String A B C Delimited by size into E

Does not require the use of End-String

My "rule of thumb" is to use then when the following are used:

IF - always

On Exception
On Overflow
Invalid Key
Not Invalid Key
... what I'm saying is that you need to use the explicit scope
terminator only when you use conditional statements.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73g4ld$7qv@sjx-ixn9.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4ig$808@dfw-ixnews5.ix.netcom.com> <365b6a50.2622056@news1.ibm.net>`

```

Thane Hubbell wrote in message <365b6a50.2622056@news1.ibm.net>...
>On Tue, 24 Nov 1998 00:21:56 -0800, "William M. Klein"
><wmklein@ix.netcom.com> wrote:
…[4 more quoted lines elided]…
>>terminators" (and NOT conditionals) when using this style.  From things
that
>>you have written in the past, aren't many of your customers still stuck on
>>'74 compilers.  If so, I think you will find the one-period per paragraph
…[20 more quoted lines elided]…
>

There are some problems with this not putting scope delimiters on imperative
statements, for example

Read XYZ
  Invalid Key
    Add  A to B
       On Size Error
             ADD 1 to Error-num
          End-Add
        Display "Which Add has been ended?"
   Not on Size error Perform Q   *>  Is this a valid statement or
   Not Invalid Key Perform Q      *> Is this a valid statement

Most people would probably (maybe?) want to use (or think would be valid) to
put the  NOT INVALID KEY statement there (thinking both ADDs have been
finished)  UNFORTUNATELY, I believe that the current interpretation of the
Standard is that the End-ADD would be *forced* to go with the second ADD, so
the 1st one is still "un-terminated" when you get to the NOT statement.

Just a warning:
   Even if you don't want to use them with the imperative form of
statements, your compiler may force you into doing so.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f46cd.20436384@netnews>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4ig$808@dfw-ixnews5.ix.netcom.com> <365b6a50.2622056@news1.ibm.net> <73g4ld$7qv@sjx-ixn9.ix.netcom.com>`

```
'Twas Tue, 24 Nov 1998 21:29:28 -0800, when "William M. Klein"
<wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:

>There are some problems with this not putting scope delimiters on imperative
>statements, for example
…[19 more quoted lines elided]…
>statements, your compiler may force you into doing so.

Point well taken, but your example is flawed.  You are correct that the
END-ADD pairs with the second ADD, and this is a problem for someone who
expects it to end the first ADD.  Therefore, NOT ON SIZE ERROR is valid,
but so is NOT INVALID KEY.  The NOT INVALID KEY will implicitly terminate
the first ADD.  (I would give a reference from CD 1.4, but it's back in 
L A, and I'm up at Tahoe).
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73puu4$ooa@dfw-ixnews10.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4ig$808@dfw-ixnews5.ix.netcom.com> <365b6a50.2622056@news1.ibm.net> <73g4ld$7qv@sjx-ixn9.ix.netcom.com> <365f46cd.20436384@netnews>`

```

Randall Bart wrote in message <365f46cd.20436384@netnews>...
>'Twas Tue, 24 Nov 1998 21:29:28 -0800, when "William M. Klein"
><wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:
>
>>There are some problems with this not putting scope delimiters on
imperative
>>statements, for example
>>
…[10 more quoted lines elided]…
>>Most people would probably (maybe?) want to use (or think would be valid)
to
>>put the  NOT INVALID KEY statement there (thinking both ADDs have been
>>finished)  UNFORTUNATELY, I believe that the current interpretation of the
>>Standard is that the End-ADD would be *forced* to go with the second ADD,
so
>>the 1st one is still "un-terminated" when you get to the NOT statement.
>>
…[9 more quoted lines elided]…
>L A, and I'm up at Tahoe).

Sorry, Randall - you have fallen into one of the most common misconceptions
of the '85 Standard (and the draft).

It is true that there is in '85 (and still in the draft) a rule about one
conditional for an "outside verb" terminating any still outstanding
conditionals for inside verbs - HOWEVER, as J4 realized (when they had an
interpreation request on this), this ONLY applies to the IF/ELSE (and
possibly SEARCH) statement.

Why, you may ask?
Because if you look at the general format of ALL the rest of the verbs
(statements) in the '85 Standard, the conditional parts of the statement
REQUIRE an "imperative" statement and does not allow a "conditional
statement".

Therefore, in the example given, you canNOT have a NOT INVALID KEY
(terminating the INVALID KEY part of the READ) because the INVALID KEY (in a
Standard conforming program) *must* include ONLY an imperative statement -
and the ADD ON SIZE ERROR (without any END-ADD) is conditional rather than
imparative.

Note: Some *but not all* compilers do allow the conditional statements to be
nested in non-IF statements - however, this is definitely non-Standard.
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0S62.5342$w_6.3114394@news2.mia>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <73f4ig$808@dfw-ixnews5.ix.netcom.com>`

```
William M. Klein wrote:
>Judson,
>  As someone who "likes" the one period per paragraph style, I do need to
…[4 more quoted lines elided]…
>style possible but pretty clumsy.


That's right.  For me it would be a future thing.  One of those clients
has started to use COBOL 85 a bit, but the COBOL 85 compiler on the
Unisys A Series is much slower than the COBOL 74 compiler, which is
why they haven't already switched.  I have a number of PC clients and
I use MF COBOL there (looking at switching to Fujitsu), but I have found
that keeping my coding habits consistent is important enough for me to
use basically COBOL 74 on the PC until I can switch across the board.
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f4ss$cik$1@news.igs.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
Personally, I am quite at ease with the period as it
sits, and am not even that pro on the various scope
indicator being added.  There is the odd place where
I see them as being clarifying, but to tell the truth I tend
to write code using fairly simple constructs composed
of fairly short paragraphs.

As I see it, writing code is not that different than writing
in any other language.  If your meaning is unclear, you
do not scrap the language and redefine it; you rewrite
the section so that your meaning *is* clear.
Judson McClendon wrote in message ...
>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
…[18 more quoted lines elided]…
>
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10c4e2c698e3cbb99896b4@news.earthlink.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
In article <oHB62.2702$Sf1.2628221@news3.mia>, judmc123@bellsouth.net 
says...
> I have been thinking about the concept of 'one period per paragraph'.
> Thane Hubbell first introduced me to the idea and I didn't like it,
…[10 more quoted lines elided]…
> comments?

Here are my two cents. <g>

1) When I did discuss this issue with some colleges it seemed that the
majority of them did not like the idea. We never got into any reasons
why they did not like it so I have no solid reasons why they disliked
the idea. 

2) I think that it would be very hard to change the use of a period 
in Cobol. Given the amount of code that exists today it would be
risky to start changing the use of a period in an older program. 
The chance of creating errors would go up dramatically, IMO. 

If the code uses the style of a period per line I would stay with
that method.  On the other hand, if someone is writing new code it
would be fine to use the one period method, I think.


3) I guess I am equally skeptical as you are on this issue. What I need
to do is try out using only one period per paragraph and see how the
code looks and feels then I could judge if I like the style. 

4) Finally, I think that for the immediate future most of the Cobol
code will continue to have multiple periods per paragraph. The use
of a single period per paragraph will catch on only if it can provide
a significant advantage. But then habits die hard and it is likely
that the "Old Dogs" will not likely change their ways. 

> --
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)
…[6 more quoted lines elided]…
> 
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365B309F.1F2@swbell.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
Judson McClendon wrote:
> 
> I have been thinking about the concept of 'one period per paragraph'.
…[11 more quoted lines elided]…
> comments?

I coded mainframe COBOL for years, using periods in the old fashioned
way.  Recently I moved to MicroFocus under Unix, and took the 
opportunity to try out the 1-period-per-paragraph (1PPP) style.

I still haven't gotten used to 1PPP, and I have to actively suppress
my old habits, but so far it doesn't really seem to make a whole
lot of difference.

Many people have asserted that the old style invites a lot of bugs
through period abuse -- periods missing or misplaced.  Personally I
never had that problem much.  My weaknesses lie elsewhere, like
perpetually typing PERFROM, but at least the compiler catches that one.

The 1PPP style pretty much requires a liberal use of scope
terminators such as END-IF, which take up a lot of space, and which
are subject to a different kind of abuse.  In complex logic, especially 
with sloppy indentation, it can be difficult to keep track of which 
scopes are active at a given point.  You have to match up your IFs and 
END-IFs all the way up to the top of the paragraph (or section) before 
you can tell whether you're all the way out.  

You may be able to reduce the need for this kind of tedious analysis
by breaking everything up into tiny paragraphs, but that approach
seems backwards to me.  The packaging into paragraphs should be 
driven by considerations of modularity, not by syntactical convenience.

All in all I can't get excited about it either way.  It's more
important to code consistently than to code one way or another.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981124234854.07622.00000250@ng-cr1.aol.com>`
- **References:** `<365B309F.1F2@swbell.net>`

```

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html

Date: Tue, 24 Nov 1998 16:18:07 -0600
said, in part, 


<<

The 1PPP style pretty much requires a liberal use of scope
terminators such as END-IF, which take up a lot of space, and which
are subject to a different kind of abuse.  In complex logic, especially 
with sloppy indentation, it can be difficult to keep track of which 
scopes are active at a given point.  You have to match up your IFs and 
END-IFs all the way up to the top of the paragraph (or section) before 
you can tell whether you're all the way out.  
>>

He's right, and maintenance programmers, IMHO, know this best.

It seems theoretical to some, but the vertical dimension of the bandwidth of
the CRT and its progeny are crucial factors in the efficiency of the
human-machine interface.

More and more scope terminators does more than take up vertical realestate, it
removes meaningful information from the screen. That drains the bandwidth of
content.

And also in there somewhere, as an efficiency consideration, is the depth of
the code. IF-STATEMENTS that over years have evolved deeper and deeper are
definitely prone to being further manipulated erroneously.

A central fact of COBOL programs is the longevity of the code.  COBOL programs
get modified again and again, frequently under extreme pressure. Finding the
right place to insert the explicit scope terminator can be a problem, whether
we move to a 1PPP standard or not.

But what will increase is the number of times that a fix goes wrong because of
the lack of an addition of an explicit scope terminator (not just the
misplacement of such).

For a 1PPP standard to be viable we would have to turn right around and add the
period back in in the form of an END-EVERYTHING-I-AM-NOT-A-PERIOD super
terminator which would function as a period but satisfy the requirement of not
being a period (very COBOLesque).

Nesting IF-STATEMENTS (or any other constructs), I believe, actually makes us
more efficient.  Because it allows us to see deeper into the code while staying
at just one level (we do not have to page down). This available efficiency is
delivered to the mind much more readily if we use the graphical support
technique of indenting.

But there is a point of dimminishing returns.  The more we nest, the harder it
becomes to hold onto the overall sense of what is happening. One measure of
that inefficiency is the frequency with which we make errors while modifying a
deeply nested code structure. That metric will increase if we do not allow the
period at the end of a deep nest in the middle of a paragraph (procedure).

To a lesser extent, I would also mention that use of periods, even on shallow
nests, allows consumption of minimum horizontal dimmension while avoiding
consumption of (potentially multiple) units of vertical dimension.

I know for sure that this seems needlessly cerebral to some, and I do respect
that. But a computer language _IS_ an interface between man and machine. The
efficiency of that interface relates directly to social costs for production
and maintenance, and social risks per reliability.

We should lock in on cost and reliability as deciding factors. Needless waste
of the veritcal aspect of the presentation of the COBOL robs the interface of
content per unit of time. The effect on comprehension of the code, especially
when under production down duress, is direct and palpable.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73huot$6er@dfw-ixnews3.ix.netcom.com>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com>`

```
On 25 Nov 1998 04:48:54 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:

>It seems theoretical to some, but the vertical dimension of the bandwidth of
>the CRT and its progeny are crucial factors in the efficiency of the
>human-machine interface.

Please, Robert, PLEASE, tell us that you wrote this as a test of
our having read your post :)

And, may I use it in my sig sometime in the future?  I PROMISE to
give it proper attribution!

Happy Thansgiving to all,

Rick Anderson
Seattle
anderson  ï¿½atï¿½  pobox  ï¿½fullstopï¿½  com
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CC024.9BABAE35@att.net>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com>`

```
RKRayhawk wrote:
> 
(snip)
> 
> He's right, and maintenance programmers, IMHO, know this best.
…[7 more quoted lines elided]…
> content.

I'm going to disagree respectfully here. I don't think the scope
delimiters waste the screen real estate. I've been using the delimiters
religiously since I gained access to a COBOL II compiler, and urge
others to use them, END-IF especially, as routinely as they code
END-EXEC to terminate a CICS command. IMHO the value of the delimiters
to is bring closure as you read thru the code. I suspect we COBOL folk
have been conditioned by all those years before the '85 standard to
unbalanced constructs which often just trail off into nothing and accept
this as the norm. Using some other languages, e.g., REXX, which requires
delimiters (on IF, SELECT, DO, etc.) helps give one a different slant
on, and appreciation of, other ways (better ways?) of coding.

By the same token I am also maniacal in getting the indentation right,
and changing it as I modify a program, so the visual impression *is* the
logic. I'd be interested to hear if any others share this view.

Bill Lynch

PS: If all else fails we can always check the logical levels at the left
margin of the COBOL listing (my experience is IBM mainframe). This has
been especially useful when converting a program or making major
changes.

PPS: In the spirit of "Just because you can doesn't mean you *have* to",
I'd like to suggest Lynch's corollary, "Just because you don't have to
doesn't mean you shouldn't".
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73ig0o$36j@dfw-ixnews7.ix.netcom.com>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net>`

```

William Lynch wrote in message <365CC024.9BABAE35@att.net>...
  <some snippage>
>
>By the same token I am also maniacal in getting the indentation right,
…[4 more quoted lines elided]…
>


Bill,
  I agree with you in general on getting the indentation right - HOWEVER,
like missing periods this can be error prone (on occasion).  When I think I
have done it correctly, but have actually made a mistake, I do have a
tendency (that I don't think is unique) to read the indentation rather than
the actual (incorrect) code that I have created.

P.S.  The IBM "nesting level" counter on source listing is REALLY nice.  For
those of you who haven't seen it, do try to find a "blue" friend who can
show it to you.  (It applies to ALL the conditionals - so an INVALID KEY in
the middle of an ON SIZE ERROR in the middle of an IF would get a level "3"
indicator.)

P.P.S.  How do you indent nested IFs - that don't quite logically "feel"
like an EVALUATE statement - e.g.

If A = B
    Perform AB
Else
   IF L > M
      Perform LM
   Else
       If XYZ or AAA
         Perform XYZ-AAA
       END-IF
   END-IF
END-IF

Personally, I usually do it as above - but after about 3 to 5 levels of
nesting, I do sometimes use the

    ELSE IF on-one-line

variation.  As with many parts of this thread, it is a "style" issue - but
one that (at least for me) doesn't have any real good "solution" (unless you
want to go to EVALUATE TRUE - which always seemed like a "cop out" to me).
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E1844.F2B5362E@att.net>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <73ig0o$36j@dfw-ixnews7.ix.netcom.com>`

```
"William M. Klein" wrote:
> 
> William Lynch wrote in message <365CC024.9BABAE35@att.net>...
…[11 more quoted lines elided]…
> like missing periods this can be error prone (on occasion).

Of course, no human (including yours truly) can do this as consistently
as a mature compiler. Otherwise I'd never have to consult the "nesting
level" counter. <g>

> When I think I
> have done it correctly, but have actually made a mistake, I do have a
…[22 more quoted lines elided]…
> END-IF

I'd code it exactly as you did above (the three END-IF's look normal to
me here <g>). If the logic is IF...THEN...ELSE, then that's what should
be coded. When the nesting gets this deep (3 or 4) I start running out
of space to code, so I'm likely to split the rest off into a separate
paragraph, although I understand it's not mandated by any principles of
structured programming. Before the '85 standard I'd code multiple IF's
at the left margin if what I was coding was, in real life, a case
structure (EVALUATE killed that, happily for me).

I really never code a subsequent IF on the same line as ELSE, I find
that extremely ugly. I wonder if this discussion smacks of the
mathematical vs. linguistic mapping Bob Rayhawk mentioned yesterday (I
definitely hope to hear more about that). Wondering out loud here, is
there another division of us folk into groups, like IBM CEs, who are
happy with code just strung out end to end, vs. those like me (and Bill
Klein, too, I think) who really want the logic to follow the appearance? 

Bill Lynch

PS: Hope everyone, USA or not, had a very happy Thanksgiving!
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662D02B.E27BD4D2@home.com>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <73ig0o$36j@dfw-ixnews7.ix.netcom.com> <365E1844.F2B5362E@att.net>`

```
> I really never code a subsequent IF on the same line as ELSE, I find
> that extremely ugly. I wonder if this discussion smacks of the
…[4 more quoted lines elided]…
> Klein, too, I think) who really want the logic to follow the appearance?

One exception to the standard indention is in pre-evaluate long IF
statements:
     IF MY-VALUE = 'A' THEN PERFORM PARAGRAPH-A
     ELSE
     IF MY-VALUE = 'B' THEN PERFORM PARAGRAPH-B
     ELSE
     IF MY-VALUE = 'C' THEN PERFORM PARAGRAPH-C
     ELSE
     IF MY-VALUE = 'D' THEN PERFORM PARAGRAPH-D...

but even then, I like to separate ELSE to make them visible.  New
compilers make this ugly construct unnecessary.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uk9#7DYG#GA.218@upnetnews05>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net>`

```

William Lynch wrote in message <365CC024.9BABAE35@att.net>...
>RKRayhawk wrote:
>>
…[4 more quoted lines elided]…
>> It seems theoretical to some, but the vertical dimension of the bandwidth
of
>> the CRT and its progeny are crucial factors in the efficiency of the
>> human-machine interface.
>>
>> More and more scope terminators does more than take up vertical
realestate, it
>> removes meaningful information from the screen. That drains the bandwidth
of
>> content.
>
…[14 more quoted lines elided]…
>logic. I'd be interested to hear if any others share this view.

I'll "rubber-stamp" that point of view, Bill.  Even though constant
realignment of IF / END-IF makes for a longer day, future maintenance work
will move along more effortlessly.

>Bill Lynch
>
…[7 more quoted lines elided]…
>doesn't mean you shouldn't".

ROTFLMAO! That is one helluva corollary!
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E18B5.E9D075A8@att.net>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <uk9#7DYG#GA.218@upnetnews05>`

```
"Dennis J. Minette" wrote:
> 
> William Lynch wrote in message <365CC024.9BABAE35@att.net>...
(snip)
> >
> >By the same token I am also maniacal in getting the indentation right,
…[5 more quoted lines elided]…
> will move along more effortlessly.

Glad to have you on board, Dennis!

(snip2)
> >
> >PPS: In the spirit of "Just because you can doesn't mean you *have* to",
…[3 more quoted lines elided]…
> ROTFLMAO! That is one helluva corollary!

Feel free to use it as you wish,

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<plu72.6107$Sf1.4257748@news3.mia>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <uk9#7DYG#GA.218@upnetnews05>`

```
Dennis J. Minette wrote:
>
>William Lynch wrote:
…[7 more quoted lines elided]…
>will move along more effortlessly.

Me too.  I believe two attributes which contribute toward becoming a 'good'
programmer are a small bit of laziness so you will work efficiently, and
a lot of perfectionism so you will expend any necessary effort to make sure
it is correct. :-)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365F5836.DE66CA0C@att.net>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <uk9#7DYG#GA.218@upnetnews05> <plu72.6107$Sf1.4257748@news3.mia>`

```
Judson McClendon wrote:
> 
(snip)
> >
> >I'll "rubber-stamp" that point of view, Bill.  Even though constant
…[6 more quoted lines elided]…
> it is correct. :-)

Right on the money! The laziness aspect is what motivates me to develop
so many tools and the perfectionist aspect is what makes them robust.

Bill Lynch (who believes he quilifies in both categories)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3664065B.71139EB9@IMN.nl>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net>`

```
William Lynch wrote:
8<

> ... I am also maniacal in getting the indentation right,
> and changing it as I modify a program, so the visual impression *is* the
> logic. I'd be interested to hear if any others share this view.
>
> Bill Lynch

Which reminded me of the executable code in the )PROC division of ISPF Panel
Definitions.
These actually have NO period, NO scope terminators or whatever. When you see ...

)PROC
 If condition1
    statement1
    If condition2
       statement2
    Else
       statement3
    statement4
 Else
    statement5
 statement6

... it does what it shows: statement4 is within the true-branche of the outer if and
likewise statement6 whint the else of it, purely by indentation!
Nice, because no extra type work for any kind of delimiter (dot nor end-x)
required.

The Frog
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** Ralph Jones <leclay@ibm.net>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366B10E9.B3832035@ibm.net>`
- **References:** `<365B309F.1F2@swbell.net> <19981124234854.07622.00000250@ng-cr1.aol.com> <365CC024.9BABAE35@att.net> <3664065B.71139EB9@IMN.nl>`

```
Ditto Mr. Lynch. But indents show you what is intended not what is programmed
rjj :-))

"COBOL Frog (Huib Klink)" wrote:

> William Lynch wrote:
> 8<
…[40 more quoted lines elided]…
>   (Download ICQ at http://www.icq.com/)
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** d.s.kirk@ix.netcom.com (David)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365d4953.1299010@nntp.ix.netcom.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
On Tue, 24 Nov 1998 17:05:24 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
…[10 more quoted lines elided]…
>comments?

well, in my books i've spoken strongly against more than one period
per paragraph.  in fact, i recommend treating the period as a verb,
i.e, put it on a separate line. helps readability a lot.  all the
period does is say to the compiler 'stop sequential execution'.   we
should not be needing this.  most compilers now will place one period
at end of paragraph anyway.  the period no longer serves any useful
purpose, now that we have ansi 85 syntax.  all of the major coding
problems i've seen had misplaced periods. eliminate the periods and
your coding style improves dramatically.... yes, i know many will
strongly defend their use of PERFORM THRU and GO TO exit paragraphs,
but it's a battle long lost.   
david
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C13A8.C5E9B17D@home.com>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia> <365d4953.1299010@nntp.ix.netcom.com>`

```
all of the major coding
> problems i've seen had misplaced periods. eliminate the periods and
> your coding style improves dramatically.... yes, i know many will
> strongly defend their use of PERFORM THRU and GO TO exit paragraphs,
> but it's a battle long lost.
> david

I hate PERFORM THRU and PERFORM section.  But I have seen very few
errors caused by having extra periods.  I do remember when a junior
programmer couldn't find her error on a listing when a global replace
moved a period into column 73!

Having too few periods has caused programming errors, but END-IFs should
remove that problem  (most programs I see were created before END-IFs
were available).  But if all IFs (and similar constructs) have END-IFs,
it shouldn't matter whether there are periods or not.  Errors will be
caught by the END statements.
```

##### ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981124231101.07622.00000238@ng-cr1.aol.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com>`

```

For those who would like a floating pargraph name in the COBOL language, try
this idea.

There are a number of text markup languages that _start_ commands with a
period.  Such as 

.sp 5

might be a command to print five spaces. This kind of syntax is present in
Script 370 on mainframes and Tex document processors on desktop machines.

I am not sure, but seems like the originators knew that sentence-ending periods
would be followed by white space (blank, tab, new line, or EOF).  It is also
true that decimal points (or European thousand separators) would be preceeded
by numbers.  Thus a dot-command was distinct from any other expected lexical
pattern.

A future version of COBOL could exploit this same opportunity.  A DOTTED NAME
could be a paragraph (procedure) name.

In old format in A-margin
001000 .DOT-YOUR-AYES.
                  MOVE DOTS TO SCREEN.


This would also be consistent with floating format.  (Imagine being able to
indent entire paragraphs, label and all, We could have lots of committee
meetings on that).

This strategy will allow the continued recognition of a period followed by
white space, as a terminator.

This kind of syntax will require white space infront of period. 

This change, I think, can not break any existing code. Becasue no current
program will compile with a period not followed by a space.

For the aged mainframes we could add a special rule that a period in column 72
will never be considered part of a DOTTED NAME. (That will require environment
specific logic). 

.Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73g565$8ad@sjx-ixn9.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com>`

```
I just thought that I would show the group when you can have problems if you
don't want ANY periods to be required.

In the draft Standard the A-margin and B-margin have gone away.
Furthermore, there are new things called "words reserved in context" which
are words that you CAN use as user-defined words (data names and procedure
names - for example).  Therefore, the following code is an issue for the use
of periods.

Accept Long-Num
    from Date
    YYYYMMDD
     Display ABC

The question (if you didn't require periods) is whether YYYYMMDD is a new
paragraph name or if it is the "reserved in context" optional word to tell
the ACCEPT statement to get the date with a 4-digit year.  If you don't
require periods at the end of each paragraph, then there is no way to figure
this out.  (Even adding a period AFTER YYYYMMDD wouldn't help).

If "you all" are really saying that you prefer getting rid of the period
requirement OVER getting rid of the A-margin/B-Margin rule, then this is
something that you should let J4 know (because they have gone the other
way).  This example (and MANY others) just shows that you can't get rid of
both of them (and many compilers - as an extension - have already gotten rid
of the A-margin/B-margin rules).
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c2333.0@news3.uswest.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com>`

```
Does this means the majority of committee members would rather have periods
than columns?  My feelings are the other way around.

William M. Klein wrote in message <73g565$8ad@sjx-ixn9.ix.netcom.com>...
>I just thought that I would show the group when you can have problems if
you
>don't want ANY periods to be required.
>
…[3 more quoted lines elided]…
>names - for example).  Therefore, the following code is an issue for the
use
>of periods.
>
…[8 more quoted lines elided]…
>require periods at the end of each paragraph, then there is no way to
figure
>this out.  (Even adding a period AFTER YYYYMMDD wouldn't help).
>
…[4 more quoted lines elided]…
>both of them (and many compilers - as an extension - have already gotten
rid
>of the A-margin/B-margin rules).
>
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c2a5a.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net>`

```
I think it is more important to get rid of the A/B margins
than of the period. I can live with ONE period at the end
of the paragraph on a line by itself. The END-PARAGRAPH
works as well, but is too heavy for regular use.

Stray thought: if the paragraph marker (?) was terminated by
a colon (:) instead of a period (.) that might serve to resolve
any ambiguity as to what is a paragraph. I don't think this
would conflict with reference modification (which is between
parentheses).

Chris Osborne wrote in message <365c2333.0@news3.uswest.net>...
>Does this means the majority of committee members would rather have periods
>than columns?  My feelings are the other way around.
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hdiv$ovi$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <365c2a5a.0@news1.ibm.net>`

```
There is an old saying: If it ain't broke, then don't fix it.

There is a great danger here of turning "lets revise the
standard" into "lets invent a brand new language".

First, we do away with location as syntactically meaningful.
No more A and B areas.  Now we have a problem knowing
what is a paragraph name, and what is a statement.  Then
we do away with most periods, and replace them with scope
delimiters.

Now we need a way to show a paragraph, so we add a full
colin as the "paragraph" mark.

Now, our syntax is:
paragraph: This is subroutine module, essentially, and
                    includes everything up until
                    end-paragraph
                    .
Why not just make the "end-paragraph" a return statement,
do away with the final period, and call it a new kind of
assembler?  Then we could put in a semi-colin, and make
everything to the right of it a comment?

Leif Svalgaard wrote in message <365c2a5a.0@news1.ibm.net>...
>I think it is more important to get rid of the A/B margins
>than of the period. I can live with ONE period at the end
…[10 more quoted lines elided]…
>>Does this means the majority of committee members would rather have
periods
>>than columns?  My feelings are the other way around.
>>
…[6 more quoted lines elided]…
>>>Furthermore, there are new things called "words reserved in context"
which
>>>are words that you CAN use as user-defined words (data names and
procedure
>>>names - for example).  Therefore, the following code is an issue for the
>>use
…[8 more quoted lines elided]…
>>>paragraph name or if it is the "reserved in context" optional word to
tell
>>>the ACCEPT statement to get the date with a 4-digit year.  If you don't
>>>require periods at the end of each paragraph, then there is no way to
…[6 more quoted lines elided]…
>>>way).  This example (and MANY others) just shows that you can't get rid
of
>>>both of them (and many compilers - as an extension - have already gotten
>>rid
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c3bbb.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <365c2a5a.0@news1.ibm.net> <73hdiv$ovi$1@news.igs.net>`

```
I know, I know. Should have kept my mouth shut.

Donald Tees wrote in message <73hdiv$ovi$1@news.igs.net>...
>There is an old saying: If it ain't broke, then don't fix it.
>
…[58 more quoted lines elided]…
>>>>The question (if you didn't require periods) is whether YYYYMMDD is a
new
>>>>paragraph name or if it is the "reserved in context" optional word to
>tell
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C3EC6.EF9E8AE4@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <365c2a5a.0@news1.ibm.net> <73hdiv$ovi$1@news.igs.net>`

```
Donald Tees wrote:
> 
> There is an old saying: If it ain't broke, then don't fix it.
> 
> There is a great danger here of turning "lets revise the
> standard" into "lets invent a brand new language".

Yep, that will break COBOL just nicely.  Then the Academics will be able
to say "I told you COBOL wasn't a decent language".
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sW62.5417$w_6.3243227@news2.mia>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net>`

```
Chris Osborne wrote:
>Does this means the majority of committee members would rather have
>periods than columns?  My feelings are the other way around.

I agree, Chris.  Columns have never bothered me, except perhaps the
column 72 limit.  If we simply had the option of eliminating the
archaic sequence number, shifting Area A to column 1, Area B to
column 5, and relaxing the rightmost limit, I would be very happy
with columns (You would still probably need a rightmost limit of,
say 100 or 132, just to make the listings readable).  I think it
improves readability by making paragraphs more visible.  There
could be a standard compiler command to say whether you wanted
sequence numbers or not, for those who need or want them.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c3628.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia>`

```

Judson McClendon wrote in message <6sW62.5417$w_6.3243227@news2.mia>...
>Chris Osborne wrote:
>>Does this means the majority of committee members would rather have
…[10 more quoted lines elided]…
>sequence numbers or not, for those who need or want them.


That would be nice. It should not be hard for the compiler to
discover that copybooks may have the old format and simply
allow them in the old format even if the program is without
sequence numbers.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hdml$ovu$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia>`

```
Now that sounds sensible.  The only change I would make
is area B should be column 8 instead of 5.  I say that because
it is far more standard for tab settings.

Judson McClendon wrote in message <6sW62.5417$w_6.3243227@news2.mia>...
>Chris Osborne wrote:
>>Does this means the majority of committee members would rather have
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C3D11.62943D24@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia>`

```
> I agree, Chris.  Columns have never bothered me, except perhaps the
> column 72 limit.  If we simply had the option of eliminating the
…[3 more quoted lines elided]…
> say 100 or 132, just to make the listings readable).  

VAX COBOL has this as a compiler option.  It was smart enough to tell
whether column 1 replaced column 7 or column 8.  (you still need column
7).  I forget whether it had an equivalent of columns 73-80.   But it
certainly was an 80 column image.  This system works when your editor
displays 80 columns of data.  If you have line commands such as TSO
uses, then you really want a wider display to see your data.

I don't like having 100 or 132 columns when most people do their work on
PCs, or when they want print outs it is to make notes on them.  80 is
sufficient.  

One trouble though is that COBOL doesn't have the ability to put both
code and comments on the same line.  Lots of shops get around this by
using change control type comments in the margins of the code.

Another trouble is converting from that option to standard COBOL. 
Consider a literal 5 lines long using a - in column 1...
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N%X62.5436$w_6.3293801@news2.mia>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com>`

```
Howard Brazee wrote:
>
>VAX COBOL has this as a compiler option.  It was smart enough to tell
…[4 more quoted lines elided]…
>uses, then you really want a wider display to see your data.

We don't need column 7.  From your other comments, I think you might
agree that we really need a 'line termination comment' token, like
'//' in C++, or ';' in many assembly languages.  Something like that.
A limit of 80 columns would be fine with me.  Will we ever be rid of
the 80-column punched card? :-)
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C5826.87BE07BC@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[12 more quoted lines elided]…
> the 80-column punched card? :-)

We need some way of having comments.  Currently that is with column 7. 
I never write programs with a dash in column 7, but it is standard, and
DEC did move that to column 1 when using that compiler option.

I suspect the 80 column card will stay with us.  We shouldn't have to
page left and right to see our source code on our screens.  Now, it
would be nice to have our SPF type editor to have 80 columns PLUS
positions to do line commands.

I am working with a system where we got code changes from the vendor for
Y2K.  This vendor keeps old changes, with the change number in columns
1-6 for either adds or deletes.  The deletes had an asterisk in column
7.   We also use ADSO, and it used comment delimiters to put this same
information in the front of the code.  Deletes did not have the final
delimiter. 

C++ allows for either line comments or delimited comments.  Since
REMARKS has changed, all COBOL has is line comments.  (and column
delimited comments 1-6 & 73-80)

Here are some types of comment indicators:
1.  When you hit one, the rest of the line is a comment.
2.  When you hit one, the rest of the line is a comment unless
delimited.
3.  When you hit one, the rest of the program is a comment unless
delimited.
   (you may have some problems with nested comments this way)
   (nested comments are common when a procedure with comments is
commented out)
4.  The compiler recognizes that this code does not belong to anything.
   (I comment JCL and SORT statements after whitespace after data)
5.  Certain columns are ignored and thus available for comments
   (It is irritating to have compilers tell me my sequence numbers are
out of order,
    but that happens with copymembers anyway unless I leave sequences
all blank!)
6. Keywords indicating comments.  e.g. the REMARKS used to do this.  It
is possible too modify COBOL to accept comments after the period in
paragraph names, for instance.

When I am developing a new program, I generally sequence between
compiles.  This is so I can easily find the source line from a listing
containing copycode.  When I am finished, I remove the sequence
numbers.  I haven't dropped a deck in years.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hli7$sms$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia>`

```

Judson McClendon wrote in message ...

>We don't need column 7.  From your other comments, I think you might
>agree that we really need a 'line termination comment' token, like
>'//' in C++, or ';' in many assembly languages.  Something like that.
>A limit of 80 columns would be fine with me.  Will we ever be rid of
>the 80-column punched card? :-)


I like that idea too.  As long as we do not need an "end-comment"<G>.
I dislike the style of comment that requires an ending ... the end of line,
assembler style seems to work best.  I would suggest, actually, using
the asterisk, just for traditions sake.  Perhaps "**".

The only problem with eliminating column 7 is the debugging mode
variance.  I have recently been playing with the idea (presented in
this echo) of using it to be able to run a program in two separate
modes, and I quite like it.

I wrote an interpreter in Cobol, and used the debug mode command
to test it.  I ended up with two programs: one runs the interpreted
code (with debugging mode off) while the second effectively single
steps the code (with debugging mode on). It is quite a neat way
of writing code, actually.

I think, from now on, when I make changes I am going to test them
as "debug on" and a D in column seven.  Then it can be changed
back by turning debug mode off. Making them permanent will just
involve removing the D.

I also think that for tricky areas of code that I end up putting
displays into while debugging, that I am going to play with the
idea of a "debug mode" single step subroutine that can be
turned off and on for maintenance ... where the programmer
actually sees what is happening on the screen.  Not sure
how those two items are going to work out, but then styles
evolve by trying things for a while.

As for the 80 columns ... have you ever tried reading anything
in a natural language where the line length is far too wide? It
makes lines very difficult to read, regardless of language. I find,
for example, that I can read paperbacks at the rate of 275 pages
per hour, relaxed reading.  Hardcovers with a wider page slow
me down to about 180 pages per hour.

I could not figure out why, until I programmed the firmware for
a dot matrix printer.  While I was doing that project, I found myself
reading a book, and it occurred to me that I read bi-directionally
(that is, serpentine fashion, like a printer)
as long as the number of words per line does not exceed six
or seven.  When the word count starts to exceed that, the brain
starts chunking it down as you read.  Up to there, the brain can
read the line backwards, and still comprehend the message.(at
least for my brain).

Based on that totally flimsy evidence, I suspect that more than
the existing sixty or so character positions per line would decrease
readability quite a bit.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c7f59.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net>`

```
Donald Tees wrote in message <73hli7$sms$1@news.igs.net>...
>Judson McClendon wrote in message ...
>>We don't need column 7.  From your other comments, I think you might
…[3 more quoted lines elided]…
>>the 80-column punched card? :-)


>As for the 80 columns ... have you ever tried reading anything
>in a natural language where the line length is far too wide? It
>makes lines very difficult to read, regardless of language.

News papers use narrow columns for easier reading too.

>I could not figure out why, until I programmed the firmware for
>a dot matrix printer.  While I was doing that project, I found myself
>reading a book, and it occurred to me that I read bi-directionally
>(that is, serpentine fashion, like a printer)

there is a wonderful English word for that:
boustrophedonically ('as the ox turns' - in plowing)

>as long as the number of words per line does not exceed six
>or seven.  When the word count starts to exceed that, the brain
…[6 more quoted lines elided]…
>readability quite a bit.


I agree with that. I have seen C-programs where some lines are
200+ characters long. Even on a 21 inch screen, these are next
to impossible to read.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73idtu$crh$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <365c7f59.0@news1.ibm.net>...
>>(that is, serpentine fashion, like a printer)
>
>there is a wonderful English word for that:
>boustrophedonically ('as the ox turns' - in plowing)
>
<G>What a wonderful word.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73ih3c$jg9@dfw-ixnews3.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net>`

```

>>>(that is, serpentine fashion, like a printer)
>>
…[4 more quoted lines elided]…
>>
On Wed, 25 Nov 1998 21:28:23 -0500, "Donald Tees"
<donald@willmack.com> wrote:
>
><G>What a wonderful word.
>
Dunno.  It's all Greek to me <g>!


Rick Anderson
Seattle
anderson  ï¿½atï¿½  pobox  ï¿½fullstopï¿½  com
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net>`

```
On Wed, 25 Nov 1998 21:28:23 -0500, "Donald Tees"
<donald@willmack.com> enlightened us:

>boustrophedonically

Actually that is not the proper form for the word.  The American
Heritage Dictionary has:

bouï¿½stroï¿½pheï¿½don  n. 1. An ancient method of writing in which the
lines are inscribed alternately from right to left and from left to
right. [From Greek boustrophedon turning like an ox while plowing.

The adjective is boustrophedonic.  There is no adverb form of this
word.  But still a wonderful word.  Now if I could just use it in a
normal conversation :)

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Today's tip for annoying your relatives over the holidays:
Make beeping noises when you back up.


 Steve
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 12)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb2qqMxG#GA.96@upnetnews03>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net>`

```

SkippyPB wrote in message
<9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.ne
t>...
>On Wed, 25 Nov 1998 21:28:23 -0500, "Donald Tees"
><donald@willmack.com> enlightened us:
…[11 more quoted lines elided]…
>word.

Apparently there is now<g>.  English is a living language that adds and
invents adverbs continuously.  I believe that once a person has described a
habit of reading a newspaper column boustrophedonically, the audience can
"get the drift" if the other usages of the word are understood.

But still a wonderful word.  Now if I could just use it in a
>normal conversation :)

How about:

A few posters in this ng take a boustrophedonic approach toward the topic of
some threads.

or

The topic of some threads in this ng are approached boustrophedonically by
some posters.


You might even be able to work it into a commentary involving Bill Clinton,
obfuscations/explanations and draft avoidance (evasion?)

>Regards,
>
…[8 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 13)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73q0e9$qip$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <eb2qqMxG#GA.96@upnetnews03>`

```
Dennis J. Minette wrote in message ...

>Apparently there is now<g>.  English is a living language that adds and
>invents adverbs continuously.  I believe that once a person has described a
>habit of reading a newspaper column boustrophedonically, the audience can
>"get the drift" if the other usages of the word are understood.


Is it true that boustophedonically reading palindromes causes
you to go cross-eyed?
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 14)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OXllC39G#GA.261@upnetnews03>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <eb2qqMxG#GA.96@upnetnews03> <73q0e9$qip$1@news.igs.net>`

```

Donald Tees wrote in message <73q0e9$qip$1@news.igs.net>...
>Dennis J. Minette wrote in message ...
>
>>Apparently there is now<g>.  English is a living language that adds and
>>invents adverbs continuously.  I believe that once a person has described
a
>>habit of reading a newspaper column boustrophedonically, the audience can
>>"get the drift" if the other usages of the word are understood.
…[4 more quoted lines elided]…
>

Absolutely - happens to me all the time!
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 12)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3660ec8b.39824359@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net>`

```
'Twas Fri, 27 Nov 1998 17:49:11 GMT, when swiegand@neo.rr.com (SkippyPB)
illuminated comp.lang.cobol thusly:

>The adjective is boustrophedonic.  There is no adverb form of this
>word.

How can this be.  AFAIK, there is no adjective in the English language
which can't be turned into an adverb.  Does your dictionary explicitly say
that boustrophedonically (or any other adverb) doesn't exist ?
```

###### ↳ ↳ ↳ boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 13)_

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3661613F.E71E9553@ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews>`

```
My two cents:
The site
http://huis.huis.hiroshima-u.ac.jp/Computer/Jargon/LexiconEntries/Boustrophedon.html
contains this definition and reference to the adverbial form.

boustrophedon
[from a Greek word for turning like an ox while plowing] n. An ancient method
of writing using alternate left-to-right and right-to-left lines. This term is

actually philologists' techspeak and typesetters' jargon. Erudite hackers use
it for an optimization performed by some computer typesetting software
and moving-head printers. The adverbial form `boustrophedonically' is also
found (hackers purely love constructions like this).



Randall Bart wrote:

> 'Twas Fri, 27 Nov 1998 17:49:11 GMT, when swiegand@neo.rr.com (SkippyPB)
> illuminated comp.lang.cobol thusly:
…[15 more quoted lines elided]…
> l    |/ MS^7=6/28/107   http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 14)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36617174.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews> <3661613F.E71E9553@ix.netcom.com>`

```
John Trifon wrote in message <3661613F.E71E9553@ix.netcom.com>...
>My two cents:
>The site
>http://huis.huis.hiroshima-u.ac.jp/Computer/Jargon/LexiconEntries/Boustroph
edon.html
>contains this definition and reference to the adverbial form.
>
>boustrophedon
>[from a Greek word for turning like an ox while plowing] n. An ancient
method
>of writing using alternate left-to-right and right-to-left lines. This term
is
>
>actually philologists' techspeak and typesetters' jargon. Erudite hackers
use
>it for an optimization performed by some computer typesetting software
>and moving-head printers. The adverbial form `boustrophedonically' is also
>found (hackers purely love constructions like this).



Since I started this, I may be allowed a word here. Of course, there is an
adverbial form; any adjective can be turned into an adverb by adding "ly".
As for practical use of the word, I once participated in building the
Stanford Solar Observatory. We had a 'scanning table' that stepped an
aperture (a small hole to select a portion of the solar image) a 0.01 of
an inch for each measurement. The stepping was boustrophedonically
to minimize mechanical forces.
```

###### ↳ ↳ ↳ Re: boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 15)_

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73shnd$l1t@dfw-ixnews3.ix.netcom.com>`
- **References:** `<19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews> <3661613F.E71E9553@ix.netcom.com> <36617174.0@news1.ibm.net>`

```
On Sun, 29 Nov 1998 10:08:13 -0600, "Leif Svalgaard"
<leif@ibm.net> wrote:

>Since I started this, I may be allowed a word here. Of course, there is an
>adverbial form; any adjective can be turned into an adverb by adding "ly".
…[3 more quoted lines elided]…
>an inch for each measurement.

>The stepping was boustrophedonically to minimize mechanical forces.

Nope!  You want an adjective here; viz., "The stepping was
boustrophedonic ...." -- it is a predicate adjective.

However: "The stepping was [PERFORMed] boustrophedonically ...."

[There!  We kept this baby on topic!! --RA]

Rick Anderson
Seattle
anderson  ï¿½atï¿½  pobox  ï¿½fullstopï¿½  com
```

###### ↳ ↳ ↳ Re: boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 16)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3661d80b.0@news1.ibm.net>`
- **References:** `<19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews> <3661613F.E71E9553@ix.netcom.com> <36617174.0@news1.ibm.net> <73shnd$l1t@dfw-ixnews3.ix.netcom.com>`

```
Richard Anderson wrote in message <73shnd$l1t@dfw-ixnews3.ix.netcom.com>...
>On Sun, 29 Nov 1998 10:08:13 -0600, "Leif Svalgaard"
><leif@ibm.net> wrote:
…[15 more quoted lines elided]…
>[There!  We kept this baby on topic!! --RA]


Of course, I meant 'was done bou...' or as you say PERFORMed.
Gimme a break :-)
Leif
```

###### ↳ ↳ ↳ Re: boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 17)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36640AFA.AB4C006D@IMN.nl>`
- **References:** `<19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews> <3661613F.E71E9553@ix.netcom.com> <36617174.0@news1.ibm.net> <73shnd$l1t@dfw-ixnews3.ix.netcom.com> <3661d80b.0@news1.ibm.net>`

```
Leif did it correct. He wrote:

> >>The stepping was boustrophedonically to minimize mechanical forces.

As usual in COBOL syntax, non-underlined words are not mandatory.

> >However: "The stepping was [PERFORMed] boustrophedonically ...."

Hey, I remember my school teacher telling that the"ly" was required in case of a
verb:
The stepping was xxx. It stepped xxxLY. In natural speech, naturally spoken.

Is my grammar still correct[ly used]?

Jumpingly Froggedly yours.
Frog
```

###### ↳ ↳ ↳ Re: boustrophedon - Was Is one period per paragraph a good idea?

_(reply depth: 18)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<743jmi$jf9$1@news.igs.net>`
- **References:** `<19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews> <3661613F.E71E9553@ix.netcom.com> <36617174.0@news1.ibm.net> <73shnd$l1t@dfw-ixnews3.ix.netcom.com> <3661d80b.0@news1.ibm.net> <36640AFA.AB4C006D@IMN.nl>`

```
COBOL Frog (Huib Klink) wrote in message <36640AFA.AB4C006D@IMN.nl>...

>Hey, I remember my school teacher telling that the"ly" was required in case
of a
>verb:
>The stepping was xxx. It stepped xxxLY. In natural speech, naturally
spoken.
>Is my grammar still correct[ly used]?


Yes.  The "ly" changes it from an adjective to an adverb.  My
old man was a stickler for grammar; I can remember being told
a thousand times at the dinner table: "you did not do
"REAL GOOD", you did "REALLY WELL".
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 13)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9E4FB672FA3DAADA.80EEC00339582198.189DD133D93777E9@library-proxy.airnews.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365c7f59.0@news1.ibm.net> <73idtu$crh$1@news.igs.net> <9B2619169B4A3C12.FD7265450D18EA10.CFD9F7670F8B6A55@library-proxy.airnews.net> <3660ec8b.39824359@netnews>`

```
On 29 Nov 1998 06:47:22 GMT, Barticus@att.spam.net (Randall Bart)
enlightened us:

>'Twas Fri, 27 Nov 1998 17:49:11 GMT, when swiegand@neo.rr.com (SkippyPB)
>illuminated comp.lang.cobol thusly:
…[6 more quoted lines elided]…
>that boustrophedonically (or any other adverb) doesn't exist ?

It does not show boustrophedonically as a valid construct of the word
boustrophedonic.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Today's tip for annoying your relatives over the holidays:
Make beeping noises when you back up.


 Steve
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c7f5c.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net>`

```
Donald Tees wrote in message <73hli7$sms$1@news.igs.net>...
>Judson McClendon wrote in message ...
>>We don't need column 7.  From your other comments, I think you might
…[3 more quoted lines elided]…
>>the 80-column punched card? :-)


>As for the 80 columns ... have you ever tried reading anything
>in a natural language where the line length is far too wide? It
>makes lines very difficult to read, regardless of language.

News papers use narrow columns for easier reading too.

>I could not figure out why, until I programmed the firmware for
>a dot matrix printer.  While I was doing that project, I found myself
>reading a book, and it occurred to me that I read bi-directionally
>(that is, serpentine fashion, like a printer)

there is a wonderful English word for that:
boustrophedonically ('as the ox turns' - in plowing)

>as long as the number of words per line does not exceed six
>or seven.  When the word count starts to exceed that, the brain
…[6 more quoted lines elided]…
>readability quite a bit.


I agree with that. I have seen C-programs where some lines are
200+ characters long. Even on a 21 inch screen, these are next
to impossible to read.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CC480.980FA01B@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Judson McClendon wrote in message ...
…[10 more quoted lines elided]…
> the asterisk, just for traditions sake.  Perhaps "**".

Being just a little nitpickey, that's not how an Assembler statement is
terminated. Assembler has an optional name field (which starts in column
one, if present), one or more blanks, an op code (might be a macro), one
or more blanks, operand(s) (also optional under some circumstances), one
or more blanks. The final "one or more blanks" terminates what is being
assembled, but doesn't terminate the statement. We all code meaningful
comments, don't we? And these may spill over to the next several card
images, so long as you code a non-blank in column 72. (of course, if the
operand(s) ends in a comma and column 72 is non-blank, the operand is
continued onto the next statement (in column 16)).

As far as permitting comments on the same line as code (free form?), how
about the "/* this is a comment */" notation used by so many other (IBM,
at least) languages? Even IDCAMS uses this!

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73iq7r$l8f$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365CC480.980FA01B@att.net>`

```
William Lynch wrote in message <365CC480.980FA01B@att.net>...

What assembler is that?  Can't recall ever seeing a scheme like
that.  Most of the 8086 stuff will accept anything from a semi
colin on (to the end of the line) as comment. As I remember, most
Dec machines are the same.  I've used a couple of microchip
assemblers that used asterisks ...

>Being just a little nitpickey, that's not how an Assembler statement is
>terminated. Assembler has an optional name field (which starts in column
…[3 more quoted lines elided]…
>assembled, but doesn't terminate the statement. We all code meaningful
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Wb72.37$Lx2.274@news1.atlantic.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365CC480.980FA01B@att.net> <73iq7r$l8f$1@news.igs.net>`

```

Donald Tees wrote in message <73iq7r$l8f$1@news.igs.net>...
>William Lynch wrote in message <365CC480.980FA01B@att.net>...
>
…[12 more quoted lines elided]…
>
Most, if not all, assemblers where each source statement is considered
to be a punched card image. Generally, these assemblers originated from
the mainframe.

OTOH, assemblers which originated from mini-computers tend to have
less restrictive formats since the input was variable length lines from a
teletype.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E19E3.BD880866@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net> <365CC480.980FA01B@att.net> <73iq7r$l8f$1@news.igs.net>`

```
Donald Tees wrote:
> 
> William Lynch wrote in message <365CC480.980FA01B@att.net>...
> 
> What assembler is that?  Can't recall ever seeing a scheme like
> that.

Sorry, I should have included my standard disclaimer about being IBM
mainframe oriented. By "Assembler" I meant IBM's S/360 Assembler and its
successors. What I said is true for them, including HLASM. I forget,
repeatedly, how diverse this NG and USENET are.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Wb72.36$Lx2.274@news1.atlantic.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <73hli7$sms$1@news.igs.net>`

```

Donald Tees wrote in message <73hli7$sms$1@news.igs.net>...
>
>I like that idea too.  As long as we do not need an "end-comment"<G>.
…[3 more quoted lines elided]…
>
** is not a good idea. That is the combination for exponentiation; as in:

    compute nth-power = x ** n
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#kfSLbVG#GA.286@upnetnews05>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia>`

```

Judson McClendon wrote in message ...
>Howard Brazee wrote:
>>
…[11 more quoted lines elided]…
>the 80-column punched card? :-)

Well,  there WAS a cute, little 96-hole card available from IBM small
systems for awhile, but they never really caught on because of progress in
use of key-to-tape and key-to-disk devices, as well as a rapidly increasing
use of on-line data entry.

>--
>Judson McClendon      judmc123@bellsouth.net  (remove numbers)
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E1B60.401A6BA8@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <#kfSLbVG#GA.286@upnetnews05>`

```
"Dennis J. Minette" wrote:
(snip)
> Well,  there WAS a cute, little 96-hole card available from IBM small
> systems for awhile, but they never really caught on because of progress in
> use of key-to-tape and key-to-disk devices, as well as a rapidly increasing
> use of on-line data entry.

Interestingly enough, these 96-column cards haven't disappeared yet. The
ATM at my local bank branch issues these cards as the receipt (at least
they did in Sept. 1997). I hung on to the card for sentimental reasons.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f46c6.20428914@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <#kfSLbVG#GA.286@upnetnews05> <365E1B60.401A6BA8@att.net>`

```
'Twas 27 Nov 1998 03:23:30 GMT, when William Lynch <wblynch@att.net>
illuminated comp.lang.cobol thusly:

>"Dennis J. Minette" wrote:
>(snip)
…[7 more quoted lines elided]…
>they did in Sept. 1997). I hung on to the card for sentimental reasons.

AFAIK, all IBM ATMs use 96-column cards for receipts.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#xb1oMxG#GA.154@upnetnews03>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <#kfSLbVG#GA.286@upnetnews05> <365E1B60.401A6BA8@att.net>`

```

William Lynch wrote in message <365E1B60.401A6BA8@att.net>...
>"Dennis J. Minette" wrote:
>(snip)
>> Well,  there WAS a cute, little 96-hole card available from IBM small
>> systems for awhile, but they never really caught on because of progress
in
>> use of key-to-tape and key-to-disk devices, as well as a rapidly
increasing
>> use of on-line data entry.
>
>Interestingly enough, these 96-column cards haven't disappeared yet. The
>ATM at my local bank branch issues these cards as the receipt (at least
>they did in Sept. 1997). I hung on to the card for sentimental reasons.


But those receipts don't have any holes punched in them, do they? Maybe your
bank got a volume discount on a 20 year supply of those blank System/3 cards
and is just using them up??

Dennis
CCCO

>Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3660C3DE.BD4120B3@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <365c2333.0@news3.uswest.net> <6sW62.5417$w_6.3243227@news2.mia> <365C3D11.62943D24@home.com> <N%X62.5436$w_6.3293801@news2.mia> <#kfSLbVG#GA.286@upnetnews05> <365E1B60.401A6BA8@att.net> <#xb1oMxG#GA.154@upnetnews03>`

```
"Dennis J. Minette" wrote:
> 
(snip)
> 
> But those receipts don't have any holes punched in them, do they? Maybe your
> bank got a volume discount on a 20 year supply of those blank System/3 cards
> and is just using them up??

You're right, no holes (I think I'd jump out of my skin if I ever heard
an ATM making 514/519 noises <g>).

It's just a printed receipt on oddly shaped, heavy stock. Maybe you're
right about the bank buying a 20-year supply of the cards; I hope they
bought sufficient ATMs & spare parts to last that long! Of course, the
cards are pre-printed as a "Transaction Record" with card no., date,
amount, etc.

Bill Lynch
```

###### ↳ ↳ ↳ New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com>`

```
OK folks, it sound like time for me to tell you what IS in the draft of the
next Standard for "reference format".  (And to let you know that IMHO there
is ZILCH chance of dramatically changing this to keep the A-margin/B-margin
stuff and get rid of the period instead.)

1) There are two types of format supported
   - fixed format source code (similar to the existing stuff)
   - free format source code

2) Fixed format source code has gotten rid of the entire concept of
A-margin/B-margin.  (By the way the "r-margin" which most of you think of as
column 72 in an 80 byte source code is NOT in the Standard and never has
been - as to where it is.  Any compiler vendor could make this column 81,
132, or anything else they want - even today)

3) There is a new inline comment indicator "*>" which allows you to make the
end (but not the middle) of any line a comment.  This can also be used in
free format source code to make an entire line a comment.

4) There is a  new >>PAGE compiler directive that takes the place of "/" in
column 7 for free format source code (and can also be used in fixed format
source code)

5) There is a new >>D indicator to take the place of "D" in column 7 to
indicate debugging lines (which are going to be made obsolete anyway -
because "conditional compilation" will replace them - with even more
powerful)

6) You can now continue alphanumeric (and a bunch of the new type of)
literal by placing a "-" at the end of the Continued line (in both fixed and
free format source code), for example
      Move  "This is a single "-
                  "literal" to message-area

(Note: There is also a new feature of "concatenated" literals that IN MOST
CASES works the same way. For example
    Move  "This is a concatenated" & "literal" to message-area

7) Given "*>" ">>PAGE"  ">>D" and the new way of continuing literal, there
is no need to use any "column 7" stuff - although it has been kept for fixed
format source code.

Note: Continuation of COBOL words has been made archaic or obsolete (I can't
remember which) - but this really is NOT done very often or in most "good"
programming.  This is what lets you code today something like:
       Mo
 -        ve this to th
 -        at

8) There is a new compiler directive that lets you switch back and forth
between fixed and free format source code in the same compilation. Among
other things that this  whole feature has been designed with is the fact
that IF you code a COPY member so that it only has source code in the
"program text area" (what most of you think of as columns 8 thru 72) then
that same text can be copied "correctly" into either fixed or free format
source code.

   *****

I hope this little presentation has given you a glimpse into what is coming
in the next Standard (and what many vendors already have or have a similar
feature to - as an extension).
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73ie51$cs9$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`

```

William M. Klein wrote in message <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>...
>OK folks, it sound like time for me to tell you what IS in the draft of the
>next Standard for "reference format".  (And to let you know that IMHO there
>is ZILCH chance of dramatically changing this to keep the A-margin/B-margin
>stuff and get rid of the period instead.)


It all sounds fine, actually.  Very workable and close enough
that there should not be a huge job switching styles. I like the
continuation stuff.  That has always been a hack.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C7474.2C22001B@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`

```
> 4) There is a  new >>PAGE compiler directive that takes the place of "/" in
> column 7 for free format source code (and can also be used in fixed format
> source code)

I wasn't sure whether the "/" was standard COBOL.  I know EJECT is an
IBM extension, but I thought I had seen where "/" didn't work before.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f46bc.20419302@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7474.2C22001B@home.com>`

```
'Twas Wed, 25 Nov 1998 14:19:48 -0700, when Howard Brazee
<NOSPAMbrazee@home.com> illuminated comp.lang.cobol thusly:

>> 4) There is a  new >>PAGE compiler directive that takes the place of "/" in
>> column 7 for free format source code (and can also be used in fixed format
…[3 more quoted lines elided]…
>IBM extension, but I thought I had seen where "/" didn't work before.

In pre-ANSI COBOL, the indicator area (column 7) was for continuation
only.  Because of the screwy specification of NOTE, COBOL-68 added "*" for
comments.  I'm not sure where "/" for page eject was first used, but since
the source listing was "beyond the purview of the standard" until the
current draft, I don't know what ANSI could have had to say on the
subject.  It has been a comment indicator in every COBOL-74 or COBOL-85
compiler I've used.  
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C7538.E98BC1F2@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`

```
> 5) There is a new >>D indicator to take the place of "D" in column 7 to
> indicate debugging lines (which are going to be made obsolete anyway -
> because "conditional compilation" will replace them - with even more
> powerful)

I haven't heard of this even more powerful conditional compilation. 
What are its features?
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hvvk$kb4@dfw-ixnews7.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com>`

```

Howard Brazee wrote in message <365C7538.E98BC1F2@home.com>...
>> 5) There is a new >>D indicator to take the place of "D" in column 7 to
>> indicate debugging lines (which are going to be made obsolete anyway -
…[4 more quoted lines elided]…
>What are its features?

Conditional compilation is a way of including or excluding specific parts of
your code from ever being compiled.  It assumes that you have things called
"conditional variables"  (which are close to - but not quite the same as
"constants" as used by many vendors today). These variables can be defined
in your source code (or I suspect most vendors will also let you pass them
to the compiler).  Then you can test either for their existence or for
specific values.  (All of this is available today in several PC compilers).
For example you can have (trivial example)

>>If quarter-report defined
     Move "Q" to report-type
     Perform Quarter-report-summary
>>else
    Move "D" to report-type
    Perform Daily-report-processing
>>Evaluate Day-of-Week
>>when 1 thru 5
      Move "Weekday" to Heading-type
>>when other
      Move "Weekend" to Heading-type
>>end-evaluate
>>end-if

Note: the testing of the quarter-report and Day-Of-Week conditional
variables is done at COMPILE-TIME so that you can have a single source
program that will actually product 2 or more "object programs" depending on
what variables are passed to it.

This was a simple case (which probably would be done in another manner in a
"real" program) but should show you what the technique looks like.  (I also
haven't tried to "compile" this sample - so it may even have syntax errors.)
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73iec9$d65$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com>`

```

William M. Klein wrote in message <73hvvk$kb4@dfw-ixnews7.ix.netcom.com>...

While I really like the conditional compilation idea, I am
not fussy about the syntax chosen.  Is that the methodology
that is going to be used?

>Conditional compilation is a way of including or excluding specific parts
of
>your code from ever being compiled.  It assumes that you have things called
>"conditional variables"  (which are close to - but not quite the same as
>"constants" as used by many vendors today). These variables can be defined
>in your source code (or I suspect most vendors will also let you pass them
>to the compiler).  Then you can test either for their existence or for
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73ifap$2mh@dfw-ixnews7.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <73iec9$d65$1@news.igs.net>`

```

Donald Tees wrote in message <73iec9$d65$1@news.igs.net>...
>
>William M. Klein wrote in message <73hvvk$kb4@dfw-ixnews7.ix.netcom.com>...
…[4 more quoted lines elided]…
>
  <original note snipped>

Yes, this is the style being used for ALL "compiler directing statements".
Folks, when reading the following, please note that the initial ">"
characters are COBOL syntax and NOT part of replying to NG posts.

ALL the compiler directing statements start with ">>".  This takes the place
of "$SET" (used by Micro Focus) or CBL/PROCESS (used by IBM) and a variety
of other indicators used by other vendors.  Therefore, you can have things
like

   Conditional compilation
       >>IF
       >>EVALUATE
       >>DEFINE

   Listing control
      >>PAGE
      >>LIST ON

   Flagging directives
       >>FLAG-85      (this checks for differences from '85 Standard
interpretations, similar to IBM FLAGMIG option)

  Exception checking (turn on or off)
     >>TURN

Does this take some of the "fuzziness" out of my original post (or did I
miss what your real question was)?
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73iqbs$l93$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <73iec9$d65$1@news.igs.net> <73ifap$2mh@dfw-ixnews7.ix.netcom.com>`

```

William M. Klein wrote in message <73ifap$2mh@dfw-ixnews7.ix.netcom.com>...

>Does this take some of the "fuzziness" out of my original post (or did I
>miss what your real question was)?


I think I just missed something first read.  Must be the pot,
maybe just old age ...
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** Binyamin_Dissen@theoffice.net (Binyamin Dissen)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f378c.41115678@news.netvision.net.il>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <73iec9$d65$1@news.igs.net> <73ifap$2mh@dfw-ixnews7.ix.netcom.com>`

```
On Wed, 25 Nov 1998 18:43:47 -0800 "William M. Klein" <wmklein@ix.netcom.com>
wrote:

   [ snipped ]

:>ALL the compiler directing statements start with ">>".  This takes the place
:>of "$SET" (used by Micro Focus) or CBL/PROCESS (used by IBM) and a variety
:>of other indicators used by other vendors.  Therefore, you can have things
:>like

:>   Conditional compilation
:>       >>IF
:>       >>EVALUATE
:>       >>DEFINE

:>   Listing control
:>      >>PAGE
:>      >>LIST ON

:>   Flagging directives
:>       >>FLAG-85      (this checks for differences from '85 Standard
:>interpretations, similar to IBM FLAGMIG option)

:>  Exception checking (turn on or off)
:>     >>TURN

:>Does this take some of the "fuzziness" out of my original post (or did I
:>miss what your real question was)?

I hope that isn't all the constructs.

I don't see a looping construct.

      >>PERFORM VARYING %I FROM 1 TO 10
             05  TABLE-FIELD-%I     PIC X(10)
      >>END-PERFORM

There will also be a need for some kind of assignment and arithmetic
processing.

Just the IF, DEFINE and EVALUATE will not really allow much conditional
compilation.
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73kj5q$him@dfw-ixnews9.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <73iec9$d65$1@news.igs.net> <73ifap$2mh@dfw-ixnews7.ix.netcom.com> <365f378c.41115678@news.netvision.net.il>`

```

Binyamin Dissen wrote in message
<365f378c.41115678@news.netvision.net.il>...
>On Wed, 25 Nov 1998 18:43:47 -0800 "William M. Klein"
<wmklein@ix.netcom.com>
>wrote:
>
>   [ snipped ]
>
>:>ALL the compiler directing statements start with ">>".  This takes the
place
>:>of "$SET" (used by Micro Focus) or CBL/PROCESS (used by IBM) and a
variety
>:>of other indicators used by other vendors.  Therefore, you can have
things
>:>like
>
…[37 more quoted lines elided]…
>Director, Dissen Software, Bar & Grill - Israel

Assignment (including arithmetic expressions) is supported thru the >>DEFINE
statement.  However, there is no looping (or GO TO - or even "procedure
labeling)) directive (as I recall).   There are also ways to get
"parameters" and "conditional variables" into your source code. There are
several others directives that I haven't listed as well - but not all that
many. For those of you familiar with other languages, there is NO attempt to
make this a "full macro" language like PL/I - for example.

If you are interested in the actual details of this facility and as the
current draft is no longer available online, you might want to contact the
chair of J4 for information on obtaining a hard-copy.  He can be reached at
    das@microfocus.com
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 11)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f46b4.20411777@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <73iec9$d65$1@news.igs.net> <73ifap$2mh@dfw-ixnews7.ix.netcom.com> <365f378c.41115678@news.netvision.net.il> <73kj5q$him@dfw-ixnews9.ix.netcom.com>`

```
'Twas Thu, 26 Nov 1998 14:01:38 -0800, when "William M. Klein"
<wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:

>Binyamin Dissen wrote in message
><365f378c.41115678@news.netvision.net.il>...

>>      >>PERFORM VARYING %I FROM 1 TO 10
>>             05  TABLE-FIELD-%I     PIC X(10)
>>      >>END-PERFORM

Use this 

               05  TABLE-FIELD        PIC X(10)  OCCURS 10.

>For those of you familiar with other languages, there is NO attempt to
>make this a "full macro" language like PL/I - for example.

Pity, but we can add it in COBOL 2023.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365D3B2B.68E05E80@zip.com.au>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com>`

```
Well the C preprocessor comes to Cobol.

I have always thought about running CCP followed by Cobol but it would
create totally non standard COBOL.

One of the special features is the use of a define on the command line
so that you can include debugging code:

	cc fred.c  -DDEBUG

	#ifdef DEBUG
		do something
	#endif

Is there something similar.  Note that it is handy to have multiple
flags for each type of debugging interface, windowing code, or some
special calculation.

Now all we need is an ASSERT macro that makes it easy to debug:

	ASSERT(I_have_not_mucked_up, display 'Yes you have @ T300-x')

Ken

William M. Klein wrote:
> 
> Conditional compilation is a way of including or excluding specific parts of
…[29 more quoted lines elided]…
> haven't tried to "compile" this sample - so it may even have syntax errors.)
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73kjjm$hrc@dfw-ixnews9.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <365D3B2B.68E05E80@zip.com.au>`

```
Yes, the >>IF DEFINED facility lets you test for the existence (or not) of a
conditional variable (and your example is WHY the committees have been able
to make debugging lines obsolete - with this new facility)

No, there is no "display" statement for conditional compilations (although
this was suggested relatively recently).  Having used Micro Focus'
conditional compilation, I am quite certain that most vendors will end up
having to add this as an extension.

What does the C "assert" statement do (if something more than just a
display)?  Being non-C-literate, I don't know if the new facility has this
function or not.

Finally, as stated in another note, the new facility is NOT intended to be a
full "macro preprocessor" - although there certainly is room for future
enhancements (or vendor extensions) to make it closer to one.

Ken Foskey wrote in message <365D3B2B.68E05E80@zip.com.au>...
>Well the C preprocessor comes to Cobol.
>
…[24 more quoted lines elided]…
>> Conditional compilation is a way of including or excluding specific parts
of
>> your code from ever being compiled.  It assumes that you have things
called
>> "conditional variables"  (which are close to - but not quite the same as
>> "constants" as used by many vendors today). These variables can be
defined
>> in your source code (or I suspect most vendors will also let you pass
them
>> to the compiler).  Then you can test either for their existence or for
>> specific values.  (All of this is available today in several PC
compilers).
>> For example you can have (trivial example)
>>
…[16 more quoted lines elided]…
>> program that will actually product 2 or more "object programs" depending
on
>> what variables are passed to it.
>>
>> This was a simple case (which probably would be done in another manner in
a
>> "real" program) but should show you what the technique looks like.  (I
also
>> haven't tried to "compile" this sample - so it may even have syntax
errors.)
>
>
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E84DD.77F2E159@zip.com.au>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <365D3B2B.68E05E80@zip.com.au> <73kjjm$hrc@dfw-ixnews9.ix.netcom.com>`

```
William M. Klein wrote:
> 
> 
> What does the C "assert" statement do (if something more than just a
> display)?  Being non-C-literate, I don't know if the new facility has this function or not.
> 

Basically the asert macro is a simple way of saying
	ASSERT( condition, something )

>>IFDEF DEBUG
  >>IF  condition
	something
	display  compile-file-id compile-line-number
        STOP RUN 9999
  >>ENDIF
>>END-IF

It just saves a heap of typing that's all.  If you have some macro
expansions then this should not be to hard to implement.

I am still waiting for my HTML cobol reference  :->
```

###### ↳ ↳ ↳ Assertion

_(reply depth: 9)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f46ac.20403703@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <365D3B2B.68E05E80@zip.com.au> <73kjjm$hrc@dfw-ixnews9.ix.netcom.com>`

```
'Twas Thu, 26 Nov 1998 14:09:02 -0800, when "William M. Klein"
<wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:

>What does the C "assert" statement do (if something more than just a
>display)?  Being non-C-literate, I don't know if the new facility has this
>function or not.

ASSERT is a piece of debugging code.  I didn't know it was a feature of
the C language; at Unisys it was a macro that we used in ALGOL and NEWP
programs.

A simple assertion has only one boolean parameter.  When the programmer is
just sure that a certain condition will be true at this point in the code,
unless something is screwed up, he puts in a ASSERT statement.  If the
condition is true, nothing happens.  If the condition is false, the
program blows up.  Ken's example of ASSERT includes an error message to be
displayed when the assertion is false.

An example in COBOL:

    PERFORM SOME-PARAGRAH VARYING COUNT FROM 1 UNTIL COUNT > 10
    ASSERT COUNT = 11

Under normal conditions the assertion will be true, and nothing will
occur.  If SOME-PARAGRAPH changes COUNT, then the program will blow up.

As I said, this is debugging code.  Once your program is debugged, all the
assertions should be true.  So when you compile without debugging the
ASSERTs turn into CONTINUE statements.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ube72.848$Pc1.1242141@news.rdc1.on.wave.home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <365D3B2B.68E05E80@zip.com.au>`

```

Ken Foskey wrote in message <365D3B2B.68E05E80@zip.com.au>...
>Well the C preprocessor comes to Cobol.
>
…[14 more quoted lines elided]…
>special calculation.


Well, there's finally a legitimate reason to talk about my company's
product, Netron Fusion http://www.netron.com/products/fusion.htm

Fusion is a bunch of software development tools. The Fusion processor can be
loosely described as a macro preprocessor for any language, with a bias
toward COBOL.. It is somewhat more than just a macro preprocessor since it
applies OO techniques to the assembly of source code.

It assembles code from reusable components which we call frames. For COBOL
you can think of them as copybooks with additional operators.

By the way, for COBOL, it uses the % sign to delimit comments on the end of
lines. The preprocessor strips them out before feeding the result to a COBOL
compiler.

Visit http://www.netron.com/frames.htm for a better introduction to frame
technology.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3661b201.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C7538.E98BC1F2@home.com> <73hvvk$kb4@dfw-ixnews7.ix.netcom.com> <365D3B2B.68E05E80@zip.com.au>`

```
Ken Foskey wrote in message <365D3B2B.68E05E80@zip.com.au>...
>Well the C preprocessor comes to Cobol.
>I have always thought about running CCP followed by Cobol but it would
…[14 more quoted lines elided]…
>> Conditional compilation is a way of including or excluding specific parts
of
>> your code from ever being compiled.  It assumes that you have things
called
>> "conditional variables"  (which are close to - but not quite the same as
>> "constants" as used by many vendors today). These variables can be
defined
>> in your source code (or I suspect most vendors will also let you pass
them
>> to the compiler).  Then you can test either for their existence or for
>> specific values.  (All of this is available today in several PC
compilers).
>> For example you can have (trivial example)
>>
…[16 more quoted lines elided]…
>> program that will actually product 2 or more "object programs" depending
on
>> what variables are passed to it.
>>
>> This was a simple case (which probably would be done in another manner in
a
>> "real" program) but should show you what the technique looks like.  (I
also
>> haven't tried to "compile" this sample - so it may even have syntax
errors.)


The ETK Toolset contains a Cobol Preprocessor that you can use today.
Go to http://www.etk.com then 'downloads', then 'syset'.

Here is the read me file for the Preprocessor to give you an idea of what
is possible:


The ETK Cobol Preprocessor SYSET:

Usage:  syset [filename...] [switch...]

SYSET preprocesses COB, CPY, or CBL files that contain non-portable or
special code. No file extensions should be given, as SYSET looks for .COB,
.CPY, or .CBL implicitly. If no parameters are given, SYSET shows a help
text. SYSET assumes a traditional Cobol source structure with sequence
numbers in columns 1-6, and comments in cols 73-80.

By default, SYSET looks in the current directory for files. You can set an
environment variable ETK to a path list to tell SYSET where to look, e.g.

set etk=d:\myproject1;c:\project2;

The output file is always written to the current directory. The output
file uses TABs. If you do not want this, use the exptab <file.ext> utility
supplied with this distribution to turn the TABs into spaces.

SYSET allows you to maintain a single version of a file which may have
several
target systems.  Uses for SYSET include: maintaining non-portable sources;
keep one schema or program with embedded versions for several systems;
manage debugging or scaffolding code (e.g. assertions).

SYSET should not be misused as a way of sneaking significant amounts of
non-portable code into a large application.  The problem here is that it is
very difficult to maintain the code for several targets in parallel.

Switches (can also be abbreviated to first letter):

/system:target          Specify target name; default is DEFAULT.

/filter:filename        Produce clean 'filtered' file as output to the file
                        given.

/output:filename        Direct the output to the file instead of changing
the
                        input file in place.

/type:filetype          Force filetype of COB, CPY, or CBL.

/parm:parameter         General parameter value passed to SYSET.

/quiet                  Suppress informational messages.

/restore                Restores defined values to their definitions.

Example:
> syset myprog /system:as400 /filtered:prog400

If you do not use the /filtered switch, SYSET copies the input file to
itself
(with appropriate safeguards against errors) looking for and acting upon
commands in comment lines as follows:

*#SET system...
        Defines the set of valid system names.  You must define
        such a command at the start of the file (e.g. after
        PROGRAM-ID).  Remember that a COBOL program cannot
        start with a comment line.

*#IF [system...] | logical expression
        Starts a block of code to be output if any of the listed
        systems is the current target.  If not, the code up to the
        next #ELSE, #ELIF, #CASE  or #END is commented.  If
        no system is specified, DEFAULT is assumed.

*#IFNOT [system...] | logical expression
        Starts a block of code to be output if none of the listed
        systems is the current target.

*#ELSE
        Includes/excludes the block of code until the next #END
        depending on the inverse of the condition on a previous
        #IF, #IFNOT, #ELIF or #CASE command.

*#ELIF [system...] | logical expression
        Combined #IF and #ELSE.  Note that #IFs and #IFNOTs
        cannot be nested.

*#EF [system...] | logical expression
        Same as #ELIF.

*#CASE [system...] | logical expression
        Like #ELIF, except that the first #IF may be a #CASE.

*#END
        Ends a block of code starting with an #IF, #IFNOT,
        #ELSE, #ELIF or #CASE.

*#END-IF
        Same as #END.

*#.
        Same as #END.

*#DEF definition = value    [ -- any comment text ]
        Defines a substitution value.  The definition must be a
        word with no embedded blanks.  The value can be any
        text, including other definitions (prefixed by #).  If a
        definition value refers to other definitions the substitution
        is made when the #DEF command is processed.  There
        must be white space on both sides of the equal sign.  An
        optional comment can follow a pair of dashes preceded by
        a space beginning at least three characters after the equal
        sign.  The comment extends to the end of the line.

*#FORMAT definition = value format
        Defines a substitution value like the #DEF command
        except that only characters specified in the format string
        are used.  The format string is a mixture of literal
        characters (except digits and the equal-sign which both
        must be escaped by being prefixed by `=') and of ranges
        of the form `from pos':`to pos'.  Characters from the value
        replace the range in the format string.  Example: value
        19951231, with format 5:6/7:8/3:4 results in 12/31/95.

*#LET definition = arithmetic expression
        Defines a substitution value as an arithmetic expression.

*#DROP definition : logical expression
        Defines a condition under which a line containing a
        reference to the definition name should be commented
        out.  A logical expression evaluates to 1 (true) or 0 (false).
        The line is commented out if the condition is true at the
        time when the line is processed.  There must be white
        space on both sides of the colon.  Use the #DROP
        command rather than tedious repetitions of the #IF
        command when several lines are conditioned upon
        definition values.

*#DROP definition relational operator arithmetic expression
        This is a simpler version of the #DROP command.  There
        must be white space on both sides of the relational
        operator.

*#INCLUDE filename [filetype]
        Continue input from the file given (the default filetype is
        that of the original input file) until it is exhausted, then
        return to the original input file where it left off.  Include
        files can be nested, but are meant for processing of pre-
        processor commands only (e.g. #SET, #DEFs, and
        #LETs), and are not copied to the output file.

*#SPACE character | NONE
        The character given is used as a 'hard space' allowing
        leading/trailing spaces in definition values.  NONE
        cancels a previous setting of the hard-space character,
        which is off when SYSET starts.

*#SKIP character | NONE
        The character given is used as a 'skip character' in the
        following sense: when a definition value containing skip
        characters is inserted, a skip character is not output, but
        instead causes the text that follows to be shifted one
        character position to the left, allowing fine control over
        the alignment of the resulting text.  NONE cancels a
        previous setting of the skip-character, which is off when
        SYSET starts.  If you use the #SKIP command, you must
        specify which target system was used when you recover
        the file, because definitions may have different numbers
        of skip characters for different targets.

*#DISPLAY text
        Displays the text even if the /QUIET switch is used.

*#CANCEL {text}
        Cancels the run of SYSET, recovering the original file.
        Displays an optional text even if the /QUIET switch is used.

*#* something
        A comment line which is excluded from filtered output

*# blank line
        A comment line which is excluded from filtered output.

**...
        This is a comment line which is kept in filtered output.

*
        Comment lines beginning with a single asterisk cannot be
        handled correctly by SYSET if the comment appears inside
        a block of code under control of an #IF, #IFNOT, #ELIF,
        #ELSE or #CASE command.

Note, that some command have aliases, e.g. #ELIF and #END, to allow
you to use a form you may feel more comfortable with.

Include files allow targets and definitions to be centrally defined and
managed.

Here is an example of an include file:

*#SET WANG AS400 GCOS7 GCOS8

*#CASE WANG
*#    DEF INTEGER = BINARY
*#    DEF SHORT   = #INTEGER
*#CASE AS400
*#    DEF INTEGER = PIC S9(5)  COMP
*#    DEF SHORT   = PIC S9(4)  BINARY
*#CASE GCOS7
*#    DEF INTEGER = PIC S9(4)  BINARY
*#    DEF SHORT   = #INTEGER
*#CASE GCOS8
*#    DEF INTEGER = COMP-6
*#    DEF SHORT   = COMP-1
*#ELSE
*#    DEF INTEGER = PIC S9(4)  COMP
*#    DEF SHORT   = #INTEGER
*#END

Four target systems are defined by the *#SET command.  Definitions of
INTEGER
and SHORT are then made for each of the four systems and (at the ELSE) for
all
other systems. Note, that at times a SHORT is simply the same as an INTEGER
SHORT = #INTEGER).  Use of another definition in a definition requires the
definition used to be defined first.

A block of code has been highlighted for the AS/400 target.  To improve
readability, SYSET commands can be indented as long as the '#' marker still
appears in column eight.

Here is sample code that uses the above include file:

 IDENTIFICATION DIVISION.
 PROGRAM-ID.    EDITPK.
 ...
 ENVIRONMENT DIVISION.

 CONFIGURATION SECTION.
 SOURCE-COMPUTER. PORTABLE.
 OBJECT-COMPUTER. PORTABLE.
*#INCLUDE EDITDEFS

 DATA DIVISION.

 WORKING-STORAGE SECTION.

 01  BEGIN-DYNAMIC-STORAGE       PIC X(4)   VALUE "<ETK".

 01  LINE-INDEX-LT-32K.
     02  LINE-INDEX              #SHORT     OCCURS 9998.

 01  DELETED-LINES.
     02  DELETED-INDEX           #INTEGER   OCCURS  150.

 01  PASTEBOARD-BUFFER.
     02  PASTED-LINE             PIC X(72)  OCCURS  500 TIMES.

 01  VARIOUS-CONSTANTS.
     02  WORK-FILE-NEAR-FULL     #INTEGER   VALUE +9500.
     ...

The following command replaces the defined keywords by their proper values
for
the AS/400 target:

> syset editpk /system:as400

If a different system (or none) is specified, SYSET first undoes the
substitutions for the previous system and then applies the definitions for
the new system; so, to get a version for the GCOS8 operating system,
execute:

> syset editpk /system:gcos8

The ETK COBOL editor marks lines with substituted SYSET definitions to warn
you to be careful when changing these.  In addition, you should first
recover
the original source if you are going to change the order of the definitions
or
move text around that has definitions.

To recover the original text without substituted definitions, use the
/RESTORE switch (which also overrides a possible /SYSTEM switch):

> syset editpk /restore

A convenient use of the /RESTORE switch is illustrated by the following
MS-DOS
.BAT file:

CALL SYSET %1 /R                     restore original
CALL EDIT  %1                        edit original
CALL SYSET %1 /S:PC                  make PC version
CALL COBOL %1                        compile PC version

If definitions used skip characters, you must specify the original target
system when you recover, eg.:

> syset editpk /system:as400 /restore

The expression used with the #IF, #IFNOT, #ELIF, #LET, and #DROP commands is
evaluated by CALCPK unless it contains strings in which case the value of
the
expression is the text itself.  Logical expressions contain relational
operators (like = or >=) and evaluate to 1 (true) or 0 (false).  The result
of an arithmetic expression is truncated to a signed integer with at most
9 digits.

Here are some examples of the use of expressions:

 ENVIRONMENT DIVISION.
*#SET BULL-TDS BULL-TP8 TEST

 CONFIGURATION SECTION.
*#IF BULL-TDS
*#   LET RECSIZE  = 8192
*#   LET NSIZE    = 510
*#   LET MAXLNK   = 32768 / #NSIZE
*#ELSE
*#   LET RECSIZE  = 8192
*#   LET NSIZE    = 256
*#   LET MAXLNK   = 32768 / #NSIZE
*#END
*#
*#*FIXED VALUES
*#   DEF IDSIZE   = 26    -- SIZE OF ID HEADER
*#
*#*DERIVED VALUES
*#   LET MAXBLK   =  #RECSIZE -  4
*#   LET NOD/REC  = (#RECSIZE -  #IDSIZE) / #NSIZE
*#   LET CTXRFILL = (#RECSIZE -  #IDSIZE) % #NSIZE)

 WORKING-STORAGE SECTION.

 01  CTXRIO-DATA.
     02  CTXRIO-KEY              PIC 9(6).
     02  CTXRIO-DATA-PART.
         03  CTXRIO-ID           PIC X(#IDSIZE).
         03  FILLER              REDEFINES  CTXRIO-ID.
             04  CTXRIO-NODE-COUNT
                                 PIC 9(2).
             04  CTXRIO-PROGRAM  PIC X(8).
             04  CTXRIO-USER-ID  PIC X(8).
             04  CTXRIO-HHMMSSCC PIC 9(8).
         03  CTXRIO-NODES                   OCCURS #NOD/REC.
             04  CTXRIO-NODE     PIC X(#NSIZE).
*#IF #CTXRFILL > 0
         03  FILLER              PIC X(#CTXRFILL).
*#END
     02  FILLER                  REDEFINES  CTXRIO-DATA-PART.
         03  CTXRIO-BLOCK-FREE   PIC 9(4).
         03  CTXRIO-BLOCK-MAP    PIC X      OCCURS #MAXBLK TIMES.

You could also have controlled the use of the line with the #CXTRFILL
definition value by declaring a #DROP condition:

*#DROP CTXRFILL :  #CTXRFILL = 0

This is particularly useful if several instances must be conditional;
an even simpler way can be used if the expression does not contain
other definitions:

*#DROP CTXRFILL = 0

The conditions also work with strings, like:

*#IF "#TARGET" = "PC"

There are several built-in standard values that can be used in expressions
(and be redefined at any time):

#SIZE
        This value is increased by the size of each PIC clause
        encountered.  OCCURS and REDEFINES clauses are not
        taken into account.

#LINE
        This value is incremented by one for each line output.

#DATE
        This value contains the date in the form YYYYMMDD.  Use
        the #FORMAT command to define a formatted synonym.

#PARM
        This value contains the general parameter passed from the
        command line.

#TARGET
        Evaluates to the target system specified with the /SYSTEM switch.

Instead of hard-coding IDSIZE in the example above, we could use the #SIZE
value as follows:

 01  CTXRIO-DATA.
     02  CTXRIO-KEY              PIC 9(6).
     02  CTXRIO-DATA-PART.
*#LET SIZE = 0
         03  CTXRIO-NODE-COUNT   PIC 9(2).
         03  CTXRIO-PROGRAM      PIC X(8).
         03  CTXRIO-USER-ID      PIC X(8).
         03  CTXRIO-HHMMSSCC     PIC 9(8).
*#LET NOD/REC  = (#RECSIZE -  #SIZE) / #NSIZE
*#LET CTXRFILL = (#RECSIZE -  #SIZE) % #NSIZE
         03  CTXRIO-NODES                   OCCURS #NOD/REC.
             04  CTXRIO-NODE     PIC X(#NSIZE).

Even better would be to store the value of #SIZE in an appropriate
intermediate
definition and then use that:

*#LET IDSIZE   = #SIZE
*#LET NOD/REC  = (#RECSIZE -  #IDSIZE) / #NSIZE

Definitions are not evaluated in lines beginning with two or more asterisks,
or with `*#', but are evaluated in all other comment lines.  This allows you
to trace the evolution of redefined or calculated definition values by
placing
them in comment lines.

Definitions are not evaluated in strings except if the string is on the
left-hand side of a comparison.

Definitions should not be equal to the beginning of other definitions, nor
should they contain blanks, the punctuation marks (".", ",", ";",
parentheses or
quotes) or the definition introducer itself ("#").  When building
expressions,
you should surround binary operators with white space just as COBOL
requires.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365C772B.1BB80DA3@home.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`

```
(By the way the "r-margin" which most of you think of as
> column 72 in an 80 byte source code is NOT in the Standard and never has
> been - as to where it is. 

I wonder how that became a de-facto standard.  Having duplicate sets of
sequence numbers is silly.  I wonder how vendors will treat right
margins with the new de-jour standard.

Some editors automatically put strings in particular columns when you
edit code.  Standards using those editors often have your work request
and/or initials in columns 73-80.  Maybe they will continue with "*>".
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365cd3ca.8846662@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com>`

```
On Wed, 25 Nov 1998 14:31:23 -0700, Howard Brazee
<NOSPAMbrazee@home.com> wrote:

>(By the way the "r-margin" which most of you think of as
>> column 72 in an 80 byte source code is NOT in the Standard and never has
…[8 more quoted lines elided]…
>and/or initials in columns 73-80.  Maybe they will continue with "*>".


For my shop (back then) 73-80 contained the program name and 1-6 the
sequence number.  (73-80 being 8 characters don't you know).  Anyway,
that way when the deckS dropped you could sequence them AND tell which
program the cards were from.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E1CB2.3CE2B3A1@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
(snip)
> 
> For my shop (back then) 73-80 contained the program name and 1-6 the
> sequence number.  (73-80 being 8 characters don't you know).  Anyway,
> that way when the deckS dropped you could sequence them AND tell which
> program the cards were from.

Undoubtedly for those occasions when the card tray contained more than
one program. This is real "Jurassic Park" stuff, I wonder if we can get
Speilberg interested? Maybe Kitty'd like to play the COBOL equivalent of
the paleobotanist (the Laura Dern role)?

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365e21bf.0@news1.ibm.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net> <365E1CB2.3CE2B3A1@att.net>`

```
William Lynch wrote in message <365E1CB2.3CE2B3A1@att.net>...
>Thane Hubbell wrote:
>> For my shop (back then) 73-80 contained the program name and 1-6 the
…[7 more quoted lines elided]…
>the paleobotanist (the Laura Dern role)?


In 1972 I wrote Fortran programs for a CDC6600 (supercomputer of its
day). Its compiler allowed two statements per card (an innovation then).
I once saw a program where each card was labeled with its line number
and the second statement on the card was a GOTO to the next card.
That way, if you dropped the desk (happened often...) you could just
scoop up the mess and insert it in the card reader, and the program
would still run as long as the original first card (which was green) was
still the first. Now, there was a good use of a goto statement.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73lemo$8mt$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net> <365E1CB2.3CE2B3A1@att.net> <365e21bf.0@news1.ibm.net>`

```
Is that the ultimate "alter" statement?
;<)

Leif Svalgaard wrote in message <365e21bf.0@news1.ibm.net>...
>William Lynch wrote in message <365E1CB2.3CE2B3A1@att.net>...
>>Thane Hubbell wrote:
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73msp0$i8e@dfw-ixnews7.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net> <365E1CB2.3CE2B3A1@att.net>`

```

William Lynch wrote in message <365E1CB2.3CE2B3A1@att.net>...
>Thane Hubbell wrote:
>>
…[12 more quoted lines elided]…
>Bill Lynch :-)

(For the IBM mainframers)  Doesn't (or didn't) Panvalet or Librarian use
columns 73-80 for storing version numbers - some how?
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10c902b275a640a49896b9@news.earthlink.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net> <365E1CB2.3CE2B3A1@att.net> <73msp0$i8e@dfw-ixnews7.ix.netcom.com>`

```
In article <73msp0$i8e@dfw-ixnews7.ix.netcom.com>, wmklein@ix.netcom.com 
says...
> 
> William Lynch wrote in message <365E1CB2.3CE2B3A1@att.net>...
…[19 more quoted lines elided]…
> 
I have not used it for some time but I do remember that it did store a 
version number/name. Just looking at a listing and it did/does store 
version numbers in 73 thru 80. 
> 
> 
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365F5938.EC44046E@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365C772B.1BB80DA3@home.com> <365cd3ca.8846662@news1.ibm.net> <365E1CB2.3CE2B3A1@att.net> <73msp0$i8e@dfw-ixnews7.ix.netcom.com>`

```
"William M. Klein" wrote:
> 
(snip)
> 
> (For the IBM mainframers)  Doesn't (or didn't) Panvalet or Librarian use
> columns 73-80 for storing version numbers - some how?

It's optional with Librarian. Our masters are set up to sequence number
externally, i.e., columns 81-86.

Bill Lynch
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CC635.3512438E@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com>`

```
"William M. Klein" wrote:
> 
(snip)
> 
> 3) There is a new inline comment indicator "*>" which allows you to make the
> end (but not the middle) of any line a comment.  This can also be used in
> free format source code to make an entire line a comment.

Pity, something like the "/* comment */" would be a better choice. I
really think it would prove more powerful over time.

> 4) There is a  new >>PAGE compiler directive that takes the place of "/" in
> column 7 for free format source code (and can also be used in fixed format
> source code)

Is "EJECT" being dropped (or was it an IBM extension)? I never used the
"/" in column 7, looks too messy to me.

Bill Lynch
> 
> (Note: There is also a new feature of "concatenated" literals that IN MOST
> CASES works the same way. For example
>     Move  "This is a concatenated" & "literal" to message-area

I'm guessing this is a STRING which pads the receiving field if the
sending field is shorter.
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73ijk7$bvs@sjx-ixn6.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net>`

```

<snip>
>> 4) There is a  new >>PAGE compiler directive that takes the place of "/"
in
>> column 7 for free format source code (and can also be used in fixed
format
>> source code)
>
…[3 more quoted lines elided]…
>Bill Lynch


EJECT (and SKIP1/2/3) were IBM extensions.  (Or at least are such now - I
don't know if they were part of '68)
```

###### ↳ ↳ ↳ Re: New "REFERNCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4CB67D3E91F42B56.73D84F8973955BDC.D5333F754C0BEEA5@library-proxy.airnews.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net>`

```
William Lynch wrote:
> 
> "William M. Klein" wrote:
…[9 more quoted lines elided]…
> 
(snip)

I rather like the "*>" instead.  The "/* ... */" pair is too easily
confused (dyslexia).  Although I am not dyslexic myself, I still have to
perform a mental pause "asterisk left or right---comment on or off?"  If
they ever decide to include "middle of the line" comments, I think the
end-comment indicator should be something other than a reversal of the
start-comment symbol.  Even "*<" would be good enough.
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73v88v$5ua@dfw-ixnews9.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net>`

```

William Lynch wrote in message <365CC635.3512438E@att.net>...
>"William M. Klein" wrote:
>>
>(snip)
>>
>> 3) There is a new inline comment indicator "*>" which allows you to make
the
>> end (but not the middle) of any line a comment.  This can also be used in
>> free format source code to make an entire line a comment.
…[3 more quoted lines elided]…
>


I went back to the J4 people and asked why they did not go with a "start AND
end" comment delimiter.  (I remembered it had been discussed - but not why
it got rejected.)

The answer was that - in those languages that support both a beginning and
end delimiter, i.e. allow "totally inline" comments - forgetting the closing
delimiter is one of the MOST COMMON coding errors.  Therefore, the committee
felt that adding this facility had insufficient merit for the problems (for
programmers) that it would cause.

Having never worked with such languages, I can't confirm or deny the current
perception - but I do understand that many of those who voted against this
feature HAVE worked with languages that support it.
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36638786.CAB3C18A@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net> <73v88v$5ua@dfw-ixnews9.ix.netcom.com>`

```
"William M. Klein" wrote:
> 
(snip)
> I went back to the J4 people and asked why they did not go with a "start AND
> end" comment delimiter.  (I remembered it had been discussed - but not why
…[10 more quoted lines elided]…
> feature HAVE worked with languages that support it.


Well, thanks for asking.

BTW, I've heard a common error by programmers in languages that use the
period to end a sentence is misplaced periods - maybe we should write
them out of the standard? :-)))

Bill Lynch
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 8)_

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<740j4n$5jq$1@nnrp1.dejanews.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net> <73v88v$5ua@dfw-ixnews9.ix.netcom.com> <36638786.CAB3C18A@att.net>`

```
In article <36638786.CAB3C18A@att.net>,
  wblynch@worldnet.att.net wrote:

> (snip)
>
…[5 more quoted lines elided]…
>

Hey, seriously, why not replace the dots by statements like 'END-PARAGRAPH'
and 'END-SECTION'. This would be much clearer to interpret and would cause
less errors when doing maintenance!

Cheers

Daniel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 9)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OOj230aH#GA.117@upnetnews03>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net> <73v88v$5ua@dfw-ixnews9.ix.netcom.com> <36638786.CAB3C18A@att.net> <740j4n$5jq$1@nnrp1.dejanews.com>`

```

daniel.jacot@winterthur.ch wrote in message
<740j4n$5jq$1@nnrp1.dejanews.com>...
>In article <36638786.CAB3C18A@att.net>,
>  wblynch@worldnet.att.net wrote:
…[13 more quoted lines elided]…
>

The parsing process in any competent COBOL compiler could easily identify
the end of a paragraph or end of a section without explicit periods (full
stops) or END-xxxx features, at least in the standard format using A and B
margins.

A paragraph end is indicated by presence of the next division or section or
paragraph name, or the physical end of the source code.

A section end is indicated by presence of the next division or section name,
or the physical end of the source code.
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 10)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36664ddc.81805569@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net> <73v88v$5ua@dfw-ixnews9.ix.netcom.com> <36638786.CAB3C18A@att.net> <740j4n$5jq$1@nnrp1.dejanews.com> <OOj230aH#GA.117@upnetnews03>`

```
'Twas Tue, 1 Dec 1998 20:55:05 -0500, when "Dennis J. Minette"
<dennis_minette@email.msn.com> illuminated comp.lang.cobol thusly:

>The parsing process in any competent COBOL compiler could easily identify
>the end of a paragraph or end of a section without explicit periods (full
>stops) or END-xxxx features, at least in the standard format using A and B
>margins.

Forget A and B margins.  Too many compilers have already done away with
them; too many J4 decisions have been made which assume margins are gone.
You will not revive margin restrictions; they are dead, dead, dead.
```

###### ↳ ↳ ↳ Re: New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3663D10A.39CB426D@zip.com.au>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com> <73hqdl$2rm@dfw-ixnews3.ix.netcom.com> <365CC635.3512438E@att.net> <73v88v$5ua@dfw-ixnews9.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I went back to the J4 people and asked why they did not go with a "start AND
…[11 more quoted lines elided]…
> feature HAVE worked with languages that support it.

With colour hilighting this is not a problem really.  Even MVS now
hilights in colour.

Try forgetting that quote on a sring literal, this is the same problem
should we eliminate them???

Ken
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hqg6$2tk@dfw-ixnews3.ix.netcom.com>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <73g565$8ad@sjx-ixn9.ix.netcom.com>`

```
Please see my new thread titled

   New "REFERENCE FORMAT" (was: Is one period per paragraph a good idea?

for answers to many of the issues raised in this thread (as they will be in
the next Standard).
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8BkKbVG#GA.153@upnetnews05>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com>`

```

RKRayhawk wrote in message <19981124231101.07622.00000238@ng-cr1.aol.com>...
>
>For those who would like a floating pargraph name in the COBOL language,
try
>this idea.
>
…[8 more quoted lines elided]…
>I am not sure, but seems like the originators knew that sentence-ending
periods
>would be followed by white space (blank, tab, new line, or EOF).  It is
also
>true that decimal points (or European thousand separators) would be
preceeded
>by numbers.  Thus a dot-command was distinct from any other expected
lexical
>pattern.
>
>A future version of COBOL could exploit this same opportunity.  A DOTTED
NAME
>could be a paragraph (procedure) name.
>
…[17 more quoted lines elided]…
>For the aged mainframes we could add a special rule that a period in column
72
>will never be considered part of a DOTTED NAME. (That will require
environment
>specific logic).
>
…[3 more quoted lines elided]…
>RKRayhawk@aol.com

This dot-paragraph-name suggestion is brilliant!  It would definitely allow
the A and B margin rules to expire.  But I would not want to be responsible
for maintenance in any free-form, stream of consciousness code that might
evolve from 'floating' paragraph/procedure names.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365CC0CB.2AEF3ACF@att.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com>`

```
RKRayhawk wrote:
> 
(snip)
> 
> A future version of COBOL could exploit this same opportunity.  A DOTTED NAME
…[4 more quoted lines elided]…
>                   MOVE DOTS TO SCREEN.

As Professor Higgins said: "By Jove, I think you've got it".

Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73iqgr$l9s$1@news.igs.net>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <365CC0CB.2AEF3ACF@att.net>`

```

William Lynch wrote in message <365CC0CB.2AEF3ACF@att.net>...
>> A future version of COBOL could exploit this same opportunity.  A DOTTED
NAME
>> could be a paragraph (procedure) name.
>>
>> In old format in A-margin
_________
>> 001000 .DOT-YOUR-AYES.     <--this is paragraph 1000000.DOT-YOUR-AYES.
                                                           (real old format)
>>                   MOVE DOTS TO SCREEN.
>
>As Professor Higgins said: "By Jove, I think you've got it".
>
>Bill Lynch
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 4)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365f44d3.19931238@netnews>`
- **References:** `<365d4953.1299010@nntp.ix.netcom.com> <19981124231101.07622.00000238@ng-cr1.aol.com> <365CC0CB.2AEF3ACF@att.net>`

```
'Twas 26 Nov 1998 02:44:38 GMT, when William Lynch <wblynch@att.net>
illuminated comp.lang.cobol thusly:

>RKRayhawk wrote:

>> A future version of COBOL could exploit this same opportunity.  A DOTTED NAME
>> could be a paragraph (procedure) name.
…[5 more quoted lines elided]…
>As Professor Higgins said: "By Jove, I think you've got it".

My copy is 400 miles away, but I believe that the current draft says that
a period must be followed by a space to be recognized as a period token,
therefore you will need an extra space between the period and the
paragraph name.  However, the following is illegal in Cobol-85:

    PROCEUDRE DIVISION
    . A SECTION.
    . B.

This is illegal, because the period before B is a sentence between the
section header and the paragraph header, which is prohibited in Cobol-85,
but allowed in the draft.
```

###### ↳ ↳ ↳ Re: Is one period per paragraph a good idea?

_(reply depth: 5)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981127210554.23446.00001694@ng153.aol.com>`
- **References:** `<365f44d3.19931238@netnews>`

```
Barticus@att.spam.net (Randall Bart)
Date: 28 Nov 1998 00:43:05 GMT
wrote, in part ...

<< 
...

the following is illegal in Cobol-85:

    PROCEUDRE DIVISION
    . A SECTION.
    . B.

This is illegal, because the period before B is a sentence between the
section header and the paragraph header, which is prohibited in Cobol-85,
but allowed in the draft.
>>

You are right, but, ...

The proposed DOTTED NAME would change the rules for the parser in such a way as
to _NOT_ jeopardize any existing code.

Today all sentence-ending periods must be followed by white-space. (it is
optional to preceed them by white-space).

A DOTTED-NAME would be a period (mandatorily preceded by white space), which
must be followed by an alphabetic (that is, followed by non-white space).

The parsers chances of picking out the DOTTED NAMEd procedure name would be
enhanced further if we manadated that such a procedure name would still have to
be followed by a period.  

So that the format is really white-space/period/name/period/white-space.

Perform verbs would still just reference the name, without leading or trailing
period.

As far as this proposal is concerned, periods as sentence ending indicators
could still appear anywhere.
 
Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Is one period per paragraph a good idea?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b6931.2335088@news1.ibm.net>`
- **References:** `<oHB62.2702$Sf1.2628221@news3.mia>`

```
On Tue, 24 Nov 1998 17:05:24 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>I have been thinking about the concept of 'one period per paragraph'.
>Thane Hubbell first introduced me to the idea and I didn't like it,
…[10 more quoted lines elided]…
>comments?

I think the period is needed to define paragraph names, but I would be
content to have it "assumed" when a new paragraph/section/division/
end of source is encountered.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
