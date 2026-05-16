[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting ISAM files to RDB

_9 messages · 3 participants · 2001-05_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`VSAM, files, sorting`](../topics.md#files)

---

### Converting ISAM files to RDB

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-05-27T01:00:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b0fabd6_6@Usenet.com>`

```
A number of people are successfully using DECLGEN to convert ACCESS table
definitions into COBOL Host Variable definitions and record layouts, so
their Relational Databases (not just ACCESS) can be easily accessed from
COBOL, using ODBC.

However, a requirement has been expressed to do the OPPOSITE! That is to
take COBOL file definitions and automatically generate RDB tables from them.
(NEGLCED <G>?).  This would be the first step towards converting an
Application system based on the COBOL File system (primarily using Indexed
Datasets, but not necessarily only IDs) to a system using Relational
Database.

(Initially, MS ACCESS, but not limited to this in the long run.)

There is quite a bit of work involved in doing this as the COBOL FD and
corresponding 01 level(s) must be parsed for sublevel numbers, REDEFINES,
OCCURS, KEY field definitions, and PICTURE Clauses, and this data must then
be used to generate correct corresponding SQL CREATE definitions (or,
possibly, DAO definitions for MS ACCESS). At the same time, ideally, the
Database can be automatically Normalized to 2NF by removal of Repeating
Groups (OCCURS clauses) to appropriate tables with Foreign Keys. The final
normalization to 3NF (removal of key dependencies) would probably need to be
done manually. It still means that a large portion of the conversion can be
automated, and a Database in at least 2nd Normal Form can be automatically
obtained.

Now, I already have a fair proportion of the code required to do this (yes,
some of it is Components...<G>), but before embarking on the exercise I
wondered if any people here would be interested in such software. I will
make it available for free (at least the Beta version) as I did with
DECLGEN, and only for enhanced functionality like automatic generation of
code for Database Maintenance, would there be a charge.

If enough people respond to make it worth doing, it will happen.

If you would like to register your interest in such a tool, please either
respond here or (if you don't want to be seen to do so publicly) mail me
privately.  If there is no interest, I won't undertake it.

Thanks,

Pete.






Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Converting ISAM files to RDB

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-05-26T13:49:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%vOP6.6628$DW1.292027@iad-read.news.verio.net>`
- **References:** `<3b0fabd6_6@Usenet.com>`

```
In article <3b0fabd6_6@Usenet.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:

[snippage]

>That is to
>take COBOL file definitions and automatically generate RDB tables from them.
…[3 more quoted lines elided]…
>Database.

... and thereby, of course, ignoring most of the capabilities of a
Relational Database in favor of duplicating the present related-index-file
structure.

Pardon me whilst I bellow, e'er-so-eloquently... BLEARGH!

Yes, I know this is done All The Time and Everywhere but it still causes
me visceral upset... it is similar to the Corner Office Idiot calling in
The Troops and saying 'Ol' Bernice 'n Louie have been keeping our books
in bound folios, making entries with goose-quills... We want to bring
them into the Computer Age... so write something which duplicates - and
duplicates *exactly* - everything they do but on a computer.'

DD
```

##### ↳ ↳ Re: Converting ISAM files to RDB

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-05-26T18:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0FF37F.703E5A8@home.com>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net>`

```


NA wrote:

> In article <3b0fabd6_6@Usenet.com>,
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
…[23 more quoted lines elided]…
> DD

I find your comments negative and non-productive. If somebody, (just as Michael
does with numerics), offers a piece of software to help development - I fail to
see the reasoning for your cynicism.

Is this in defence of Pete Dashwood - No ! Check out the thread "ESQL & ODBC" -
he is ALREADY royally pissed off at me - and we are no longer communicating
privately ! So be it.

What he is offering is a piece of software that will disassemble COBOL records
into meaningful DB formats. It provides a first stage conversion - it is then up
to the developer to take what is generated  and 'nurse' it to the format he
wants. Would I use it - No. My reasoning, (and I'm not going to go into a deep
explanation),  is that I do not unquestioningly accept the whole kerboodle
regarding DB Normalization, any more than I accept a 'purist' approach to OO
technology.

All tools *must* be adjusted to suit your perceived needs - and whether your
results fit the 'idealistic theory' doesn't matter a damn - the only thing that
counts is, does it work easily and efficiently, and as Howard would say,  "Is it
easily maintainable ?".

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Converting ISAM files to RDB

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-05-26T23:00:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vAWP6.6694$DW1.297928@iad-read.news.verio.net>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net> <3B0FF37F.703E5A8@home.com>`

```
In article <3B0FF37F.703E5A8@home.com>,
James J. Gavan <jjgavan@home.com> wrote:
>
>
…[29 more quoted lines elided]…
>I find your comments negative and non-productive.

Rather telling, some might say, that you have not stated you find them to
be untrue... what comes next, accusations that I might not be a Team
Player?

>If somebody, (just as Michael
>does with numerics), offers a piece of software to help development - I fail to
>see the reasoning for your cynicism.

What I stated were expressions of association ('... it seems similar to
me') and aesthetics ('BLEARGH'); such things are not always reconcileable
to reasoning.

DD
```

###### ↳ ↳ ↳ Re: Converting ISAM files to RDB

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-05-27T14:43:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b106ad7_5@Usenet.com>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net> <3B0FF37F.703E5A8@home.com> <vAWP6.6694$DW1.297928@iad-read.news.verio.net>`

```
Personally, Doc, I found your objection very fair, and associated with an
excellent (and entertaining)analogy.

Nevertheless, it WAS negative and didn't help the case...<G>

And, like Jimmy, I cannot refute it as untrue.
(But then, I WOULD say that...having worked with RDBs since they were
invented...<G>)

Pete.

" NA" <docdwarf@clark.net> wrote in message
news:vAWP6.6694$DW1.297928@iad-read.news.verio.net...
> In article <3B0FF37F.703E5A8@home.com>,
> James J. Gavan <jjgavan@home.com> wrote:
…[10 more quoted lines elided]…
> >> >take COBOL file definitions and automatically generate RDB tables from
them.
> >> >(NEGLCED <G>?).  This would be the first step towards converting an
> >> >Application system based on the COBOL File system (primarily using
Indexed
> >> >Datasets, but not necessarily only IDs) to a system using Relational
> >> >Database.
> >>
> >> ... and thereby, of course, ignoring most of the capabilities of a
> >> Relational Database in favor of duplicating the present
related-index-file
> >> structure.
> >>
> >> Pardon me whilst I bellow, e'er-so-eloquently... BLEARGH!
> >>
> >> Yes, I know this is done All The Time and Everywhere but it still
causes
> >> me visceral upset... it is similar to the Corner Office Idiot calling
in
> >> The Troops and saying 'Ol' Bernice 'n Louie have been keeping our books
> >> in bound folios, making entries with goose-quills... We want to bring
…[12 more quoted lines elided]…
> >does with numerics), offers a piece of software to help development - I
fail to
> >see the reasoning for your cynicism.
>
…[5 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Converting ISAM files to RDB

_(reply depth: 5)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-05-27T03:18:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ym_P6.6729$DW1.298720@iad-read.news.verio.net>`
- **References:** `<3b0fabd6_6@Usenet.com> <3B0FF37F.703E5A8@home.com> <vAWP6.6694$DW1.297928@iad-read.news.verio.net> <3b106ad7_5@Usenet.com>`

```
In article <3b106ad7_5@Usenet.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>Personally, Doc, I found your objection very fair, and associated with an
>excellent (and entertaining)analogy.
…[3 more quoted lines elided]…
>And, like Jimmy, I cannot refute it as untrue.

Hmmmmm... so that which cannot be refuted as untrue can be fair,
associated with excellence and entertainment, negative and unhelpful.

Fair amount o' ground covered, it seems.

DD
```

###### ↳ ↳ ↳ Re: Converting ISAM files to RDB

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-05-27T14:39:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b106ad2_5@Usenet.com>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net> <3B0FF37F.703E5A8@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B0FF37F.703E5A8@home.com...
>
>
…[8 more quoted lines elided]…
> > >take COBOL file definitions and automatically generate RDB tables from
them.
> > >(NEGLCED <G>?).  This would be the first step towards converting an
> > >Application system based on the COBOL File system (primarily using
Indexed
> > >Datasets, but not necessarily only IDs) to a system using Relational
> > >Database.
> >
> > ... and thereby, of course, ignoring most of the capabilities of a
> > Relational Database in favor of duplicating the present
related-index-file
> > structure.
> >
…[11 more quoted lines elided]…
> I find your comments negative and non-productive. If somebody, (just as
Michael
> does with numerics), offers a piece of software to help development - I
fail to
> see the reasoning for your cynicism.
>
So do I. But I totally understand where Doc is coming from.

> Is this in defence of Pete Dashwood - No ! Check out the thread "ESQL &
ODBC" -
> he is ALREADY royally pissed off at me - and we are no longer
communicating
> privately ! So be it.

I am not "Royally pissed off at you" (had no idea you were such a sensitive
soul...) I am disappointed with your behaviour. That is really my problem,
not yours. As for not communicating privately, you have already received
private help from me since I expressed my dismay.

> >>
> What he is offering is a piece of software that will disassemble COBOL
records
> into meaningful DB formats. It provides a first stage conversion - it is
then up
> to the developer to take what is generated  and 'nurse' it to the format
he
> wants. Would I use it - No. My reasoning, (and I'm not going to go into a
deep
> explanation),  is that I do not unquestioningly accept the whole kerboodle
> regarding DB Normalization, any more than I accept a 'purist' approach to
OO
> technology.
>
> All tools *must* be adjusted to suit your perceived needs - and whether
your
> results fit the 'idealistic theory' doesn't matter a damn - the only thing
that
> counts is, does it work easily and efficiently, and as Howard would say,
"Is it
> easily maintainable ?".
> >>

Yes Jimmy, a good argument. However it is really necessary to learn the
rules BEFORE you start breaking them. At least, it is if you REALLY want to
get the best results you can. (If you don't understand Normalization you
really can't just dismiss it as Academic theory.) I don't doubt for a minute
you will get a working result. However, I KNOW it could be better...

Actually, I really don't care whether what you end up with is perfect or
not.

What I care about is that you will blame RDB and dismiss it as "another
academic crap technology" before you have ever really understood it. It is
the injustice of it, and the fact that other fragile minds who hang on your
every word may be persuaded by you, that pisses me off...<G>

Pete.




Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Converting ISAM files to RDB

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-05-27T14:21:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b10670a_5@Usenet.com>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net>`

```
I totally agree Doc. And I share the sentiments paraphrased in your last
paragraph (excellent analogy, by the way...<G>).

It is NOT something I would do myself, but, like I said, I have had a
request to do it.

Here are some gentle arguments as to why I will do it, if there is enough
interest in it.

Sometimes we can't afford the luxury of rebuilding from scratch, sometimes,
for commercial reasons rather than "optimum computer system design" it is
necessary to get things into the market place because people want it.

For example, (and this is an actual case), a small software house has a very
successful package which they have developed over years using the COBOL file
system (primarily, ISAM) on PCs. Their customers want better reporting
facility, and the Software house also want to continue improving the
product) and this means continuing to use COBOL to produce these reports.
But the file system is closed so it is necessary to write COBOL programs
(which must be maintained) if the user wants to export or share data with
other standard Office software.Customer says: "Well XXXX package uses
Database technology and I can write my own reports and easily Query it using
Crystal or SQL. Not only that but I can export EXACTLY the subset I want to
Excel and examine it there, even if I don't know today what my requirements
are going to be tomorrow". There is now a competitive pressure on the
software house to make their product open, accessible and scalable.
It is also good Marketing for the package to be seen to be using RDB
technology.

All of these are good reasons for converting as far as the Software House is
concerned. It really has little to do with the aesthetics of database design
which, in a perfect world, you and I would prefer to see implemented.

If you are still not convinced, how about this as another argument...

There are a huge number of applications written using ISAM. Most of them are
very successful, but you are 100% correct that simply converting them will
not unleash the full power of Relational Technology. (I stress that I have
no issue with you on this; I love to see people getting the full benefit a
good relational design).

However, people need to start somewhere. The argument is that is better to
start with an Application they already know backwards, than to come to grips
with the foreign concept of Relational Design from day one (although, I
agree there are circumstances where this can also be advantageous...green
field sites, f'r'instance).

Using the tool I am proposing they will get their system (which they already
know and understand) converted into an unfamiliar format which will not be
too threatening... they will find that tables can be accessed the same as
their old files were and there is minimum impact on their existing code. By
splitting out the repeating groups they get introduced to the concept of
Normalization and, if their existing ISAM system was fairly efficient
anyway, the new RDB based one will be reasonably useful as well.

Once it is achieved and they realise it was not too traumatic, they will
hopefully be encouraged to do more.

I agree that it is not a perfect solution, but it is a start.

It will certainly get people familiar with the basic concepts of RDB and
accessing them in COBOL with ODBC. And it will remove some of the fear of
this technology which has been engendered over the years. I believe that is
a major step forward. The next system they design will be better... so is it
ever.

Please don't be too disparaging; the world is not a perfect place...<G>

Pete.


" NA" <docdwarf@clark.net> wrote in message
news:%vOP6.6628$DW1.292027@iad-read.news.verio.net...
> In article <3b0fabd6_6@Usenet.com>,
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
…[4 more quoted lines elided]…
> >take COBOL file definitions and automatically generate RDB tables from
them.
> >(NEGLCED <G>?).  This would be the first step towards converting an
> >Application system based on the COBOL File system (primarily using
Indexed
> >Datasets, but not necessarily only IDs) to a system using Relational
> >Database.
…[14 more quoted lines elided]…
> DD


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Converting ISAM files to RDB

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-05-27T03:15:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_i_P6.6728$DW1.298830@iad-read.news.verio.net>`
- **References:** `<3b0fabd6_6@Usenet.com> <%vOP6.6628$DW1.292027@iad-read.news.verio.net> <3b10670a_5@Usenet.com>`

```
In article <3b10670a_5@Usenet.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>I totally agree Doc. And I share the sentiments paraphrased in your last
>paragraph (excellent analogy, by the way...<G>).

Pfoo... you'se jes' easily impressed.  *Some* folks, though, might think I
have a Bad Attitude.

>
>It is NOT something I would do myself, but, like I said, I have had a
>request to do it.

Hmmmm... a 'request' is one thing, a Purchase Order (or a reasonable
facsimile thereof) is quite another.

>
>Here are some gentle arguments as to why I will do it, if there is enough
…[4 more quoted lines elided]…
>necessary to get things into the market place because people want it.

This appears to be a variation of 'We don't have enough time to do it
right but we *will* have enough time to do it over'... again, a moderately
common situation.  The clause of '... because people want it' I will take
to signify '... because people will sign checks for it'.

>Customer says: "Well XXXX package uses
>Database technology and I can write my own reports and easily Query it using
…[3 more quoted lines elided]…
>software house to make their product open, accessible and scalable.

... so that folks will buy *it*, rather than the competition.  Notice,
however, that the customer's motive is to include a capability of
relational technology (in this case an increased ease for ad hoc
queries... yes, I know that some file-based systems have Right Powerful
Query Tools written for them but it has been my experience that folks who
use a database of some type are more ready to demand ad hoc capabilities.)

>It is also good Marketing for the package to be seen to be using RDB 
>technology.

... so that more folks can be made to want to buy it, sure.

>
>All of these are good reasons for converting as far as the Software House is
>concerned. It really has little to do with the aesthetics of database design
>which, in a perfect world, you and I would prefer to see implemented.

Weeeelllll... in my case it is more a 'right tool for the right job'
aesthetic... consider:

'I gotta pound in some nails... what tools do we got?'

'We got a hammer 'n we got a torque-wrench.'

'Hmmmm... both'll work but we'll be more marketable if we can say our team
has experience with torque-wrench technology... so let's everyone pound in
nails with *those*!'

>
>If you are still not convinced, how about this as another argument...

Really, it is not a matter of convincing... remember my assertion of 'Yes,
I know this is done All The Time and Everywhere but it still causes me
visceral upset...'

[snippage]

>However, people need to start somewhere.

... and this is why, away-back-when, so many companies kept on
bank-after-bank of 'hello girls' after their first PBX was installed...
no... wait, did it happen *that* way or did a change in the technology
used to accomplish a task cause a change in workforce composition?

>The argument is that is better to
>start with an Application they already know backwards, than to come to grips
>with the foreign concept of Relational Design from day one (although, I
>agree there are circumstances where this can also be advantageous...green
>field sites, f'r'instance).

... and then again a company which Spells Acronyms Properly comes at this
in an exact opposite manner; they propose that you study the business and
determine what it is that one needs human-being type folks to do and what
can be left to machines.

(yes, I know that this software doesn't always get installed right and
doesn't always work the way folks hope... I also know that these
observations have been made of many other kinds of softwary, as well.
sometimes things work, sometimes they don't)

[snip]

>Please don't be too disparaging; the world is not a perfect place...<G>

Never said that it was nor did I say that it should be... what I *did* say
was that I think I've seen things like this before and they make me go
'BLEARGH!'

DD

>
>" NA" <docdwarf@clark.net> wrote in message
…[33 more quoted lines elided]…
>                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
