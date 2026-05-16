[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Style vs Substance

_9 messages · 6 participants · 2001-07_

---

### Re: Style vs Substance

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-12T13:37:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4D9A1C.2D911549@Azonic.co.nz>`

```
> Mr. Dashwood accuses me of 'denigrating' his code. What I actually 
> said was 'Mr. Dashwood's post gives us all an opportunity to compare
> a structured program with one written in a sensible manner. . .'.

Implying that his was not sensible.

> This suggests to me that Mr. Dashwood judges COBOL code primarily
> by what it LOOKS LIKE rather than whether it is efficient, simple,
> compact, sensible, easy-to-comprehend, and so on.

What is 'easy-to-comprehend', or is considered 'simple', is entirely
what one is used to.  A point that you continually fail to understand. 
While your code is 'simple' and 'easy-to-understand' _TO_YOU_, this does
not make it these in any absolute way.

The reason that it is _NOT_ simple and easy-to-understand to others is
that they do not have the several decades of experience of working with
this code.  You have a built-in 'dictionary' so that when you look at a
single line of your code you can immediately see its place in your
universe.

Others do not.  For them to understand your program they have to
understand _all_ of it by tracing through each path and referring back
to each data item, keeping track of actual usage.

Similarly you think that other programmer's work is 'hard to understand'
and 'complicated' because it is not like one of yours, and doesn't use
the same 'dictionary' as you do.

You appear to consider that third parties _should_ think that your
programs are 'better', or at least 'easier-to-understand', simply
because you do. There are actually very good reasons why they do not.  

One reason is that, upon coming across a completely new system, it is
necessary to understand it in small parts and expand this knowledge
outwards.  Modular styles of programming cater for a modular approach to
understanding.  Your programs are not modular (though they are
repetitive), they must be understood in the large.  While your programs
are generally 'small' they are not as small and easy to understand as a
module in other programmer's work.

The other problem is that you do not use names that are meaningful to
others.  They are highly meaningful to you because you have created and
reused these for decades.  In order to understand your programs it is
first necessary to learn, or build, a dictionary that you have built in.

You 'know' that 'M1' (or whatever) has a very specific meaning, what you
completely fail to realise is that _nobody_else_knows_nor_cares_.  Nor
are they likely to bother learning what all those codes are for, which
is the prerequite for understanding your code.

> On the other hand, Mr. Dashwood's code is markedly different - upon
> a casual glance it might even be C or Java or something with

Most programmers continue to learn new languages and apply what they
consider to be improvements into their coding.  

> its nested construction and mostly lower-case style and lots of lines
> and wasted space.

It is rather 'confusing' until you get used to it, as is everything else
that does not look exactly what one expects to see.  However, while you
find 'nested contruction', lower-case, and spaced out style 'confusing'
and 'hard to understand', we do not.  We are confused and frustrated by
tangles of GO TOs, meaningless (to us) codes instead of names, and
clustered compact code.

> This suggests to me that Mr. Dashwood judges COBOL code primarily
> by what it LOOKS LIKE rather than whether it is efficient, simple,
> compact, sensible, easy-to-comprehend, and so on.

> A good example of cluttering programs up with useless stuff in order
> to make them seem, perhaps, more stylish, is Mr. Dashwood's 
> use of 'binary-fields', indexing, COMP-5 and SECTION.

How ironic.  You complain that PD judges code on appearance and not on
whether it is 'efficient', 'compact' and 'sensible', and then you
comment on the _appearance_ of using "'binary-fields', indexing, COMP-5"
when these actually produce more compact, more efficient and more
sensible code.

> It is categorically impossible to justify the use of these things
> on TECHNICAL GROUNDS, 

You are entitled to your _opinions_, but once again you treat these as
if they are some sort of absolute that must be accepted by everyone.

> On the other hand, my code is totally devoid of any unnecessary
> frou-frou, 

It is also devoid of anything that would make it understandable to
_others_.  You write for yourself, and judge your own code by how easy
it is for _you_ to read and understand.  You have no idea at all how
others view it (except from messages posted here which you completely
ignore).

> is utterly simple, compact, easy-to-read, neat,
> efficient, 

An APL programmer would say exactly that about their APL code.  To
others it is meaningless gibberish.

> and, although one could change it, it would be hard
> to make a significant improvement. 

I would agree that changing it would not make any improvement.  The
fault with it lies in your whole approach to programming which is to
base all code on an unspecified set of inbuilt (to you) codeification
which is unavailable to others.

> My approach to programming
> is to do what I need to do with the utmost economy both in terms
> of the time it takes to write and the efficiency of the code.

With no thought _at_all_ to others being able to understand it.

> My approach to programming
> is to do what I need to do with the utmost economy both in terms
> of the time it takes to write 

What makes you think that others take longer to finish a program than
you do.  While you may well reduce the number of keystrokes, others may
use more powerful editors that can produce the code more intelligently,
such as with key-macros and completions, or simple copy-paste with
multiple files open.

Now for example for a master file edit program, it may only take you
half a day to construct one for a new file (based on what you have said
about how you write programs).  But I have a huge complex file
maintenance program that will maintain all the files that I design with
a simple text dictionary and screen layout.  I'll bet I can put together
a simple system much faster than you can write new programs to do it.

I also have a screen code generator that will take a text layout and an
FD and generate a file maint program faster than you could load up your
editor.

Much more importantly, If there is an improvement that I can make in the
user interface then I only need do it once instead of into each separate
program that you seem to have.  You may well be able to write 'more
programs per day', but I will get the job done faster by not writing
programs.


> I don't really care if people write inane programs full of
> ostentatious stuff, but I do care when people criticize me for
> not doing the same thing. 

No. We criticise you for completely failing to understand, or accept,
what others have been saying.  You have been writing code in isolation
for decades and have completely failed to 'grow' with the industry, or
even to cater for others.

What you consider 'inane' and 'pretentious' is what makes the program
understandable by third parties (yourself being an obvious exception). 
While you write for yourself only (but don't understand that this is the
case), most others write for 'the next maintainer'.
```

#### ↳ Re: Style vs Substance

- **From:** "Paul Pigott" <paul.pigott@worldnet.att.net>
- **Date:** 2001-07-12T02:07:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8D737.1455$gj1.46454@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3B4D9A1C.2D911549@Azonic.co.nz...

    <<large snip>>

> > I don't really care if people write inane programs full of
> > ostentatious stuff, but I do care when people criticize me for
…[10 more quoted lines elided]…
> case), most others write for 'the next maintainer'.

As a systems manager over COBOL programmers, one of the things I always tell
them is to write your code as if you (the original programmer) were the one
coming back to maintain it 5 years from now.  It's not always _necessary_ to
write for the maintainer, but it's easier in the long run if you always
_do_.

Paul
```

#### ↳ Re: Style vs Substance

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-07-12T15:22:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b4d1c00_2@news2.newsgroups.com>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz>`

```
A very balanced and fair commentary, Richard.

Personally, I find it hard to be as understanding about it as you have been,
but that's because of the past acrimony which affects my judgement when it
comes to "things Foodman"...<G>

I derived benefit from reading your comments.

I seem to recall you made some similar points to him the last time he
requested judgement on "modern code" (using a small sample I posted, which I
would never claim is as "good as it gets"),  against his (which utilises the
"Dilworth special" technique).

Sadly, it's like talking to a brick wall...

Pete.

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B4D9A1C.2D911549@Azonic.co.nz...
> > Mr. Dashwood accuses me of 'denigrating' his code. What I actually
> > said was 'Mr. Dashwood's post gives us all an opportunity to compare
…[154 more quoted lines elided]…
> case), most others write for 'the next maintainer'.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

#### ↳ Re: Style vs Substance

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-13T08:06:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4E9DDC.9E5B6F9F@Azonic.co.nz>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz>`

```
> Richard made the point that Tony's "style" requires an innate "dictionary"
> that Tony has developed and memorised over years. I would say that every
> program he codes should contain a commentary that describes this
> "dictionary" for ordinary mortals (maybe a COPY book). I wonder if they
> do...?

The sad thing is that Tony _knows_ his style requires an intensive
training course in order to become indoctrinated:

From "The Big Picture" by 'Foodman' (Tony Dilworth)--------------------
> On day one, hour one, my new employee (if I needed one) would be
> presented with the following:
…[10 more quoted lines elided]…
> to manufacture until they gained experience.
----------------------------------------------------------------------

Yet he still insists that he should be able to post small samples and
have others think it 'easy to understand' and 'simple' without having
been through this requirement of solitary confinement.

He also had to choose his victims:

TD> In the olden-days, when I hired people, a lot of them would lose
TD> interest when told that they would have to adhere to strict
standards.

Or perhaps when they saw what those standards were.

TD> So, I hired raw trainees. People who had completed any COBOL course.
TD> Prior experience undesirable. Computer Science degree undesirable.
TD> ...
TD> The people I hired were grateful to get the job.

It seems that to 'appreciate' FoodMan's 'style' there is a requirement
that one be a clueless student who has never seen how others write code
and who can't get a job somewhere else.

For those new to the discussion go back into Dejanews and read "The Big
Picture" then you can form an objective view rather than relying on my,
and Peter's, bias.
```

##### ↳ ↳ Re: Style vs Substance

- **From:** "Douglas Gallant" <dgallan1@nycap.rr.com>
- **Date:** 2001-07-14T01:13:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W0N37.38393$EF2.5790887@typhoon.nyroc.rr.com>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz> <3B4E9DDC.9E5B6F9F@Azonic.co.nz>`

```
Now, I also dislike Tony's particular coding style, however the
indoctrination on coding standards I don't believe is uncommon in large
installations. The goal being the same - if we agree on some basics then
coding and maintenance hopefully are easier as compared to everyone just
doing their own thing.


"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B4E9DDC.9E5B6F9F@Azonic.co.nz...
> > Richard made the point that Tony's "style" requires an innate
"dictionary"
> > that Tony has developed and memorised over years. I would say that every
> > program he codes should contain a commentary that describes this
…[45 more quoted lines elided]…
> and Peter's, bias.
```

#### ↳ Re: Style vs Substance

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-13T12:41:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4EDE61.A00BBE3B@Azonic.co.nz>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz>`

```
Peter Lacey (lacey@mb.sympatico.ca) wrote:

>  The  program specs or documentation in theory
> have the answer, but in practice nobody keeps them current.  The ONLY way to
> preserve this sort of knowledge is to put it in the program source as a
> comment.

The way that I deal with this is to have the user documentation for the
program incorporated into the program source code as HTML in comment
lines.  This is extracted into the help directory for the users to read
if required.  In the program source these lines are marked so that
commented code or other comments are not extracted.

In this way I can remember to update the documentation as I work on the
code and, more importantly, there is a direct relationship between the
code and the documentation lines.  Sometimes I shuffle the program
source to ensire that the resulting documents are structured better (the
extract is linear), but then this matters not because I haven't used
paragraph numbers, which always seemed a useless contrivence after I
progressed beyond card-packs and lineflow listings.
```

##### ↳ ↳ Re: Style vs Substance

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-07-13T03:04:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010712230451.22572.00000968@nso-fq.aol.com>`
- **References:** `<3B4EDE61.A00BBE3B@Azonic.co.nz>`

```
In article <3B4EDE61.A00BBE3B@Azonic.co.nz>, Richard Plinston
<riplin@Azonic.co.nz> writes:

>
>The way that I deal with this is to have the user documentation for the
…[5 more quoted lines elided]…
>

Could you show an example of how you go about doing this?
I am a little slow on the up-take of such ideas.
I am curious how you would code your comments to differentiate
between actual program source code, internal program comments,
and comments for HTML User documentation.

I like the idea, just not sure I understand how you get there.

Thanks for your time.
```

##### ↳ ↳ Re: Style vs Substance

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2001-07-12T22:57:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4E71B1.B88EE22E@mb.sympatico.ca>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz> <3B4EDE61.A00BBE3B@Azonic.co.nz>`

```
Richard Plinston wrote:

> Peter Lacey (lacey@mb.sympatico.ca) wrote:
>
…[10 more quoted lines elided]…
>

A good practice!  But, one question: how do you differentiate between what the
users need and what the programmers need?  They aren't always the same thing.

PL
```

###### ↳ ↳ ↳ Re: Style vs Substance

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-14T08:32:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4FF576.59DA5336@Azonic.co.nz>`
- **References:** `<3B4D9A1C.2D911549@Azonic.co.nz> <3B4EDE61.A00BBE3B@Azonic.co.nz> <3B4E71B1.B88EE22E@mb.sympatico.ca>`

```
Peter Lacey wrote:
> 
> A good practice!  But, one question: how do you differentiate between what the
> users need and what the programmers need?  They aren't always the same thing.

In the program the lines that are extracted are marked as a block by
tags <html> and </html>, all comment lines btween these are extracted.  

       *<html>
       * To customer type determines the price used with:
       *<dl> 
            EVALUATE Customer-Type
       *<dt> R <dd> Retail price.
            WHEN "R"        MOVE PR-Retail    TO WS-Price
                            MOVE ZERO         TO WS-Plusage
       *<dt> C <dd> Cost Plus, used for Interbarch transfers
       *            and staff sales.
           WHEN "C"         COMPUTE WS-Price = PR-Last-Cost 
                                  * ( 1 + ( CR-Plusage / 100 ) )
                            MOVE CR-Plussage  TO WS-Plussage
       ^ etc
       *</dl>
       *</html>

The extractor builds a basic html framework, there is a <title> line at
the start to use for the heading.  It also adds <p> tags whenever there
is a blank comment line to separate the paragraphs.  Some special
processing is done for <pre> blocks.  It can process COPY files by
following a *<include> filename, though I seldom need to do
this.              

Comments that are not within an <html> block are not extracted.
 
There is another program that builds an index for these from the menu
file so that this looks like the application menu and when they click on
an item it goes into the program document.  

This set of program documentation is intended to cover the detail
aspects of the programs, there are also overview pages as well.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
