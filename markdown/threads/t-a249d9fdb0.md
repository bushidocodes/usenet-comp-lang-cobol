[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SAS sucks

_25 messages · 15 participants · 2000-02 → 2000-03_

---

### SAS sucks

- **From:** jacob elgart <j_elgart@hotmail.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B2111E.3BA05B58@hotmail.com>`

```
I was interviewing for a p/a position in a major bank. The ad had
"...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
(I have about 7 years of practical experience) but then I was asked
about SAS and since I don't know it I said I didn't. The manager
informed me that they were looking for a p/a in a "list management" team
working for marketing in a "very dynamic" environment and SAS was
critical. In other words, I didn't get the position. It seemed pretty
moronic as the way he described their work it looked to me like just
writing programs, and he even went on to say that he personally couldn't
care less what language a p/a uses as long as the "list pull" (??) is
ready on-time.

So, what is so special about the "list management"? And what is the big
fuzz about SAS that they need it so badly that COBOL alone is not
enough? And what is SAS anyways?
```

#### ↳ Re: SAS sucks

- **From:** "keldin" <keldin@mciworld.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICws4.16779$NP6.345697@pm02news>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```

Statistics Anaylsis http://www.sas.com/
SAS has its benifits, you can quickly get reports using it, with little
concern about layout issues.  In our bank, Business Anaylsts in NY use it to
verify that code implemented in COBOL actually does what it was meant to do.
I personally like it to do Proc Freqs to quickly get the ranges of values in
a field, it can do it in about 20 lines of code with SAS. Anyone that knows
COBOL should be able to pick it up (the basics) in like 1 day.  It would be
worth it to take a 2 to 3 day beginner course form the SAS Institute, most
Fortune 500 companies use it to some degree.

"jacob elgart" <j_elgart@hotmail.com> wrote in message
news:38B2111E.3BA05B58@hotmail.com...
> I was interviewing for a p/a position in a major bank. The ad had
> "...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
…[13 more quoted lines elided]…
>
```

#### ↳ Re: SAS sucks

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B29ABE.A47681C2@iinet.net.au>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
jacob elgart wrote:
> 
> So, what is so special about the "list management"? And what is the big
> fuzz about SAS that they need it so badly that COBOL alone is not
> enough? And what is SAS anyways?

SAS, which stands for Statistical Analysis System from memory, is an
extremely powerful data manipulation and reporting language.

A given SAS program is broken up into discrete steps. Each of these
steps can be a nominal DATA manipulation step or a PROCedure step.

The Data unit in SAS is a table of data referred to as a SAS file. SAS
files are passed between DATA steps and PROCedure steps.

The secret to SAS is to create a table of data that has columns and rows
such that you can invoke one of the MANY PROCedure steps to produce your
desired output.

The DATA step is what would traditionally be regarded as the PROGRAM.
There are some unique features of SAS that can trap the unwary. First
of, the DATA step is usually passed a file to process (note: not a
record or a parameter, but the WHOLE FILE).
Because of this each statement in the DATA step is processed for each
record retrieved from the file. Record retrieval is automatic and does
not need to be programmed.

Here's a sample:

DATA in1;
 INPUT fname lname;
 CARDS;
Joe Blogs
Harry Smith
Mary Short
RUN;

TITLE 'A small title for a basic report';
PROC PRINT DATA=in1 SPLIT='*';
 VAR fname lname;
 LABEL
  fname = 'First*Name'
  lname = 'Last*Name';
RUN;

The above program reads in via the DATA step the data after the CARDS;
statement and creates a table with variables fname and lname. There will
be 3 rows, the DATA step ends automatically upon encountering thr RUN;
statement. Please note the INPUT statement is executed once per CARD
read, i.e. 3 times.

Then the PROC step will print the data in table in1, created by the DATA
step.
The PRINT procedure is instructed to print only the variables fname and
lname.
The fname and lname columns are labeled with the '*' meaning split the
label into two lines at the '*'.

There are numerous statistical PROCedures that make it one of the most
powerful data analysis tools in existence.

Hope this helps!
```

#### ↳ Re: SAS sucks

- **From:** jeffreyfarkas@earthlink.net (Jeff Farkas)
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.131c8b3c61a7e942989690@news.earthlink.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
In article jacob elgart says...
> I was interviewing for a p/a position in a major bank. The ad had
> "...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
…[14 more quoted lines elided]…
> 
Sorry to hear that they held that against you. It is not a hard language
to learn and with your experience you could pick it up in a few days. 
Even if it took two weeks that would be no big deal! 

 All of the other posts are correct with their description of SAS. It is 
a very good language for generating ad-hoc reports and general reports. I 
have used it a lot for that and other functions. And it has saved me lots 
of time and pain when I need to generate a report at the last moment. So, 
SAS does not suck. 
 
 From what you said it sounds that they either generate reports on the 
fly or they generate files that get sent out of the company. SAS is great 
for this and that is why it was "critical". 

 My suggestion is to check out the SAS web site.. www.sas.com and they 
have some good books to learn how to use it. The best that I have found 
is "Professional SAS Programming Secrets" by Rick Aster and 
Rhena Seidman.
It covers the basics and advanced topics. If you want to pick it up and 
use it that is the book I would go with! 

Hope that gives you more information.. if you have any other questions 
feel free to email me.

Jeff..
```

##### ↳ ↳ Re: SAS sucks

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-ElkDCgS3CT9w@localhost>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <MPG.131c8b3c61a7e942989690@news.earthlink.net>`

```
"All of the other posts are correct with their description of SAS. It is 
a very good language for generating ad-hoc reports and general reports."

Shucks, I even wrote an entire Dungeons & Dragons player management system in it, not to mention doing the math' for several Aggie kinethesiologists to get their Masters with!
Easy to learn, literally only days to get comfortable, but containing a wealth of *very* powerful subroutines.  Also very common in COBOL shops as a replacement for Report Writer.

Sorry to hear you got cut off without the opportunity to show you could learn SAS.

=Dwight=
X1=L, X2=L & the domain is phonetic
```

###### ↳ ↳ ↳ Odd things to do with a language

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B2E58C.B02767E6@cusys.edu>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <MPG.131c8b3c61a7e942989690@news.earthlink.net> <1tGZ16mMk7i4-pn2-ElkDCgS3CT9w@localhost>`

```


mixxerdw@eye_eye_echs.com wrote:

> "All of the other posts are correct with their description of SAS. It is
> a very good language for generating ad-hoc reports and general reports."
>
> Shucks, I even wrote an entire Dungeons & Dragons player management system in it, not to mention doing the math' for several Aggie kinethesiologists to get their Masters with!

I one time had time to kill while monitoring jobs on a VAX.  I used DCL to write a program which did multiplication and division by shifting bits in supplied numbers instead of using
the supplied multiplication and division commands.  I wanted to see how difficult that would be and DCL was available.
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** jeffreyfarkas@earthlink.net (Jeff Farkas)
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.131d02cc205980ee989694@news.earthlink.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <MPG.131c8b3c61a7e942989690@news.earthlink.net> <1tGZ16mMk7i4-pn2-ElkDCgS3CT9w@localhost>`

```
In article mixxerdw@eye_eye_echs.com says...
> "All of the other posts are correct with their description of SAS. It is 
> a very good language for generating ad-hoc reports and general reports."
…[8 more quoted lines elided]…
> 
Well, they did not let me get that far into it.. but it still saved me on 
a number of times!! The place I used it was only using base SAS.. so... I 
could not do as much as I wanted to.. such is life!!

Jeff...
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** xlr82sas@aol.com (Xlr82sas)
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000223135159.16401.00000443@ng-dc1.aol.com>`
- **References:** `<1tGZ16mMk7i4-pn2-ElkDCgS3CT9w@localhost>`

```
Keep in mind that SAS has one of the best C++ cross compilers. You could write
dungeons and dragons in SAS and then run it under MVS on the mainframe.
Roger J DeAngelis
CompuCraft Inc
XLR82SAS@aol.com ( Accelerate to SAS )
http://members.aol.com/xlr82sas/utl.html
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-HpmYYb74soU2@localhost>`
- **References:** `<1tGZ16mMk7i4-pn2-ElkDCgS3CT9w@localhost> <20000223135159.16401.00000443@ng-dc1.aol.com>`

```
It seems  xlr82sas@aol.com (Xlr82sas) keyed the following on Wed, 23 Feb 2000 18:51:59:

> You could write
> dungeons and dragons in SAS and then run it under MVS on the mainframe.
> 
That's where I ran it in SAS!  (Now, the price of OS/2 SAS being beyond my taste, I moved it to a combo of Mesa/2 and REXX.)
=Dwight=
X1=L, X2=L & the domain is phonetic
```

#### ↳ Re: SAS sucks

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88ugj9$pe6$1@nntp8.atl.mindspring.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
Jacob,

        In my opinion, you were better off NOT getting the position. SAS is
a wimpy language for non-techie types (basically for the DP101 crowd), used
in creating Ad-Hoc reports, specialized "One-Time" programs and what-not.
The fact that you didn't get the position tells me that the MAJORITY of your
time would have been spent in SAS coding, which would have been a definite
step backwards for you.

        Count your blessings and move forward.

Cheers,

WOB

jacob elgart <j_elgart@hotmail.com> wrote in message
news:38B2111E.3BA05B58@hotmail.com...
> I was interviewing for a p/a position in a major bank. The ad had
> "...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: SAS sucks

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B2CDF5.EBAE99C1@cusys.edu>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```


WOB wrote:

> Jacob,
>
…[5 more quoted lines elided]…
> step backwards for you.

I had to write some SAS programs in a shop which had lost all of their SAS
manuals.  Inferring from other code how to write SAS was not the easiest thing
in the world.  I suppose it would have been harder to learn RPG that way, but
just barely.
```

##### ↳ ↳ Re: SAS sucks

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-fFml2wGhBird@localhost>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```
" SAS is
a wimpy language for non-techie types (basically for the DP101 crowd), used
in creating Ad-Hoc reports,"

Bull!

=Dwight=
X1=L, X2=L & the domain is phonetic
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** mel5133928@aol.com (MEl5133928)
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000222150435.18151.00001019@ng-cc1.aol.com>`
- **References:** `<1tGZ16mMk7i4-pn2-fFml2wGhBird@localhost>`

```
Ditto! A little SAS knowledge can make you much more productive. How it can be
called wimpy is beyond me! Maybe you just aren't prepared to learn something
new?
```

##### ↳ ↳ Re: SAS sucks

- **From:** jeffreyfarkas@earthlink.net (Jeff Farkas)
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.131cbac399c651cf989692@news.earthlink.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```
In article WOB says...
> Jacob,
> 
…[11 more quoted lines elided]…
> WOB

    I would agree with you, that if that was the majority of his tasks 
then I would agree that it would be a step backwards. But, SAS is far 
from a DP101 language. It can be simple for simple reports.. and as 
complex as you want it to be. I have used it and found it to help solve a 
lot of odd problems that would have been very hard in COBOL.

Just my 2 cents..

Jeff..
```

##### ↳ ↳ Re: SAS sucks

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88uu70$ia0$1@nnrp1.deja.com>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```
In article <88ugj9$pe6$1@nntp8.atl.mindspring.net>,
  "WOB" <wobconsult@sprynet.com> wrote:

<Snipped>

It seems I've gotten several of you a little upset. That was not my
intention.

What got me about Jacob's plight was the fact that here's someone with
7 years experience in COBOL and DB2. It seemed that the Interviewing
Manager was only looking for someone to be the SAS "Boy". SAS indeed
has its place, but to take an experienced person, who may or may not be
desperately looking for work and try to sucker him/her into a position
that (IMHO) is a step backwards, rivals that of some pimp at your local
DP Headhunting Group looking for a "Body".

The order of qualifications (as Jacob listed them) placed SAS "Last" in
line. Possibly a lesson learned for the lad.

As someone indicated, SAS can be mastered in a short period of time.
However, COBOL T/W DB2 is an acquired study, not easily mastered by
many, regardless of the time-period. Exploiting one's skills to place
them in a back-room position is something that should not be tolerated.

Hence, my opinion.

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: SAS sucks

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B3008D.E7958F41@istar.ca>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```
Don't tell that to the IBM Mainframe community.  I was in the minority
of systems programmers that didn't use SAS to manipulate the systems
usage data.  This is not a trivial task and I have great respect many of
those who I know use it and whose technical knowledge is far greater
than mine.  SAS and add-on packages to it are extremely powerful tools.

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca   

WOB wrote:
> 
> Jacob,
…[31 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B30B5C.62F3AAA3@cusys.edu>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net> <38B3008D.E7958F41@istar.ca>`

```
It seems that SAS can do things that COBOL can't, possibly because it goes around
some "sandbox" type safeguards.  Not to mention statistical reporting is easier.
Is this still the case, or do pointers and new functions bring them closer
together?
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88v4fh$jif$1@nntp9.atl.mindspring.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net> <38B3008D.E7958F41@istar.ca> <38B30B5C.62F3AAA3@cusys.edu>`

```
Actually, some of the character-string manipulation facilities of SAS are
*more* powerful than those in COBOL (said the COBOL- bigot) - similar in
"power" to that in REXX.  Most of these can be done in COBOL (with a LOT of
work) but have easy "simple to understand/maintain" statements in SAS.
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 5)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BE014E.383789AF@mediaone.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net> <38B3008D.E7958F41@istar.ca> <38B30B5C.62F3AAA3@cusys.edu> <88v4fh$jif$1@nntp9.atl.mindspring.net>`

```
Bill,

True, but guess what? Recently in SAS group, some folks were bitching about
SAS's _lack_ of all string-handling capabilities compared to those available in
Perl. Really, there is no such thing as too sweet a candy...

Kind regards,
==========================
Paul M. Dorfman
Jacksonville, FL
==========================

"William M. Klein" wrote:

> Actually, some of the character-string manipulation facilities of SAS are
> *more* powerful than those in COBOL (said the COBOL- bigot) - similar in
…[14 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B38217.E0D0BD19@mediaone.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net> <38B3008D.E7958F41@istar.ca> <38B30B5C.62F3AAA3@cusys.edu>`

```
Howard Brazee wrote:

> It seems that SAS can do things that COBOL can't, possibly because it goes around
> some "sandbox" type safeguards.  Not to mention statistical reporting is easier.
> Is this still the case, or do pointers and new functions bring them closer
> together?

Pointers in SAS are rudimentary, and I have not seen them used even as often as in
COBOL. Although pointer usage in COBOL is cumbersome, COBOL holds the edge here. As
far as the functions go, COBOL has kind of started catching up. However, there is
still some way to go since SAS has over 250 of those. Not to mention SAS procedures
including a complete SQL implementation...I do not think COBOL has anything similar.
And I am talking only about Base SAS, of course.

Kind regards,
==========================
Paul M. Dorfman
Jacksonville, FL
==========================
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B3C424.5F4B85D@zip.com.au>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net> <38B3008D.E7958F41@istar.ca> <38B30B5C.62F3AAA3@cusys.edu>`

```
Howard Brazee wrote:
> 
> It seems that SAS can do things that COBOL can't, possibly because it
…[3 more quoted lines elided]…
> closer together?

SAS MXG is very powerful and incredibly hungry on machine time.  I did
it in Cobol, just run an SMFDUMP and take this program (not on pages
go direct).

http://www.zipworld.com.au/~waratah/scssmf1.cob

It takes far less resources and once you customize it to your needs
away you go...

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: SAS sucks

- **From:** William Reed <adamreed@bellsouth.net>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B3415B.132B9B1C@bellsouth.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com> <88ugj9$pe6$1@nntp8.atl.mindspring.net>`

```
I had a SAS "programmer" (who was an accounting type, and NOT a programmer) who
was constantly bugging me to provide him with data extracts for his SAS
"programs".

He claimed several times that the data I sent him was "bad".  I checked my data,
and there was nothing wrong with my data, just his programs.  On one such
occasion, my "bad data" turned out to be a missing semi-colon in his SAS
"program".


WOB wrote:

> Jacob,
>
…[12 more quoted lines elided]…
>
```

#### ↳ Re: SAS sucks

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B37E0D.1258C7D7@mediaone.net>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
jacob elgart wrote:

> I was interviewing for a p/a position in a major bank. The ad had
> "...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
…[8 more quoted lines elided]…
> ready on-time.

First of all, the choice of the name you have picked for the thread appears
quite poor to me. It is in part pandering, in part inflammatory. I can
understand your frustration, yet it is kind of silly to make a piece of
software guilty just because you do not know it.

> So, what is so special about the "list management"?

I have worked in list management, so I can tell you. Usually it is a team of
programmers preparing files (lists) listing existing (portfolio) or
potential (acquisition) customers targeted in a specific marketing campaign
or promotional offer. Where I worked, the criteria were given by Marketing
out to the team on the 7th of each month, and the promotions would be
distributed among the members of the team. About 70 percent of all
promotions are inserts, bill head messages, and alike, so they HAD to be
ready at least 2 days before Billing ran its merge, i.e. on the 19th. The
rest - telemarketing and solo mailings which were due before the 28th.
Depending on the month and staffing, an LM programmer would get 10 to 15
promotions a month to handle. For each promotion, s/he had first to locate
the data specified in the criteria. Usually, it was a collection of about 10
customer catalog tables, 3-year static, term balance and transaction
history, credit bureau, response tracking tables, and a wild collection of
other data (flat and VSAM files, backup tapes, snapshots from online
facility, Excel and other PC junk, SAS datasets from modelling...) needed to
segment the population, create control groups, exclude prior solicitations,
etc. Having located the sources, you would write a program to extract,
match, compute, unmatch... and run it against a 5% subset of the entire
customer universe (so-called 'galaxy' prepared in COBOL production), produce
a couple of dozen of reports showing, in effect, how the marketing criteria
affected the output numbers and their distributions. If it was OK with the
marketing manager, the program would be run against the entire population,
control and targeting groups separated by assigning promo tracking codes to
corresponding accounts randomly, and special files for bill merge written.
If not, the manager would change the criteria, and you would run against the
galaxy again, produce any reports the marketing guy would desire, all until
either it was eventually OK to run against the universe or established that
the promotion had to be cancelled because it would lack population or
profitability. Then - on to the next promotion. As you can see from this
*very brief* description, the schedule was pretty tight. In reality, an LM
programmer living in a constant ad-hoc state had 2 days max to finish a
promotion. The knowledge of COBOL was critical because all the legacy code
was written in it; most of the copybooks and DCLGENs were kept in COBOL as
well.

> And what is the big
> fuzz about SAS that they need it so badly that COBOL alone is not
> enough?

A building can be built from a variety of preassembled panels, bricks and
cement. Or it can be built using bricks and cement only. Which way is it
built faster and less error-prone? Because SAS uses the panel approach to
build a program, it usually gets written, like it or not,  at least 5 times
faster than COBOL by a programmer equally proficient in both, and requires 5
to 1000 less lines of code depending on the task. In a typical *fast-paced*
list management the business goal is to produce lists before the brick-wall
deadline, else nobody needs them. That is why in list management, SAS is
critical. In the concrete environment described above, the time factor (not
the software quality or personal preferences) had made a mere thought of
using COBOL for "list production" programming ludicrous.

> And what is SAS anyways?

Originally called "Statistical Analysis System", SAS System for Information
Delivery (as it is called now) is an integrated set of data management tools
from SAS Institute, Cary, NC. It runs on a variety of platforms from PCs to
S/390 Enterprise Servers. Its core called Base SAS software consists of a
complete programming language, a macro language, and a number of prewritten
modules called procedures. Base procedures exist for reporting, data
management and file maintenance. One of them, for a small change, represents
the entire ANSI SQL enhanced by all SAS functions (about 250), formats and
informats existing in SAS. A great many of other procedures are included in
additional SAS products licensed separately. They embrace modules for
statistical analysis, spreadsheets, CBT, presentation graphics, project
management, operations research, scheduling, linear programming, statistical
quality control, econometric, time series analysis, to name a few.

Do yourself a favor and learn SAS. Having it under the belt on the market
now is is about the same as offering a large box of Snap-On tools and ample
skill of using them to a manager of an auto repair shop.

Kind regars,
======================
Paul M. Dorfman
Jacksonville, Fl
======================
```

#### ↳ Re: SAS sucks

- **From:** "Tim Hillock" <timhillock@home.com>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ro0t4.73819$45.4063289@news2.rdc1.on.home.com>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
I've used Sas for about 1 year.  I prefer Culprit.  It's a CA product that
can read flat and IDMS files.
```

#### ↳ Re: SAS sucks

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1325fb2dc54af67989914@news.mersinet.co.uk>`
- **References:** `<38B2111E.3BA05B58@hotmail.com>`

```
I noticed that jacob elgart as j_elgart@hotmail.com said...
> I was interviewing for a p/a position in a major bank. The ad had
> "...COBOL, DB2, SAS" (in this sequence). COBOL/DB2 part went just fine
…[8 more quoted lines elided]…
> ready on-time.

I'm surprised that SAS wasn't listed as an essential skill.  Is this 
common in your neck of the woods?  Over here, we tend to see work 
advertised with two skills lists - essential and desirable.  So you might 
see "COBOL CICS DB2 TELON" in the essential list and "JCL  Easytrieve" in 
the desirable list.  Sounds like a cock-up (snafu) to me and a waste of 
your time at which you are justifiably upset enough to use a thread title 
that some might say is inflammatory.

SAS is, or can be, a major stats analysis and reporting package with 
loads of add-ons these days.  I've used it in a fairly basic way but 
wouldn't dream of going for work where it hits the essential list.  Over 
here in the UK, you can command a premium on your rate for SAS.

Given the choice between SAS, Easytrieve and Selcopy (the three main 
quick reporting tools in my armoury), I'd choose Selcopy over Easytrieve 
over SAS any day.  But then that also indicates my degree of comfort, 
born from usage, with these products.  In its environment, SAS is rather 
good but for most quick and easy stuff, I think Selcopy is far better - 
also the Selcopy manual is in a one-and-a-half inch powder blue binder 
while the SAS manuals fill at least one shelf of boring-coloured three 
inch ones.

I would avoid like the plague anything to do with marketing departments.  
They are controlled by the Department Of Terribly Bright Ideas which, as 
eny fule nose, cannot be found anywhere and yet impacts all sorts of 
areas.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
