[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Where is the holy grail...(Part II)

_48 messages · 14 participants · 2003-09_

---

### Where is the holy grail...(Part II)

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-18T12:06:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
Hello everyone,

here is part II, can you please read this article on the listed below
link and post what do you really think about this topic? Regards, Kellie.

http://www.embedded.com/1999/9908/9908feat1.htm
```

#### ↳ Re: Where is the holy grail...(Part II)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-18T16:16:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkd3qk$pie$1@news.btv.ibm.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
Puppet Girl,

<=======
Putting it all together, we're able to determine that the downLoad register
is at location 0x80000022 in physical memory. Notice how we had to look all
over the place to discover this simple fact.
=======>
I guess three/four places is "all over the place" now.
If he had a 10 module program that had a global variable and a bug hit...he
has to search all 10 modules for that...so I say NUTS to that.

<=======
Thus, rather than being helpful, information hiding is a hindrance.
=======>
Really.....at least you know that it is being changed in a controlled
validated manner....I don't implicitly trust the end users - even if the
code I write is used by my BEST friend in the whole world.....unless I
define an interface how would he know what was ok?

<=======
Wouldn't you know it-even in this simple example, there's a bug. This bug
turned out to be rather serious, and was worked on by three programmers
before I tracked it down.
=======>
Well, you could knock me down with a feather....a difficult bug? Procedural
code has never had one of them..NEVER EVER EVER..even when you exceed a
boundary condition in a separate module that is called that happened to
overwrite something that it shouldn't have - those are easy to find.

<=======
The new C++ compiler interpreted this as a requirement to actually read the
value stored at that location. This behavior is correct, since data was
declared volatile. The solution is to rewrite the operator and return a
Register, or *this.
=======>
So he wrote his code with an error? Interesting....and this is OOP's fault?
or was it the prior compiler...I forget which.....

MYTHS
<=======
Objects are needed to protect data.
In fact, this is the sole purpose of the class in my example. By
implementing the class with a private member for the pointer, the pointer
was protected. Otherwise, it's just a global variable, available for anyone
to clobber. I balance these comments with my experience. Frankly, I haven't
had problems with global variables.
=======>
I have.
<======
Objects are needed to group data and procedures
Objects are needed when implementing large programs
=======>
Cannot say I've heard these arguments before.

<======
Objects are easier to maintain.
Because information is hidden, as is the wont of OO programmers, finding
what you need to know takes more time. This fact was illustrated in the
previous example, where we had to examine four files before we understood
the assignment statement
======>
This is an anti C++ argument.

<======
The switch statement is bad. Ever read one of those introductory C++ books
that describes a graphics interface? You typically have a Shape class that's
inherited by Circle, Square, and Triangle classes. The upshot of all this is
that you can avoid those horrible switch statements by using inheritance and
polymorphism. You can also avoid pimples by chopping off your head. There's
nothing wrong with switch statements. I've never had problems with too many
switch statements. So what's your beef?
======>
Maybe he's worked on projects that should have been procedural.   Also
picking on an example to convey a principle is a cheap shot.

<======
Object-oriented programming requires more time, up front, doing design work.
Object-oriented programming requires more time to code a solution
Object-oriented programming results in a more complex solution
Object-oriented programming results in code that is more error-prone
Object-oriented programming results in increased maintenance costs
======>
Bigot.  Bad OO results in all these. Bad procedural results in all these....

AND HIS CONCLUSION IS (I THINK):

----------CHOOSE THE RIGHT TOOL FOR THE RIGHT JOB ------------

So why the OO bashing?

So how *is* your class going ?

JCE

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309181106.199c19f@posting.google.com...
> Hello everyone,
>
…[3 more quoted lines elided]…
> http://www.embedded.com/1999/9908/9908feat1.htm
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-20T01:03:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030919210327.22634.00001301@mb-m23.aol.com>`
- **References:** `<bkd3qk$pie$1@news.btv.ibm.com>`

```
"jce" defaultuser@hotmail.com 
Date: 9/18/03 3:16 PM EST
Message-id: <bkd3qk$pie$1@news.btv.ibm.com>

follows Puppet Girls lead out into cyberspace and encounters some notions to be
contentious about.  Can't blame him, and his full expressions interleaved with
quotes of the target text are good reading.  I want to make a point with one of
"jce's" interactions with the text encountered. His post read like this, I
quote it with preceding and following aol <<, >> boundaries. He starts by
quoting the target text and then adds his comment.

(snips)
<<
<======
The switch statement is bad. Ever read one of those introductory C++ books
that describes a graphics interface? You typically have a Shape class that's
inherited by Circle, Square, and Triangle classes. The upshot of all this is
that you can avoid those horrible switch statements by using inheritance and
polymorphism. You can also avoid pimples by chopping off your head. There's
nothing wrong with switch statements. I've never had problems with too many
switch statements. So what's your beef?
======>
Maybe he's worked on projects that should have been procedural.   Also
picking on an example to convey a principle is a cheap shot.
>>
(snips)

The small point I would like to add in here is an insight that can bring people
together. OOP tools automate the code generation process.

Overriding methods as of inheritance (not inheritance per se) and polymorphism
infact _DO_ eliminate the switch(), or cascaded if/elif. This is really
important for manageres to understand.  OOP tools are code generators. The
transparent code built into the OOP runtime effectively selects a correct
method. That is an efficiency because the origianator did not have to code it. 
And the maintainer does not have to maintain a switch() or a cascaded if/elif.

Java, or competent OO COBOL automates that execution branching.

It is best if we come together. This will pay dividends if we all understand
that the original programmer must 1) know what this is, and 2) want to do the
work, and 2) the maintenance programmer know what this is and want to do the
work, and 3) the business DP managers understand the characteristics of this
automation of DP work with OOP tools.

If you are against it by predisposition or by long drawn out profound
conclusion, you are not too likely to be part of the efficiency.  That is not
personal.

The virtual pointer and its array of pointers to methods is a profound
technological improvement as dramatic to all of us as ATMs are to bank
employees who once had jobs in brick and mortar facilities.

The problem with switch() statements is that we have to pay people for them. 
The idea is to save some of that money, and if the design tools are used
correctly, to create a somewhat more reliable system.

All of "jce's" comments are good. We need to understand that the decision to go
OO is always partial. A portion of economically significant systems will be
procedural (declarative and imperative).  IMHO, however, this does not preclude
the use of OOD to organize our work, and the heavy use of OOP tools to automate
data processing work.

We are in this together.  It appears to me that the most important resource,
the people, are going to be arriving with object orientation on their minds. 
If we are thinking that people will build our future systems, there is a chance
that object orientation will not only influence the code but also the
organization of the labor. 
Specifically, OOP tools generate code. Object oriented program design
eloborates layering. 

The new world is going to be one in which the original coder placed the
fundamental item of interest much deeper in code nests than prior coding
practices did. This is not an us and them issue. This is an issue of how to we
establish a vocabulary that names this problem, minimizes it at initial system
deployment, and manages it effectively during maintenance.

An opposition to polymorphism is not of much consequence. Nor is a religious
commitment to procedural lexical topology. The new automation will create
difficulties in maintenance. It is a good idea to begin to discourse on that
dispassionately. 

Best Wishes
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-20T02:18:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tNOab.13145$kg.9093@twister.tampabay.rr.com>`
- **References:** `<bkd3qk$pie$1@news.btv.ibm.com> <20030919210327.22634.00001301@mb-m23.aol.com>`

```
Comments are interspersed.

"RKRayhawk" <rkrayhawk@aol.com> wrote in message
news:20030919210327.22634.00001301@mb-m23.aol.com...
> "jce" defaultuser@hotmail.com
> Date: 9/18/03 3:16 PM EST
> Message-id: <bkd3qk$pie$1@news.btv.ibm.com>
>
> follows Puppet Girls lead out into cyberspace and encounters some notions
to be
> contentious about.  Can't blame him, and his full expressions interleaved
with
> quotes of the target text are good reading.  I want to make a point with
one of
> "jce's" interactions with the text encountered. His post read like this, I
> quote it with preceding and following aol <<, >> boundaries. He starts by
> quoting the target text and then adds his comment.
> (snips)
> <<
Contentious only because his arguments are about as considered as most of
mine when I don't have the time to put my thoughts together...which is
often.

> <======
> The switch statement is bad. Ever read one of those introductory C++ books
> that describes a graphics interface? You typically have a Shape class
that's
> inherited by Circle, Square, and Triangle classes. The upshot of all this
is
> that you can avoid those horrible switch statements by using inheritance
and
> polymorphism. You can also avoid pimples by chopping off your head.
There's
> nothing wrong with switch statements. I've never had problems with too
many
> switch statements. So what's your beef?
> ======>
…[3 more quoted lines elided]…
> (snips)
Once again my grammar has let me down.  Not sure if it read correctly.
I meant:  The Shape class with Circle, Square and Triangle classes are made
up to convey the principles of Polymorphism and inheritance.
His criticism of that is a cheap shot.  It's not a real world example - it's
like taking Cat in the Hat and saying it has no merit because it only uses
short words.

> The small point I would like to add in here is an insight that can bring
people
> together. OOP tools automate the code generation process.
Until the day comes when they are "consistent" they will prove to be
problematic.  Have you ever had an application written in a WeGenCode
package and then decided to upgrade to the WeGenCodeBetter package?  Never
as easy as you want because they still generate code for a specific runtype
or development evironment.

In the application world, a software like Visio is incredibly powerful,
useful and very proprietary (if you want to make some money reverse engineer
the vsd file) - but VERY used.

Graphical design tools - by this I mean interactive code generators - are
only now (I think) beginning to standardize import / export data in the form
of XMI and the like -  which will only help.   I've seen a very steady
improvement very quickly in these types of tools though.  Creating DADs,
MQSeries clusters, Data Interchange, Middleware management tools are
maturing very quickly. The idea of plugins for existing platforms (such as
with eclipse) is quickly creating a common interface to the tasks of coding,
designing and testing....and draggin'n'droppin

Interestingly enough, I say code generators but it is not really code
generation that is occuring but more a clever use of pre created code and
components used to create an execution context.

I still don't see coders going away - someone has to write
Linux/AIX/MVS/JVM/Device Drivers for the foreseeable future.  It's sad to
say but finding a good MVS system programmer is getting very hard (and I'm
clueless).  Kraftsman tools still make hammers guaranteed for life :-)

> Overriding methods as of inheritance (not inheritance per se) and
polymorphism
> infact _DO_ eliminate the switch(), or cascaded if/elif. This is really
> important for manageres to understand.  OOP tools are code generators. The
> transparent code built into the OOP runtime effectively selects a correct
> method. That is an efficiency because the origianator did not have to code
it.
> And the maintainer does not have to maintain a switch() or a cascaded
if/elif.
> Java, or competent OO COBOL automates that execution branching.
>
> It is best if we come together. This will pay dividends if we all
understand
> that the original programmer must 1) know what this is, and 2) want to do
the
> work, and 2) the maintenance programmer know what this is and want to do
the
> work, and 3) the business DP managers understand the characteristics of
this
> automation of DP work with OOP tools.
>
> If you are against it by predisposition or by long drawn out profound
> conclusion, you are not too likely to be part of the efficiency.  That is
not
> personal.
Switches and polymorphism as two totally separate things.
Polymorphism can remove a certain type of switch - namely branching...and
with better event models and action listeners a good gui design almost has
no switches (not like the older days with windows programming event
handlers).  The syntax of a switch will still exist for as long as we have
the if.  But I do agree with you.

I don't view the world turning to objects as a whole  - I think it's
important to understand all forms of thinking (OO or other).
Because most of the understands english - doesn't mean one couldn't get a
lot from learning Greek or Latin (I wish had learned either).

> All of "jce's" comments are good.
I doubt that.

-snip-

> An opposition to polymorphism is not of much consequence. Nor is a
religious
> commitment to procedural lexical topology. The new automation will create
> difficulties in maintenance. It is a good idea to begin to discourse on
that
> dispassionately.
I think I agree with that statement more than any other that I have read in
a newsgroup....bravo!

> Best Wishes
> Bob Rayhawk
> RKRayhawk@aol.com

JCE
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-22T15:07:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309221407.64cdefb7@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com>`

```
"jce" <defaultuser@hotmail.com> wrote in message news:<bkd3qk$pie$1@news.btv.ibm.com>...
> Puppet Girl,
> > AND HIS CONCLUSION IS (I THINK):
…[7 more quoted lines elided]…
> JCE,

I am NOT bashing OO cobol, simply trying to compare between the old and
the new to see if it is worth the efforts and the learning curve. Also, my
cobol teacher thinks that OO cobol is hyped and over sold due to the GUI
interface that made it popular. Thanks for your response. Kellie.

***

> 
> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
…[6 more quoted lines elided]…
> > http://www.embedded.com/1999/9908/9908feat1.htm
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-22T18:45:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EYKbb.1141$PT3.218088@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com>`

```
"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309221407.64cdefb7@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote in message
news:<bkd3qk$pie$1@news.btv.ibm.com>...
> > Puppet Girl,
>
…[4 more quoted lines elided]…
>

There is no GUI interface that made it (sic) popular.

OOP has nothing to do with a specific interface.

Perhaps you could tell us what amazing interface he is talking about

Donald
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 4)_

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-22T20:57:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309221957.3f5071ad@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message news:<EYKbb.1141$PT3.218088@news20.bellglobal.com>...
> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> news:41758a6b.0309221407.64cdefb7@posting.google.com...
…[9 more quoted lines elided]…
> Donald


here we go. I am just quoting my Cobol Teacher.

"OOD concept and programming became popular because of the GUI interfaces.
In fact, many computer users think that "Object" in OOD means a screen object
such as a button, an icon, or a listbox. They often talk about drag-and-drop
"objects". So, GUI has sold products. Anything associated with GUI's interfaces
was popular and sure to get market share and generate sales and get attention,
regardless of whether that association was accurate or not".

Kellie.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-23T04:27:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vYPbb.3487$eS5.1580@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com>`

```

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309221957.3f5071ad@posting.google.com...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:<EYKbb.1141$PT3.218088@news20.bellglobal.com>...
> > "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> > news:41758a6b.0309221407.64cdefb7@posting.google.com...
…[15 more quoted lines elided]…
> In fact, many computer users think that "Object" in OOD means a screen
object
> such as a button, an icon, or a listbox. They often talk about
drag-and-drop
> "objects". So, GUI has sold products. Anything associated with GUI's
interfaces
> was popular and sure to get market share and generate sales and get
attention,
> regardless of whether that association was accurate or not".

This is true in a sense.  OOD/OOP has become more popular because of
drag-and-drop; however, not in the sense of
creating interfaces and GUIs which are generally created out of visual
components and objects.
Where it has become popular is in the ability for a GUI to manage objects in
a palette or workspace to create real/true processes.
Some of the effort in coding has been reduced to dragging and dropping
components..

Take for example a tool where you can drop a PortListener onto a work
area...then you pick a ServiceHandler and drop it...then you add a
LoggingObject and a ServiceProcessObject...and then last a
PortResponder....you could now connect these items using a GUI connecters
and have built yourself a new web service with little to no code.  This is
not something unique to OO...I've been cutting and pasting and reusing
libraries for years....it's just the the OO movement has brought these new
tools more to the fore.

Why wouldn't people buy tools that automate some (not all) of the coding
effort?

JCE






>
> Kellie.
>
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 5)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-23T08:06:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mHWbb.4637$yD1.666109@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com>`

```
"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309221957.3f5071ad@posting.google.com...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:<EYKbb.1141$PT3.218088@news20.bellglobal.com>...
> > "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> > news:41758a6b.0309221407.64cdefb7@posting.google.com...
…[15 more quoted lines elided]…
> In fact, many computer users think that "Object" in OOD means a screen
object
> such as a button, an icon, or a listbox. They often talk about
drag-and-drop
> "objects". So, GUI has sold products. Anything associated with GUI's
interfaces
> was popular and sure to get market share and generate sales and get
attention,
> regardless of whether that association was accurate or not".
>
> Kellie.

Another luddite ignoramous teaching Cobol.  No wonder the language is
becoming obsolete.

Donald
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-23T17:50:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F70891B.D194DFBC@shaw.ca>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com> <mHWbb.4637$yD1.666109@news20.bellglobal.com>`

```


Donald Tees wrote:

> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> > > Perhaps you could tell us what amazing interface he is talking about
…[20 more quoted lines elided]…
> becoming obsolete.

Donald,

Think you were a bit harsh on him. As quoted I think it's a fairly accurate
statement of what OO is perceived to be - a tool to do GUIs/Web. That's not how
it started out with Simula (simulation), followed by Smalltalk - but Xerox PARC
added 'stick figures' so that young school kids could interact with graphics.
Then Steve Jobs picked up on their concept and gave us the Apple 'Lisa',
followed smartly by Bill Gates who 'half inched' the Apple concept and gave us
Windows.

If the instructor is at fault, it partially lies in another statement that
Kellie made - "Wanting auto garbage collection using PROCEDURAL programs" -  NOT
Classes !!  I don't necessarily think he is a Luddite, but unless he's thinking
outside the box beyond GUIs - then he isn't conveying to her all the other
facets of OO. For example, has he conveyed the significance of "instantiation".
Instantiate one class and you can have 10, 15, 30 or more objects using the same
code ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 7)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-23T22:08:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030923180826.29142.00000076@mb-m24.aol.com>`
- **References:** `<3F70891B.D194DFBC@shaw.ca>`

```

 "James J. Gavan" jjgavan@shaw.ca 
Date: 9/23/03 12:50 PM EST
Message-id: <3F70891B.D194DFBC@shaw.ca>


is right on it with 

<< ...
unless he's thinking
outside the box beyond GUIs - then he isn't conveying to her all the other
facets of OO. For example, has he conveyed the significance of "instantiation".
Instantiate one class and you can have 10, 15, 30 or more objects using the
same
code ?
>>

I think that our industry just does not have the term we need.  Things can be
clearer if we establish a vocabulary that keep distinct ideas separate.

Experts like Dijkstra would use the term 'recursion'.  Experts know that this
word applies to two concepts, but non-experts do not know that.

The ability to make a reference to a program with all of its parts, the data
and its operations, from within programs. Is a separate and general concept.
The experts know that. Most of us do not really clearly call forth this general
meaning when we say 'recursion', although experts can keep things straight.

There is a special case where a specific program refers to  _itself_ with
invocative semantics. (That is, it means to call itself). This is just a
special case, but is the usual meaning that folks have in mind when they say
'recursion'.

Technically, to keep folks together, the execution time fundamental capacity
for a thing to be called in this recursive manner generally by any program (by
itself, or by other programs), is call 'serially reusable'.  That was pointed
our by a recent poster (my sincerest regrets that I can not fetch that back for
proper credit). This is just one mainframe culture's parlance.

The resistance to general recursion concepts, is quite simply do to the lack of
stack features in architectures of machines with extremely wide distribution.
To get recursion to work,  _the_compiler_vendor_ has to do the work. Thus,
RECURSIVE took friggin _decades_ to arrive in COBOL.  Duh !!!!!!!!!!!!


In the same post  "James J. Gavan", ever the gentleman, is complementary of the
professor of the COBOL class, opinning that 
<<...
As quoted I think it's a fairly accurate
statement of what OO is perceived to be - a tool to do GUIs/Web. That's not how
it started out with Simula (simulation), ..
...>>

I have snipped, and resequenced the two qoutes.


With his focal point I am in complete agreement. Folks do thing that OO has to
do with GUIs. And that is too bad, because business data processing has to do
with making money and keeping money by being efficient. OO has to do with
efficiency.  

But as the grand poster from North of here glides into the Simula detail, ... I
would like to make a small point.  I think that Simula is the basic break point
for the extremely fluid specificaion of CLASSes and instantiating objects.
However, and this is small, but I think useful.

ALGOL is where major procedural languages first gained the ability to reference
other procedures on the lexical surface to any depth of recursion (general
sense).

((if I am not mistaken, LISP is even earlier, but it is not a procedural
language as I would use the term.  For historical clarity, since we have a
valued student as the major participant here, suffice it to say, LISP is very
early.))

So, I will simply koine the term, general recursion. We need a better term so
that it does not even sound like the term for the special ipsa-recursion case

If I have an OOP tool I can invent the operation AWK, and I do not need the
standards committee to approve. AWK could be on the scale of SORT.  AWK can be
thought of as a VERB (just most exactly like SORT), with variations
(alternative syntax diagrams for old codgers, method overloading for newbies).
I have automated the standards committee function out of existance. (we still
need those guys, 'though).

As an aside, the absence of standard automatic garbage collection in COBOL OO
offerings is the same old problem.  Lots of other languages have this all
figure out. What is the problem? The compiler vendor's are the problem. Serious
data processing managers should atleast say 'strike two'. But the vendors don't
care, they will get you comming and going. For anyone to claim that we do not
have enough gc algorithms for selection as effective solution in COBOL OO, is
to publish a real joke.


So in old COBOL I could CALL 'programA'.
But programA was not a verb.  In object oriented tools, I can just make it a
verb (call that a program, call it a sub-program, call it a method, call it a
procedure, or best call it an operation). But now I have _extended_ my language
so that the textual material programA pops right up onto the surface, looking
just like a reserved word, a verb.

The ability to do this inside of programA itself is a special case, a
distraction.

Type PROCEDURE-POINTER very nearly extends this capability into the flatlander
portion of COBOL, but not quite; ye vendors, they kick and they scream, ya
know. Duh !!!!

Best Wishes for All, 
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 8)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-23T22:34:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030923183404.29142.00000078@mb-m24.aol.com>`
- **References:** `<20030923180826.29142.00000076@mb-m24.aol.com>`

```

This is for all puppet afficionadoes.

http://www.cs.utexas.edu/users/EWD/transcriptions/EWD12xx/EWD1284.html

I will quote from the passage 
near  EWD1284 - 13
where  Edsger W. Dijkstra is talking about a reference that 
"...denotes activation of the procedure..."

<<To give you some idea of the significance
of this sentence, it was crucial in enabling Tony Hoare to complete the 
design of one of computing's most famous algorithms, viz. Quicksort. 
Prior to knowing ALGOL 60, he had the idea, but it remained an elusive 
vision, a dream that defied formulation, but as soon as he saw ALGOL 60 
offering him just what he needed, Quicksort materialized in all its 
glory.

>>

So, to get the full meaning you have to read the paragraph or so above that. 
But this is an historical notation from someone who was there as of the
begining of object-think. Simula definitely achieves the excellent syntax that
would be mimmicked into C++ and Java (with many further excellent
achievements). But ALGOL is where the lexical surface changed.


Maybe we should use some variation of Dijkstra's phrase, such as 'activation
denotation', we need a good term that does not ring out like 'recursion', which
has two meanings the general (which is 'activation denotation', and the special
case of self-referencing activation, or ipsa-recursion; of which quicksort is
an elegant illustration).


A more general entry point for the extraordinary material at University of
Texas at Austin can be found at
 
http://www.cs.utexas.edu/users/EWD/welcome.html


We should feel indebted not only to Dijkstra but to the hard working grad
students, et al, who are completing the transcriptsions.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 7)_

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-23T20:12:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309231912.595fab@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com> <mHWbb.4637$yD1.666109@news20.bellglobal.com> <3F70891B.D194DFBC@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3F70891B.D194DFBC@shaw.ca>...
> Donald Tees wrote:
> 
…[11 more quoted lines elided]…
> Jimmy, Calgary AB


the class we are taken right now is about procedrual cobol with GUI interfaces
and an introduction to OO cobol. Most of the focus is on learning how to code
dialogue language to design the gui boxes and all the controls on it. Also,
what you saying here for instantiation is what was explained to us as the OO
inheritance process and with it you could have objects re-useability. Kellie.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 7)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-24T07:59:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VGfcb.2517$PT3.423219@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com> <mHWbb.4637$yD1.666109@news20.bellglobal.com> <3F70891B.D194DFBC@shaw.ca>`

```
Perhaps you are right ... but the GUI / OOP dichtomony is getting rather
stale.

Donald.

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3F70891B.D194DFBC@shaw.ca...
>
>
…[10 more quoted lines elided]…
> > > "OOD concept and programming became popular because of the GUI
interfaces.
> > > In fact, many computer users think that "Object" in OOD means a screen
> > object
…[15 more quoted lines elided]…
> Think you were a bit harsh on him. As quoted I think it's a fairly
accurate
> statement of what OO is perceived to be - a tool to do GUIs/Web. That's
not how
> it started out with Simula (simulation), followed by Smalltalk - but Xerox
PARC
> added 'stick figures' so that young school kids could interact with
graphics.
> Then Steve Jobs picked up on their concept and gave us the Apple 'Lisa',
> followed smartly by Bill Gates who 'half inched' the Apple concept and
gave us
> Windows.
>
> If the instructor is at fault, it partially lies in another statement that
> Kellie made - "Wanting auto garbage collection using PROCEDURAL
programs" -  NOT
> Classes !!  I don't necessarily think he is a Luddite, but unless he's
thinking
> outside the box beyond GUIs - then he isn't conveying to her all the other
> facets of OO. For example, has he conveyed the significance of
"instantiation".
> Instantiate one class and you can have 10, 15, 30 or more objects using
the same
> code ?
>
> Jimmy, Calgary AB
>
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 5)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2003-09-25T02:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BHscb.7788$XF.3934515@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<41758a6b.0309221957.3f5071ad@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com>`

```
My problem in grasping the uniqueness of OO is finding an example that 
makes it all clear. I have recently spent days viewing code from various
downloads that probably qualify (as the Win API's seem to do).

 From my background it is clear that if the rulers of ACCOUNTING could
agree on the rules, a corporate or simple business model would be 
possible based upon those rules.  Perhaps someone knows of one. I'll bet
it's expensive, and I'll also bet that no ordinary person could 
understand the code unless they first understood the model. IMHO

I believe that some concrete examples would help a whole lot. Not all 
systems need a fancy GUI, or even paper reports these days. But the guys
and gals reading the quarterly reports do not involve themselves in 
things like OO as such. They look at the bottom line and critical ratios.

I don't believe compilers, generalized report generation, communication
utilities, etc. fall into the area of OO. Only the geeks know what's 
going on, and they keep inventing new languages and the tower grows and 
grows.  To me this subject *absent some examples beyond an I/O system"
is part of the 'confuse them, and maybe we can outsell them' free market 
way. (Not that there is anything wrong with that!) So why COBOL at all?
A lot of people seem to be missing the point. (However, most of you 
people seem to know what you are talking about!) Now if this effort to
build reusable code had as an outcome the generalization of data 
recording formats and some other unique features in the marketplace,
then progress is being made. But that wouldn't be democratic, and a lot
of people would be looking for another horse to ride.

Warren Simmons,
wsimmons5@optonline.net




KELLIE FITTON wrote:

> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message news:<EYKbb.1141$PT3.218088@news20.bellglobal.com>...
> 
…[28 more quoted lines elided]…
> Kellie.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 6)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-25T00:10:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkttbh02ffi@enews1.newsguy.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com> <EYKbb.1141$PT3.218088@news20.bellglobal.com> <41758a6b.0309221957.3f5071ad@posting.google.com> <BHscb.7788$XF.3934515@news4.srv.hcvlny.cv.net>`

```

"Warren Simmons" <wsimmons5@optonline.net> wrote in message
news:BHscb.7788$XF.3934515@news4.srv.hcvlny.cv.net...
> My problem in grasping the uniqueness of OO is finding an
example that
> makes it all clear. I have recently spent days viewing code
from various
> downloads that probably qualify (as the Win API's seem to
do).

Win API collectively refers to the exported functions from a
number of windows DLLs.  Some of the internals suggest
"objects" -- like in the GDI for instance -- but there's
nothing object-oriented about the interface.  (I'm not trying
to "bust" you here, I just thought you'd like to know that the
win api is *not* an illustration of OOP.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-23T01:29:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MlNbb.1783$eS5.1473@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <bkd3qk$pie$1@news.btv.ibm.com> <41758a6b.0309221407.64cdefb7@posting.google.com>`

```

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309221407.64cdefb7@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote in message
news:<bkd3qk$pie$1@news.btv.ibm.com>...
> > Puppet Girl,
> > > AND HIS CONCLUSION IS (I THINK):
…[12 more quoted lines elided]…
> interface that made it popular. Thanks for your response. Kellie.

I wasn't claiming that you were OO bashing....just the author of your
original link.

Sorry for the confusion :-)

I'm not sure that it is over hyped and over sold relative to
say.....hmmm...Java....


JCE
```

#### ↳ Re: Where is the holy grail...(Part II)

- **From:** docdwarf@panix.com
- **Date:** 2003-09-18T16:51:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkd5rk$hlu$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
In article <41758a6b.0309181106.199c19f@posting.google.com>,
KELLIE FITTON <KELLIEFITTON@YAHOO.COM> wrote:
>Hello everyone,
>
…[3 more quoted lines elided]…
>http://www.embedded.com/1999/9908/9908feat1.htm

Hmmmm... are you sure the author hasn't been posting to this group?  'I 
ran across an instance of something like this on an ENIAC back  in 
nine-teen-noughty-none and ever since then I've...'

DD
```

#### ↳ Re: Where is the holy grail...(Part II)

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-19T07:09:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmlsgo9elrls0c@corp.supernews.com>`
- **In-Reply-To:** `<41758a6b.0309181106.199c19f@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
KELLIE FITTON wrote:
> Hello everyone,
> 
…[3 more quoted lines elided]…
> http://www.embedded.com/1999/9908/9908feat1.htm

I'm really having trouble figuring you out...  :)

Are you here to rail against reuse and OO?  Are you taking a college
class on OO?  You've asked several questions here now, and I can't
recall you stating your feelings on these articles.  We know from your
inaugural post that you were confused about what value OO can bring.
It's fine to stimulate discussion, but it's good to participate as well.
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-19T11:58:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309191058.68219883@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <vmlsgo9elrls0c@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote in message news:<vmlsgo9elrls0c@corp.supernews.com>...
> KELLIE FITTON wrote:
 I'm really having trouble figuring you out...  :)

I am trying to learn computer programming using cobol language, and
been reading a lot of books and articles on the internet regarding the
new OO cobol vs the old procedrual cobol. Kellie.

> 
> 
…[9 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-19T23:31:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmnm0qikjo0e4f@corp.supernews.com>`
- **In-Reply-To:** `<41758a6b.0309191058.68219883@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <vmlsgo9elrls0c@corp.supernews.com> <41758a6b.0309191058.68219883@posting.google.com>`

```
KELLIE FITTON wrote:

> LX-i <LXi0007@Netscape.net> wrote in message news:<vmlsgo9elrls0c@corp.supernews.com>...
> 
…[6 more quoted lines elided]…
> new OO cobol vs the old procedrual cobol. Kellie.

Ah - there's such a thing as information overload.  That may be what 
you're experiencing.  :)  I'm sure you'll get there if you persevere - 
in the end, it's all just 1's and 0's anyway.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-21T14:28:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EAibb.152333$3o3.10889627@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <vmlsgo9elrls0c@corp.supernews.com> <41758a6b.0309191058.68219883@posting.google.com> <vmnm0qikjo0e4f@corp.supernews.com>`

```

"LX-i" <LXi0007@Netscape.net> wrote in message
news:vmnm0qikjo0e4f@corp.supernews.com...
|
| in the end, it's all just 1's and 0's anyway.

Until they perfect Quantum Computing.
```

#### ↳ Re: Where is the holy grail...(Part II)

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-09-19T11:34:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hmFab.72500$PD3.4757600@nnrp1.uunet.ca>`
- **In-Reply-To:** `<41758a6b.0309181106.199c19f@posting.google.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
KELLIE FITTON wrote:
> Hello everyone,
> 
> here is part II, can you please read this article on the listed below
> link and post what do you really think about this topic? Regards, Kellie.
>
[snip]

Like any Big Idea, OO is ripe for abuse.  Blindly following the tenets 
of OO design, or applying it in inappropriate ways is obviously not a 
good idea.

Of course, the problem with Big Ideas is that there is a lot of opinion 
on what is "inappropriate".

Having cut my teeth on functional coding, I have a natural leaning 
toward solving problems that way first, and only reaching for objects 
when I'm sure there is no other way.  It all depends on the scope and 
lifespan of the project, as well as how "appropriate" I feel OO is to 
the problem.

Now, I come from a background of maintenance developer.  I usually 
maintain other people's code.  This means I'm expose to a lot of legacy 
code, written in a variety of languages.  I've seen some real neat uses 
for OO which allows for easy expansion, reuse and maintenance of big 
product suites.  I've also hacked at seriously scary C code, where a 
goto was the best way to get out of a snarl of several years of 
maintainence cruft without.

Maintence coders often like to minimize changes to code between 
revisions (from the point of view of archiving changes) so that 
regressions (which are always a risk) are easier to find.

Anyway, to stay /somewhat/ on topic, I found that the main thrust of the 
article in question is knowing when OO is appropriate, especially in the 
context of embedded systems programming.  Having done a bit of embedded 
work myself, I tend to agree with *some* of his assertions.  I recognize 
many of the isssues I've run into as a maintenance coder in the "Myths 
and facts" section!

If the article was meant to present the argument that embedded systems 
coders often need to solve problems where OO may not be strongest and 
might even get in the way, I mostly agree (with the caveats and context 
stated above).  Much of what OO brings to my particular bag of tricks is 
just not appropriate to embedded systems programming (or systems 
programming, for that matter).

I'd probably reach for C or Forth, with some hand-tuned assembler for 
speed or size, for anything that was truly embedded.  However, I 
cheerfully admit that there might be some hot coder out there who can 
bury me with OO on the same project.  I can't help but feel there is a 
sweet-spot where OO just can't compete with good functional design.

Ok, roll me in flame-bait and toss me to the trolls.  I've dared to 
state an opinion on USENET!

-- cm
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** docdwarf@panix.com
- **Date:** 2003-09-19T20:07:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkg5nd$1ks$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <hmFab.72500$PD3.4757600@nnrp1.uunet.ca>`

```
In article <hmFab.72500$PD3.4757600@nnrp1.uunet.ca>,
clvrmnky  <clvrmnky@coldmail.com.invalid> wrote:
>KELLIE FITTON wrote:
>> Hello everyone,
…[8 more quoted lines elided]…
>good idea.

Oh, I *cannot* resist... you realise, of course, that you might do well to
hire someone to start your car for you if you substitute 'OO' with 'GO
TO-less' in that statement.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-20T11:25:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <hmFab.72500$PD3.4757600@nnrp1.uunet.ca> <bkg5nd$1ks$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bkg5nd$1ks$1@panix1.panix.com...
| In article <hmFab.72500$PD3.4757600@nnrp1.uunet.ca>,
| clvrmnky  <clvrmnky@coldmail.com.invalid> wrote:
…[4 more quoted lines elided]…
| >> link and post what do you really think about this topic? Regards,
Kellie.
| >>
| >[snip]
…[8 more quoted lines elided]…
|

GO TO-less is not an objective, it's a result.

There are good and bad practitioners in any discipline.

Do you know of any restructuring facilities that convert structured code to
"GO TO" code?
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-09-20T13:46:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GRkwP4B5wEb$Ewc6@ld50macca.demon.co.uk>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <hmFab.72500$PD3.4757600@nnrp1.uunet.ca> <bkg5nd$1ks$1@panix1.panix.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>`

```
In message 
<XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>, Harley 
<dennis.harleyNoSpam@worldnet.att.net> writes
>
>GO TO-less is not an objective, it's a result.

Before it can be a result it must be an objective, unless it is achieved 
as a bye-product of some other process. IIRC, Michael Jackson (gloveless 
guru of structured programming) states as an objective, but fails to 
achieve in his examples, goto-less code.

>
>There are good and bad practitioners in any discipline.
>
>Do you know of any restructuring facilities that convert structured code to
>"GO TO" code?

Yes, I saw an example of code produced by an IBM provided utility that 
purportedly restructured spaghetti code. It produced code that I would, 
as a trainee, have been ashamed to produce. It contained GOTOs galore.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 5)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-20T15:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030920114402.26244.00000116@mb-m04.aol.com>`
- **References:** `<GRkwP4B5wEb$Ewc6@ld50macca.demon.co.uk>`

```


Cup cake for excellent phrasing  goes to 

Alistair Maclean alistair@ld50macca.demon.co.uk 
Date: 9/20/03 7:46 AM EST
Message-id: <GRkwP4B5wEb$Ewc6@ld50macca.demon.co.uk>


for this

<<
Michael Jackson (gloveless 
guru of structured programming)
>>

Nice touch!
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-20T09:26:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkhkit$a0c$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <hmFab.72500$PD3.4757600@nnrp1.uunet.ca> <bkg5nd$1ks$1@panix1.panix.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>,
Harley <dennis.harleyNoSpam@worldnet.att.net> wrote:
>
><docdwarf@panix.com> wrote in message news:bkg5nd$1ks$1@panix1.panix.com...
…[19 more quoted lines elided]…
>GO TO-less is not an objective, it's a result.

That's an interesting assertion and one which contradicts programmers I
know who have said it is their objective to make their programs
GO-TO-less.  As I interpret English 'objective' requires intention
('something towards which effort is directed') and a 'result' is simply a
matter of cause ('to proceed or arise as a consequence') (both definitions
from http://www.m-w.com); if this interpretation is correct then *all* 
programming - an intentional activity, no matter *what* some code everyone 
might have seen looks like - is 'objective' activity.

Might you be so kind as to post the reasoning which you have used to 
conclude otherwise?

>
>There are good and bad practitioners in any discipline.

This was never contested; this also can be used to support the conclusion 
that there good practioners of GO TO-ful programming.

>
>Do you know of any restructuring facilities that convert structured code to
>"GO TO" code?

I do not know of much of a market for such things no... but market 
conditions, being a result of human activity, can be seen as *anything* 
but logical.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-22T11:16:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <hmFab.72500$PD3.4757600@nnrp1.uunet.ca> <bkg5nd$1ks$1@panix1.panix.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net> <bkhkit$a0c$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bkhkit$a0c$1@panix1.panix.com...
| In article <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>,
| Harley <dennis.harleyNoSpam@worldnet.att.net> wrote:
| >
| ><docdwarf@panix.com> wrote in message
news:bkg5nd$1ks$1@panix1.panix.com...
| >| In article <hmFab.72500$PD3.4757600@nnrp1.uunet.ca>,
| >| clvrmnky  <clvrmnky@coldmail.com.invalid> wrote:
…[3 more quoted lines elided]…
| >| >> here is part II, can you please read this article on the listed
below
| >| >> link and post what do you really think about this topic? Regards,
Kellie.
| >| >>
| >| >[snip]
…[5 more quoted lines elided]…
| >| Oh, I *cannot* resist... you realise, of course, that you might do well
to
| >| hire someone to start your car for you if you substitute 'OO' with 'GO
| >| TO-less' in that statement.
…[6 more quoted lines elided]…
| GO-TO-less.

Maybe they don't have a full understanding of Structured Coding.

|As I interpret English 'objective' requires intention
| ('something towards which effort is directed') and a 'result' is simply a
…[7 more quoted lines elided]…
|

It's the mindset.
GO TO, structured, OO, all have a mindset associated with them.
Once you think in with a structured coding mindset, your code becomes
goto-less.
You don't think about the goto.
Initially you reject structures that require the go to, but after you master
the methodology,  goto-less isn't an issue.

Structure programming goes far beyond being GOTO-less.
A GOTO-less program isn't necessarily a good structured program.

| >
| >There are good and bad practitioners in any discipline.
|
| This was never contested; this also can be used to support the conclusion
| that there good practioners of GO TO-ful programming.

Maybe, but when I'm offered additional resources, I check the work product
of the person. Since I'm interested in producing a consistent product, I
will reject GOTO-ful practicioners.
I'm sure GOTO-ful practicioners would reject me also.

|
| >
| >Do you know of any restructuring facilities that convert structured code
to
| >"GO TO" code?
|
…[3 more quoted lines elided]…
|

You could write one.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-22T07:54:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkmnte$mrc$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net> <bkhkit$a0c$1@panix1.panix.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net>,
Harley <dennis.harleyNoSpam@worldnet.att.net> wrote:
>
><docdwarf@panix.com> wrote in message news:bkhkit$a0c$1@panix1.panix.com...
…[29 more quoted lines elided]…
>Maybe they don't have a full understanding of Structured Coding.

I barely know what *I* understand, let alone anyone else; what is apparent 
is that their use of English appears to be completely appropriate.

>
>|As I interpret English 'objective' requires intention
…[10 more quoted lines elided]…
>It's the mindset.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>GO TO, structured, OO, all have a mindset associated with them.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>Once you think in with a structured coding mindset, your code becomes
>goto-less.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>You don't think about the goto.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>Initially you reject structures that require the go to, but after you master
>the methodology,  goto-less isn't an issue.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>
>Structure programming goes far beyond being GOTO-less.

This is an assertion, it is not reasoning... sounds kinda Zen, dude.

>A GOTO-less program isn't necessarily a good structured program.

This was never questioned.

A pattern is beginning to emerge here... you seem to have redefined words 
to use them in a Humpty-Dumpty style of 'what I want them to mean' and 
when asked for reason you respond with assertions about unquantifiable 
matters such as 'mindset'... dude.

This makes what I was taught to call 'rational discourse' a bit... 
difficult.

>
>| >
…[7 more quoted lines elided]…
>will reject GOTO-ful practicioners.

What you do was not questioned; what was pointed out was that your 
arguments work as much for you as against you (and as shown above you have 
admitted this possibility.

>I'm sure GOTO-ful practicioners would reject me also.

This was never questioned.

>
>|
…[9 more quoted lines elided]…
>You could write one.

Many things could be done... this was never questioned.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-09-22T13:44:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71XVkA96ub$Ew9D@ld50macca.demon.co.uk>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net> <bkhkit$a0c$1@panix1.panix.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com>`

```
In message <bkmnte$mrc$1@panix1.panix.com>, docdwarf@panix.com writes
>A pattern is beginning to emerge here... you seem to have redefined words
>to use them in a Humpty-Dumpty style of 'what I want them to mean' and
…[3 more quoted lines elided]…
>

Didn't Winston Churchill also say that a word has the meaning that he 
attributes to it, nothing more, nothing less?
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 8)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-22T18:46:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rZKbb.1142$PT3.218141@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net> <bkhkit$a0c$1@panix1.panix.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk>`

```
"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:b71XVkA96ub$Ew9D@ld50macca.demon.co.uk...
> In message <bkmnte$mrc$1@panix1.panix.com>, docdwarf@panix.com writes
> >A pattern is beginning to emerge here... you seem to have redefined words
…[8 more quoted lines elided]…
>

No, that was the caterpiller in Alice Through the Looking Glass.

Donald


> -- 
> Alistair Maclean
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 9)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-22T18:48:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z%Kbb.1144$PT3.218611@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net> <bkhkit$a0c$1@panix1.panix.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <rZKbb.1142$PT3.218141@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote in >
> No, that was the caterpiller in Alice Through the Looking Glass.
>
> Donald
>
Or was it Alice in Wonderland?

Donald
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-22T22:04:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bko9mt$asl$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <rZKbb.1142$PT3.218141@news20.bellglobal.com> <Z%Kbb.1144$PT3.218611@news20.bellglobal.com>`

```
In article <Z%Kbb.1144$PT3.218611@news20.bellglobal.com>,
Donald Tees <Donald_Tees@sympatico.ca> wrote:
>"Donald Tees" <Donald_Tees@sympatico.ca> wrote in >
>> No, that was the caterpiller in Alice Through the Looking Glass.
…[3 more quoted lines elided]…
>Or was it Alice in Wonderland?

The latter, and Humpty Dumpty rather than the Caterpillar.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 11)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-23T08:08:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TJWbb.4639$yD1.666692@news20.bellglobal.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <rZKbb.1142$PT3.218141@news20.bellglobal.com> <Z%Kbb.1144$PT3.218611@news20.bellglobal.com> <bko9mt$asl$1@panix1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:bko9mt$asl$1@panix1.panix.com...
> In article <Z%Kbb.1144$PT3.218611@news20.bellglobal.com>,
> Donald Tees <Donald_Tees@sympatico.ca> wrote:
…[10 more quoted lines elided]…
>
I can never keep characters straight after a couple tokes.

Donald
;<)
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-23T08:49:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkpfhn$1kv$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <Z%Kbb.1144$PT3.218611@news20.bellglobal.com> <bko9mt$asl$1@panix1.panix.com> <TJWbb.4639$yD1.666692@news20.bellglobal.com>`

```
In article <TJWbb.4639$yD1.666692@news20.bellglobal.com>,
Donald Tees <Donald_Tees@sympatico.ca> wrote:
><docdwarf@panix.com> wrote in message news:bko9mt$asl$1@panix1.panix.com...
>> In article <Z%Kbb.1144$PT3.218611@news20.bellglobal.com>,
…[11 more quoted lines elided]…
>I can never keep characters straight after a couple tokes.

If 'keeping straight' is the goal then perhaps toking is best avoided, 
aye.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-22T22:01:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bko9h3$aa3$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk>`

```
In article <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In message <bkmnte$mrc$1@panix1.panix.com>, docdwarf@panix.com writes
>>A pattern is beginning to emerge here... you seem to have redefined words
…[7 more quoted lines elided]…
>attributes to it, nothing more, nothing less?

If he had done so then he might have said it with knowledge of the
quotation to which I refer and which pre-dated him: 'When I use a word,'
Humpty Dumpty said, in a rather scornful tone, 'it means just what I
choose it to mean--neither more nor less.' (Written by The Reverend 
Charles Lutwidge Dodgson under the psuedonym Lewis Carroll in the book 
'Alice's Adventures in Wonderland', 1865)

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-23T02:47:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F6FB45B.720FA8A1@shaw.ca>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <bko9h3$aa3$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:

> In article <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk>,
> Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
…[18 more quoted lines elided]…
> DD

Just some trivia about the Rev. D. At one time he lived in a house in the
'Mews' (?) close to Guildford Castle, Surrey. Purportedly, he saw the first
'Alice' at a seaside resort, Llandudno (pronounced G'KLAN-DUD-KNOW), in N.
Wales, (geographically, very close to Liverpool). It has two beaches, being a
peninsula - the West (?) Beach sports a fountain, the centre piece of which is
the White Rabbit. Needless to say their most popular sale of seaside postcards
are views of the Rabbit and fountain.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-23T06:15:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkp6g2$e7n$1@panix1.panix.com>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <bko9h3$aa3$1@panix1.panix.com> <3F6FB45B.720FA8A1@shaw.ca>`

```
In article <3F6FB45B.720FA8A1@shaw.ca>, James J. Gavan <jjgavan@shaw.ca> wrote:
>
>
…[30 more quoted lines elided]…
>are views of the Rabbit and fountain.

I was not familiar with the geography involved, Mr Gavan, but when I was 
studying Ancient Greek at my alma mater decades back I was informed that 
Alice Liddell's father, Henry George Liddell, was Robert Scott's co-author 
for the definitive Liddell & Scott's Greek Lexicon.

(As with many reference books this came in two forms, a smaller one for 
daily use and a Great Big Hulking One that lived in the library... the 
former usually referred to as the Little Liddell and the latter as the 
Great Scott.)

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T15:44:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkse4i$chs$1@peabody.colorado.edu>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <WRAbb.154348$3o3.10988937@bgtnsc05-news.ops.worldnet.att.net> <bkmnte$mrc$1@panix1.panix.com> <b71XVkA96ub$Ew9D@ld50macca.demon.co.uk> <bko9h3$aa3$1@panix1.panix.com>`

```

On 22-Sep-2003, docdwarf@panix.com wrote:

> If he had done so then he might have said it with knowledge of the
> quotation to which I refer and which pre-dated him: 'When I use a word,'
…[3 more quoted lines elided]…
> 'Alice's Adventures in Wonderland', 1865)

The question is, which is to be master.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-20T15:39:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030920113935.26244.00000114@mb-m04.aol.com>`
- **References:** `<XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" dennis.harleyNoSpam@worldnet.att.net 
Date: 9/20/03 6:25 AM EST
Message-id: <XOWab.146246$0v4.10809883@bgtnsc04-news.ops.worldnet.att.net>


writes

<<
Do you know of any restructuring facilities that convert structured code to
"GO TO" code?

>>

Yes, that is called a compiler ;-).
```

#### ↳ Re: Where is the holy grail...(Part II)

- **From:** "RH" <nospam@hotmail.com>
- **Date:** 2003-09-24T02:49:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%C7cb.3128$AC3.160493@news2.telusplanet.net>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com>`

```
I think it comes down to what he says here:

I'm not advocating that we never use objects. I do advocate their use when
they provide new functionality, or the objects have been proven correct.

Objects derived from the Standard Template Library have been used by
thousands of programmers, and tested millions of times. This fact
effectively removes them from consideration when bug-tracing.

This is the way it's supposed to be.  Just like a compiler should never have
a bug in it.  Or a major class like "String" should never have a bug in it.
But... sometimes you find them.  How is that different from finding a bug in
a major C function or major COBOL subroutine?

Polymorphism/Encapsulation/Inheritance can have their down side... but it's
also a boon when done correctly.  The same can be said for procedural code.

The following article hints that people still hold technology/tools
responsible for their problems.  We don't need idiot-proof technology/tools,
we need better  developers... especially when they are developing
base-classes or class-libraries:

http://inquirerinside.com/?article=11651




"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309181106.199c19f@posting.google.com...
> Hello everyone,
>
…[3 more quoted lines elided]…
> http://www.embedded.com/1999/9908/9908feat1.htm
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-24T16:13:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030924121356.12528.00000110@mb-m04.aol.com>`
- **References:** `<%C7cb.3128$AC3.160493@news2.telusplanet.net>`

```
"RH" cites an article and comments that the


<<...
article hints that people still hold technology/tools
responsible for their problems.  We don't need idiot-proof technology/tools,
we need better  developers... especially when they are developing
base-classes or class-libraries:

>>

That is true. And it is a serious challenge to define the personnel
requirements from a business stand-point for the class & lib developers. As
well, it is tough to define the qualifications for someone to be brought in at
a later mature stage of maintenance and support, which individual will manage
the class collection and any repositories.

This kind of stuff will lead to some distinction in the staffing strategies, I
would guess. This is really a revisit of the fundamental issue of how to manage
legacy code. Doing the design of the classes and libraries is an initial part,
_and_ an ongoing part of the legacy management.

It is just that if OOP tools work, then an effect will be that we _do_ reuse a
larger amount of code. Can we handle that change? This is really an unsung
tune. The change has to be in management not the code or the tools.

My sense is that because the current facts on the ground are interoperability
rather than full commitment to new development methods, for a considerable
intermediate period managing the common code base (there's a phrase), is going
to be a thankless job.

Looked at from another perspective; when we see the industry begin to staff
this class design, and common code base area of responsibility as a distinct
job category (not just an add-on for the recruiters to talk down pay), then we
will be seeing the actual acceptance of OOD concepts as part of DP management.

I agree with "RH",  'we need better  developers'. But my personal sense of this
is that we need them better recognized, and we need them better supported. The
OOD strategies involve new organizational commitments.

Maybe we should spin it positive. We need Common Base Architects (CBAs) and
Common Base Enablers (CBEs for maintenance, debugging and for further
profitable exploitation of existing solutions).

These people would not necessarily be coders.
And we should not call these people 'administrators' lest they sleep so much
like the DBAs. 

The word Common in these titles should map well to businesses using COBOL
oriented tools.
Now there's a phrase, .. COBOLOTs.

To some extent CBAs and CBEs might be senior resources, but I think that is not
necessarily the case as tools evolve, and a shop collects numerous classes,
there could be a number of roles, not always requiring extreme depth of
experience.

CBAs and CBEs would not be analyst in the more traditional sense. They would be
involved in the technical aspects of systems analysis, but would not need as
much indepth application understanding as a traditional application project
analyst. 

For these comments to be correct we will have to begin a very long industry
process of standardizing classes so that they, infact, can be understood
without extraordinary application knowledge. That is not going to be easy.

My definitions here, then, are consciously circular. The CBAs and CBEs could
function with shallow application knowledge if the class collections contain
easily perceived individual entries (I am avoiding the OOP buzwords, and
steering away from 'component' with my word entries).

If such a strategy is not taken, then our need for 
'better  developers' will be disbursed to the application projects ... and
there we will have a statistical probability of either the absence of the
requisite talent, or lack of commitment from the project manager.

Thus for the long term benefits of potential re-use of code that will certainly
be much more modularized under the force of emerging technologies, the
commitment must come from very high in an organization.

At his time, DBAs are considered as part of the systems programming staff, by
and large. They do not function as part of the application group in many
instances.  I think that we need closer connections between the CBA/CBE group
and the applications.

I think also that mentoring and training from CBA/CBE staff will now be a
fundamental and repeating function. To use the stuff in those libraries, you
have to learn what they are and how to use them. CBEs in particular will really
be involved in a continuous technology transfer.

Now there's a phrase; continuous technology transfer - the work of Common Base
Enablers that encourages new use of proven proprietary information technology. 

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com


P.S. Gosh, Kellie, did you start all this?
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-24T15:00:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309241400.2736301b@posting.google.com>`
- **References:** `<%C7cb.3128$AC3.160493@news2.telusplanet.net> <20030924121356.12528.00000110@mb-m04.aol.com>`

```
rkrayhawk@aol.com (RKRayhawk) wrote in message news:<20030924121356.12528.00000110@mb-m04.aol.com>...
> "RH" cites an article and comments that the
> 
> 
>  
> P.S. Gosh, Kellie, did you start all this?


sorry bob, I must admitted I did start all this. by the way, great
point of view. regards, Kellie.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "RH" <nospam@hotmail.com>
- **Date:** 2003-09-25T01:58:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sZrcb.20551$H86.277087@news1.telusplanet.net>`
- **References:** `<%C7cb.3128$AC3.160493@news2.telusplanet.net> <20030924121356.12528.00000110@mb-m04.aol.com>`

```

All great points :)

Although I have a long COBOL background, all of my OO has been in C++,
Delphi and Java.  So I have to come at it from that angle...

> Looked at from another perspective; when we see the industry begin to
staff
> this class design, and common code base area of responsibility as a
distinct
> job category (not just an add-on for the recruiters to talk down pay),
then we
> will be seeing the actual acceptance of OOD concepts as part of DP
management.

> Thus for the long term benefits of potential re-use of code that will
certainly
> be much more modularized under the force of emerging technologies, the
> commitment must come from very high in an organization.

> Maybe we should spin it positive. We need Common Base Architects (CBAs)
and
> Common Base Enablers (CBEs for maintenance, debugging and for further
> profitable exploitation of existing solutions).
>

This is certainly key.  I mentioned this in my post below (H. Brazee).  It
takes time (ie: $) to do OOD properly -- to get the big rewards.  That
requires proper OO architecture in the design phase, which can be handed
down to the developers via UML diagrams or whatnot, and then to applications
support (CBE).

If you go to http://suned.sun.com/US/certification/java/index.html you'll
notice that they have a "Developer" cert for J2SE and an "Architect" cert
for J2EE.  Both these would fall into your definition of "CBA".

I know for a fact that suggesting an "Architect" to a COBOL shop doesn't go
over well.  (At least it didn't with my current client).  But if they're
going to use OO (regardless of language), they need to do their homework and
admit that there is another mouth to feed (architect) -- at least
temporarily.  Even if they threw a Business Analyst, Senior Systems Analyst
and Senior Developer together, they still may not come up with the proper
plan.  In fact, I may be able to substantiate this claim in the next 6
months ;)

> To some extent CBAs and CBEs might be senior resources, but I think that
is not
> necessarily the case as tools evolve, and a shop collects numerous
classes,
> there could be a number of roles, not always requiring extreme depth of
> experience.
>
> CBAs and CBEs would not be analyst in the more traditional sense. They
would be
> involved in the technical aspects of systems analysis, but would not need
as
> much indepth application understanding as a traditional application
project
> analyst.
>

This is an interesting point, because IMO applications support personnel
need to up their game a bit in certain OO environments... to the point of
touching the developer's realm.  Not because they can break code... but
because they can make code breakable.  Fi: they don't use a Datasource
class, and instead go to a data-source directly.  On the other hand, look at
a language like PERL5 which is highly module based, and takes care of many
tasks which aren't included in many class libraries -- or are included as
add-ons (ex: JavaMail).  Maybe I'm setting the bar too high?

> At his time, DBAs are considered as part of the systems programming staff,
by
> and large. They do not function as part of the application group in many
> instances.  I think that we need closer connections between the CBA/CBE
group
> and the applications.

Yes!  Right now all my applications need to be sanctioned by a DBA/SysAdmin
before rollout.  This particular DBA has a software-engineering degree.  And
he knows when apps are not written to the best-practice credo (OO or
otherwise).  This mentality eventually gets pushed back to the Project &
Development Manager, who must then re-evaluate why a project can't go
forward.  It's always enlightening.
```

##### ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T20:28:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksuoq$sl8$1@peabody.colorado.edu>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <%C7cb.3128$AC3.160493@news2.telusplanet.net>`

```

On 23-Sep-2003, "RH" <nospam@hotmail.com> wrote:

> This is the way it's supposed to be.  Just like a compiler should never have
> a bug in it.  Or a major class like "String" should never have a bug in it.
> But... sometimes you find them.  How is that different from finding a bug in
> a major C function or major COBOL subroutine?

I found one in "unstring" once (Univac 9030).

Reusing the Standard Template Library is very much like trusting the compiler.
But as far as that goes, it is like having a compiler, with more complicated
verbs than most and a huge vocabulary.    Actually "clause' is a better term.

To me the best part about this library is that I can pick the language that is
most suited for my program, and the library is part of the language.

But that's not how OO is sold.   OO is sold with the concept that I create my
own objects - business rules objects.    These objects are subject to being
changed, not so much because of bugs, but because of changing conditions.   That
is the hardest thing to sell in environments like the ones I have worked in.  
Changing an object that is used by lots of programs either requires a lot of
trust or extensive testing.   That means money.

Now if I limit the object to only a couple of programs, that is a different
matter.   I often see when that would be useful, and the cost of testing a
change is manageable.   But the trade off is that this is limiting its
reusability.
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** "RH" <nospam@hotmail.com>
- **Date:** 2003-09-25T01:01:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C7rcb.20516$H86.271215@news1.telusplanet.net>`
- **References:** `<41758a6b.0309181106.199c19f@posting.google.com> <%C7cb.3128$AC3.160493@news2.telusplanet.net> <bksuoq$sl8$1@peabody.colorado.edu>`

```

>
> I found one in "unstring" once (Univac 9030).
>
I actually found a bug in a Unisys COBOL compiler once ;)

> But that's not how OO is sold.   OO is sold with the concept that I create
my
> own objects - business rules objects.    These objects are subject to
being
> changed, not so much because of bugs, but because of changing conditions.
That
> is the hardest thing to sell in environments like the ones I have worked
in.
> Changing an object that is used by lots of programs either requires a lot
of
> trust or extensive testing.   That means money.
>
> Now if I limit the object to only a couple of programs, that is a
different
> matter.   I often see when that would be useful, and the cost of testing a
> change is manageable.   But the trade off is that this is limiting its
> reusability.

This is entirely true, and I'm actually in this situation right now with my
current client.  Moving to a Java/Oracle environment, they see huge benefits
in code re-use (so do I).  But I don't think the management really
understands how important "best practice" is, or champion it.  Specifically
in regards to inheritence, which is subject to the "breaking code"
phenomenon.

Joshua Bloch has an interesting take on it in his book Effective JavaT:
Programming Language Guide

"...it should be apparent that designing a class for inheritance places
substantial limitations on the class. This is not a decision to be
undertaken lightly. There are some situations where it is clearly the right
thing to do, such as abstract classes, including skeletal implementations of
interfaces. There are other situations where it is clearly the wrong thing
to do, such as immutable classes.
But what about ordinary concrete classes? Traditionally, they are neither
final nor designed and documented for subclassing, but this state of affairs
is dangerous. Each time a change is made in such a class, there is a chance
that client classes that extend the class will break. This is not just a
theoretical problem. It is not uncommon to receive subclassing-related bug
reports after modifying the internals of a nonfinal concrete class that was
not designed and documented for inheritance.

The best solution to this problem is to prohibit subclassing in classes that
are not designed and documented to be safely subclassed."

On top of that, there are occasions where APIs are hard to nail down over
the long run.  I worked with an OpenGL library for 2 years.  And I was quite
certain that many of the classes I was using would rarely, if ever change...
unless the laws of mathematics or physics changed.  A ray is a ray.  A plane
is a plane.  Etc etc.  I wasn't too worried about my 3D engine breaking down
the road.  Furthermore, changes to the underlying API were usually additions
that you could take or leave.  A good example being the inclusion of
pixel/shader routines in both OpenGL and DX9, which are currently all the
rage.  There is a progressive "move forward" in these cases.

From a business perspective it's a bit different.  I've seen unions, for
example, come up with contract clauses that can create code-change
nightmares.  That's certainly going to affect code more than the scenario
above...  I guess the question is -- how much can you abstract a business
process?
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part II)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-26T02:58:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030925225804.24044.00000162@mb-m14.aol.com>`
- **References:** `<bksuoq$sl8$1@peabody.colorado.edu>`

```

"Howard Brazee" howard@brazee.net 
Date: 9/24/03 3:28 PM EST
Message-id: <bksuoq$sl8$1@peabody.colorado.edu>

Comments on reluctance to change a frequently used module, and state that ..

<<
Now if I limit the object to only a couple of programs, that is a different
matter.   I often see when that would be useful, and the cost of testing a
change is manageable.   But the trade off is that this is limiting its
reusability.

>>

This is going to just keep happening. OOD does not do away with the trade-offs.
 And it should not be sold to anyone as though it could. The trade-offs still
need to be balanced. 

Consider a date routine, a fundamental routine. Probably alot of folks in the
shop use it.  Knowing what we know you would not consider changing it without
some thought.  And it will be the case that sometimes we will make copies and
isolate our change, atleast for a while.

I think that OOD's honest promise is 'more reusablity'. By my own point of view
is that automating the technical workers is a lot more of a cost factor than
code re-use.

But in Howard's post is the kernel of truth that we really need to get to to
defuse these kinds of important discussion of any potential for division.  The
matter is probably a mathematical principle of some kind.

It is like that the more a piece of code is re-used in a shop, the more money
we are making from the work that went into abstracting it and refining it. But
in parallel with this increased value is an ever increasing reluctance to ever
touch it again. 

So there is a part of the OOD philosophy that is contradicted here. And it
really is structured development methodologies in general that reach a point
where it turns back on itself.

We modularize for more than one reason.  Getting re-use is an economic
efficiency. Distinctly, establishing a single point of expression that can be
changed once and function differently everywhere is efficiency also; but it is
different managable feature of our work place.

Change once, and modify all uses is the part that has the growing reluctance.
The risk of changing code increases as the number of uses increase. That is a
very important economic principle.  We will save money if we do not cause
expensive damage. Re-usable code is a multiplier waiting to explode, which tend
to not explode if you leave them alone.

But the dichotomy is clear enough, a reluctance to change re-usable code is not
a reluctance to  keep re-using code in all of its current places. 

So there are two tenets in there (and it is structured programming not just OOD
concepts), code re-use and more code re-use are positive. One development
effort, then more and more repeating mechanism delivering return on the
investment; ever growing positive.. Separately, single piece of code, single
place to change, an efficiency but it has a factor that grows and grows
negative. 

Changing re-usable code is not the same as re-using re-usable code yet again. 
So even if you have been reluctant to change common code, and even replicated
it and made a variation ... does not at all mean don't re-use that original
re-usable code on yet another occassion when its characteristics seem just
fine.

But willingness to change re-usable code should have an inverse relation to the
number of uses of that code. 

Yet we are dealling with two different tenets: re-use and the efficiency of
change once to modify all users.

The fact that I use a date routine many thousands of times does not mean I
should be afraid to use it in yet another place. But those many uses do lead me
to be reluctant to change it.  

The reluctance to change common code is however utterly objective, and not
subjective. During Y2K work, it is absolutely certain that some businesses got
profound payback for having committed long before awareness of an approaching
event threshold to common routines to handle date manipulations.

An unsung song here is that Y2K was successful largely because of a culture of
code re-use that readily accepted modularization and further modularization of
this set of requirements.

It is a fact that sometime you have to change the interface. This statement
will be true of every OO COBOL, every Java, and every C# system, no matter how
much you wrap the attributes, sometimes you will still have to make changes
that are externally visible.

But part of the business of business data processing is to minimize risk when
making code changes.  The very success of our structured development (object
oriented or not) does produce cases where we need to balance our interest in a
changed behavior against the computed cost of a possible mistake in the change
(and, as Howard mentioned, the cost of larger testing efforts). Those
trade-offs are here to stay. If OOD does succeed in producing more re-usable
code, then we actually have an increase in this management responsibility. But
hey, one of the reasons to make money and save money is so we can pay the
manager who sizes up each of these trade-offs.

Anyway, it is mathematical. The larger the number of re-uses, the larger the
reluctance to change it (and the larger the tendency towards the fallback
options ... dup, rename, isolate, wait for more testing budget, get another cup
of coffee ...).

But a reluctance to change is not a reluctant to re-use on another occassion.

Actually, just as an aside; OOP tools make the dup process easier, for better
or worse. If what we really want to get to is all wrapped up inside an object,
and the thing we are not satisfied with is a basic mutator like doItThisWay(),
.. all we might need to do is write noDoItThisWay(), and regenerate the system.

Hidden in there is the fact that violating re-use tenets is extremely easy with
OOP tools. There is no hand that reaches out of the black box and slaps us on
the wrist if we create another method, or overload an identically named method
(although overloading at point blank range can produce wide spread damage as
older methods might have been engaged via the substitution principle, and your
new overload will catch the wind of those invocations in your new method's
sails, ... maybe not what you want).  But dup the method, rename and jam that
puppy right into the class, off to lunch.   OOP tools are extremely powerful. 

As shops mature they will get special groups that own classes, not always
becauase they buy into a new management philosophy, but to prevent certain
gotchas. OOP tools are very powerful. The better programmers will need to be
kept tame.

Best Wishes, 
Bob Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
