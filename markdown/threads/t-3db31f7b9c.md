[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen Section

_66 messages · 17 participants · 1999-10 → 1999-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Screen Section

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381734D2.6199A8B3@home.com>`

```
Partially this refers to Judy's problem in thread "Constructive
Criticism..", and Thane this refers back to my comments re Screen
Section in your book.

Given that we are approaching Y2K - should 'schools' still be promoting 
Screen Section as an introduction to window/screen-handling ? I realize
that there will be DOS text programs with Screen Section rolling over
beyond Y2K - but will any current/future systems be designed using
Screen Section. Because of 'rollover' COBOL-xxx must still contain
Screen Section.

When I read Arranga/Coyle or Wilson Price on OO - to get their
respective points across, they avoided the issue of both Screen Section
and GUIs - sticking with a simple ANSI Accept/Display. (Using an M/F
compiler they could have used Screen Section or GUIs - and lost their
readers' attention, as a result). In his book Thane keeps it as simple
as possible, not getting into coloring/colouring.

In Judy's case, and from what she subsequently wrote to me privately, my
guess is she singled out Screen Section as being a challenge to get out
of the way first, and got herself into a bit of a fix taking this
approach. (I suggested to her the 3-tier approach, work out the logic of
the business application, then determine flat-file structure and then
make the Screen Section fit the problem. Had she been only required to
produce simple Accept/Display - I don't think she would have been
confused).

It seems to me using Screen Section is akin to accessing flat-files from
diskettes. During its time Screen Section was an excellent tool - but
should it still be offered as an introductory tool now ?

Jimmy, Calgary AB
```

#### ↳ Re: Screen Section

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v763r$e4k$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com>`

```

James J. Gavan wrote in message <381734D2.6199A8B3@home.com>...
[...]
>Given that we are approaching Y2K - should 'schools' still be promoting
>Screen Section as an introduction to window/screen-handling ?

What does Y2K have to do with Screen Section?

Perhaps you meant to say we are approaching "the age of GUI"
or something like that. :-)

> I realize
>that there will be DOS text programs with Screen Section rolling over
>beyond Y2K - but will any current/future systems be designed using
>Screen Section. Because of 'rollover' COBOL-xxx must still contain
>Screen Section.

Remember that Screen Section from X/Open COBOL also
applied to Unix and Mainframes. When you think "standard
COBOL", you must not consider MS-DOS or PC-DOS as the
only point of reference! (When you think Mainframe, you must
not consider IBM as the only point of reference!)

Nonetheless, Screen Section did not exist in any prior ANSI
COBOL standard; hence there is no "rollover" from ANSI
COBOL.

As to whether Screen Section will be used in the future, I made
the point, months ago, that Screen Section is an important
addition to the standard, even if it is used only for debugging
and testing. Considering my opinion about the usefulness of
OO for most COBOL programming, I would suggest the Screen
Section is a far more important addition to the language!
[...]
>It seems to me using Screen Section is akin to accessing flat-files from
>diskettes. During its time Screen Section was an excellent tool - but
>should it still be offered as an introductory tool now ?

It is possible that Screen Section will be accepted into the new
standard. If it is accepted into the new standard, then to teach
"standard COBOL" means teaching Screen Section, in addition
to all the other new features.
------------------
Rick Smith
```

##### ↳ ↳ Re: Screen Section

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38176BC4.834FB309@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net>`

```


Rick Smith wrote:
> 
> James J. Gavan wrote in message <381734D2.6199A8B3@home.com>...
…[7 more quoted lines elided]…
> or something like that. :-)

Yep. That says it. Not specifically "GUI" a la Windows - but the term
generally.
> 
> > I realize
…[29 more quoted lines elided]…
> to all the other new features.

I think Screen Section was/is a damn good tool. I emulated Windows with
it (popup menus, listboxes etc..), while Windows was still flexing its
muscles. It would have made sense to me if Screen Section had been used
as the COBOL model for building GUIs on ALL PLATFORMS.

> .....and testing. Considering my opinion about the usefulness of
> OO for most COBOL programming, I would suggest the Screen
> Section is a far more important addition to the language!

I might not be too swift, but when it comes to OO, I'd already guessed
you had (D)oubting (T)homas branded on your forehead <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PZ7S3.8469$l22.68800@news1.mia>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <38176BC4.834FB309@home.com>`

```
James J. Gavan wrote:
>
>I might not be too swift, but when it comes to OO, I'd already guessed
>you had (D)oubting (T)homas branded on your forehead <G>

Ah!  So *that's* what it means. :-)
```

##### ↳ ↳ Re: Screen Section

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vaf2n$pc2$1@plutonium.btinternet.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net>`

```

Rick Smith wrote in message <7v763r$e4k$1@news.hitter.net>...
>
>James J. Gavan wrote in message <381734D2.6199A8B3@home.com>...
…[30 more quoted lines elided]…
>Section is a far more important addition to the language!


Why, we dont want to continue using the crappy old DOS displays anymore
end-users just dont want this.  If I turned round to my company
tommorrow, or my customers and said "im gonna do a DOS interface instead,
coz its easier" they would laugh in my face, and tell me that I should use
C++
or some other kind of language.

I think if COBOL is going to continue and continue to be sucessfull in
future years
then the "new" Cobol must be released, instead or as well as the old screen
section
clauses.


>>It seems to me using Screen Section is akin to accessing flat-files from
>>diskettes. During its time Screen Section was an excellent tool - but
>>should it still be offered as an introductory tool now ?


No it should'nt, why walk backwards?


>It is possible that Screen Section will be accepted into the new
>standard. If it is accepted into the new standard, then to teach
>"standard COBOL" means teaching Screen Section, in addition
>to all the other new features.


Yes, I can see this being a valid statement, *only* because we have many,
many
existing Cobol screen section programs currently in use today.
But I certaintly would'nt recommend using it as a new development tool.
After all, "everyone" uses GUI displays now no matter what platform.


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vakvl$dbf$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com>`

```
Simon R Hart wrote in message <7vaf2n$pc2$1@plutonium.btinternet.com>...
>Why, we dont want to continue using the crappy old DOS displays anymore

Well, there is no Screen Section = DOS for Acucobol variant. Screen Sections
in Acucobol is fully graphical. You should also see my note regarding the
approach of Delphi and Visual Basic.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vc3lr$dov$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com>`

```

Simon R Hart wrote in message <7vaf2n$pc2$1@plutonium.btinternet.com>...
>
>Rick Smith wrote in message <7v763r$e4k$1@news.hitter.net>...
[...]
>>As to whether Screen Section will be used in the future, I made
>>the point, months ago, that Screen Section is an important
>>addition to the standard, even if it is used only for debugging
>>and testing.
[...]
>Why, we dont want to continue using the crappy old DOS displays anymore
>end-users just dont want this.
[...]
>After all, "everyone" uses GUI displays now no matter what platform.

Private Development

If you write an application that supports your development work,
you are the end-user of that application. GUIs require more
development effort than Screen Section. Would you consiously
spend more development effort than is necessary to create an
application that you will see but that your customers will never see?

Interactive Testing

I work with data collection terminals. These terminals barely have
a user interface, character or otherwise. The data from these
terminals is currently processed as batches. To change the
operating mode from batch to on-line, I will need to provide a
user interface for testing the transactions, interactively. I will
be the end-user of the test environment. Would you insist that
I should use GUI, rather than Screen Section, for the test
environment?

Interactive Debugging

Consider a distributed application with a GUI interface for
end-users. The language for the GUI interface is not COBOL
and does not run on the same machine as the COBOL
program. A user reports that certain types of entries do not
give the expected results. I am the user of the debugging
environment. Would you insist that I should not use a COBOL
program with Screen Section emulating the GUI to find and
correct the problem?

Summary

There are different types of users and end-users for different
applications and environments.

In an Age of GUI, there are still valid reasons for using simple
character mode screens.

Having Screen Section in the COBOL standard makes sense.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vauis$t6t$1@aklobs.kc.net.nz>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com>`

```
Simon R Hart <hart1@technologist.com> wrote:

: Why, we dont want to continue using the crappy old DOS displays anymore
: end-users just dont want this.  If I turned round to my company
: tommorrow, or my customers and said "im gonna do a DOS interface instead,
: coz its easier" they would laugh in my face, and tell me that I should use
: C++
: or some other kind of language.

Just because a system may use text mode or 'DOS' displays does
not mean that it cannot have a useful user interface.  It
doesn't need to be Windows to be a WIMP UI.

In fact some of the worst UIs I have seen have been done in
MS Windows.

What is important is that the user should be able to invoke
whatever functions they require quickly and consistently.

This does not excludeX/Open ACCEPT/DISPLAY or SCREEN SECTION, but
it may be easier for the programmer to use some other tools.

One problem that I do see with SCREEN SECTION (and why I have
not used it) is that it tends towards the user having to
fill all fields and then have them processed.  This makes it
difficult (but not impossible) for the program to deal with 
each field as the user enters them.

For the last 20 years or so I have used field by field ACCEPT/
DISPLAY/process which warns users of errors and problems on
each field while allowing the user to request value lists or
help at any point.

If the user relates 'DOS' with 'bad user interface' that is
the fault of the system designers, not of DOS or text mode.
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vb1cv$jd9$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vauis$t6t$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote in message <7vauis$t6t$1@aklobs.kc.net.nz>...
>In fact some of the worst UIs I have seen have been done in
>MS Windows.

This is so true as it is said. I agree wholeheartly!

>One problem that I do see with SCREEN SECTION (and why I have
>not used it) is that it tends towards the user having to
>fill all fields and then have them processed.  This makes it
>difficult (but not impossible) for the program to deal with
>each field as the user enters them.

This is not true for Acucobol, I have complete control with every individual
field there, I can control it prior to and after entry, I can change focus,
enable/disable fields on the fly or prior to display, yes it may even let me
process events unrelated to the screen section.

What Cobol are you using?

>If the user relates 'DOS' with 'bad user interface' that is
>the fault of the system designers, not of DOS or text mode.

Definitely true.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381903E6.97BEE56F@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vauis$t6t$1@aklobs.kc.net.nz>`

```


Richard Plinston wrote:
> 
> Simon R Hart <hart1@technologist.com> wrote:
…[5 more quoted lines elided]…
> each field as the user enters them.

Richard, 

Wanted to collect all my thoughts together before replying on 'Screens'
- but just to clarify the point above. (and I've forgotten all I used to
know about Screen Section). Your comment is only true if you say ACCEPT
MYSCREEN; but nothing to stop you coding ACCEPT MYFIELD(n). I was doing
that with a 10 x 24 table, prompting user down the column then back up
to the next, with the Screen Section coded to take a table. I'm doing
exactly the same using OO/GUI, totally ignoring the Tab key.

Jimmy
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3819A821.676197A8@NOSPAMhome.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com>`

```
Simon R Hart wrote:

> Yes, I can see this being a valid statement, *only* because we have many,
> many
> existing Cobol screen section programs currently in use today.
> But I certaintly would'nt recommend using it as a new development tool.
> After all, "everyone" uses GUI displays now no matter what platform.

Not true.  But I like the recommendation that we supply standard reports
to users who can use Crystal Reports to format their output the way they
want.   

Also, I have written COBOL programs which wrote in a format that the
users' spreadsheets could read my output.  Why would I need GUI
abilities for this?

I have also had mainframe databases from which we extracted data to
secondary databases which GUI programs used.  This extraction doesn't
need to be GUI.
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vd080$n4$2@aklobs.kc.net.nz>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <3819A821.676197A8@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:

: I have also had mainframe databases from which we extracted data to
: secondary databases which GUI programs used.  This extraction doesn't
: need to be GUI.

I once tried using a tape backup program which probably had
the most inappropriate user interface imaginable.  It had
all the bells and whistles, selection lists, buttons, menus
funtion keys.  It could be manouvered with ease, anything
at all could be done.

The problem was it _had_ to be done.  What was actually required
for a tape backup was a _command_line_ utility that could be
buried in a user menu as 'do backup' or, even better, done
automatically as a cron job (or similar).

But this program had no way of saving selections for later
processing, the user had to work through all the wonderful
UI gadgets to specify what was required.  They neither
knew nor cared about this.

Fortunately there was an older program that could be used
to do the job automagically.  A 'complicated' command line
driven one.
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfES3.10305$qy6.163432@news2.mia>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <3819A821.676197A8@NOSPAMhome.com> <7vd080$n4$2@aklobs.kc.net.nz>`

```
Fastback? :-)
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vruki$n0f$1@nntp4.atl.mindspring.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com>`

```
This is still a semi-contentious issue at J4 and WG4 - but as it stands the
"traditional" Screen Section (with ACCEPT/DISPLAY - but for a NON-gui
interface) is being ADDED to the draft of the next Standard as a REQUIRED
feature (but in the Processor Dependent list).

PROs:

1) There are existing X/Open conforming applications that this will make
portable

2) There is *STILL* no GUI "Standard" for Unix or (most) Mainframe
environments.  This will give SOME portable user-interface for such
applications

3) The use of the current ANSI/ISO "DISPLAY" is still used SIGNIFICANTLY as a
"debugging" tool (when you don't want or can't invoke a "modern" debugger).
Adding the enhanced Accept/Display is viewed as a useful "quick and dirty"
debugging tool.


CONs:

1) All the world is becoming Windows "look alike" - so anything that doesn't
work that way will have a serious problem in "real world" use.

2) Those vendors that already support a 'green screen' interface (such as IBM
CICS) probably won't implement this feature anyway - and their users wouldn't
want to use it if they did.

3) What programmers "want" is to code once - use with any compiler on any
platform AND to get the 'user-interface' that is appropriate to that
environment.  This feature definitely will NOT provide that.

 ***

Personally, I believe fairly strongly that it will "nice" to have this in the
Standard - but will certainly not be the proof of the new Standard for
wide-spread use.
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vsap9$76f$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net>`

```
William M. Klein wrote in message <7vruki$n0f$1@nntp4.atl.mindspring.net>...
>3) What programmers "want" is to code once - use with any compiler on any
>platform AND to get the 'user-interface' that is appropriate to that
>environment.  This feature definitely will NOT provide that.

This is what you get with Acucobol.

>>Simon R Hart <hart1@technologist.com> wrote in message
>> Yes, I can see this being a valid statement, *only* because we have many,
…[3 more quoted lines elided]…
>> After all, "everyone" uses GUI displays now no matter what platform.

I have a big problem seeing that Screen sections and GUI is mutually
exclusive. I believe the solution that is chosen in Acucobol is elegant and
efficient. It is GUI all over. Best of all; it is portable.

As I have said previously, Borland Delphi and Visual Basic and certainly a
number of other tools have evolved into using a Screen section equivalent.
It would be really stupid if Cobol which has had it for several years,
should leave it, while others start using it.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vskgo$7oj$1@nntp6.atl.mindspring.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net>`

```
Cheesle <cheesle@online.NoSpamPlease.no> wrote in message
news:7vsap9$76f$1@news.cerf.net...
> William M. Klein wrote in message
<7vruki$n0f$1@nntp4.atl.mindspring.net>...
> >3) What programmers "want" is to code once - use with any compiler on any
> >platform AND to get the 'user-interface' that is appropriate to that
…[3 more quoted lines elided]…
>

I understand (and previously knew) that AcuCOBOL has this feature.
Unfortunately, neither X/Open nor the ANSI/ISO people have "taken up" this
feature.  Therefore, the Acucorp feature is portable across platforms (where
AcuCOBOL exits), but is NOT portable (nor is it going to be) across
compilers.

As I previously mentioned, there is an ANSI/ISO Standard for "FIMS" (Forms
Interface Management System - I think) that does provide what you are talking
about (for functionality) but which never "caught on" among implementors.
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vtlfk$gp5$2@news.igs.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net>`

```
Perhaps we should define a "screen object", and make it external.

William M. Klein wrote in message <7vskgo$7oj$1@nntp6.atl.mindspring.net>...
>Cheesle <cheesle@online.NoSpamPlease.no> wrote in message
>news:7vsap9$76f$1@news.cerf.net...
>> William M. Klein wrote in message
><7vruki$n0f$1@nntp4.atl.mindspring.net>...
>> >3) What programmers "want" is to code once - use with any compiler on
any
>> >platform AND to get the 'user-interface' that is appropriate to that
>> >environment.  This feature definitely will NOT provide that.
…[6 more quoted lines elided]…
>feature.  Therefore, the Acucorp feature is portable across platforms
(where
>AcuCOBOL exits), but is NOT portable (nor is it going to be) across
>compilers.
>
>As I previously mentioned, there is an ANSI/ISO Standard for "FIMS" (Forms
>Interface Management System - I think) that does provide what you are
talking
>about (for functionality) but which never "caught on" among implementors.
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 7)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vtu78$hoi$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net>`

```
donald tees wrote in message <7vtlfk$gp5$2@news.igs.net>...
>Perhaps we should define a "screen object", and make it external.

Are you thinking of using an external third party screen generator like
Cobol Sp II?

It is a solution, I do however prefer to have it in Cobol.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vvpit$qrc$2@news.igs.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net>`

```
I am thinking of writing a screen "object" that I can invoke.

IE:  INVOKE SCREEN-OBJECT "display-screen-01".
       INVOKE SCREEN-OBJECT "accept-screen-01".


Cheesle wrote in message <7vtu78$hoi$1@news.cerf.net>...
>donald tees wrote in message <7vtlfk$gp5$2@news.igs.net>...
>>Perhaps we should define a "screen object", and make it external.
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 9)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8024v8$s6j$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net>`

```

donald tees wrote in message <7vvpit$qrc$2@news.igs.net>...
>I am thinking of writing a screen "object" that I can invoke.
>
>IE:  INVOKE SCREEN-OBJECT "display-screen-01".
>       INVOKE SCREEN-OBJECT "accept-screen-01".

What would be the difference of DISPLAY display-screen-01 and ACCEPT
display-screen-01?

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 10)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8048hi$t5r$1@news.igs.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net>`

```
I could use the screen sections from one Cobol in another, or, for example,
use screen sections on one platform, but a GUI on another. The screen
interface would be in a library that exists outside the main code, rather
than imbedded.

As I see current systems, the disk I-O, screen I-O, and the main program
logic should be clearly delineated into three distinct modules.  Only the
calling sequence between the three need be fixed.  OO probably gives us the
cleanest break.

It is not unusual in a modern system to use three different languages for
those three functions (for example, SQL & a DBM, SP2, and pure Cobol).  By
making all three of those OO Cobol modules, then you have the ability to
substitute any given one without changing the other two.


Cheesle wrote in message <8024v8$s6j$1@news.cerf.net>...
>
>donald tees wrote in message <7vvpit$qrc$2@news.igs.net>...
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3825CC11.D8B8F2F3@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net> <8048hi$t5r$1@news.igs.net>`

```


donald tees wrote:
> 
> I could use the screen sections from one Cobol in another, or, for example,
…[12 more quoted lines elided]…
> substitute any given one without changing the other two.

Agreed - three-tier systems.

Jimmy
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 12)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804n8g$ovf$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net> <8048hi$t5r$1@news.igs.net> <3825CC11.D8B8F2F3@home.com>`

```
James J. Gavan wrote in message <3825CC11.D8B8F2F3@home.com>...

>Agreed - three-tier systems.


Unfortunately this often ends up as "Three-times-as-slow-systems" :-)

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 13)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806ov0$dcl$2@news.igs.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net> <8048hi$t5r$1@news.igs.net> <3825CC11.D8B8F2F3@home.com> <804n8g$ovf$1@news.cerf.net>`

```
Why is that? The overhead of a call is not that great.

Cheesle wrote in message <804n8g$ovf$1@news.cerf.net>...
>James J. Gavan wrote in message <3825CC11.D8B8F2F3@home.com>...
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38264942.BA622CDC@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net> <8048hi$t5r$1@news.igs.net> <3825CC11.D8B8F2F3@home.com> <804n8g$ovf$1@news.cerf.net>`

```


Cheesle wrote:
> 
> James J. Gavan wrote in message <3825CC11.D8B8F2F3@home.com>...
…[3 more quoted lines elided]…
> Unfortunately this often ends up as "Three-times-as-slow-systems" :-)

Sorry Cheesle - just not true. 

Logically, you would think having all three lumped together would ensure
best results. Keeping the concept of three-tier, as I think Donald said,
allows you to switch the modules for screen presentation and file
handling, without a major upheaval.

In my own situation, from my business.cbl in two programs(classes) I can
hop back and forth between two full windows (window1.cbl and
window2.cbl) without any show of slowness whatsoever, and on OK update
the business.cbl invokes my file routines (dbi.cbl) and does a
write/rewrite without apparent delay - then displays window1.cbl to
accept next choice or exit.

I've mentioned before - N/E users have found COBOL GUIs more effective
than doing calls to Visual Basic - and to the best of my knowledge, they
weren't even referring to OO. I have no personal experience of VB - so I
just have to take what they have said on face value.

There is a fractional slowness when I first invoke business.cbl because
in the two programs I'm referring to, I am dynamically creating tables.
But I consider this minimal delay acceptable at program start-up.

I see in your separate reply to Donald you mention VB - or ActiveX could
be the answer. Well, I've commented above about VB and as regards
ActiveX - you may recall Pete Dashwood 'swears by it'. Not something
I've yet got into, but taking that three-tier approach I just swap -
window1 and window2.cbl which are GUIs now become window3 and
window4.cbl which are ActiveX(s) - but here we are talking specific to a
platform. Perhaps better still, at some future date they become SP2
to overcome the platform problem.

Jimmy
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 11)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804n6f$oun$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <7vvpit$qrc$2@news.igs.net> <8024v8$s6j$1@news.cerf.net> <8048hi$t5r$1@news.igs.net>`

```
donald tees wrote in message <8048hi$t5r$1@news.igs.net>...
>I could use the screen sections from one Cobol in another, or, for example,
>use screen sections on one platform, but a GUI on another. The screen
>interface would be in a library that exists outside the main code, rather
>than imbedded.

>As I see current systems, the disk I-O, screen I-O, and the main program
>logic should be clearly delineated into three distinct modules.  Only the
>calling sequence between the three need be fixed.  OO probably gives us the
>cleanest break.

Interesting, Borland Delphi has this ability as well as VB. I agree on your
idea.

ActiveX is probably the answer here.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 8)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38232275.14880965@news.enter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

>donald tees wrote in message <7vtlfk$gp5$2@news.igs.net>...
>>Perhaps we should define a "screen object", and make it external.
…[8 more quoted lines elided]…
>

The last thing I want to do is get in another spirited discussion
regarding what is COBOL and what is not COBOL....the last time I
checked, CALL USING.....is COBOL.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 9)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vvdea$8ck$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <38232275.14880965@news.enter.net>`

```
Bob Wolfe wrote in message <38232275.14880965@news.enter.net>...
>The last thing I want to do is get in another spirited discussion
>regarding what is COBOL and what is not COBOL....the last time I
>checked, CALL USING.....is COBOL.

Correct, however, what is happening inside what is called is not Cobol.

You are much too sensitive about this :-)

Sp2 is a good utility, it just isn't something for me.

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 10)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3823561e.28108665@news.enter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net> <7vtlfk$gp5$2@news.igs.net> <7vtu78$hoi$1@news.cerf.net> <38232275.14880965@news.enter.net> <7vvdea$8ck$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

>Bob Wolfe wrote in message <38232275.14880965@news.enter.net>...
>>The last thing I want to do is get in another spirited discussion
…[3 more quoted lines elided]…
>Correct, however, what is happening inside what is called is not Cobol.

...and what is happening inside the Acucobol runtime is not COBOL
either.

I'm completely and totally perplexed why you insist on comparing the
Acucobol-GT syntax with the internals of our sp2.dll.  That is
absolutely comparing apples and oranges.

You *should* be making the comparision as follows:

Compare the actual logic which the COBOL programmer writes to control
the screens in both products....ergo Acu-GT screen syntax with COBOL
sp2 CALL's.

If you want to compare the internals of the sp2 screen handler, then
you should compare that with the internals of the Acucobol runtime.

>You are much too sensitive about this :-)

If I am sensitive about this, it is because the logic which is used by
the COBOL programmer in a COBOL sp2 application to control the GUI
screen is, in fact COBOL.  In fact, it is ANSI standard COBOL.  You
keep telling people it is not, but it *is*!

The logic which is used by the COBOL programmer in an Acucobol
application to control the GUI screen is, in fact an extension to the
COBOL language.

In BOTH cases, the WinAPI is ultimately being invoked by a non-COBOL
program.  In the case of the sp2.dll, the WinAPI is in fact being
invoked by a C language program.  In the case of the Acucobol
WRUN32.EXE, the WinAPI is in fact being invoked by a C language
program.

If I am sensitive, it is because the programming interface in sp2 IS
COBOL.....whatever is "under the covers" is immaterial.

>Sp2 is a good utility, it just isn't something for me.

That's fine.  I'm sure that you've seen my posts before which suggest
that we do NOT believe that sp2 is right for everyone.  We wouldn't be
so pompous or arrogant as to suggest otherwise.

I know that there are companies out there who do indeed attempt to
convince people that they have the ultimate tool.  They make
ridiculous claims that their tool is a "one size fits all" tool.
There is no tool available which is "all things to all people" and my
advice is to turn and run in the other direction when you hear a sales
rep make that claim.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vt0er$20c$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <7vsap9$76f$1@news.cerf.net> <7vskgo$7oj$1@nntp6.atl.mindspring.net>`

```
William M. Klein wrote in message <7vskgo$7oj$1@nntp6.atl.mindspring.net>...
>As I previously mentioned, there is an ANSI/ISO Standard for "FIMS" (Forms
>Interface Management System - I think) that does provide what you are
talking
>about (for functionality) but which never "caught on" among implementors.

Too bad, in my opinion Screen sections properly programmed are an excellent
and structured way of programming.

Well, I am happy :-)

Cheesle
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382248B1.32E1D23B@nbnet.nb.ca>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net>`

```
I was hoping that the new standard, complete with SCREEN SECTION would
allow me to pressure IBM to prove the ability to compile code for the
CICS environment without coding any EXEC CICS code.
 
Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca

massive snipping
> 
> 
…[7 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
more snippage
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vuaus$2ss$1@nntp2.atl.mindspring.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382248B1.32E1D23B@nbnet.nb.ca>`

```
Clark Morris <morrisc@nbnet.nb.ca> wrote in message
news:382248B1.32E1D23B@nbnet.nb.ca...
> I was hoping that the new standard, complete with SCREEN SECTION would
> allow me to pressure IBM to prove the ability to compile code for the
> CICS environment without coding any EXEC CICS code.

It certainly would be worth your "conveying" this message to IBM. (I don't
think they have heard it - or not much).  Interesting enough, I had some
recent conversation on using "standard" I/O (READ, WRITE) etc for COBOL under
LE.  I think that IBM *could* do this (even though this would allow LESS
"granularity" of I/O than CICS).

>
> Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca
…[4 more quoted lines elided]…
> > 2) Those vendors that already support a 'green screen' interface (such as
IBM
> > CICS) probably won't implement this feature anyway - and their users
wouldn't
> > want to use it if they did.
> >
…[4 more quoted lines elided]…
> more snippage
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382250AF.876500BE@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> This is still a semi-contentious issue at J4 and WG4 - but as it stands the
…[3 more quoted lines elided]…
> environment.  This feature definitely will NOT provide that.

How come you are able to zero-in on EXACTLY what (GUI) programmers want
and J4 or WG4 don't seem to have a bloody clue ! Cheesle's AcuCobol
Screen Section Text/GUI examples show an  obvious candidate for
standarization.

Seriously, why should screen/windows handling, (for desktops) be any
more alien than our verbs are for handling flat-files. I realize it
doesn't have the same emphasis for the big-iron, but over and above
their number-crunching capabilities, many of those systems are
associated with 'feeder' systems where there are multi-users requiring a
Screen Section/GUI-feel to screen displays.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38227f5e.26900323@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382250AF.876500BE@home.com>`

```
On Fri, 05 Nov 1999 03:27:36 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[19 more quoted lines elided]…
>

New GUI objects are added all the time.  There's noting static or
compatible about a GUI across platforms.  Within a very limted set,
yes, but get more "Graphical" than the most rudimentary GUI and you
have things that just aren't portable.

OS/2's containers for example are not supported by win32s.  

I am of the opinion that the UI is going to change faster than any
language standard can accept.  Is GUI defined in any other languages
standard?  It's always platform dependant, OS dependant, and should
remain so.   I don't think the interface (and that means perhaps
excluding the screen section) should be standardized.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3824A1A7.C72E256B@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382250AF.876500BE@home.com> <38227f5e.26900323@news1.attglobal.net>`

```


Thane Hubbell wrote:
> 
> On Fri, 05 Nov 1999 03:27:36 GMT, "James J. Gavan" <jjgavan@home.com>
…[36 more quoted lines elided]…
> excluding the screen section) should be standardized.

Thane,

You may be right - I just don't know. But specifically I'm thinking of
the 'standard' windows controls which are all in fact 'mini-windows'.
There isn't a limitless set. They appear in M/S DialogEditor and the
M/F Dialog Editor. 

Accepting these controls as the basis I can't see a reason why they
shouldn't be obtainable from an enhanced Screen Section, regardless of
platform.

When you say :-

> I am of the opinion that the UI is going to change faster than any
> language standard can accept.  

Do you have specific areas in mind. Consider your message about Fujitsu
- W. Gates III can do what he likes with Windows 2000, but it is
irrelevant until our COBOL compilers/tools comply.

Now let's try another tack. Simon Hart - you studied Smalltalk at
university - are its GUIs so far removed from Windows that they are
totally incompatible, or are they close to what you are using in
NetExpress.

Anybody dabbling with Linux - again are GUI controls incompatible ?

Remember folks - Xerox PARC Simula/Smalltalk - simulation and GUIs being
the raison d'ï¿½tre; concept picked up by Steve J., smartly followed by
William G.

PS: Hey that's neat - spellchecker put the 'hat' on 'd'ï¿½tre for me !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<584V3.3009$Ss1.29527@dfiatx1-snr1.gtei.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382250AF.876500BE@home.com> <38227f5e.26900323@news1.attglobal.net> <3824A1A7.C72E256B@home.com>`

```

James J. Gavan wrote in message <3824A1A7.C72E256B@home.com>...
>Remember folks - Xerox PARC Simula/Smalltalk - simulation and GUIs being
>the raison d'�tre...

>PS: Hey that's neat - spellchecker put the 'hat' on 'd'�tre for me !

Hey, a French-biased spellchecker! Finally, a piece of software which *must*
handle 'xenophobic' !!

No merde!

MCM
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 7)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3824feff.161166142@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382250AF.876500BE@home.com> <38227f5e.26900323@news1.attglobal.net> <3824A1A7.C72E256B@home.com>`

```
On Sat, 06 Nov 1999 21:37:39 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Thane,
>
…[8 more quoted lines elided]…
>

Linux has GUI with KDE or GNOME - X/Windows has been around as long or
longer than Windows - some people where I work run it as an interface
under VMS - which has it's own GUI - the controls are similar, but
different from MS-Windows.  There may or may not be a common subset.
We should not LIMIT COBOL to this set, nor should we limit our
development with COBOL by such a set.  Standardizing something as
fluid as the UI is just not a good idea IMHO.  Keep it external.

>
>> I am of the opinion that the UI is going to change faster than any
…[5 more quoted lines elided]…
>

That's a platform dependant area.  If the platform changes out from
under you, you are at a loss.  The vendors need to keep up - but
SHOULD be able to rely on at least some level of downward
compatibility.  


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vubdh$rok$1@nntp2.atl.mindspring.net>`
- **References:** `<381734D2.6199A8B3@home.com> <7v763r$e4k$1@news.hitter.net> <7vaf2n$pc2$1@plutonium.btinternet.com> <7vruki$n0f$1@nntp4.atl.mindspring.net> <382250AF.876500BE@home.com>`

```
Playing "devil's advocate" (or something) - as most readers of this NG know,
I do NOT agree with some of J4's/WG4's decisions - but ...

The problems are: (I think)

A) J4 and WG4 do not want to LIMIT COBOL to those environments that have
screens.  (For example, some day your car's carburetor COULD be programmed in
COBOL)

B) As stated elsewhere in this thread there is VERY little in UI's that are
actually available in all (or even most) platforms.  "Assuming" a Windows
look-and-feel, may make "real-world" sense (at least for some people) but
most certainly DOES NOT make sense for "international Standards".  (If there
WERE a standard for UNIX, this might not be as big an issue, but considering
the largest "open system" still doesn't have a Standard GUI is pretty
"discouraging".)

C) I keep mentioning FIMS - but this really WAS an attempt to get something
that was cross-language and cross-compiler for "interfaces".  There was
originally native COBOL syntax - but it was changed to a COBOL "binding".
But there STILL isn't sufficient user-demand for this to get implemented on
many platforms.  Until this (or this type of thing) to get true user-demand,
I don't see it getting into the COBOL Standard.
```

#### ↳ Re: Screen Section

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38176f69.13636135@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com>`

```
On Wed, 27 Oct 1999 17:13:57 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:
Everything snipped....

James - 

I teach the screen section for the user interface with my Book, Sams
Teach Yourself COBOL in 24 Hours, for a couple of reasons.

1.  It is FAIRLY standard.  (I use the x/Open subset as much as
possible - with minor changes my examples work with all compilers).

2.  The user interface is NOT my main thrust - the Screen Section is a
means to an end.  I get a common interface so the student can
communicate with a program.  It is SIMPLE, so we can concentrate on
the basics of COBOL before moving into advanced topics.

I teach the GUI at the end because I think it IS important - but it is
NOT the only user interface to a COBOL program.  In fact, until the
Screen Section is part of the formal COBOL standard, there IS no
standard user interface for a COBOL program save simple Accept and
Display statements (with no screen positioning).

Should it be taught  - Yes - as a means to get into the guts of COBOL.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Screen Section

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v82s8$rgi$1@news.cerf.net>`
- **References:** `<381734D2.6199A8B3@home.com>`

```
James J. Gavan wrote in message <381734D2.6199A8B3@home.com>...
>Given that we are approaching Y2K - should 'schools' still be promoting
>Screen Section as an introduction to window/screen-handling ? I realize

I join the comment about the connection between screen sections and Y2K, you
really must explain that one to me.

Regarding Screen sections in general;

I consider them to be the ultimate tool. Given proper programming techniques
a screen section approach is clean, structured and strong for reuse.

I myself have been using screen sections heavily over the last 5 years. In
my opinion it makes your application source much more readable. It opens for
structured implementation of variant screens and makes n-thier solutions
easier to implement.

With Acucobol the possibilites within the Screen section has increased way
beyond what was possible in the 85 standard, I can understand your view if
this is not true for your (other) vendor(s).

The only item I miss in the Acucobol screen sections is support for window
declaration, if that had been in there too, it would have been the ultimate
tool for development of n-thier applications.

I don't know if you know it, but Delphi, Visual Basic and to some extent
Visual C++ does use a variant of screen section for form declaration. Of
course all of the above mentioned tools may also be used without this. For
Delphi and VB, their popularity as a RAD tool heavily depends on their form
files, which is basically a screen section variant.

The Acubench utility from Acucorp provides to a great extent the same
functionality as of Delphi and VB in gui design, and while the Acubench
stores the stuff in .scn files do Delphi store in .dfm files.

This approach is way easier to read and maintain than multiple code lines
with allocation of objects and an endless stream of object property
settings.

Well, that's my 2 cents.

Cheesle
```

##### ↳ ↳ Re: Screen Section

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N9fS3.1853$9H3.18732@news3.mia>`
- **References:** `<381734D2.6199A8B3@home.com> <7v82s8$rgi$1@news.cerf.net>`

```
I'm in complete agreement with Cheesle's post below.  Just because GUI
is glitzy is no reason to use it for *everything*.  I once wrote a
labor and equipment management cost tracking system for a small county.
In the vehicle maintenance shop the supervisor had implemented a 3x5
note card system with one card per vehicle, listing type of spark plugs,
oil, etc.  He asked me about putting that on the computer.  I told him
"Look, your current system has 100% uptime, extremely low maintenance
costs and you can update it in 30 seconds.  Putting it on a computer
could not possibly improve what you have."  Many, many computers are
used exclusively (or almost so) for simple data entry.  It is not now,
and never will be, quicker or easier to move your hand from the key-
board and click a button than it is to simply type a letter.  On many
applications, there is virtually no benefit from GUI, and often some
disadvantages.  If a user interface is well designed, many systems
can have a text based interface that is just as clear to understand
and easy to use as a GUI.  We need simple solutions just as much as we
need more complex ones.  Both have their value, and their place.  Just
because something is newer is no reason to completely abandon the old
methods, as long as those old methods are more effective for certain
tasks.  Urban police have found that an officer on a horse is a more
effective solution for some tasks than an officer in a squad car, or
on foot. :-)
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3819EC5F.CB97E9F1@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7v82s8$rgi$1@news.cerf.net> <N9fS3.1853$9H3.18732@news3.mia>`

```
Many thanks to those who responded to my query re Screen Section - so
Screen Section LIVES, and Thane can safely go for a reprint without
changing a word of the text <G>. There were many compelling reasons
given why it should continue to exist.

But something based on a comment George made about teaching Screens.
Just some 40 years ago all we had was program logic and files
(input/output) no dumb terminals, VDUs, CRTs, desktops etc... COBOL was
taught effectively just covering those two areas. Using simple ANSI
Display/Accept perhaps - should the school curriculum concentrate on
these two facets and then at a later stage introduce Screen
Section/GUIs/SP2 etc... to round out the learning. Ignoring screens at
Stage I also emphasizes the desirability of validity checking input - a
very important concept to put across. My own view is that if you
establish the business/program logic, re-inforced by file-handling, then
the communication with the user, (screen displays), fits easier into
place.

My own particular preference - I'd love to still be programming in
Screen Section - without all the headaches of the latest technology.
And what an excellent tool on which to base a platform independent COBOL
screen handler whether text or GUI.

Ignore the big retail chains, which have dedicated POS systems, but the
smaller retailers here, (Calgary), seem to have a mixed bag of text
based POS systems and the very latest, Windows-fashion, with the screen
used as a magnified calculator or even touch-screens. The 'small guys'
will go for the proven, and invariably cheaper, text systems, whereas
the guys with several branches, wanting to go high-tech, appear to get
into GUI systems.

But Simon's comments re 'advancing' are true. It is consumer-driven. I'm
not saying it is right, but in high-tech Calgary, with its oil/patch, if
I attempted to sell a text screen system instead of Windows/GUIs - they
would show me the door. Meanwhile the small guy can see no reason for
paying the price of high-technology and will opt for text-based. This
GUI bit has been re-inforced by the computing arm of the international
accounting firms offering systems in C/C++ etc. Further, realizing the
oil patch is a money-maker, a short while back, Oracle bought out the
computer arm of one accounting firm - and we now have an Oracle branch
in Calgary - and I don't think they offer text based systems.

Jimmy, Calgary AB
```

#### ↳ Re: Screen Section

- **From:** "George E. Zielinski" <georgezielinski@retired.airforce.net>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>`
- **References:** `<381734D2.6199A8B3@home.com>`

```
Please keep in mind, students are not at the level we are.  They are still
trying to wrestle with basic concepts (such as --does the program really
have to produce the correct output or is it acceptable to look like it
produces the correct output :) ).  Seriously, they are attempting to learn
both a programming language syntax and programming concepts.

Colleges and universities are in the same boat that corporations are.
Software costs money, and which of the products out there are we going to
promote (sorry, teach).  Are we going to use Dialog, Flexus, A VB
derivative, etc.

Screen sections are still used in those applications where functionality is
more important than form.  I am not saying that form is unimportant, but in
an academic environment, functionality is more important.  It allows the
student to reinforce some programming concepts (picture clauses, and
formatting characteristics) while introducing some additional ones (input
fields vs. output fields vs input/output fields; field characteristics, and
placement) and enhancing their ability to deal with their choices.

I do not know of any professor (contrary to what students say) that does not
enhance the presentation beyond what is available in the screen section.
But you must be prepared to learn to walk before you can be prepared to run.

I liken it to --  do we really need to teach math,  I mean doesn't everyone
have a calculator.
```

##### ↳ ↳ Re: Screen Section

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7k1c$n1v$2@neptunium.btinternet.com>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>`

```

George E. Zielinski wrote in message
<5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>...
>Please keep in mind, students are not at the level we are.  They are still
>trying to wrestle with basic concepts (such as --does the program really
…[17 more quoted lines elided]…
>I do not know of any professor (contrary to what students say) that does
not
>enhance the presentation beyond what is available in the screen section.
>But you must be prepared to learn to walk before you can be prepared to
run.
>
>I liken it to --  do we really need to teach math,  I mean doesn't everyone
>have a calculator.


Given what you said that students must learn the basics first is true in
some aspects.  Although this is what the language Pascal is used for
teaching software development, rather than any language.

If Universities keep on teaching out of date technologies god knows where we
are going to end up.  Universities should teach the latest technologies
wherever possible no matter how difficult they are, after all, if the
student finds it too hard then they are in the wrong business right?

Realistically if a programmer cannot apply DBMS, OO/GUI and the other
luxuries that we can enjoy with these great technologies then their is not
alot of problems that people/business's want solved.
Therefore no jobs for new grads.

Just my 2pence ;)


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7ire$lu7$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com>`

```

Simon R Hart wrote in message <7v7k1c$n1v$2@neptunium.btinternet.com>...
[...]
>Given what you said that students must learn the basics first is true in
>some aspects.

No, it is true in every aspect (respect)! :-)

[...]
>If Universities keep on teaching out of date technologies god knows where
we
>are going to end up.

In one of the millions of companies that use older, reliable,
well-known technologies? ;-)

>  Universities should teach the latest technologies
>wherever possible no matter how difficult they are, after all, if the
>student finds it too hard then they are in the wrong business right?

Sometimes the latest technologies are the latest technological
fads! :-)

Sometimes the best methods for teaching aren't known until
a technology has been around for a while. It would be a
shame for a student to give up because good concepts,
explanations, and examples are not available.

I found this particularly true of OO. It took four years for me to
"get it" because of all the lame, useless examples given in a
myriad of text books. Finally, I found someone who gave
reasonable, useful examples; then OO made sense.

Should I, as a student of OO, have given up all programming
because some authors presented impractical examples to
demonstrate OO concepts?

Now consider that thousands of students passed courses on
OO design and programming after having been taught
impractical designs as examples of OO concepts. These
students are now creating systems with defective class
heirarchies that will most certainly cause problems later.

It is far better to have a difficult time learning that which is
correct than to have an easy time learning that which is
wrong!
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38179edb.25783754@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net>`

```
On Wed, 27 Oct 1999 19:00:37 -0400, "Rick Smith"
<ricksmith@aiservices.com> wrote:

Posted and mailed (Maybe - Attglobal.net is denying my mail about 80%
of the time, anyone else notice that problem?).

>reasonable, useful examples; then OO made sense.

From where, pray tell?  A book we all can get?





---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Class Invariance (was: Re: Screen Section)

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v85ne$11bi$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net>`

```

I can suggest reading these in the order given:

< http://www.objectmentor.com/publications/ooadpcpp.pdf >
< http://www.objectmentor.com/publications/casestud.pdf >
< http://www.objectmentor.com/publications/underlay.pdf >

Particularly the parts that deal with the design of a payroll system.
The text and diagrams given were also published in the book,
Designing Object-Oriented C++ Applications Using The Booch
Method, by Robert C. Martin, 1995.

Unless you wish to wade through a bunch of C++, the book
should not be necessary.

The typical examples given in other publications, including
examples in section C18 of the draft COBOL standard, show
inheritance such as Manager --> Employee; that is, Manager
inherits from Employee or Manager is-a Employee. Another
common example is Hourly --> Employee, Salaried --> Employee,
and Commissioned --> Employee. This last is analyzed in the
above web references.

The big problem, that I had, was that I knew the inheritance
heirarchies were wrong, I just didn't know why; for four years!

The part I did not understand, and which the books I read did not
explain, was what I will call "Class Invariance"; that is, once an
object is instantiated as a particular class, it can never be changed.
Yet I knew, from my work with Employee systems, that Hourly
Employees can become Salaried Employees; but inheriting these
types from an Employee class meant that an object of type Hourly
Employee could not be changed to an object of type Salaried
Employee. Likewise, the Manager --> Employee inheritance means
that an Employee object cannot be changed to a Manager object.

The last of the above web references made that point clear.

Finally, with an understanding of Class Invariance, the earlier books,
that did not make sense, became clearer. Just ignore the examples
used to describe inheritance!
------------------
Rick Smith

Thane Hubbell wrote in message <38179edb.25783754@news1.attglobal.net>...
>On Wed, 27 Oct 1999 19:00:37 -0400, "Rick Smith"
><ricksmith@aiservices.com> wrote:
…[6 more quoted lines elided]…
>From where, pray tell?  A book we all can get?
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381910B7.285BF3AA@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net>`

```


Rick Smith wrote:
> 
> I can suggest reading these in the order given:
…[3 more quoted lines elided]…
> < http://www.objectmentor.com/publications/underlay.pdf >

Thanks for the references Rick - I've downloaded to read.

But your 'Invariance' - why not apply what I'll modestly call Gavan's
Law - "Computer technology is available to assist the programmer. It is
not incumbent upon the programmer to slavishly follow the tools".
Bend the bloody rules as you see fit to get the desired results.

> The typical examples given in other publications, including
> examples in section C18 of the draft COBOL standard, show
…[19 more quoted lines elided]…
> The last of the above web references made that point clear.

We are talking flat-files or DBs to get at employee data - so throwing
the theory to one side, what's the big deal ? Have a flag in the
Employee Record : 1 = WeeklyPaid, 2 = Salaried - change the code back
and forth and you hit the right class or sub-class with an invoke based
on an Evaluate. Similarly the Employee Record has a flag saying whether
he/she is a Serf or a Manager. I just don't buy throwing away our file
technology to sub-divide a record into many parts to achieve many
objects. 

Here's a classic case - Customers of a retail chain - can be various
types, Cash, Plastic, Store-Card, Instalment Payment etc.. Also
Employees are Customers too (the incentive being staff discounts). In
non-OO do we confuse A/R Customer Names with a Payroll Employee Names.
Ah - but they both belong to Class Person - BS !

Really, where it all gets screwed up is designers sticking to what they
think is the pure OO model. (And I'll take a guess, lacking the business
acumen of COBOL, that's what is happening in the other OO languages).

Why I asked about Multiple Inheritance ? I agree, at this point, with
the OO author in 'COBOL Unleashed" - it's impractical - until somebody
shows me a coded example. Fujitsu have a paragraph on Multiple
Inheritance headed "CAUTION". As you indicated, you 'could have fun'
making it work and in the process probably break the rules to make it
work efficiently. 

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vbv4c$api$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com>`

```

James J. Gavan wrote in message <381910B7.285BF3AA@home.com>...
[...]
>But your 'Invariance' - why not apply what I'll modestly call Gavan's
>Law - "Computer technology is available to assist the programmer. It is
>not incumbent upon the programmer to slavishly follow the tools".
>Bend the bloody rules as you see fit to get the desired results.
[...]
>We are talking flat-files or DBs to get at employee data - so throwing
>the theory to one side, what's the big deal ? Have a flag in the
…[5 more quoted lines elided]…
>objects.

The problem, of course, is setting theory aside!

At first you solve the incorrect class hierarchy by using a small
number of statements to change the flags to make the data fit
the correct class. The number of possible WHENs in the
EVALUATE is N * (N - 1). For four possible classes, there
are only twelve possible changes. Add another class to the
hierarchy and there are twenty possible changes, an so on.

Of course, there is more than one defective class hierarchy.
Each of these hierarchies has its own set of possible
changes.

It may not be too difficult to live with the maintenance, in the
EVALUATE mechanisms, for adding new classes; but,
in theory, OO should reduce maintenance!

Now management decides to replace the RDB with an OODB.
In theory, the OODB should reduce the time required to load
and save objects. The problem is that the OODB screws up
the first application of Gavan's Law; but, we could apply
Gavan's Law, a second time, to the objects themselves. All
that is needed, at this point, is to replace the statements in
the WHENs of the EVALUATE mechanism with subprograms
that convert the objects of one class to objects of another class.
If we have only 250 WHENs in the EVALUATEs, we need only
write 250 programs to do the possible conversions among the
appropriate classes. Where we once added a WHEN and a
few statements to change the flags, we now add a subprogram
to create the new class, copy the appropriate data from the old
class, and delete the old class.

Did I make the point that defective class hierachies are
unacceptable at any level?
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381a6b98.209296290@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net>`

```
Posted and mailed.

On Fri, 29 Oct 1999 10:54:39 -0400, "Rick Smith" 
<ricksmith@aiservices.com> wrote:

>Did I make the point that defective class hierachies are
>unacceptable at any level?
>------------------ 

Yes.  Now can you show us an example of a good class hierarchy?  Just
a simple example.  I am learning, but I've not "Got it" yet.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vfllp$2p0q$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net>`

```
[Posted and mailed]

I think some good examples are on page 3 (and following)
in the discussion of the Payroll Application in the following
web reference:
< http://www.objectmentor.com/publications/underlay.pdf >.

The discussion (and diagrams) demonstrate how using
abstraction can identify the base of a hierarchy and how
to build from that base without creating the problem of
Class Invariance.

Several abstract classes are developed to represent
certain concepts associated with Employees and Payroll.
The abstract classes are used to derive subclasses which
are then used to implement the methods for each of the
requirements.

It occurs to me that most COBOL systems have record
layouts that may be translated into good class hierarchies;
but this may not be obvious due to OO teminology and
because the depth of the hierarchy is not that great.

Since I have used Employee examples frequently, I think
I would like to try another area for examples. What is
another application area were COBOL is a good fit
and you and others might find interesting?
------------------
Rick Smith

Thane Hubbell wrote in message <381a6b98.209296290@news1.attglobal.net>...
>Posted and mailed.
>
…[8 more quoted lines elided]…
>a simple example.  I am learning, but I've not "Got it" yet.
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381c7229.342071570@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net> <7vfllp$2p0q$1@news.hitter.net>`

```
On Sat, 30 Oct 1999 20:37:30 -0400, "Rick Smith"
<ricksmith@aiservices.com> wrote:
Rick,

Perhaps something like a contact management system, or better yet,
something I deal with every day - a Transactional billing system.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vieaq$1h0b$1@news.hitter.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net> <7vfllp$2p0q$1@news.hitter.net> <381c7229.342071570@news1.attglobal.net>`

```

Thane Hubbell wrote in message <381c7229.342071570@news1.attglobal.net>...
>On Sat, 30 Oct 1999 20:37:30 -0400, "Rick Smith"
><ricksmith@aiservices.com> wrote:
…[3 more quoted lines elided]…
>something I deal with every day - a Transactional billing system.

These might be interesting; but I have never worked with
either of these types of systems and I have no reference
material to help me understand how they might work
internally. I think it better that I profess my ignorance in
these areas than to prove it beyond a doubt.

In any case, it will likely be several days before I can offer
anything. I need to determine how far to carry the examples
and I have to play catch-up with my work due to losing
a couple days. Take father to hospital, take care of mother
for a few days (sister's help appreciated), spend hours and
hours at hospital, take father home from hospital, that sort
of thing. Father will be fine. Mother is fine. I need a good
night's sleep. (Private note: Yes, me too; but only 10 miles.)
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381CAEB3.26502A08@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net> <7vfllp$2p0q$1@news.hitter.net>`

```


Rick Smith wrote:
> 
> Since I have used Employee examples frequently, I think
> I would like to try another area for examples. What is
> another application area were COBOL is a good fit
> and you and others might find interesting?

Go with Judson's suggestion. Thane threw me, perhaps it was his word
'Transactional'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 11)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381cbfca.15887789@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net> <7vfllp$2p0q$1@news.hitter.net> <381CAEB3.26502A08@home.com>`

```
On Sun, 31 Oct 1999 20:55:17 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[8 more quoted lines elided]…
>'Transactional'.

I work for a service company that bills customers by the transaction.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yQWS3.7066$DM3.67290@news4.mia>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <7vbv4c$api$1@news.hitter.net> <381a6b98.209296290@news1.attglobal.net> <7vfllp$2p0q$1@news.hitter.net>`

```
Rick Smith wrote:
>
>Since I have used Employee examples frequently, I think
>I would like to try another area for examples. What is
>another application area were COBOL is a good fit
>and you and others might find interesting?

Try Order Entry or Accounts Payable.  Both are intiutive and simple
in concept, even for people who have not worked with them, and both
have simple heirarchial structure.
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381ADE72.89C330D3@zip.com.au>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com>`

```
"James J. Gavan" wrote:
> 
> We are talking flat-files or DBs to get at employee data - so throwing
…[13 more quoted lines elided]…
> 

Jimmy there is no such thing as a pure OO model.  You can watch
comp.object arguing between themselves on this one :->

Whether an employee is a person or whether an employee contains a
person or whether it contains a reference to a person is all in how
you model the system.

The employee would contain a reference to a pay structure that could
be replaced (weekly to monthly, monthly to casual).  If you where a
payroll firm then you would logically see the system as a pay that
happens to have an employee.  It really is dependant upon your
perspective of the system.

When the employee shops at the store they are a person that happens to
have an employee discount card.  This is polymorphism, the system only
sees as much of the interface as it is interested in.

Example of bad polymorphism:

	if type = employee
		process payment * .95
	else
	        process payment.

The internal structure must not have switches based upon types

	process discounted( payment ).

The base case is just return the price and the employee overrides with
returning price * .95.

Boring you yet...
Ken
```

###### ↳ ↳ ↳ Re: Class Invariance (was: Re: Screen Section)

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381B44D8.674DB590@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net> <7v85ne$11bi$1@news.hitter.net> <381910B7.285BF3AA@home.com> <381ADE72.89C330D3@zip.com.au>`

```


Ken Foskey wrote:
> 
> "James J. Gavan" wrote:
…[33 more quoted lines elided]…
> Ken

Ken,

Glad you jumped in - hoping you would <G>; and you aren't boring me.
The crux is as you say, there isn't a pure OO model - although some like
to propose there is. Again, the technology has to fit the application;
and make it fit what you want to do. (Incidentally, I have a class
Description File, one fixed-format, many record types - with some
REDEFINES to include certain record-types in the fixed format; arguably
you could say this should have sub-classes, but I treat it as one class
and quite sucessfully make decisions based on Record-Type).

Agree with you about comp.obj - they're running around like blue-a....
flies getting nowhere. And as you nicely pointed out to one gentelmeman,
there is one language which is far more readable than Smalltalk; it's
called COBOL.

Jimmy
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38183d8e_3@news3.prserv.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <7v7k1c$n1v$2@neptunium.btinternet.com> <7v7ire$lu7$1@news.hitter.net> <38179edb.25783754@news1.attglobal.net>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:38179edb.25783754@news1.attglobal.net...
> On Wed, 27 Oct 1999 19:00:37 -0400, "Rick Smith"
> <ricksmith@aiservices.com> wrote:
…[3 more quoted lines elided]…
>
I have had problems with attglobal too
```

##### ↳ ↳ Re: Screen Section

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381766FB.C2E7532C@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>`

```

"George E. Zielinski" wrote:
> 
> Please keep in mind, students are not at the level we are.  They are still
> trying to wrestle with basic concepts (such as --does the program really
> have to produce the correct output or is it acceptable to look like it
> produces the correct output :) ). 

That was really my point George; they are beginners - and need to grasp
the overall concept of programming, then they have to untangle in their
minds what flat-file handling is about. (You wouldn't throw DBs at them
in the early stages - would you?) I question whether throwing in Screen
Section at an early stage, with all its options, is better than a simple
Ansi Accept/Display.

Following on from what you wrote later - I wonder if an introductory
course even has the time to discuss Dialog/GUIs/Flexus/VB  etc. in
sufficient detail - it is an area which becomes so specific to the
compiler/tools the 'new' programmer finishes up using.

> Screen sections are still used in those applications where functionality is more important than form.  

If that's the case, (that Screen Section is still used), then so be it.

> I liken it to --  do we really need to teach math,  I mean doesn't everyone have a calculator.

Yes ! and I always use the calculator in preference to math <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381771f9.14292289@news1.attglobal.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net> <381766FB.C2E7532C@home.com>`

```
On Wed, 27 Oct 1999 20:47:56 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Following on from what you wrote later - I wonder if an introductory
>course even has the time to discuss Dialog/GUIs/Flexus/VB  etc. in
>sufficient detail - it is an area which becomes so specific to the
>compiler/tools the 'new' programmer finishes up using.

My fan mail says it can be done.  Seriously, it HAS been done.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Screen Section

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QbNR3.984$lG6.29988@dfiatx1-snr1.gtei.net>`
- **References:** `<381734D2.6199A8B3@home.com> <5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>`

```
George E. Zielinski wrote in message
<5827897607071300.CA1E1D2014963ECC.A1AB9F185B812289@lp.airnews.net>...
>--does the program really
>have to produce the correct output or is it acceptable to look like it
>produces the correct output...

It must actually produce the correct output.  Unless you are a marketing
major.


MCM
```

#### ↳ Re: Screen Section

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vcg25$t84$1@news.inet.tele.dk>`
- **References:** `<381734D2.6199A8B3@home.com>`

```
Well I beleive that it is time for me to join - I mean, everyone is here
anyway.
I like to keep my life simple, and I can agree with most of your views but
less of your arguments.

I have tried to produce solutions for customers in more than 30 years. When
a customer needs something and the best solution is char-based, fast
data-entry, I'll check my language reference for screen section. If it's
there, I will consider it legal to use it.

Making solutions is not to make the applications you and I love to produce.
It is to look at the users situation too. Your application must fit in -
just to respect the users. They have a life after work, and if they are
confident with Char, Function Keys and all that stuff, and if you just
extend functionality in an existing application, I beleive your choice
should be Screen Section.

We should only be completely 'up-to-date' when we develop new applications
or when we change the user-interface upon elderly ditto.

Software architecture is a fine art. Our contribution to the industry is to
respect existing applications while they exist and to do whatever we can to
produce damd good new ones.

That - I think - will give everyone an uncomplicated life. Listen to the
customer/user, and remember that we have 2 ears, 2 eyes but only 1 mouth.

At a conference in San Fransisco some 5 years back, the theme was
'EVOLUTION - not REVOLUTION. We can learn from that.

My conclusion is simple as I try to keep my life. Decide from task to task
what is best for the customer. The number og Screenset applications will
decrease and the number of OO applications with exciting GUI will increase.
Just listen to the customers.

Regards
Ib

James J. Gavan skrev i meddelelsen <381734D2.6199A8B3@home.com>...
>Partially this refers to Judy's problem in thread "Constructive
>Criticism..", and Thane this refers back to my comments re Screen
…[29 more quoted lines elided]…
>Jimmy, Calgary AB
```

##### ↳ ↳ Re: Screen Section

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vel8g$o2v$1@uranium.btinternet.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7vcg25$t84$1@news.inet.tele.dk>`

```

Ib Tanding wrote in message <7vcg25$t84$1@news.inet.tele.dk>...
>Well I beleive that it is time for me to join - I mean, everyone is here
>anyway.
…[31 more quoted lines elided]…
>Just listen to the customers.


Very true, after all we, as software developers have to develop software
(from a customers point of view) that:

A: Solves the problem.
B: Easy to use.

If we dont get these two very important rules right(never mind the others)
then the customer simply wont buy it.

"Listen to the customers" nail on the head, all the cutomers that I have
ever dealt with also in-house end-uers have pleaded easy to use software.
As Jimmy said earlier if he offered a "old" boring to look at text based
screens the customers wont buy it, so why use it?

*Most* customers want the lastest "stuff" so it is my job to sell them the
lastest.


Simon R Hart
Eaton, Ottery St. Mary, UK.



>Regards
>Ib
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0ES3.4731$9H3.49311@news3.mia>`
- **References:** `<381734D2.6199A8B3@home.com> <7vcg25$t84$1@news.inet.tele.dk> <7vel8g$o2v$1@uranium.btinternet.com>`

```
Simon R Hart wrote:
>
>*Most* customers want the lastest "stuff" so it is my job to sell them
>the lastest.

'Most customers' is irrelevant, unless you are developing for mass market
sales.  'Your customer' is what counts. :-)  Just this past Wednesday I
sat in a client's office discussing the new development we were planning.
I laid out the pros and cons of staying with a character based (Screen
Section) interface like they now have, or going GUI.  I remarked that I
would personally enjoy developing the GUI interface, hoping they would
let me do it.  The client quickly decided that he wanted to keep the
familiar character based interface.  It is familiar, easy, and the GUI
offered no significant benefit for this application.  It depends entirely
on the user's desires and the target application.  For some applications
I would strongly encourage GUI, for others I would strongly encourage
character based.  There is no 'better' between the two, only better for
one purpose or another.  In my opinion, many people these days confuse
flashy appearance appearance with value.  Just as COBOL is foolishly
considered a dinosaur because of failure to correctly judge what is
important about COBOL, many of us are also rushing toward GUI as the be-
all-end-all of interfaces.  Most times companies are mainly interested
in the bottom line.  A GUI interface can cost more to implement and
maintain than a simple character interface, and is *not* always easier
or cleaner to use.  Is it worth it?  Often it is, sometimes it is not.
It would be foolish to throw away all our handsaws because power saws
are available.  Both have their place, and so do GUI and character
interfaces.

In my opinion, we would be much better off dropping discussion of 'why
we should completely abandon character interfaces for GUI', with 'when
and where and how are each best and most effectively utilized'.  To me,
it is the 'COBOL is dead, we have all new and better tools' argument
all over.  When there are no longer any applications where character
interfaces offer any advantages, when GUI is always as cheap or cheaper,
and as quick or quicker to develop, when it is always as easy or easier
to use, when GUI building and language interface is just as standardized
(is there even a GUI spec in the new standard?), then we can discard it.
That time has not yet come, folks. :-)
```

###### ↳ ↳ ↳ Re: Screen Section

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381B401A.7025C34C@home.com>`
- **References:** `<381734D2.6199A8B3@home.com> <7vcg25$t84$1@news.inet.tele.dk> <7vel8g$o2v$1@uranium.btinternet.com> <d0ES3.4731$9H3.49311@news3.mia>`

```


Judson McClendon wrote:
> 
> Simon R Hart wrote:
…[5 more quoted lines elided]…
> sales.  'Your customer' is what counts. :-)  Just this past Wednesday 


Judson,

There isn't a line of what you've written that I disagree with. But just
to emphasize the high-tech bit, the following from to-day's Calgary
Herald, and the article was really talking about transportation issues,
current problem Canadian Airlines and Air Canada :- 

"....Calgary boasts the second-largest number of corporate head offices
in Canada, for example, and has a thriving high-technology sector
numbering 1,100 companies and generating $7 billion annually,......."

The largest of course, would be Toronto, or rather the greater Toronto
metropolitan area. By comparison to the former Calgary is but 0.8
million people. And as I said, I don't agree with it, but the prevailing
attitude in this high-tech community is, 'If it aint Windows, it aint
computing'. Same thinking used to apply 20 years ago, 'If it aint Big
Blue, it aint computing'.

And we aren't necessarily talking mass-market here; there is some, but
most is localized to the oil industry.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
