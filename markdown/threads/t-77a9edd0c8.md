[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Extensions, APIs, and meeting user/customer demand

_7 messages · 4 participants · 1998-09_

---

### Extensions, APIs, and meeting user/customer demand

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com>`

```
Given the recent discussion on the "evils" of programmers using extensions
to the COBOL language, I thought I would start a new thread on this topic.
My background has included (roughly in order)

  - MVS (IBM mainframe) COBOL application programmer
  - MVS COBOL (and other program products) system programmer and "help desk"
type work
  - Employee of an MVS software company (ADS which then produced Xpediter -
a COBOL debugging tool)
  - Head of the GUIDE (IBM user group) COBOL group (also major requirement
writer and processor)
  - Employee of a PC/Workstation/Unix COBOL compiler company (Micro Focus)
  - Consultant to a representative on the X/Open COBOL group
 - Representative to the CODASYL , J4 (X3J4-ANSI), WG4 (ISO) COBOL
committees
 - On disability so I don't have to "defend" anyone's company or official
position concerning COBOL

This has given me an unusual set of views  concerning COBOL Standardization,
extensions, and similar topics.

To start with,
   COBOL vendors are in the business of making a profit.  If users didn't
want things, then the vendors (in most cases) wouldn't do it - and
conversely, if customers don't buy something, then the vendor  is highly
likely to drop it.  This is "truth" and I assume pretty obvious to most
readers.

As far as the ANSI/ISO COBOL groups go, their members are VOLUNTEERS whose
companies (or groups) are willing to pay for the members to attend meetings
5-7 times (weeks) a year. (The companies pay meeting fees, hotel bills,
etc - as well as the members salaries - in most cases).  There are
ABSOLUTELY no requirements for becoming a member of the ANSI committee - and
the ISO committee members are part of "country delegations" (rules
established by each country).  Please don't talk about these people getting
"fired" or working harder or doing more - until you are ready to join and
spend the time that they do "for gratis".

Now - let's get back to the major topic.

For those of you who are IBM COBOL users, just consider writing a program
without a single GOBACK or COMP-3.  It would be possible, but it just never
happens.  Those who are "suggesting" that you should write COBOL without any
extensions are asking you to code that way. (Not to mention not ever using
an EXEC CICS statement or a CALL 'CBLTDLI' - or even a 'single quote'
instead of a "double quote")

For most PC programmers, try picturing a production program without any
COMP-5 items (and imagine your code "walking" rather than "running").

The simple truth is that extensions ARE useful in optimizing a program for a
specific operating system.

They are also the major (well one of the major) problem when trying to
migrate to another operating system (or sometimes another compiler on the
same operating system).

Let's face it,
  When the majority of the IBM CICS or IMS production systems were written,
no one even considered porting them to another vendor's COBOL (and probably
not to another operating system).  Gradually, as customers demanding this
facility, IBM has come up with compatible compilers, databases, and TP
monitors for those other environments.

However, if you are developing a new system, then there really is a question
of what you think will happen to that application during its expected life
time.

If I were assigned the design and creation of a production ISPF system
today, my guess is that it would live its entire life on an IBM mainframe.

If, on the other hand, I was told to design and create a "Workstation/PC"
GUI data entry system, then my guess is that it would end up on multiple
operating systems - and quite possibly with multiple  compilers during its
life time.

In the 1st case, I would use IBM extensions to my heart's content; in the
2nd case, I would try to isolate as many extensions (including screen I/O
and file access) into separate programs - or at least paragraphs/sections.
But I would STILL use some extensions that optimized my environment (such as
USING BY VALUE, COMP-5, RETURNING, etc)

Now, let's look at the Standardization process.
  It is too slow.
     It is WAY too slow
         It seems to be getting slower all the time.

I have some ideas on why this happens (happened) - much of it having to do
with the limited number of "users" on the committees - but I won't detail my
complaints about this process here.

The bottom-line is that there is a REAL need for certain "extensions" to the
COBOL language LONG before any Standard gets passed.  (This becomes worse in
situations like some of the NG readers talk about when their customers are
STILL running '74 compilers - almost a decade and a half after the '85
Standard came out.)  In the '80s there were some attempts to get "consortia"
to define COBOLs that would be portable - before the Standard got updated.
Both X/Open COBOL and MIA COBOL were such attempts.  My use of the word
"attempts" gives you a good idea of how successful those were (in my
opinion).

Having worked for a compiler vendor, I *KNOW* that there was user demand for
features such as USAGE POINTER,   EXIT PROGRAM RETURNING, and other "modern"
features long LONG before any Standard was going to solve these problems.  I
think that any vendor who refused to consider their customers' needs for
these features was simply foolish (and has probably lost much of the COBOL
market - if their users have any choices for compilers).  On the other hand,
most such vendors are forced into either supporting old "extensions" even
after there are new methods of doing something (compare COMP-3 and
Packed-Decimal) or of providing "dialect" support for older versions of the
language (compare IBM's "CMPR2" or Micro Focus "FLAG(OSVS)").  Another
product that this necessitates is the creation of "migration" software,
classes, and companies.

  OK - what is (are) my point(s)?

1) Be careful  what extensions you ask your vendor for; you might get what
you ask for and be sorry later.

2) Use extensions for "optimization" or when required for program logic or
interfacing with other systems/software - but always be aware of the
trade-offs in doing so.  (Be particularly careful about isolating major
extensions - whenever possible - in systems that may be ported some day to
other operating systems or compilers)

3) Try to get your company, your user group, or some type of user
representative/input to the COBOL Standards group(s).  (At least make
certain that you review the "substantive changes" when a new Standard is out
for public comment.)

4) Know how to run your compiler's "Standards flagging" mechanism so you can
at least SEE what extensions you are using. (And issue bug reports when they
are not flagging some extensions.)

   ******

So much for my 2 (or more) cents worth!
```

#### ↳ Re: Extensions, APIs, and meeting user/customer demand

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36033185.37FE11A7@inficad.com>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com>`

```
William M. Klein wrote:

> Given the recent discussion on the "evils" of programmers using extensions
> to the COBOL language, I thought I would start a new thread on this topic.
> My background has included (roughly in order)

<major snippage>


>
>
> So much for my 2 (or more) cents worth!

Mr Klein covered a lot of ground, and very well.  At one time, I chaired
a
committee in
CODASYL made up of reps from any user group. Our efforts were aimed at
the
continued education of those who attended or read the minutes of such
meetings.
We met in different parts of the country to attract visitors from the
local
major users, and our members tried to create programs for their users
group.  We
had to quit because a "users group" with a very small constituency
gained
admission to our meetings, and brought it to it's knees.  So much for
voluntary
efforts.  Few major players can afford (they believe) to support
standardization
efforts in any manner, but at that time the USGov, the USMil, the
Canadian Gov.,
and many users groups were participating.

I am heartened by the discussions going on in this NG because many of
you are
more aware of the good and bad of this effort, and some very fine
suggestions
are bound to occur.  I hope you know that you can submit proposals to
X3J4, but
you may be asked
to follow a method they find helpful, and you may need someone who is
active to
be a
front runner for you.  In past times, those who sent proposals were
often asked
to attend a meeting where their proposal would be discussed.

I am personally a little shy about the camel thing with committee work,
but I'm
sure that left to a small group like the project that created ADA did no
better
IMHO.

In the old days (forgive me) bit fiddling was unheard of if it was a
business
data processing
application by many of the vendor members of the COBOL committee.  Most
were no
where near as aware of the kinds of things users do in the language as
this
group.  It was very difficult to get anyone to say yes we all need to
provide
that.  Even if it were obvious, some members marketing departments had
more
influence than the compiler builders.

I am most upset about the small expansion made by the screen section.  I
feel
the requirements are no more difficult than the addition of SORT/Merge
or Report
Writer, etc. Even sync left and right and string are major extensions to
me.

Being able to define an input/output medium (I/O) is the guts of the
Data
Division. Omitting the recognition of the way in which screens are used,
and the
properties of the
text, and other elements seems like a natural growth of the language,
and not
something that should be left to vendors to implement in a dozen
different ways.

The basic element is a record or a field and a collection of fields.  A
collection of them is a file.  Funny that the rest of the world has it
seems
hundreds of file types, and COBOL seems only to recognize variations on
single
dimensional space except in tables.

I will say that some of the GUI products seem to do a nice job.  I don't
have
any experience with them.  I hate it though that when looking at the
source
code, it is not
apparent what the generated code is doing.  A little increase in the
vocabulary
is natural with the age of a language.  I even understand some of the
things
young people say.

An added 2 cents.

Warren Simmons
warrens@iname.com
```

#### ↳ Re: Extensions, APIs, and meeting user/custo

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298261.73266.29632@kcbbs.gen.nz>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com>`

```
In message <<6tuqv3$qse@sjx-ixn10.ix.netcom.com>> "William M. Klein" <wmklein@ix.netcom.com> writes:
> 
> To start with,
…[4 more quoted lines elided]…
> readers.

But surely it is quite the other way around.  Vendors make
more money by increasing their market share.  This can be
done in several ways, one is to provide extensions which
differentiate their product in such a way that existing
users are 'locked in' and new users are attracted by these
features.

They must also provide portability paths from other vendor's
products to 'unlatch' that vendors lock-in.

> 
> As far as the ANSI/ISO COBOL groups go, their members are VOLUNTEERS whose
…[7 more quoted lines elided]…
> spend the time that they do "for gratis".

While they are volunteers and do a lot of work they are
supported by the compant because they are expected to 
promote their companies extensions over those of the
competitor's extensions.

For OO Cobol there were several incompatible (or vaguely
compatible schemes).  Each company wants theirs to be
adopted because:

     Ego - they will have got it 'right'
     Market advantage - the standard is implemented now
     Less work - the others will have to re-implement

So the cycle is:

     Create some useful extensions
     Get users to use and like them
     Get them adopted as 'standard'

The more an extension is used the more support that vendor
has for getting its unique features adopted as standard.
The more these are adopted the more likely that the
extensions of that vendor are used with confidence, and
other vendors copy them.
```

##### ↳ ↳ Re: Extensions, APIs, and meeting user/custo

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u1aif$a16@sjx-ixn6.ix.netcom.com>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com> <3298261.73266.29632@kcbbs.gen.nz>`

```

Richard Plinston wrote in message <3298261.73266.29632@kcbbs.gen.nz>...
>In message <<6tuqv3$qse@sjx-ixn10.ix.netcom.com>> "William M. Klein"
<wmklein@ix.netcom.com> writes:
>>
>> To start with,
…[11 more quoted lines elided]…
>features.

That would work for maybe one or two releases - but it sure doesn't work as
an ongoing strategy.  Vendors provide extensions to meet customer needs NOT
to "lock them in".  In fact, once any vendor provides an extension, often
(not quite always), many of the other vendors will have the same extension
(usually with the same syntax) within a release or two. Some examples,
   IBM introduced COMP-3, GOBACK, USAGE POINTER, APOST -
     All of those are now available in almost all other compilers

 Micro Focus introduced RETURNING, COMP-5 (may have been another vendor
1st), LOCAL-STORAGE
    All of those are now available in LOTS of compilers

Micro Focus has made a preprocessor available for the original AcuCOBOL
"windowing" syntax; Fujitsu has copies of many of the Micro Focus cbl_
routines, etc, etc, etc.


>
>They must also provide portability paths from other vendor's
>products to 'unlatch' that vendors lock-in.
>

True, - but so what?

>>
>> As far as the ANSI/ISO COBOL groups go, their members are VOLUNTEERS
whose
>> companies (or groups) are willing to pay for the members to attend
meetings
>> 5-7 times (weeks) a year. (The companies pay meeting fees, hotel bills,
>> etc - as well as the members salaries - in most cases).  There are
>> ABSOLUTELY no requirements for becoming a member of the ANSI committee -
and
>> the ISO committee members are part of "country delegations" (rules
>> established by each country).  Please don't talk about these people
getting
>> "fired" or working harder or doing more - until you are ready to join and
>> spend the time that they do "for gratis".
…[4 more quoted lines elided]…
>competitor's extensions.

Have you ever attended any J4 or WG4 meeting? It is absolutely FALSE that a
primary (or even a secondary) goal of most representatives is to "push"
their extensions.  I know this wasn't the case when I was a representative -
and I know a variety of other reps who repeatedly vote AGAINST features that
are "compatible" with a current implementation. (And of course you have
cases like IBM where their OS/400 and MVS compilers have almost no common
extensions - but each has lots of their own - what would you expect their
rep to do?)

>
>For OO Cobol there were several incompatible (or vaguely
>compatible schemes).  Each company wants theirs to be
>adopted because:

  Boy, do you have this one backwards!
    None of the implementations came out even close to the time the original
J4 proposal was completed.  Micro Focus came out with a version about one
year after the J4.1 technical report was mostly finished; IBM came out with
theirs later, Fujitsu was later than that.

The fun thing to do is to watch how the existing implementations all tried
to match the (then current) OO definition at J4.  But in each case, by the
time the product had come to market, the Standard definition had already
changed!  (This is, of course, the problem with creating any extension that
is aimed at meeting a *DRAFT* version of the next Standard.  Those drafts
keep changing while the extensions are already "in production".  Talk to any
IBM mainframe person who had to deal with the change in EVALUATE from VS
COBOL II R1 to R1.1)

>
>     Ego - they will have got it 'right'
…[7 more quoted lines elided]…
>     Get them adopted as 'standard'

This exact cycle has been suggested to J4 at times - because some people
have thought that it would SPEED UP the standardization process. (You only
add stuff to the Standard that is already "proven" in the market place.)
Personally, I think it has some good points to it - but the Standards groups
have always steadfastly rejected it.

>
>The more an extension is used the more support that vendor
…[4 more quoted lines elided]…
>
Set above.
  It is absolutely true that the more users use one vendors extensions, the
more likely it is for other vendors to pick it up.  But again, what does
this prove or mean?  The only thing this reflects is how SLOW the Standards
process is and the only way to get new features into general use quickly is
via extensions.


>
```

###### ↳ ↳ ↳ Re: Extensions, APIs, and meeting user/custo

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36045280.7AF3DA74@inficad.com>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com> <3298261.73266.29632@kcbbs.gen.nz> <6u1aif$a16@sjx-ixn6.ix.netcom.com>`

```


William M. Klein wrote:

> Richard Plinston wrote in message <3298261.73266.29632@kcbbs.gen.nz>...
> >In message <<6tuqv3$qse@sjx-ixn10.ix.netcom.com>> "William M. Klein"
> <wmklein@ix.netcom.com> writes:
> >>

<snippage>

>
>   It is absolutely true that the more users use one vendors extensions, the
…[5 more quoted lines elided]…
> >

At first, COBOL was one big extension.  We encouraged the vendors to follow the
spec, and fix the tool to be able to program their hardware so that we could
learn.
We expected that the cycle would include extensions, and often the vendors
brought us
problems that they wanted to do in a mutually compatible way. Once the users
dropped out of the mix, the full load of development and standardization fell on
the standards effort. PLus don't forget that an international effort plays a
really big part of this effort. This in NOT a tool for the USA.  I know we are
very proud of that.

I've been impressed most by the things the engineers have done to help the
compiler builders in the hardware they offer. My background is in the 64
instruction Univac I and II.  It had no operating system, no standard I/O, and
you did it all.

I know the language has grown considerably since the '60 version, but compared
to the English that it's based on, I don't think it has grown excessively. In
fact some of the things I've been learning about today's COBOL have been done by
allowing some words into some statements were they were not allowed before. So,
you might expect, I favor the addition of some new words, or picturers in the
Data and Screen areas. In fact, I still believe the Enviornment Division could
take some extension. <VBG>

Warren Simmons
warrens@iname.com
```

###### ↳ ↳ ↳ Re: Extensions, APIs, and meeting user/custo

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360459ae.0@news1.ibm.net>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com> <3298261.73266.29632@kcbbs.gen.nz> <6u1aif$a16@sjx-ixn6.ix.netcom.com> <36045280.7AF3DA74@inficad.com>`

```
It is interesting to note that there may be a 'backing off' from extensions.
IBM's newest compilers do not anymore support old non-standard IBM-
extensions (e.g. EXAMINE).

Warren G. Simmons wrote in message <36045280.7AF3DA74@inficad.com>...
>
>
…[10 more quoted lines elided]…
>>   It is absolutely true that the more users use one vendors extensions,
the
>> more likely it is for other vendors to pick it up.  But again, what does
>> this prove or mean?  The only thing this reflects is how SLOW the
Standards
>> process is and the only way to get new features into general use quickly
is
>> via extensions.
>>
>> >
>
>At first, COBOL was one big extension.  We encouraged the vendors to follow
the
>spec, and fix the tool to be able to program their hardware so that we
could
>learn.
>We expected that the cycle would include extensions, and often the vendors
>brought us
>problems that they wanted to do in a mutually compatible way. Once the
users
>dropped out of the mix, the full load of development and standardization
fell on
>the standards effort. PLus don't forget that an international effort plays
a
>really big part of this effort. This in NOT a tool for the USA.  I know we
are
>very proud of that.
>
>I've been impressed most by the things the engineers have done to help the
>compiler builders in the hardware they offer. My background is in the 64
>instruction Univac I and II.  It had no operating system, no standard I/O,
and
>you did it all.
>
>I know the language has grown considerably since the '60 version, but
compared
>to the English that it's based on, I don't think it has grown excessively.
In
>fact some of the things I've been learning about today's COBOL have been
done by
>allowing some words into some statements were they were not allowed before.
So,
>you might expect, I favor the addition of some new words, or picturers in
the
>Data and Screen areas. In fact, I still believe the Enviornment Division
could
>take some extension. <VBG>
>
>Warren Simmons
>warrens@iname.com
>
```

###### ↳ ↳ ↳ Re: Extensions, APIs, and meeting user/custo

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u2s43$mei@dfw-ixnews6.ix.netcom.com>`
- **References:** `<6tuqv3$qse@sjx-ixn10.ix.netcom.com> <3298261.73266.29632@kcbbs.gen.nz> <6u1aif$a16@sjx-ixn6.ix.netcom.com> <36045280.7AF3DA74@inficad.com> <360459ae.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <360459ae.0@news1.ibm.net>...
>It is interesting to note that there may be a 'backing off' from
extensions.
>IBM's newest compilers do not anymore support old non-standard IBM-
>extensions (e.g. EXAMINE).
  <much snippage>

In general (and there certainly are exceptions), IBM (and many other
vendors) are moving away from extensions when the "Standard" provides the
same functionality - especially when it is easy to convert from one to the
other (as it is from EXAMINE to INSPECT). On the other hand, IBM (in its
"newer" compilers - now many years old) has many extensions, such as USAGE
POINTER, PROCEDURE-POINTER, PIC N, etc - that still aren't (yet) in the
Standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
