[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ethical Question

_39 messages · 25 participants · 1998-09_

---

### Ethical Question

- **From:** "Garry Dell" <Garry_dell@hotmail.com>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#CD7Tf819GA.172@upnetnews05>`

```
I am doing some y2k conversions and I am comming across some extremely
poorly written code.


I have a question to ask of this newsgroup.


I have seen quite a few "GOTO"s, in several programs,  should I remove them
or leave them intact?


Any feedback would be greatly appriciated.


I personally believe that I should remove them.
```

#### ↳ Re: Ethical Question

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sor42$rpl$1@callisto.clark.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
In article <#CD7Tf819GA.172@upnetnews05>,
Garry Dell <Garry_dell@hotmail.com> wrote:
>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
…[12 more quoted lines elided]…
>I personally believe that I should remove them.

I can understand your desire... and i would suggest that you do your best
to restrain yourself.

You were, by your description, hired/assigned to make the code
Y2K-compliant, not to insure that the code adheres to a particular school
of program structure.

The fewer your modifications, the fewer the bugs that will be introduced
by your modifications.  Y2K is a fixed deadline; code which unstructured
but Y2K-compliant *will* run.

In other words...

IF PROGRAM-RUNS
    PERFORM NEXT-ASSIGNMENT
ELSE
   PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING WORKS.

... and do what you were hired/assigned to do.

DD
```

#### ↳ Re: Ethical Question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-mNuEdL4J7dKK@Dwight_Miller.iix.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
On Fri, 4 Sep 1998 05:52:40, "Garry Dell" <Garry_dell@hotmail.com> 
wrote:

> I am doing some y2k conversions and I am comming across some extremely
> poorly written code.
…[13 more quoted lines elided]…
> 

I don't write new code with GO TO.   HOWEVER, you stand a LARGE chance
of breaking the code if you mess with it.  Do your job, fix the Y2K, 
and program in the STYLE that the programmer before you used.  Even if
you don' t like it.
```

#### ↳ Re: Ethical Question

- **From:** "G. van Vlimmeren" <gvlimmer@hoogenbosch.nl>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdd7d3$e984aea0$2c050380@s70>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```

> I have seen quite a few "GOTO"s, in several programs,  should I remove
them
> or leave them intact?

Hi.

If you can get someone to pay for it, change them :)

Otherwise, don't. The most important task for a program is 'to work'.
Everything else, like structure or readablility, is a bonus. :) And hey,
would you repaint a Rembrandt, because the clothes on his paintings look
out of date?

Oh, you can always change the 'GO TO' into 'GO'. Is shorter, looks nicer,
doesn't look as much like a 'GOTO'.

Gerben 'GO' van Vlimmeren
```

#### ↳ Re: Ethical Question

- **From:** "Alan Macro" <AlanM@hpdi.no-luncheon-meat.demon.co.uk>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<904898026.9805.0.nnrp-01.9e98b131@news.demon.co.uk>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
Conform to the old adage "if it works, don't fix it"! Removing GOTOs from a
working program (I assume its working!) is going to involve some
re-structuring. This is likely to create new bugs and increase the amount of
de-bugging and testing required.

Alan Macro
Hill Price Davison, London
AlanM@no-luncheon-meat.hpdi.demon.co.uk
"no-luncheon-meat."(i.e. no spam)  should be removed from email address

Garry Dell wrote in message <#CD7Tf819GA.172@upnetnews05>...
>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Ethical Question

- **From:** "Mike Rochford" <miker@easirun.co.za>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sob13$6et$1@news01.iafrica.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```

Garry Dell wrote in message <#CD7Tf819GA.172@upnetnews05>...
>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
…[14 more quoted lines elided]…
>

Gary

Why should you remove them ???

If the programs are working fine and all they require is amending to
recognise the century, why touch the GOTO statements ???

Sounds like you are makig unnecessary work for yourself, and with the crisis
mode that most places are in due to the year 2000, the last thing you should
be doing is making additional work.

Mike.
```

#### ↳ Re: Ethical Question

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sobof$r9v$1@juliana.sprynet.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
If it works, don't fix it....

WOB,
Atlanta

Garry Dell wrote in message <#CD7Tf819GA.172@upnetnews05>...
>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Ethical Question

- **From:** trblshtr@my-dejanews.com
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6son1u$gu0$1@nnrp1.dejanews.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
In article <#CD7Tf819GA.172@upnetnews05>,
  "Garry Dell" <Garry_dell@hotmail.com> wrote:
> I am doing some y2k conversions and I am comming across some extremely
> poorly written code.
…[10 more quoted lines elided]…
>

Why?  At best you can only "hide them" at the "expense" of additional
processing overhead and conversion costs.  "Poorly written", or not, the
programs apparently function well enough.  Else why would they require y2k
conversion?
```

#### ↳ Re: Ethical Question

- **From:** sbarsky@my-dejanews.com
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6son1e$gtp$1@nnrp1.dejanews.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
What has this got to do with "ethics"?

Leave em in.
>
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Ethical Question

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EFC384.3FC4F6DF@infonet.com.py>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```


Garry Dell wrote:

> I am doing some y2k conversions and I am comming across some extremely
> poorly written code.
…[8 more quoted lines elided]…
> I personally believe that I should remove them.

Goin' fishing, Garry?

Regards
Albert Ratzlaff
```

#### ↳ Re: Ethical Question

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35efdd51.0@news1.ibm.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```

Garry Dell wrote in message <#CD7Tf819GA.172@upnetnews05>...
>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
>I have a question to ask of this newsgroup.
>I have seen quite a few "GOTO"s, in several programs,  should I remove them
>or leave them intact?

The golden rule of maintenance is to do only ONE thing at a time.
So if you are fixing Y2K don't mess with anything else.
Leave the GO TO structure the way it is.


Also, do NOT try to change the coding style of the original program.
```

##### ↳ ↳ Re: Ethical Question

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sp4p5$ld4$2@news.enterprise.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35efdd51.0@news1.ibm.net>`

```
In article <35efdd51.0@news1.ibm.net>, leif@ibm.net says...

>The golden rule of maintenance is to do only ONE thing at a time.

Oh yes indeed and book it back into your source control system after each step 
too.

>So if you are fixing Y2K don't mess with anything else.
>Leave the GO TO structure the way it is.

As others have said - if it ain't broke, don't touch it.

>
>
>Also, do NOT try to change the coding style of the original program.
>

Of the original sure but if you're adding code, I don't think you should 
restrict your coding style to an outdated style guide. Eg. I don't think you 
should use GO TO's instead of EVALUATE just because the original style guide 
didn't support ANSI85 syntax.
```

#### ↳ Re: Ethical Question

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f52a8f.2624900@news.teo-computer.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05>`

```
"Garry Dell" <Garry_dell@hotmail.com> wrote:

>I am doing some y2k conversions and I am comming across some extremely
>poorly written code.
…[7 more quoted lines elided]…
>

Depends on a lot of factors.

But first, is there time to do this additional work, and do you think
it's necessary.

Any program that is enhanced and maintained quite a bit, can be
justified for trying to make the code more maintainable.  Otherwise,
if it works, don't fixit.

Multiple GOTOs can lead to "spaghetti" code.   GOTOs should be,
generally speaking, avoided, but IMO, I think it's a mistake to
totally avoid GOTOs, on grounds of strict structured doctrine.

Something else you also need to keep in mind, is that all programmers
have different styles.  Some good, some very different, but still
good, and some not so good.  Whenever enhancing a program, try and
keep the logic flow consistant.  Radically different styles in the
same program will make things very difficult for the next programmer
to work on the program in question.

Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

##### ↳ ↳ Re: Ethical Question

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F606ED.B26FBDE1@mindspring.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com>`

```
I'm not a professional, but in some pgms of mine, I use go to's.  For
instance, 1st part of the pgm is screen i-o say 13-14 lines.  Since i am
coding every last detail, after each prompt the pgm has to check for
f-12 to back-up a prompt or exit, or f-4 "done with whatever", i tried
it with performs and it came out just as long either way.  after part 1,
part 2 is printing some report; from the f-4 i go to part 2.  as long as
the code is neat and well-documented, why not?

Tim Oxler wrote:
> 
> "Garry Dell" <Garry_dell@hotmail.com> wrote:
…[36 more quoted lines elided]…
> http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: Ethical Question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com>`

```
skidmike wrote:
>I'm not a professional, but in some pgms of mine, I use go to's.  For
>instance, 1st part of the pgm is screen i-o say 13-14 lines.  Since i am
…[4 more quoted lines elided]…
>the code is neat and well-documented, why not?

For very good reasons, why not.  From around 1960, there was a significant
amount of reaearch done on what makes 'good' code.  One of the surprising
things found (very, very, mucho good evidence) is that excessive use of
GO TO results in poor code.  This prompted Edsger W. Dijkstra's now famous
article in the March 1968 "Communications of the ACM", "Goto Statement
Considered Harmful".  The resulting uproar resulted in the formulation of
what we call "Structured Programming" and "Structured Design".  One of the
tenets of structured programming is that GO TO, if used at all, must be
confined to a very narrow pattern of use.

No one who is knowledgable about the issue would argue that this is not a
good idea.  The argument is about just how far we should go (not GO TO)
in eliminating GO TO. :)  One camp believes GO TO is like a disease, never
good, and should be eliminated entirely, no exceptions.  The other camp
believes that, while GO TO can be dangerous, there are certain very
limited uses for which GO TO is useful, and not harmful.  In general, you
will find that everyone agrees on at least this: that every code block
should have only one entry and only one exit point, and that the code block
should be called (or PERFORMED), and that there should *NEVER, EVER* be a
GO TO out of the code block.  That this is a good idea can be mathematically
proven.

In COBOL, this means that every paragraph is PERFORMED, and the only GO TO
ever allowed (if even that) is a GO TO the paragraph exit.  Understand, the
only real argument is whether we use

       PERFORM paragraph
          THRU paragraph-exit

    paragraph.
       ...
       GO TO paragraph-exit.
       ...
    paragraph-exit.
       EXIT.

and permit the GO TO exit, or

       PERFORM paragraph

    paragraph.
       ...

with no GO TO ever allowed.  Note that the only reason for using the
former instead of the latter is that most languages support constructs
to permit an early exit from a code block (here, a paragraph), but the
current COBOL 85 standard does not.  The new standard in progress does
support such constructs, and then the argument will be moot.  Without
an EXIT PARAGRAPH statement, the code will inevitably be more
complicated at times.  The disagreement is over whether it is better
to use GO TO to simplify the code, or to avoid GO TO altogether, even
at the cost of more complex code.

Having originally tried eliminating GO TO altogether, and seeing the
added costs in extra and more complex code, I personally use PERFORM
... THRU exit and GO TO exit.  But I will drop it like a hot potato
when EXIT PARAGRAPH is available.  Hopefully before I retire. :-)
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 4)_

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t5tcf$o3q$1@news.enterprise.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>`

```
In article <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>, 
judmc123@bellsouth.net says...
>
>
…[3 more quoted lines elided]…
>when EXIT PARAGRAPH is available.  Hopefully before I retire. :-)

Why not just use sections all the time instead of paragraphs. Then use EXIT 
SECTION. You also avoid completely the PERFORM ... THROUGH trickle problem 
where another programmer inserts an unconnected paragraph in the middle of your 
PERFORM ... THROUGH 'structure'. 

If you use sections, you can avoid GO TO completely and not be forced into 
adding EXIT paragraphs.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 5)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f6a01f.0@news2.uswest.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net>`

```
Shaun C. Murray wrote in message <6t5tcf$o3q$1@news.enterprise.net>...
>In article <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>,
>judmc123@bellsouth.net says...
…[9 more quoted lines elided]…
>where another programmer inserts an unconnected paragraph in the middle of
your
>PERFORM ... THROUGH 'structure'.
>
…[6 more quoted lines elided]…
>


My COBOL Reference manual from IBM says that SECTION is an organizational
division, and doesn't go any farther.  Our local shop's standard is to avoid
SECTION or PEFROM-THRU (and no GO TOs under any circumstances, it's that
camp of thought).

However, SECTION is obviously more than just this, because when sections and
paragraphs are mixed, as IBM puts it, "Your results may be unpredictable."

Does anyone know what SECTIONS are really for?  Beyond the organizational
feature.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t6afi$hg5$1@callisto.clark.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net>`

```
In article <35f6a01f.0@news2.uswest.net>,
Chris Osborne <chris_n_osborne@yahoo.com> wrote:

[snippolinio]

>Does anyone know what SECTIONS are really for?  Beyond the organizational
>feature.

Paging efficiency.

DD
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 7)_

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F75ADD.1E59@netbox.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:
> >Does anyone know what SECTIONS are really for?  Beyond the organizational
> >feature.
…[3 more quoted lines elided]…
> DD

But how many people remember the early days of Virtual Storage, and
aligning your CSECTS in the load module for efficiency ?

Bob
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 8)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f80dff.0@news2.uswest.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net> <35F75ADD.1E59@netbox.com>`

```
I've read that it used to be done, but didn't know it was related to
SECTIONs.


Bob Berman wrote in message <35F75ADD.1E59@netbox.com>...
>docdwarf@clark.net wrote:
>> >Does anyone know what SECTIONS are really for?  Beyond the
organizational
>> >feature.
>>
…[15 more quoted lines elided]…
><----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 9)_

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F8B106.3F47@netbox.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net> <35F75ADD.1E59@netbox.com> <35f80dff.0@news2.uswest.net>`

```
Chris Osborne wrote:
> 
> I've read that it used to be done, but didn't know it was related to
…[15 more quoted lines elided]…
> >Bob

Sections generate CSECTS - if you aligned your CSECTS on a page
boundary, it was more likely that the all of the code relating to a
function, within a section, would be in main memory, and not be split
over multiple pages (4K), some of which might be paged out to virtual
storage

Bob.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 10)_

- **From:** "M.Kobobel" <classicmek@sprynet.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbahc$aga$1@juliana.sprynet.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net> <35F75ADD.1E59@netbox.com> <35f80dff.0@news2.uswest.net> <35F8B106.3F47@netbox.com>`

```
<<Sections generate CSECTS - if you aligned your CSECTS on a
page
boundary, it was more likely that the all of the code
relating to a
function, within a section, would be in main memory, and not
be split
over multiple pages (4K), some of which might be paged out
to virtual
storage>>

Seems to me I remember a long - long time ago that sections
were assigned numbers, and in the environment division you
could specify SEGMENT LIMIT IS to control how the compiler
broke up your code for this purpose.

Bob Berman wrote in message <35F8B106.3F47@netbox.com>...
>Chris Osborne wrote:
>>
>> I've read that it used to be done, but didn't know it was
related to
>> SECTIONs.
>>
>> Bob Berman wrote in message <35F75ADD.1E59@netbox.com>...
>> >docdwarf@clark.net wrote:
>> >> >Does anyone know what SECTIONS are really for?
Beyond the
>> organizational
>> >> >feature.
…[5 more quoted lines elided]…
>> >But how many people remember the early days of Virtual
Storage, and
>> >aligning your CSECTS in the load module for efficiency ?
>> >
>> >Bob
>
>Sections generate CSECTS - if you aligned your CSECTS on a
page
>boundary, it was more likely that the all of the code
relating to a
>function, within a section, would be in main memory, and
not be split
>over multiple pages (4K), some of which might be paged out
to virtual
>storage
>
>Bob.
>--
><----------------------------------------------------------
------------>
>                 Bob Berman   -    West Hartford, CT
>  mailto:bberman@netbox.com    homepage:
http://www.ntplx.net/~bberman
>
>                 THE TRUE TERRORISTS IN AMERICA ARE
>          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !
><----+----+----+----+----+----+----+----+----+----+----+---
-+----+----+>
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t8m2o$lad$1@callisto.clark.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net> <35F75ADD.1E59@netbox.com>`

```
In article <35F75ADD.1E59@netbox.com>, Bob Berman  <bberman@netbox.com> wrote:
>docdwarf@clark.net wrote:
>> >Does anyone know what SECTIONS are really for?  Beyond the organizational
…[7 more quoted lines elided]…
>aligning your CSECTS in the load module for efficiency ?

I would say that those who have done their own homework would know of such
things... consider the following interchange:

'How many particles are in a gram-equivalent weight of an element or
compound?

'Avogadro's number.'

Asked and answered, no?

DD
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 9)_

- **From:** Ibis redibis numquam peribis <rrg10300@dasb.fhda.edu>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.OSF.4.03.9809130045140.11282-100000@octane.dasb.fhda.edu>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f6a01f.0@news2.uswest.net> <6t6afi$hg5$1@callisto.clark.net> <35F75ADD.1E59@netbox.com> <6t8m2o$lad$1@callisto.clark.net>`

```


On 10 Sep 1998 docdwarf@clark.net wrote:

=> In article <35F75ADD.1E59@netbox.com>, Bob Berman  <bberman@netbox.com>
=> wrote:
=> >docdwarf@clark.net wrote:
=> >> >Does anyone know what SECTIONS are really for? Beyond the organizational
=> >> >feature.
=> >> 
=> >> Paging efficiency.
=> >> 
=> >> DD
=> >
=> >But how many people remember the early days of Virtual Storage, and
=> >aligning your CSECTS in the load module for efficiency ?
=> 
=> I would say that those who have done their own homework would know of
=> such things... consider the following interchange:
=> 
=> 'How many particles are in a gram-equivalent weight of an element or
=> compound?
=> 
=> 'Avogadro's number.'
=> 
=> Asked and answered, no?
=> 
=> DD
=> 
=> 
=> 
Are those "elementary particles" ?

rrg
=====================================================
Scattered sciences, remnants of a shattered Science

moles and molecules...her and hercules

and now for something compleatly different:

UNIFIED FIELD THEORY		
by Tim Joseph (amended by rrg aka ibis)

          I
In the beginning there was Aristotle.
And objects at rest tended to remain at rest,
And objects in motion tended to come to rest,
And soon everything was at rest.
And God saw that it was boring.

          II
Then God created Newton.
And objects at rest tended to remain at rest,
And objects in motion tended to remain in motion,
And energy was conserved, and momentum was conserved, 
          and matter was conserved.
And God saw that it was conservative.

          III
Then God created Einstein.
And everything was relative.
And fast things became short,
And straight things became curved,
And the universe was filled with inertial frames.
And God saw that it was relatively general, but some of it
                    was especially relative.

          IV
Then God created [Planck]
And there was the principle,
And the principle was quantum,
And all things were quantified,
But some things were still relative.
And God saw that it was confusing.

                                   V
                         Wherefore God created Pauli.
                         And Pauli begat Heisenberg.
                         From Pauli there was limited vacancy,
                         And Heisenberg found it to be uncertain.
                         And God saw that the confusion was indeterminate.

                                   VI
                         Wherefore God created Schroedinger.
                         And Schroedinger begat De Broglie.
                         And waves were probable,
                         And matter was wavy,
                         And waves were material.
                         And God saw that the confusion was dualistic.

         VII
Then God was going to create Furgeson.
And Furgeson would have unified,
And he would have fielded a theory,
And all would have been one.
But it was the seventh day,
And God rested,
And objects at rest tend to remain at rest.

=====================================================
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t6jdd$94h$1@news.igs.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net>`

```
>Does anyone know what SECTIONS are really for?  Beyond the organizational
>feature.
>

Most Cobol compilers use quite different programs for each section.
While that was probably not the original purpose, it does make the
compiler writer's job easier ... keeping in mind that most original Cobol
compilers were written for extremely small computers.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f6d3eb.0@news1.ibm.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <35f6a01f.0@news2.uswest.net> <6t6jdd$94h$1@news.igs.net>`

```

Donald Tees wrote in message <6t6jdd$94h$1@news.igs.net>...
>>Does anyone know what SECTIONS are really for?  Beyond the organizational
>>feature.
…[4 more quoted lines elided]…
>compilers were written for extremely small computers.


SECTIONS were a means of making and managing "overlays" of
code, so that the program would fit in the small memory of earlier
computers. I still have a Cobol program that in the environment
section specifies that it needs 400 words of core to run.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** john@watkins.cix.[nospam]co.uk (John Watkins)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<memo.19980911002258.161R@john.watkins.cix.co.uk>`
- **References:** `<35f6a01f.0@news2.uswest.net>`

```
> Does anyone know what SECTIONS are really for?  Beyond the organizational
> feature.

We are a 'SECTION shop'. This means you get code style like this:

A000-MAIN SECTION.

    PERFORM B000-DO-SOMETHING.
    
    GOBACK.

B000-DO-SOMETHING SECTION.

    blah
    blah
    IF ERROR GOTO B000-MAIN-EXIT.
    blah
    blah
    and now fall though to EXIT paragraph...
    
B000-MAIN-EXIT.
    EXIT.    
    
In pre-ANSI'85 COBOL this meant that you could avoid excessive flag testing 
and/or nested IF statements by jumping out to the EXIT paragraph. Of course 
any section longer than 40 lines (just under two terminal screens) should be 
re-structured.

+--------------+------------------------------------+
| John Watkins | mailto:john@watkins_dot_cix.co.uk  |
|              | http://www_dot_cix.co.uk/~watkins/ |
+--------------+------------------------------------+
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 7)_

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F88B21.E3916358@inficad.com>`
- **References:** `<35f6a01f.0@news2.uswest.net> <memo.19980911002258.161R@john.watkins.cix.co.uk>`

```
SECTIONS were added to COBOL to allow the complilation of program OVERLAYS.
PERIOD, PARAGRAPH.
Any other use has been added or became a feature that was unintended at the
time.
If your compiler SUPPORTS sections as designed, then a program that might
require
several megs to run (pick your own size), might run in a few, or only one meg of
RAM.

SECTIONS were important when RAM was very restricted.  There are situations
today where one might wish to page the code rather than pass the data.

Warren Simmons


John Watkins wrote:

> > Does anyone know what SECTIONS are really for?  Beyond the organizational
> > feature.
>
> We are a 'SECTION shop'. This means you get code style like this:
>
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-t29kndNYWQHd@Dwight_Miller.iix.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net>`

```
On Wed, 9 Sep 1998 12:47:11, scm@enterprise.net (Shaun C. Murray) 
wrote:

> Why not just use sections all the time instead of paragraphs. Then use EXIT 
> SECTION. You also avoid completely the PERFORM ... THROUGH trickle problem 
> where another programmer inserts an unconnected paragraph in the middle of your 

Cause if your compiler does not support Exit Paragraph, it likely does
not support Exit Section - both are part of the NEXT standard.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** beta1@bigfoot.com
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F71CBD.952D7E08@bigfoot.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <6t5tcf$o3q$1@news.enterprise.net> <Jl0PnHJ5PvPd-pn2-t29kndNYWQHd@Dwight_Miller.iix.com>`

```
Go to paragraph-exit.

Exit paragraph.

When the latter is available, it will generate the same code as the former now does
-- a branch to the end of the block of code.

A rose by any other name is still ... a go to.

Thane Hubbell wrote:

> On Wed, 9 Sep 1998 12:47:11, scm@enterprise.net (Shaun C. Murray)
> wrote:
…[6 more quoted lines elided]…
> not support Exit Section - both are part of the NEXT standard.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298251.82430.28056@kcbbs.gen.nz>`
- **References:** `<6t5tcf$o3q$1@news.enterprise.net>`

```
In message <<6t5tcf$o3q$1@news.enterprise.net>> scm@enterprise.net  writes:
> 
> Why not just use sections all the time instead of paragraphs. Then use EXIT 
…[5 more quoted lines elided]…
> adding EXIT paragraphs.

I think that you are confused.

The only reason to choose perform section or perform thru over
perform paragraph is that it is possible to do a GO TO in the
first two but cannot in the last.

If you do not use sections but only ever do a perform paragraph
then it eliminates the possibility of GO TO.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 4)_

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f68512.1073336@news.teo-computer.com>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>`

```
"Judson McClendon" <judmc123@bellsouth.net> wrote:


>
>Having originally tried eliminating GO TO altogether, and seeing the
…[3 more quoted lines elided]…
>--

Agreed.

The only other use of GO TO that I use is:

READ file
    AT END
        GO TO paragraph exit


But I have to say, if I'm enhancing a program that is "GO TO less", I
will try and keep the logic style, and try to avoid adding GO TOs.

Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F6CA10.C08CB01E@att.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f68512.1073336@news.teo-computer.com>`

```
Tim Oxler wrote:
> 
(snip)
> Agreed.
> 
…[4 more quoted lines elided]…
>         GO TO paragraph exit

No longer necessary to do this (assuming IBM and COBOL II, or higher):

READ file
     AT END
         SET END-OF-INPUT-FILE TO TRUE  (or)  MOVE 'Y'  TO
INPUT-FILE-SWITCH
     NOT AT END
         PERFORM record_processing_logic
END-READ

> But I have to say, if I'm enhancing a program that is "GO TO less", I
> will try and keep the logic style, and try to avoid adding GO TOs.

I'm with you.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F7B868.A71ED662@infonet.com.py>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f68512.1073336@news.teo-computer.com> <35F6CA10.C08CB01E@att.net>`

```


Bill Lynch wrote:

> Tim Oxler wrote:
> >
…[24 more quoted lines elided]…
> Bill Lynch

Any reason not to use declarative and the FILE-STATUS variable? Then:

02 w-file-status PIC X(2).
    88  status-ok VALUE "00".
    88  end-file VALUE "10".
    88  others...

READ file
IF status-ok
    PERFORM record_processing_logic

I [ab]use the file status variable for a lot of things. It's practical
because you can invent your own "exceptions".

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 7)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F7ED4E.53FB38CD@att.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f68512.1073336@news.teo-computer.com> <35F6CA10.C08CB01E@att.net> <35F7B868.A71ED662@infonet.com.py>`

```
Nope.

Albert Ratzlaff wrote:
> 
> Bill Lynch wrote:
…[44 more quoted lines elided]…
> Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 4)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f69e4f.0@news2.uswest.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net>`

```
Judson McClendon wrote in message ...
>skidmike wrote:
>>I'm not a professional, but in some pgms of mine, I use go to's.  For
…[26 more quoted lines elided]…
>GO TO out of the code block.  That this is a good idea can be
mathematically
>proven.
>
…[42 more quoted lines elided]…
>

I've only been professionally programming for a year, but so far I just
haven't found a reason to use GO TOs on my own.

To go hand in hand with this, I'm porting a COBOL application off an old
Prime computer to an IBM mainframe.  The code is classic GO TO filled
spaghetti.  One of my assistant programmers is often heard to say, "I'm
Italian, and even I can't follow it."

The programmer who wrote the original code felt no hesitation to read or
write to the five files used by the program from anywhere in the program.
He felt no hesitation to write the screen from anywhere (I just checked, and
he has over 240 separate lines of code writing to the screen).  He,
apparently, felt an unrelenting compulsion to use GO TOs everywhere, and
this was written back in about 1987.  This is compounded by instances of
puzzling code, where the author did crazy things: like clearing an array by
moving spaces to each element in a loop instead of just moving spaces to the
group-item above the loop; individually initializing every variable in the
program to zero or spaces (hundreds of them) instead of just using
Initialize; and other, less easily explainable insanities.

Although, overall, I can just attribute the problems of the program to the
author's lack of skill (or whatever), the use of GO TOs, and file and screen
calls all over the place, definitely contribute to horror this code has
become.
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 5)_

- **From:** "Garry Dell" <Garry_dell@hotmail.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#KZMGyS39GA.91@upnetnews03>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f69e4f.0@news2.uswest.net>`

```
Here's one better!


6614 lines to print a one page report!
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 6)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f97e5d.0@news3.uswest.net>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f69e4f.0@news2.uswest.net> <#KZMGyS39GA.91@upnetnews03>`

```
Garry Dell wrote in message <#KZMGyS39GA.91@upnetnews03>...
>Here's one better!
>
>
>6614 lines to print a one page report!
>


I'll bite.  What crazy things did the author do?
```

###### ↳ ↳ ↳ Re: Ethical Question

_(reply depth: 7)_

- **From:** "Garry Dell" <Garry_dell@hotmail.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#HqW9G239GA.313@upnetnews05>`
- **References:** `<#CD7Tf819GA.172@upnetnews05> <35f52a8f.2624900@news.teo-computer.com> <35F606ED.B26FBDE1@mindspring.com> <ITtJ1.828$p61.1325388@news4.mia.bellsouth.net> <35f69e4f.0@news2.uswest.net> <#KZMGyS39GA.91@upnetnews03> <35f97e5d.0@news3.uswest.net>`

```
The program originally did several other things, then the write statements
(MANY!) were remmed out.
Chris Osborne wrote in message <35f97e5d.0@news3.uswest.net>...
>Garry Dell wrote in message <#KZMGyS39GA.91@upnetnews03>...
>>Here's one better!
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
