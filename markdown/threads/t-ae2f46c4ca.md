[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What language?

_49 messages · 19 participants · 2002-04 → 2003-02_

---

### What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-23T01:29:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
This question might upset some of you; if so, I'm sorry but it has to
be asked.

 I have old 16 bit versions of the Realia compiler and ScreenIO but I
can't afford to upgrade so essentially I'm going to have to change
languages. The question is: to what? And how to make the process as
easy as possible.

Quite clearly, other language people speak...well, another language.
One would have thought that like real world languages (French, German,
etc) there would be certain fundamentals such as a dictionary and a
grammar which in COBOL are known collectively as the "Language Manual"
(normally issued by IBM) and the little tricks and techniques and
efficiencies are in another manual called the "Application Programming
Guide". Know these manuals by heart and you know everything there is
to know about the language.  Naturally I presumed that (for example)
VB6 would have a "Language Manual" but whenever I question a VB6
programmer about its existence they get a funny little smile on their
face and profess ignorance. How a language can operate without such an
essential, I have difficulty grasping.

Looking at the "Teach Yourself [insert language]" books in B&N brings
up a new problem. As every COBOL programmer knows: read a file, do
some processing, write a record. That's it. COBOL in a nutshell. And,
oh, that "processing" is generally shifting around data; mathematics
beyond adding up values are best left to the Fortran programmers. So
what I expect is that the "Learn [some language]" will start with data
definition, file organization, and data output and maybe some brief
overview of computational aspects. A beginning program example might
be to input an 80 char record (say a card), add up the number input,
and write each one out to the printer and also to a sequential tape
file.

That's not what I've found. These other languages don't seem to have
heard of data types, redefinitions, files...all those important things
in the real world. Instead we get a chapter on playing sound or
putting up pretty pictures and and program examples seem to be limited
to "Hello World". Either a) I have the wrong language or b) I have the
wrong book. (Of course it's highly suspicious that there are SO MANY
books of "Learn [this language]" making one think that maybe the rest
of the world is wrong.)

However, let's ask the question to the people who might know: this NG.
If someone tears that COBOL compiler out of your hot little hands and
forbids you to use it what is the next language you would use? And
what book/website gives the best introduction? (For example there used
to be an IBM publication "C for COBOL programmers" about 15 years ago
but I don't think it has been re-issued.)

Bear in mind that I need an industrial strength file system (I hate
using the term but call it a database), a non-crippled language (this
is why Fujitsu is no good), and it has to run on NT4. I have access to
a free Visual Studio and free SQL server. I only have one application
and it only runs on one machine (mine).

COBOL is lousy for two things: screen input and print output. Thus
ScreenIO and for the minimal amount I print, I output an ASCII file
and have canned macros in WPerfect to format and print. It seems that
VB6 might be good for the screen input although I'm a little worried
that it doesn't seem quite as comprehensive as I would like. For
example a list box file look up function where the language manages
all the I/O and display would seem to be a good addition but I don't
see that in my minimal exposure to VB6. I can continue using the
output to WPerfect or (if the function exists) output it to IE.

Or looking at the postings on this group over the last couple of days
I see a reference to Ada. Free compiler! There's one of the
requirements straight away! But as soon as I start looking at the
website I start to see the gobblydegook: inheritance, encapsulation,
reentrant, etc, and don't see: "Ada supports the following file types:
blah, blah.", "Here's how you define an 36 byte alphanumeric field:
blah blah" etc. Depressing.

So guys help me see clearly, please.

TIA
```

#### ↳ Re: What language?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-04-23T13:51:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cc55cac_5@Usenet.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
Comments below...
<Nospam@neverspam.com> wrote in message
news:fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com...
> This question might upset some of you; if so, I'm sorry but it has to
> be asked.
>
Not me. It is only computer programming...

>  I have old 16 bit versions of the Realia compiler and ScreenIO but I
> can't afford to upgrade so essentially I'm going to have to change
> languages. The question is: to what? And how to make the process as
> easy as possible.
>

Remarkable. Change Languages?! Why? There are free 32 bit compilers
available. Check the COBOL FAQ.

> Quite clearly, other language people speak...well, another language.
> One would have thought that like real world languages (French, German,
…[10 more quoted lines elided]…
>
 Language Manual, User Guide. So you can't imagine any other way of doing
it? VB programmers learn by writing sample code. They are introduced to
concepts like FUNCTIONS, then left to search out the functions they require.
Their IDE (Integrated Development Environment) presents suitable functions
to them and also checks their syntax as they write; the concept of a
Language Manual is like telling a guy with a chain saw that flint axes are
pretty good for cutting down trees... The point is that unless you are
prepared to be more flexible in what you expect, you are doomed to
disappointment in your quest for a COBOL replacement. It really is no good
saying "This is what I know and love so I expect everything else to be like
it...". (If that is really the case, then don't switch...)

> Looking at the "Teach Yourself [insert language]" books in B&N brings
> up a new problem. As every COBOL programmer knows: read a file, do
…[9 more quoted lines elided]…
>
Yes, that it is an exact description of what COBOL has been doing for the
last 43 years. And it is a viable approach to teaching COBOL. It has been so
efficacious that it is now enshrined in Fortress COBOL, where mainframe
Priests still worship at the altar of Batch Processing and kid themselves
that CICS will stem the advance of the Barbarian hordes.

However, some Sects have broken away and pushed COBOL into the 21st Century.
These Heretics talk about encapsulation, inheritance, objects, classes,
properties, methods....all that nasty stuff that you reject below.

> That's not what I've found. These other languages don't seem to have
> heard of data types, redefinitions, files...all those important things
> in the real world.

Er, which "Real World" was that? Oh yes, the COBOL Real World... (I live in
a number of different realities when it comes to Computer Programming...<G>)

> Instead we get a chapter on playing sound or
> putting up pretty pictures

Pretty useful if you need to play sound or deal with Graphics.

Believe it or not, SOME people think computers are for having fun as well as
doing serious business. These people (usually young) are having the temerity
to invade the domain of the "programmer" and learn how to make THEIR
computer do what THEY want. (I know...it's sacrilege. Imagine if Users could
get a computer system to do what they wanted...doesn't bear thinking about,
does it <G>?)

>  and and program examples seem to be limited
> to "Hello World".

Have to agree with you here. I have never seen the relevance of this. I
reckon it should say: "This message has been produced from a very basic
computer program."

> Either a) I have the wrong language or b) I have the
> wrong book. (Of course it's highly suspicious that there are SO MANY
> books of "Learn [this language]" making one think that maybe the rest
> of the world is wrong.)
>

...or c) the wrong attitude?

> However, let's ask the question to the people who might know: this NG.
> If someone tears that COBOL compiler out of your hot little hands and
> forbids you to use it what is the next language you would use?

Straight serious answer (no joking or irony): Java.

But it won't work for you. You will find it bewildering and not a bit like
what you are expecting. (See, like most modern computer programming
languages, it is "Object Oriented". That means all that mystical heretical
stuff mentioned above, and discarded by you below... To have a chance of
succeeding with Java you need to be able to clear your mind of pre-conceived
ideas. I suggest that, based on what you have posted here, that will be an
almost impossible exercise for you personally.)

Why not simply spend a few bucks and upgrade what you know?


> And
> what book/website gives the best introduction? (For example there used
> to be an IBM publication "C for COBOL programmers" about 15 years ago
> but I don't think it has been re-issued.)
>

Avoid anything that says "X for COBOL Programmers". ALL modern Languages are
OO and cannot be directly related to COBOL. (This includes OO COBOL! Until
you have grasped the underlying concepts of OO (which are, in fact, quite
simple), you will make no progress with OO COBOL (I can say this based on
first hand experience - I sweated OO COBOL for at least 6 weeks... gave up.
Learned Java from scratch, (in 2 weeks), picked up OO COBOL again and
suddenly all was revealed (thanks also to Will Price's excellent book on the
subject).).

Buy "Java Made Simple" and/or "Java in 24 hours". The latter is beautifully
written with a wicked sense of humour and makes learning entertaining as
well as educational.

> Bear in mind that I need an industrial strength file system (I hate
> using the term but call it a database),

No you don't. Nobody does. Bin it and learn SQL. Get with the program! <G>


> a non-crippled language (this
> is why Fujitsu is no good),

Funny, my Fujitsu version 6.1 compiler doesn't seem to hobble along...
inspection reveals absolutely NO evidence of crippling whatsoever... I have
been using Fujitsu products since release 3 (MicroFocus before that...) I
don't recall ANY of them being crippled. Ah, but then I DID pay for them
(except release 3). Why not check out Tiny COBOL? It is free and it deserves
support.

> and it has to run on NT4. I have access to
> a free Visual Studio and free SQL server. I only have one application
> and it only runs on one machine (mine).

SQL Server free? ...and you are worried about a file system?! Go for it!
(Irrespective of whether you stay with COBOL or not...You can embed SQL
calls in almost any Language.)

>
> COBOL is lousy for two things: screen input and print output.

Er, compared to what? A sharp stick and a rubber stamp?...

As Michael Matthias (another frequent contributor to this forum) has sagely
reminded us on a number of occasions: "It is the Artist, NOT the
paintbrush."  Personally, I have absolutely NO problem with using COBOL for
Screen input (either using GUI (PowerCOBOL) or Screen Section) and I have no
problem using COBOL to prepare print output as a formatted report on a
mainframe or as a Word Processed document on Client/Server (I DO use OLE
(via OO COBOL) to invoke MS WORD or WordPerfect)

>Thus
> ScreenIO and for the minimal amount I print, I output an ASCII file
> and have canned macros in WPerfect to format and print.

That is a good solution if you can't use OO COBOL to invoke the WP functions
directly as an OLE server.


> It seems that
> VB6 might be good for the screen input although I'm a little worried
…[5 more quoted lines elided]…
>
The secret is to build a component (in either VB or C++ or OO COBOL) or a
Java Bean that does exactly what you describe, then simply embed the
component in your desktop application or your Web Pages...but it DOES mean
learning OO and you have indicated that you don't intend to do that.

You could also switch to using Web Forms for your screen input, in which
case you will need to learn HTML and, ideally, JavaScript. Then you will
need a Java Applet/Servlet to get the input, or CGI COBOL to get and process
it. All of this is far removed from your comfortable world of files,
redefinitions, and pictures.(You can learn HTML in an afternoon (it is
another slant on Word Processing) and CGI COBOL is good fun. So, even
without having to learn Java you could get by quite adequately).

> Or looking at the postings on this group over the last couple of days
> I see a reference to Ada. Free compiler! There's one of the
…[5 more quoted lines elided]…
>

Well, it's only depressing if you are not prepared to learn. And
gobbledygook is only gobbledygook until you understand it (in this case, at
least).

It's really a bit pointless to castigate the world because it bypassed
Fortress COBOL and moved on. COBOL had every opportunity to come in from the
cold. Many people spent countless hours formulating OO additions to the
Language, vendors even implemented stuff ahead of the standard to give COBOL
a fighting chance of remaining pertinent, and it was rejected by the
entrenched COBOL establishment because it didn't look like what they were
used to, and they couldn't be bothered to get to grips with it. The general
reaction was exactly the one you have expressed here.

> So guys help me see clearly, please.
>

To see clearly you will need to set aside what you know (at least
temporarily) and approach things with a completely fresh perspective. Many
people are simply unable to do this. Their careers as computer programmers
are not likely to go anywhere...

1. Learn Java. (This has the side effect of teaching you OO concepts.)

2. Look at OO COBOL. It is VERY useful, especially for writing business
components.

3. Be prepared to spend SOME money on SOMETHING. (If you are serious about
it, why wouldn't you?)

Good luck.

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T01:46:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

><Nospam@neverspam.com> wrote in message
>news:fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com...

>Remarkable. Change Languages?! Why? There are free 32 bit compilers
>available. Check the COBOL FAQ.

Not true except for the crippled and the obsolete standard and anyway
this doesn't solve the ScreenIO problem unless you think I'm going to
suddenly start writing Screen section statements.

> Language Manual, User Guide. So you can't imagine any other way of doing
>it?

I can't imagine a language, natural or computer, without
specifications, no.

> VB programmers learn by writing sample code. They are introduced to
>concepts like FUNCTIONS, then left to search out the functions they require.
>Their IDE (Integrated Development Environment) presents suitable functions
>to them and also checks their syntax as they write;

That might be how they learn however somewhere someone has a complete
list of all those functions together with the syntax.

> the concept of a
>Language Manual is like telling a guy with a chain saw that flint axes are
>pretty good for cutting down trees...

No. The absence thereof would be like telling the logger to cut down
certain species of tree and not telling him how to identify those
trees.

> The point is that unless you are
>prepared to be more flexible in what you expect, you are doomed to
>disappointment in your quest for a COBOL replacement.

I realize nothing will be quite as good as COBOL but unfortunately I
have to change.

>Er, which "Real World" was that? Oh yes, the COBOL Real World... (I live in
>a number of different realities when it comes to Computer Programming...<G>)

>> Instead we get a chapter on playing sound or
>> putting up pretty pictures

>Pretty useful if you need to play sound or deal with Graphics.

>Believe it or not, SOME people think computers are for having fun as well as
>doing serious business. These people (usually young) are having the temerity
…[3 more quoted lines elided]…
>does it <G>?)

Frivolity certainly has its place however we're talking about serious
computing here. Please keep to the point.

>> However, let's ask the question to the people who might know: this NG.
>> If someone tears that COBOL compiler out of your hot little hands and
>> forbids you to use it what is the next language you would use?

>Straight serious answer (no joking or irony): Java.

I do not have a free copy of Java (although I might be willing to
spring for a few hundred dollars if it does everything just as well as
COBOL <g>). Also I'm emotionally opposed to any language that would
name itself after a slang term for coffee, just as you won't find me
anywhere near an apple (unless you're talking about the fruit).
Further, isn't Java that thing that makes surfing the web annoying
with pop-up windows and rotating elephants etc.?

>But it won't work for you. You will find it bewildering and not a bit like
>what you are expecting. (See, like most modern computer programming
…[4 more quoted lines elided]…
>almost impossible exercise for you personally.)

That's why you're going to tell me how to use the language in the same
manner as I would use COBOL.

>Why not simply spend a few bucks and upgrade what you know?

Are you aware of the prices of the compilers and ScreenIO?

>Avoid anything that says "X for COBOL Programmers". ALL modern Languages are
>OO and cannot be directly related to COBOL. (This includes OO COBOL! Until
…[5 more quoted lines elided]…
>subject).).

I'm sorry I don't intend to take up an occupation based on this; I
just want to rewrite my sole application. As to OO COBOL, <heh, heh>
if you only knew...

I suppose this is as good a place as any:

Understand that as far as my use of whatever language I choose and its
environment I'm the DP manager, Project leader, Analyst, Programmer,
Sole User, QA person, Customer Engineer (or whatever they call
hardware guys these days), Accounting department, Chairman of the
board, COO, CEO, CFO, ... everything. Specifications? In my head,
baby. Documentation? If it's not written down in the program and I
can't remember, it doesn't exist. User acceptance? Does it work on
live data? Parallel processing? Don't be silly.

Integrated Development Environment? If you mean by that control of
source code, versions, etc., you must be crazy. I have one directory
with the current source, one with the current executables, and a third
with the live data. Duplicating those I have three parallel test
directories. If I make a change I copy the current copy to my test
source, make the change, execute the compiler and linkage editor and
then copy the live data to the test data directory and run it. If it
works, copy the test data to the live data and the new source and
excecutables to the live directories. Cutting out all the BS I can do
in a couple of hours what used to take a couple of weeks in the
corporate world.

Programs are all executables (EXE) and one big monster starting at the
beginning and finishing at the end. No calls unless obliged such as by
ScreenIO. Why should I? Why incur the agro? I have at least 128 meg of
memory to play with (and more memory is cheap) and then there's the
swap file. Frankly I can't imagine ever getting even close to 128
meg... or even 64...ten, maybe. NT loads it all into memory at the
beginning and then awaits my bidding. Computers still process one
instruction at a time in a sequential manner, don't they?

How about some re-usable code? That's what the copy function is for.
Either copy the entire program and change it or copy a performed
routine within the same program. Where's the problem?

As I understand Fujitsu's Power COBOL which looks like it parallels
VB, each screen becomes a little program and we go merrily along from
one screen to another executing the associated code. I can live with
that. I'll just see it as a set of go to's (naughty me; that's
probably a dirty word).  

>Funny, my Fujitsu version 6.1 compiler doesn't seem to hobble along...
>inspection reveals absolutely NO evidence of crippling whatsoever... I have
>been using Fujitsu products since release 3 (MicroFocus before that...) I
>don't recall ANY of them being crippled. Ah, but then I DID pay for them
>(except release 3).

There's your problem, right there!

> Why not check out Tiny COBOL? It is free and it deserves
>support.

74 standard and no ScreenIO.

>> It seems that
>> VB6 might be good for the screen input although I'm a little worried
…[4 more quoted lines elided]…
>> output to WPerfect or (if the function exists) output it to IE.

>The secret is to build a component (in either VB or C++ or OO COBOL) or a
>Java Bean that does exactly what you describe, then simply embed the
>component in your desktop application or your Web Pages...but it DOES mean
>learning OO and you have indicated that you don't intend to do that.

And it means "build[ing] the component"; I rather hoped someone (like
the language maker) had already done this for me. It has nothing to do
with OO.

>It's really a bit pointless to castigate the world because it bypassed
>Fortress COBOL and moved on. COBOL had every opportunity to come in from the
…[5 more quoted lines elided]…
>reaction was exactly the one you have expressed here.

It's not a question of what the establishment is used to but rather
that the OO people have not (as you haven't here) shown a need for
their functions. In other words, instead of accusing the
"establishment": of being old fogeys and so putting their backs up,
the proponents of these new-fangled ideas need to show how much better
their method is. "Better" means that it makes my life easier, not that
it satisfies some esoteric programming standard that someone has
convinced the management will suddenly reduce the development time to
zero and allow them to employ minimum wage guys from McD's.

Anecdote: I went to a C programming course back a few years ago and
the lecturer, a gung-ho young guy, wasted a couple of days showing us
how to write a program in C to (IIRC) convert a comma-delimited file
into one with fixed length records, a function I could do with
REALCOPY in a minute and that includes looking up the manual.
Obviously this guy had no idea of how to justify C.

Second anecdote: I also went to a class on database normalization and
listened to the bombastic consultant tell us that we'd done everything
wrong for our entire lives and how he had this better method (which he
had already sold to the powers-that-were) which would basically
recover us to the level of the guy in the mailroom. After he reached
the fifth level of normalization (I think that's the one where no
letter of the alphabet is duplicated in the entire DB; everything is
just pointers <g>) we realized that all this was just common sense
(no, not the fifth level); we'd been doing it all along (without the
reams of forms and procedure manuals by the pound, of course).   

>3. Be prepared to spend SOME money on SOMETHING. (If you are serious about
>it, why wouldn't you?)

Because I'm cheap?
```

###### ↳ ↳ ↳ Re: What language?

- **From:** docdwarf@panix.com
- **Date:** 2002-04-24T06:18:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa60pn$81$1@panix1.panix.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com>`

```
In article <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com>,
 <Nospam@neverspam.com> wrote:
>"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:
>
>><Nospam@neverspam.com> wrote in message
>>news:fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com...

[snippage]

>> VB programmers learn by writing sample code. They are introduced to
>>concepts like FUNCTIONS, then left to search out the functions they require.
…[4 more quoted lines elided]…
>list of all those functions together with the syntax.

'A list of all those functions together with the syntax' sounds like a 
Manual or User's Guide... such things abound, last I looked.

>
>> the concept of a
…[5 more quoted lines elided]…
>trees.

It is the logger's job to know such things.

[snip]

>>Believe it or not, SOME people think computers are for having fun as well as
>>doing serious business. These people (usually young) are having the temerity
…[6 more quoted lines elided]…
>computing here. Please keep to the point.

Plural majestatus est... who determines 'serious'?

>
>>> However, let's ask the question to the people who might know: this NG.
…[7 more quoted lines elided]…
>COBOL <g>).

Nothing does anything 'just as well' as anything else; do some Serious 
Business and evaluate ROI.

>Also I'm emotionally opposed to any language that would
>name itself after a slang term for coffee, just as you won't find me
>anywhere near an apple (unless you're talking about the fruit).

Put your emotions aside, 'we' are talking serious business here.

>Further, isn't Java that thing that makes surfing the web annoying
>with pop-up windows and rotating elephants etc.?

Just as COBOL is that thing which makes reports that are printed out 
daily, measured by the yard and immediately discarded.

[snip]

>>Why not simply spend a few bucks and upgrade what you know?
>
>Are you aware of the prices of the compilers and ScreenIO?

Answering a question with a question is no answer at all... you get what 
you pay for.

[snip]

>Understand that as far as my use of whatever language I choose and its
>environment I'm the DP manager, Project leader, Analyst, Programmer,
…[5 more quoted lines elided]…
>live data? Parallel processing? Don't be silly.

Hey, looks like you are Chief Cook and Bottlewasher... do whatever you see 
fit, you have control of it all and it is going to be right every step of 
the way; after all... you don't need parallel processing.

[snip]

>>Funny, my Fujitsu version 6.1 compiler doesn't seem to hobble along...
>>inspection reveals absolutely NO evidence of crippling whatsoever... I have
…[4 more quoted lines elided]…
>There's your problem, right there!

Paying for software is a problem... and you expect to make a living 
writing code?
>
>> Why not check out Tiny COBOL? It is free and it deserves
>>support.
>
>74 standard and no ScreenIO.

Ummmmm... didn't you say that anyone who expected you to learn to use 
ScreenIO is insane?

This is beginning to resemble dealing with Mr Dilworth.  As Darwin came 
close to saying, 'Mutate or die'.

DD
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-24T17:37:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC6ECFF.6C513404@shaw.ca>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:

>
> This is beginning to resemble dealing with Mr Dilworth.  As Darwin came
> close to saying, 'Mutate or die'.
>
> DD

Having asked an initially somewhat oblique question, "can't afford...", some
responded with what they thought were helpful suggestions. Having seen his
succession of replies, over and above your 'Dilworth' reference, my reaction was
we are dealing with a myopic Tightwad !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-24T14:10:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa6sdp$lhi$1@panix1.panix.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com> <3CC6ECFF.6C513404@shaw.ca>`

```
In article <3CC6ECFF.6C513404@shaw.ca>, James J. Gavan <jjgavan@shaw.ca> wrote:
>
>
…[11 more quoted lines elided]…
>we are dealing with a myopic Tightwad !

Perhaps so, Mr Gavan... I read another posting in this thread which stated 
that the software is used for maintaining files which are sent off to 
someone for publication; not being able to see a Legitimate Business 
Expense/Deduction for a reflexively-spewed haze of Costs Too Much!!! does 
appear to be a bit of shortsightedness.

DD
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T23:00:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com>,
> <Nospam@neverspam.com> wrote:
…[3 more quoted lines elided]…
>>>news:fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com...

>>That might be how they learn however somewhere someone has a complete
>>list of all those functions together with the syntax.

>'A list of all those functions together with the syntax' sounds like a 
>Manual or User's Guide... such things abound, last I looked.

And from: "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>

>Want to bet? This is Microsoft we are talking about here. They LIVE off
>obfuscation. Even the MSDN
>disks do not provide what you suggest.Not a complete list, and not all in
>one place.

These are two contradictory statements. Looks like you guys need to
talk to each other.

>>>Believe it or not, SOME people think computers are for having fun as well as
>>>doing serious business. These people (usually young) are having the temerity
…[3 more quoted lines elided]…
>>>does it <G>?)

>>Frivolity certainly has its place however we're talking about serious
>>computing here. Please keep to the point.

>Plural majestatus est... who determines 'serious'?

"We" = the other poster and myself or the rest of the group and
myself. No royal "we" intended.

I'm not going to enter into a debate as to what is serious and what is
not because at least at this point it's not germane.

>>>> However, let's ask the question to the people who might know: this NG.
>>>> If someone tears that COBOL compiler out of your hot little hands and
>>>> forbids you to use it what is the next language you would use?

>>>Straight serious answer (no joking or irony): Java.

>>I do not have a free copy of Java (although I might be willing to
>>spring for a few hundred dollars if it does everything just as well as
>>COBOL <g>).

>Nothing does anything 'just as well' as anything else; do some Serious 
>Business and evaluate ROI.

ROI = Return on Investment I suppose. Pretty low. I'm not in this for
the money.

The first part of your statement is incorrect. A Honda Civic gets you
to where you're going just as well as a Mercedes. An enormous number
of examples exist outside the computer world (and probably in it).

>>Also I'm emotionally opposed to any language that would
>>name itself after a slang term for coffee, just as you won't find me
>>anywhere near an apple (unless you're talking about the fruit).

>Put your emotions aside, 'we' are talking serious business here.

Ah no. Just as one gets an instinctive feeling about cars,
restaurants, movies, people, etc., so also one gets an instinctive
feeling about computer languages. If the makers adopt a flippant
attitude to the language name, the likelihood is that they adopt a
similar attitude in constructing the language, fixing bugs,
implementing the boring stuff, etc.

>>Further, isn't Java that thing that makes surfing the web annoying
>>with pop-up windows and rotating elephants etc.?

>Just as COBOL is that thing which makes reports that are printed out 
>daily, measured by the yard and immediately discarded.

I doubt it today but anyway I don't see those reams of paper, other
languages can and do produce similar quantities, and the quantity of
paper is a function of the type of application. In the days before the
proliferation of PC's and monitors, those huge reports were the only
way to communicate to the user. The more modern the system the less
paper will be generated.

OTOH, I do see those pop-ups and rotating elephants and they annoy me
daily...today... not in some legacy application designed forty years
ago. It goes again to those instinctive feelings about the quality of
the language.

Thirdly, I'm told (here, on this NG) that I couldn't possibly learn
Java due to the fact that I don't have the faith--or some
quasi-religious state of mind. That seems to kill Java for me. 

>>>Why not simply spend a few bucks and upgrade what you know?

>>Are you aware of the prices of the compilers and ScreenIO?

>Answering a question with a question is no answer at all... you get what 
>you pay for.

It's a rhetorical question.

As to your second point, are you familiar with a product called Xtree
(Gold/Pro)? I bought that back in the mid-eighties and used it until I
migrated to NT about two years ago. Cost around $20. Great product.
Well worth the money.

If you look in the headers to this post, you'll see that I'm using
Forte Agent. It's not a pirate. I shelled out around $30 for it.
Another great product put out by a competent SERIOUS company.

For my jpg viewing on the net I use XNview. Free product. Wonderful
package. Much better than LV~something or other~ which kept hounding
me to pay a fee for itself. I'm glad I changed.

OTOH, I bought an address book called Ist Act for around $30. What a
piece of junk.

I also purchased a mailing list generator/processor (prepares sorted
mail for the USPS so you can make bulk mailings). I seem to remember a
cost of around $200 but I can't remember the name of the product. The
psych people would probably tell me that I've suppressed it because I
had such a bad experience with the program. Can you imagine standing
on the loading dock of the mail sorting center and being told that
they couldn't take your shipment of 10,000 pieces due to the sort not
being correct, the fault of this piece-of-sh-- package? Do you have
any idea how tedious it is to sort 10,000 pieces manually?

From the above I think you'll see that you don't get what you pay for.
A high price is not a guarantee of excellence nor a low price (or
free) an indication of poor quality.

>Paying for software is a problem... and you expect to make a living 
>writing code?

When did I say I made a living writing code? I don't.

>>74 standard and no ScreenIO.

>Ummmmm... didn't you say that anyone who expected you to learn to use 
>ScreenIO is insane?

No I didn't. I currently use 16 bit ScreenIO although "use" is a bit
of an exaggeration since I haven't actually done any work with it in
over a year.

>This is beginning to resemble dealing with Mr Dilworth.  As Darwin came 
>close to saying, 'Mutate or die'.

I've got another one for you: "If it ain't broke, don't fix it."
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-25T06:19:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa8l7s$6jf$1@panix1.panix.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com> <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com>`

```
In article <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com>,
 <Nospam@neverspam.com> wrote:
>docdwarf@panix.com wrote:
>
…[21 more quoted lines elided]…
>talk to each other.

These two statements are not contradictory; perhaps you need to learn the 
difference between 'a list' and 'a list of all'.

>
>>>>Believe it or not, SOME people think computers are for having fun as well as
…[15 more quoted lines elided]…
>not because at least at this point it's not germane.

So you feel free to call something 'frivolous' or 'serious' but say that 
defining your terms is not germane... might it be asked where you studied 
logic?

>
>>>>> However, let's ask the question to the people who might know: this NG.
…[13 more quoted lines elided]…
>the money.

That might explain the amateurish stance you've taken, certainly.

>
>The first part of your statement is incorrect. A Honda Civic gets you
>to where you're going just as well as a Mercedes.

Do a little research on what happens to a Honda Civic and a Mercedes when 
'getting you there' involves a collision.

>An enormous number
>of examples exist outside the computer world (and probably in it).

Strange that you could not find one to support your view, then.

>
>>>Also I'm emotionally opposed to any language that would
…[5 more quoted lines elided]…
>Ah no.

Ummmm... didn't you just mention, a few paragraphs back, something about 
'we're talking serious business here'?
 
>Just as one gets an instinctive feeling about cars,
>restaurants, movies, people, etc., so also one gets an instinctive
…[3 more quoted lines elided]…
>implementing the boring stuff, etc.

Oh, *I* see... you like to judge a book by its cover!

>
>>>Further, isn't Java that thing that makes surfing the web annoying
…[10 more quoted lines elided]…
>paper will be generated.

You might want to tell that to some serious clients I've had in the past 
little while... they seem to disagree with you and they still produce 
reports by the yard.

>
>OTOH, I do see those pop-ups and rotating elephants and they annoy me
>daily...today... not in some legacy application designed forty years
>ago. It goes again to those instinctive feelings about the quality of
>the language.

Perhaps, given the same amount of time to mature, these might go the way 
of those yards of reports you claim not to have seen.

>
>Thirdly, I'm told (here, on this NG) that I couldn't possibly learn
>Java due to the fact that I don't have the faith--or some
>quasi-religious state of mind. That seems to kill Java for me. 

You believe what you are told readily enough... now, about this bridge I 
have...

>
>>>>Why not simply spend a few bucks and upgrade what you know?
…[6 more quoted lines elided]…
>It's a rhetorical question.

It is still not an answer.

>
>As to your second point, are you familiar with a product called Xtree
…[25 more quoted lines elided]…
>From the above I think you'll see that you don't get what you pay for.

From the above I've seen that you didn't pay for any research into what 
the mail-sorting center needed and purchased some software which did not 
meet your needs; don't blame the tool for your own lack of research.

>A high price is not a guarantee of excellence nor a low price (or
>free) an indication of poor quality.

Life has few guarantees, in case you've not noticed.

>
>>Paying for software is a problem... and you expect to make a living 
>>writing code?
>
>When did I say I made a living writing code? I don't.

That is why I asked the question; thanks for answering.

>
>>>74 standard and no ScreenIO.
…[4 more quoted lines elided]…
>No I didn't.

Thanks for clearing that up, as well

>I currently use 16 bit ScreenIO although "use" is a bit
>of an exaggeration since I haven't actually done any work with it in
…[5 more quoted lines elided]…
>I've got another one for you: "If it ain't broke, don't fix it."

Ummmmmm... I thought the groundwork for your posting was that is *is* 
broke and you are looking for something to replace it.

DD
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 6)_

- **From:** Liam Devlin <LiamD@optonline.net>
- **Date:** 2002-04-27T16:51:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CCAD712.7E7D247F@optonline.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com> <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com> <aa8l7s$6jf$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> In article <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com>,
…[76 more quoted lines elided]…
> 'getting you there' involves a collision.

I wouldn't go here. This is pure Newtonian physics and the more massive
object always wins in a collision with a less massive one. If you focus
on this aspect, we'd all opt to drive buses or dump trucks, both of
which can crush a Merc and not miss a beat. Locomotives might also be a
good choice, but you'd have to adapt them for street use. Besides,
Porsche might go out of business:-)
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 7)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-04-27T17:03:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRAy8.563$Yi1.80061832@newssvr16.news.prodigy.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <aa60pn$81$1@panix1.panix.com> <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com> <aa8l7s$6jf$1@panix1.panix.com> <3CCAD712.7E7D247F@optonline.net>`

```
    That being the case, I think I'd opt for one o' them new Crusader tanks
I've read about lately.  :D
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-27T18:10:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aaf7lf$aa2$1@panix1.panix.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com> <aa8l7s$6jf$1@panix1.panix.com> <3CCAD712.7E7D247F@optonline.net>`

```
In article <3CCAD712.7E7D247F@optonline.net>,
Liam Devlin  <LiamDspam@optonline.nospam.net> wrote:
>docdwarf@panix.com wrote:
>> 
>> In article <i5secu0m8smmth57vvmk0uqhp3pfsgghno@4ax.com>,
>>  <Nospam@neverspam.com> wrote:
>> >docdwarf@panix.com wrote:

[snip]

>> >>Nothing does anything 'just as well' as anything else; do some Serious
>> >>Business and evaluate ROI.
…[13 more quoted lines elided]…
>I wouldn't go here.

I try not to go anywhere that involves collisions... but they seem to 
happen despite my efforts.

DD
```

###### ↳ ↳ ↳ Re: What language?

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-24T12:55:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MWxx8.7716$Y03.416126@typhoon.austin.rr.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com>`

```
Oh brother - this guy just *has* to be a troll. He doesn't even know how to
dowload the Java SDK?

> > VB programmers learn by writing sample code. They are introduced to
> >concepts like FUNCTIONS, then left to search out the functions they
require.
> >Their IDE (Integrated Development Environment) presents suitable
functions
> >to them and also checks their syntax as they write;
>
> That might be how they learn however somewhere someone has a complete
> list of all those functions together with the syntax.

Want to bet? This is Microsoft we are talking about here. They LIVE off
obfuscation. Even the MSDN
disks do not provide what you suggest.Not a complete list, and not all in
one place.


> >Believe it or not, SOME people think computers are for having fun as well
as
> >doing serious business. These people (usually young) are having the
temerity
> >to invade the domain of the "programmer" and learn how to make THEIR
> >computer do what THEY want. (I know...it's sacrilege. Imagine if Users
could
> >get a computer system to do what they wanted...doesn't bear thinking
about,
> >does it <G>?)
>
> Frivolity certainly has its place however we're talking about serious
> computing here. Please keep to the point.

Sure - serious computing without spending any capital? Not unless you are
using GNU tools, which are all
quite a bit more advanced than what you are using.

> >Straight serious answer (no joking or irony): Java.
>
…[7 more quoted lines elided]…
>

This level of ignorance cannot be accidental - troll alert.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T23:01:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<masecu89bcproestkj4i74hieben4o6g0o@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <MWxx8.7716$Y03.416126@typhoon.austin.rr.com>`

```
"Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:

>Oh brother - this guy just *has* to be a troll. He doesn't even know how to
>dowload the Java SDK?

Now why on earth would I know how to download the Java SDK or even
know of such a thing's existence? I'm presuming that you're intimately
involved in the programming or at least the software business; I'm
not. Even when I was actively in data processing it was as a project
manager knowing the user side of the business and writing the
specifications, not as a programmer or as anything to do with the
nitty-gritty of day-to-day activities.

Having mentioned it is there some reason to download this language? Is
it likely to meet my specifications? I could clutter my machine with
every language under the Sun <heh, heh> but I don't think that's the
right way to go about choosing one.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 5)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-25T03:05:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WnKx8.9449$d17.411905@typhoon.austin.rr.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <MWxx8.7716$Y03.416126@typhoon.austin.rr.com> <masecu89bcproestkj4i74hieben4o6g0o@4ax.com>`

```
You claim to be a COBOL programmer needing to change to another language
because it is to expensive,
yet you are making all sorts of wild and disinformative statements.

As to HOW you could know about it - ever hear of Google?  Or read a
newspaper?
Java has been out for years, and has always been free.

-Paul

<Nospam@neverspam.com> wrote in message
news:masecu89bcproestkj4i74hieben4o6g0o@4ax.com...
> "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:
>
> >Oh brother - this guy just *has* to be a troll. He doesn't even know how
to
> >dowload the Java SDK?
>
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 6)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T23:42:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3jtecukn2l9jvmqc5rj8enp60v2s83dive@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3cc55cac_5@Usenet.com> <jlhccu4a46djjfs8j9778t7f6edhamtf8i@4ax.com> <MWxx8.7716$Y03.416126@typhoon.austin.rr.com> <masecu89bcproestkj4i74hieben4o6g0o@4ax.com> <WnKx8.9449$d17.411905@typhoon.austin.rr.com>`

```
"Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:

>You claim to be a COBOL programmer needing to change to another language
>because it is to expensive,
>yet you are making all sorts of wild and disinformative statements.

I don't believe I ever said I was a COBOL programmer, just as I'm not
a plumber but I do most of my own plumbing and am quite happy to
debate the use of plastic instead of cast iron for DWV pipe. My
connection to COBOL was as described below in constructing accounting
applications. I've been on one course in COBOL at IBM for about a week
thirty--my, how time flies--odd years ago. I have however written my
personal application (the one I talk about all the time) in COBOL and
in a business environment I've pitched in to help on occasion.

>As to HOW you could know about it - ever hear of Google?  Or read a
>newspaper?

I know about Java and have heard of it but I didn't know that there
was an SDK. Why would I care? AFAIK this is some super-sophisticated
product that runs on SUN workstations (I don't have one of those) and
is used to do something to web applications. Something annoying, I
believe. How it integrates with HTML and all the other alphabet soup
of add-ons, languages, and browsers I know not, nor do I care because
I have no interest in writing a web application.

Now it appears from this exchange that Java can be used on a
standalone computer entirely independent of the web. Well, great, you
learn something every day but don't accuse me of being a troll based
on my ignorance of Java.

>Java has been out for years, and has always been free.

Like I said, I was aware of the product but did not know it was free
(refer to below).

><Nospam@neverspam.com> wrote in message
>news:masecu89bcproestkj4i74hieben4o6g0o@4ax.com...
>> "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:

>> >Oh brother - this guy just *has* to be a troll. He doesn't even know how
>to
>> >dowload the Java SDK?

>> Now why on earth would I know how to download the Java SDK or even
>> know of such a thing's existence? I'm presuming that you're intimately
…[4 more quoted lines elided]…
>> nitty-gritty of day-to-day activities.

>> Having mentioned it is there some reason to download this language? Is
>> it likely to meet my specifications? I could clutter my machine with
>> every language under the Sun <heh, heh> but I don't think that's the
>> right way to go about choosing one.
```

#### ↳ Re: What language?

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-04-23T14:16:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```

<Nospam@neverspam.com>

> However, let's ask the question to the people who might know: this NG.
> If someone tears that COBOL compiler out of your hot little hands and
> forbids you to use it what is the next language you would use?

I'd open a pig farm.

>
> Bear in mind that I need an industrial strength file system (I hate
…[3 more quoted lines elided]…
> and it only runs on one machine (mine).

Fujitsu is not crippled. And why would anyone insist the compiler run on a
last-generation OS like NT4?

>
> COBOL is lousy for two things: screen input and print output.

Not true. Fujitsu's PowerCOBOL (and others) devises screens much like VB.
Economical add-ons such as SP2 or ScreenIO add GUI functionality to
virtually any COBOL.

>Thus
> ScreenIO and for the minimal amount I print, I output an ASCII file
…[6 more quoted lines elided]…
> output to WPerfect or (if the function exists) output it to IE.

A ListBox can have a file input in VB (or FJ's PowerCOBOL or others). VB is
the gold standard of screen manipulation. Others are 'as good as,' or
'almost as good as...'

Why Word Perfect? This product is even more out of date than NT4. Besides
there are only eight people left who use Word Perfect (and they're all in
Canada - one used to be in Sri Lanka, but he died.).

>
> Or looking at the postings on this group over the last couple of days
> I see a reference to Ada. Free compiler! There's one of the
> requirements straight away!

ADA! Shit, I don't even think the government uses ADA - and they're the one
that promoted it. Why not ALGOL? Anyway, there are at least two free COBOL
compilers out there.


>But as soon as I start looking at the
> website I start to see the gobblydegook: inheritance, encapsulation,
> reentrant, etc, and don't see: "Ada supports the following file types:
> blah, blah.", "Here's how you define an 36 byte alphanumeric field:
> blah blah" etc. Depressing.

Think pigs.
```

##### ↳ ↳ Re: What language?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-23T18:07:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC5A266.37C44219@shaw.ca>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com>`

```


JerryMouse wrote:

>
> A ListBox can have a file input in VB (or FJ's PowerCOBOL or others). VB is
…[6 more quoted lines elided]…
>

Well if it's any consolation I'm not one of the eight. I switched to Word when
it came as a freebie with the machine. You're dead (pun ?) wrong about the Sri
Lankan. He emigrated to Calgary about 30 years ago, the husband of my wife's
friend. Jesus ! Can he screw up a computer. I keep telling him,  use your
fingers on the keyboard, not your elbows, plus a pussy cat is no substitute for
a mouse.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T01:46:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca>`

```
My ISP, neverspam.com, failed to pick up JerryMouse's reply so I
copied it from google:

JerryMouse wrote:

>Nospam@neverspam.com> wrote:

>> Bear in mind that I need an industrial strength file system (I hate
>> using the term but call it a database), a non-crippled language (this
>> is why Fujitsu is no good), and it has to run on NT4. I have access to
>> a free Visual Studio and free SQL server. I only have one application
>> and it only runs on one machine (mine).

>Fujitsu is not crippled.

According to multiple people the free versions of Fujitsu are crippled
by omitting optimization and SQL calls.

> And why would anyone insist the compiler run on a
>last-generation OS like NT4?

NT4 is fine for my purposes. Like with IBM, always remain at least one
release behind so someone else can have the pleasure of fixing the
manufacturer's bugs.

>> COBOL is lousy for two things: screen input and print output.

>Not true. Fujitsu's PowerCOBOL (and others) devises screens much like VB.

Not COBOL, an add-on.

>Economical add-ons such as SP2 or ScreenIO add GUI functionality to
>virtually any COBOL.

I'd question the concept of "economical". You're talking to a guy who
reused his son's copy of Turbotax to avoid paying the $30.

>A ListBox can have a file input in VB (or FJ's PowerCOBOL or others). VB is
>the gold standard of screen manipulation. Others are 'as good as,' or
>'almost as good as...'

OK this seems to be the general consensus and fits in nicely with what
I can obtain for free.

>Why Word Perfect? This product is even more out of date than NT4. Besides
>there are only eight people left who use Word Perfect (and they're all in
>Canada - one used to be in Sri Lanka, but he died.).

Actually I know half a dozen people who use WPerfect and guess what:
every time a virus is reported we sit back and laugh about those using
Word and Outlook Express. The reason I personally use WPerfect is that
I got it free from my employer back around 1992 and it works fine
although I'm currently negotiating for a free 32 bit version.

>> Or looking at the postings on this group over the last couple of days
>> I see a reference to Ada. Free compiler! There's one of the
>> requirements straight away!

>ADA! Shit, I don't even think the government uses ADA - and they're the one
>that promoted it. Why not ALGOL? Anyway, there are at least two free COBOL
>compilers out there.

According to this:

http://www.adaic.org

Ada is alive and well.

As to ALGOL, I'm sure you're not serious but if you were I'd like to
remind you that I'm trying to simplify my life, not the opposite.

I didn't see any free COBOL compilers in the FAQ other than the
crippled Fujitsu version and a 74 standard version but even if there
were other free compilers I'd still have the problem of a replacement
for ScreenIO.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-24T12:49:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iRxx8.7714$Y03.415330@typhoon.austin.rr.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com>`

```
The post I replied to your original message in does not seem to have made it
to the newsgroup, but
essentially, if you are making money off this software, why are you so cheap
with your tools? If you are
not making money off COBOL, and instead are just playing with it, why
agonize? If you want to move
to another language, go ahead - there are lots of nice languages out there
for free - including Ada which
does meet all your supposed criteria. If you are simply looking for an
excuse to buy Visual Basic, just do it.
Most people here probably have. I certainly did, and I certainly regretted
the wasted bucks. Besides being
tied to a single platform, the damn thing is buggy. You publish an
application with it, and the application breaks
because Microsoft changed a DLL on you or something. Not worth the time and
effort, and certainly not
acceptable as a production quality program. Not in my opinion at least.

The Free Fujitsu compiler is not crippled in any sense, other than being
shackled with an abysmal GUI which
fortunately, can be ignored. Sure, it doesn't support SQL calls, but from
your note, what modern Database
are you using anyway? dBASE II does not support SQL. :)

The point is, most of your assumptions are just plain wrong. Very good GUI
capabilities exist for most COBOL's.
The prices are high, but not excessively so for work you make money off of,
and many companies, in particular IBM,
make it possible for you to obtain the latest and greatest tools at a price
that is more than reasonable. Prices so low
that they are, in fact, just covering the media costs.

So given that, I must conclude either you posted a modestly clever troll for
some reason, or you just haven't
thought through your situation.

I'd be pleased to find out I am wrong on that however.

-Paul


<Nospam@neverspam.com> wrote in message
news:clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com...
> My ISP, neverspam.com, failed to pick up JerryMouse's reply so I
> copied it from google:
…[35 more quoted lines elided]…
> >A ListBox can have a file input in VB (or FJ's PowerCOBOL or others). VB
is
> >the gold standard of screen manipulation. Others are 'as good as,' or
> >'almost as good as...'
…[18 more quoted lines elided]…
> >ADA! Shit, I don't even think the government uses ADA - and they're the
one
> >that promoted it. Why not ALGOL? Anyway, there are at least two free
COBOL
> >compilers out there.
>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 5)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T23:09:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <iRxx8.7714$Y03.415330@typhoon.austin.rr.com>`

```
"Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:

>The post I replied to your original message in does not seem to have made it
>to the newsgroup, but
>essentially, if you are making money off this software, why are you so cheap
>with your tools?

I don't make money writing programs (if that's what you mean) but I do
have a commercial (albeit half-hobby) use for the resulting
application.

> If you are
>not making money off COBOL, and instead are just playing with it, why
>agonize?

Because I don't want to spend a lot of time learning and using another
language if it's not the appropriate one.

> If you want to move
>to another language, go ahead - there are lots of nice languages out there
>for free - including Ada which
>does meet all your supposed criteria.

Other people seem to think it doesn't but I would suggest that you and
most of the others who replied don't know what my criteria are. Only
one of you questioned (indirectly) what I was going to use the
resulting application for and although I replied in a vague sense I
don't think it sank in. Now I can't expect on a NG and for free to
write pages of specifications and have someone spend hours analysing
them but I can expect that you would make some assumptions and using
your (the general "your") wealth of experience suggest another
language. Instead, it's been a constant sniping about my (obvious)
contempt for many of the "cool" languages and functions. I'll meet you
(not you personally) toe to toe but I don't think it's very
productive.

> If you are simply looking for an
>excuse to buy Visual Basic, just do it.

I already have VB6, and C++, and Foxpro, and SQL, and InterDev, and a
host of others and while the cost of these is certainly an important
factor it's not the only one.

>Most people here probably have. I certainly did, and I certainly regretted
>the wasted bucks. Besides being
…[4 more quoted lines elided]…
>acceptable as a production quality program. Not in my opinion at least.

Whoa. And this is the gold standard (another poster)? However maybe
we're talking about apples and oranges. Out of VB6 do I get a
standalone exe file? Or can I? If so why would anything Microsoft does
affect one's operation? Unless, I suppose, they remove some functions
from the operating system.

Alternatively I have no need to publish this outside of my machine (if
I did I'd feel really guilty about using a pirate version) so even if
Microsoft changed DLL's how would this affect me? I'm not going to
update the language.

>The Free Fujitsu compiler is not crippled in any sense, other than being
>shackled with an abysmal GUI which
>fortunately, can be ignored. Sure, it doesn't support SQL calls, but from
>your note, what modern Database
>are you using anyway? dBASE II does not support SQL. :)

From Fujitsu's website:

"Limitations
In Fujitsu COBOL Version 3 for students both ODBC connectivity and
optimization are disabled. You will need to purchase Fujitsu COBOL
Version 4 to obtain these functions. "

Optimization???

You might be right about SQL. As I explained elsewhere, I currently
use 18 linked indexed files. On rewrite that will grow to about 33 if
I continue with the same method.

>The point is, most of your assumptions are just plain wrong. Very good GUI
>capabilities exist for most COBOL's.
…[4 more quoted lines elided]…
>that they are, in fact, just covering the media costs.

Just cover media costs? Just where is this cornucopia of IBM tools?
The only thing I've used from IBM in recent years was Disk Manager and
that didn't work properly.

>So given that, I must conclude either you posted a modestly clever troll for
>some reason, or you just haven't
>thought through your situation.

No troll. But you're probably right that I don't know enough to ask
the right questions.

Maybe if I approach it differently and expose just a little of my
application and see what you might recommend as an appropriate
language:

I've already told you in another post that the application is data
entry for a specialized set of movies and parallels what the imdb must
do to capture their data. Let's deal with the area where I enter the
cast of a particular movie, bearing in mind that the following is a
mixture of the current system and how I want to enhance it.

Sample of application***************

I don't like typing and like most people I make lots of typos so
instead of entering a full name each time I have a 1 to 3 character
mnemonic for the most popular actors. Say Tom Hanks is "TH". The
correspondence between the mnemonic of TH and the name Tom Hanks is in
an indexed file called the prompt file. The primary key is the name
and the secondary with no duplicates is the mnemonic. There's also a
third field (and key) which is a sequential computer-allocated number
(in comp-4) which is unique for Tom Hanks. This allows me to use the
number instead of the name as a unique key in the other associated
information about Hanks (DOB, is he a vegetarian, married to, etc.) as
well as the link between the movie and his name (i.e. the movie record
has an array of these numbers indicating who's in the movie).

So, to enter the cast the names of which are written down on a piece
of paper beside me, I bring up a screen (understand we're half-way
though the application) which has just a column of empty slots 25
characters wide and a write only column for the mnemonic. If I have
already entered some actors those slots will be filled with the names
(and if applicable the corresponding mnemonic) and I'll continue to
enter names or delete them or change them or resequence them but I'm
not going to describe those processes. Presume all slots are empty.

The cursor is positioned at the first slot left justified. I enter T-H
(case is indifferent) and hit enter. Presuming that it's not already
on display the program opens up a new box called the prompt list and
fills it with the names of the actors around Tom Hanks, not around the
mnemonic. It gets the list by doing a random read of the prompt file
using the mnemonic as the key (this gives the name)  and then start
not less than Tom Hanks with a key of the name. A read back for five
records and then a read forward (from the original) for five (or how
many there are on the screen) will fill up the prompt list. Naturally
it goes through all the tedious stuff of dealing with the start and
end of file. Tom Hanks and the mnemonic are now highlighted in the
prompt list but the cursor remains on the cast list at the third
position of the first slot (positions 1 and 2 are "T" and "H"
respectively). If the user hits return, the name "Tom Hanks" replaces
the mnemonic, the mnemonic moves to the read only mnemonic column (I
want to keep reminding myself),  and the cursor repositions on slot 2.
The prompt list stays open at the Tom Hanks position.

If "TH" doesn't exist on the prompt file a floating error box opens up
saying "no mnemonic" and the cursor is positioned on character 1 of
slot 1. As soon as the user types a character, the error box goes away
and we start back at the beginning. If the user doesn't hit enter on
characters 1, 2, or 3 we presume he's entering a name that doesn't
have a mnemonic and as from position 4 we'll start the prompt file not
less than the characters typed already and position and highlight the
closet match five from the top with all the happy BS about end and
beginning of file. As each character is typed we'll reposition the
prompt list. Think about the index to the help function in most
windows products with the addition that we show the five before.

As soon as the user sees the name that he wants he uses the mouse to
click on it (maybe a double click?) and the name is copied into the
slot on the cast list. The user could also click on the scroll bar to
move the prompt list up and down (normal windows function) to find the
right name. The cursor remains positioned on the cast slot and never
moves. If the user doesn't find the name on the prompt list he can
continue to type until he has the full name that he wants to add. As
with the mnemonic, he hits enter. If it's a match with the name on the
prompt list we're OK; if not up comes a floating box saying "Name
doesn't exist. Do you want to add?" "Yes/No/Maybe".

If he says "Yes" he'll start the whole process of entering data about
the actor which will drive him down a number of screens but which I
won't go into here. If he says "No" The cursor will remain positioned
at the slot waiting until he enters a valid name and he can go through
this process until the cows come home. Or, at the bottom of the cast
list box are a series of buttons, one of which will be "Finished
adding cast". If he picks that he'll get a floating warning box that
the last one won't be added and he can make the appropriate decision.
There are other buttons on the bottom of the cast list such as one to
allow entry of three or less character names (so they won't be treated
as mnemonics) but again we'll leave that alone.   

End sample******************

The difficulties in COBOL are the tedious screen manipulation (I don't
know how it works in GUI but in 16 bit I have to count each line and
do relative positioning of the cursor and to do the prompt list I have
to hide the cursor (because it's a separate screen)), and the tedious
file positioning especially dealing with the beginning and end.

So without doing anything other than read the above and imagine ten or
fifteen (depending on how you count) other similar lists, what say you
as to the best language?
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-25T03:23:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IEKx8.9456$d17.415015@typhoon.austin.rr.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <iRxx8.7714$Y03.415330@typhoon.austin.rr.com> <kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com>`

```
If you are as cost limited as you say, then COBOL is definitely your best
answer. Fujistu would
do just fine for it in fact. SPFII would remove the tedious problems with
the screen in no time.
If you really don't like the begin/end processing, you could load DB/2. A
Personal Edition of it is
free for developers, I think. If not, it is a very small cost.

If I wanted a pretty cool GUI, I would probably code that in Java, and if I
had a database behind it,
I might code the entire application in Java.

Part of the issue is you need to redesign that application. It sounds overly
complicated with your
screen handling. If you rethink the application path, you can probably find
a simpler, easier to use,
and even better user interface design, and that has nothing to do with text
or GUI or whatever.

On another note, you should really destroy all those MSDN disks (or whatever
you are using to
pirate the MS software from.) Especially if you plan to have any commercial
application. There is
no excuse to pirate, even from Microsoft, when perfectly good free tools
like Fujitsu and Java are
available.

Or you can join PWD at IBM, and investigate tools in the Software Mall.
These are within anyone's
budget.

I expect you won't receive much, if any help around here if you continue to
brag about your
pirate activities.

<Nospam@neverspam.com> wrote in message
news:kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com...
> "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:
>
> >The post I replied to your original message in does not seem to have made
it
> >to the newsgroup, but
> >essentially, if you are making money off this software, why are you so
cheap
> >with your tools?
>
…[12 more quoted lines elided]…
> >to another language, go ahead - there are lots of nice languages out
there
> >for free - including Ada which
> >does meet all your supposed criteria.
…[21 more quoted lines elided]…
> >Most people here probably have. I certainly did, and I certainly
regretted
> >the wasted bucks. Besides being
> >tied to a single platform, the damn thing is buggy. You publish an
> >application with it, and the application breaks
> >because Microsoft changed a DLL on you or something. Not worth the time
and
> >effort, and certainly not
> >acceptable as a production quality program. Not in my opinion at least.
…[31 more quoted lines elided]…
> >The point is, most of your assumptions are just plain wrong. Very good
GUI
> >capabilities exist for most COBOL's.
> >The prices are high, but not excessively so for work you make money off
of,
> >and many companies, in particular IBM,
> >make it possible for you to obtain the latest and greatest tools at a
price
> >that is more than reasonable. Prices so low
> >that they are, in fact, just covering the media costs.
…[5 more quoted lines elided]…
> >So given that, I must conclude either you posted a modestly clever troll
for
> >some reason, or you just haven't
> >thought through your situation.
…[103 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-25T05:11:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC78F84.3F814B13@shaw.ca>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <iRxx8.7714$Y03.415330@typhoon.austin.rr.com> <kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com>`

```


Nospam@neverspam.com wrote:

Well Mr. NoSpam,

I'm not going to belabour this one, but just quickly cover some points. I can
understand your initial reluctance to spell out in detail what the systems was
about. But below gives us more insight. It would also have helped if you had
already told us what software you already had.

1. Commercial application or your hobby - there's a price to pay, if you wish to
advance, or in your case you are suggesting you are going to blow current
limitations. Even a hobby - they don't come cheap. I live in the Great White
North - but I don't ski, too damned expensive. (That's a cop-out - I hate heights
<G>).

2. You mentioned you *were* a project manager designing - that implies the ugly
words "systems analyst", guilty as charged, to which I happily admit. My friend
Don in Toronto will be gritting his teeth - he thinks those are the two filthiest
words in the English language <G>. As you *were* a project manager, I'm gong to
assume you are either semi retired or retired. That puts a limit on your wish to
learn a new gizmo (language) - plus a factor in the costing.

3. With what you have described, you would be OUT OF YOUR MIND to drop COBOL,
which obviously you have expertise in, plus analyst tricks like the mnemonics for
the names. (I have an application where I don't even store descriptions; the user
enters as many as eight characters and I 'generate' the description by stringing
various parts from different tables - if that doesn't make sense, historically
700 sets of files, averaging 300-500 items each, and each record used to hold  a
40 character description. Boy does that save storage !.)

.I'm not even sure that you even need to upgrade your CA-Relia - what is grabbing
all the space in your Data Division - have you got reams of files referenced in
one program ? Even if you picked another viable COBOL, there is still a learning
curve, both CA-R and the 'new one' will be '85 compliant; do you currently use
any Realia specific extensions. Even assuming old and new mesh like a glove,
there is still a reasonable learning curve with a new COBOL product. Does your
current CA-R handle SQL - See 4 below.

4. I can certainly see justification for SQL in your application, and I'm not
addressing all that 4th, 5th level normalization jazz. Your application as is, is
obviously set up to take care of the earlier normalizations, (doing the obvious
things like not repeating fields....) . If you haven't absorbed any SQL yet, go
take a look at the following which should pique your interest. Perhaps you wrote
it, or it was produced by a buddy  :-

            http://www.fluffycat.com/sql/

MS Access is a good tool, (a freebie if you had it installed with your version
of  Windows). Don't know how it would sit with your volumes, or how it would
perform with your volumes  - do a check on an MS site and ask the specific
question. Failing that, take a look at other possible DBs, the price range varies
quite a bit. And as you aren't concerned with being 'portable' pick the DB for
the right price with the right volumes. An attractive feature - those files you
want to generate to send to the printing house - a real cinch from Access -
generate Query Tables in Access in the sequences you want, naming them
appropriately - you can then send the Access Tables (they are bound to have a
copy), or export them as you do currently to CSV files.

Without absorbing your spec in detail, there must be an awful lot of Alternate
keys, or you are achieving it through SORT. SQL/DB largely avoids the sorting.

5. VB - so you have a copy. What's involved time wise switching from ScreenIO to
VB - your effort in days, months. How integrated are your current ScreenIO calls
-
if well embedded in your COBOL - it makes sense you stay with ScreenIO. OK, an
upgrade cost - but put that against the time to learn and use VB effectively,
plus fair chunks of rewrite to invoke VB. (The other possibility was the latest
and greatest from SP2 - but not sure Bob wants to sell you a copy now <G>).

6. Any of the other languages will do - but you have a reticence towards OO - so
why even bother. Plus it really doesn't make sense to completely rewrite an
application that WORKS, in another language, just for the hell of it,
particularly as this is part business/part hobby. It really applies to VB as
well, unless you are solely going to use it as a Dialog tool.

Summary :-

- stick with COBOL
- review your approach to COBOL programs - can you get rid of that Data
  Division limitation by chopping into separate discrete programs
- go DB with SQL. (Can you minimize what's in your Business Logic programs by
  calling separate programs to do the donkey work for SQL queries, just returning

  the result to Business Logic - i.e., your Business program just contains
necessary
  copyfiles in COBOL pic 9/pic x.)
- hopefully stick with ScreenIO - you know it, so upgrade only if necessary

- Lastly, go check your bank balance and get 'expansive'. It's your dime, you
make
  the call. (Come back in 6 months time and tell us you aren't a Tightwad <G>).

Jimmy, Calgary, AB

Footnote : Just out of interest and some forty years ago.

(1) Met a Percy X (can't remember name), who bred hamsters in Surrey, UK.
Zillions of 'em. Started out as a hobby, and when I and my wife visited - he was
well established as a business. The hamsters came in all sorts of colours, sizes,
coat lengths, through breeding - you wouldn't believe. No ramshackle sheds, he
had very swish buildings with electricity, heating and running water and of
course umpteen cages - the little buggers fight one another when there is a pair
in one cage. And most importantly the place didn't stink one bit.

(2) Second one is even more interesting - from memory Virginia Water area in West
Surrey. We went to him to buy a canary, a Yorkshire Roller. My mother hated it.
The louder she spoke, the louder the canary whistled <G>. His business started
out as a childhood hobby. He was into imported birds. You name it, he had it. At
one stage Guinness used a Toucan for advertising that excellent brew. He had the
contract to bring in the birds they photographed for their ads. The attic to his
bungalow was a complete haven for birds, all chirruping their merry little heads
off. Oh, yes, he employed an accountant to 'fix his taxes', and outside his front
door  was his Rolls Royce !!!!

Jimmy, Calgary AB

"Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote:

>
> >The post I replied to your original message in does not seem to have made it
…[194 more quoted lines elided]…
> as to the best language?
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 7)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-26T01:00:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jjjhcu4g74nd5tevilsefbjh8r8nud7n5f@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <iRxx8.7714$Y03.415330@typhoon.austin.rr.com> <kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com> <3CC78F84.3F814B13@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>Nospam@neverspam.com wrote:

>.I'm not even sure that you even need to upgrade your CA-Relia - what is grabbing
>all the space in your Data Division - have you got reams of files referenced in
>one program ?

Yep, main update program processes 19 files, of which 16 are indexed.
No processing is done in the file section; all reads are read into w/s
and writes are write from w/s. Main consumers of space though are the
tables. Lots of tables.

> Even if you picked another viable COBOL, there is still a learning
>curve, both CA-R and the 'new one' will be '85 compliant; do you currently use
>any Realia specific extensions.

{Move X'F8' to 1-byte-data-field} (for example) is Realia extension I
think but easy enough to change. I use this to translate a 9(8) comp-4
field into hex so I can directly modify the files in cases where the
prog abended (not common now; all too frequent in Win 3.1).

I believe {Read file-name prior record} was a Realia extension, now
incorporated into the standard.

The statement:

String Field-A delimited by '(2 spaces)' '(,1 space)' delimited by
size Field-B (Subs-cript) delimited by '(2 spaces)' into Field-A.

(the (2 spaces) is really '  ' but you can't see that too well unless
your newsreader is in fixed point.) Field-A is X(8000) and Field-B
occurs 255 times pic X(25). What I'm doing is stringing the cast into
one long record, squeezing out the spaces, and comma separating them.
I do this under the control of a perform up to 255 times.

This works but according to the manual, the result in Field-A is
indeterminate. I believe that this is now OK in the 85 standard.

Those are the only three dubious items I believe. No esoteric items
(like Initialize or Call by reference) or old stuff (like Alter).

> Even assuming old and new mesh like a glove,
>there is still a reasonable learning curve with a new COBOL product. Does your
>current CA-R handle SQL - See 4 below.

Absolutely not. It's 16 bit.

>4. I can certainly see justification for SQL in your application, and I'm not
>addressing all that 4th, 5th level normalization jazz. Your application as is, is
…[3 more quoted lines elided]…
>it, or it was produced by a buddy  :-

>            http://www.fluffycat.com/sql/

<heh, heh> I notice he even uses Tom Hanks as an example. Looks
simple.

>MS Access is a good tool, (a freebie if you had it installed with your version
>of  Windows). Don't know how it would sit with your volumes, or how it would
>perform with your volumes  - do a check on an MS site and ask the specific
>question.

I have an acquaintance who's a VB programmer, knows my application,
and who has had a lot of experience with Access. He says don't even
consider it. If I can't move to SQL Server or better, keep with the
lean and mean indexed files. The volume is just too high.

>Without absorbing your spec in detail, there must be an awful lot of Alternate
>keys, or you are achieving it through SORT. SQL/DB largely avoids the sorting.

No and no. Most files have one primary key and one alternate. No Sort
(if you mean the verb) is used. There are however internal sorts using
those tables I spoke about earlier.

>5. VB - so you have a copy. What's involved time wise switching from ScreenIO to
>VB - your effort in days, months.

Don't know. VB doesn't look that hard but I'm sure that there are lots
of intricacies I  haven't seen yet.

> How integrated are your current ScreenIO calls

I don't understand the question. All ScreenIO calls are essentially
the same and occur, I don't know, maybe about one every 40 lines of
code.

>if well embedded in your COBOL - it makes sense you stay with ScreenIO. OK, an
>upgrade cost

I can't just upgrade ScreenIO. I have to use a 16 bit with a 16 bit
and a 32 bit with a 32 bit so both the compiler and the front end have
to come up together.

Nor, in response to your other suggestion can I use a 32 bit SQL with
a 16 bit DOS program (at least I don't think so).

Thanks for your efforts. At this stage I'm inclined to try Fujitsu V3
compiler using VB as the front end and keep with the indexed files.
"Try" means doing a small sample (but related) program.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 8)_

- **From:** Edward Reid <edward@paleo.org>
- **Date:** 2002-04-26T09:08:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B8EEC981011021DF0DB3DC60@news-east.usenetserver.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <iRxx8.7714$Y03.415330@typhoon.austin.rr.com> <kbsecukrtojbs79dp5r9o74ae59l7jm2vv@4ax.com> <3CC78F84.3F814B13@shaw.ca> <jjjhcu4g74nd5tevilsefbjh8r8nud7n5f@4ax.com>`

```
On Fri, 26 Apr 2002 1:00:03 -0400, Nospam@neverspam.com wrote
> String Field-A delimited by '(2 spaces)' '(,1 space)' delimited by
> size Field-B (Subs-cript) delimited by '(2 spaces)' into Field-A.
>[...]
> This works but according to the manual, the result in Field-A is
> indeterminate. I believe that this is now OK in the 85 standard.

Nope. Still "indeterminate", and probably always will be. If you have 
any thought of moving a program to another compiler, you should avoid 
this situation. Nowadays, it just doesn't cost that much to STRING into 
another data item and move it back if necessary.

Edward Reid
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-04-24T13:42:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fDyx8.9643$5J6.1066043@bin2.nnrp.aus1.giganews.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com>`

```

<Nospam@neverspam.com>
>
> >Fujitsu is not crippled.
>
> According to multiple people the free versions of Fujitsu are crippled
> by omitting optimization and SQL calls.

Fujitsu is not crippled.

>
> > And why would anyone insist the compiler run on a
…[4 more quoted lines elided]…
> manufacturer's bugs.

Cavalier attitude. You're already two releases behind (Win2K, WinXP).

>
> >> COBOL is lousy for two things: screen input and print output.
…[3 more quoted lines elided]…
> Not COBOL, an add-on.

Nope. Native, included, integrated, combined, packaged together,
proposed-standard conforming. One package. All-in-one, and less of an
"add-on" than the linker.

>
> >Economical add-ons such as SP2 or ScreenIO add GUI functionality to
…[3 more quoted lines elided]…
> reused his son's copy of Turbotax to avoid paying the $30.

Yes, other words do come to mind.

>
> >A ListBox can have a file input in VB (or FJ's PowerCOBOL or others). VB
is
> >the gold standard of screen manipulation. Others are 'as good as,' or
> >'almost as good as...'
…[12 more quoted lines elided]…
> although I'm currently negotiating for a free 32 bit version.

Good. All six of your friends (plus the eight in Canada) can exchange
WordPerfect files as attachements to Eudora. Meanwhile, the rest of the
world will get on with pushing back the foreskin of progress.

>
> >> Or looking at the postings on this group over the last couple of days
…[3 more quoted lines elided]…
> >ADA! Shit, I don't even think the government uses ADA - and they're the
one
> >that promoted it. Why not ALGOL? Anyway, there are at least two free
COBOL
> >compilers out there.
>
> According to this:
>
> http://www.adaic.org

Yeah, and according to the hit counter, 177 people have looked at the page
since 1986.


> I didn't see any free COBOL compilers in the FAQ other than the
> crippled Fujitsu version and a 74 standard version but even if there
> were other free compilers I'd still have the problem of a replacement
> for ScreenIO.

Your problem is not a replacement for ScreenIO.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-04-24T18:30:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cc6efaa.19503986@news.epix.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com>`

```
Nospam@neverspam.com wrote:

>My ISP, neverspam.com, failed to pick up JerryMouse's reply so I
>copied it from google:
…[33 more quoted lines elided]…
>reused his son's copy of Turbotax to avoid paying the $30.

Mr. No Spam:

The concept of "economical" is "in the eye of the beholder" so to
speak.  I know people who place a value on their own time of $150 or
more per hour.  Therefore, if a tool such as ScreenIO or sp2 can help
them save as little as an hour of time per week (or even per month),
then the tool pays for itself very quickly.

I also know people who will spend dozens of hours on a low "out of
pocket" cost alternative when they could have spent $50 and
accomplished the same result in 10 minutes.  Although it may feel good
to save the $50, there is no savings if the value of one's time is
taken into consideration.  This is generally referred to as being
"penny wise and pound foolish."

One other thing.....you may wish to take into consideration the value
of "time served" if Intuit should catch up with you as both you and
your son have violated their license agreement by reusing his copy of
Turbotax.

It is one thing to be cheap and quite another to violate a software
vendor's license agreement.  Now I understand why you choose to remain
anonymous.  You have admitted above to a violation of United States
Copyright Law.  

Oh...and by the way, I believe that Turbo Tax only costs $29.95 at
Staples.  I find it utterly amazing that you would commit a Federal
crime for thirty bucks.

The following is an extract of the license agreement contained in my
legally purchased copy of Turbo Tax 2001:

Software License and Services Agreement and Limited Warranty
Tax Year 2001 TurboTax(r) Software

PLEASE CAREFULLY REVIEW THE TERMS AND CONDITIONS IN THIS LEGAL
AGREEMENT BEFORE INSTALLING OR USING THE SOFTWARE.  BY INSTALLING OR
USING THE SOFTWARE, YOU ARE ACCEPTING THE TERMS AND CONDITIONS IN THIS
AGREEMENT BETWEEN YOU AND INTUIT INC.  IF YOU DO NOT AGREE TO THESE
TERMS AND CONDITIONS, YOU SHOULD CLICK ON THE "I DO NOT ACCEPT" BUTTON
AND THE SOFTWARE WILL NOT BE INSTALLED. IF YOU DO NOT ACCEPT THIS
AGREEMENT AND OBTAINED THE SOFTWARE FROM A RETAIL STORE, RETURN THE
SOFTWARE AND ACCOMPANYING ITEMS TO THAT STORE WITHIN 60 DAYS OF YOUR
PURCHASE WITH A DATED RECEIPT FOR A FULL REFUND.  IF YOU OBTAINED THE
SOFTWARE DIRECTLY FROM INTUIT, RETURN IT WITH THE ORIGINAL PACKING
SLIP WITHIN 60 DAYS OF SHIPMENT OF THE SOFTWARE TO INTUIT RETURNS,
6060 NANCY RIDGE DRIVE, SUITE 100, SAN DIEGO, CA 92121-3290, FOR A
FULL REFUND.
 
IT IS A VIOLATION OF THIS AGREEEMENT TO GIVE A COPY OF THE SOFTWARE OR
THE ORIGINAL DISK THAT YOU RECEIVED TO ANOTHER PERSON, EVEN IF YOU
HAVE COMPLETED YOUR OWN TAX RETURN.  IF YOU DID NOT PURCHASE A LICENSE
FOR THIS SOFTWARE FROM INTUIT OR AN INTUIT AUTHORIZED RETAILER (FOR
EXAMPLE YOU GOT A COPY FROM A FRIEND OR DOWNLOADED IT FROM A
NON-INTUIT INTERNET SOURCE) YOU ARE NOT AUTHORIZED TO USE THIS
SOFTWARE.

blah, blah, blah.......




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 5)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T22:56:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mtqecuoum1f7u76kbrt5rvrjkf74d1gui4@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <01ex8.143276$3L2.12929971@bin7.nnrp.aus1.giganews.com> <3CC5A266.37C44219@shaw.ca> <clhccu8rmin24f5mtb48c7ohbupuuibuoo@4ax.com> <3cc6efaa.19503986@news.epix.net>`

```
rtwolfe@flexus.com (Bob Wolfe) wrote:

>Nospam@neverspam.com wrote:

>>>Economical add-ons such as SP2 or ScreenIO add GUI functionality to
>>>virtually any COBOL.

>>I'd question the concept of "economical". You're talking to a guy who
>>reused his son's copy of Turbotax to avoid paying the $30.

>The concept of "economical" is "in the eye of the beholder" so to
>speak.  I know people who place a value on their own time of $150 or
>more per hour.  Therefore, if a tool such as ScreenIO or sp2 can help
>them save as little as an hour of time per week (or even per month),
>then the tool pays for itself very quickly.

Not my case. As one person (nothing to do with this NG) put it: "COBOL
and ancillary products are priced for the corporate marketplace where
the costs can be spread over thousands of machines and millions of
dollars of product sales." I cannot recover any expenditure.

>I also know people who will spend dozens of hours on a low "out of
>pocket" cost alternative when they could have spent $50 and
…[3 more quoted lines elided]…
>"penny wise and pound foolish."

Unfortunately we're not talking about $50.

>One other thing.....you may wish to take into consideration the value
>of "time served" if Intuit should catch up with you as both you and
>your son have violated their license agreement by reusing his copy of
>Turbotax.

I'm shaking in my boots. Piracy is only a federal offense where it's a
commercial activity--at least that's the way it works for movies--and
even then it has to be more than just a few copies.

While I have some sympathy for people like yourselves (and Norcom and
even CA-Realia) I have none whatsoever for Bill nor in this case for
Intuit. Picture this: I'm happily installing my pirate copy when lo
and behold it suddenly starts installing IE V5.[whatever the current
version is]. No by your leave, please may we... or any warnings. Not
only that but it changes my settings so that on startup IE logs into
Microsoft to check if I really have the latest copy. If you've read
the other postings in this thread, you'll understand how enraged I was
about that. To add further insult it installs a whole series of ads on
my desktop (for AOL etc) which, and I'm sure this is my fault, have to
be removed in a two step process: remove the underlying software and
then next time you boot, remove the shortcut. If you try and do it all
at once you get a sharing violation. 

It's about time I tried pirating one of Turbotax's competitors <g>.
```

#### ↳ Re: What language?

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-04-23T15:36:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa3upt$7mt$1@peabody.colorado.edu>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```

On 22-Apr-2002, Nospam@neverspam.com wrote:

> However, let's ask the question to the people who might know: this NG.
> If someone tears that COBOL compiler out of your hot little hands and
> forbids you to use it what is the next language you would use?

I can't repeat the language I would use - children might be reading this
message.


But - I would use whatever language is appropriate for the task and
environment I am working in.  There is no general answer to what my business
needs would be.
```

##### ↳ ↳ Re: What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T01:46:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lhccu8a62q3ronbniho6s2m5l0ji17qcg@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <aa3upt$7mt$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote:

>On 22-Apr-2002, Nospam@neverspam.com wrote:

>> However, let's ask the question to the people who might know: this NG.
>> If someone tears that COBOL compiler out of your hot little hands and
>> forbids you to use it what is the next language you would use?

>I can't repeat the language I would use - children might be reading this
>message.

<heh, heh>

>But - I would use whatever language is appropriate for the task and
>environment I am working in.  There is no general answer to what my business
>needs would be.

OK...that's a fair statement but I would have thought it was obvious
that I'm comfortable with COBOL and the application works reasonably
well in COBOL + ScreenIO.

I presume everyone is familiar with the imdb; if not:

http://us.imdb.com/search

Behind all the information that they present there must be (a) data
entry/db maintenance program(s). That's my application but I deal with
a specialized set of movies. I do much the same as they do except that
instead of outputting the information to a website, every couple of
years I output an ASCII file with embedded codes which I copy to
diskette(s) and send to my publisher. He feeds it into Quark Xpress
and a month or two later out comes a book.

The actual data is spread over 18 indexed files and in addition to the
main maintenance program there are about 30 other programs to do
housekeeping tasks (for example: check the relationship between each
of the 18 indexed files to ensure nothing has broken). By and large
the 30 additional are batch processing programs. You should be able to
imagine the data entry activities and file storage requirements.
```

##### ↳ ↳ Re: What language?

- **From:** Edward Reid <edward@paleo.org>
- **Date:** 2002-04-25T01:55:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B8ED128000A910ED0DB3DC60@news-east.usenetserver.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <aa3upt$7mt$1@peabody.colorado.edu>`

```
On Tue, 23 Apr 2002 11:36:57 -0400, Howard Brazee wrote
> I can't repeat the language I would use - children might be reading this
> message.

When you're lying awake with a dismal headache
And repose is taboo'd by anxiety,
I conceive you may use any language you choose
To indulge in without impropriety.
  -- W S Gilbert

If anyone cares, I'd use Fortran90. Good language, good compilers 
available at reasonable prices, don't know about IDEs.

Edward Reid
```

#### ↳ Re: What language?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-23T19:22:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC5B3FB.9F2EF25F@shaw.ca>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```


Nospam@neverspam.com wrote:

> This question might upset some of you; if so, I'm sorry but it has to
> be asked.
…[5 more quoted lines elided]…
>

Firstly serves you right for getting involved with CA-Relia. I had a copy
before I latched on to Micro Focus VISOC, predecessor to Net Express. My
reaction to Realia was, this was just another Computer Associates tool,
amongst their many.
I got the impression they didn't have a commitment to COBOL in the sense
that Fujitsu or Micro Focus have. I dropped the product real quick. (It's
yonks ago, but I still get invites to attend their annual gabfests in
Florida or elsewhere - and I see bugger all mentioned about COBOL in their
glossies).

Your reasoning, "can't  afford to upgrade". That kinda shuts out COBOL.
Unfortunately there are no cheapies. Is it that you really feel a need to
switch to one of the sexy languages. At the PC level it narrows down to
VB, C++ or Java. Not familiar, but I think there is a price for VB. We
know that Java starts out cheap (freebie), but for serious production work
you need add-on tools like an IDE (Integrated Development Environment).
Can't recall whether CA-Realia had one, so if it doesn't, my comment might
leave you a bit perplexed - but believe me IDEs are a great boon in the PC
world. Then of course, I suspect whichever of the above three you might
choose, at some stage you are going to want some support libraries,
provided by third parties - here's where additional dollars come in.

(Quick reminder, should you switch to another COBOL,  you can still use
Screen IO).

To be honest, if I was starting from scratch on a PC, I'd go for Java with
C++ as a second. But here's a problem, you've indicated you aren't too
thrilled about the OO jazz - and these are both OO languages. You'll have
to bite the bullet on OO if you are going to make a switch.

I think you are right on the button about the less than business like
approach of explaining these 'other' languages. They just don't seem to be
co-ordinated in the same fashion as COBOL texts. Here are some texts
designed to help the COBOL programmer switch from 'christianity to heresy'
:-

- "Moving from COBOL to C" - Mo Budlong - SAMS Publishing - ISBN:
0-672-30327-2

- "Java for the COBOL Programmer" - Doke & Hardgrave - Cambridge U. Press
- ISBN : 0-521-65892-6 (has a CD)

- "Java for COBOL Programmers " - John C. Byrne -  Charles River Media -
ISBN: 1-886801-84-3 (has a CD). More comprehensive than the previous book.

- "Visual Basic for COBOL Programmers" - Greg Perry - QUE books - ISBN :
0-7897-0268-1 (has a diskette)

And as regards what the others don't cover, I have, "Pitfalls of OO
Development" with chapter headings which cover "Conceptual, Political,
Management, Analysis and Design, Environment, Language and Tool,
Implementation, Class and Object, Coding, Quality Assurance, Reuse" - all
followed by the word 'Pitfalls'. Read this guy's book and kinda looks like
everything is honky dory about files/DBs - they get no mention, not even
in the index !!!

Jimmy, Calgary AB
```

##### ↳ ↳ Re: What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T01:46:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>Nospam@neverspam.com wrote:

>>  I have old 16 bit versions of the Realia compiler and ScreenIO but I
>> can't afford to upgrade so essentially I'm going to have to change
>> languages. The question is: to what? And how to make the process as
>> easy as possible.

>Firstly serves you right for getting involved with CA-Relia. I had a copy
>before I latched on to Micro Focus VISOC, predecessor to Net Express. My
…[6 more quoted lines elided]…
>glossies).

Before they were acquired by CA, they were a dynamic COBOL-committed
company. Back in the early eighties when the company I worked for was
looking for a COBOL compiler Realia were head and shoulders over the
competition, particularly:

- they simply used IBM's language manual and as we all know if IBM
says so, it's so.

- they produced 370 assembler code which although not useful for me,
impressed the hell out of the big iron systems programmers. It may
have even convinced some of them that the PC was not just a toy.

- there was no run-time fee.

- the compliler ran like a bat out of hell in comparison to such
monstrosities as RM COBOL.

- the people from Realia wore suits and white shirts at each of our
meetings. Laugh all you like but this was impressive to a conservative
company. One of the DB mfg's (I think Oracle) didn't get our business
because they dressed casually for their meeting. 

>Your reasoning, "can't  afford to upgrade". That kinda shuts out COBOL.
>Unfortunately there are no cheapies.

Unfortunately you're right.

> Is it that you really feel a need to
>switch to one of the sexy languages.

Hmmm. I don't feel a need in the sense that I'm going to get some
satisfaction out of changing. I'm being pushed to change:

- my indexed files in the application are nearing the magic 64 meg
limit at which I believe the world ends. Splitting these files up
would entail a lot of work

- I have reached and surpassed the limit of Data Division size. Each
time I expand a table those items at the end of the data division just
magically disappear. No warning from the compiler and no abend at
execution time. The data just falls into the bit bucket. This results
in a scramble to cut data items elsewhere and I'm running out of
surplus items.

- I could profit from an expanded screen (beyond 25 * 80).

- I can't run the compiler in a DOS box under NT. I have to boot up
DOS 6.1 and run full screen. Do you know what 25 * 80 looks like on a
19 inch monitor, not to mention the ugliness of having to go through
the compile and then boot NT to run the application. Oops, bug. Shut
down NT, reboot DOS...well, you get the idea.

- I would like to use a mouse.

> At the PC level it narrows down to
>VB, C++ or Java. Not familiar, but I think there is a price for VB.

Not if I have a working copy in my hot little hands, which I do.

> We
>know that Java starts out cheap (freebie), but for serious production work
>you need add-on tools like an IDE (Integrated Development Environment).
>Can't recall whether CA-Realia had one,

Not my version but I believe later ones did and do.

> so if it doesn't, my comment might
>leave you a bit perplexed - but believe me IDEs are a great boon in the PC
>world. Then of course, I suspect whichever of the above three you might
>choose, at some stage you are going to want some support libraries,
>provided by third parties - here's where additional dollars come in.

Hmmm, maybe.

>(Quick reminder, should you switch to another COBOL,  you can still use
>Screen IO).

I'm don't think that 16 bit ScreenIO will work with a 32 bit compiler.

>To be honest, if I was starting from scratch on a PC, I'd go for Java with
>C++ as a second. But here's a problem, you've indicated you aren't too
>thrilled about the OO jazz - and these are both OO languages. You'll have
>to bite the bullet on OO if you are going to make a switch.

>I think you are right on the button about the less than business like
>approach of explaining these 'other' languages. They just don't seem to be
>co-ordinated in the same fashion as COBOL texts. Here are some texts
>designed to help the COBOL programmer switch from 'christianity to heresy'

>- "Moving from COBOL to C" - Mo Budlong - SAMS Publishing - ISBN:
>0-672-30327-2

>- "Java for the COBOL Programmer" - Doke & Hardgrave - Cambridge U. Press
>- ISBN : 0-521-65892-6 (has a CD)
>
>- "Java for COBOL Programmers " - John C. Byrne -  Charles River Media -
>ISBN: 1-886801-84-3 (has a CD). More comprehensive than the previous book.

>- "Visual Basic for COBOL Programmers" - Greg Perry - QUE books - ISBN :
>0-7897-0268-1 (has a diskette)

Sounds great but unfortunately out of print and no used copies
available (I just checked on the last one).
```

###### ↳ ↳ ↳ Re: What language?

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-04-24T13:56:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rQyx8.111623$XV5.10015779@bin4.nnrp.aus1.giganews.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com>`

```

<Nospam@neverspam.com>

> - my indexed files in the application are nearing the magic 64 meg
> limit at which I believe the world ends. Splitting these files up
> would entail a lot of work

I think Fujitsu recently upped their 1 Gig file limit size.

>
> - I have reached and surpassed the limit of Data Division size. Each
…[4 more quoted lines elided]…
> surplus items.

Again, for Fujitsu:
Maximum data item length: 2,147,483,647 bytes
Max char length of elementary item: 2G
Max len alphnumeric edited item: 2G
Max len of numeric edited item: 160
Max value of subscript: 2G
Max repeat count of occurs: 2G
Max number of keys for table element: 2G
Max depth of implicit pointer qualification: 7
For indexed files:
Max rec length: 32760
Max data names in RECORD KEY clause: 254
Max ALTERNATE RECORD KEYs: 254
Max file capacity: 1,073,741,824 bytes

I'm sure other, modern, compilers have similarly generous limitations.
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T23:09:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fqsecu0o6r9h4fcfhts85vsk8c6r586e5v@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com> <rQyx8.111623$XV5.10015779@bin4.nnrp.aus1.giganews.com>`

```
"JerryMouse" <nospam@invalid.com> wrote:

><Nospam@neverspam.com>

>> - my indexed files in the application are nearing the magic 64 meg
>> limit at which I believe the world ends. Splitting these files up
>> would entail a lot of work

>I think Fujitsu recently upped their 1 Gig file limit size.

>> - I have reached and surpassed the limit of Data Division size. 
<snip>

>Again, for Fujitsu:
>Maximum data item length: 2,147,483,647 bytes
<snip>

>I'm sure other, modern, compilers have similarly generous limitations.

None of that was ever in question.
```

###### ↳ ↳ ↳ Re: What language - Realia?

- **From:** <mkozelka@remove.ameritech.net>
- **Date:** 2002-04-24T14:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kazx8.8918$d7.2830721@newssrv26.news.prodigy.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com>`

```
Hi,

    Are you saying that you cannot compile & link DOS-based Realia in a
window on NT4?  We have been using Realia 4.2 (non-GUI, 16 bit) to compile &
link on NT 4.0 for years.  RealDbug also runs.  No need to reboot.

    And if you need to use the "modern" 32-bit version of COBOL from
Fujitsu, you can also compile & link it at the command prompt - no GUI. I
call this "reactionary COBOL".  I'm hanging on, tooth & nail, to the C
prompt.
```

###### ↳ ↳ ↳ Re: What language - Realia?

_(reply depth: 4)_

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-24T22:28:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l0qecu8a431u717jvqeq7gv21j1vhabukd@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com> <kazx8.8918$d7.2830721@newssrv26.news.prodigy.com>`

```
<mkozelka@remove.ameritech.net> wrote:

>    Are you saying that you cannot compile & link DOS-based Realia in a
>window on NT4?  We have been using Realia 4.2 (non-GUI, 16 bit) to compile &
>link on NT 4.0 for years.  RealDbug also runs.  No need to reboot.

I think the problem is in the bind step. I use a batch file but
executing Realbind and just incidentally Realif and Realcopy on their
own return me immediately to the NT desktop.
```

###### ↳ ↳ ↳ Re: What language - Realia?

_(reply depth: 5)_

- **From:** <mkozelka@remove.ameritech.net>
- **Date:** 2002-04-25T19:57:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DcZx8.9102$d7.2931670@newssrv26.news.prodigy.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com> <kazx8.8918$d7.2830721@newssrv26.news.prodigy.com> <l0qecu8a431u717jvqeq7gv21j1vhabukd@4ax.com>`

```
    I just tested it again on NT 4.0, using Realia vers 5.xxx.  And Realcopy
works too.

    This is the bat file I use for Realia 5.x, using a replaceable parameter
for the source file:
>
    forcedos c:\real2\cobol %1,%1,%1
    pause
    forcedos c:\real2\optlink %1,%1,%1,
c:\real2\lib\realcob,c:\real2\lib\realexe.def
    pause
    forcedos c:\real2\realbind /E %1.EXE
>

    I put the pauses in to look for errors (never have any).

    The key is the "forcedos" command. i.e.: C:\>forcedos realcopy
data.txt[t] data.prn[u]
```

###### ↳ ↳ ↳ Re: What language?

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-04-24T18:36:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cc6fa9c.22306118@news.epix.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <3CC5B3FB.9F2EF25F@shaw.ca> <flhccuc6jopfibsgk9ibt02mb44n1hbpil@4ax.com>`

```
Oh...and one other thing, Mr. Nospam:

We have a 16 bit Windows product which would allow you to develop a
GUI screen using your existing compiler.  We even still provide
support for it.

I might have given the software to you under other circumstances, but
I'm not sure that I would want to provide product to someone who
publicly admits that they violate Intuit's license agreement.


Nospam@neverspam.com wrote:

>"James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[121 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: What language?

- **From:** Gary Scott <Gary.L.Scott@lmtas.lmco.com>
- **Date:** 2002-04-23T15:54:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC5C9FB.68B8E7B7@lmtas.lmco.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
Visual Fortran...A step in the OO direction, but one in which you can
advance at your own pace.  Lot's of cross-platform GUI builders
available for it also.

http://www.compaq.com/fortran

Nospam@neverspam.com wrote:
> 
> This question might upset some of you; if so, I'm sorry but it has to
…[74 more quoted lines elided]…
> TIA
```

#### ↳ Re: What language?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-04-24T23:15:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa7vu0$72q$1@slb3.atl.mindspring.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
Lots of notes have gone back and forth on this thread.  Some of them
"silly" - some wrong - some "name calling" - but let me try and understand
what "nospam" is looking for:

1) A compiler (product) that runs on PC's (don't worry about Unix, Linux,
mainframe, whatever) and generates code for this environment

2) The entire "development" product cost should be minimal (my guess is
certainly less than $150 - and probably he/she wants less than $35).

3) The product should (is required to?) produce code for 32-bit Windows
(including Windows NT, Windows XP, Windows 2000) but also (???) for 16-bit
Windows

4) The software needs to support "screen" I/O (I think GUI is preferred, but
I have lost track of that too).

5) The software should require MINIMAL training and conversion from an
existing RM/COBOL source base

6) The software should be "optimized" to run well, support complex (indexed)
file systems, and large/complex data structures.

  ***

If this really is (are) the requirements, I think I have some ideas - but I
do want to verify first that these are the requirements.

nospam,
  Please correct whatever errors I may have made (if any)
```

##### ↳ ↳ Re: What language?

- **From:** Nospam@neverspam.com
- **Date:** 2002-04-25T01:17:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eg1fcukj4gkqduvlhbego8pc1iql0g6l1o@4ax.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <aa7vu0$72q$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

>Lots of notes have gone back and forth on this thread.  Some of them
>"silly" - some wrong - some "name calling" - but let me try and understand
>what "nospam" is looking for:

>1) A compiler (product) that runs on PC's (don't worry about Unix, Linux,
>mainframe, whatever) and generates code for this environment

OK

>2) The entire "development" product cost should be minimal (my guess is
>certainly less than $150 - and probably he/she wants less than $35).

It's a he and yes, those numbers would be acceptable, even the upper
one and for a really appropriate product (which I'm afraid I haven't
been able to identify yet) we could talk about double that.

>3) The product should (is required to?) produce code for 32-bit Windows
>(including Windows NT, Windows XP, Windows 2000) but also (???) for 16-bit
>Windows

Just NT presuming an upgrade to any later Windows version will not
obsolete the product. There is no reason for it to run under 16-bit
Windows. 

>4) The software needs to support "screen" I/O (I think GUI is preferred, but
>I have lost track of that too).

Well ScreenIO (Norcom's product) in a 16 bit format is what I
currently use for screen processing. This is of course character
based. I want to move to 32 bit and GUI but there's no reason (not
that I have anything against it except the cost structure) to insist
on ScreenIO. 

>5) The software should require MINIMAL training and conversion from an
>existing RM/COBOL source base

No conversion required. I will rewrite the application. As to
training...hmmm... I suppose I expect to learn as I go but it would be
nice to have some similarity to what I already know.

>6) The software should be "optimized" to run well, support complex (indexed)
>file systems, and large/complex data structures.

It should run as fast as my current application. Speed is not my
current problem and although I complain about Fujitsu's lack of
optimization, it appears that this only slows down batch processing
and is only noticeable over 100,000 records. While I exceed this
number (by multiples) I only do so a couple of times a year and I
could live with a (reasonable) speed constraint.

If you think an indexed file is complex, OK, I'll agree with that
part.

I don't know what large/complex data structures are. I'm tempted to
say it should support anything COBOL (say Fujitsu's) will support but
that might prejudice the direction of thought.

If you look at my reply to Raulerson dated 2/24/02 at 11.09 pm, you'll
see at the end a description of part of the application. I don't
believe I'm the only person in the world with a look up problem or an
end-of- or beginning-of-file problem or a display problem so I'd be
perfectly happy to consider a product that is not a language itself
but rather a solution at a much higher level. Analogy: I could build
my own word processor but it's a lot cheaper and easier to buy
WPerfect or even Word <g>.

Thanks for your consideration.
```

###### ↳ ↳ ↳ Re: What language?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-04-25T11:50:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24Sx8.9691$d96.9079@nwrddc04.gnilink.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <aa7vu0$72q$1@slb3.atl.mindspring.net> <eg1fcukj4gkqduvlhbego8pc1iql0g6l1o@4ax.com>`

```

<Nospam@neverspam.com> wrote in message
news:eg1fcukj4gkqduvlhbego8pc1iql0g6l1o@4ax.com...
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> >2) The entire "development" product cost should be minimal (my guess is
> >certainly less than $150 - and probably he/she wants less than $35).

$150.00, 32-bit GUI/Windows, AND minimal training? No way.

Pick any two and you have a chance.

MCM
```

#### ↳ Re: What language?

- **From:** Richard Riehle <richard@adaworks.com>
- **Date:** 2002-04-25T18:28:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC8AD32.B413C993@adaworks.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
Nospam@neverspam.com wrote:

> Or looking at the postings on this group over the last couple of days
> I see a reference to Ada. Free compiler! There's one of the
…[4 more quoted lines elided]…
> blah blah" etc. Depressing.

For an easy introduction to Ada, you may download my little booklet,
Ada Distilled, for free from http://www.adaic.org.    I include fully
coded programs, annotation of the each code example, and even
annotate the standard libraries included in the book.   For a really
simple
approach to programning Microsoft Windows in Ada, download a
free set of libraries called JEWL using the http://www.adapower.com
website.   From either site you can download a couple of free compilers.
I recommend the GNAT compiler as a starting place.   If you are going
to program Linux,  you can get a good set of libraries for that as well.

Richard Riehle
```

#### ↳ Re: What language?

- **From:** robert_s_quinn@yahoo.com (Robert Quinn)
- **Date:** 2002-04-30T21:51:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<db500a4f.0204302051.1356d601@posting.google.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
> Or looking at the postings on this group over the last couple of days
> I see a reference to Ada. Free compiler!

Since you mention Ada I will just say that it certainly is NOT dead. 
It is a great language for many people's purposes, from low-level to
systems.

Whether or not it is best for your purposes, I don't know.  If you
drop by comp.lang.ada with any questions (an active group) you could
probably throw out any technical/practical questions you have.

The language Ada is one of those love/hate topics that you see a lot
of people taking passionate stands for and against, like the writings
of Ayn Rand.  I would just say investigate and think with your own
mind about it.

Regards,
Robert Quinn
```

#### ↳ Re: What language?

- **From:** robert_s_quinn@yahoo.com (Robert Quinn)
- **Date:** 2002-04-30T21:54:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<db500a4f.0204302054.5f54360d@posting.google.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```
Oh yes, and I understand you can interface Ada to Cobol, if that means
anything to you.
```

#### ↳ Re: What language?

- **From:** bsambartolo <member24915@dbforums.com>
- **Date:** 2003-02-13T19:48:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2526463.1045165734@dbforums.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com>`

```

do you still have that 16-bit realia compiler? if so i'd be interested
in buying it
```

##### ↳ ↳ Re: What language?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-14T01:23:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4c448e.66742353@news.optonline.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <2526463.1045165734@dbforums.com>`

```
bsambartolo <member24915@dbforums.com> wrote:

>do you still have that 16-bit realia compiler? if so i'd be interested
>in buying it

I have it. Will send a copy for free. I doubt CA considers it valuable enough to
protect.
```

###### ↳ ↳ ↳ Re: What language?

- **From:** bsambartolo <member24915@dbforums.com>
- **Date:** 2003-02-14T14:01:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2529753.1045231311@dbforums.com>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <2526463.1045165734@dbforums.com> <3e4c448e.66742353@news.optonline.net>`

```

would you email it? (is it not copy-protected?)

Originally posted by Robert Wagner 
> bsambartolo  wrote:
>
…[5 more quoted lines elided]…
> enough to
protect. 
```

###### ↳ ↳ ↳ Re: What language?

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T02:11:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4da14e.156035529@news.optonline.net>`
- **References:** `<fqm9cug7ith14ta32hs8gdu6s38qdod6vl@4ax.com> <2526463.1045165734@dbforums.com> <3e4c448e.66742353@news.optonline.net> <2529753.1045231311@dbforums.com>`

```
bsambartolo <member24915@dbforums.com> wrote:

>
>would you email it? (is it not copy-protected?)

I already tried .. to member24915@dbforums.com. The message bouced. 

>Originally posted by Robert Wagner 
>> bsambartolo  wrote:
…[10 more quoted lines elided]…
>Posted via http://dbforums.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
