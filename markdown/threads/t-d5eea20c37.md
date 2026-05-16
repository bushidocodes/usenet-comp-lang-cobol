[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# benefits of cobol in the present?

_15 messages · 9 participants · 2002-01_

---

### benefits of cobol in the present?

- **From:** Chris Humphries <chumphries@devis.com>
- **Date:** 2002-01-08T15:01:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3AC316.8080705@devis.com>`

```
Hello All,
     I am starting to learn COBOL, and am just curious what would be the
  benefit of learning it besides to update older programs? I am learning
  it for fun (most i tell that too tell me "I'm sorry" or "Are you out of
  your mind?!").
     Is cobol "worth" learning in todays environment, with things like
  python and c++?


     Thanks in advance.

-chris humphries
  systems analyst
```

#### ↳ Re: benefits of cobol in the present?

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-01-08T15:42:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com>`
- **References:** `<3C3AC316.8080705@devis.com>`

```

On  8-Jan-2002, Chris Humphries <chumphries@devis.com> wrote:

>      I am starting to learn COBOL, and am just curious what would be the
>   benefit of learning it besides to update older programs? I am learning
…[3 more quoted lines elided]…
>   python and c++?

It depends on what's "fun".

CoBOL's benefits are pretty much the same as they always were - being the
dominant language for business applications.   (not counting whatever
"language" spreadsheets are).  While it's not quite as dominant, as business
needs have broadened into such things as XML and such, most business rules
are still being implemented in CoBOL.

I'm not sure though that you will find business rules, accounting, and
typical business needs to be fun.   So we need a better definition of your
goals before we can give you a meaningful answer.
```

##### ↳ ↳ Re: benefits of cobol in the present?

- **From:** Chris Humphries <chumphries@devis.com>
- **Date:** 2002-01-08T16:14:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3AD438.5090106@devis.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com>`

```
fun as in learning a new language. Not really after any specific
goals (like building a game or something). I just enjoy learning
new languages, and that is satisfaction in and of itself.

just curious on the road ahead, and how cobol may be better
at some things and how it may compare to other languages in the
scope of neat and powerful things you can do with it.

thanks :)
-chris



Howard Brazee wrote:

> On  8-Jan-2002, Chris Humphries <chumphries@devis.com> wrote:
> 
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2002-01-08T08:11:29-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3B2841.44C0270B@dced.state.ak.us>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com>`

```
On the one hand I can think of very little that is better for learning good
programming techniques than COBOL. Of course I only work in 2 languages-COBOL and
VB. (I used to work in C but haven't used it in years.)

Working with VB programmers I find that they place so much emphasis on the
interface that they (in general) lack the ability to follow the data. Further,
they are so blinded by VB's 'event-driven' model that they don't seem to realize
that nearly *all* programs are actually sequential. VB simply hides/automates the
main control loop. (The only reason I said nearly all is because there are
supposedly some multi-threaded VB programs out there. I've never seen any but if
they exist then those programs, as a whole, would not be truly sequential. Each
thread, however, would be.)

These lacks IMO make VB programmers unsuited for 'the big time'.

Now COBOL doesn't force you to write well-designed programs, but it does force you
to pay attention to what happens to the data as you execute the program. Moreover,
it also forces you to think about the order in which code is actually executed-not
only within each 'module' but also the order in which the different modules are
executed. In my experience all of that is important to writing a well-designed
program. It's really not any harder to write a well-designed program in VB than it
is in COBOL, but it seems as if VB-only programmers simply lack the
experience/training to do so. At least that's been my experience with them.

Chris Humphries wrote:

> fun as in learning a new language. Not really after any specific
> goals (like building a game or something). I just enjoy learning
…[4 more quoted lines elided]…
> scope of neat and powerful things you can do with it.
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-01-08T19:09:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HtH_7.129$zq1.452462@paloalto-snr2.gtei.net>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com> <3C3B2841.44C0270B@dced.state.ak.us>`

```
Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us> wrote in message
news:3C3B2841.44C0270B@dced.state.ak.us...
> Working with VB programmers I find that they place so much emphasis on the
> interface that they (in general) lack the ability to follow the data.
Further,
> they are so blinded by VB's 'event-driven' model that they don't seem to
realize
> that nearly *all* programs are actually sequential. VB simply
hides/automates the
> main control loop. (The only reason I said nearly all is because there are
> supposedly some multi-threaded VB programs out there. I've never seen any
but if
> they exist then those programs, as a whole, would not be truly sequential.
Each
> thread, however, would be.)

I do not work in VB (I use PowerBASIC), but in Windows in general
"sequential" is relative: it depends on how you define "re-entrant."

It would not be uncommon at all for a procedure to call itself when
processing messages. The closest I could write this in COBOL might be
something like....

PROGRAM-ID. MAIN.

...
   CALL 'function' using parm-1 parm-2

END PROGRAM MAIN.
PROGRAM-ID. FUNCTION.

PROCEDURE DIVISION USING parm-1, parm-2
....
     CALL 'function' using a, b


Under Windows, in the "main control loop" (the message loop), it is really,
really easy to execute some system call which triggers a series of other
calls to the "main control loop", totally transparently. (It is all
documented quite nicely, but looking up each action to see what additional
actions it may rmay not trigger can be quite tedious). Not to mention, user
or other actions can "CALL FUNCTION" while "function" is still processing an
earlier request.

VB's design philosophy is to "hide" all this from the programmer - at the
cost of some functionality (i.e., true multi-threading). So, yes, VB
programmers "should" be able to handle "pure" sequential processing, as
using the "VB default processing" is pretty much that. However, writing
re-entrant code is advanced in any language.

Let's not forget that Microsoft VB was designed to allow non-rocket
scientists to write simple programs, and has succeeeded (spectacularly!) in
attracting those non-rocketeers to its ranks. As a result, IMNSHO,  the
average COBOL programmer is a far better programmer than the average VB
programmer; and what is "simple" to the average COBOL programmer may in fact
be totally alien to the average VB programmer.

MCM
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

_(reply depth: 5)_

- **From:** Chris Humphries <chumphries@devis.com>
- **Date:** 2002-01-08T19:21:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3B0000.7070300@devis.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com> <3C3B2841.44C0270B@dced.state.ak.us> <HtH_7.129$zq1.452462@paloalto-snr2.gtei.net>`

```
X Windows has been using the callbacks forever, and it totally
event driven.

VB isnt that great a language, and isnt portable. But i guess
some just would rather stick in M$ than with *nix. I dont understand
it.

anywho, my 2 cents.



Michael Mattias wrote:

> Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us> wrote in message
> news:3C3B2841.44C0270B@dced.state.ak.us...
…[71 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-09T11:03:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c3b7327_8@Usenet.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com>`

```
This is a good response Chris; I admire (and share) your sense of seeking
new things for the "fun" of it.

Normally, I wouldn't respond to a thread such as this because these
arguments have been flogged to death here many times and are, frankly,
boring. (Well they are to me, at least...<G>)

However, here's what you asked for:

1. COBOL is the best language bar none for manipulating da





Chris Humphries <chumphries@devis.com> wrote in message
news:3C3AD438.5090106@devis.com...
> fun as in learning a new language. Not really after any specific
> goals (like building a game or something). I just enjoy learning
…[18 more quoted lines elided]…
> >>  it for fun (most i tell that too tell me "I'm sorry" or "Are you out
of
> >>  your mind?!").
> >>     Is cobol "worth" learning in todays environment, with things like
…[5 more quoted lines elided]…
> > CoBOL's benefits are pretty much the same as they always were - being
the
> > dominant language for business applications.   (not counting whatever
> > "language" spreadsheets are).  While it's not quite as dominant, as
business
> > needs have broadened into such things as XML and such, most business
rules
> > are still being implemented in CoBOL.
> >
> > I'm not sure though that you will find business rules, accounting, and
> > typical business needs to be fun.   So we need a better definition of
your
> > goals before we can give you a meaningful answer.
> >
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-09T11:50:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c3b787e_2@Usenet.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com>`

```
This is a good response Chris; I admire (and share) your sense of seeking
new things for the "fun" of it.

Normally, I wouldn't respond to a thread such as this because these
arguments have been flogged to death here many times and are, frankly,
boring. (Well they are to me, at least...<G>)

However, here's what you asked for:

1. COBOL is the best language bar none for manipulating data, both in memory
and from external media. Type casting is unnecessary (it is done for you)
and it is transportable across platforms, ensuring that the form most
efficient on the platform it is compiled to is utilised automatically. For
example, you can define arithmetic fields as USAGE COMP and know they will
be efficient on ANY platform. In recent years (well, the 80s are "recent" to
old timers like me...<G>) with the advent of "Little Endian" processors,
this usage has been extended to COMP-5, so we could use this across all such
platforms. A small and simple enhancement to the code for machines with this
architecture, implemented easily with a text editor, and providing optimum
efficency.

2. COBOL (when written properly) is the easiest source code to maintain.
This is arguable of course (one man sees "readability" as another's
"verbosity"), but its English like nature does make it quick to pick up when
you have to change it after a year or so.

3. COBOL provides a level of control which allows you to do very "clever"
things with data. For example, I never use "bound" controls on Databases.
While they work OK, I prefer to use COBOL with ESQL to manipulate my
Relational DB stuff. This way I have total control over what I want to do
and am not constrained to what the bound control can do. (This one will be a
personal choice and I don't think using bound controls is "wrong", I just
prefer to use COBOL).

4. In today's Web Oriented World, COBOL has a useful place in CGI
programming where its data manipulation capabilities make it more useful
than Python or PERL and a serious contender to Java Servlets. (Watch for the
 release of  DOT NET next month and Fujitsu's NetCOBOL which is designed to
integrate with it. Fujitsu and MicroSoft are partners.)

5. Object Oriented COBOL is ideal for building ActiveX (COM and DCOM)
components and my personal belief is that this is where the future lies. The
days of Source Language being relevant are nearly over. Systems like .NET
will run code that is written in a plethora of languages and we are at last
approaching a stage where it will be "the best language for the job" that
decides what a given component will be written in.

I already have applications where components written in C++, VB, and COBOL
all peacefully co-exist on the same Windows form and I see this being
extended in the future. Note that the person using the application neither
knows nor cares what source was used, as long as the components function as
required (and they do).

If 300,000,000 people are all accessing the Internet, it is fair to asssume
they have a computer <G>. If they have a computer they will want to use it.
They are not about to become computer programmers and we are already seeing
"Wizards" which enable non-technical people to achieve a level of competence
for certain jobs where specific code is necessary. This idea will expand
rapidly in the present and next decade and we will see people interacting
with their Wizards to get the functionality they require. The Wizards will
get much "smarter" and will have access to thousands of components, which
will be written in the "best language for the job".(And the users won't
care...the arguments about code elegance and choice of source language will
be left to academics (and that's properly where they belong, in my
opinion...))

COBOL IS the "best language" for certain jobs. However the public perception
that it is a Legacy Language for mainframes is hampering its advancement,
and the attitudes of COBOL programmers and the COBOL "establishment" is
doing nothing to help it either. "Fortress COBOL" dug in on the mainframes,
is NOT where the Language has to go if it is to survive. Client/Server
systems written in COBOL, utilizing the COBOL file system, so they are
"closed" and can only be accessed by COBOL programs, are another nail in
COBOL's coffin. Today's businesses require interconnectivity and "open"
exchange of data. Code that can't participate in this will become "pariah"
code to be shunned and discouraged by all (and quite correctly; there is no
need for this, and people who do it believing they are ensuring COBOL's
continued use are just plain wrong...)

Please go to www.aboutlegacycoding.com. Click the "Archive" button and read
an article that was published in April 2001, called "Meet the Future". This
article covers most of my arguments as to why you should learn COBOL.

I wish you every success in the future and please don't let anyone grind the
edge off your sense of what is "fun" <G>.

Pete.

Chris Humphries <chumphries@devis.com> wrote in message
news:3C3AD438.5090106@devis.com...
> fun as in learning a new language. Not really after any specific
> goals (like building a game or something). I just enjoy learning
…[18 more quoted lines elided]…
> >>  it for fun (most i tell that too tell me "I'm sorry" or "Are you out
of
> >>  your mind?!").
> >>     Is cobol "worth" learning in todays environment, with things like
…[5 more quoted lines elided]…
> > CoBOL's benefits are pretty much the same as they always were - being
the
> > dominant language for business applications.   (not counting whatever
> > "language" spreadsheets are).  While it's not quite as dominant, as
business
> > needs have broadened into such things as XML and such, most business
rules
> > are still being implemented in CoBOL.
> >
> > I'm not sure though that you will find business rules, accounting, and
> > typical business needs to be fun.   So we need a better definition of
your
> > goals before we can give you a meaningful answer.
> >
>





 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

_(reply depth: 4)_

- **From:** Chris Humphries <chumphries@devis.com>
- **Date:** 2002-01-09T23:00:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3C8504.2000108@devis.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com> <3c3b787e_2@Usenet.com>`

```


> Please go to www.aboutlegacycoding.com. Click the "Archive" button and read
> an article that was published in April 2001, called "Meet the Future". This
> article covers most of my arguments as to why you should learn COBOL.


very nice article,
a little M$ centric, but hey :P
at least you talked about xerox lab :)

very handy. i can say i learned things from :)

> 
> I wish you every success in the future and please don't let anyone grind the
> edge off your sense of what is "fun" <G>.

heh, i wont. seems to be working great for me so far. I work at a
consulting firm doing .gov contracts. I am doing pretty well since I am
only 23 and have no college education or certs or anything like that.
Being curious has paid off :) Being the most flexible is the key :)
know M$, unix, databases, and lots of languages.... and people skills
( probably the hardest part :P)


anywho. thanks for the help. it is much appreciated, and look forward to
knowing COBOL and all it has to offer me.

thanks,
chris
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2002-01-09T13:35:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GGX_7.564$q67.253014196@newssvr11.news.prodigy.com>`
- **References:** `<3C3AC316.8080705@devis.com> <krE_7.51743$wa.3506395@bin6.nnrp.aus1.giganews.com> <3C3AD438.5090106@devis.com>`

```
Whether fun or torture, learning a new language improves your skill--that's
good.

"Chris Humphries" <chumphries@devis.com> wrote in message
news:3C3AD438.5090106@devis.com...
> fun as in learning a new language. Not really after any specific
> goals (like building a game or something). I just enjoy learning
…[10 more quoted lines elided]…
>
```

#### ↳ Re: benefits of cobol in the present?

- **From:** Richard Riehle <richard@adaworks.com>
- **Date:** 2002-01-08T09:39:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3B2EE6.1474D0A7@adaworks.com>`
- **References:** `<3C3AC316.8080705@devis.com>`

```
Chris Humphries wrote:

> Hello All,
>      I am starting to learn COBOL, and am just curious what would be the
…[4 more quoted lines elided]…
>   python and c++?

One of the most dreadful things that has happened in the world of software
is the widespread adoption of C++.   Even worse has been the replacement
of COBOL in many shops with C++.

COBOL, in its earlier forms, with high dependance on global data was
certainly difficult to maintain, error-prone,  and needed updating.  It
has, in fact, proven quite resilient to such updating, and the current
versions provide good techniques for support of both low-coupling
and high-cohesion, qualities missing in earlier versions.

COBOL continues to be easy to learn and use for business data processing
applications.    It is much maligned by those who have not kept current
in their knowledge of its progress.

C+ began as a fairly simple set of extensions to C.   It too has evolved.
Unfortunately, the evolution of C++ has produced a large, complex, and
error-prone language that is inaccessible to the typical business data
processing programmer.

C++ is its own virus.

All that being said, my own preference, currently is for Ada 95.  Once again,

those who malign Ada are unaware of the evolution of that language into
a first-rate language for business data processing (including COBOL-like
picture clauses and COBOL-compatible decimal types), as well as for
many other kinds of programming.

It is all too easy for those who are ignorant of the current state of COBOL
or
Ada to criticize, especially when the popularity of another language is
(often
undeservedly) high in the current literature.

Make you decision on the basis of sound criteria, not on the basis of what
seems
popular.   COBOL, in its current version, is still a viable language for
writing
programs targeted to business data processing problems.

Richard Riehle
```

##### ↳ ↳ Re: benefits of cobol in the present?

- **From:** Chris Humphries <chumphries@devis.com>
- **Date:** 2002-01-08T18:07:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3AEED6.6000907@devis.com>`
- **References:** `<3C3AC316.8080705@devis.com> <3C3B2EE6.1474D0A7@adaworks.com>`

```
yeah i'm not backing c++ at all. i personally am not a big fan of
it. i prefer python and C, though know many more.  I will learn it
for my own personal interest, not for career gain or such.was just
curious if there was is a market for it. I assume that it would be
in a slump after the rave of Java and C++.

just curious,
chris



Richard Riehle wrote:

> Chris Humphries wrote:
> 
…[52 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: benefits of cobol in the present?

- **From:** Richard Riehle <richard@adaworks.com>
- **Date:** 2002-01-08T10:43:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3B3DCD.F6FF7F3F@adaworks.com>`
- **References:** `<3C3AC316.8080705@devis.com> <3C3B2EE6.1474D0A7@adaworks.com> <3C3AEED6.6000907@devis.com>`

```
Chris Humphries wrote:

> yeah i'm not backing c++ at all. i personally am not a big fan of
> it. i prefer python and C, though know many more.  I will learn it
> for my own personal interest, not for career gain or such.was just
> curious if there was is a market for it. I assume that it would be
> in a slump after the rave of Java and C++.

Just one caution.  There are some truly awful COBOL books out there.
One of the worst is the  COBOL in 21 Days Book.    A better one, oddly
enough, is the COBOL in 21 Hours book.   Also,  focus, if you can, on
the current ideas related to the object-oriented standard.    There are
some good books by Wison Price and by Ed Arranga as well as others
that deal with contemporary COBOL.   I cannot for the life of me undestand
why people continue to publish out-of-date COBOL books.

I was asked by a publisher several years ago to write a COBOL book for
them.   It turns out they wanted the same tired old COBOL, mainly to meet
the demand of the Y2K hysteria.    I wanted to do a book that would clearly
illustrate the value of modern COBOL.    Publishers and witers don't
always see eye-to-eye.

Richard Riehle
```

#### ↳ Re: benefits of cobol in the present?

- **From:** "Rational One" <noreligion@nogod.com>
- **Date:** 2002-01-08T20:01:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4eI_7.7214$DG5.74200@rwcrnsc53.ops.asp.att.net>`
- **References:** `<3C3AC316.8080705@devis.com>`

```

"Chris Humphries" <chumphries@devis.com> wrote in message
news:3C3AC316.8080705@devis.com...
> Hello All,
>      I am starting to learn COBOL, and am just curious what would be the
…[11 more quoted lines elided]…
>
```

#### ↳ Re: benefits of cobol in the present?

- **From:** "T. Scott Ankrum" <ankrums@mitre.org>
- **Date:** 2002-01-09T09:14:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3C5039.7F3289BE@mitre.org>`
- **References:** `<3C3AC316.8080705@devis.com>`

```
For many arguments on why COBOL is still a valuable language, see my article
COBOL: A Best Practice at www.cobolreport.com.



Chris Humphries wrote:

> Hello All,
>      I am starting to learn COBOL, and am just curious what would be the
…[9 more quoted lines elided]…
>   systems analyst
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
