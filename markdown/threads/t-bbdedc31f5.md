[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO in Batch (Was: Program ID)

_38 messages · 13 participants · 2004-06 → 2004-10_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO in Batch (Was: Program ID)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-25T08:08:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```
There seem to be a great number of people that don't believe batch 
processing can benefit from object oriented code.  This confuses me, I 
can think of several places where it would be a geat boon.  JOTTOMH:


   Files & Databases.  
   The traditional batch program needs to be recompiled and retested 
when file attributes change, data formats are shifted, IMS layout 
changes, etc.  In a shop with a large number of programs, this can be 
troublesome and time consuming.  
   With OO, a file access object can be created which will read records 
and publish a set of standard property fields.  Adding, removing and 
reformatting fields requires operation on a single object and a single 
set of source.


   Collections & Tables.
   Cobol has been living in data structure poverty for a long time.  
It's only collection structure, the table, is quite limited.  Using LE 
(or your compilers utility routines) storage allocation routines and 
either manual or automatic complex-ODO one can usually represent the 
most complicated of structures.  But it is not pretty.
   OO offers us a way to build dynamically resizeable collections 
easily.  And saves us from excessive preallocation.
```

#### ↳ Re: OO in Batch (Was: Program ID)

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-06-25T08:34:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a%UCc.40531$MU4.1149920@news20.bellglobal.com>`
- **In-Reply-To:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```
Joe Zitzelberger wrote:
> There seem to be a great number of people that don't believe batch 
> processing can benefit from object oriented code.  This confuses me, I 
…[21 more quoted lines elided]…
> easily.  And saves us from excessive preallocation.

I also think the OOP structure in general, is a better structure for 
most systems, particularly in Cobol.

Once you understand the structure of Cobol OOP (refering to the actual 
sytactical structure here, rather than the generalized theory of OOP), 
it makes far more sense architecturally speaking.  Takes a bit of 
getting use to, but provides a much better model for building systems 
than does the older "copies and calls" methodology.

While that may seem simplistic to the OOP purists, I think even non-OOP 
proponents should look at the structural aspects very seriously.

Donald
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-28T09:32:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-2290A7.09320228062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <a%UCc.40531$MU4.1149920@news20.bellglobal.com>`

```
In article <a%UCc.40531$MU4.1149920@news20.bellglobal.com>,
 Donald Tees <donald_tees@sympatico.ca> wrote:

> While that may seem simplistic to the OOP purists, I think even non-OOP 
> proponents should look at the structural aspects very seriously.
> 
> Donald


I don't think anyone can learn OOP without having their 
structured/modular/procedural design styles forever changed.

Once that light-bulb comes on, the light shines on everything.
```

#### ↳ Re: OO in Batch (Was: Program ID)

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-06-25T11:58:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10doir79ojc8cad@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```

Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com...
> There seem to be a great number of people that don't believe batch
> processing can benefit from object oriented code.

Mr Zitzelberger, your statement seems to be an absolute not
supportted by anything I have posted or read lately. Stroustrup,
for example, stated that "existing techniques developed over
decades are adequate"; which, to me, suggests that benefit is
relative. A similar sense comes from McConnell.

The question is not whether batch processing can benefit from
object orientation; but how to use the technology to maximize
the benefit.

Years ago, I analyzed a stand-alone, 58K source line application.
The application was part interactive and part batch. My conclusion
was that object oriented design followed by procedural
implementation would have provided the greatest benefit. I stopped
work on the project when I became disabled. [Mr Zitzelberger, you
may recall our previous discussion on Social Security Disability.
I had stated previously, in 2000, that I had retired; but, in fact, I was
in denial.]

After the project was kiled, I continued to think about it. I realized
that persistant storage of business objects requires that persistant
objects, at the storage level, be built though composition not
inheritance and that objects included by composition had very thin
inheritance heirarchies. This makes it quite easy to use redefinition
or separate fields for storage and to use evalute to simulate
polymorphism. This makes procedural implementation rather
straight-forward.

>  This confuses me, I
> can think of several places where it would be a geat boon.  JOTTOMH:
…[10 more quoted lines elided]…
> set of source.

While this would make it easier to accomodate some changes,
but what you suggest is little more than a procedural server for a
procedural client, effectively modular progrmming. Consider that
field definitions (usage and picture) must still be consistent
elsewhere in the application. That is, changes in the server will
show up somewhere in its clients.

>
>
…[7 more quoted lines elided]…
> easily.  And saves us from excessive preallocation.

A dynamic tables facility was proposed for 2002; but was dropped
due to unresolved issues. It is still proposed for the next standard.

I had suggestted to J4 the inclusion of a dynamic storage facility
that would enable the building of complex data structures without OO.
When last I checked, the item had a low priority. I have not been able
to work on it further due to my disability.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-06-25T18:22:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cbhqi0$r48$1@peabody.colorado.edu>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <10doir79ojc8cad@corp.supernews.com>`

```

On 25-Jun-2004, "Rick Smith" <ricksmith@mfi.net> wrote:

> > There seem to be a great number of people that don't believe batch
> > processing can benefit from object oriented code.
…[9 more quoted lines elided]…
> the benefit.

I think Mr. Zitzelberger is absolutely correct.   Which leads me to think that
the following are the major questions:

1.   How do we persuade the average batch shop that it is worth while going OO
for their batch processing.
2.   How do we persuade them that CoBOL is still an appropriate tool for their
needs.

I bet most batch CoBOL shops had ANSI-68 programs being used until Y2K, and
aren't likely to convert their current batch programs to the next compiler
unless they have to.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-28T09:29:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-BDA5F5.09295728062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <10doir79ojc8cad@corp.supernews.com>`

```
In article <10doir79ojc8cad@corp.supernews.com>,
 "Rick Smith" <ricksmith@mfi.net> wrote:

> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message
> news:joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com...
…[7 more quoted lines elided]…
> relative. A similar sense comes from McConnell.

I never want to just be "adequate".  I want people to be amazed at how 
easy it is to enhance, extend and maintain systems that I write.

McConnell also has some not-so-nice things to say about "existing 
techniques developed over decades" in other areas.  I think I cited him 
extensively in a thread about source formatting and indention where he 
shot down decades of block structure source format style as a 
code-horror (with the hair-raised icon next to it).


> >  This confuses me, I
> > can think of several places where it would be a geat boon.  JOTTOMH:
…[17 more quoted lines elided]…
> show up somewhere in its clients.

New technologies often build on the current state-of-the-art.  Much of 
OO is simply compiler support for techniques that have been found to be 
helpful (data hiding, polymorphism, et al).  For example, 
variable-length records with different data lengths or a record-type 
indicator represent an early form of polymorphism -- processing was 
similar for some parts, different for other parts of different records.  
Of course it was completely up to the programmer to enforce this.  With 
OO, you get compile time checks that it was enforced.
```

#### ↳ Re: OO in Batch (Was: Program ID)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-06-25T13:50:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0406251250.67ada577@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 

> There seem to be a great number of people that don't believe batch 
> processing can benefit from object oriented code.  This confuses me, I 
> can think of several places where it would be a geat boon.  JOTTOMH:

>    Files & Databases.  
>    The traditional batch program needs to be recompiled and retested 
> when file attributes change, data formats are shifted, IMS layout 
> changes, etc.  In a shop with a large number of programs, this can be 
> troublesome and time consuming.  

>    With OO, a file access object can be created which will read records 
> and publish a set of standard property fields.  Adding, removing and 
> reformatting fields requires operation on a single object and a single 
> set of source.

There are other ways of doing this too.  For example database 'views'
or not using '*' in the selects but specifying every field that is
needed.  Of course if the change is something that the program needs
to deal with then it will be recompiled because it has changed.

With systems using ISAM data files I always have generous fillers as
space that can be used for data items later without worrying about
programs that won't be concerned with it.  Actually, a couple of
decades ago, I adopted a set of 'standard' layouts that used the
pre-defined fields as required and left room for expansion.

So while you are quite correct that recompiling and retesting whole
systems is a complete pain, there have been ways of avoiding most of
this, or at least making it much less frequent.

I have also used an interfacing mechanism, much as you describe, to
allow a single file maintenance program and a single reporting program
to work on almost any data file.  These were initially written for CIS
Cobol on CP/M and another 8bit system.  The reporting program reads a
script text that specifies the file, the selection criteria,
calculations, output format.  It calls interfaces for the specific
file(s) and has a dictionary to relate the names to the actual field
positions.

The file maintenance program also uses the same interfaces and
dictionary but also has a text 'screens layout' that specify how the
several subscreens for each file should look plus editing criteria.

If I had OO Cobol 20 odd years ago it would have been done using it,
and would have been better for that. But the OO approach does not need
special syntax.
 
>    Collections & Tables.
>    Cobol has been living in data structure poverty for a long time.  
…[5 more quoted lines elided]…
> easily.  And saves us from excessive preallocation.

Actually Cobol's 'collection structure' is the file, and the file
mechanisms are much richer than any other language.  Much of other
language emphasis on trees, lists, and other collections are because
they can't easily do it with files.  Given that in most cases the data
to be put into these structures comes from files in the first place
they should be (in general) held in that structure in the file.

Granted that Cobol tables are not extensible, but they can be used to
build any complex structure by providing index (or subscript) entries
in the table for navigation or chaining.

There _are_ things which can be done using OO which are much more
difficult without, for example replication.  For the reporting program
(above) it has to use specific interface routines for the primary and
secondary files, with OO I would use several instances of the same
file objects saving some duplication of code and making it more
extensible, and probably allowing more flexibility in systems design.

But here is the problem: I have a system developed over more than two
decades which has allowed me to put together the basis of completely
new systems in just a couple of weeks and allows me to write many new
user requested reports in just a few minutes (in fact some users write
their own scripts or use a generator that I wrote).

The benefits of OO don't outweigh the cost of redeveloping all that I
have done, mainly because I have much of the benefits already
implemented.

Certainly I do use OO in other languages, mainly Python, which I have
been using for several years, but there was no existing baggage to
overcome.

In the case of the example where a small change in one file does
require a complete rebuild and retest then certainly this would not be
the case if it had been OO.  The cost of a complete rewrite would be
higher than the costs associated with this problem.  It is only
feasible to 'go OO' if a redevelopment is required anyway, you can't
just add a bit of OO here and there and expect benefits immediately.

It's about the cost/benefit equation.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-26T01:20:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40dcc936.38554326@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <217e491a.0406251250.67ada577@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>There are other ways of doing this too.  For example database 'views'
>or not using '*' in the selects but specifying every field that is
>needed.  Of course if the change is something that the program needs
>to deal with then it will be recompiled because it has changed.

In four out of five shops where I've worked recently, database changes were
routinely made without the need to retest programs accessing it. Programs were
not permitted it use '*'  not the equivalent on INSERT.

The fifth shop was obviously using database as a substitute for VSAM thinking.
Program comments referred to 'records' rather than rows.

If you use databases correctly, database changes can indeed be made independent
of program logic. There is no need to retest programs when the database changes.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-25T20:17:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406251917.2bddbf3a@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <217e491a.0406251250.67ada577@posting.google.com>`

```
Richard,

I found this to be an interesting post.

I like your description of specific processes being abstracted and
generalised so that you can produce reports and do file maintenance
very quickly.

It is my belief that imaginative approaches like this make the
difference.

Yet, I have encountered resistance to them on some installations.
Usually, it is because if things get too easy and Users start doing
it, it could threaten programmers jobs. (Someone actually said this to
me on a site in Germany many years ago...) There is often resentment
by management also that a generalised solution may take slightly
longer (they never think about the time it will save in the future...)

Your comments regarding baggage and OO are very much in line with my
own response in this thread (I read your mail after I posted it).

Everything has to be balanced and I endorse your final statement 100%.

Pete.

(TOP post, nothing below...)

Riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0406251250.67ada577@posting.google.com>...
> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 
> 
…[95 more quoted lines elided]…
> It's about the cost/benefit equation.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-28T09:06:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-9DB050.09060928062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <217e491a.0406251250.67ada577@posting.google.com>`

```
In article <217e491a.0406251250.67ada577@posting.google.com>,
 riplin@Azonic.co.nz (Richard) wrote:

> There are other ways of doing this too.  For example database 'views'
> or not using '*' in the selects but specifying every field that is
> needed.  Of course if the change is something that the program needs
> to deal with then it will be recompiled because it has changed.


I'm a product of my mainframe environment.  When I think of changing a 
table, or converting a table to a view it fills me with horror.  Not 
only do I need to need to recompile everything (because separate binds 
are dangerous, so sayth the DBAs), but it also involved getting buy-in 
from 1 to a dozen DBAs.

My PC history makes me rebel against the tight control of tables by 
another department.  Their goals never seem to be the same as the 
application developers.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-29T01:14:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40e0c12f.298682973@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <217e491a.0406251250.67ada577@posting.google.com> <joe_zitzelberger-9DB050.09060928062004@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <217e491a.0406251250.67ada577@posting.google.com>,
> riplin@Azonic.co.nz (Richard) wrote:
…[11 more quoted lines elided]…
>from 1 to a dozen DBAs.

Dynamic binding is the norm in Unix, Windows and IBM, according to IBM
literature. Sounds like your DBAs are applying lessons learned 20+ years ago.

>My PC history makes me rebel against the tight control of tables by 
>another department.  Their goals never seem to be the same as the 
>application developers.

You're right. They seem to take delight in obstructing progress.

In my world, programmers develop Views and Triggers in their own schema in a
sandbox. When it's time to promote the package through change management (CM) ,
they create a script to build the objects in higher levels (in production
schemas) and insert those files into CM along with source programs. DBAs may or
may not review them, but they can't sit on them indefinately.

The key to success is to treat database changes the same as source code changes.
Don't let DBAs make them something 'special' that avoids deadlines and
management oversight. They should have Good Reason to block a change. 'I didn't
get around to it' doesn't make the grade.
```

#### ↳ Re: OO in Batch (Was: Program ID)

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-26T01:20:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40dcbe08.35691947@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>   Collections & Tables.
>   Cobol has been living in data structure poverty for a long time.  
…[3 more quoted lines elided]…
>most complicated of structures.  But it is not pretty.

Last year I presented a demo that constructed ODO, dynamically allocated,
instances of programs, lines and words.  I thought it was pretty. The ODO was
simple, not complex.
```

#### ↳ Re: OO in Batch (Was: Program ID)

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-25T19:53:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406251853.11455e8a@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>...
> There seem to be a great number of people that don't believe batch 
> processing can benefit from object oriented code.  

I'm one, Joe.

It isn't that batch processing CAN'T benefit, rather that the hassle
of moving an installation into OO JUST for the sake of Batch
processing, is not supportable.

You also have to look at what happens currently. COBOL is ideally
suited to writing Batch applications. It doesn't need OO to do that.

An installation that uses well-established structured modular
programming for mainly Batch processing, is not going to gain enough
from OO to make the migration worthwhile.

>This confuses me, I 
> can think of several places where it would be a geat boon.  JOTTOMH:
…[6 more quoted lines elided]…
> troublesome and time consuming. 

Only if you are stupid enough to integrate DB access in to your
application programs. If you have a layered (multi tier) system
design, with modules that access the files and/or databases, you will
gain nothing from moving it to an OO architecture.

If you DON'T have such a design, it is still easier to revise your
architecture into multi-tier using the standard programming you know
and love, than it is to revise your architecture into multi tier AND
try and understand OO at the same time. From a Management POV the
risks are just unnecessary.
 
>    With OO, a file access object can be created which will read records 
> and publish a set of standard property fields.  Adding, removing and 
> reformatting fields requires operation on a single object and a single 
> set of source.
> 
As it does with a single structured module that provides that service
in a multi tier architecture.

> 
>    Collections & Tables.
…[6 more quoted lines elided]…
> easily.  And saves us from excessive preallocation.

Yes, I agree completely with you here. I HATE to see ODO in programs
and will not use it myself. OO does provide NODE classes that are
extremely useful for collections, but would you be prepared to
recommend a move to OO just so a Collection facility can be enjoyed?

The problem is that, for most existing COBOL sites, the inertia and
attitude re-shaping that needs to be overcome in order to implement OO
systems effectively, cannot be justified if all they are doing is
batch processing, or if that is the nub of their business. It is a
major cost and major business risk to migrate to OO. There is no point
in doing it unless you are very sure that the benefits are worth it.
As far as Batch processing goes, they generally aren't. COBOL sites
have always, and will continue to, cope with Batch processing. No cost
justifiable benefit in migrating to OO.

When it comes to the Network, and their interactive processing, a
different case can be made.

It is interesting to me to see posts here in support of OO, when I
think of the resistance  and even personal attacks that were
encountered when some of us suggested it might be a good idea, around
7 years ago... I guess CLC is like a herd of elephants; ponderous, not
quick to grasp new ideas, but devastating once they get moving... <G>

Pete.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-06-26T16:07:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40DD9F30.8040605@optonline.net>`
- **In-Reply-To:** `<b3638c46.0406251853.11455e8a@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com>`

```
Peter, I'm enjoying the debate a great deal. It's most difficult for
me to see the need for OO in batch processing.

Yet, in my following of the TinyCobol project, I've learned that they
use Berkley DB for their non screen I/O, and I was interested enough
to download the package, and do what I knew how to do. Open up the
installed file(S) and try to comprehend the design.

Because of it's collection of I/O methods (I believe excluding the full
DB) I think the package serves as a great example of the use of OO
to create a generalized software tool.

For the same purpose (learning), several interesting applications for
Linux users have been likewise reviewed and I've concluded the same
there.

 From reading here and there, I believe Windows dose not fully qualify as
an OO tool. But attempts to do so. Perhaps the next version.

My biggest hangup about OO in COBOL stems from the purpose of making the
program self documenting (not for programmers, but for Management). The
OO examples I've seen lack the description of what the program is doing.
And why. To me this reflects my own lack of knowledge of these methods, 
and an adverse reaction to reading the procedures of example Cobol 
programs using OO.  Jimmy has tried to help me overcome some of my
problems in this regard, but it seems to me that the things he used
belonged in the generalized tool class. Oh, and I will probably never
get used to identifying what is a CLASS, OBJECT, ETC. However, I've
begun to like the idea of property. As I see it, the COBOL Picture is
a property set of symbols. It seems, also that to extend them to
support the usual properties of an editor for certain kinds of record
types would be very helpful in todays world.

Your comments regarding OO seem consistent with your position in past
discussions of the idea that the  proper tool for the job at hand.
In my old world, the job at hand is still to make the source
program represent a description of the function of the step being
computerized.

I enjoy your participation in this forum. Thank you.

Warren Simmons
P.S. In case you have missed it, Bob Beamer has died. His web
page is apparently still on line, and full of "stories" of
things past. Some I could elaborate on.



Peter E. C. Dashwood wrote:
> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>...
> 
…[85 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-26T18:02:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406261702.60b55f52@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <40DD9F30.8040605@optonline.net>`

```
Warren Simmons <wsimmons5@optonline.net> wrote in message news:<40DD9F30.8040605@optonline.net>...
> Peter, I'm enjoying the debate a great deal. It's most difficult for
> me to see the need for OO in batch processing.
…[8 more quoted lines elided]…
> to create a generalized software tool.

Yes, OO is very good for that. BUT, you CAN do it with structured
modular programming and a multi-tier design also. The point here is
that OO is NOT the only way...(However, there are some things for
which OO IS the only way and these are the areas where OO shines and
returns on investment.)

> 
> For the same purpose (learning), several interesting applications for
…[5 more quoted lines elided]…
> 

Oboy! I never thought I'd see the day when you would be pulling the
cat's tail, Warren <G> Good for you!

I'm not touching this one with a barge pole, but I will say that
Windows has improved out of sight since the early 16 bit
implementations. XP Pro is very stable and behaves the way an OS
should. It is the first Windows implementation I've been satisfied
with. As for being OO, well any OS doesn't necesarily have to BE OO,
just so long as it SUPPORTS OO.


> My biggest hangup about OO in COBOL stems from the purpose of making the
> program self documenting (not for programmers, but for Management). The
> OO examples I've seen lack the description of what the program is doing.
> And why. 

That's a very valid point. For myself, I don't consider a component is
complete until I've finished the help file for it, describing all of
it's Methods, Properties, and Events. Of course if you are writing in
OO COBOL there is no excuse not to document what you do, just as you
would for standard COBOL.

I have some reservations about whether "Management" should be allowed
near source code (or any code, for that matter...<G>). I think it is
best to keep discussions with them on a "functional" rather than "in
depth technical" nature. There is still a marked tendency for what
someone here (sorry, I can 't remember who it was, but it is very
apposite) calls "airline magazine Management" where they don't really
understand the technology but they know what they read.

The argument for self documenting Source Code is no longer as strong
as it was 30 years ago. Why would you document source code? Because
you intend to change it or will need to change it.

But what if you build your system from predefined "blocks" that have
known functions and will NEVER be changed? These days, particularly in
systems built with components, where the source is probably not
available, the relevance of source code is immaterial. I have systems
running and deployed live that utilise comonents I didn't write and
have no access to the source code for. If I want to, I can change
their behaviour without having to recompile them. I can add new
components and modules that use different Methods in them or modify
the behaviour of Methods already being used, all without re-compiling
the component. (See my posts to the thread about regression testing).
This concept is pretty hard for COBOL people to take. We are used to a
world where Source code is King. In the modern world it is not program
source code that is King, it is DELIVERED FUNCTIONALITY. That's why
the same functions get reused over and over.

I've posted about this before and I don't intend to go over it all
again. Properly conceived and built components do not require
maintenance in the COBOL sense. A function is a function is a
function. Minor changes to its behaviour can be achieved by modifying
its properties; the basic interface does not change.

The concepts applicable to designing systems for Procedural
programming are NOT applicable in component based design and that's
why I get frustrated in this forum. (I accept it is my own fault, not
the people here... <G>)


> To me this reflects my own lack of knowledge of these methods, 
> and an adverse reaction to reading the procedures of example Cobol 
> programs using OO.  Jimmy has tried to help me overcome some of my
> problems in this regard, but it seems to me that the things he used
> belonged in the generalized tool class. 

I won't comment on Jimmy Gavan's interpretation of things OO. He has
something that works for him.

There is a whole argument that says reading ANYONE's sample COBOL OO
code (including mine...) will not give you a proper insight into how
OO works.

It is quite natural for COBOL Programmers to continue writing
procedural code and simply wrapping it as OO. The breakthrough occurs
when the MINDSET changes.

(For me this happened when I taught myself Java and realised that
beans could encapsulate functionality without ever needing
maintenance; it was a fairly easy step from there to building
components, especially as Fujitsu really facilitate this process in
their PowerCOBOL product.)

COBOL was NOT designed as an OO language. It had OO bolted onto it (I
have referred to it in the past as "Jake the Peg" but this will be
lost on people who have never heard of Rolf Harris.) In my opinion,
the implementation of OO COBOL is one of the most admirable feats of
software engineering in the history of programming. The people who
designed and built it have my admiration and gratitude. But it is
still "Jake the Peg". It will never have the seamless OO integration
that Java has, for example. (That doesn't mean it is no use; I use it
almost every day to create new functionality wrapped as components
that can run across platforms and on the web.)

> Oh, and I will probably never
> get used to identifying what is a CLASS, OBJECT, ETC. However, I've
…[3 more quoted lines elided]…
> types would be very helpful in todays world.

Be careful here Warren. It is all too easy to approach new stuff with
the "ITSA" filter turned on. An invoked object and a called module
have very important subtle differences, but many COBOL people, on
encountering INVOKE and seeing syntax they recognize from previous
experience, go "ITSA called module..." It isn't, but it IS similar.

(One reason why young people without COBOL experience pick up OO so
easily, is because they don't have ITSA filters in place... For myself
I try and develop an ITMIGHTBE or ITSLIKE filter, then explore why it
ISN'T what I thought it could be...<G> We all need hooks to hang new
stuff on when we are learning...)

Don't worry too much about getting your head around the jargon.
(Amazingly enough, OO modules and components, (provided they are
correctly coded and logically sound) will actually work, even if the
programmer doesn't understand what polymorphism or an abstract class
are...<G>)

If it helps, you might remember that a CLASS is a group of things with
similar properties, and an OBJECT is one instance (member) of that
group. (While this is not a completely accurate definition, it is
certainly good enough for everyday use.)

As for a COBOL Picture being a property, it certainly can be. In fact
OO COBOL allows the word "PROPERTY" to be attached preceding or
following a picture, so that that data element can be treated as an
object property. (Usually this means making it PUBLIC). You might also
like to have a look at the meaning of TYPEDEF, as defined in the new
standard.

> 
> Your comments regarding OO seem consistent with your position in past
> discussions of the idea that the  proper tool for the job at hand.

You have no idea how much it cheered me up to read that <G> Someone at
least has taken something I said on board.

Yes, I am on record as saying that we should use the right tool for
the job in hand, and I stand by it. Originally I said this partly to
defuse the "COBOL and NOTHING else" war that was going on, and stop it
degenerating into a slagging match between usng COBOL and using other
languages. I was also genuinely concerned that many career COBOL
programmers could find themselves out of a job unless they expanded
their horizons. Sadly, this proved to be true. Time has moved on and I
think everyone has now come to the realisation that COBOL will not
stem the tide of modern languages. A recent Gartner survey (and
remember, Gartner have a vested interest in COBOL) said that 15% of
new development is still being carried out in COBOL. This is
encouraging, but it is a long way from the 85% of 35 years ago.  The
fact is that COBOL programmers need to have other tools in their bag
as well as COBOL. I still think everyone should invest some of their
time in learning Java. It will be with us for some time to come.

> In my old world, the job at hand is still to make the source
> program represent a description of the function of the step being
> computerized.
> 

Yes, but that is no longer as important as it was, Warren. (See
above).

> I enjoy your participation in this forum. Thank you.
> 

Thanks for that, Warren. I'll be here as long as it serves some useful
purpose.

Regards,

Pete.

> Warren Simmons
> P.S. In case you have missed it, Bob Beamer has died. His web
…[93 more quoted lines elided]…
> > Pete.
```

##### ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-27T21:42:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-776A1E.21424427062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com>`

```
Sooner or later, someone other than me is going to have to do some new 
development in Cobol or the platform will just die out.  I'm just 
suggesting that there are useful ways that OO could be integrated into 
those new platforms.  I wasn't suggesting migrating the alread 
functioning platforms to OO just for the sake of OO.

I have to say though, an I/O module to do file or database access isn't 
much better than doing the I/O in the program.  Field location and 
datatype are still bound at compile time.  Even if it is only a 
recompile to pick up the new copybook, it is still a huge PITA in a 
non-trivial system.  However, you can get a property bound at runtime* 
with almost no effort.  The benefits of that are great.

(*No specific Cobol-OO implementation in mind, just general OO 
approaches to things)


In article <b3638c46.0406251853.11455e8a@posting.google.com>,
 dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message 
> news:<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com>...
…[79 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-28T02:12:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H8LDc.9850$x9.8787@nwrddc02.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com>`

```
<grin> I do new development in COBOL. I've just decided not to do so with
the current
Microfocus or AcuCOBOL products, mostly because I am  annoyed with their
idea of what
a fair price is. RM Cobol here in Austin seems to understand that well, and
I think the next
major project I have to do on a PC I will strongly consider doing with their
product.

I do use IBM COBOL on mainframe and the PC's right now, CobolSet for AIX on
the pSeries, and
(it would appear!) a couple versions of COBOL on the  iSeries machines now.
The lack of a usable
and reliable compiler for Linux is a PITA, but deploying under Linux means
deploying with
tightly controlled costs. At least it means that if one intends to stay
solvent!

As a consequence, when deploying under Linux on the mainframe, we are using
HLASM. Works
great, much less cost, and runs like greased lightening.

-Paul


"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-776A1E.21424427062004@corp.supernews.com...
> Sooner or later, someone other than me is going to have to do some new
> development in Cobol or the platform will just die out.  I'm just
…[57 more quoted lines elided]…
> > >    With OO, a file access object can be created which will read
records
> > > and publish a set of standard property fields.  Adding, removing and
> > > reformatting fields requires operation on a single object and a single
…[39 more quoted lines elided]…
> > Pete.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-28T11:01:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40dff3c5.246088688@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net>`

```
"PAUL RAULERSON" <pkraulerson@verizon.net> wrote:

><grin> I do new development in COBOL. I've just decided not to do so with
>the current
>Microfocus or AcuCOBOL products, mostly because I am  annoyed with their
>idea of what
>a fair price is.

We all are. As I've said, it's a supply/demand. If demand for Cobol was
comparable to C# or Java, MF could sell compilers for $100 too.

How many dot-Net developers do you think are interested in Cobol? My unsupported
guess would be few. I've not seen a job ad asking for that skill.

>RM Cobol here in Austin seems to understand that well, and
>I think the next
>major project I have to do on a PC I will strongly consider doing with their
>product.

I'd consider Fujitsu before RM. I'm surprised RM is still in business.

>As a consequence, when deploying under Linux on the mainframe, we are using
>HLASM. Works
>great, much less cost, and runs like greased lightening.

Why not GCC? It's the best compiler ever written. Assembly language takes three
times as long to write and isn't portable.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 5)_

- **From:** "Paul Raulerson" <pkraulerson@verizon.net>
- **Date:** 2004-06-28T12:34:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfUDc.11252$DT5.5646@nwrddc03.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net>`

```
Assembler does not take 3x the time to write that most people think, and if the target
platform is a mainframe (or even an Intel platform) it is pretty portable indeed.
In addition, a good HLASM programmer can write code as quickly as a COBOL
programmer, and the code will be just about as understandable (with comments :)

In the old days, you could pretty much do a one to one comparison of COBOL
with Assembler - and indeed many folks used the COBOL compiler to learn assembler.
Nowadays, we just teach people.

We choose HLASM syntax because it is both more understandable and more powerful
than the AT&T syntax used by the GNU toolset. In addition, GAS syntax is meant
to process compiler output, while HLASM is meant to be used by humans.

MOVE A TO MYVAR   vs. MVI   MYVAR,C'A'   is still pretty much one to one.

To read from a file, for instance, you use the CLIB routines or SVC calls. I think
SVC 3 is read, so the code would be:

LHI     R2,FILEDES            UNIX FD IN R2
LA      R3,INBUFAD           ADDRESS OF BUFFER TO READ INTO
LHI    R4,50                        READ UP TO 50 CHARS
SVC   3
ST      R2,RC                      STORE RETURN CODE

That equates to  rc=read(FILEDES, &INBUF, 50). You can see that the logic is
of course, identical. The composition is slightly more wordy, but the programmer
still has to consider the same 5 issues.

It beats the heck out of paying say, 180K for compiler and runtime rights on a system
just to be able to say

READ IN-FILE-RECORD

That is a pure dollars and cents type of thing though. A technical second choice.

Intel Assembler under Linux is slightly more complex, but not much. Just have to deal
with those nutcase Intel registers. Note though, that Linux uses the Intel registers pretty
much like GPR's.


-Paul



"Robert Wagner" <robert.deletethis@wagner.net> wrote in message news:40dff3c5.246088688@news.optonline.net...
> "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:
>
…[24 more quoted lines elided]…
> times as long to write and isn't portable.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-28T16:27:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406281527.54e87fc5@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net>`

```
Hi Paul,

thanks for posting something we can seriously disagree about <G>.

Reading your post was like a time warp and made the hairs on the back
of my neck stand up (that's about the only place I have any remaining
these days...<G>).

I remember having these exact same arguments in 1969. Spooky.

It's not that I'm anti-Assembler (I write it (or "wrote" it) for both
the Intel platform and the mainframe. It's just that I remember WHY
the World moved away from it.

If nothing else, your post made me think about those arguments again.

(BTW, there are some web sites dedicated to assembler programming on
both the Intel and mainframe platforms, so you are certainly not
alone. Furthermore, your Company has taken a business decision based,
apparently, on the cost of a COBOL compiler. I have to wonder who did
the sums... Any kind of long term cash flow, with maintenance,
portability, availability of staff, time to debug, and the loss of
vendor options,  factored into it would show that it might be cheaper
(in the long run), to bite the bullet and buy the compiler...)

Anyway, some specific responses below, and thanks for a good response
to Robert's also excellent post.

"Paul Raulerson" <pkraulerson@verizon.net> wrote in message news:<qfUDc.11252$DT5.5646@nwrddc03.gnilink.net>...
> Assembler does not take 3x the time to write that most people think, and if the target
> platform is a mainframe (or even an Intel platform) it is pretty portable indeed.

Oh no it isn't...  It is portable to another mainframe of the same
type and you are now locked in to that supplier. Always supposing you
can find people to write it and maintain it for you. (You can always
outsource this, of course but the rates for IBM assembler guys (most
of whom moved into Systems Programming years ago) are at least double
what it costs to get COBOL people.)

On the Intel platform you are at the mercy of low level API calls
which vary with every release of the OS. If you go the whole hog and
decide not to use system services, then your company should question
what business it is in.

And, even if you use macro assembler and cut and paste most of your
"modules" it still takes a lot more time than writing it in COBOL. (I
won't say "3x" because I haven't done specific quantification, but I
know from my own experience that it definitely takes longer to develop
even small assembler modules, than it does to do them in a high level
language. The degree of research required and the attention to detail
is MUCH greater. It isn't ALL about MVI this or MVC that; that's just
a small part of it.

> In addition, a good HLASM programmer can write code as quickly as a COBOL
> programmer, and the code will be just about as understandable (with comments :)
> 

So why did everybody move away from Assembler back in the 60s? The
whole world got it wrong? One of the reasons for the acceptability of
COBOL was that it was SELF documenting (or is when you write it
properly). The equivalent in assembler requires a comment on every
line. That takes time.

> In the old days, you could pretty much do a one to one comparison of COBOL
> with Assembler - and indeed many folks used the COBOL compiler to learn assembler.
> Nowadays, we just teach people.
> 

NOBODY in my experience ever used the COBOL compiler to learn
Assembler. Assembler programmers already knew Assembler (and were
dragged kicking and screaming into COBOL) and new programmers learned
COBOL without NEEDING to learn Asssembler. Sure, after a couple of
years some of them became interested in the generated code and this
led to acquiring some Assembler knowledge, but knowing the various
formats and Opcodes of the most generated (by COBOL) instructions does
NOT make an Assembler programmer.

> We choose HLASM syntax because it is both more understandable and more powerful
> than the AT&T syntax used by the GNU toolset. In addition, GAS syntax is meant
> to process compiler output, while HLASM is meant to be used by humans.
> 

Can't comment as I have no experience in this area. I believe Robert
suggested in his original mail that an Open source solution might be
appropriate. If your response is that Assembler is "more
understandable" then I have to ask: "More understandable than what?"
Is one form of Assembler more understandable than another? If you are
concerned with readability, why use Assembler at all?


> MOVE A TO MYVAR   vs. MVI   MYVAR,C'A'   is still pretty much one to one.
>

Yes it is. But there is a lot more "baggage" to Assembler programming
than that.
 
> To read from a file, for instance, you use the CLIB routines or SVC calls. I think
> SVC 3 is read, so the code would be:
…[10 more quoted lines elided]…
> 

You are arguing against your own case here... It isn't "slightly more
wordy" it is MUCH more wordy. And the meaning of the words is not
immediately obvious, although I agree it is well coded and the
comments are good.

What happens when a future release of the OS implements SVC 3 in a
slightly different way?  Can't happen? I wish...


> It beats the heck out of paying say, 180K for compiler and runtime rights on a system
> just to be able to say
> 
> READ IN-FILE-RECORD
>

Being able to issue a READ statement is not the sole justification for
using COBOL, but if you believe that, then I can understand the
climate in which this surprising decision was taken.

Whether a compiler is worth the price or not cannot be considered in
isolation. You do a thorough business case and factor in all the
things I mentioned above. It also depends on the budget for your IT
department. Maybe the company simply can't afford to use a mainframe.
I cannot (and do not) believe that writing your critical applications
in Assembler is a cheaper long term solution than writing them in
COBOL or another High Level language. What other options were
considered before deciding on Assembler? Why not move to Java? It
would be more intelligible and would provide more options in terms of
platform portability.
 
> That is a pure dollars and cents type of thing though. A technical second choice.
> 
…[3 more quoted lines elided]…
>

Yeah, right... Wait until you have written some Intel Assembler before
deciding ITSA...

Summing up:

In this day and age, to move towards application development (as
opposed to system programming) in Assembler Language has to be
questioned strongly. What exactly are the special and particular
business factors that led to this? Was independent advice sought, or
did the vendor take a few people to lunch and extol the virtues of an
"efficient platform"? (That has you locked in to them forever...) How
comprehensively were the options examined?

While I respect the right of every company to manage their business
and take the decisions they see fit, moving back to the 1960s has to
be seriously questioned.

What's next?

Flared pants, marijuana, and acid rock? (Hey, I just realised how they
made the decision...<G>)

Pete.

> 
> -Paul
…[30 more quoted lines elided]…
> > times as long to write and isn't portable.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-29T04:20:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<466Ec.15090$x9.3662@nwrddc01.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <b3638c46.0406281527.54e87fc5@posting.google.com>`

```
<grin> Ah, the wannabe assembler programmer clarion call! :)
Comments below.

"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:b3638c46.0406281527.54e87fc5@posting.google.com...
> Hi Paul,
>
…[7 more quoted lines elided]…
>

I won't swear the summer of love attitude has nothing to do with it, but...
I won't swear it doesn't either. :)

> It's not that I'm anti-Assembler (I write it (or "wrote" it) for both
> the Intel platform and the mainframe. It's just that I remember WHY
…[16 more quoted lines elided]…
> "Paul Raulerson" <pkraulerson@verizon.net> wrote in message
news:<qfUDc.11252$DT5.5646@nwrddc03.gnilink.net>...
> > Assembler does not take 3x the time to write that most people think, and
if the target
> > platform is a mainframe (or even an Intel platform) it is pretty
portable indeed.
>
> Oh no it isn't...  It is portable to another mainframe of the same
…[5 more quoted lines elided]…
>

Basically, if you write it on a mainframe, it is portable between mainframe
platforms
and semi-portable between mainframe OS's.

> On the Intel platform you are at the mercy of low level API calls
> which vary with every release of the OS. If you go the whole hog and
> decide not to use system services, then your company should question
> what business it is in.
>

You can use the CLIB just as easily, which protects you much more
than than usiing the SVC calls. But why the overhead? The same call,
when using the clib, will execute close to a hundred, perhaps even more,
instructions before it gets around to making the SVC call. [Okay, INT 80
for you Intel types! 8] A macro with equates gives almost as much protection
as using the CLIB, since it is unlikely indeed that basic service calls like
OPEN, CLOSE, READ,WRITE, etc are going to drastically change between
versions. Heck, if they did, the corresponding CLIB call would have to
change
as well.



> And, even if you use macro assembler and cut and paste most of your
> "modules" it still takes a lot more time than writing it in COBOL. (I
…[6 more quoted lines elided]…
>

No it isn't, and when you run into an Assembler issue, you often spend a
lot more time focusing on 'tiny' issues than on 'the big picture.' I would,
however, argue that the same is true in COBOL. I spent hours fussing with
a never-to-be-sufficiently-cursed COBOL program the other day, only to
find out there was an extension I didn't know about.

Watched an associate of mine fight will copying null terminated strings
around in Assembler too - until I introduced him to the MVST instruction.
<grin>

It depends upon what you really want to do I suppose. I don't appreciate
writing TCP/IP socket servers in assembler, though I *can* - while on the
other hand, but then I don't like doing that in COBOLeither, though I *can*.
Given a choice, I usually tend towards COBOL first, Ada second, C third,
Java fourth, and a plethora of other languages from there down.

> > In addition, a good HLASM programmer can write code as quickly as a
COBOL
> > programmer, and the code will be just about as understandable (with
comments :)
> >
>
…[5 more quoted lines elided]…
>

What makes you think they did? :) z/OS is in every sense, a very modern O/S,
but it still
has an assembler interface. OS/400 doesn't even SPEAK assembler, and it
still has an
API strongly - very strongly! - influenced by assembler.

<grin> Okay, I'll stop being annoying and tell you the real reason-
assembler is alive and
well in mostly niche markets. In my 'day' job, we run the business with a
lower operating cost
that almost any other shop you can imagine - and with a very limited
progrmaming staff.
We could quadruple the staff though, and still easily undercut processing
costs for
any company 5 times our size. Indeed, that is because the core programs are
assembler
and don'thave a lot of fluff around 'em. Still provides real time, and
secure, access to
data over the web with nice looking pages almost as quickly as it does to
hundreds of
users with green screen access. And it doesn't even make a single z800 IFL
break a sweat
yet. :)



> > In the old days, you could pretty much do a one to one comparison of
COBOL
> > with Assembler - and indeed many folks used the COBOL compiler to learn
assembler.
> > Nowadays, we just teach people.
> >
…[9 more quoted lines elided]…
>

I know quite a few people who did exactly that, including me. Heck, under
Linux, I;ve been
known, more than once, to code something complex in C and take a look at the
assembly.
Works nicely in a lot of cases.

> > We choose HLASM syntax because it is both more understandable and more
powerful
> > than the AT&T syntax used by the GNU toolset. In addition, GAS syntax is
meant
> > to process compiler output, while HLASM is meant to be used by humans.
> >
…[7 more quoted lines elided]…
>

HLASM is far more understandable than GAS, even though they accept similar
mnemonics, and produce the same object code. Assembler is readily readable
when shop standards are in place, keeping the look and feel of the code
consistent.
This is, however, not an 'assembler' thing. It is just as important when
dealing with
COBOL or Java or Ada or even PERL.

>
> > MOVE A TO MYVAR   vs. MVI   MYVAR,C'A'   is still pretty much one to
one.
> >
>
> Yes it is. But there is a lot more "baggage" to Assembler programming
> than that.
>

With IBM assembler, not as much as you might think. Everything is macroed
for the most part. The example below would be the expanded source from
a macro that looks something like:

  OPEN UFB=INFILE,MODE=INPUT

(That's the Wang version, the IBM version is essentially the same, but the
names change a little.:)


> > To read from a file, for instance, you use the CLIB routines or SVC
calls. I think
> > SVC 3 is read, so the code would be:
> >
…[6 more quoted lines elided]…
> > That equates to  rc=read(FILEDES, &INBUF, 50). You can see that the
logic is
> > of course, identical. The composition is slightly more wordy, but the
programmer
> > still has to consider the same 5 issues.
> >
…[5 more quoted lines elided]…
>

Not really, in C, unless your audience knows the function call prototype,
you need to explain
the arguments somewhere, perhaps in a comment. In assembler, you are just
making line comments
to fit the bill.


> What happens when a future release of the OS implements SVC 3 in a
> slightly different way?  Can't happen? I wish...
>
>
> > It beats the heck out of paying say, 180K for compiler and runtime
rights on a system
> > just to be able to say
> >
…[17 more quoted lines elided]…
>

While the main argument for keeping things in assembler is that it
is more cost effective to NOT try and port it to a different language,
there is still a lot of argument to develop in assembler as well.
You are not limited to HLASM from IBM, as there are at least
two other compilers on the market that both do a GREAT job.
(Dignus and Tachyon, slightly different approaches, both are
great tools. If pushed, I favor Dignus because I personally find
them easier to work with, but both Dave Rivers (& crew) and
Dave Bond  are great people to work with, and extremely well
versed in all things assembler. :)


> > That is a pure dollars and cents type of thing though. A technical
second choice.
> >
> > Intel Assembler under Linux is slightly more complex, but not much. Just
have to deal
> > with those nutcase Intel registers. Note though, that Linux uses the
Intel registers pretty
> > much like GPR's.
> >
…[3 more quoted lines elided]…
>

Oh, I've written a few lines of Intel assembler - but I restrict myself to
protected mode
only code on 386 and above machines. Also well versed in 680x0, Vax, PDP-11,
Varian, and PowerPC assembler. HLASM is a much 'higher' level language
than any of the above.

> Summing up:
>
…[7 more quoted lines elided]…
>
Cost cost cost
Performance performance performance
legacy code legacy code legacy code
Market advantage
More.

Assembler is a viable application development tool on the mainframe.
I believe it to be under Intel Linux too, but I am not 100% positive
on that one. :)



> While I respect the right of every company to manage their business
> and take the decisions they see fit, moving back to the 1960s has to
…[6 more quoted lines elided]…
>

I do rather miss those bell bottom jeans. They were comfortable, and the
ladies look really good in them. :)

> Pete.
>
…[5 more quoted lines elided]…
> > "Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40dff3c5.246088688@news.optonline.net...
> > > "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:
> > >
> > > ><grin> I do new development in COBOL. I've just decided not to do so
with
> > > >the current
> > > >Microfocus or AcuCOBOL products, mostly because I am  annoyed with
their
> > > >idea of what
> > > >a fair price is.
> > >
> > > We all are. As I've said, it's a supply/demand. If demand for Cobol
was
> > > comparable to C# or Java, MF could sell compilers for $100 too.
> > >
> > > How many dot-Net developers do you think are interested in Cobol? My
unsupported
> > > guess would be few. I've not seen a job ad asking for that skill.
> > >
> > > >RM Cobol here in Austin seems to understand that well, and
> > > >I think the next
> > > >major project I have to do on a PC I will strongly consider doing
with their
> > > >product.
> > >
> > > I'd consider Fujitsu before RM. I'm surprised RM is still in business.
> > >
> > > >As a consequence, when deploying under Linux on the mainframe, we are
using
> > > >HLASM. Works
> > > >great, much less cost, and runs like greased lightening.
> > >
> > > Why not GCC? It's the best compiler ever written. Assembly language
takes three
> > > times as long to write and isn't portable.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-29T08:31:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-96BEFE.08313029062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <b3638c46.0406281527.54e87fc5@posting.google.com>`

```
In article <b3638c46.0406281527.54e87fc5@posting.google.com>,
 dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

> So why did everybody move away from Assembler back in the 60s? The
> whole world got it wrong? One of the reasons for the acceptability of
> COBOL was that it was SELF documenting (or is when you write it
> properly). The equivalent in assembler requires a comment on every
> line. That takes time.

They did?  I can think of some large, world-wide, financial sysems that 
use nothing but assember.  If your wallet is prone to contain little 
plastic squares, as many are, then you are likely to be using said 
systems.


> What's next?
> 
…[3 more quoted lines elided]…
> Pete.

The Dead are bringing their summer tour near enough to my house that I 
cannot resist loading up the backpack and spending a few days in the 
parking lot.  I might wear some flared pants, as they seem to be back in 
style.  But I doubt I will smoke any marijuana, least I fail my drug 
test.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 8)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-06-29T08:35:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XodEc.161903$207.862493@news20.bellglobal.com>`
- **In-Reply-To:** `<joe_zitzelberger-96BEFE.08313029062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <b3638c46.0406281527.54e87fc5@posting.google.com> <joe_zitzelberger-96BEFE.08313029062004@corp.supernews.com>`

```
Joe Zitzelberger wrote:
> In article <b3638c46.0406281527.54e87fc5@posting.google.com>,
>  dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:
…[28 more quoted lines elided]…
> test.

Well, I doubt I'd wear flared pants ...

Donald
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-29T01:14:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40e0c1f4.298880091@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net>`

```
"Paul Raulerson" <pkraulerson@verizon.net> wrote:

>Assembler does not take 3x the time to write that most people think

Twice when I was a full-time assembler programmer, once mainframe and once
Intel, I thought the same. I thought I could write just as fast in asm as in a
HLL (Cobol). So I did a test by writing and debugging the same non-trivial
function in both languages.

The results were 3x slower in asm. I urge you to perform a similar test.

>In addition, a good HLASM programmer can write code as quickly as a COBOL
>programmer, and the code will be just about as understandable (with comments :)

I used to think that. I found line count per hour about the same. Asm source
code was three times as big.

>We choose HLASM syntax because it is both more understandable and more powerful
>than the AT&T syntax used by the GNU toolset. In addition, GAS syntax is meant
>to process compiler output, while HLASM is meant to be used by humans.

All those macros amount to a 'private language' that's not designed as well as
Cobol, C or other HLLs. I once worked with a CS PhD who designed a very high
level language through the use of macros. Not only was it hard for others to
understand (as expected), its more serious failure was that, under the covers,
it produced clunky machine code.

>MOVE A TO MYVAR   vs. MVI   MYVAR,C'A'   is still pretty much one to one.
>
>To read from a file, for instance, you use the CLIB routines or SVC calls. I
think
>SVC 3 is read, so the code would be:
>
…[7 more quoted lines elided]…
>of course, identical. The composition is slightly more wordy, but the
programmer
>still has to consider the same 5 issues.
>
>It beats the heck out of paying say, 180K for compiler and runtime rights on a
system
>just to be able to say
>
>READ IN-FILE-RECORD
>
>That is a pure dollars and cents type of thing though. A technical second
choice.

Penny wise and pound foolish. You're giving up so much to save money on your
most fundamental tool, the programming language.

I confess to doing the same in the Bad Old Days, when machines were slow, men
were men, etc. We did it out of necessity. I wouldn't do it today, now that raw
CPU speed can plow through big obstacles. 

A final note -- I've seen GCC actually BEAT well-crafted assembly language that
I wrote myself. My first reaction was "that's impossible". After inspecting the
generated code, I realized the 'back-end guy' knew more about Intel than me.
GCC is free.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-29T04:27:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jc6Ec.15128$x9.288@nwrddc01.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <40e0c1f4.298880091@news.optonline.net>`

```
Have to agree to disagree here.
"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40e0c1f4.298880091@news.optonline.net...
> "Paul Raulerson" <pkraulerson@verizon.net> wrote:
>
…[3 more quoted lines elided]…
> Intel, I thought the same. I thought I could write just as fast in asm as
in a
> HLL (Cobol). So I did a test by writing and debugging the same non-trivial
> function in both languages.
>
> The results were 3x slower in asm. I urge you to perform a similar test.
>

We have, and it depends upon the programmer. I can write in COBOL about
1/2 again as fast as assembler, but that is because I have written more
COBOL.

Other folks I know can code about 2x as fast in assembler as in COBOL.
Depends almost entirely on the skill set of the person doing the
programming,
and how well defined the problem is.


> >In addition, a good HLASM programmer can write code as quickly as a COBOL
> >programmer, and the code will be just about as understandable (with
comments :)
>
> I used to think that. I found line count per hour about the same. Asm
source
> code was three times as big.
>

In terms of pure byte count, that is not usually true, though it may be in
terms of
LOC.


> >We choose HLASM syntax because it is both more understandable and more
powerful
> >than the AT&T syntax used by the GNU toolset. In addition, GAS syntax is
meant
> >to process compiler output, while HLASM is meant to be used by humans.
>
> All those macros amount to a 'private language' that's not designed as
well as
> Cobol, C or other HLLs. I once worked with a CS PhD who designed a very
high
> level language through the use of macros. Not only was it hard for others
to
> understand (as expected), its more serious failure was that, under the
covers,
> it produced clunky machine code.
>

Well, we dont' allow 'clunky' machine code under the covers. We don't abuse
Macro's
either, and design to produce efficient output. I don't care if a Macro is
500 lines long, as
long as it produces the right 5 lines of code for every set of input.

Well, actually, I do care, I much prefer 'simple' macros and I don't agree
with hiding all
the complexity ina Macro either. But in assembler, with good shop standards,
it isn't an issue.


> >MOVE A TO MYVAR   vs. MVI   MYVAR,C'A'   is still pretty much one to one.
> >
> >To read from a file, for instance, you use the CLIB routines or SVC
calls. I
> think
> >SVC 3 is read, so the code would be:
…[7 more quoted lines elided]…
> >That equates to  rc=read(FILEDES, &INBUF, 50). You can see that the logic
is
> >of course, identical. The composition is slightly more wordy, but the
> programmer
> >still has to consider the same 5 issues.
> >
> >It beats the heck out of paying say, 180K for compiler and runtime rights
on a
> system
> >just to be able to say
…[6 more quoted lines elided]…
> Penny wise and pound foolish. You're giving up so much to save money on
your
> most fundamental tool, the programming language.
>
> I confess to doing the same in the Bad Old Days, when machines were slow,
men
> were men, etc. We did it out of necessity. I wouldn't do it today, now
that raw
> CPU speed can plow through big obstacles.
>
> A final note -- I've seen GCC actually BEAT well-crafted assembly language
that
> I wrote myself. My first reaction was "that's impossible". After
inspecting the
> generated code, I realized the 'back-end guy' knew more about Intel than
me.
> GCC is free.
>

Sure - I can do the same thing on a Mainframe, gaining several free
instructions
if I want to. A compiler can do that kind of optimization automatically.
But even the best GCC compiled code adds hundreds of uneeded instructions i
into a program. That can really bite you even on very fast processors. All
you need to do is execute 100 extra instructions a billion times or so...

>
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-06-29T14:25:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cbru5n$kdu$1@peabody.colorado.edu>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <40e0c1f4.298880091@news.optonline.net> <Jc6Ec.15128$x9.288@nwrddc01.gnilink.net>`

```

On 28-Jun-2004, "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:

> We have, and it depends upon the programmer. I can write in COBOL about
> 1/2 again as fast as assembler, but that is because I have written more
> COBOL.

Yep.   But someone who is fully competent in both languages would tend to write
the same speed with each language.   That speed being measured in lines per
minute.

But lines per minute isn't a good measurement.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-06-29T08:08:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cbs0m0$12av$1@si05.rsvl.unisys.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <qfUDc.11252$DT5.5646@nwrddc03.gnilink.net> <40e0c1f4.298880091@news.optonline.net>`

```
"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40e0c1f4.298880091@news.optonline.net...

> A final note -- I've seen GCC actually BEAT well-crafted assembly language
that
> I wrote myself. My first reaction was "that's impossible". After
inspecting the
> generated code, I realized the 'back-end guy' knew more about Intel than
me.
> GCC is free.

Burroughs figured out something similar nearly a half-century ago.

Back in the days when the Burroughs B5000 was being designed, the first
ALGOL compiler was "hand-written" in ALGOL primarily as a design description
step, and then manually translated into (I think it was) Burroughs B260
assembler language as a cross-compiler -- running on the B260 to produce
B5000 object code.

This cross-assembler-based compiler was built to the point where it was
possible to use it to compile the ALGOL-based compiler, which by then had
been transcribed into cards.  The object code produced by the ALGOL-based
compiler was *significantly* smaller and *significantly* faster than the
assembler-based version, which I'm fairly sure was abandoned before the
first B5000 was even built (the early software work was done using a
software simulator on a Philco 2000 system).

To this day, the compilers for the ALGOL dialects are "triple-compiled" as
part of the release process, and every such compiler in the entire history
of the Burroughs Large System can trace its compilation "parentage" back to
that first ALGOL-based compiler on the B5000.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 5)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-28T08:59:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-88643B.08590928062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net>`

```
In article <40dff3c5.246088688@news.optonline.net>,
 robert.deletethis@wagner.net (Robert Wagner) wrote:

> "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:
> 
…[7 more quoted lines elided]…
> comparable to C# or Java, MF could sell compilers for $100 too.

That cuts both ways -- if MF sold compilers for $100 there would be many 
more casual users.

Remember the TurboPascal success story?
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-06-28T15:31:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com>`

```
But remember that Fujitsu "gave away" their V3 compiler - and although lots of
people took it, very few used it for any profitable work.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-28T23:01:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-80C7B4.23012028062004@corp.supernews.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>`

```
In article <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> But remember that Fujitsu "gave away" their V3 compiler - and although lots of
> people took it, very few used it for any profitable work.
…[25 more quoted lines elided]…
> 

I remember that -- I think they sent me a CD with a windows installer.  
What use is that in a Macintosh / Linux / Solaris house?

I've noticed that geeks tend to use off-brand OSes far more often than 
non-computer savvy people.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 7)_

- **From:** paul@raulersons.com (Paul Raulerson)
- **Date:** 2004-06-29T08:58:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b475f.0406290758.3e3e4fc9@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>`

```
Had to think about that one Bill. Yes, the gave away a pretty good
compiler, but the free version was pretty well limited to the Windows
platform, and the for cost versions under SunOS/Solaris and HP/UX,
while not over prived, were definately under-featured. No SCREEN
section among other things.

The Editor and IDE were also rather clunky. Still, it was a good
product.

With Version 4, they did some pretty nice improvements, but the cost
started rising, and they got into a Microsoft like upgrade cycle. It
got costly rather quickly, at least as compared to the pricing for V 3
& 4.

Then they went over the brainbow and decided that .NET was their path
to the future. That's where I parted ways with 'em I am afraid. The
COBOL compiler became a whole lot less about COBOL than about being a
GUI screen designer as in Visual Basic.

In short, the product evolved from something that could be used to get
business done without worrying all that much about 'Windows' to
something so intimately tied to Windows that it is impossible to
disassociate the user interface from the business rules and logic. Or
at least, very difficult to do so.

If instead, they had taken the Solaris version, added a screen
section, and published it for $49.95 under Linux, well, there might
have been a whole different set of pictures happening.

I think both Microfocus and AcoCOBOL has superior products by any
measure, but I also think they view themselves pretty much solely as
compeition for ex-mainframe customers. Netiher of them has promoted
COBOL uder Linux on the Mainframe to any signfigant extent, and, from
their point of view, with good reason. People will expect it to be
inexpensive under Linux - even on the mainframe. Perhaps especially on
the mainframe.

I've had people try to tell me they were giving me a really good
bargain by charging me $100K for a product under Linux on the
mainframe that costs $299 per developer under Linux on a PC. It is not
uncommon for vendors to hear the work mainframe and jump from $100 to
$10,000. Again, ridiculous.

This tendancy by VARs to want to rape the mainframe market is the #1
reason mainframes are viewed with suspicion and irritation these days.
Sure, you pay a lot for a mainframe, more than you would for an
AS/400, which costs more than you pay for an AIX machine. The levels
of reliability and capability go right along with the pricing.

But... you then have a flock of rabid VARS on the loose complaining
that the machine undercuts their 'investment' in S/390 or zSeries.
Poppycock! They are
saying they want to keep riding the gravy train of unrealistically
high priced software. While I think making a profit is a good thing,
companies like CA are being obscene about it when it comes to the
mainframe. They are playing on a historical point of view that is no
longer true. (*sigh*)

Our open systems COBOL vendors haven't yet found a way to deal with
Linux in a business model that produces the same kind of profit level
they enjoy today. But today they have a shrinking market. Sooner or
later, they will be forced to realize that embracing Linux and
providing reasonably priced software will be how they can continue in
business for decades to come. Heck, the compiler part is pretty
reasonably priced these days, with support and a really good compiler
coming in around $3K. It is those pesky runtimes that rack up the
dollars, and are nothing but the company saying "our stuff is so good
if we don't take drastic steps to protect it, everyone will steal it!"

Yeah, people will steal it - no matter if it is protected or not. But
why would anyone steal it if they can buy the thing at a reasonable
cost and be 'legal'? Certianly no developer is going to steal it, nor
will any of the highly audited companies in the U.S. It isn't worth
the penalty of being caught!

Anyway, I'll jump off my soapbox here and stop howling about this
situation. It will be self correcting, inevitably so. Some wise guy(s)
will find a niche and become sucessful in it, and the entrenched
traditionalists, once they have their noses rubbed in the fact it
makes money, will follow suit. Kicking and
screaming all the way, I have no doubt, but they will follow. 

IBM leading with Linux on all the platforms is a very brave and
deserving move, and has already upset VARs from CA to SCO. <grin>


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>...
> But remember that Fujitsu "gave away" their V3 compiler - and although lots of
> people took it, very few used it for any profitable work.
…[23 more quoted lines elided]…
> > Remember the TurboPascal success story?
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 8)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-30T22:39:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40e33a9c.460864375@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com>`

```
paul@raulersons.com (Paul Raulerson) wrote:

>Our open systems COBOL vendors haven't yet found a way to deal with
>Linux in a business model that produces the same kind of profit level
…[7 more quoted lines elided]…
>if we don't take drastic steps to protect it, everyone will steal it!"

I just learned that Fujitsu sells a Cobol compiler for Linux (on Intel) for
$1,500. THERE ARE NO RUNTIME FEES. Features include an integrated SQL
precompiler,  support for some IBM and Micro Focus extensions, an Eclipse (open
source) IDE, support for generating CGI,  and OO.

As for Screen Section, they say  

"Applications that make extensive use of unsupported IBM or Micro Focus
extensions may be able to use the IBM or Micro Focus syntax converters.

Applications that have extensive screen interactions may take more effort to
port. Depending on the design and purpose of the applications, they may be able
to transition to becoming Web-based applications using CGI, or take on new
graphical user interfaces using a more GUI focused language while preserving the
main business logic in COBOL."

They offer free 30-day trial. I'm considering doing two projects with it, using
CGI (Web) as a user interface.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 9)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-07-01T01:36:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QUJEc.18146$x9.14015@nwrddc02.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com> <40e33a9c.460864375@news.optonline.net>`

```
I've looked at it, and found it pretty well unusable without using something
like a COBOL based
thin client screen handler. (Check out Flexus.) That adds considerable cost
to the project, as
well as complexity.

Support for Microfocus or AcoCOBOL screen sections would not be all that
difficult to
achieve.


-Paul

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40e33a9c.460864375@news.optonline.net...
> paul@raulersons.com (Paul Raulerson) wrote:
>
…[11 more quoted lines elided]…
> I just learned that Fujitsu sells a Cobol compiler for Linux (on Intel)
for
> $1,500. THERE ARE NO RUNTIME FEES. Features include an integrated SQL
> precompiler,  support for some IBM and Micro Focus extensions, an Eclipse
(open
> source) IDE, support for generating CGI,  and OO.
>
…[5 more quoted lines elided]…
> Applications that have extensive screen interactions may take more effort
to
> port. Depending on the design and purpose of the applications, they may be
able
> to transition to becoming Web-based applications using CGI, or take on new
> graphical user interfaces using a more GUI focused language while
preserving the
> main business logic in COBOL."
>
> They offer free 30-day trial. I'm considering doing two projects with it,
using
> CGI (Web) as a user interface.
>
>
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-06-30T23:34:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0406302234.3e6b2422@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com> <40e33a9c.460864375@news.optonline.net> <QUJEc.18146$x9.14015@nwrddc02.gnilink.net>`

```
"PAUL RAULERSON" <pkraulerson@verizon.net> wrote

> I've looked at it, and found it pretty well unusable without using something
> like a COBOL based
> thin client screen handler. (Check out Flexus.) That adds considerable cost
> to the project, as
> well as complexity.

SP/2 has a Unix/Linux text mode GUI package that I use (though I use
the DOS text mode designer for this).  This also has no runtimne fees.
It will then run on almost any client machine from dumb terminal,
simple telnet/ssh box, Linux client machine or putty on MS Windows -
locally or over internet (use ssh).

The same code will run using SP/2 thin client (which only has MS
Windows clients).

While this is an issue when converting existing Screen Section based
code, for new systems it is much easier (once learnt) than Screen
Section and gives a better UI (IMHO).

Fujitsu also runs well as Web Server CGI systems.

> Support for Microfocus or AcoCOBOL screen sections would not be all that
> difficult to achieve.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 11)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-07-01T12:19:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0jTEc.22418$x9.18483@nwrddc01.gnilink.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com> <40e33a9c.460864375@news.optonline.net> <QUJEc.18146$x9.14015@nwrddc02.gnilink.net> <217e491a.0406302234.3e6b2422@posting.google.com>`

```
Oh? I'm out of date on Bob's stuff then. I thought there were only GUI
clients, each of which
ran with a runtime and associated cost. I guess I need to beebop over there
and have a
look. It's a great product indeed.

-Paul

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0406302234.3e6b2422@posting.google.com...
> "PAUL RAULERSON" <pkraulerson@verizon.net> wrote
>
> > I've looked at it, and found it pretty well unusable without using
something
> > like a COBOL based
> > thin client screen handler. (Check out Flexus.) That adds considerable
cost
> > to the project, as
> > well as complexity.
…[17 more quoted lines elided]…
> > difficult to achieve.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-01T12:31:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407011131.41902330@posting.google.com>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com> <40e33a9c.460864375@news.optonline.net> <QUJEc.18146$x9.14015@nwrddc02.gnilink.net> <217e491a.0406302234.3e6b2422@posting.google.com> <0jTEc.22418$x9.18483@nwrddc01.gnilink.net>`

```
"PAUL RAULERSON" <pkraulerson@verizon.net> wrote 

> Oh? I'm out of date on Bob's stuff then. I thought there were only GUI
> clients, each of which ran with a runtime and associated cost. 

Bob's site is actually the one 'out of date'.  He still lists DOS and
OS/2, and also UNIX Motif which he hasn't offered in some time.

"""COBOL sp2 has been continually enhanced to provide new features.
sp2 (and it spredecessor, screenplay) versions and release dates have
been as follows:

    * screenplay v.1.0 - May 1986
    * COBOL sp2 v.1.0 - October 1987
    [..]
    * COBOL sp2 v.3.2 - August 1995 """

Uhhhh, Bob, that's nearly 9 years ago, and its up to release 4.1.xx.
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2004-10-02T14:32:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjl5pe$cic$1@domitilla.aioe.org>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com> <JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net> <7b475f.0406290758.3e3e4fc9@posting.google.com>`

```
Paul,

I'm not going to labour this any further, but there are a few things you
could consider.

1. Your position is predicated on the fact that programming will remain
procedural as it has been, and commercial applications will be developed by
writing lines of code, for the foreseeable future.

You may be right, but it is by no means certain and is at best, arguable.

Personally, I don't think so. But that is because I have been exposed to
tools and software that are extrememly powerful and NOT based in this
paradigm.

Furthermore, I am developing successful applications that include
functionality I didn't write and have no need to maintain. It is cheap and
very easy. (The applications can be "maintained", but the building blocks
needn't be. None of it REQUIRES procedural code, although I still use COBOL
just out of fondness...)

2. Do you really think that there will be no major breakthroughs in the way
we use computers, in the next, say, 20 years, and we will continue doing
what we have been doing since the 60s?

I understand your resistance to Windows, but the fact is that once the
landslide starts, the pebbles don't get to vote. Fujitsu were not wrong to
provide extensive support for the MS environment; that's where the market
is.

Having said that, I'm not convinved about dot net yet (nice rhyme, isn't it
:-)) but I think it is only a matter of time.

As for Linux, I am finding it increasingly attractive and people who I
respect are advocating that I look at it. I will install it on the next
notebook I buy when the current one comes up for replacement. (If any of you
have ever played "Age of Wonders" or "Warcraft", do you find that the Giant
Penguins used by the Frostlings just make you think of Linux? There is
something satisfying in surrounding them and hacking them to bits...but I
digress.)

3. I agree with you about the overpricing of mainframe software. It's a
case of "what the traffic will bear". You don't HAVE to use a mainframe.

4. I predict that within 15 years AS400 will disappear, and the lower range
mainframes will be priced down to fill that spot. The only reason AS400
exists at the moment is because of marketing. It is coming under pressure
from new Intel technology (and Motorola) and the increase in price over a
standard server will not be justifiable, as reliability of server software
and hardware increases. Nailing your flag to a system that is marked for
obsolescence may not be a wise choice.

The future, as always, will reveal itself. It will be interesting.

Pete.

(Top post, no more)

"Paul Raulerson" <paul@raulersons.com> wrote in message
news:7b475f.0406290758.3e3e4fc9@posting.google.com...
> Had to think about that one Bill. Yes, the gave away a pretty good
> compiler, but the free version was pretty well limited to the Windows
…[84 more quoted lines elided]…
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:<JRWDc.3873$lh4.3569@newsread1.news.pas.earthlink.net>...
> > But remember that Fujitsu "gave away" their V3 compiler - and although
lots of
> > people took it, very few used it for any profitable work.
> >
…[10 more quoted lines elided]…
> > > > ><grin> I do new development in COBOL. I've just decided not to do
so with
> > > > >the current
> > > > >Microfocus or AcuCOBOL products, mostly because I am  annoyed with
their
> > > > >idea of what
> > > > >a fair price is.
> > > >
> > > > We all are. As I've said, it's a supply/demand. If demand for Cobol
was
> > > > comparable to C# or Java, MF could sell compilers for $100 too.
> > >
> > > That cuts both ways -- if MF sold compilers for $100 there would be
many
> > > more casual users.
> > >
> > > Remember the TurboPascal success story?
>
```

###### ↳ ↳ ↳ Re: OO in Batch (Was: Program ID)

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-29T01:14:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40e0c246.298961475@news.optonline.net>`
- **References:** `<joe_zitzelberger-8EB06C.08082925062004@corp.supernews.com> <b3638c46.0406251853.11455e8a@posting.google.com> <joe_zitzelberger-776A1E.21424427062004@corp.supernews.com> <H8LDc.9850$x9.8787@nwrddc02.gnilink.net> <40dff3c5.246088688@news.optonline.net> <joe_zitzelberger-88643B.08590928062004@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <40dff3c5.246088688@news.optonline.net>,
> robert.deletethis@wagner.net (Robert Wagner) wrote:
…[15 more quoted lines elided]…
>Remember the TurboPascal success story?

Pricing is a classic subject in management schools. If your product has mass
appeal, go for volume. If you're selling into a niche market, maximize profit
with high prices.

Airlines try to burn the candle at both ends by charging 'business' passengers a
high rate and 'pleasure' passengers a low rate. They differentiate by ability to
plan ahead (how ironic that 'managers' cannot plan ahead). In the long run it
doesn't work. Southwest, JetBlue and Virgin prosper by catering to the masses
while the big guys teeter on the brink of failure.

If you want to be a 'populist hero' write a Cobol compiler and sell it for $100.
The experience will turn you into a cynic.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
