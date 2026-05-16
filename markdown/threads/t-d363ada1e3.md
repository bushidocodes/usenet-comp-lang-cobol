[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO Example

_5 messages · 5 participants · 2006-12_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO Example

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-12-05T09:38:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET>`

```
One of my duties is a programmer for a web-based system that provides 
configuration management for COBOL programs (among other things).  We're 
converting it to .net (C# / ASP.net), and as such, I'm trying to put 
some OO design together.  My first page is a replacement for the "Lines 
of Code" report that we currently had.

My first thought is "OK, a program is an object."  I can create a 
constructor for the object that is passed a program ID, and then has all 
sorts of properties.  In my report, I would instantiate the object, add 
its "lines of code" to the totals for that type of element, then destroy 
it, instantiate the next, etc.  Some of the properties of the program 
would be objects themselves (owning programmer, for example, would be a 
user object, instead of just the ID).

Anyway, I thought I had my head wrapped around it, then I followed the 
links that you folks have been posting - now I'm not so sure.  :)  I 
understand the theory behind "as few getters/setters as possible" - and 
I also know that even the "getters/setters are evil" guy conceded that 
"boundary" systems would need to have them to support interfacing with 
procedural systems.  I also understand that, for example, when a program 
is checked out, I shouldn't use some other object to set the properties 
of the program object, but rather have a method of the program object 
that, given a user object, does the work of checking that program out to 
that use.

I guess my question comes down to this - am I thinking about this report 
correctly?  Or is there some "report object" paradigm that I'm not 
getting?  A method is, generally speaking, a small snippet of procedural 
code that supports the work of the object (at least that's the way I 
understand it).  It just seems to me that I'm going to have to have some 
properties returned somewhere.

Or, should I just make a SQL statement to select COUNTs and SUMs from 
the database, and forget about making this some OO prototype?  :)
```

#### ↳ Re: OO Example

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-12-05T10:53:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Cgdh.104047$Cu4.1499630@wagner.videotron.net>`
- **References:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:e4f97$45759272$454920f8$30633@KNOLOGY.NET...
> One of my duties is a programmer for a web-based system that provides 
> configuration management for COBOL programs (among other things).  We're 
…[4 more quoted lines elided]…
> My first thought is "OK, a program is an object."
[...]
>
> I guess my question comes down to this - am I thinking about this report 
…[7 more quoted lines elided]…
> database, and forget about making this some OO prototype?  :)

    Honestly, I've never felt the OO paradigm worked well for web 
applications. Explaining to the computer how to format and emit a particular 
web page seems much better suited to a procedural style, IMHO. If a single 
SQL statement with COUNTs and SUMs will do the job, I'd definitely go with 
that over several classes, spread out over several files.

    - Oliver
```

##### ↳ ↳ Re: OO Example

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-05T11:07:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55dbn2hc8kokr6kj88hvueo97tche7hdbi@4ax.com>`
- **References:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET> <3Cgdh.104047$Cu4.1499630@wagner.videotron.net>`

```
On Tue, 5 Dec 2006 10:53:34 -0500, "Oliver Wong"
<owong@castortech.com> wrote:

>    Honestly, I've never felt the OO paradigm worked well for web 
>applications. Explaining to the computer how to format and emit a particular 
>web page seems much better suited to a procedural style, IMHO. If a single 
>SQL statement with COUNTs and SUMs will do the job, I'd definitely go with 
>that over several classes, spread out over several files.

Lots of web design doesn't need to be analyzed in an OO methodology. A
shop has their way of doing stuff, and we just write programs and plug
them into the existing design.    If the main tools are Java, SQL and
XML, we write in the style of existing Java, SQL and XML.
```

#### ↳ Re: OO Example

- **From:** "P. Raulerson" <paul.rl@raulersons.com>
- **Date:** 2006-12-05T20:50:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Idqdh.61281$1w6.26020@newsfe16.lga>`
- **References:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET>`

```
LOL!  That is a masterful summary if I have ever heard of one.
I would suggest layering the problem a little bit. Start with your Programs 
as Objects idea:

     new Program PROG001

Now you have a nice object out there. It is sort of a blank slate. You have 
the right idea to modify it's properties.
Here is there layering starts in though. Let's say one of those properties 
is OWNER.  Well, OWNER in itself is probably
a rather complex object, so here's what you do:

    new Owner PROG001_OWNER

Now think about an owner? Is it atomic yet, meaning will it have more 
objects in it, or will it be a "base" level object, holding just simple data 
like strings and numeric values? In this case, we will say it is atomic, 
though in reality, it may decompose further.

We are now at the issue we have been discussing. Let owner have two 
properties, say Name and Phone. You could simply expose these two properties 
and set them something like this:

     PROG001_OWNER.Name = 'Paul'
     PROG001_OWNER.Phone='5551212'

Note that there is no validation possible on the values when you do it this 
way. That isn't necessarily bad, it is just something to be aware of. Things 
that need to be edit checked should be set with a SETTER. (IMNSHO of course. 
:)  If you wanted validation, you would use a setter here, and hidden within 
the object, the method would do whatever it has to do to validate the entry. 
Such as looking up 'Paul' in a table of validated users or something.

Now step back up one level and think of the Program object...

We have our program object PROG001 and a owner object, PROG001_OWNER.

In this case we could once again just expose the Owner property  in the 
program object and do something like:
       PROG001.OWNER = PROG001_OWNER.

However, this case, we run into practical difficulties, equivalent to using 
structures in C. How do you get the REAL owner object into the Program 
Object? What if the language you are using only passed it by reference? Edit 
checks are a little more important here, etc.

This is a case where I believe you should use a setter. Not only does the 
Owner object now serve as an interface, but by using a setter you can do a 
lot of other things, like COPY the data from the Owner object and store it 
however the heck you want to - in an array, a list, a string, a remote DB2 
table on the other side of the planet... etc. So you want to use something 
like:

    PROG001.SetOwner( in Owner PROG001_OWNER)


So basically if you look at that pattern and repeat it till you have set of 
'atomic' objects you will have done a pretty decent OO design, without the 
frippery and such. In some ways you can equate it to normalizing a database; 
and that is because of the specific task you outlined. The programs and data 
objects are really acting more like an object oriented database than like 
say, a GUI.

And yes, you could basically do the same think in procedural COBOL. ;) 
That's the dirty little secret of OO, it is really not a whole lot more than 
a simple codification of most of the good practices programmers have learned 
over the past few decades. But don't tell 'em I told ya so... ;)

-Paul

"LX-i" <lxi0007@netscape.net> wrote in message 
news:e4f97$45759272$454920f8$30633@KNOLOGY.NET...
> One of my duties is a programmer for a web-based system that provides 
> configuration management for COBOL programs (among other things).  We're 
…[46 more quoted lines elided]…
> man who's offended by a God he doesn't believe in?" - Brad Stine
```

#### ↳ Re: OO Example

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2006-12-07T15:18:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1165533537.851931.243160@16g2000cwy.googlegroups.com>`
- **In-Reply-To:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET>`
- **References:** `<e4f97$45759272$454920f8$30633@KNOLOGY.NET>`

```


On Dec 5, 3:38 pm, LX-i <lxi0...@netscape.net> wrote:
> One of my duties is a programmer for a web-based system that provides
> configuration management for COBOL programs (among other things).  We're
…[33 more quoted lines elided]…
> --

Hi,

OO is a great technique for Web apps, imo.

There are numerous OO design principles that can come into place to
successful model and implement a  web app.

'Single Responsibility Principle' - Every class does exactly one job,
aka has one Responsibility.
'Tell Don't Ask' - Instead of one object calling the getter of another
object, it 'tells it' to do a job.
   E.g.

instead of :

  //  Inside a reporter object....

    reportLinesList  = db.getReportLines
    for each element in reportLinesList
       display element
    end


We do:

    Reporter.display( db.getReportLines )

  This way, Reporter class does not even know where the ReportLines
list comes from, its given it, by another part of the application
(Typically called a Presenter or Controller - see below)


With those in mind, here's how I'd approach your web app's Report:

Class Model - contains the business logic and/or data for the report
(e.g. runs the SQL above and sends a simple (none SQL containing)
message to a Presenter object).

Class View - contains the UI rendering display logic (e.g. creates
HTML, JSPs, etc for displaying the report results)

Class Presenter - provides a translation of UI events into model
updates/retrival requests, etc. (e.g. handles the user request to
refresh the report by sending a message to the model to refresh itself,
or the presenter might silently consume the UI request to prevent the
user from trying to refresh to often.
On receipt of the  refresh message, the Model will re run the sql. The
Model can then decide to inform its Presenter(s) if the results have
changed or not.

What this is trying to show, is that each class, whilst working
together to display a report, are all individual. They even do not need
to know what the other will do with the information or events they
send.

Hope this helps in some way...

Andrew
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
