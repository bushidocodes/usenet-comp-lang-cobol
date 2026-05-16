[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Recommendation for refreshing and updating skills

_11 messages · 7 participants · 2009-02_

---

### Recommendation for refreshing and updating skills

- **From:** scott97007@gmail.com
- **Date:** 2009-02-17T15:08:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>`

```
Hi, all!

It's been a while since I posted on c.l.c.  I left the mainframe world
at the end of 2003.  Recently I was laid off from a place where I was
testing PC software. Now I'm looking for employment in mainframes
again.  I'm focusing my job search on employment for the State of
Oregon since they are one of the few places left in my state that
still uses a lot of basic mainframe skills.

My first interview for a state position was a bust.  It was a
technical interview and my skills were out of date.  I blew some
simple DB2 and CICS questions.  It's been a few years since I used
these skills and the times when I did use use them I didn't use them
much.  So I'm refreshing my skills and trying to improve them to where
I can pass the State's technical interviews.

Do you have suggestions for a training environment that can be
installed on Windows XP?

I currently have DB2 Express-C installed and the free version of
MicroFocus COBOL.  I'm not sure what to do for CICS.

Also, any pointers for State technical interviews would be
appreciated.

-  Scott Ball
```

#### ↳ Re: Recommendation for refreshing and updating skills

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-18T14:49:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnh75k$ied$1@reader1.panix.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>`

```
In article <15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>,
 <scott97007@gmail.com> wrote:

[snip]

>My first interview for a state position was a bust.  It was a
>technical interview and my skills were out of date.  I blew some
…[3 more quoted lines elided]…
>I can pass the State's technical interviews.

Leaving aside the thorny ethical problems of 'do you want to learn the 
materials so you can pass the test or do you want to learn the test so 
that you can get the job and realise the test had next-to-nothing to do 
with the Actual Work Being Done?'...

... spend a bit of time on Google, using search terms like 'DB2 tech 
interview questions' (no ') and 'CICS tech interview questions'.  It might 
prove fruitful.

For an anecdote let me point you to 
<http://groups.google.com/group/comp.lang.cobol/msg/3b3fd01de89eb71d?hl=en&dmode=source>

--begin quoted text:

(I was once asked Interview Question Number 17 (DB2 sheet) of 'What do you 
do to get a COBOL source-code file which contains SQL statements to run?'; 
my answer was 'Well, what *I* do is go into my library, grab the right 
compile skeleton, do a global replace on the member-name and SUB the 
result... but you're probably looking for the Textbook Answer of 
'Precompile, Compile, Link and Bind', right?'

I got the contract... but imagine what would have happened if the 
interviewer was not familiar with the steps of 'go into my library, grab 
the right compile skeleton, do a global replace on the member-name and SUB 
the result'.)

--end quoted text

DD
```

##### ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** Scott Lindstrom <sclind@gmail.com>
- **Date:** 2009-02-18T14:42:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71e236c5-fecf-45bf-88be-498174319870@e1g2000pra.googlegroups.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <gnh75k$ied$1@reader1.panix.com>`

```
> (I was once asked Interview Question Number 17 (DB2 sheet) of 'What do you
> do to get a COBOL source-code file which contains SQL statements to run?';
…[3 more quoted lines elided]…
> 'Precompile, Compile, Link and Bind', right?'

I think it would be great to find an interviewer who was looking for
'real world' answers like that.

I think if someone told me one of their first steps in coding a
program was to find one that did something similar and start from
there I would be impressed that they were willing to say so.
Reinventing the wheel (introducing new bugs) is a waste of time.
```

###### ↳ ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-19T01:23:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnicam$9lk$1@reader1.panix.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <gnh75k$ied$1@reader1.panix.com> <71e236c5-fecf-45bf-88be-498174319870@e1g2000pra.googlegroups.com>`

```
In article <71e236c5-fecf-45bf-88be-498174319870@e1g2000pra.googlegroups.com>,
Scott Lindstrom  <sclind@gmail.com> wrote:

[snip]

>I think if someone told me one of their first steps in coding a
>program was to find one that did something similar and start from
>there I would be impressed that they were willing to say so.

Started doing that a longer time ago, before there was such a thing as 
DB2... the one I recall is 'What steps would you take in defining a KSDS?' 
and my response was along the lines of 'I'd ask to look into the lead 
programmer's library so that my version would look Just Like Everyone 
Else's... and if he refused I'd ask someone else... and if they all 
refused I'd check the system sample libraries... and if someone had RACF'd 
me out of all of those I'd grab my copy of Trombetta & Finklestein so that 
if what I did was wrong at least I'd be wrong according to the textbook...

... and if my copy of Trombetta & Finklestein wasn't around I'd quit the 
contract because I wouldn't work with thieves who'd steal my books... but 
you probably want to talk about boring things like what's important to 
include in the DELETE/DEFINE/REPRO steps, right?'

(That job I did *not* get... or rather, I did not take; turned out that 
while I was looking to be an independent they were looking for someone to 
be part of their stable, 'We'll keep paying you even if you're on the 
beach between contracts'... and the fellow blanched when I mentioned 
escrow accounts.)

>Reinventing the wheel (introducing new bugs) is a waste of time.

But... but it's *my* wheel, at least... and if you really look closely 
you'll see I started with a triangle and then began to round the sides out 
so while it mostly works like a wheel it sometimes exhibits polygonal 
behavior... and that's good, except for the times when it happens at 2:am 
and they gotta call the New Kid to fix it... but everyone has to live 
through that, right, and besides... it's *my* wheel, not anyone else's!

DD
```

#### ↳ Re: Recommendation for refreshing and updating skills

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-18T16:14:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DL%ml.54002$tg5.44682@en-nntp-05.dc1.easynews.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>`

```
I don't have a great answer for this, but I was thinking that if you look at the 
"Migration Guides" (and at least see what TOPICS they discuss), this might get 
you started.  Each product has its own.  Consider starting with:

COBOL
  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGY3MG40/CCONTENTS

LE
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA6190/CCONTENTS

CICS
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/DFHEEC00/CCONTENTS

ISPF
  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/ISPZUG70/FRONT_2.1

DB2
 http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/dsnapk13/1.1

IMS
 http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/DFSRPGF8/CCONTENTS

   * * * * * * * *

I am NOT suggesting that you read all of these, but looking at them MIGHT help 
(or look at the ones that most impact you).  What I have provided are links to 
the BookManager versions.  Most of them have PDF versions that you can 
download - if that is easier for you.  Obviously, there are also changes in 
other things (like JCL, RACF, DFSort, etc)
```

#### ↳ Re: Recommendation for refreshing and updating skills

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2009-02-18T15:27:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0a4a4ac-a08d-40c4-9044-4f71fff407f7@i38g2000yqd.googlegroups.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>`

```
On 17 Feb, 23:08, scott97...@gmail.com wrote:
> Hi, all!
>
…[23 more quoted lines elided]…
> -  Scott Ball

Mike Murach's books have seemed quite reasonable and economical,
though I haven't checked them recently.

Another option in the reading line is to download the language
reference manuals and programming guides for as many recent releases
of COBOL, CICS and DB2 as you can free from IBM.  Somewhere in the
front of each will be a list of recent enhancements and the guides
usually provide some examples.

Another option is to follow questions and answers on comp.lang.cobol,
comp.databases.ibm-db2 and subscribe to the email only list of cics-
l@listserve.uga.edu which you can join by

sending an email to LISTSERV@LISTSERV.UGA.EDU
<mailto:LISTSERV@LISTSERV.UGA.EDU>  and, in  the text of your message
(not
        the subject line), write: SUBSCRIBE CICS-L

I am afraid I don't know of any easily affordable CICS emulators.

Robert
```

#### ↳ Re: Recommendation for refreshing and updating skills

- **From:** scott97007@gmail.com
- **Date:** 2009-02-19T10:31:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com>`

```
Thanks for the feedback.

I have MicroFocus, so think I can get a lot of DB2 + COBOL practice
with that.  The problem is getting practice with CICS.

I wasn't able to find any inexpensive CICS emulators.  Do you think it
would it be too difficult to write one?  At least one with enough
functionality to practice basic transaction concepts?  It wouldn't
hurt too much if I went into an interview and mention that I practiced
CICS on an emulator I wrote myself.  A preprocessor for "EXEC CICS"
would not be to hard to write.  I think I could use a web server with
PHP in place of SNA to handle the maps in and out. There a few hundred
CICS API commands.  I don't need to implement all of those.

I guess to partially answer my own question is that it depends on how
much of CICS I want to emulate.

What parts of CICS would be most useful to emulate?
```

##### ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-19T15:18:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N0knl.271538$NN4.30353@en-nntp-08.dc1.easynews.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com>`

```
*NO* you do not want to try to write your own CICS emulator.  However, there is 
a new "product" that might be exactly what you are looking for.  Check out:

 http://www.zcobol.org/

It does include CICS support.
```

##### ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-02-20T13:52:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnn0fo020tn@news3.newsguy.com>`
- **In-Reply-To:** `<1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com>`

```
scott97007@gmail.com wrote:
> 
> I wasn't able to find any inexpensive CICS emulators.  Do you think it
> would it be too difficult to write one?

"Too difficult" is a subjective evaluation. Would it be difficult?
Yes, quite.

>  At least one with enough
> functionality to practice basic transaction concepts?

A small team of very good developers, some of whom have written CICS
emulators in the past, can implement a minimal set of CICS
functionality in a few months.

Of course, anyone could read the CICS docs and create something that
acts as they think CICS should act, for some fraction of CICS
applications. Once the basic API infrastructure (macro processing,
CICS calling conventions, etc) is in place - not trivial, but doable -
you could stub out as many CICS macros and system calls as you like,
and have them return the "correct" value for inputs of your choosing.

Without a real CICS system to compare it to, though, how would you
know whether your mock-up was behaving like the real thing?

>  It wouldn't
> hurt too much if I went into an interview and mention that I practiced
> CICS on an emulator I wrote myself.  A preprocessor for "EXEC CICS"
> would not be to hard to write.

True, though it's more complicated than it looks at first blush. And
there's a lot that's not conceptually hard, but tiresome - predefined
constants and that sort of thing.

>  I think I could use a web server with
> PHP in place of SNA to handle the maps in and out.\

For simple pseudoconversational traffic, yes. For more complex
operations, the semantics of HTTP are wrong. That's why web-based
front-ending products for CICS (EnterpriseLink, OnWeb, etc) are
themselves pretty complex.

> I guess to partially answer my own question is that it depends on how
> much of CICS I want to emulate.

Definitely, though the preprocessor and the other elements of the API
interface (CICS constants, etc) aren't as amenable to partitioning -
you pretty much need most of that, or you don't have anything usable.

> What parts of CICS would be most useful to emulate?

Well, that's the rub. It depends on the parts of CICS that your
prospective employers 1) use and 2) would like you to know on the
first day. Do they use channels and containers? Do they use CICS Web
Services? Do they use EZASOKET? Do they use TS/TD? Do they use SPI
(the Systems Programming Interface)?

Those are all features that are outside the CICS "core", so to speak -
a lot of classic CICS apps would never use any of them - but I see
customers using them extensively in the CICS applications that they're
trying to maintain and modernize. Where there are CICS jobs, they
often seem to emphasize newer or more esoteric CICS features;
precisely because if you're going to maintain CICS apps, you might as
well bring them up to date.

That said, I don't want to discourage you from trying to write your
own emulator. It's an interesting project (interesting to me, anyway).
```

##### ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** scott97007@gmail.com
- **Date:** 2009-02-20T14:51:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1d1e3f2a-ac83-4341-9bc7-357eac814ac8@w34g2000yqm.googlegroups.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com>`

```
Thanks for the feedback guys.  I'd love to write an open source CICS
emulator.  Unfortunatly, time is finite and I need to focus on
improving my career right now.

To practice JCL, I’ll set up Hercules with MVS. I just have to figure
out how to configure Hercules, and then how to install and configure
MVS on it. This system should have VSAM available on it, so I can play
with that a bit.

For a COBOL, I believe that an older compiler is available on Hercules
or MVS. For my purposes it won’t work for DB2 and CICS work.  To get
started, I'll use MicroFocus' free edition. zCOBOL will be coming out
in early March, and it may be closer to a true mainframe compiler, so
I may be using this more after it's out.

For DB2, I’ll use IBM’s free version. MicroFocus works with DB2. I’m
not sure about zCOBOL, but unless they add "EXEC SQL" support to z390,
I don’t believe it will. "EXEC SQL" is still on the to-do list for
z390, and until it’s in z390, I doubt it will go into zCOBOL.

For CICS, there is a CICS transaction server for z390. The instruction
set is limited, but it should have enough functionality to do basic
CICS style programming. The zCOBOL compiler will work with this psuedo-
CICS environment.  I don't know if MicroFocus will.

Just getting all of this set up an running on a PC should make me
stand out in an interview.

Don Higgins and the guys who support the z390 project deserve a gold
medal or something for all the great work they’ve done. Same goes for
the Hercules folks.  And you too Bill.

Shees! How many people really thought we’d be running mainframes on
our desktop PCs for free in the year 2009?
```

###### ↳ ↳ ↳ Re: Recommendation for refreshing and updating skills

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-02-20T20:16:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wpednWKfP_hTyALUnZ2dnUVZ_gmWnZ2d@earthlink.com>`
- **References:** `<15555e7f-f5d3-4b4e-9622-f05b0b073bbb@r41g2000prr.googlegroups.com> <1c2bd04b-76f8-421c-898e-79ff56c9c75b@40g2000prx.googlegroups.com> <1d1e3f2a-ac83-4341-9bc7-357eac814ac8@w34g2000yqm.googlegroups.com>`

```
<snip>

I have been a successful COBOL/CICS programmer for many years.  I learned 
all I needed to get started books from Mike Murach.  His CICS books should 
still be relevant.  His DB2 books are kind of old and somewaht dated but I 
believe you can get the basics of embedded SQL from them.  Fot JCL I would 
recommend author Gary DeWard Brown.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
