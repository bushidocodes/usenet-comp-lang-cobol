[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reflection Ability

_36 messages · 13 participants · 2003-02_

---

### Reflection Ability

- **From:** dynamosteve92@yahoo.com (DynamoSteve)
- **Date:** 2003-02-14T14:13:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```
Hi All,  I have a question regarding Cobol's capabilities.  First a
disclaimer - I know very little, if anything about Cobol.  I'm a
development manager that is having to work with a Cobol dev team.  I
am trying to learn a thing or two about the language's ability.  I
know the answer to my question may depend on what flavor of Cobol is
in use - I can't answer that so if you can at least give me some
general advice I would appreciate it.

My question - does Cobol have reflection/introspection abilities
similar to Java.  What I want to do is set the value of a "variable"
in Cobol to a certain other value based on the value of a key
variable.  In psuedo-code what I'm talking about is this.

FNAME PIC X(30)
KEY   PIC X(5)
.
.
.
KEY = "FNAME"
FIND_VARIABLE(KEY) = "STEVE";
// The FIND_VARIABLE() language construct "points" at the variable
FNAME because that's the string value of the variable KEY that was
passed in.

In other words, I want to set the value of the variable who's name
coincides with value of the KEY variable.  Generally speaking, can
this be done?

Thanks in advance,
-Steve.
```

#### ↳ Re: Reflection Ability

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T02:49:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4daa14.158282266@news.optonline.net>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```
dynamosteve92@yahoo.com (DynamoSteve) wrote:

>Hi All,  I have a question regarding Cobol's capabilities.  First a
>disclaimer - I know very little, if anything about Cobol.  I'm a
…[24 more quoted lines elided]…
>this be done?

Yes, it can be done. The mechanism is different depeding on where the value is
coming from:
, An environment variable
. An internal table
. A COBOL indexed file
. A database

Robert
```

##### ↳ ↳ Re: Reflection Ability

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-14T23:21:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302142321.278440d2@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >In other words, I want to set the value of the variable who's name
> >coincides with value of the KEY variable.  Generally speaking, can
> >this be done?
> 
> Yes, it can be done. 

I think that you misunderstand the question.  Cobol does not support
introspection.

> The mechanism is different depeding on where the value is
> coming from:
…[3 more quoted lines elided]…
> . A database

None of those.  He wants to have a Cobol user word (variable name) in
a text string and use this to obtain the value of that named item from
where the compiler has put it in memory.

The name would need to be looked up the the compiler's data map, or
possibly the debug information file, but this is (usually) not
available to the running program in any way that is supported by the
language's syntax.
```

###### ↳ ↳ ↳ Re: Reflection Ability

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T14:03:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4e48b2.4932204@news.optonline.net>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[23 more quoted lines elided]…
>language's syntax.

The COBOL program can store variable names and pointers to their values in a
table, look them up with a SEARCH verb, SET the ADDRESS OF an abstract variable
in LINKAGE SECTION to the pointer, and perform operations on it. 

It could also do that with environment variables, where the OS looks up the name
and returns its value. Granted that is not a COBOL language feature, but can be
called by a COBOL program (as well as a Java program).

Of course, it could WRITE name-value pairs to an indexed file and retrieve them
with a READ.  

Robert
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-15T10:56:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302151056.182d0eae@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <3e4e48b2.4932204@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >The name would need to be looked up the the compiler's data map, or
> >possibly the debug information file, but this is (usually) not
…[5 more quoted lines elided]…
> in LINKAGE SECTION to the pointer, and perform operations on it. 

Introspection is where this is done by syntax supported by the
language.  What you are suggesting is writing the interpreter for a
scripting language in Cobol and then introspection will be supported
in _that_.

> It could also do that with environment variables, where the OS looks up the name
> and returns its value. Granted that is not a COBOL language feature, but can be
> called by a COBOL program (as well as a Java program).

This is because the environment strings support having the name
available.  If Cobol variables were implemented like that then (such
as may be done in a scripting language) it would satisfy his needs (or
wants), however environment variables are _not_ Cobol variables.
 
> Of course, it could WRITE name-value pairs to an indexed file and retrieve them
> with a READ.  

When you have found out what this discussion is actually about then
please do come and join in.
```

###### ↳ ↳ ↳ Re: Reflection Ability

- **From:** dynamosteve92@yahoo.com (DynamoSteve)
- **Date:** 2003-02-15T06:52:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b63a55.0302150652.65d16368@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com>`

```
Ok, so if we can't do that can you offer some further advice on how to
efficiently accomplish something in Cobol?  We are going to have a
string of data coming in to the program.  The string will be available
through a variable (user word?).  The format of the string will be
similar to a URI --key1=value1&key2=value2&key3=value3 -- not exactly
like that but close enough.  The key names passed in any one string
are basically random.  They could be any combination of up to 100 or
so.

Apparently the Cobol folks have a few routines to efficiently split
this string apart into individual key/value pairs.  They were planning
on doing a giant if then... else if... else if... type of thing to
assign the value to the variable identified by the key.  Again, in
psuedo-code, something like this ..

INPUT = "key1=value1&key2=value2"
FNAME PIC X(30)
LNAME PIC X(30)
KEY PIC X(30)
VALUE PIC X(3)
WHILE more pairs available in INPUT {
  split the next pair into KEY and VALUE
  IF KEY == "FNAME" THEN
    FNAME = VALUE;
  ELSE IF KEY == "LNAME" THEN
    LNAME = VALUE;
  ELSE
    error becasue key is unknown
}

Simple enough with two possible keys, but how would you approach this
when the potential keys are many?

Thanks again to all.


riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0302142321.278440d2@posting.google.com>...
> robert@wagner.net (Robert Wagner) wrote
> 
…[23 more quoted lines elided]…
> language's syntax.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** jp <jpbeaud@gmx.fr>
- **Date:** 2003-02-15T17:52:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4E704B.F6B2DDA3@gmx.fr>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com>`

```
I am not sure, I have well understood what you want, but I think it is something like:

You know how much key and value there are at maximum:

01 INPUT-DATA Occurs 100.
    05 KEY pic X(30).
    05            pic x.
    05  VALUE pic X(30).
    05            PIC X.


INITIALIZE INPUT-DATA
MOVE INPUT INTO INPUT-DATA
PERFORM VERYING i from 1 by 1 until ( i > 100 OR KEY  (i ) = SPACES  )
    Evaluate True
    When Key(i) = 'FNAME'
        Move Value (i) to FNAME
    When KEY(i) = 'LNZAME'
        Move Value (i) to LNAME
    When Other
        DISPLAY 'ERROR!!!'
    End-Evaluate
END-PERFORM






>
>
…[46 more quoted lines elided]…
> > language's syntax.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-15T11:32:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XRudndR-jvSf59OjXTWciQ@giganews.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com>`

```

"DynamoSteve" <dynamosteve92@yahoo.com> wrote in message
news:36b63a55.0302150652.65d16368@posting.google.com...
> Ok, so if we can't do that can you offer some further advice on how to
> efficiently accomplish something in Cobol?  We are going to have a
…[31 more quoted lines elided]…
> Thanks again to all.

The COBOL folk are on the right track - except the multiple if-then-else
construct is kinda kludgy.

What you are trying to do is realtively common as a transaction stream. For
example:

EMP-NO:1234,HRS-WORKED:4.5,BASE-PAY:12.50,EXP:16.50^EMP-NO:4321...

or

N=1235,H=4.5,R=12.50,E=16.50^N=4321....

Yeah, this sort of thing happens every day. Remembering that COBOL is file
and record oriented:

1. Decompose stream into 'input records'
2. Decompose individual record into values for specific data fields
3. Apply the values to the master record

I encourage you to make haste with this project:

As of Friday, Feb 14th:

"Hours after a federal court of appeals blocked an order forcing Microsoft
to incorporate Sun Microsystems' Java programming language, the Redmond,
Wash.-based software giant went ahead anyway removing its own Virtual
Machine (VM) (define) from its Windows XP operating system."

"As a result of SP1a, Microsoft will no longer provide Microsoft VM as a
download off of its Windows Update site. No new Microsoft product will
include the Microsoft VM, including Windows Server 2003 and Windows 2000 SP4
[nor inlcude Sun's rendition of JVM]"

Story at:
http://www.internetnews.com/bus-news/article.php/1578841

Java's a goner.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-02-15T13:00:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2lv8l$2e2$1@panix1.panix.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com>`

```
In article <36b63a55.0302150652.65d16368@posting.google.com>,
DynamoSteve <dynamosteve92@yahoo.com> wrote:
>Ok, so if we can't do that can you offer some further advice on how to
>efficiently accomplish something in Cobol?

I would suggest hiring a consultant to provide your organisation to 
provide it with the skills, knowledge and techniques which are, it seems, 
sorely lacking... as is evidenced by their placing a person in charge of a 
COBOL team who has no experience with the language and is trying to 
second-guess his team by asking questions of a UseNet group.

DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 5)_

- **From:** dynamosteve92@yahoo.com (DynamoSteve)
- **Date:** 2003-02-15T17:15:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b63a55.0302151715.52b8ca6b@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com>`

```
Ah, I knew it was a matter of time before a cocky, full of himself,
prick would chime in with some wonderful advice.  I'll tell you DD,
when I run across assholes like you hiding behind the anonymity of the
net, I tell myself "there's a person who knows he doesn't have the
skills, knowledge or technique to function in the real world".

Now, at which point was it that I said I was in charge of a Cobol
(cased this way on purpose in hopes that something as piddly as that
will annoy the shit out of you) team?  I didn't.  In fact the
development team for this project consists of mostly Java folks. 
However, we have a need to use some logic located in legacy cOBOL
apps.  I'm simply trying to understand what the coBOL'ers are telling
me so I can understand their logic when the estimate scope and time.

I am second-guessing nobody.  In fact the coboL team is, in my
extremely non-skilled, ignorant and technique-less opinion, quite
competent.  Do they know all the answers? No.  Are the unsure of the
best architecture to accomplish what we need? Yes.  Is that a crime?
No.

Ok, DD.  Time to pony up.  You're obviously King cObOl so tell us all,
exactly how would you do this?  Surely someone as sharp as you can
cook something up.  Otherwise, shut the hell up.  We've each taken our
public whack... email me privately and I'll be happy to frustrate
myself fow weeks to come trying to knock some sense into you.

Warmest regards,
-Steve.

docdwarf@panix.com wrote in message news:<b2lv8l$2e2$1@panix1.panix.com>...
> In article <36b63a55.0302150652.65d16368@posting.google.com>,
> DynamoSteve <dynamosteve92@yahoo.com> wrote:
…[9 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: -Reflection Ability

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-15T23:15:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302152315.5a156cad@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com>`

```
dynamosteve92@yahoo.com (DynamoSteve) wrote 

> Now, at which point was it that I said I was in charge of a Cobol
> team?  I didn't.  

I thought that you had implied this here:

"I'm a development manager that is having to work with a Cobol dev
team."

But then I wouldn't want to stop you sounding off at the dwarf, I
should stand back and watch the fur fly   ;-)
```

###### ↳ ↳ ↳ Re: -Reflection Ability

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-02-16T11:40:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2oetm$ern$1@panix1.panix.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <217e491a.0302152315.5a156cad@posting.google.com>`

```
In article <217e491a.0302152315.5a156cad@posting.google.com>,
Richard <riplin@Azonic.co.nz> wrote:
>dynamosteve92@yahoo.com (DynamoSteve) wrote 
>
…[9 more quoted lines elided]…
>should stand back and watch the fur fly   ;-)

Fur?  Come now, Mr Plinston, this is so undeveloped as to scarce approach 
peachfuzz; it is a kind of weary interchange along the lines of:

'How do I do this?'

'Hire people who knows how, pay them well and step back so they can Do
Their Job.'

'Oh, yeah?  I bet you can't tell me, Mr Poopie-head... go on, I double-dog 
*dare* you to show that you know!'

'I'd be happy to... once you hire me, pay me well and step back so I can 
Do My Job.  Please post a rate, or range of rates, associated with the 
position(s) offered.'

DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-02-16T08:41:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v4v4lkqc5dnjbb@corp.supernews.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com>`

```

DynamoSteve <dynamosteve92@yahoo.com> wrote in message
news:36b63a55.0302151715.52b8ca6b@posting.google.com...
[...]
> Now, at which point was it that I said I was in charge of a Cobol
> (cased this way on purpose in hopes that something as piddly as that
> will annoy the shit out of you) team?  I didn't.

Richard already mentioned this; but I will mention it, again.
You wrote, "I'm a development manager that is having to work
with a Cobol dev team." While it may have been clear to you,
it was not clear to me that there were two teams.

>  In fact the
> development team for this project consists of mostly Java folks.
> However, we have a need to use some logic located in legacy cOBOL
> apps.  I'm simply trying to understand what the coBOL'ers are telling
> me so I can understand their logic when the estimate scope and time.

I once estimated a project at 16 weeks. The project was to
interface a device to a terminal. My part was the firmware.
An associate called the manufacturer, of the device, and
asked how long it should take. Their response was 30 minutes.

This discrepancy caused the associate to question my
competence. The associate was unaware that the 30 minutes
was to connect the device to a PC using Visual Basic controls
that were supplied with a SDK. My estimate had to include
writing and testing 50 C functions because VB will not run on
an 8051 microprocessor.

You may not be able to understand their estimates by asking
questions in a news group. This is because, you can never
provide to those, in the news group, all that is required to
educate you to the other team's logic.

> I am second-guessing nobody.

I hope that is true. Raising anything that you believe you
learned here may cause friction between the teams.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-16T15:16:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com>`

```
"DynamoSteve" <dynamosteve92@yahoo.com> wrote in message
news:36b63a55.0302151715.52b8ca6b@posting.google.com...
> I'll tell you DD, when I run across assholes like you hiding behind the
anonymity of the net..

Give me a break. "dynamosteve" is hardly less "anonymous" than "docdwarf."

How would I do this ["reflection/introspection"]?

No COMPETENT COBOL programmer - or consultant - would ever find himself in
need of such a tool, because there are so many better ways for the COMPETENT
COBOL programmer to debug his or her program.

Of course, you wouldn't know that, because even INCOMPETENT 'any language'
programmers - and self-proclaimed experets and consultants - know what they
don't know; or at a minimum, they know THAT they don't know.

-
Michael Mattias
Tal Systems, Inc.
Racine WI
mmattias@talsystems.com
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 7)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-02-16T13:03:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2onaq0o5s@enews1.newsguy.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com...
> "DynamoSteve" <dynamosteve92@yahoo.com> wrote in message
> news:36b63a55.0302151715.52b8ca6b@posting.google.com...
> > I'll tell you DD, when I run across assholes like you
hiding behind the
> anonymity of the net..
>
> Give me a break. "dynamosteve" is hardly less "anonymous"
than "docdwarf."
>
> How would I do this ["reflection/introspection"]?

I don't want to get in the middle of the debate in this thread
(whatever it is,) but this remark interests me:

> No COMPETENT COBOL programmer - or consultant - would ever
find himself in
> need of such a tool, because there are so many better ways
for the COMPETENT
> COBOL programmer to debug his or her program.

> Of course, you wouldn't know that, because even INCOMPETENT
'any language'
> programmers - and self-proclaimed experets and consultants -
know what they
> don't know; or at a minimum, they know THAT they don't know.

I'm not a COBOL programmer by any rigorous standard, but can
see how reflection could be made use of.  (Again, this is a
sincere request for discussion, not an attempt to support any
viewpoint other than my own.)

For instance, if you could inspect the structure and values of
your working storage, you could write a generic error handler
that would "core dump" your program on fatal errors.  I've used
similar mechanisms, where I can, and it's been a tremendous
boon to debugging code that has erred in the field.

The ability to reflect your code has to be paid for with an
increased overhead, so perhaps it's not worth it -- but does
wanting/exploiting such a feature qualify as incompetence?
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-17T10:51:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302171051.3308aaee@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com> <b2onaq0o5s@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote 

> The ability to reflect your code has to be paid for with an
> increased overhead, so perhaps it's not worth it -- but does
> wanting/exploiting such a feature qualify as incompetence?

Different languages are developed specifically because they offer
different facilities.- this leads to solutions being structured in
different ways.  In fact it is probably that a particualr solution
could not be easily coded in existing languages that leads to new
languages.

Reflection seems to be useful when interacting with code that is
alien.  That is as a means of a program to determine the properties
and functions of something with which interaction is required.

It is unlikely to be of any use where there is complete control over
all the code in a system, or even where there are adequate specs that
can be relied on for code that you don't have control over.

As it happens I doubt that Reflection/introspection would be the
solution that was asked for given the actual problem.  Now that _is_
incompetence.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 9)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-02-17T13:17:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2rcgv05b5@enews1.newsguy.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com> <b2onaq0o5s@enews1.newsguy.com> <217e491a.0302171051.3308aaee@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0302171051.3308aaee@posting.google.com...
> "Grinder" <grinder@no.spam.maam.com> wrote
>
> > The ability to reflect your code has to be paid for with an
> > increased overhead, so perhaps it's not worth it -- but
does
> > wanting/exploiting such a feature qualify as incompetence?
>
> Different languages are developed specifically because they
offer
> different facilities.- this leads to solutions being
structured in
> different ways.  In fact it is probably that a particualr
solution
> could not be easily coded in existing languages that leads to
new
> languages.

I've seen systems that have attempt to retrofit reflective
services into an application -- with varying degrees of
success.  There's no argument from me that deciding to do so
should carefully look at benefit vs. overhead, benefit vs.
effort, etc, to see if it's worth doing.  Something I was
hoping to dialog on, though, is that if this feature is
provided by the language (or environment,) would it still be of
no use to the COBOL programmer.

> Reflection seems to be useful when interacting with code that
is
> alien.  That is as a means of a program to determine the
properties
> and functions of something with which interaction is
required.
>
> It is unlikely to be of any use where there is complete
control over
> all the code in a system, or even where there are adequate
specs that
> can be relied on for code that you don't have control over.

Would it be incompetent to use reflection in the aforemention
"core dump" example?

> As it happens I doubt that Reflection/introspection would be
the
> solution that was asked for given the actual problem.  Now
that _is_
> incompetence.

Again, I'm not trying to estimate DynamoSteve's competency, I
just though this would an interesting avenue of discussion.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-17T15:29:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302171529.3a4bc96@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <fXN3a.1802$UF6.596037@newssrv26.news.prodigy.com> <b2onaq0o5s@enews1.newsguy.com> <217e491a.0302171051.3308aaee@posting.google.com> <b2rcgv05b5@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote 

> Would it be incompetent to use reflection in the aforemention
> "core dump" example?

I have no idea how you were thinking of making this useful.  A core
dump is a static file on the disk, it cannot reflect itself because it
won't execute.

Certainly it would be useful to map a core dump back to the original
source code via some sort of debugger that has access to compiler and
linker maps, but how would reflection be used ?

Or were you just thinking that intertwining the variable names as text
in between the actual variables would give you the ability to follow a
hex dump better ?
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2003-02-16T11:24:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2oe01$c4e$1@panix1.panix.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com>`

```
In article <36b63a55.0302151715.52b8ca6b@posting.google.com>,
DynamoSteve <dynamosteve92@yahoo.com> wrote:

[snip]

>
>Ok, DD.  Time to pony up.  You're obviously King cObOl so tell us all,
>exactly how would you do this?

When you aren't too busy polishing up what seem to be your trolling skills 
you might try to polish up your reading comprehensions skills... this 
question is answered in the posting you quoted below.

DD


>docdwarf@panix.com wrote in message news:<b2lv8l$2e2$1@panix1.panix.com>...
>> In article <36b63a55.0302150652.65d16368@posting.google.com>,
…[10 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-16T13:49:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jgCdnWHlT5pXdtKjXTWcjA@giganews.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com>`

```

"DynamoSteve" <dynamosteve92@yahoo.com>
>
> Ok, DD.  Time to pony up.  You're obviously King cObOl so tell us all,
> exactly how would you do this?

He told you.

Hire someone competent.

It is self-evident you and your Java team are not competent (further
evidenced by your anti-social top-posting).

From what you say, your "COBOL" team cannot convert their business case to
your annointed 'language-de-jour.'

There are only three other possibilities:
1. Your Java programmers learn COBOL (probably not possible);
2. Your COBOL programmers learn Java (but why would they want to?**);
3. Forget about it.

I hereby withdraw my earlier proposed solution to your problem and replace
it with the suggestion that you and your crew open an unsanitary taco stand.

** Microsoft announced last Thursday that Microsoft would not ship JVM -
either theirs or Sun's - in any future edition of Windows (starting with XP
SP1a). Java's on the way out.


> Surely someone as sharp as you can
> cook something up.  Otherwise, shut the hell up.  We've each taken our
…[6 more quoted lines elided]…
> docdwarf@panix.com wrote in message
news:<b2lv8l$2e2$1@panix1.panix.com>...
> > In article <36b63a55.0302150652.65d16368@posting.google.com>,
> > DynamoSteve <dynamosteve92@yahoo.com> wrote:
…[4 more quoted lines elided]…
> > provide it with the skills, knowledge and techniques which are, it
seems,
> > sorely lacking... as is evidenced by their placing a person in charge of
a
> > COBOL team who has no experience with the language and is trying to
> > second-guess his team by asking questions of a UseNet group.
> >
> > DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-17T10:17:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302171017.1330d4e0@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> ** Microsoft announced last Thursday that Microsoft would not ship JVM -
> either theirs or Sun's - in any future edition of Windows (starting with XP
> SP1a). Java's on the way out.

Microsoft, once again, tries to punish its enterprise customers in an
effort to control the industry. By making this move it is forcing a
choice between Java and Windows.  Windows is on the way out, not just
because it doesn't have Java, but because Microsoft will probably
detect and ensure that it doesn't run.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 8)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-17T14:58:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z16dnQL2Aflc0cyjXTWchw@giganews.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0302171017.1330d4e0@posting.google.com...
> "JerryMouse" <nospam@bisusa.com> wrote
>
> > ** Microsoft announced last Thursday that Microsoft would not ship JVM -
> > either theirs or Sun's - in any future edition of Windows (starting with
XP
> > SP1a). Java's on the way out.
>
…[4 more quoted lines elided]…
> detect and ensure that it doesn't run.

Nah. Microsoft's not trying to punish its enterprise customers; Microsoft is
trying to punish Sun Microsystems. Enterprise customers are just 'collateral
damage.' (Although I would point out, Java users are not completely
'innocent victims' inasmuch as they allied themselves with Sun at the
get-go. Java users, in this regard, are like the Palestinians during the
Gulf War: their support of Iraq was based more on hope than reason and they
ended up getting screwed.)

I can't agree that Microsoft is 'forcing' a choice between Java and
Windows - Microsoft is certainly STRONGLY pushing toward Dot-Net, but one
can still download JDK from Sun - as long as Sun stays in business, that is.

If Microsoft is on the way out, it won't be too bad; we still have Fujitsu's
Linux COBOL. By the way, is anybody working on a COBOL compiler for Java?
(Before anyone says: "Java's not an operating system you twit!" I'll admit
that I thought that was the only reason Microsoft would wage war against
Sun, to prevent competition in the OS market.)

And Microsoft certainly won't refuse to run Java. Unless of course Microsoft
determines that doing so would adversely affect the user's computing
experience.

I predict:
1. COBOL will outlast Java.
2. COBOL might outlast Microsoft.
3. COBOL will outlast Sun Microsystems.
4. COBOL will outlast the sun.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-17T21:59:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e515a97.206151665@news.optonline.net>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com> <z16dnQL2Aflc0cyjXTWchw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

> By the way, is anybody working on a COBOL compiler for Java?

LegacyJ's PERCOBOL generates code for the JVM.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 10)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-17T21:05:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rp2cnXsy2_vWPsyjXTWchA@giganews.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com> <z16dnQL2Aflc0cyjXTWchw@giganews.com> <3e515a97.206151665@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e515a97.206151665@news.optonline.net...
> "JerryMouse" <nospam@bisusa.com> wrote:
>
> > By the way, is anybody working on a COBOL compiler for Java?
>
> LegacyJ's PERCOBOL generates code for the JVM.

Ooo! Right. I forgot. Thanks.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-18T01:36:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E518E47.32F0459C@shaw.ca>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com> <z16dnQL2Aflc0cyjXTWchw@giganews.com>`

```


JerryMouse wrote:

> And Microsoft certainly won't refuse to run Java. Unless of course Microsoft
> determines that doing so would adversely affect the user's computing
…[6 more quoted lines elided]…
> 4. COBOL will outlast the sun.

Having tossed your runes and made a prediction, I would suggest they are a
little contradictory in view of the following.

Firstly the 'Holy Trinity' - IBM, HP/Compaq and Sun - backing Linux. Then on to
Java. Having done a cursory look at the IBM OO documentation :-

Class-id.    ThisIsMyClass inherits Base.

Repository.

    Class ThisIsMyClass             is 'myclass'
    Class Base                            is "java.lang.object".

While your can write in Standard OO COBOL the whole emphasis is on using Java as
the support mechanism. Not unlike I can write non-OO or OO-programs in M/F that
contain SQL syntax and the ODBC pre-processor, provides the actual access to the
DB .

IBM is using the Java Base for "new" instances and If I make a typo in my
methodname "getTHUSInfo", instead of "getTHISinfo", it's the Java Base that is
going to report the error not the IBM OO.

Bill made the comment in another message that lack of COBOL Standard classes was
a deterrent to IBM-ers. True, but at the same time, with the IBM OO link to
Java, the latter's Standard classes are automatically available, plus IBM can
invoke Java and Java can invoke IBM.

Which raises an interesting point. Although not part of their current offering,
IBM are active members in J4 discussing standard classes. So a poser - WHEN J4
comes up with a specific set of Standard Classes :-

- Will IBM bother to implement - seeing that existing Java saves them the
effort.
 (And here I'm thinking where Bill responded to me privately that IBM doesn't
need to implement R/W, they have it available from a third party)
- Will Fujitsu adopt to the new standard (and from I've seen I would call
Fujitsu's current Standard classes 'COBOL Lite').
- Will both Hitachi and Micro Focus - having developed a large set of Standard
classes, based on the Smalltalk model  - also drop theirs in favour of a new J4
Standard ?

It kind of reminds me of posters that were pasted all over Underground and
railway stations in England when I was a kid during WW2. To save energy, they
read, "Is your journey really necessary ?". Possibly the same question applies
to J4.

Back to your predictions we know that over the past 20 odd years it has been :-

    Microsoft - 2     IBM  - 0         (DOS/ MSDOS and OS2/Windows).

Can IBM really afford to let Billy Boy  win the next round ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 10)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-02-17T23:20:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0302172320.521f0370@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com> <z16dnQL2Aflc0cyjXTWchw@giganews.com> <3E518E47.32F0459C@shaw.ca>`

```
Since we are prognosticating - see below...

"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3E518E47.32F0459C@shaw.ca>...
> JerryMouse wrote:
> 
…[12 more quoted lines elided]…
> 

.. snip snip ..

> 
> Back to your predictions we know that over the past 20 odd years it has been :-
…[4 more quoted lines elided]…
> 

No - My prediction (shared privately with others before and with no
inside knowledge whatsoever):

IBM Buys SUN (or the part of Sun that owns Java - but probably will
have to buy it all).

Timeframe - before first quarter 2004.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-18T10:55:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302181055.4938c502@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com> <b2lv8l$2e2$1@panix1.panix.com> <36b63a55.0302151715.52b8ca6b@posting.google.com> <jgCdnWHlT5pXdtKjXTWcjA@giganews.com> <217e491a.0302171017.1330d4e0@posting.google.com> <z16dnQL2Aflc0cyjXTWchw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> Nah. Microsoft's not trying to punish its enterprise customers; Microsoft is
> trying to punish Sun Microsystems. Enterprise customers are just 'collateral
…[4 more quoted lines elided]…
> ended up getting screwed.)

So, if Java users are hurt, then it is their own fault for trying to
use something that was not 'Microsoft approved' ? (actually it was,
there were Microsoft version of Java).

And more, if they had used 'reason' they would have remained using
Microsoft products such as Visual C++.

> I can't agree that Microsoft is 'forcing' a choice between Java and
> Windows - Microsoft is certainly STRONGLY pushing toward Dot-Net, but one
> can still download JDK from Sun - as long as Sun stays in business, that is.

No, only as long as 'patch x' doesn't change how the JRE runs. (ref:
see DR-DOS, Lotus 123, etc).

If you had read recent Microsoft EULAs you would know that you had
granted Microsoft the _right_, without any other prior approval or
acknowledgement, to search your computer, update any part and to
remove any software it doesn't like.

> And Microsoft certainly won't refuse to run Java. 

It doesn't need to refuse, it just needs to make it difficult, slow,
incompatible.

For example for several years Windows will 'optimise' your hard disk,
it will shuffle directories so that your frequently used documents and
programs will be at the start and thus will load quicker.

Well actually it will move MS programs and documents to the start and
competitors to the very end, making them slower.

They can then claim that MS products are 'better' because they are
faster.

And, of course, MS has APIs that are undocumented that its own
software can use, but others cannot.  For example Word vs.
WordPerfect, IE vs Netscape.  Competitors only had available the
published APIs which ran slowly while MS products used internal
shortcuts.

> Unless of course Microsoft
> determines that doing so would adversely affect the user's computing
> experience.

It hasn't been about 'computing experience' for years, it has been
about control and revenue.  Certainly Windows has been about
'featurism' as they try to come up with reasons to buy a new version
every year or so, otherwise everyone would still be using Win95.  MS
ran out of reasons why enterprise should buy anything since Win98 so
they imposed Licence 6 to attempt to lock in 3 years revenue and
enforced upgrades.

Now that MS are talking about having to reduce prices in the light of
compettition I wonder how many Licence 6 users will be paying reduced
rates ?

The history of MS is one of cooperating with other vendors until MS's
own products are good enough to cut them off without air, and bugger
the users. MS used to be a languages company co-operating with DRI
(CP/M) and Unix (Xenix) until they managed to sign a deal for
supplying a rip-off of CP/M to IBM. Then their languages wouldn't run
on the new CP/Ms.

MS cooperated fully with Novel for servers until they managed to
licence a copy of IBM's LAN Manager and SMB and then it wasn't quite
so easy to use Novell.

In all these cases, no doubt, you would say that non-MS users were
'collateral damage' and it was their own fault, if they had used
'reason' they would have bought MS products, or waited for them, or
realised that if MS didn't do it then it shouldn't be done.
Well maybe it is the turn for MS users to be collateral damage.
```

###### ↳ ↳ ↳ Re: eflection Ability

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-15T11:20:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302151120.130522f5@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com>`

```
dynamosteve92@yahoo.com (DynamoSteve) wrote

> similar to a URI --key1=value1&key2=value2&key3=value3 -- not exactly
> like that but close enough.  The key names passed in any one string
> are basically random.  They could be any combination of up to 100 or
> so.

>   IF KEY == "FNAME" THEN
>     FNAME = VALUE;
…[4 more quoted lines elided]…
> }

With CGI URLs Python, PHP, and other languages will split the incoming
parameters and make them variables.  It can do this because they are
typeless scripting languages.  Cobol cannot do this as in any way
other than handling it just as data.

The question then is why do you want to have this data put into actual
variables of the same name as the string ?  Why do you want to emulate
what other languages do ?  Just put it into a table of name and value
pairs, and collect each value into some working variables as they are
required to be used.
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T22:01:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4eb8c8.33630179@news.optonline.net>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <3e4daa14.158282266@news.optonline.net> <217e491a.0302142321.278440d2@posting.google.com> <36b63a55.0302150652.65d16368@posting.google.com>`

```
dynamosteve92@yahoo.com (DynamoSteve) wrote:

>Apparently the Cobol folks have a few routines to efficiently split
>this string apart into individual key/value pairs.  They were planning
…[20 more quoted lines elided]…
>when the potential keys are many?

All those hard-coded values in an if (or case) statement are ugly, unnecessary
and a maintenance headache. Do it like this:

01  entry-count value zero pic s9(04).
01  name-table.
     05  name-entry occurs 1 to 200 dplending on entry-count indexed by x-name. 
          10  name-word           pic  x(30).
          10  value-word           pic  x(30).

parse input string using UNSTRING verb

*> putting values into the table
set x-index to 1
search name-entry
     at end
         add 1 to entry-count
         move input-name to name-word (entry-count)
         move input-value to value-word (entry-count)
     when name-word (x-index) = input-name
         move input-value to value-word (x-index
end-search

*> getting values from the table
set x-index to 1
search name-entry
     at end (not found)
     when name-word (x-index) = input-name
         move value-word (x-index) to output-value
end-search
```

#### ↳ Re: Reflection Ability

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-02-15T13:33:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2m4m701h5r@enews1.newsguy.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```

"DynamoSteve" <dynamosteve92@yahoo.com> wrote in message
news:36b63a55.0302141413.740eddfe@posting.google.com...
> Hi All,  I have a question regarding Cobol's capabilities.
First a
> disclaimer - I know very little, if anything about Cobol.
I'm a
> development manager that is having to work with a Cobol dev
team.  I
> am trying to learn a thing or two about the language's
ability.  I
> know the answer to my question may depend on what flavor of
Cobol is
> in use - I can't answer that so if you can at least give me
some
> general advice I would appreciate it.

It would be worthwhile to ask this question of Fujitsu.
Refelection is a part of the dotnet framework, but I cannot say
if there are caveats to is use in cobol.net.
```

#### ↳ Re: Reflection Ability

- **From:** dynamosteve92@yahoo.com (DynamoSteve)
- **Date:** 2003-02-16T11:54:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b63a55.0302161154.6206e69b@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```
To all that have offered advice in an intelligent and and professional
manner I say "Thank You".  You've certainly contributed to helping me
quite a bit.

To the ignorant few, well, I've emailed you privately, so you know
what I think of your wonderful contributions to this thread.
```

##### ↳ ↳ Re: Reflection Ability

- **From:** docdwarf@panix.com
- **Date:** 2003-02-17T00:24:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2prlm$6r8$1@panix1.panix.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <36b63a55.0302161154.6206e69b@posting.google.com>`

```
In article <36b63a55.0302161154.6206e69b@posting.google.com>,
DynamoSteve <dynamosteve92@yahoo.com> wrote:
>To all that have offered advice in an intelligent and and professional
>manner I say "Thank You".

You are most welcome.  Have you determined how you will go about finding 
someone competent?

DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

- **From:** dynamosteve92@yahoo.com (DynamoSteve)
- **Date:** 2003-02-17T02:58:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b63a55.0302170258.5aab714a@posting.google.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <36b63a55.0302161154.6206e69b@posting.google.com> <b2prlm$6r8$1@panix1.panix.com>`

```
F-U-C-K  O-F-F.  Out.

docdwarf@panix.com wrote in message news:<b2prlm$6r8$1@panix1.panix.com>...
> In article <36b63a55.0302161154.6206e69b@posting.google.com>,
> DynamoSteve <dynamosteve92@yahoo.com> wrote:
…[6 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Reflection Ability

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-02-17T06:29:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2qh2a$8g4$1@panix1.panix.com>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com> <36b63a55.0302161154.6206e69b@posting.google.com> <b2prlm$6r8$1@panix1.panix.com> <36b63a55.0302170258.5aab714a@posting.google.com>`

```
In article <36b63a55.0302170258.5aab714a@posting.google.com>,
DynamoSteve <dynamosteve92@yahoo.com> wrote:
>F-U-C-K  O-F-F.  Out.

Hmmmmm... your imperatives will be given all the attention they deserve, I 
am sure.

DD

>
>docdwarf@panix.com wrote in message news:<b2prlm$6r8$1@panix1.panix.com>...
…[8 more quoted lines elided]…
>> DD
```

#### ↳ Re: Reflection Ability

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-17T16:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2r0ud$25u$1@peabody.colorado.edu>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```
When someone tries to do something like this - in a language that is ill-suited
for this technique, my response is to step back and ask what is it the they
REALLY want.

Do you really have a business function that requires such reflection ability?

Or is this the Java solution to a different problem?    If so, perhaps coding a
Java solution in COBOL isn't optimal.

So what are your business needs that made you suggest reflection is the correct
way to code a solution?  Maybe we can recommend the best way to do it in COBOL.
```

#### ↳ Re: Reflection Ability

- **From:** "Thomas Li" <aizhongli@sprint.ca>
- **Date:** 2003-02-17T11:58:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pB84a.4388$Wy1.33985@newscontent-01.sprint.ca>`
- **References:** `<36b63a55.0302141413.740eddfe@posting.google.com>`

```
Reflection is not a standard part of COBOL 85 at least. And so far I haven't
found any support in OO COBOL.
But in nonstandard way, a compiler can support it. My COBOL compiler whcich
will be released next month will support full Java reflection in Java way.

Thomas Li



DynamoSteve <dynamosteve92@yahoo.com> wrote in message
news:36b63a55.0302141413.740eddfe@posting.google.com...
> Hi All,  I have a question regarding Cobol's capabilities.  First a
> disclaimer - I know very little, if anything about Cobol.  I'm a
…[27 more quoted lines elided]…
> -Steve.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
