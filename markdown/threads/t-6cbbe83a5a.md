[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Visual Age Cobol, or Java ?

_82 messages · 25 participants · 2002-12_

---

### Visual Age Cobol, or Java ?

- **From:** trento2002@hotmail.com (Harry M)
- **Date:** 2002-12-09T23:07:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
I have a system developed in Cobol with 110 online programs and 125
batch programs. The system is on HP3000 and needs to be converted to a
different platform since HP is dropping support for the HP3000. I plan
to use DB2 for data base, Linux on the server and Windows on the
desktop.

One thought is to convert the whole system to Visual Age Cobol, the
other is to switch the batch programs to VA Cobol and the online to
Java. My concern is Java may not be able the handle the heavy amount
of data base access in some programs. There are 75 tables in the
system and some programs access as many as 25 tables.

If the system is converted to Java, should it use servlets, or Java
applications on the desktop?

What are the good and bad points about VA Cobol?
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-10T09:39:41
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at4cpa$5qa$1@hyperion.microfocus.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
Hi Harry,

You will need to check that VA COBOL can handle Java/COBOL interoperability.

You might want to look at Net Express from Micro Focus. It's a Windows Based
COBOL IDE and can 'wrap' COBOL with Java - and even create EJB's. Micro
Focus Server Express is the Unix based cobol that can be used to deploy
mixed Java/COBOL applications - but it's not yet supported on the
Intel-based Linux distributions. That's because of the current threading
model is not the same as the PThreads used in Unix.

Linux on the IBM zSeries is a different matter. Micro Focus are in the
process of putting Server Express on this as a lot of work has gone into it
to support pthreads.

Micro Focus have a version of Object COBOL Developer Suite on linux but this
does not have the Java interoperability biold in as it does not support
multi-threading.

You are right in your concern about the scalability of Java. That's why
Micro Focus have invested heavily in Java/COBOL interoparability - so that
you can get Java to do the bits its good at, and keep your core COBOL
business logic - what COBOL is best at - even on the desk top.

If you want to run the bulk of your application on the server the servlets
might be the way to go. Running a Java GUI from the server would reduce the
maintenece overhead for the client PCs and then the servlets would call the
COBOL to do the real work. You could even have your user interface in HTML
and forget all about Java.

If you want to run the applicatrion on the desk-top then you would not need
to use Java in which case there are other alternatives. Net Express provides
a too for developing GUI interfaces. If you are more comfortable with VB
then you could use that to develop your user interface and wrap your cobol
(using Net Express) as COM or MTS objects.

DB/2 is fully supported by all of Micro Focus COBOL products.

Please feel free to visit www.microfocus.com and also contact the sales
office for your location.

Paul

"Harry M" <trento2002@hotmail.com> wrote in message
news:b8d390f9.0212092307.46ef573c@posting.google.com...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
…[13 more quoted lines elided]…
> What are the good and bad points about VA Cobol?
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-10T04:02:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212100402.430dcc17@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
trento2002@hotmail.com (Harry M) wrote in message news:<b8d390f9.0212092307.46ef573c@posting.google.com>...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
…[3 more quoted lines elided]…
>

Is that a choice or is it being dictated by other factors? Opinion
would be fiercely divided on all of these choices.
 
> One thought is to convert the whole system to Visual Age Cobol, the
> other is to switch the batch programs to VA Cobol and the online to
> Java. My concern is Java may not be able the handle the heavy amount
> of data base access in some programs. There are 75 tables in the
> system and some programs access as many as 25 tables.

I am not suggesting or recommending that you SHOULD use Java, but
there is no problem with Java and RDB access.

> 
> If the system is converted to Java, should it use servlets, or Java
> applications on the desktop?
>

Servlets would give more flexibility.

But there are some fundamentals here that seem not to have been
considered.

VA COBOL is capable of doing the whole job so why not just convert it
to that?

It also looks like there is no inherent "Layering" of the Application.

The idea is to separate Database access and User interaction into
their own layers ("tiers"). COBOL lends itself to this. Conversion is
a good opportunity to formalize this distinction. Once you have
decomposed the existing integrated programs along these lines, you
could then decide whether you need/want to use Java for the User
interface, and even if you do, there is certainly no need to use it
for the Data Access layer if you have any qualms or reservations about
doing this. (Actually, once you have your Application layered, you
have many options as to what you can use for the User Interface,
including using the Browser to Web Enable it...)

> What are the good and bad points about VA Cobol?

That would be purely speculation and opinion.

Personally, if I were you, I would concentrate on the existing COBOL
code and look at getting it layered. Once you achieve that, you can
convert it to any version of COBOL you like (VA, MicroFocus, Fujitsu,
Realia, whatever...) and you can use whatever User Interface you think
is appropriate.

Pete.
```

##### ↳ ↳ Re: Visual Age Cobol, or Java ?

- **From:** trento2002@hotmail.com (Harry M)
- **Date:** 2002-12-10T13:09:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8d390f9.0212101309.31cf0aa0@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com>`

```
> > to use DB2 for data base, Linux on the server and Windows on the
> > desktop.
> >
> 
> Is that a choice or is it being dictated by other factors?

These are choices, for the following reasons:
DB2 - Scalability, availability on most OS and hardware.
Linux - Low cost, robustness, and hardware independence.
Windows - Predominance on the desktop.
-------------------------------------------------------------------------

> > If the system is converted to Java, should it use servlets, or Java
> > applications on the desktop?
> >
> 
> Servlets would give more flexibility.

Does using servlets imply that the user interface must be HTML? Or can
regular java graphical objects be used? I have taken a Java course,
but have not used it to do anything of sustance yet.
-------------------------------------------------------------------------

> VA COBOL is capable of doing the whole job so why not just convert it
> to that?

I have been experimenting with VA Cobol for about a year. In some ways
it is so different from HP Cobol as to be a completely new language.
Is it better to spend time on something that is still Cobol, or go
with something that has more flexibility and may have more staying
power, i.e. Java ?
-------------------------------------------------------------------------

> It also looks like there is no inherent "Layering" of the Application.

There is layering of the database access, but not of the user
interface. All database calls are stored in INCLUDE files. The user
interface is using VPLUS, which uses block mode (the entire screen
contents is sent at once). The UI must be redeveloped entirely in
graphical form.
-------------------------------------------------------------------------

> doing this. (Actually, once you have your Application layered, you
> have many options as to what you can use for the User Interface,
> including using the Browser to Web Enable it...)

> Pete.

What would be the steps in Web Enabling, assuming the application were
already layered and converted to VA Cobol?
```

###### ↳ ↳ ↳ HP COBOL vs VA COBOL

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2002-12-10T13:32:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF65D85.E1681E1F@attglobal.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com>`

```
You state that HP and VA COBOL are very different.  Undoubtedly, both
compilers have been blessed as conforming to the ANSI COBOL Standard.  The
standard has relatively few areas that are "implementor defined", and careful
design can usually produce applications that are acceptably efficient and
still protable.

So, are they "very different" because the HP application you speak of made
use of HP extensions to the COBOL language?  If so, you now know (1) why
vendors add extensions to their compilers (to capture their customers), and
(2) why users are well advised to avoid using the extensions (because
sometimes, you need to migrate).

Harry M wrote:

> (snip)
> > VA COBOL is capable of doing the whole job so why not just convert it
…[6 more quoted lines elided]…
> power, i.e. Java ?

(snip)
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-12-11T06:26:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rUAJ9.310776$NH2.21842@sccrnsc01>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com>`

```
"Harry M" wrote:

> I have been experimenting with VA Cobol for about a year. In some ways
> it is so different from HP Cobol as to be a completely new language.
> Is it better to spend time on something that is still Cobol, or go
> with something that has more flexibility and may have more staying
> power, i.e. Java ?

Harry, HP Cobol on the 3000 is licensed technology from Micro Focus. A
migration to another Micro Focus platform would be very easy (at least as
far as the syntax goes). Wrt flexibility, do some research on what each of
the major COBOL vendors has to offer here -- I think you will be surprised
at what COBOL can do today.

One other thing to point out specifically wrt VA COBOL is that it doesn't
seem to be going to 64-bit, nor Linux on z/OS, nor Itanium. Seems more like
a chicken, not a pig.

Gazaloo.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 4)_

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-11T15:19:55
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at7l49$ghj$1@hyperion.microfocus.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01>`

```
This brings us back to Micro Focus. Thanks Gaz ;-)

go to www.microfocus.com and follow the link for white papers. There's a
specific one about HP3000 migrations.

"Gazaloo" <gaz@a.loo> wrote in message
news:rUAJ9.310776$NH2.21842@sccrnsc01...
> "Harry M" wrote:
>
…[13 more quoted lines elided]…
> seem to be going to 64-bit, nor Linux on z/OS, nor Itanium. Seems more
like
> a chicken, not a pig.
>
> Gazaloo.
>
>
```

###### ↳ ↳ ↳ 20 years from now

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-11T17:51:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at7tvo$1hs$1@peabody.colorado.edu>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com>`

```
I'm curious about the future.

In 20 years, will 20 year old programs created from a tool such as Visual Basic
be more maintainable than 40 year old programs created by typing in CoBOL code?

With new Java and Visual Aid tools replacing the old - what types of strategies
are being used to make sure existing applications keep up?
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-12-11T18:14:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2gLJ9.3292$in6.1262@newssvr19.news.prodigy.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```
Based on our predictions in 1980 about what computing would be like in 2000,
I don't anyone is prophetic enough to answer that question, do you?  :)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** "Joe Dzurinda" <jerryc134@home.com>
- **Date:** 2002-12-11T19:02:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ZLJ9.18104$y14.1612052@news1.east.cox.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:at7tvo$1hs$1@peabody.colorado.edu...
> I'm curious about the future.
>
> In 20 years, will 20 year old programs created from a tool such as Visual
Basic
> be more maintainable than 40 year old programs created by typing in CoBOL
code?
>
> With new Java and Visual Aid tools replacing the old - what types of
strategies
> are being used to make sure existing applications keep up?

From what I'm seeing software will have a limited lifespan of maybe 5 years.
I don't think you'll see applications last as long as what some of the old
COBOL systems have done.   Seems like there is always a new process coming
out for developement.   Read some job descriptions out there, 20% of the
things they want in a candidate I have no idea what they are.    And as fast
as you could learn these new tools there will be something newer coming out.
Right now think about where you would go to learn ORACLE or SAP or any of
these new products.   A college?    Very few, they can't keep up with the
technology either.   So that leaves you at the vendors mercy to pay them for
education.

Joe

Joe
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-11T14:46:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212111446.1a4c4f79@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net>`

```
I agree with you Joe.  I have actually seen some of the backlash to
the "write once", "rewrite again" instead of "maintain" mentality. 
It's $$$$ doing the talking.  It's too darn expensive to do this. 
Businesses realize that they are taking a dive throwing money down a
hole chasing new technology for dubious returns.  Maybe 1 in 100 of
these things is a good idea.

"Joe Dzurinda" <jerryc134@home.com> wrote in message news:<3ZLJ9.18104$y14.1612052@news1.east.cox.net>...
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:at7tvo$1hs$1@peabody.colorado.edu...
…[24 more quoted lines elided]…
> Joe
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 8)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-12T17:51:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com>`

```
Thane:

I'm surpised that you would even consider maintaining a program!!  

Because we live in the age of disposability, I buy a new car every
year.  Instead of changing the oil, changing filters, rotating the
tires, checking fluid levels and washing it, I just push it off a
cliff and buy a new one when the next model year comes out. 

After all, these newfangled auto manufacturing technologies make it
very fast and easy to build a car!

;-)

thaneh@softwaresimple.com (Thane Hubbell) wrote:

>I agree with you Joe.  I have actually seen some of the backlash to
>the "write once", "rewrite again" instead of "maintain" mentality. 
…[32 more quoted lines elided]…
>> Joe


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-12T19:04:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atamkr$sdf$1@peabody.colorado.edu>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com>`

```

On 12-Dec-2002, Bob Wolfe <rtwolfe@flexus.com> wrote:

> Thane:
>
…[10 more quoted lines elided]…
> ;-)

On the other hand, when my CPU went bad, I took it out, got out my magnifying
glass and fixed it.   I also fixed my hard drive the same way.

Seriously - I have an old PC that I have connected to my home LAN.  I like
keeping it working and I will install stuff on it that I want to test.  If worse
comes to worse, I can reformat and start over.    It also gives me emergency
access to work in case my main computer goes down.    The other day it's disk
went bad.   I bought a new disk and tried to install it.   The installation
program got stuck.  Since the drive came with a free install (minus data
moving), I took it in to have them format it.   My bios was too old to handle
this new drive.  I could spend $50 for a controller, but I have been planning to
slowly upgrade this computer to be my main one.  I checked to see how much a
motherboard costs.   The new motherboards don't fit this chassis.    I might not
be using much at all of my old computer.

And Microsoft believes nobody will upgrade their hard drive.   I get a new drive
and want to replace my old one.  I don't have any non-update versions of
Windows, and XP thinks I am installing to a new computer anyway, requiring me to
phone Microsoft and tell them it is the same computer.   Half of my software has
ties to the registry and needs to be installed anyway.  My mother uses Outlook
Express.  When she had to reinstall, OE couldn't read her old mail.   That's
because it had been upgraded a bunch of times on line.   The software can't be
copied over, it has to be installed and then upgraded before it will work.   
Microsoft doesn't mind a disposable computer, as long as we buy its products
from scratch.

Upgrading is expensive.  Conversion is expensive.   I can see why enterprises
would rather replace.  Trouble is, they don't have repositories of business
rules to make replacement easy.   Companies can try to be as generic as
possible, so they can use anybody's software - but where's the competitive
advantage in looking just like your competition?
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 10)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-13T13:49:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1pojvusm41bn4sk2t4qsd4gopgdhaavm89@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <atamkr$sdf$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote:

>
>On 12-Dec-2002, Bob Wolfe <rtwolfe@flexus.com> wrote:
…[16 more quoted lines elided]…
>glass and fixed it.   I also fixed my hard drive the same way.

Howard:

Good point, but repair versus replacement should be largely dependent
upon cost factors.  Maintaining an application that cost a half
million or more to create makes more economic sense than repairing a
$200 hard drive or a $150 CPU chip.

>Seriously - I have an old PC that I have connected to my home LAN.  I like
>keeping it working and I will install stuff on it that I want to test.  If worse
…[8 more quoted lines elided]…
>be using much at all of my old computer.

Exactly!  In your case, cost of repair was not practical based upon
economic and technical factors.  The BIOS was outdated and it only
costs $500 to $1,000 to buy a new PC.  I'm not suggesting that repair
and maintenance is ALWAYS the best alternative.  Sometimes it makes
sense to replace and sometimes it makes sense to repair.

>And Microsoft believes nobody will upgrade their hard drive.   I get a new drive
>and want to replace my old one.  I don't have any non-update versions of
…[7 more quoted lines elided]…
>from scratch.

You are 100% correct again!  Microsoft makes more money when we
replace instead of repair, therefore, they will gear their
technological strategies toward replacement rather than repair.....a
la Visual Basic.

>Upgrading is expensive.  Conversion is expensive.   I can see why enterprises
>would rather replace.  Trouble is, they don't have repositories of business
>rules to make replacement easy.   Companies can try to be as generic as
>possible, so they can use anybody's software - but where's the competitive
>advantage in looking just like your competition?

If repair is NOT easy, then repair becomes expensive.  If repair is
more expensive than replacement, then the smart business decision is
to replace.  My only objection is generalization.  To say that
replacement is always a superior business decision over repair is a
generalization.

Sometimes ya gotta replace, but sometimes the smart money is on
repair.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 10)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-13T16:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA0647.5040000@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <atamkr$sdf$1@peabody.colorado.edu>`

```


Howard Brazee wrote:
> 
> On the other hand, when my CPU went bad, I took it out, got out my magnifying
> glass and fixed it.   I also fixed my hard drive the same way.
> 

Howard,

Wow, such reckless abandon. Haven't you ever heard the wise 
proverb:

Never trust a programmer with a screwdriver!

The last time I opened up a computer, my electric 
personality shorted the hard drive controller and the 
motherboard, causing me to have to get a whole new computer. 
  Now I treat computer repairs and upgrades like I treat car 
repairs, I let someone else get their hands dirty.  That 
way, if it doesn't work I can in all honesty shift the blame 
onto someone else. :-)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 9)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-12T19:48:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF8EA3B.8000107@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com>`

```


Bob Wolfe wrote:
> Thane:
> 
…[11 more quoted lines elided]…
> 


Bob,

About those cars, before you push the next one over a cliff, 
let me know.  I'd be willing to pay top dollar for a "junk 
car" that is only one year old.  Top dollar around here is 
US$35.00! :)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 10)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-13T13:58:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hcpjvukh2l2q4s1l079gmttf3272kq7drf@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8EA3B.8000107@nycap.rr.com>`

```
Robert Graham <rgraham2@nycap.rr.com> wrote:

>
>
…[22 more quoted lines elided]…
>US$35.00! :)

Robert:

If I don't push it off the cliff, it's worth a LOT more than $35.00.
Will you go as high as $45.00?

;-)

This issue is near and dear to my heart.  Last weekend, my son wrapped
his 1993 Eagle Talon around a utility pole coming home from church.
He was coming down a hill on an "S" curve, hit loose gravel and lost
control.  (Kid has a "lead foot.")  Luckily, he was unscratched, which
is the most important thing.

But the car was a total loss.  Repairing it would have cost more than
the value of the car and even after it was fixed, it may not have been
100% safe.

Therefore, I sold a car that was worth approximately $4,000 (before
the accident) for $250.  Repair was neither a viable economic or safe
alternative.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 11)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-13T16:02:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA06DE.1010902@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8EA3B.8000107@nycap.rr.com> <hcpjvukh2l2q4s1l079gmttf3272kq7drf@4ax.com>`

```


Bob Wolfe wrote:
> Robert Graham <rgraham2@nycap.rr.com> wrote:
> 
…[40 more quoted lines elided]…
> 

Bob,
I'd go as high as $55.00 if your son hasn't driven it. :-)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 9)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-12T13:13:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF8FBE8.9010800@Sympatico.ca>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com>`

```
Bob Wolfe wrote:

>Thane:
>
…[11 more quoted lines elided]…
>
It is too hard to toss them.  First, you have to get an environmental 
asessment done.  Then you have to have it approved by the municipal 
government.  Then a plebicite. Not only that, but even after you get 
permission to scrap it, you have to take it apart, sort all the letters, 
and separate all the ones from the zeros so that they can be re-cycled, 
wash them, and pack them into two different containers before they will 
take it away.

Donald
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 10)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-13T14:01:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8FBE8.9010800@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote:

>Bob Wolfe wrote:
>
…[22 more quoted lines elided]…
>Donald

Donald:

I disagree!  Zero's are environmentally null, therefore they do not
pose an environmental threat and do not have to be washed.  One's on
the other hand, are extremely toxic and must be disposed of in a high
temperature blast furnace.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 11)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-13T13:09:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212131309.6893cb23@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8FBE8.9010800@Sympatico.ca> <dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com>`

```
Bob Wolfe <rtwolfe@flexus.com> wrote in message news:<dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com>...
> Donald:
> 
…[5 more quoted lines elided]…
> 

I beg to differ.  (I seem to be doing that a lot lately).  Zeros, are
also called O's here in the states (Pronounced OHS).  These recycled
OHS go to the OHS Zone.  This is bad stuff if down low and good stuff
if up high.  It could be all the rewritten Java (And the like) has
contributed more to this OHS Zone than we suspected, being lofty and
all and floating up over the antarctic closing the OHS Zone hole.

Maybe not.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 12)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-13T21:43:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA567F.3000102@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8FBE8.9010800@Sympatico.ca> <dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com> <bfdfc3e8.0212131309.6893cb23@posting.google.com>`

```


Thane Hubbell wrote:
> Bob Wolfe <rtwolfe@flexus.com> wrote in message news:<dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com>...
> 
…[17 more quoted lines elided]…
> Maybe not.

If Java contributed to the OHS Zone, being "lofty and all" 
then wouldn't it be the upper OHS Zone which you said was 
"good".  It is, after all, a high level programming 
language, but then that is also the description of COBOL! :-)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 12)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-14T00:00:09
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfa744a_3@Usenet.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3ZLJ9.18104$y14.1612052@news1.east.cox.net> <bfdfc3e8.0212111446.1a4c4f79@posting.google.com> <crihvusdl20fvj2gepsqoue8kdooedo2pm@4ax.com> <3DF8FBE8.9010800@Sympatico.ca> <dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com> <bfdfc3e8.0212131309.6893cb23@posting.google.com>`

```
ROFL!

Pete.
Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0212131309.6893cb23@posting.google.com...
> Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:<dtpjvug2711vot5kr6q6glndggg36krojd@4ax.com>...
> > Donald:
> >
…[14 more quoted lines elided]…
> Maybe not.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-11T19:25:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CiMJ9.315$qU5.77284@newssrv26.news.prodigy.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:at7tvo$1hs$1@peabody.colorado.edu...
> I'm curious about the future.
>
> In 20 years, will 20 year old programs created from a tool such as Visual
Basic
> be more maintainable than 40 year old programs created by typing in CoBOL
code?

As backwards-incompatible as MS makes VB, twenty years will surely make the
VB programs non-maintainable. Hell, with VB you are SOL after two years or
so.

MCM
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-11T18:26:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212111826.525c47bb@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:<at7tvo$1hs$1@peabody.colorado.edu>...
> I'm curious about the future.
>

No you're not, Howard. You've participated in debates on it for the
last several years. This is just a mischievous troll...<G>
 
> In 20 years, will 20 year old programs created from a tool such as Visual Basic
> be more maintainable than 40 year old programs created by typing in CoBOL code?
> 

Nope. In 20 years neither of these technologies will be around as
viable commercial options.

You are exhibiting the COBOL mindset that says the ONLY way to program
computers is by writing lines of procedural code. It isn't. It WAS.
And it was for many years. Hence it is hard to shake it off for those
of us who were exposed to it most of our working lives. The new
generation (of people...<G>) that will arise within the next 20 years
are unencumbered by such considerations, hence I am fairly confident
that the landslide will gather pace.


> With new Java and Visual Aid tools replacing the old - what types of strategies
> are being used to make sure existing applications keep up?

They are being replaced as quickly as possible, so there is no need to
keep them up.

Pete.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-12T14:51:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ata7qe$jiv$1@peabody.colorado.edu>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <b3638c46.0212111826.525c47bb@posting.google.com>`

```

On 11-Dec-2002, dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

> Nope. In 20 years neither of these technologies will be around as
> viable commercial options.
…[7 more quoted lines elided]…
> that the landslide will gather pace.

I expect you are correct.

> > With new Java and Visual Aid tools replacing the old - what types of
> > strategies
…[3 more quoted lines elided]…
> keep them up.

This will certainly keep programmers employed.  I'm not sure that managers are
ready for disposable IS systems, but I don't see that they will have a choice.

What is interesting is the current emphasis in auditing.  This can be helped by
separating data from process (which is an anti-OO concept).  But when companies
have million dollar fines for not archiving e-mail, maybe they need to archive
old business rules as well.   I do NOT have a handle on likely scenarios once
this paradigm shift is complete and they want stability and accountability while
IS systems get replaced that often.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-12T09:34:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212120934.3f0f7e7b@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <b3638c46.0212111826.525c47bb@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0212111826.525c47bb@posting.google.com>...

Stuff snipped.... pardon if this is a repeat, I don't think the last
version posted.

> 
> > With new Java and Visual Aid tools replacing the old - what types of strategies
…[4 more quoted lines elided]…
> 

What follows is slightly tounge in cheek, but like all satire has an
element of truth.  Personally I think the amount of COBOL out there is
still increasing, but because of what follows we might be on the
downslide:

Company X has COBOL based system.  Decides to "Modernize".  Conversion
to ...Fill in the blank...

SAP
BAAN
PeopleSoft
Oracle
Java
C++
VB
etc... etc..

Spends millions on conversion efforts over months or years.  
Ends up with:

System with partial capability compared to original.
Things work different.
Some things better, mostly things the same.
Users upset.
Recovery of $$ slow or non existent.
Disruption caused loss of business.
Best option appears to fold or declare bankruptcy.
Maybe someone will buy us.

Result - Less COBOL - Mission accomplished.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 8)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-12-12T17:53:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021212125321.15108.00000009@mb-fe.aol.com>`
- **References:** `<bfdfc3e8.0212120934.3f0f7e7b@posting.google.com>`

```
Ouch! But as you say, at least some truth to it.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-13T23:41:18
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfa731a_11@news.newsgroups.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <b3638c46.0212111826.525c47bb@posting.google.com> <bfdfc3e8.0212120934.3f0f7e7b@posting.google.com>`

```
I loved it, Thane!

Here is the response from an unnamed Director of the said Company....

Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0212120934.3f0f7e7b@posting.google.com...
>
> What follows is slightly tounge in cheek, but like all satire has an
…[7 more quoted lines elided]…
> SAP
Siebel
Chordiant
JD Edwards
> BAAN
> PeopleSoft
…[6 more quoted lines elided]…
> Spends millions on conversion efforts over months or years.

As opposed to spending millions maintaining  our COBOL IT department for a
year? <G>

> Ends up with:
>
> System with partial capability compared to original.

Because the Business and IT didn't do the job right... They interpreted all
the new capability in terms of what they were used to...some ancient
techspeak called SNOWBALL or COBBLERS or something... instead of really
understanding what it could do. I had lunch with the CEO of Mickey Mouse
Packages and he TOLD me what great capabilities their Package has...
Besides, it is used by 499 of the Fortune 500. We bought the best; it was
just the incompetence of our people that caused the failure...

> Things work different.

Because they couldn't understand the new User Interface and they didn't
educate themselves and the Business towards using it.

> Some things better, mostly things the same.
> Users upset.

Because the Business changed during the conversion, but all system
functionality was "frozen" while conversion was carried out...


> Recovery of $$ slow or non existent.

Exactly the same rate of return as we've had on every COBOL project we wrote
during the last 30 years...

> Disruption caused loss of business.

Ah, they were all malcontents...we could afford to lose them. Cost us more
than they were worth to service them...<G>


> Best option appears to fold or declare bankruptcy.

Chapter 11 while we surreptitiously buy shares back at rock bottom price...
I expect to own a small island in a warm place by Xmas...

> Maybe someone will buy us.
>

We are already in talks with our major competitor... That was what we wanted
all along....

> Result - Less COBOL - Mission accomplished.

COBOL? Sounds like a distant planet... Never heard of it and don't care
whether we have less of it or not. I leave all that techie stuff to our IT
director... Of course, I'll be firing him for incompetence later this
afternoon, but I understand he already has another job with the package
vendor...

Pete.





-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2002-12-12T07:16:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0212120716.6d6aff9d@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:<at7tvo$1hs$1@peabody.colorado.edu>...
> I'm curious about the future.
> 
…[4 more quoted lines elided]…
> are being used to make sure existing applications keep up?

<food_for_thought>

I am already in a mode where I write more programs to generate
production programs than I write actual production programs.

This seems to be a reasonable direction.  Software can write software
far faster than wetware can...

</food_for_thought>
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-12T17:49:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x_3K9.812$qU5.247489@newssrv26.news.prodigy.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <dcedb8d0.0212120716.6d6aff9d@posting.google.com>`

```
"Joe Zitzelberger" <jzitzelb@tsys.com> wrote in message
news:dcedb8d0.0212120716.6d6aff9d@posting.google.com...

> Software can write software far faster than wetware can...

But wetware writes it better.

MCM
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-12T17:26:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atagsh$ouh$1@peabody.colorado.edu>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <dcedb8d0.0212120716.6d6aff9d@posting.google.com> <x_3K9.812$qU5.247489@newssrv26.news.prodigy.com>`

```

On 12-Dec-2002, "Michael Mattias" <michael.mattias@gte.net> wrote:

> > Software can write software far faster than wetware can...
>
> But wetware writes it better.

Often.    But give management a choice between faster and better, they will
almost always prefer faster - as long as it is good enough.   This is especially
true with disposable software.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 6)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-12T19:52:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF8EB25.2020301@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu>`

```


Howard Brazee wrote:
> I'm curious about the future.
> 
…[4 more quoted lines elided]…
> are being used to make sure existing applications keep up?


The answer is:  WHO CARES?!?  In 20 years, nearly everyone 
who is posting to this newsgroup (with the exception of the 
people who ask for help and are invariably flamed) will be 
retired and hopefully living on "easy street". ;-)
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 7)_

- **From:** "db2ims" <xdb2imsN@nospam.whatever.net>
- **Date:** 2002-12-13T08:50:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oAlK9.16639$PF2.1329009@news20.bellglobal.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <rUAJ9.310776$NH2.21842@sccrnsc01> <at7l49$ghj$1@hyperion.microfocus.com> <at7tvo$1hs$1@peabody.colorado.edu> <3DF8EB25.2020301@nycap.rr.com>`

```
"Robert Graham" <rgraham2@nycap.rr.com> wrote in message
news:3DF8EB25.2020301@nycap.rr.com...
>
>
…[3 more quoted lines elided]…
> > In 20 years, will 20 year old programs created from a tool such as
Visual Basic
> > be more maintainable than 40 year old programs created by typing in
CoBOL code?
> >
> > With new Java and Visual Aid tools replacing the old - what types of
strategies
> > are being used to make sure existing applications keep up?
>
…[5 more quoted lines elided]…
>
I do.

I've been programming Cobol for 21 years and I'm only in my mid forties.  I
plan to still be programming 20 years from now.  They'll have to pry this
keyboard away from my cold dead fingers!   :-D
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 8)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-12-13T14:43:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021213094335.07110.00000033@mb-mu.aol.com>`
- **References:** `<oAlK9.16639$PF2.1329009@news20.bellglobal.com>`

```
Robert Graham writes ...

>> Howard Brazee wrote:
>> > I'm curious about the future.
…[20 more quoted lines elided]…
>keyboard away from my cold dead fingers!   :-D

Not mention the fact that some of us older folks might not be retired in 20
years! Look at what the market has done to your retirment account.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-13T15:53:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atcvp9$en5$1@peabody.colorado.edu>`
- **References:** `<oAlK9.16639$PF2.1329009@news20.bellglobal.com> <20021213094335.07110.00000033@mb-mu.aol.com>`

```

On 13-Dec-2002, scomstock@aol.com (S Comstock) wrote:

> Not mention the fact that some of us older folks might not be retired in 20
> years! Look at what the market has done to your retirment account.

If you are retiring in 20 years, what the market has done to your retirement
account isn't important.   You just don't want to retire when the market is down
and as you get closer, move to a safe investment.   When the market is down -
buy.

People who are hurt are those depending upon income now, or who have to sell
now.   You know it averages out in the long run.
```

###### ↳ ↳ ↳ Re: 20 years from now

_(reply depth: 9)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-13T16:06:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA07D4.1040006@nycap.rr.com>`
- **References:** `<oAlK9.16639$PF2.1329009@news20.bellglobal.com> <20021213094335.07110.00000033@mb-mu.aol.com>`

```


S Comstock wrote:
> Robert Graham writes ...
> 
…[39 more quoted lines elided]…
> Steve Comstock

That is true.  Enron and Worldcom really caused my 
retirement fund to take a hit.  I guess the mutual funds had 
too much in tech stocks.  I've since moved it, but since 
I've not got ESP... :(

WELCOME TO WAL-MART.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-11T03:43:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212110343.4fbd2b47@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com>`

```
Harry, you have received some good replies in this thread.

Check out Bob Wolfe's Flexus SP2. I haven't used it but the reports
are good.

Some of what you are asking is beyond the scope of this thread, but I
have tried to give quick responses below...

Pete.

trento2002@hotmail.com (Harry M) wrote in message news:<b8d390f9.0212101309.31cf0aa0@posting.google.com>...
> > > to use DB2 for data base, Linux on the server and Windows on the
> > > desktop.
…[9 more quoted lines elided]…
> 
OK. All arguable but I have no intention of arguing it here..<G>

> > > If the system is converted to Java, should it use servlets, or Java
> > > applications on the desktop?
…[6 more quoted lines elided]…
> but have not used it to do anything of sustance yet.

No, it does not imply using HTML. But it would be foolish not to...
Server side code can obviously NOT present graphics directly to the
User (they would only show on the server and that kind of defeats the
object (pardon the pun <G>))

Servlets need not interact with the user at all, but if they do, they
should do so through HTML (or XML or similar). This would be true of
ANY server side script.



> -------------------------------------------------------------------------
> 
…[7 more quoted lines elided]…
> power, i.e. Java ?

Go with the best tool for the job. It looks to me like the minimum
conversion effort will be obtained using COBOL, so that is what I
would go for. Besides, this code is debugged and implemented. For
myself, I would simply wrap it as COM and implement it as Web Based.
Java has no more flexibility than COBOL and its staying power is yet
to be decided. I can't comment on the differences as I have never used
HP3000 COBOL (It must be just about the only one I haven't <G>).

> -------------------------------------------------------------------------
> 
…[6 more quoted lines elided]…
> graphical form. 

Well, I'm not so sure... The current "full screen" processing can be
utilised under Windows and the Web (I have a number of applications
that deal with screens (Forms) rather than field by field processing.)
The DB layering is good news and you should be able to port this
directly to the new environment (recompiled to whatever you decide to
use, of course...).


> -------------------------------------------------------------------------
> 
…[7 more quoted lines elided]…
> already layered and converted to VA Cobol?

A full description is beyond the scope of this forum and besides, I
would charge you for a complete solution...<G> (Hey! I have to make a
living too, y' know...<G>). I can point you in the right direction,
though...

1. Ensure that all programs that currently contain User Interface
become callable modules with the fields they currently process passed
to them through linkage.

2. Implement code to obtain these fields from Web forms which can be
managed by just about anything (Java, ASP,HTML/XML, SP2(?), etc.)
(There is some trickiness required in doing this with COBOL but I have
managed it. Fujitsu provide great tools for this, but I'm sure
everybody else does too.) I found one Fujitsu tool that simply didn't
work, and finally I just wrote myself a tool to provide the same
function. (I can make this available to anybody who has the same
problem I had... it is to do with generating HTML for output.)

3. The response to the user must be written in generated HTML. This is
achieved by Java Servlet, COBOL CGI/ISAPI, ASP or any of a number of
tools. The point is that there are many ways to achieve what you are
after, and a lot of balancing needs to be done and thought given to
it.

The hardest part is probably interfacing the various tools. But it can
be done. After some practice you get pretty blase about it...<G>.

Split your existing code into functions (modules) that can be called.
(eliminate the standalone concept). Where and what you call these
modules from is then a matter of choice.

COBOL components work fine on the Web or in Windows. 

Good Luck!

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-11T17:40:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

>Harry, you have received some good replies in this thread.
>
>Check out Bob Wolfe's Flexus SP2. I haven't used it but the reports
>are good.

Pete:

Thank you!  Very kind of you, good sir.

I'm not sure if I have mentioned this before, but we also happen to
share the same mantra........

"Go with the best tool for the job."

Sucessful projects are usually the result of very careful management
analysis of skillsets, available personnel and the requirements of the
application to be written.....in this business, there really is no
such thing as "one size fits all."

Now...if I could also indulge upon you to send some of your warm
summer weather to us, I would be most grateful.....we're experiencing
an ice storm at the moment.

[snip]



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-11T17:54:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at7u4q$1ib$1@peabody.colorado.edu>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com>`

```

On 11-Dec-2002, Bob Wolfe <rtwolfe@flexus.com> wrote:

> "Go with the best tool for the job."

One problem people have is identifying the job.    Who gets promoted for picking
the best product for producing something that will work well in 20 years?   Is
the job getting the code out today?   Is the job getting a system that will
continue working?

Sometimes it is one, sometimes it is the other.   NASA could have saved
themselves lots of money by not designing their software until the last minute,
waiting for technology to catch up - and throwing it out after each flight...
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-12T07:12:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212120712.381e77c4@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <at7u4q$1ib$1@peabody.colorado.edu>`

```
Superb Howard!

This post really made me think. It is so obvious and yet so
overlooked...

Comments below...

Pete.
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:<at7u4q$1ib$1@peabody.colorado.edu>...
> On 11-Dec-2002, Bob Wolfe <rtwolfe@flexus.com> wrote:
> 
…[6 more quoted lines elided]…
>

This is extremely relevant.

There are always such pressures on the person who has to do the job
that it is easy to forget there are likely to be a number of "vested
interests" who will all perceive the "job" with a slightly different
spin. There are also likely to be a number of conflicting constraints
as Howard has outlined above.

I'm honestly not sure of the best way to address this.

If you use RAD,it will be addressed by Joint Development Workshops
that have all the "stakeholders" either in attendance, or represented.
Solutions are selected only after the Requirements have been
extracted, agreed by all concerned, and prioritised. "Requirements"
could/would include the factors that Howard has mentioned.

If you DON'T use RAD, (and, sadly, in my opinion, most sites don't,
because of what "everybody knows" about it, horror stories that have
become "IT urban myth", or someone knew somebody who worked on a
disastrous RAD team, <G>...), I don't see how this can be properly
addressed.

If the choice of tool is left to the programmer, he/she will choose
what they are most familiar with and the issues above will not be
addressed. If the choice of tool is left to the Business, they will
not understand what is required for the best technical implementation.

Howard is right when he says that people don't get promoted for
picking the best tool that meets one or other of the criteria...

But, people DO get promoted for consistently implementing projects on
time. So a tool or way of working that increases productivity is
likely to be viewed as a "Good Thing".

I hadn't thought of this before but I believe that getting things
implemented as quickly as possible (rightly or wrongly...) is the most
important criterion because that is what determines and measures
people's performance, and performance is what determines their future.

So you could argue that systems fall short because we are developing
systems that reward the people implementing them, rather than meeting
the requirements of the Business! (Of course, in reality it will be a
path that does both of these but it is pretty obvious which one has
the priority <G>.)


"The Best Tool for the job..." must ensure that EVERYBODY has a very
clear idea of what the "job" is...

> Sometimes it is one, sometimes it is the other.   NASA could have saved
> themselves lots of money by not designing their software until the last minute,
> waiting for technology to catch up - and throwing it out after each flight...

Hahaha! Why stop at computer technology? They could have waited for
bigger and better rockets, and infrastructure. In fact, they could
have waited until the invention of warp drive before going to the
moon...

But then, there wouldn't have been bigger and better rockets if nobody
had been using the existing ones and requiring more...<G>.

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-12T20:25:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3df8f0c7_3@Usenet.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com>`

```
Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com...
> dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:
>
…[6 more quoted lines elided]…
>
Ah, now I am convinced you haven't read my posts...<G>

I am currently in the Midlands of England and it is snowing outside. It is
really quite beautiful.The pond in my garden has a layer of ice on it and
all the fish are deep down and hibernating.

The thermometer outside my kitchen window read -2 this morning but it is now
on zero.

I have a roaring log fire in the lounge and the cottage is centrally heated
so there is no problem there.

Er... just exactly what part of this scenario would you like me to send
you...<G>

Pete.

>
>
…[4 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 6)_

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-12-12T23:47:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be9K9.129171$pN3.8932@sccrnsc03>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:
> Er... just exactly what part of this scenario would you like me to send
> you...<G>

You can just send me any real ale you may have in your fridge and if I drink
enough I can centrally heat myself (hypothermia later, but that's hours
away).

Gazaloo.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 7)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-13T07:36:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212130736.11430db5@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03>`

```
"Gazaloo" <gaz@a.loo> wrote in message news:<be9K9.129171$pN3.8932@sccrnsc03>...
> "Peter E. C. Dashwood" wrote:
> > Er... just exactly what part of this scenario would you like me to send
…[6 more quoted lines elided]…
> Gazaloo.

Hahaha! Real ale is NEVER refrigerated... That was something it took
me a long time to come to grips with when I first came here <G>.
Having been raised on cold beer, I found it outrageous that here they
drink it "warm". (Actually, because it is cellared, it is usually
cooler than room temoperature, but nowhere near what we call cold
beer...).

They also give me very funny looks when I insist on having (lots
of...) ice in my Jack Daniels <G>.

Speaking of real ale, I have some "Old Speckled Hen" in the larder...
a good drop.

But a local friend has assured me that "Bazzie's Bonce Blower", a Real
Ale brewed in Rutland (about 25 miles East of the city of Leicester)
is the strongest beer in the World. He cites the Guiness Book of
Records as agreeing...
In the keg it is 23% ABV!!! (Alcohol By Volume), and in the bottle,
12% ABV. I do plan on getting some of this....it is about an hour's
drive from where I am currently living to the brewery, so I'll report
to CLC (if I can still type <G>) after I try some of it.

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 8)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-13T16:10:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA08B7.2000006@nycap.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com>`

```


Peter E. C. Dashwood wrote:
> "Gazaloo" <gaz@a.loo> wrote in message news:<be9K9.129171$pN3.8932@sccrnsc03>...
> 
…[13 more quoted lines elided]…
> me a long time to come to grips with when I first came here <G>.

That's because the UK only discovered refregeration within 
the last 40 years, and being strong on tradition have 
refused to enter into the 20th. century (let alone the 
21st.)  At least where drinking is concerned. :D
```

###### ↳ ↳ ↳ OT: Ale (was Re: Visual Age Cobol, or Java ?)

_(reply depth: 8)_

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-12-13T16:18:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4LnK9.138016$pN3.10097@sccrnsc03>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com>`

```
"Peter E. C. Dashwood" wrote:
> Hahaha! Real ale is NEVER refrigerated... That was something it took
> me a long time to come to grips with when I first came here <G>.

Blimey, I've been in the US too long. My US passport may be a good indicator
of this, but somehow making the connection between real ale and a fridge,
really rams it home. I'm an english country boy, brought up on "warm" ale.

> Speaking of real ale, I have some "Old Speckled Hen" in the larder...
> a good drop.

'Tis.

> But a local friend has assured me that "Bazzie's Bonce Blower", a Real
> Ale brewed in Rutland (about 25 miles East of the city of Leicester)
> is the strongest beer in the World. He cites the Guiness Book of
> Records as agreeing...

This looks like it?

http://www.beerguide.co.uk/towns/somerby.htm

Just in case anyone else wants to try!

> In the keg it is 23% ABV!!! (Alcohol By Volume), and in the bottle,
> 12% ABV. I do plan on getting some of this....it is about an hour's
> drive from where I am currently living to the brewery, so I'll report
> to CLC (if I can still type <G>) after I try some of it.

The taste may be a little "odd" because of the strength, but stick with it
Pete. 4 or 5 pints should have be enough to master it.

Gazaloo.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-12-14T05:15:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2a32f$b06e3c40$86c2f943@chottel>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com>`

```
Be careful Pete! I seem to recall James Herriot drinking some homemade wine
which resulted in various part of his anatomy becoming partially paralyzed
for a while.

Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote in article
<b3638c46.0212130736.11430db5@posting.google.com>...
> "Gazaloo" <gaz@a.loo> wrote in message
news:<be9K9.129171$pN3.8932@sccrnsc03>...
> > "Peter E. C. Dashwood" wrote:
> > > Er... just exactly what part of this scenario would you like me to
send
> > > you...<G>
> > 
> > You can just send me any real ale you may have in your fridge and if I
drink
> > enough I can centrally heat myself (hypothermia later, but that's hours
> > away).
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 9)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-16T03:49:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212160349.16952160@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com> <01c2a32f$b06e3c40$86c2f943@chottel>`

```
"Charles Hottel" <chottel@cpcug.org> wrote in message news:<01c2a32f$b06e3c40$86c2f943@chottel>...
> Be careful Pete! I seem to recall James Herriot drinking some homemade wine
> which resulted in various part of his anatomy becoming partially paralyzed
> for a while.
> 

Ah, with the state of my social life at the moment, I wouldn't even
notice...<G>

I am just too tired at the end of the day to want to venture into the
fleshpots of Birmingham. And the weekends are spent re-charging for
the coming week.

As a result, most of my social interaction is through work, and I make
it a policy never to get involved with people I work with. (As a
friend expressed it to me many years ago...: "Never get your meat
where you get your bread and butter". On the very rare occasions where
I broke this rule over the years it invariably ended in disaster.)

The only way I stay sane is by reminding myself that this intensive
effort is for a finite period of time, and will enable me to return
home and do whatever I want to.

Everybody needs a goal... <G>

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 10)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-12-16T14:00:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFDDC8E.2090505@optonline.NOSPAM.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com> <01c2a32f$b06e3c40$86c2f943@chottel> <b3638c46.0212160349.16952160@posting.google.com>`

```
Peter E. C. Dashwood wrote:
> "Charles Hottel" <chottel@cpcug.org> wrote in message news:<01c2a32f$b06e3c40$86c2f943@chottel>...
> 
…[16 more quoted lines elided]…
> where you get your bread and butter".

Moses?
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 11)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-17T03:58:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212170358.4f62e6e1@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <be9K9.129171$pN3.8932@sccrnsc03> <b3638c46.0212130736.11430db5@posting.google.com> <01c2a32f$b06e3c40$86c2f943@chottel> <b3638c46.0212160349.16952160@posting.google.com> <3DFDDC8E.2090505@optonline.NOSPAM.net>`

```
Liam Devlin <LiamD@optonline.NOSPAM.net> wrote in message news:<3DFDDC8E.2090505@optonline.NOSPAM.net>...
> > 
> > As a result, most of my social interaction is through work, and I make
…[4 more quoted lines elided]…
> Moses?

Hahaha! (I guess it SHOULD have been...<G>)

While the manager of your local Supermarket would vehemently refute
this statement, I have found it to be very good advice...

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 6)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-13T14:13:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

>Bob Wolfe <rtwolfe@flexus.com> wrote in message
>news:vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com...
…[13 more quoted lines elided]…
>all the fish are deep down and hibernating.

I just looked at the "NZ" extension in the e-mail address.

I receive about 150 e-mail messages a day (about 50% spam) in addition
to the newsgroup posts and have to scan my messages rapidly.  You're
correct in that I do tend to pass over a lot of the personal stuff.

The internet makes it more difficult to determine a person's precise
location.  For example, I use 2 different domains depending upon
whether I am working at home or in the office.  Without scouring the
header, it would be impossible for anyone to know from which location
I am responding.  But in your case, I did indeed miss the fact that
you aren't south of the equator.  I admit guilt for not scrutinizing
and committing to memory each and every line of each and every one of
your postings.  But I do read them.

Sorry for missing your current location.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-13T23:19:42
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfa6be6$1_11@news.newsgroups.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com>`

```

Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:
>
…[3 more quoted lines elided]…
> your postings.

Ah, the brain cells that would take...
It's all right, Bob... you cherish the few you have left...<G>


> But I do read them.
>
> Sorry for missing your current location.

Not a problem. I would only EXPECT you to read my posts if you intended to
argue with me...
(BTW, I always read your posts...<G>)

Pete.




-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-14T17:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFB6B1E.B4B745B4@Azonic.co.nz>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com>`

```
Peter E. C. Dashwood wrote:
> 
> Not a problem. I would only EXPECT you to read my posts if you intended to
> argue with me...
> (BTW, I always read your posts...<G>)

Always well prepared to leap into an arguement without delay ?  ;-)
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-14T11:21:36
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfd95f6_1@Usenet.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <3DFB6B1E.B4B745B4@Azonic.co.nz>`

```
Absolutely! (But you knew that already...<G>)

Pete.
Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3DFB6B1E.B4B745B4@Azonic.co.nz...
> Peter E. C. Dashwood wrote:
> >
> > Not a problem. I would only EXPECT you to read my posts if you intended
to
> > argue with me...
> > (BTW, I always read your posts...<G>)
>
> Always well prepared to leap into an arguement without delay ?  ;-)



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 8)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-16T13:54:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

>
>Bob Wolfe <rtwolfe@flexus.com> wrote in message
…[8 more quoted lines elided]…
>Ah, the brain cells that would take...

Pete:

This is rather insulting.  I'm not sure what I have written to deserve
such disrespect from you.  I'll take the high road and assume that you
read my message, but may not have comprehended what I was saying.  Had
you comprehended my posting, a more correct response would have
been...

"Ah, the time that it would take to read the inumerable paragraphs
from each and every message."

>It's all right, Bob... you cherish the few you have left...<G>

Pete....I am shocked, surprised and saddened that a professional such
as yourself would resort to such statements.

>> But I do read them.
>>
…[3 more quoted lines elided]…
>argue with me...

I never argue.  It's a pointless activity.  While it is perfectly
acceptable to state an opposing opinion, argument is a huge waste of
everyone's time and energy.

>(BTW, I always read your posts...<G>)

But reading and digesting are two different things.  From your
comments attacking my intellect above, regardless of the fact that I
expressed myself clearly and concisely, I suspect that you did not
comprehend my statements.

I am confident in saying that I have never resorted to insulting you
when I happened to disagree with your opinions.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-17T08:41:32
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfee300_3@Usenet.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com>`

```
Bob,

please do a quick check and ensure that your sense of humour is still
intact.

My comments were tongue in cheek and not intended to be offensive...that's
why there is a GRIN attached to it.

The brain cells joke was against myself, as I know some of my posts are too
long.

You are much too easily "insulted" for a public forum. No offense was
intended.

...more below...

Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:
>
…[27 more quoted lines elided]…
>

Well, you're right. I wouldn't. And I didn't...(at least, not in
seriousness..)

> >> But I do read them.
> >>
> >> Sorry for missing your current location.
> >
> >Not a problem. I would only EXPECT you to read my posts if you intended
to
> >argue with me...
>
…[3 more quoted lines elided]…
>

Philosophical argument is an essential part of the learning and growth path.
When I do it, it is never pointless <G>.

> >(BTW, I always read your posts...<G>)
>
…[4 more quoted lines elided]…
>

Again, you missed the subtlety of this...it was another joke against myself.
Richard picked it up...

> I am confident in saying that I have never resorted to insulting you
> when I happened to disagree with your opinions.
>

Nor I you. Get over it.

Pete.





 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 10)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-17T13:48:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<umauvucgis46apjlbncivjosinvl1v01qf@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com>`

```
Peter:

No offense taken.  I was just a bit surprised.

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

>Bob,
>
…[93 more quoted lines elided]…
>                http://www.usenet.com


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 11)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-18T07:19:19+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atobc2$2sj@netnews.hinet.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com>`

```
I have been reading this thread although quite absent-minded.
All I can recall is that COBOL's future is  in question.

From the beginning of the age of WINTEL, there are so many
developing languages come, BASIC, Q-BASIC, DBASE, FOXBASE,
C-series, VB, DELPHI(once called VB killer), and now JAVA etc, and go.
I think SAP,  ORACLE and others are kinds of  developing tools, too.
These tools are appears in the maeket to answer new demands, mainly
GUI, TCP/IP, and INTERNET.

The COBOL is too slow in response to these new demands, that's
why COBOL looks dying.  It is in fact the COBOL vendor's  responsibilities
and attitudes.
I used MF from 2.2 to v3.1, 4.0, finally netexpress 3.0.
MF is not friendly to its user. After a crash of my HD and failure to get a
revoke key from MF, I switched to Fujitsu COBOL.

Adding to my dissatisfaction to  the cobol vendor is that I have spent
so much money on buying other tools, DELPHI and its add-ons,
J-BUILBER, INTRABUILDER, CENTURA, VB, M$'s bulky visual studio
and others. I didn't switch successfully because I got millions of lines of
cobol
codes and cobol files to mantain and convert, and I didn't have that much
time.

Futunately, COBOL vendors slowly catch up, and all the new features
can be found in COBOL language or add-on tools.

I read a local news several months ago, that in its lawsuit
M$ reveals its WINDOW OS source codes and to everybody's surprise
it is written in  BASIC language, millions of lines, not C nor JAVA.

So, as long as  COBOL can add new features to answer new demands
, it is going to be lingering like the turtle in the race against rabbits.

jason mo


"Bob Wolfe" <rtwolfe@flexus.com> ?????
news:umauvucgis46apjlbncivjosinvl1v01qf@4ax.com...
> Peter:
>
…[9 more quoted lines elided]…
> >My comments were tongue in cheek and not intended to be
offensive...that's
> >why there is a GRIN attached to it.
> >
> >The brain cells joke was against myself, as I know some of my posts are
too
> >long.
> >
…[16 more quoted lines elided]…
> >> >> and committing to memory each and every line of each and every one
of
> >> >> your postings.
> >> >
…[26 more quoted lines elided]…
> >> >Not a problem. I would only EXPECT you to read my posts if you
intended
> >to
> >> >argue with me...
…[6 more quoted lines elided]…
> >Philosophical argument is an essential part of the learning and growth
path.
> >When I do it, it is never pointless <G>.
> >
…[8 more quoted lines elided]…
> >Again, you missed the subtlety of this...it was another joke against
myself.
> >Richard picked it up...
> >
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-17T19:00:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212171900.471c45cc@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net>`

```
"jason" <not-real@ms88.hinet.net> wrote 

> These tools are appears in the maeket to answer new demands, mainly
> GUI, TCP/IP, and INTERNET.
> 
> The COBOL is too slow in response to these new demands, that's
> why COBOL looks dying.  

My first fully graphics GUI program in Cobol was done using MF 2.5 in
1991 when Windows 3.0 was the latest thing.

I did Cobol CGI over 5 years ago - without waiting for vendors or
third parties.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 13)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-19T08:12:21+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atr2rf$mi6@netnews.hinet.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <217e491a.0212171900.471c45cc@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> ?????
news:217e491a.0212171900.471c45cc@posting.google.com...
> "jason" <not-real@ms88.hinet.net> wrote
>
…[10 more quoted lines elided]…
> third parties.

Actually I used MicroSoft Cobol 2.2 and then 3.0. I didn't know it was OEM
from MF
nor there was Dialog System until I purchased MF3.1. I thought Dialog too
expensive
so I didn't buy. I also didn't take 16-bit graphic window seriously until
win95
became popular.  Then Dialog system was no match for other visual tools so
I never use it.

Current I use Fujitsu Cobol   doing  ISAPI,  and plan to use SP2 thinclient
for tcp/ip.
I am also thinking Fujitsu Cobol for .net application.  I am still cobol-er,
too.

jason
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 12)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-18T06:55:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1_UL9.5403$KW2.344100@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net>`

```

"jason" <not-real@ms88.hinet.net> wrote in message news:atobc2$2sj@netnews.hinet.net...
> I have been reading this thread although quite absent-minded.
> All I can recall is that COBOL's future is  in question.
>

Well, the future of COBOL is not in question really; it will continue to be used in hundreds of thousands of applications, and
continue to be used to develop new programs for quite some time to come. The argument that "no new applications are bing written in
COBOL" is however, at least partially true.

On the mainframe, an "application" often consists of hundreds, sometimes thousands, of different programs. There are not many new
"applications" being started today period, mostly because they are expensive to create (in any language!) and there just isn't any
driving need for new applications. Enhancments, and "ports to the Web" sure, but not new applications. Even those "ports to the web"
do not often replace the batch processes at the core of most applications. They just add a nice GUI interface.

Also, you don't hear much about those applications these days either; for good reason. Those applications are the lifeblood of most
companies and are guarded pretty jealously.


> From the beginning of the age of WINTEL, there are so many
> developing languages come, BASIC, Q-BASIC, DBASE, FOXBASE,
…[4 more quoted lines elided]…
>
'WINTEL' as you name it, really has very few true business processing applications, and those it does
have are usually custom. The typical business running on Quickbooks will almost always find themselves
outgrowing what theyare running on. They would be better served to pick up on a hosted application in
most cases, though they don't know it, and the WINTEL crowd simply has not got it yet.

The areas you pointed out, and others like E-Mail are served well by WINTEL, though I can not think of a single example that cannot
be served as well -- usually better! -- by UNIX. Both Windows and UNIX are very different from a mainframe or host based
applications, and they are also very different from each other.


> The COBOL is too slow in response to these new demands, that's
> why COBOL looks dying.  It is in fact the COBOL vendor's  responsibilities
> and attitudes.

Nope- it is just there are too many people who realized there was buck to be made in the PC market. Microsoft, for example, if all
the time coming out with things that are "new and revolutionary", but have been the norm in the mainframe world for decades. Little
things, like LPARS, still elude them though.

Oh yes, and one other thing that holds us mainframe/COBOL/assembler/CICS types back. We are all trained to think of efficiency
first, which definitely has advantages. But it also has a terrific disadvantage; Microsoft has gained a lot of market share by
putting out really slow and bloated code, and then depending upon advances in hardware to make it run "fast enough" to be accepted.
Most COBOL programmers are just not trained that way.

Perhaps, we, and the COBOL vendors, should rethink our thinking in that area. It is difficult to even suggest that idea though! :)

-Paul
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 13)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-19T07:53:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atr1ol$hs9@netnews.hinet.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <1_UL9.5403$KW2.344100@twister.austin.rr.com>`

```

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> ���g��l��
news:1_UL9.5403$KW2.344100@twister.austin.rr.com...
> On the mainframe, an "application" often consists of hundreds, sometimes
thousands, of different programs. There are not many new
> "applications" being started today period, mostly because they are
expensive to create (in any language!) and there just isn't any
> driving need for new applications. Enhancments, and "ports to the Web"
sure, but not new applications. Even those "ports to the web"
> do not often replace the batch processes at the core of most applications.
They just add a nice GUI interface.
>
> Also, you don't hear much about those applications these days either; for
good reason. Those applications are the lifeblood of most
> companies and are guarded pretty jealously.
>
…[8 more quoted lines elided]…
> 'WINTEL' as you name it, really has very few true business processing
applications, and those it does
> have are usually custom. The typical business running on Quickbooks will
almost always find themselves
> outgrowing what theyare running on. They would be better served to pick up
on a hosted application in
> most cases, though they don't know it, and the WINTEL crowd simply has not
got it yet.
>
> The areas you pointed out, and others like E-Mail are served well by
WINTEL, though I can not think of a single example that cannot
> be served as well -- usually better! -- by UNIX. Both Windows and UNIX are
very different from a mainframe or host based
> applications, and they are also very different from each other.

I had workd on IBM aminframe CICS using ASSEMBLER, RPG2 and COBOL, but
that was 20 years ago.

A local nootbook computer manufacturer with annual sales over $5 billions,
using clustered WINTEL   for thier information processes.
they don't use UNIX nor mainframe becuase of keeping compatibility and
easiness to maintain.
My point is "cluster" of small common things is the trend of future
developmet, so
riding on WINTEL or WINAND is good enough for most of us,  I guess.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 14)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-19T03:16:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GSaM9.14773$Nz5.401618@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <1_UL9.5403$KW2.344100@twister.austin.rr.com> <atr1ol$hs9@netnews.hinet.net>`

```

"jason" <not-real@ms88.hinet.net> wrote in message news:atr1ol$hs9@netnews.hinet.net...
>
> >
…[16 more quoted lines elided]…
>

Hardlly.

First off, take your $5 billion/year notebook company - who are they? And what are they running?
In particular, what the heck are they using for the accounting, inventory, billing, and manuafacturing process software? I find it
really difficult to accept they are running solely under Windows. Much more likely they have the system outsourced to an accounting
agency or something. Oh, and compatibility with *what*?

Your idea of clustering has some value I am sure, but in terms of economy, efficiency, and pure raw capabilty, centralized
processing and process control *always* wins hands down. It is simply very difficult to do that with Windows, since Windows is meant
to be a one computer one user type of thing.

-Paul
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 15)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-19T12:39:45+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atrigr$6c0@netnews.hinet.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <1_UL9.5403$KW2.344100@twister.austin.rr.com> <atr1ol$hs9@netnews.hinet.net> <GSaM9.14773$Nz5.401618@twister.austin.rr.com>`

```

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> ���g��l��
news:GSaM9.14773$Nz5.401618@twister.austin.rr.com...
>
> "jason" <not-real@ms88.hinet.net> wrote in message
news:atr1ol$hs9@netnews.hinet.net...
> >
> > >
> > > The areas you pointed out, and others like E-Mail are served well by
> > WINTEL, though I can not think of a single example that cannot
> > > be served as well -- usually better! -- by UNIX. Both Windows and UNIX
are
> > very different from a mainframe or host based
> > > applications, and they are also very different from each other.
…[4 more quoted lines elided]…
> > A local nootbook computer manufacturer with annual sales over $5
billions,
> > using clustered WINTEL   for thier information processes.
> > they don't use UNIX nor mainframe becuase of keeping compatibility and
…[8 more quoted lines elided]…
> First off, take your $5 billion/year notebook company - who are they? And
what are they running?
> In particular, what the heck are they using for the accounting, inventory,
billing, and manuafacturing process software? I find it
> really difficult to accept they are running solely under Windows. Much
more likely they have the system outsourced to an accounting
> agency or something. Oh, and compatibility with *what*?
>
> Your idea of clustering has some value I am sure, but in terms of economy,
efficiency, and pure raw capabilty, centralized
> processing and process control *always* wins hands down. It is simply very
difficult to do that with Windows, since Windows is meant
> to be a one computer one user type of thing.
>
> -Paul


It's QUANTA COMPUTER INC, headquarter in Taiwan.
It's in fact the largest NB manufacturer in the world.
http://www.quantatw.com/

QUANTA  currently have over 100 NT servers supplied from IBM, HP, Compaq and
DELL,
and does not have any UNIX machines.  By Compatibility  I mean the same OS
on every machine
so servers from different suppliers  are  exchangable and cheaper than unix
machines.

QUANTA runs SAP ERP,  SUPPLY CHAIN,  and run MRP every night for regular
orders.
After taking additonal orders from the web the next morning they run MRP
again.
The server running MRP is equipped with 16 CPU's, and takes two hours.  If
upgrades to
Itanum-2, the running time will be reduced  to 20 minutes.

I am no longer familiar wtih mainframes,
so I can just provide this case for your evaluation.

jason
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 16)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-19T06:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfdM9.13670$6H6.474139@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <1_UL9.5403$KW2.344100@twister.austin.rr.com> <atr1ol$hs9@netnews.hinet.net> <GSaM9.14773$Nz5.401618@twister.austin.rr.com> <atrigr$6c0@netnews.hinet.net>`

```

"jason" <not-real@ms88.hinet.net> wrote in message news:atrigr$6c0@netnews.hinet.net...
>
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> ���g��l��
…[55 more quoted lines elided]…
>

Well, SAP software for Windows requires SQL server and is targeted for small to medium size businesses, so I am surprised they are
using it that way.  But it still proves my point doesn't it?

100 NT servers is a hell of a lot more difficult to install and maintain than a single RS/6000 (pSeries machine), and the license
cost for Windows far exceeds the license cost for AIX. The cost for SQL server
far exceeds the cost for DB/2 as well. Where is the benefit in running Windows?

I would easily expect two UNIX machines to easily replace 98 of those NT servers; one to run core business (i.e. SAP) and one to
handle E-Mail, FTP, and other such trivia. Leav two NT servers around running CITRIX to handle things like Microsoft Word and
Outlook.

Or replace them with a single S/390 system running Linux/390.

Are there any downsides to that? Well, yes, you would have to figure out what to do with the money you save, and probably have to
find some useful for the six or seven NT admins you just put out of a job.

-Paul


> QUANTA runs SAP ERP,  SUPPLY CHAIN,  and run MRP every night for regular
> orders.
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 17)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-20T09:14:46+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<attqsh$4nt@netnews.hinet.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <1_UL9.5403$KW2.344100@twister.austin.rr.com> <atr1ol$hs9@netnews.hinet.net> <GSaM9.14773$Nz5.401618@twister.austin.rr.com> <atrigr$6c0@netnews.hinet.net> <UfdM9.13670$6H6.474139@twister.austin.rr.com>`

```

> >
> >
…[4 more quoted lines elided]…
> > QUANTA  currently have over 100 NT servers supplied from IBM, HP, Compaq
and
> > DELL,
> > and does not have any UNIX machines.  By Compatibility  I mean the same
OS
> > on every machine
> > so servers from different suppliers  are  exchangable and cheaper than
unix
> > machines.
> >
>
> Well, SAP software for Windows requires SQL server and is targeted for
small to medium size businesses, so I am surprised they are
> using it that way.  But it still proves my point doesn't it?
>
> 100 NT servers is a hell of a lot more difficult to install and maintain
than a single RS/6000 (pSeries machine), and the license
> cost for Windows far exceeds the license cost for AIX. The cost for SQL
server
> far exceeds the cost for DB/2 as well. Where is the benefit in running
Windows?
>
> I would easily expect two UNIX machines to easily replace 98 of those NT
servers; one to run core business (i.e. SAP) and one to
> handle E-Mail, FTP, and other such trivia. Leav two NT servers around
running CITRIX to handle things like Microsoft Word and
> Outlook.
>
> Or replace them with a single S/390 system running Linux/390.
>
> Are there any downsides to that? Well, yes, you would have to figure out
what to do with the money you save, and probably have to
> find some useful for the six or seven NT admins you just put out of a job.
>
> -Paul

I don't know much about why they use pure NT servers.
But the man in charge of Quanta's information process was a former
manager-level IBM employee.  He must have good reason to do so.
Anyway, everybody is happy in this case, QUANTA, Microsoft, and IBM.

jason mo
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 12)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-18T14:05:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6qv00v4nbij5nfs0ijj6mu8m078q5vdjv7@4ax.com>`
- **References:** `<b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net>`

```
"jason" <not-real@ms88.hinet.net> wrote:

Hi Jason!

Good post!
>
>So, as long as  COBOL can add new features to answer new demands
>, it is going to be lingering like the turtle in the race against rabbits.

Sounds like you are comparing the current situation with Aesop's fable
of the tortoise and the hare.

Great analogy.....COBOL improves slowly and steadily while the market
constantly changes the "language du jour" thereby causing people to
"change strategy and direction in the middle of the race."

In the story, the tortoise won because of perseverance and focus on
the task at hand.  Slow and steady wins the race!



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 13)_

- **From:** "jason" <not-real@ms88.hinet.net>
- **Date:** 2002-12-19T07:02:20+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atquo6$7tq@netnews.hinet.net>`
- **References:** `<b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <umauvucgis46apjlbncivjosinvl1v01qf@4ax.com> <atobc2$2sj@netnews.hinet.net> <6qv00v4nbij5nfs0ijj6mu8m078q5vdjv7@4ax.com>`

```

"Bob Wolfe" <rtwolfe@flexus.com> ?????
news:6qv00v4nbij5nfs0ijj6mu8m078q5vdjv7@4ax.com...
> "jason" <not-real@ms88.hinet.net> wrote:
>
…[5 more quoted lines elided]…
> >, it is going to be lingering like the turtle in the race against
rabbits.
>
> Sounds like you are comparing the current situation with Aesop's fable
…[7 more quoted lines elided]…
> the task at hand.  Slow and steady wins the race!

Thanks, Bob,
I use the tortoise and the hare as an anology.
English is my second language, I read this fable in translation,
never kenw the words used in Aesop fables,

jason
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-17T13:54:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F0GL9.1885$qU5.1102639@newssrv26.news.prodigy.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3dfee300_3@Usenet.com...
> My comments were tongue in cheek and not intended to be offensive...that's
> why there is a GRIN attached to it.

Usenet means never having to say you are sorry.

(Not that I would *ever* post anything which could be misconstrued or
'politically incorrect.' )

MCM
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 10)_

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-12-19T06:08:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:
> My comments were tongue in cheek and not intended to be offensive...that's
> why there is a GRIN attached to it.
<snip>
> You are much too easily "insulted" for a public forum. No offense was
> intended.

"Peter E. C. Dashwood" also wrote:
> My position on this is very well known and I have no intention of
re-raking
> all the reasons why I think Don and his committee are a waste of time.

So presumably, for lack of a <G>, offense was intended in this case.

Gazaloo.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 11)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-19T02:26:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212190226.7695aacd@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net>`

```
"Gazaloo" <gaz@a.loo> wrote in message news:<UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net>...
> "Peter E. C. Dashwood" wrote:
> > My comments were tongue in cheek and not intended to be offensive...that's
…[12 more quoted lines elided]…
> Gazaloo.

I wasn't smiling when I wrote it. If you are looking for offense, then
take it. I really don't care.

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 12)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-19T15:17:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YplM9.12430$KW2.571377@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212100402.430dcc17@posting.google.com> <b8d390f9.0212101309.31cf0aa0@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com>`

```
So "take it" to private e-mail. Nobody at all is interested in this waste of bandwidth.
-Paul

"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:b3638c46.0212190226.7695aacd@posting.google.com...
> "Gazaloo" <gaz@a.loo> wrote in message news:<UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net>...
> > "Peter E. C. Dashwood" wrote:
…[18 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 13)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-20T02:13:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212200213.1a43e28e@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com> <YplM9.12430$KW2.571377@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:<YplM9.12430$KW2.571377@twister.austin.rr.com>...
> So "take it" to private e-mail. Nobody at all is interested in this waste of bandwidth.
> -Paul

While I agree with the sentiment expressed, Paul, there are a couple
of things you should remember:

1. This is an UNMODERATED PUBLIC Newsgroup.

That means waste of bandwidth is par for the course, and looking round
here, there is much of it. Some of your own posts are not immune. The
rule is if you are not interested, don't read it. If you do read it
and are still not interested, don't respond to it. It's simple...

2. When did you acquire the right to decide that "nobody at all" is
interested in something?  (You are axiomatically wrong, as at least
Gazaloo and myself are interested in this particular post <G>). As
neither you nor anybody else here is a moderator for this group, all
you can do is express an opinion, not demand that something be done.

Having said all of that, I happen to agree with you on this and it
would be better served by private e-mail <G>. However, I believe that
both Gazaloo and myself have made our positions clear and, I for one,
won't be pursuing this further.

Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 14)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-21T03:52:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dARM9.22205$KW2.867482@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com> <YplM9.12430$KW2.571377@twister.austin.rr.com> <b3638c46.0212200213.1a43e28e@posting.google.com>`

```
Unmoderated does not mean there are no rules. It just means the rules are made by
the group.



"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:b3638c46.0212200213.1a43e28e@posting.google.com...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:<YplM9.12430$KW2.571377@twister.austin.rr.com>...
> > So "take it" to private e-mail. Nobody at all is interested in this waste of bandwidth.
…[23 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 15)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-21T18:06:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E04ADBC.6ADF31B5@Azonic.co.nz>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com> <YplM9.12430$KW2.571377@twister.austin.rr.com> <b3638c46.0212200213.1a43e28e@posting.google.com> <dARM9.22205$KW2.867482@twister.austin.rr.com>`

```
Paul Raulerson wrote:
> 
> Unmoderated does not mean there are no rules. It just means the rules are made by
> the group.

Who told you that ?

In an unmoderated group all rules are made by self appointed individuals
and are ignored by everyone else.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 16)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-21T19:09:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T%2N9.32088$KW2.1000397@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com> <YplM9.12430$KW2.571377@twister.austin.rr.com> <b3638c46.0212200213.1a43e28e@posting.google.com> <dARM9.22205$KW2.867482@twister.austin.rr.com> <3E04ADBC.6ADF31B5@Azonic.co.nz>`

```
No No No! That was in the 1980s and 1990s. Now they do economic impact studies...

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message news:3E04ADBC.6ADF31B5@Azonic.co.nz...
> Paul Raulerson wrote:
> >
…[6 more quoted lines elided]…
> and are ignored by everyone else.
```

###### ↳ ↳ ↳ Re: Visual Age Cobol, or Java ?

_(reply depth: 17)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-12-22T06:54:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ldN9.8386$p_6.640524@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com> <b3638c46.0212110343.4fbd2b47@posting.google.com> <vmtevu4ce14r1l3a76eevhhak43o0eupf9@4ax.com> <3df8f0c7_3@Usenet.com> <73qjvu4hp5j5vat37g3t6bmq4oomm94m3q@4ax.com> <3dfa6be6$1_11@news.newsgroups.com> <bulrvu8l4vt8r339oq4gjhiibnlnu9ndam@4ax.com> <3dfee300_3@Usenet.com> <UndM9.272378$GR5.92629@rwcrnsc51.ops.asp.att.net> <b3638c46.0212190226.7695aacd@posting.google.com> <YplM9.12430$KW2.571377@twister.austin.rr.com> <b3638c46.0212200213.1a43e28e@posting.google.com> <dARM9.22205$KW2.867482@twister.austin.rr.com> <3E04ADBC.6ADF31B5@Azonic.co.nz> <T%2N9.32088$KW2.1000397@twister.austin.rr.com>`

```

Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote in message news:T%2N9.32088$KW2.1000397@twister.austin.rr.com...

> No No No! That was in the 1980s and 1990s. Now they do economic impact studies...
>
You've heard this one, perhaps?

Many years ago, a company conducted a manual feasibility study.
They concluded that they could do their payroll faster, better, cheaper by punched card.

They installed a punched card system.

Later, they used the punched card system to conduct a feasibility study.
They concluded that they could do their payroll faster, better, cheaper by computer.

They installed a computer system.

Later, they used the computer to conduct a feasibility study.
They concluded that they could do their payroll faster, better, cheaper manually.
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-10T05:39:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212100539.79157672@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
I can't comment on Visual Age for COBOL having never used it.  

I can, however, comment on HP 3000 conversion.  Please check
http://www.adtools.com and look at the Hp 3000 conversion tools there.


trento2002@hotmail.com (Harry M) wrote in message news:<b8d390f9.0212092307.46ef573c@posting.google.com>...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
…[13 more quoted lines elided]…
> What are the good and bad points about VA Cobol?
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-10T14:44:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o1vbvuo4ajenmb8cclero1qbv1o4suf3eg@4ax.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
Harry:

A Linux application server combined with a Windows user interface
running across TCP/IP is a great environment for our COBOL sp2 (GUI)
and Thin Client (transport) software.

Everything is accomplished using COBOL CALL USING statements, you will
be able to use ANY Linux compiler, including Fujitsu COBOL, IBM VA,
Liant/RM COBOL, Micro Focus COBOL or Acucobol.  Our tools are
completely compiler independent....which is nice coming from a
proprietary environment such as the HP3000 COBOL.

In addition, you can ad remote Windows printing support later with our
FormPrint product and web enabling with our Web Client product.  We
also support embedded Active X Controls with our software so that you
can use component technology as well.  Everything is compiler
independent.

Contact me by private e-mail or take a look at our web pages at
www.flexus.com.

Good luck with your migration project!

trento2002@hotmail.com (Harry M) wrote:

>I have a system developed in Cobol with 110 online programs and 125
>batch programs. The system is on HP3000 and needs to be converted to a
…[13 more quoted lines elided]…
>What are the good and bad points about VA Cobol?


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2002-12-10T22:03:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<geidnV4C_5hIN2ugXTWcow@comcast.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
You might check out Acucobol (www.acucorp.com). The compiler has options to
compile HP3000 compatible source code.  You could then use Acu4GL to use a
database instead of Cobol files.

"Harry M" <trento2002@hotmail.com> wrote in message
news:b8d390f9.0212092307.46ef573c@posting.google.com...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
…[13 more quoted lines elided]…
> What are the good and bad points about VA Cobol?
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-12-10T22:51:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0212102251.2890fc93@posting.google.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
did you try PERCobol from www.legacyj.com ?

trento2002@hotmail.com (Harry M) wrote in message news:<b8d390f9.0212092307.46ef573c@posting.google.com>...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
> different platform since HP is dropping support for the HP3000. I plan
> to use DB2 for data base, Linux on the server and Windows on the
> desktop.
```

#### ↳ Re: Visual Age Cobol, or Java ?

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-11T15:12:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PBIJ9.167039$8D.4497243@twister.austin.rr.com>`
- **References:** `<b8d390f9.0212092307.46ef573c@posting.google.com>`

```
Hey Harry -
   You have already gotten a lot of good advice, but I will throw my $0.02 in anyway. :)
Going from the HP3000 to Linux is a pretty drastic change, and the easiest thing for you to
do is to use MF COBOL on the Linux side - avoiding for the moment your questions about
Java and assuming the configuration you specified below.

That is the EASIEST thing to do, it is probably not the best thing to do. One of the biggest issues
you will immediately run into is terminal emulation and speed. You will almost certainly have lightening
fast displays, but since the terminal will be dumb and based upon curses, typing on the display will probably be disappointing. Same
with development tools such as editors and debuggers and so forth. (Unless of course, you put a GUI on system, which is a rewrite,
not a port, and a lot more initial work.)

A choice that would probably be much better would be to port to an AS/400, for which, I might add, there exists a good set of tools
to port from an HP/3000. (I am assuming you are running under MPe?) The initial learning curve would be a little steeper, but the
benefits of the integrated system would quickly become apparent, and appreciated. :) Best of all, top of the line Web application
development tools are also pretty well integrated on the 400 (WebSphere, Java, etc.) and for development, the cost of equipment and
software can be held very low. Deployment costs are on a par with an HP/3000 or a little lower.

VA Cobol is aimed at workstation and mainframe development, a world that is pretty distant indeed from host based systems like
Linux, HP3000s, and AS/400's.

When you decide to port your app to the web, I strongly suggest servlets and java beans as your deployment pattern of choice.
Applets and Java Applications are both possible and meet particular needs, but a web application that uses them is often very large,
bulky, subject to version problems in target execution platforms, and they don't always look very good.  Using what amounts to HTML
+ JavaScript in a JSP is just about the best of both worlds, at least with current technology.

Linux deployments are much better suited for transferring systems that are primary BATCH oriented, or have very limited user
interactions to displays.  By the way, with a AS/400, if you deploy on a midsize model, you can usually run Linux in a partition at
the same time you are running OS/400, which really gives you the best of both worlds.

-Paul


"Harry M" <trento2002@hotmail.com> wrote in message news:b8d390f9.0212092307.46ef573c@posting.google.com...
> I have a system developed in Cobol with 110 online programs and 125
> batch programs. The system is on HP3000 and needs to be converted to a
…[13 more quoted lines elided]…
> What are the good and bad points about VA Cobol?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
