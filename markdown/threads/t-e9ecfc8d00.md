[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Standards

_1 message · 1 participant · 2007-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL Standards

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-19T18:40:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lIOVh.98467$aG1.53495@pd7urf3no>`

```

Bill,

This is addressing your query regarding OO developers and your J4
document on where the Standards should go.

J4 Committee.
-------------
Back when it started COBOL had some 30 or more participants, vendors and
interested commercial users. Looking at the latest set of minutes issued 
- J4 07-0072 - Meeting 260 - 2007 Feb 13 through 15, there were 4.5
attendees, (the 0.5 is if you include Chuck Stevens phoning in his
comments).

Now J4 has issued warning letters to Victor Consulting and Micro Focus 
that their membership is in jeopardy if they don't attend the next
meeting. I suppose in the due course of time our Japanese friend, Wataru
Takagi will also soon receive a warning if he doesn't show up.

How difficult is it for J4 to get the message ? Like a sinking oil
tanker three-quarters submerged, the captain has ordered up four or six
deck-chairs for the wheelhouse, which is the only place still dry.
(Perhaps somebody should throw the deck-chairs overboard). Why was it
necessary for you to have to spell it out ?

Object Orientation

Not sure what was in your mind as to what you want to deliberate upon,
but see if any of the following helps. Firstly another quote from
Raymond Obin's 1993 paperback :-

-----------------------------------------------------------------------
OO is a very wide field, and there are many topics that can be
considered at the same time. This book is intended to be an introduction
to the subject for COBOL programmers. As an introduction , it is not
exhaustive, and for COBOL programmers it does not attend to matters
outside the COBOL arena.

Class libraries are a very important part of OO programming. Any set of
classes can be called a class library, although the term class library
is often often used to refer to a set of classes with a common theme. A
standard COBOL class library has not yet been defined....... For
more information on Class Libraries and for some insight as to what a
standard COBOL class library might contain, see Ref. *Smalltalk*. (***
my emphasis ***).

Programming tools are an essential part of OO programming, and are vital
if OO is to be used effectively. Class browsers, advanced navigation
tools, class librarian tools to locate classes that can be reused,
effective debuggers etc., are all part of the OO programming
environment. (*** Me, note well the following ***). When it comes to
selecting an OO language, the choice is likely to be swayed more by the
available tools than by the features in the language. What's the point
of an all-singing, all-dancing language it is practically impossible to
use ?

*** he then briefly mentions interoperability between languages and
CORBA ****

--------------------------------------------------------------------------------

Can't find the quote, but Ray must have been feeling in Heaven after a
few good shots of whiskey, because he adds later, "Perhaps one day we
will all be using OO COBOL".

I agree with him where the original intention seems to have been to
create COBOL OO support libraries and possibly at that time Ray was also
thinking of GUI classes as being part of that support. (???)

In support of Ray's statement it was another former M/F employee who
wrote to me about 5 years ago - 'He didn't have any faith in an OO
Language which didn't have support libraries'. He wasn't referring to
the M/F compiler, but OO COBOL in general.

Now it doesn't really matter which language you use, (Ray's reference to
all-singin' all-dancin'), the way to go is TOOLS. The first approach is
an IDE, then you hit dotNet with Visual Studio and get the features that
Pete enthuses about - depending upon the object or class you are using
it gives you a prompt list of available methods. (Interestingly enough
even the 'junior' Smalltalk, 'SQUEAK' has the visual presentation of
methods which can be used with particular objects).

Not quite in the same vein, but still tools, you will have noticed I
have enthused about M/F's Open ESQL Assistant which gives you
bullet-proof SQL statements. And you can use that tool as a complete
rookie to SQL. A lesser one but useful for a newcomer; write a
program/class accessing/updating an ISAM - have you got your comp-3
field values correct ? Shortcut, open the data file in the IDE and your
file format is shown USAGE DISPLAY, and can be edited, if you wish.

Bear in mind you could quite happily design a complete application with
Classes only or Programs/Classes, using Screen Section. And it would be
perfectly legitimate to call that an OO application. GUIs/Webbing are
add-ons and not the raison d'etre for OO. Xerox PARC Smalltalk team -
their first project was to design something we all take for granted - a
word processor. (I've mentioned before, what clinched it was when Adele
Goldberg secretively nipped their computers out of the building, having
first enhanced 'Smalltalk' with stick-men, graphical figures. Took the
equipment to a local junior school and the kids embraced it because of
the 'crude' GUI). It was the 'visual presentation', as with their word
processor.

Back to those three OO languages. Both Java and C# are complete
specifications. The simple reason - one party in *CONTROL* of the
design, not a bunch of competitors without the willingness to share
ideas. Sun Micro Systems for Java and Microsoft for C# - they specified
what they wanted, obviously getting user input, and without 
interference, produced the respective languages.

Now Microsoft has the edge over others because the dotNet approach,
Visual Studio, allows them to add tools as they see fit. Tools could
never be a function of a COBOL Standard, but certainly support classes 
should have been. (I'm not familiar with Java but  I think there are 
several 'IDEs' available, so perhaps they offer a similar approach to 
the M/S Visual Studio, or could). The F/J and M/F IDEs certainly include 
the use of tools, but rather than each updating and re-inventing the 
wheel they have opted to support dotNet.

Smalltalk - it does the job but it's a bit of a mish-mash like COBOL.
Their ANSI specification was Smalltalk 80 which spelled out syntax usage
and provided the basic framework for class libraries. There is no such
thing as a Smalltalk 80 compiler. But based on that spec there are a
few/several compilers with two major leaders in the commercial world;
Dolphin has its own newsgroup and the developers appear fairly 'active'.
As a freebie there is SQUEAK, but the feeling I get is it wont cut it
for commercial applications. As Adele Goldberg wrote in another text,
"...there are various compilers and adhering to Smalltalk 80 syntax,
each vendor has produced thousands of support classes". My observation -
presumably they are using compatible method names, which in theory at
least should make it possible to switch from one Smalltalk to another.

Over and above that, in the case of Dolphin, I have noticed developers
make queries. These have been answered by the vendor with a suggested
solution from existing methods, or 'Good idea, we'll put that on our
wish-list". The items in the wish-list appear in their next Fixpack.

OO COBOL -

The J4 specification certainly provides the basic bread and butter
formats to create Classes - Factory, Object Section, instantiation etc.
To date I can't think of anything I would want added to the J4 spec,
except for what follows.

The Standard has three pre-defined objects, Null, Self, and Super

Micro Focus has an additional 'SelfClass' ( which might be clearer if it
had been named 'SelfFactory' or 'SelfStatic'); the purpose being to
allow Object Instances to invoke Factory/Static methods. Fujitsu appears 
to have something similar, 'Class of Self' etc., but you make specific
entries for those as 'Usage object reference....'.

No matter, the world isn't going to fall down if 'SelfClass' is never
part of the official language.

What we have to date is a refinement of the original OOCTG
specification, and in all probability, by team members who had knowledge
of other OO languages. Similarly the three authors I continuously refer
to, Ed Arranga/Frank Coyle and Will Price - before they tackled OO
COBOL, they each had a background of using and teaching Pascal. I may
well be wrong, but I don't get the feeling that anybody on the J4
existing team has that expertise - i.e. that they code OO COBOL for a
living. (I was coding OO COBOL for about a ten year period and I
certainly don't consider myself to be an expert).

Procedural COBOL is not an insurmountable problem to a programmer with
3-5 years experience. Throw a new procedural feature at a group, such as
John Piggott's Dynamic W/S Tables, most, if they have the patience to
read the specification, can understand it and contribute their two cents.

Not so with OO. Yes you need the syntax to get off the ground, but it
isn't the syntax that determines how it is used. It's all about
Concepts, and although somewhat overblown you also need to consider
Design Patterns which Charles recently made reference to about learning
Java. J4 is very good at dotting the 'i's' and crossing the 't's', but
that approach doesn't solve OO design.

A simple example; I suggested that the word 'callback' should be
retained, as it was used in several languages, instead of calling it an
'iterator'. Our favourite wordsmith Chuck Stevens hit the English 
language dictionaries for an accurate definition of the two words - 
conclusion, we, (J4) will go with 'iterator'. No big deal.

However, only yesterday I decided to check both words out in a
programming context :-

http://en.wikipedia.org/wiki/Iterator
http://en.wikipedia.org/wiki/Callback_(computer_science)

- they certainly appear to have a subtle, but different meaning to me, 
and a callback does include iteration. Check the two references and see 
what you think.

Collections/Dictionaries
------------------------

The most charitable thing I can write at this stage is that this feature
is ill conceived. It doesn't come even close to what Ray Obin in the
OOCTG team envisioned back in '93. Micro Focus produced EXACTLY what Ray
conveyed about class libraries. Fujitsu did the same but not quite to
the same extent, producing classes for Collections/Dictionaries only, 
i.e. a pared down 'string handling library'.

In addition to the character/array/collection handling they provide
Micro Focus have also extended their libraries to include Java and OLE
support and no doubt there are probably further classes added to Version
5.0 to deal with dotNet. (Possibly likewise with Fujitsu to operate with
dotNet).

It's rather interesting, (I can't recall the topic, nor understand the 
solution :-)), but Michael W. illustrated that COBOL was not a good fit 
for the particular problem in the M/F Forum. He illustrated it with a 
COBOL example. The result was gawdawful, not because of Michael's 
approach, but because of tables and tables of Hex values required to 
achieve the result. Hasn't been a comment here in CLC for years, but a 
phrase that used to pop-up was, 'Use the appropriate llanguage for the 
problem'.

And of course as part of their OO packages both M/F and F/J introduced
GUI modules.

Given that COBOL *did* have comprehensive support libraries then perhaps 
it could have been reasonably coded as an OO solution. Similarly, why 
reinvent the wheel for forecasting. Given that there had been a common 
class library across COBOL OO implementations, then a third party with 
real know-how on forecasting could have produced a Forecasting library 
for re-sale. Under the wraps that package would have invoked numerous 
methods from the standard COBOL libraries.

During the timespan that J4 has been figuring out TRs for Finalizer,
Collections, Dynamic W/S Tables, both M/F and F/J have moved on in the
world - dotNet.

Could we now have COBOL Class Libraries. For starters, much too late and
developers will have already looked elsewhere. It would require 
miraculous' co-operation between competitive vendors, plus of course an 
army of monkies to figure it all out. The TR for 
Collections/Dictionaries which merely specifies :-

OrderedCollection
SortedCollection
KeyedCollection
ExceptionHandling
Iterator

has taken since the year 2000 onwards and the earliest implementation,
(if their is a vendor daft enough to use it), will be 2008.

WHITHER and HOW
---------------

I took a look at the following and gave it two reads ;-

http://www.cobolstandard.info/j4/files/07-0064.doc

I agree with your paper but would question the last two paragraphs of
your EXTREME SOLUTION :-

---------------------------------------------------------------------------
10) Add a ï¿½statement of directionï¿½ to this revision indicating that it
is intended to be the LAST full revision of the COBOL Standard and that
it is intended to be placed into ï¿½maintenanceï¿½ mode soon after approval.


11) Include another ï¿½statement of directionï¿½ indicating that although
this standard is viewed as the culmination of the COBOL Standardization
process, individual implementors are expected to respond to their
changing IT environments and user needs and desires, and provide future
enhancements to the COBOL language.  (*****) When/If there appears to be
a new feature or features that have significant user demand AND that
implementors are creating multiple solutions for, SHOULD there be
ADEQUATE resources, then a future TR, Amendment, or other document may
be created.  However, this would require more development resources than
are currently available to the COBOL standardization community.
---------------------------------------------------------------------------

Paragraph 10
------------
By revision you mean the items currently outstanding, including
the TRs, presumably with an optimistic date of COBOL 2008 ?

Step 1 - which vendors on the committee are committed to implementing
perhaps 'some' of the features ?

- Acu - a 'marriage of convenience' to give Don Schricker a job
- IBM
- Micro Focus - if they don't get their pink slip first

Step 2 -

What about Acu, Hitachi, Liant(RM/COBOL), Unisys and the 'open source'
boys ?

Is it worth pursuing the outstanding list. Not too much effort to reduce
those 4.5 attendees to 3 - who is going to do what ?

Unpalatable as it may be to those J4 members still hanging in there, the
reality is, that we should call it a day and state :-

"    COBOL 2002 is the LAST COBOL Standard and includes Object
Orientation, but does not include class support libraries".

Don't like the word 'LAST' in that sentence; then use 'DEFINITIVE'. It 
says the same thing in a shrouded way just as 'surge' is a neat way of 
saying 'increase by x thousand troops'.

Note : there are two groups of OO languages - languages WITH and WITHOUT
class support libraries  - see :-
	http://en.wikipedia.org/wiki/Category:Class-based_programming_languages

Accepting the reality, is that so dreadful ? The last Smalltalk Standard
is dated 1980, and it works just fine. As Michael W. noted, Smalltalk 
lacked success because of non-existent marketing.

Paragraph 11
------------

The last part of Paragraph 11, where I have added the asterisks - I just
don't think it will work. You and I dream up a real exciting
gizmo/feature which we suggest to our compiler vendor - they embrace it
enthusiastically and depending upon its complexity it may take them 6
months or perhaps a year before they formulate the feature and add it to
their next version of their compiler - and it works smoothly. They
suggest the proven enhancement to J4. Now the fun begins. Tom, Dick
and Harry, (and Harry is from one of the vendors who has NO intention of
implementing it anyway - and it also assume there IS a third person on 
the committee called Harry !), put in their two cents, and J4 eventually
specifies or produces a TR for the feature - the chances are the only
commonality the new TR has with the original proposal - it has the same
subject title !

Above are examples, but now a real one. (Like Pete, I personally don't
see a need for a separate COBOL XML model - but nevertheless, as an
example). So Micro Focus dreamed up a new feature for XML. I haven't
read up on it. First bit of nonsense I saw tucked away in the J4 minutes 
that somebody, obviously in a fit of pique, demanded/requested that Don 
Schricker go back to CEO Tony Hill and get confirmation that Micro Focus 
would not claim copyright. (Politics has been with COBOL since Grace 
Hopper's days). What bloody nonsense - how can you possibly offer 
something to a group and as an afterthought claim copyright. Add to the 
above your own comment that although the topic is XML, there is a 
difference between the J4 spec and what Micro Focus already uses.

We know the lurkers will read this. Yes there are current and former J4
members who worked damned hard to give COBOL what it has. They got
either enmeshed in or created the internal bureaucracy, (over and above 
any bureaucracy required by ANSI), that has made COBOL enhancements so 
slow to happen. To be fair, if your number of warm bodies on the 
committee keeps on sliding down to a total of zero, how can you handle 
numerous topics anyway. Sorry folks in the days of reality TV
shows, you just haven't listened to what's going on around you, but
perhaps worse, haven't even taken notice.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
