[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Style Recommendations

_52 messages · 17 participants · 1999-06_

---

### COBOL Style Recommendations

- **From:** Tina Hayworth <tinhay@saif.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375EA3B2.A714744@saif.com>`

```
There has been much debate in our shop lately about the use of the GOTO
and PERFORM THRU verbs.  At issues is weather they should be adopted as
standards, or completely prohibited.  Our goal is to conform to industry
accepted structured programming techniques, as well as to ensure the
code is clear, and easy to maintain.

Your opinion on this matter would be greatly appreciated.  Please read
the following proposal and respond with any comments or suggestions you
may have.

Thank You,


Situation:

During several recent code walk-thrus, we have raised the issue of COBOL
standards.  The code being reviewed contained deeply nested-ifs,
repeated flag checking, and redundant logic in order to comply with our
current coding standards.  Presently, our standards do not allow use of
the GO TO xxxx-EXIT or PERFORM THRU verbs.  Yet, careful and appropriate
use of these verbs would allow us to simplify code, and streamline
program flow.

Proposal:

We propose the following changes to our COBOL coding standards:

1. Always use the PERFORM THRU option for paragraph performs.  Provide a
corresponding exit for every paragraph containing only the EXIT verb.

2. Use the GO TO verb only to go to the corresponding exit of a
paragraph or to a termination module, and only when necessary to
simplify code.
```

#### ↳ Re: COBOL Style Recommendations

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jn4ci$af4@sjx-ixn9.ix.netcom.com>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
Check out DejaNews for almost monthly discussions of this topic in this
newsgroup.  The bottom-line is that there is NO "industry Standard" on this
topic.   I think that almost agrees that it is "bad" (not structured) to use
GO TO anything but a single "exit paragraph" associated with each "normal"
paragraph header.  Similarly, you are almost guaranteed to run into problems
if you use the "THRU" option of PERFORM and also allow any paragraph (or
section) name between the two names referenced in the PERFORM statement.
```

#### ↳ Re: COBOL Style Recommendations

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
Tina,

You don't say what COBOL your shop is using, but if it is one of the 
newer releases is may have a feature available that is specified in 
the pending standard.  This is:

Exit Paragraph 

and 

Exit Section 

Using these you can avoid the perform with Thru and the associated go 
to temptation, and you can still get the same "early exit" behavior.  

Check to see if your present compiler supports this.

Just My Opinion - but I would still not buy into the perform ... 
thru... with exits.

My early attempts at go to less programming had a lot of the 
characteristics you describe (switch checking etc), but my more recent
code is much cleaner - not because of early exit, but because of more 
experience with this coding method.  I can design the program to avoid
this extra switch checking.   This is accomplished mainly by further 
breaking down the functions of the paragraphs.



On Wed, 9 Jun 1999 17:26:10, Tina Hayworth <tinhay@saif.com> wrote:

> There has been much debate in our shop lately about the use of the GOTO
> and PERFORM THRU verbs.  At issues is weather they should be adopted as
…[32 more quoted lines elided]…
> 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com>`

```
EXIT PARAGRAPH/SECTION seems always to end up getting used just like GO TO
whatever-EXIT: too often. IMO it's six of one, have a dozen of the other.

EXIT PERFORM, OTOH, is one of my personal favorites!
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375f06ab.18058461@netnews>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net>`

```
'Twas Wed, 09 Jun 1999 21:00:34 GMT, when "Michael Mattias"
<michael.mattias@gte.net> illuminated comp.lang.cobol thusly:

> EXIT PARAGRAPH/SECTION seems always to end up getting used just like GO TO
> whatever-EXIT: too often. IMO it's six of one, have a dozen of the other.

It's less likely to be coded wrong.  You can GO TO 9200-EXIT when you
meant to GO TO 9400-EXIT, and there's nothing to tell you it's wrong.
Unfortunately, EXIT SECTION when you mean EXIT PERFORM, and you're not in
the last paragraph of a SECTION will branch out of the PERFORM range.  You
can avoid this problem by making all your PERFORMed routines single
paragraph SECTIONs.

> EXIT PERFORM, OTOH, is one of my personal favorites!

It won't be in the next standard (Cobol 2002 give or take a year) but I'll
try to get into the one after (Cobol 2021, at the current rate).
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jn5ae$js3@dfw-ixnews8.ix.netcom.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews>`

```

Randall Bart <Barticus@att.spam.net> wrote in message
news:375f06ab.18058461@netnews...
> 'Twas Wed, 09 Jun 1999 21:00:34 GMT, when "Michael Mattias"
> <michael.mattias@gte.net> illuminated comp.lang.cobol thusly:
   <snip>
>
> > EXIT PERFORM, OTOH, is one of my personal favorites!
>
> It won't be in the next standard (Cobol 2002 give or take a year) but I'll
> try to get into the one after (Cobol 2021, at the current rate).

Randall,
  What makes you say this?  The "EXIT PERFORM" variation (with and without
the "CYCLE" option) has been in every draft of the next Standard for quite a
while now.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375f1bf7.1433212@netnews>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com>`

```
'Twas Wed, 9 Jun 1999 20:44:39 -0500, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

> Randall Bart <Barticus@att.spam.net> wrote in message
> news:375f06ab.18058461@netnews...
…[12 more quoted lines elided]…
> while now.

I'm sorry, I forgot that it was half implemented.  Yes, in the next
standard you can use EXIT PERFORM within an inline PERFORM.  Unfortunately
you cannot do EXIT PEFORM within a PERFORMed procedure -- as an
alternative to GO TO EXIT -- which was the feature being discussed.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jn6ta$sgk@sjx-ixn6.ix.netcom.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews>`

```
Randall Bart <Barticus@att.spam.net> wrote in message
news:375f1bf7.1433212@netnews...
> 'Twas Wed, 9 Jun 1999 20:44:39 -0500, when "William M. Klein"
> <wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:
…[9 more quoted lines elided]…
> > > It won't be in the next standard (Cobol 2002 give or take a year) but
I'll
> > > try to get into the one after (Cobol 2021, at the current rate).
> >
> > Randall,
> >   What makes you say this?  The "EXIT PERFORM" variation (with and
without
> > the "CYCLE" option) has been in every draft of the next Standard for
quite a
> > while now.
>
…[3 more quoted lines elided]…
> alternative to GO TO EXIT -- which was the feature being discussed.

OK,
  Now I am even more confused.  What you are talking about is exactly what
EXIT SECTION/EXIT PARAGRAPH (in the draft) does.  Are you saing that what is
missing is a "single" option that both exits an inline procedure and an
out-of-line procedure?  If so, then this approach was explicitly rejected by
the Standards group.  I am not positive that I agreed with that decision but
it does solve the problem of what to do if you want to EXIT an entire
SECTION while in the middle of a performed paragraph.  (Details can be
provided if this description is unclear.)
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 7)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3761b2b3.14418416@netnews>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews> <7jn6ta$sgk@sjx-ixn6.ix.netcom.com>`

```
'Twas Wed, 9 Jun 1999 21:11:46 -0500, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

>   Now I am even more confused.  What you are talking about is exactly what
> EXIT SECTION/EXIT PARAGRAPH (in the draft) does.

Consider the following:

PERFORM A THRU B
...
ABC SECTION.
A.
...
B.
...
C.
...

From paragraph A there is no statement you can use which will exit 
PERFORM A THRU B.  There are other examples of things EXIT PERFORM could
handle which it doesn't

I'm not asking for this to be changed in the current draft, but EXIT
PERFORM/SECTION/PARAGRAPH is still deficient.  I hope it will be enhanced
in the subsequent standard.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jn9hh$43c@enews1.newsguy.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews>`

```
I like exit paragraphs and the 'perform...thru' structure because when 
you're reading the code it's a nice clear delimiter of where the paragraph
ends.  Go To is ok for early exit but just don't use it too often.  But
alas, the perform...thrus and gotos are just useless bug breeders for the
most part.  For maintenance it's not that bad to use a goto for early exit
because it's better than re-writing several paragraphs to fit 'structured'
logic; it's almost always better to change as little as possible as a
maintenance programmer.

Jeff

----------
In article <375f1bf7.1433212@netnews>, Barticus@att.spam.net (Randall Bart)
wrote:


> 'Twas Wed, 9 Jun 1999 20:44:39 -0500, when "William M. Klein"
> <wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:
…[28 more quoted lines elided]…
> l    |/ Has anyone in Washington DC read the US Constitution?
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 7)_

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376117dd.6620825@usenet.acw.vcu.edu>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews> <7jn9hh$43c@enews1.newsguy.com>`

```
"Jeff Baynard" <union27@macconnect.com> wrote:

>I like exit paragraphs and the 'perform...thru' structure because when 
>you're reading the code it's a nice clear delimiter of where the paragraph
…[5 more quoted lines elided]…
>maintenance programmer.

A trick I learned since the COBOL-85 standard is to use two periods
per paragraph in the PROCEDURE DIVISION: one at the paragraph label
and the other at the end of the paragraph block like so:

 xxx-performing-paragraph-name.
     do something
     if condition
        do some items
     end-if
     .
***  end of paragraph comment

Since the avent of COBOL-85 these scope delimiters are handy.  I like
to put a end-of-paragraph comment right after the stand-alone period
to help the maintenance programmer (also me) to spot the period at 4AM
in case the printer didn't put it there.  Being a comment, it doesn't
use up computer performance the way an exit-paragraph label would.

Just my two cent worth adjusted for inflation,

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-V0ndl49fPPkj@Dwight_Miller.iix.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews>`

```
On Thu, 10 Jun 1999 02:01:56, Barticus@att.spam.net (Randall Bart) 
wrote:

> 'Twas Wed, 9 Jun 1999 20:44:39 -0500, when "William M. Klein"
> <wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:
…[20 more quoted lines elided]…
> alternative to GO TO EXIT -- which was the feature being discussed.

I hate to be dense, but won't "EXIT PARAGRAPH" and "EXIT SECTION" 
handle this?

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 7)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37600AAF.6424@saif.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews> <Jl0PnHJ5PvPd-pn2-V0ndl49fPPkj@Dwight_Miller.iix.com>`

```
> 
> I hate to be dense, but won't "EXIT PARAGRAPH" and "EXIT SECTION"
> handle this?


IBM MVS/VM COBOL on the mainframe does not support these constructs.
Pete
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 8)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-neTXZC3qo17P@Dwight_Miller.iix.com>`
- **References:** `<375EA3B2.A714744@saif.com> <Jl0PnHJ5PvPd-pn2-ddJG34dHdE0y@Dwight_Miller.iix.com> <SBA73.479$1h3.21976@dfiatx1-snr1.gtei.net> <375f06ab.18058461@netnews> <7jn5ae$js3@dfw-ixnews8.ix.netcom.com> <375f1bf7.1433212@netnews> <Jl0PnHJ5PvPd-pn2-V0ndl49fPPkj@Dwight_Miller.iix.com> <37600AAF.6424@saif.com>`

```
On Thu, 10 Jun 1999 18:57:51, Pete Wirfs <petwir@saif.com> wrote:

> > 
> > I hate to be dense, but won't "EXIT PARAGRAPH" and "EXIT SECTION"
…[4 more quoted lines elided]…
> Pete

I know!  I just told you that in e-mail - COBOL for OS/390 and VM 
2.1.1 does not support it.  My reply was in reference to the NEXT 
standard, which does. 
<G>
-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: COBOL Style Recommendations

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hQx73.312$g07.17621@iad-read.news.verio.net>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
In article <375EA3B2.A714744@saif.com>, Tina Hayworth  <tinhay@saif.com> wrote:

[snippage]

>Situation:
>
…[6 more quoted lines elided]…
>program flow.

Oh dear... you are seeking a Standards Change!  Good luck and remember
that those who made it To The Top under those Standards did so, in part,
because they were *good* at implementing said Standards.

>
>Proposal:
…[8 more quoted lines elided]…
>simplify code.

This being the only Decent, Good, True and Sane way to write code I, of
course, agree with it.. but there are others who are of different
opinions, of course.

DD
```

#### ↳ Re: COBOL Style Recommendations

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375EC586.15D54F6@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
Tina Hayworth wrote:
> 
> There has been much debate in our shop lately about the use of the GOTO
…[30 more quoted lines elided]…
> simplify code.

If you check dejanews, you will find that we periodically have religious
wars on this topic.  There are some fine programmers on this news group
who agree with your recommendations.  I strongly disagree.  I am against
SECTIONS and PERFORM THRU (and by extention GO TO).  Maintenance
problems is my biggest complaint, but I also like it when programmers'
understanding is sufficient to write clear, simple code without exit
paragraphs.

Most of the people who agree with your proposed standards are willing to
change when the next ANSI of COBOL is released allowing for an EXIT
PARAGRAPH command (I believe that's the syntax).

With a good understanding on how to structure programs, the problem you
described goes away.
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375EFFD4.4384@saif.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> Tina Hayworth wrote:
…[47 more quoted lines elided]…
> described goes away.

Hummm.
Your last paragraph suggests that PERFORM THRU / GO TO EXIT
automatically means a program is not structured.  We were taught to use
this method in 1980 as part of Warnier/Orr structured programming
techniques.

So how do you define "structured"?  Exactly HOW does GO TO EXIT
un-structure a program?

Pete
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375FB889.71F9332@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com>`

```
Pete Wirfs wrote:
> 
> Your last paragraph suggests that PERFORM THRU / GO TO EXIT
…[7 more quoted lines elided]…
> Pete

And what you are taught must be true :->

The bottom line is that using GOTO's can be very structured.  The
problem is that it is much less likely to be structured by every
practicioner in the site.  Let alone the problem with copied code
and renumbering problems that Randall brought up.

A standard should contain:

	Standards :  hard and fast rules
	guidelines:  Solid rules that may be bent for various reasons
	suggestions: good practices that the best will follow.

The GOTO under MVS cobol is a guidline.  It may very well be the
best option to use it in one case.  Your compiler milage may vary.

Thane basically hits the nail on the head.  I started coding
'periodless' about 12 months ago.  I found that my code in this
style improved with use and I would not go back now.

My big question is is this a troll.  We regularly go over this and
GOTO's generally are accepted as a bad thing since 1960 something.

Ken
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375FBD6A.C1FCF445@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com>`

```
Pete Wirfs wrote:

> > With a good understanding on how to structure programs, the problem you
> > described goes away.
…[10 more quoted lines elided]…
> Pete

There are lots of ways to build a structure.  If you build your
structure from a blueprint (Warnier/Orr), you may or may not have a good
understanding on how structures work, beyond building that particular
structure.  If you have a good understanding of structured programs,
when your requirements change (no goto), you first think about changing
your structure to fit the requirements.

If you have a poor understanding of structured programs, you change your
code to emulate the old structure which was designed around different
requirements.  You replace the GOTO EXIT with switches or make other
code based solutions instead of structure based solutions.

Any planned structure is a structure.  But someone who understands how
structures/blue prints work can change the design to best fit into a new
environment.

Does my post make more sense now?
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jot0c$doh$2@server.cntfl.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com>`

```

Pete Wirfs wrote in message <375EFFD4.4384@saif.com>...
>Howard Brazee wrote:
[...]
>> Most of the people who agree with your proposed standards are willing to
>> change when the next ANSI of COBOL is released allowing for an EXIT
…[12 more quoted lines elided]…
>un-structure a program?

Bottom line? It doesn't! It provides for a single-entry/single-exit that
is characteristic of structured programming.

I would argue that EXIT PARAGRAPH is unstructured because
it provides multiple exits from a procedure. In fact, it is unstructured
at the language level and structured at the implementation level.

Incidently, I do not use PERFORM THRU / GO TO EXIT. I find it
just as easy and clear to use CONTINUE. Conditional processing
looks like:

paragraph-name.
    IF positive-condition
        CONTINUE
    ELSE
        statements
    END-IF
    .

paragraph-name.
    IF positive-condition
        statements
    [ELSE
        statements]
    END-IF
    .

I have EXIT PARAGRAPH available; but I have never found
any reason to use it in production code. Its best use might be
to extricate a programmer from deep and convoluted logic;
that is, equivalent to a GET-ME-OUT-OF-HERE statement.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<em39znpu#GA.174@cpmsnbbsa03>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com> <7jot0c$doh$2@server.cntfl.com>`

```
I disagree strongly with this practice. Too many shops are so terrified
about using negatives (probably because they usually screw it up) that
they'll go out of their way to write worse code in order to avoid it. I'll
take

If X Not = Y
  do whatever
End-If

over

If X = Y
  Continue because this is a bogus case anyway
Else
  do what you really wanted to do in the first place
End-If

anytime.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Rick Smith wrote in message <7jot0c$doh$2@server.cntfl.com>...

>Incidently, I do not use PERFORM THRU / GO TO EXIT. I find it
>just as easy and clear to use CONTINUE. Conditional processing
…[16 more quoted lines elided]…
>    .
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7khpb9$o13@dfw-ixnews11.ix.netcom.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com> <7jot0c$doh$2@server.cntfl.com> <em39znpu#GA.174@cpmsnbbsa03>`

```
Robert M. Pritchett - RMP Consulting Partners LLC <MSN.Bus.News@rmpcp.com>
wrote in message news:em39znpu#GA.174@cpmsnbbsa03...
> I disagree strongly with this practice. Too many shops are so terrified
> about using negatives (probably because they usually screw it up) that
…[17 more quoted lines elided]…
>

I was taught (and I don't know how true it is or how compiler-independent it
is) that there is at least some efficiency in placing the "most common"
event first.  Therefore, if "X= Y" is more common than "X not = Y", then I
would pefer the 2nd alternative.  This is definetly one of the types of code
where CONTINUE (to handle the most common situation) can well be useful.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kkdpt$rtk$3@server.cntfl.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com> <7jot0c$doh$2@server.cntfl.com> <em39znpu#GA.174@cpmsnbbsa03> <7khpb9$o13@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote in message <7khpb9$o13@dfw-ixnews11.ix.netcom.com>...
>Robert M. Pritchett - RMP Consulting Partners LLC <MSN.Bus.News@rmpcp.com>
>wrote in message news:em39znpu#GA.174@cpmsnbbsa03...
>> I disagree strongly with this practice. Too many shops are so terrified
>> about using negatives (probably because they usually screw it up) that
>> they'll go out of their way to write worse code in order to avoid it.
I'll
>> take
>>
…[12 more quoted lines elided]…
>> anytime.
[I did not receive Mr. Pritchett's message due to a news server problem.]

I view X = Y and X NOT = Y to be expressions in a positive form since
both make an assertion. OTOH, NOT (X = Y) is an expression in
negative form because the assertion is negated.

The primary use of IF with CONTINUE is to more closely match a
specification. Consider a specification which states, "employees
are NOT to receive a pay check if their status is 'terminated' or they
received a pre-payment." (Note: I did not use 88's on purpose!)

IF employee-status = "T"
        OR employee-prepaid = "Y"
    CONTINUE
ELSE
    PERFORM generate-pay-check
END-IF

is a clearer expression of the specification than

IF NOT (employee-status = "T"
        OR employee-prepaid = "Y")
    PERFORM generate-pay-check
END-IF

eventhough the results are the same. The more conditions one
must consider, the clearer the positive form becomes.

Now consider an example that you might "take anytime."

IF employee-status NOT = "T"
        AND employee-prepaid NOT = "Y"
    PERFORM generate-pay-check
END-IF

Is this last example a clearer expression of the specification
than the first? When one applies DeMorgan's Theorem, the
result frequently looks wrong.


>I was taught (and I don't know how true it is or how compiler-independent
it
>is) that there is at least some efficiency in placing the "most common"
>event first.  Therefore, if "X= Y" is more common than "X not = Y", then I
>would pefer the 2nd alternative.  This is definetly one of the types of
code
>where CONTINUE (to handle the most common situation) can well be useful.

For the evaluation of a simple condition, it isn't that important.

For evaluation of complex conditions using IF - OR place the most
likely success first. For IF - AND place the most likely failure first.

For EVALUATE with no sequential evaluation dependencies, place
the most likely success first. For EVALUATE with sequential
evaluation dependencies, place the most likely successes as early
as possible. If the implementation can generate a jump table due
to the type of selection subject and values of the selection object, the
order isn't that important.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376E2606.9A60D1BA@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com> <7jot0c$doh$2@server.cntfl.com> <em39znpu#GA.174@cpmsnbbsa03> <7khpb9$o13@dfw-ixnews11.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I was taught (and I don't know how true it is or how
…[5 more quoted lines elided]…
> 

I doubt it would make any difference. A simple condition is
translated to assembler like this:

test
Branch-not-zero x:
...
goto y
x:
....
y:

Therefore for a simple case there would be no difference, the test
is still done and the jumps are still done.

For more complex examples as is commonly the case, the order of
execution is very important.  This applies to loops as well:

   perform x
       until y not = z or
             eof

will commonly perform better than

   perform x
      until eof or
            y not = z

If y or z changes more often than eof.

Ken
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376c0f2a.22103907@netnews>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <375EFFD4.4384@saif.com> <7jot0c$doh$2@server.cntfl.com> <em39znpu#GA.174@cpmsnbbsa03>`

```
'Twas Sat, 19 Jun 1999 16:22:29 -0500, when "Robert M. Pritchett - RMP
Consulting Partners LLC" <MSN.Bus.News@rmpcp.com> illuminated
comp.lang.cobol thusly:

> I disagree strongly with this practice. Too many shops are so terrified
> about using negatives (probably because they usually screw it up) that
> they'll go out of their way to write worse code in order to avoid it.

How about this for a piece of COBOL-74 code by someone who thinks it's
always better to phrase things in the positive:

IF  ((STATUS-CHANGE-DATE > CONTROL-RANGE-BEGIN-DATE)
      OR (STATUS-CHANGE-DATE = CONTROL-RANGE-BEGIN-DATE))
     AND ((STATUS-CHANGE-DATE < CONTROL-RANGE-END-DATE)
       OR (STATUS-CHANGE-DATE = CONTROL-RANGE-END-DATE))
    NEXT SENTENCE
ELSE
    GO TO END-OF-ROUTINE.

I told him it was better to write 

IF  STATUS-CHANGE-DATE < CONTROL-RANGE-BEGIN-DATE
                   OR  > CONTROL-RANGE-END-DATE
    GO TO END-OF-ROUTINE.

but he thought this was harder to understand.
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jonhn$lkm$1@nnrp1.deja.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com>`

```
In article <375EC586.15D54F6@NOSPAMhome.com>,
  Howard Brazee <brazee@NOSPAMhome.com> wrote:

<snip a lot>

< I am against SECTIONS and PERFORM THRU (and by extention GO TO)

<snip the rest>

Sorry, I don't understand you. What is wrong with SECTIONS? I never
coded THRU, I never coded a paragraph. All my programs are divided into
SECTIONs without any labels between the section-name and the ending dot
of the section. After the dot: another SECTION or the END of the
Program. Do you think this style is not OK? What makes you believe that
paragraphs are better style than SECTIONs?
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AQT73.67$S2.4230@iad-read.news.verio.net>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com>`

```
In article <7jonhn$lkm$1@nnrp1.deja.com>,
Daniel Jacot  <daniel.jacot@winterthur.ch> wrote:
>In article <375EC586.15D54F6@NOSPAMhome.com>,
>  Howard Brazee <brazee@NOSPAMhome.com> wrote:
…[12 more quoted lines elided]…
>paragraphs are better style than SECTIONs?

Ummmmm... I am confused.  What I read you as saying here is:

PROCEDURE DIVISION.

    PERFORM 1000-HOUSEKEEPING.
    PERFORM 5000-MAIN-LINE UNTIL NO-MORE-INPUT.
    PERFORM 900-EOJ.
    GOBACK.

1000-HOUSEKEEPING SECTION.

    OPEN files
    ACCEPT dates
    READ initial-records
    (more of the same)
    .                  <== only '.' in section

5000-MAIN-LINE SECTION.

    IF record-meets-processing-criteria
      (do a bunch of stuff)
    ELSE
        READ driver-file
          AT END SET NO-MORE-INPUT TO TRUE
    .                  <== only '.' in section

9000-EOJ SECTION.

    CLOSE files
    IF any-recs-meet-criteria
        (do total-tiruals)
    .                  <== only '.' in section

.. and if this is, in fact, what you are stating as a good practise then I
am confused as to what benefit there is to including the extra word of
'SECTION'; these 'sections' have, to my eye, the exact same function as
paragraphs.

DD
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hXT73.3280$hh1.1045@news1.mia>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <AQT73.67$S2.4230@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
>
>PROCEDURE DIVISION.
…[3 more quoted lines elided]…
>    PERFORM 900-EOJ.

*** SYNTAX ERROR: LABEL 900-EOJ UNDEFINED ***     ;-)

>    GOBACK.
>
…[27 more quoted lines elided]…
>paragraphs.


I agree.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jp4m6$i5q$1@server.cntfl.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com>`

```

Daniel Jacot wrote in message <7jonhn$lkm$1@nnrp1.deja.com>...
>In article <375EC586.15D54F6@NOSPAMhome.com>,
>  Howard Brazee <brazee@NOSPAMhome.com> wrote:
…[13 more quoted lines elided]…
>
Ah, yes, the old sections versus paragraphs debate!

The primary objections are in the form of a proscription; that is,
if one does not use sections, one cannot introduce paragraphs
with the possibility of unintended fall-through when performing the
section or the GO TO xxxx-EXIT that would be required. One
cannot introduce a coding error due to failing to include the word
SECTION. Finally, it requires more typing. There are other
objections, as well.

Other than that, it is not a problem. I have used that style myself.
If you are comfortable with using sections in the manner you
described, by all means, continue using them.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3760244A.4A5A1A12@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com>`

```
Daniel Jacot wrote:
> 
> In article <375EC586.15D54F6@NOSPAMhome.com>,
…[13 more quoted lines elided]…
> paragraphs are better style than SECTIONs?

It sounds like you are using SECTIONs the same way as I use PARAGRAPHs. 
If everything is working correctly, there's no advantage either way. 
The disadvantage is if some maintenance programmer adds a new performed
piece of code and forgets to put SECTION after the name.  He now has a
PARAGRAPH which is inadvertently called by the SECTION above it.   Of
course, the reverse can happen, someone can accidentally make a
paragraph the first paragraph of a SECTION, but I think that's less
likely.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jqgkt$ad4$1@nnrp1.deja.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com>`

```
In article <3760244A.4A5A1A12@NOSPAMhome.com>,
  Howard Brazee <brazee@NOSPAMhome.com> wrote:

> It sounds like you are using SECTIONs the same way as I use
> PARAGRAPHs. If everything is working correctly, there's no advantage
…[5 more quoted lines elided]…
> less likely.

Thank you for these explanations, Howard! Now I understand the problem.
I come from the PL/I side, and in my understanding of SECTIONS was, they
were somehow similar to PROC, but without parameters, without local
variables and without nesting. That's why I LOVE nested programs ;-)

The point is not to mix sections and paragraphs in the same source code,
I think. It's a pitty that there is no END-SECTION clause! This would
make the things clearer!
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#PnI3UFt#GA.137@nih2naaf.prod2.compuserve.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com> <7jqgkt$ad4$1@nnrp1.deja.com>`

```
<SNIP>

>> It sounds like you are using SECTIONs the same way as I use
>> PARAGRAPHs. If everything is working correctly, there's no advantage
…[6 more quoted lines elided]…
>
<SNIP>

    Actually, there is a difference between sections and paragraphs in the
16 bit world.
When the procedure division of a generated program exceeds 64K in size, the
MF
compiler can auto segment, but only at a section header.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uEoNxtpu#GA.174@cpmsnbbsa03>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com> <7jqgkt$ad4$1@nnrp1.deja.com>`

```
What I've found useful to do when there are sections (or when converting
perform-thru'd paragraph ranges to sections) is to create a dummy section
at the end of each section to serve as a section terminator to help prevent
destruction of sectioning when they get moved around etc. e.g.

ABC Section.
    do this
    do that
    .
End-Of-ABC Section.
    Exit.


XYZ Section.
    do this
    do that
    .
End-Of-XYZ Section.
    Exit.


The dummy sections may require Exit. to keep the compiler happy. Make sure
never to reference these end sections or you'll have the whole paragraph
exit label abuse problem back all over again. That's one more reason to get
rid of all the sectioning entirely if you get to finish the cleanup.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Daniel Jacot wrote in message <7jqgkt$ad4$1@nnrp1.deja.com>...

It's a pitty that there is no END-SECTION clause! This would
>make the things clearer!
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R_783.6548$Ej6.979@news3.mia>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com>`

```
Howard Brazee wrote:
>
>It sounds like you are using SECTIONs the same way as I use PARAGRAPHs.
…[6 more quoted lines elided]…
>likely.

How do you 'accidentally' type the word SECTION? ;-)  You can also
get rid of extraneous use of SECTION very easily by doing a regular
expression search and replace of the Procedure Division, replacing
one or more spaces, followed by "SECTION", followed by a period, with
a period.  Adding missing ones is much more difficult. :-)
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37610DAB.97BB5961@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com> <R_783.6548$Ej6.979@news3.mia>`

```
My shop has an IDMS ABORT copy member which is a section.  To avoid
syntax errors, I stick in a SECTION at the top of my code before my
first paragraph.  If your shop has no standard on whether to use
SECTIONS or PARAGRAPHS, or has old COBOL which required SECTIONs for
sorts, I can see why the copy you stick at the end of your program is a
SECTION (to avoid drop through code).

Inadvertant SECTIONs could also result from cut and pastes, Y2K copy
routines, etc.  But as I said, I think it is more likely to error the
other way around, so I'm in favor of eliminating sections.

Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[19 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3761B3E3.784E0006@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com> <3760244A.4A5A1A12@NOSPAMhome.com> <R_783.6548$Ej6.979@news3.mia> <37610DAB.97BB5961@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> My shop has an IDMS ABORT copy member which is a section.  To avoid
…[5 more quoted lines elided]…
> 

The section does not actually stop drop through.  Totally
confusing style and probably not realistic code to explain why:-

perform a thru b

a.  
    ...
	goto c
    ...
b.
	exit.

c.
    ...

d section.
    ...

Once the goto has gone then it just marches on through.  Maybe not
realistic because who would mix it up this much.

Ken
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uDxlyqpu#GA.196@cpmsnbbsa03>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jonhn$lkm$1@nnrp1.deja.com>`

```
That's fine in that case, and sections can be especially handy in
maintenance and when transitioning a program from Perform Thru ranges to
Sections to make them all straight Performs as part of a cleanup process -
better to perform a section than to perform thru a range of paragraphs.
However, if you get to carry this process to completion and have only
singly performed sections consisting of only one unlabelled paragraph each,
then you can get rid of all the Section words and you have singly performed
paragraphs, which is ideal. Then it makes it harder for someone else to
slip in extra paragraphs into your sections.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Daniel Jacot wrote in message <7jonhn$lkm$1@nnrp1.deja.com>...

>Sorry, I don't understand you. What is wrong with SECTIONS? I never
>coded THRU, I never coded a paragraph. All my programs are divided into
…[3 more quoted lines elided]…
>paragraphs are better style than SECTIONs?
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jot09$doh$1@server.cntfl.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com>`

```

Howard Brazee wrote in message <375EC586.15D54F6@NOSPAMhome.com>...
[...]
>Most of the people who agree with your proposed standards are willing to
>change when the next ANSI of COBOL is released allowing for an EXIT
>PARAGRAPH command (I believe that's the syntax).

The timing for changing from PERFORM THRU / GO TO EXIT to
EXIT PARAGRAPH is dictated by the compilers they must use,
not the approval of the standard! :-)

You are right though; a change is coming.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8UT73.3274$hh1.1315@news1.mia>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com> <7jot09$doh$1@server.cntfl.com>`

```
Rick Smith wrote:
>
>Howard Brazee wrote:
…[9 more quoted lines elided]…
>You are right though; a change is coming.

I've been one of the more vocal proponents of PERFORM/THRU and EXIT
paragraphs in the newsgroup.  But I would not use them at all, except
with a utility that verifies that PERFORM/THRU paragraphs match, and
no GO TO outside the paragraph.  Too dangerous.  And I will gladly
drop PERFORM/THRU and EXIT paragraphs altogether when EXIT PARAGRAPH
is available on all my target platforms.  Until then, I prefer to
write code that, as much as possible, compiles on all the platforms.
That unfortunately still includes COBOL 74. :-(

I don't think anybody here advocates any other use of GO TO at all,
except some do use it for error termination routines.  I prefer to
PERFORM those, myself.
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eWmKznpu#GA.174@cpmsnbbsa03>`
- **References:** `<375EA3B2.A714744@saif.com> <375EC586.15D54F6@NOSPAMhome.com>`

```
Sure, I'm a structured programming fanatic - although I know that
structured programs can be written with anything including GoTo's, I'm
against them because they also make it so easy to write unstructured
garbage. To me there's no excuse for including GoTo's in totally new
development, and as far as standards recommendations, I feel the same way
about Perform Thru, most forms of Exit, Sections, Next Sentence, Alter, and
periods except as the last thing in each paragraph and on lines by
themselves (if the compiler won't take it, use Exit. as the last stmt. in
each par.). I prefer pure usage of single-paragraph performed routines
only. The initial main paragraph would be the only one not Performed and
would also be the only place where there would be a GoBack or equivalent,
at the end and at top level only.

I could maybe see an Exit Perform for inline use as an exit in the middle
of a loop, but even that can be abused.

For maintenance, of course, you usually have to compromise somewhat with
the existing style - but I'm not sure that even here some of these new
standards proposals would be appropriate. Maybe better than GoTo's at
least.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: COBOL Style Recommendations

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375ec149.26054954@usenet.acw.vcu.edu>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
Tina Hayworth <tinhay@saif.com> wrote:

>There has been much debate in our shop lately about the use of the GOTO
>and PERFORM THRU verbs.  At issues is weather they should be adopted as
…[32 more quoted lines elided]…
>

A good way to start a flame war; I'll light the match...

I've never used PERFORM THRU in any of my COBOL programs and never
used GO TO since COBOL-85 (because SORT now support paragraphs and not
sections in its INPUT and OUTPUT PROCEDURE clauses).  IMHO these are
spaghetti code hooks waiting to happen.  A well-thought out design
using modern methodologies doesn't need these crutches.

My advice is: if your shop doesn't use these, don't introduce a
problem.  If your shop is using them, stop now and restructure the
programs at the next routine maintenance cycle.  If you're fixing a
broken program with PERFORM THRU's and GO TO's already in them, try to
patch it without adding more if you can.

Just my two cents worth adjusted for inflation,

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375EFAD9.745C@saif.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu>`

```
Boyce G. Williams, Jr. wrote:
> 
<snip>


I work with Tina.

Let me share some of the political background for this shop.  From 1980
to 1996, the standard was we always coded PERFORM THRU, and GO TO was
allowed only for the purpose of branching to an EXIT paragraph.  This
coupled with a homegrown code generator that built everything to our
standards made us very productive.  Maintenance became a breeze, because
every program was coded using the same style/structure.

Then in 1996, some "outsiders" were hired, and changed the standards
without any staff re-training! (Really smart, hu?)  The standards now
state that you may not use THRU, and you may not use GO TO.  But the
staff still perform maintenance and "think" in THRU / GO TO programming
style.

Even if re-training is the correct thing to do, we now have a huge
production inventory of programs that follow the THRU/GO TO EXIT style. 
And since we have become a client-server shop, we really don't write
very many new COBOL programs.  We now rely on EasytrievePlus for batch
applications, so new COBOL programs usually are limited to CICS.

So should we re-train?  Or should we change the standards back to 1980
so that there will be more consisency with our existing production
software inventory?  This is not a black-and-white question.

Other food for thought:
I personally have implemented several vendor products in the last 2
years that required I use their sample COBOL exits.  More often than
not, these vendor exits use PERFORM THRU / GO TO EXIT.  Therefore, it is
my opinion that this coding style, even if "old", still works very well
and is considered world-wide as an acceptable approach.

I too wish that EXIT PARAGRAPH existed.  This would support the "old"
structure technique without using THRU or GO TO.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375FBA4C.B2C5144E@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com>`

```
Pete Wirfs wrote:
> to 1996, the standard was we always coded PERFORM THRU, and GO TO was
> allowed only for the purpose of branching to an EXIT paragraph.  This
> coupled with a homegrown code generator that built everything to our
> standards made us very productive.  Maintenance became a breeze, 


Very different question.  Your style should rely on the code being
modified.  Modifying a 10,000 line program to a new style for a
simple change is a waste of time, don't do it.

When you reengineer the code significantly then the code is
restructured.  You need to be clear as to when this occurs before
the coder starts work.  If the change turns out easy then they
still renovate, if it turns out hard and they restructure a lot
then it their call (often you do not work out how big a change is
until after you have finished recoding half the program).

The problem with most code is that it is not fundamentally written
in the style of period less and the renovation is blind.  You
really need to dramatically move functionality around to make it
work.  If you are a maintenance shop then it will be tough to
change unless the other programmers are 100% sold.  The ones that
are not get the mickey mouse changes, the good ones get the meaty
ones.

Tough problem
Ken
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jofm6$7vn$1@news.igs.net>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com>`

```
I think consistancy more important than being GOTOless, provided that it is
controlled strictly by use of the standard "one paragraph, one exit that is
an "exit" statement" rules.  That is quite a workable standard, in my
opinion.  However, I would still outlaw the use of the "thru", and I would
also outlaw the use of GOTO outside the current paragraph, even to an abort
routine.

Pete Wirfs wrote in message <375EFAD9.745C@saif.com>...
>Boyce G. Williams, Jr. wrote:
>>
…[36 more quoted lines elided]…
>structure technique without using THRU or GO TO.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7joi5a$aq9$2@news.igs.net>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com> <7jofm6$7vn$1@news.igs.net>`

```
Sorry about that ... I meant outlaw the use of thru to any paragraph but the
single exit paragraph. IE:

para-name.
        lots
       of
       stuff.
para-name-exit. exit.

No other paragraph names in the middle.

donald tees wrote in message <7jofm6$7vn$1@news.igs.net>...
>I think consistancy more important than being GOTOless, provided that it is
>controlled strictly by use of the standard "one paragraph, one exit that is
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#uFRtzpu#GA.308@cpmsnbbsa03>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com>`

```
My recommendation would be to transition away from Perform Thru and Exit
and GoTo entirely. When maintaining an old program, new code should be in
the new style and clearly marked. It may even be worthwhile to convert all
Perform Thru ranges to Sections to help with this. Be sure and add a
warning at the top of the program that it's in transition. Educate everyone
in both styles as needed but all new code should be only in the new style.
I've found it handy especially when converting to sections to add e.g.


Single-Paragraph-Routines Section.

This-paragraph.
    do this
    do that
    .

That-paragraph.
    do whatever
    do something else
    .

End-Of-Single-Paragraph-Routines Section.
    Exit.


before/after the other sections as a place to put any newly added or
extensively modified paragraphs. Eventually most of the whole program will
be only this section when can then be unsectioned.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Pete Wirfs wrote in message <375EFAD9.745C@saif.com>...
>Boyce G. Williams, Jr. wrote:
>>
…[36 more quoted lines elided]…
>structure technique without using THRU or GO TO.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376E3BBB.A79BBCDE@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com> <#uFRtzpu#GA.308@cpmsnbbsa03>`

```
If you have exit paragraphs which should never be reached, why not
replace the NOP exit statement with a DISPLAY "THIS PARAGRAPH SHOULD NOT
BE PERFORMED - IF THIS DISPLAY OCCURS, PLEASE NOTIFY PROGRAMMER."  ??

Robert M. Pritchett - RMP Consulting Partners LLC wrote:
> 
> My recommendation would be to transition away from Perform Thru and Exit
…[72 more quoted lines elided]…
> >structure technique without using THRU or GO TO.
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376F7408.2889EE5F@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com> <#uFRtzpu#GA.308@cpmsnbbsa03> <376E3BBB.A79BBCDE@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> If you have exit paragraphs which should never be reached, why not
…[3 more quoted lines elided]…
> 

I have done this sort of coding (warning messages in source to say
things did not work out).  The bottom line is that it went into
production unchecked on at least two occassions.

If you want to put in these sort of messages make the message
terminal. This applies even if you put off the inevitable for the
end of program execution to maximise the warnings reported.

Ken
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376F8CB3.DCDF2824@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com> <#uFRtzpu#GA.308@cpmsnbbsa03> <376E3BBB.A79BBCDE@NOSPAMhome.com> <376F7408.2889EE5F@zip.com.au>`

```
Ken Foskey wrote:
> 
> Howard Brazee wrote:
…[9 more quoted lines elided]…
> production unchecked on at least two occassions.

So, it goes into production.  When things are working correctly, they
never display.  When things are working incorrectly, then you get warned
quickly.

> If you want to put in these sort of messages make the message
> terminal. This applies even if you put off the inevitable for the
> end of program execution to maximise the warnings reported.
> 
> Ken

Why?  I want them to exist when someone does poor maintenance (even for
an emergency fix) somewhere down the line.   If the code is working
correctly, the displays don't happen.

Of course, I don't write THRU statements, and the only time I write
sections is where I have an IDMS COPY containing a SECTION, so this only
would occur in maintenance.

Hmmm.  In regular copies can we do a COPY REPLACING to eliminate SECTION
?
```

###### ↳ ↳ ↳ Re: COBOL Style Recommendations

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3770CEFA.1EBFCEF7@zip.com.au>`
- **References:** `<375EA3B2.A714744@saif.com> <375ec149.26054954@usenet.acw.vcu.edu> <375EFAD9.745C@saif.com> <#uFRtzpu#GA.308@cpmsnbbsa03> <376E3BBB.A79BBCDE@NOSPAMhome.com> <376F7408.2889EE5F@zip.com.au> <376F8CB3.DCDF2824@NOSPAMhome.com>`

```
I will simplify. In MVS (where I am) displays do not appear in
your face, you must go looking for them in a job log.  This is
probably not the case in most other systems (syserr in unix and
the console (sorry window) on the PC).  The only thing that
mainframe programmers notice is a condition code (move X to
return-code) or an abend.

This may be a comment specific to MVS, however the C assert macro
does not display and quietly go on, it kills the program.

Ken
```

#### ↳ Re: COBOL Style Recommendations

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jmsj1$8v8$1@news.igs.net>`
- **References:** `<375EA3B2.A714744@saif.com>`

```
I am of the opinion that you should use neither GO TO's or PERFORM THRU's,
though I will grant that having a single exit and allowing goto's to that
exit is probably the most controversial issue in Cobol.

I tend to use pre-reads and more performs to get rid of the nested IF's.
However, with the new features, even those can be avoided.  The new scope
delimiters and the NOT AT END between them eliminate just about every reason
for the GO TO EXIT-PARAGRAPH conundrum.

Certainly, a GOTO a termination should NOT be allowed, even if you decide to
use the "every paragraph has an exit" method.  The reason is simple.  A
termination procedure is always error handling, and can be performed.  As
the languages and platforms evolve, error *correcting* procedures can be
developed.  For example, most of my code performs a print message and abort
procedure for Isam error status codes.  However, Fujitsu allows a dynamic
rebuild for scrambled Isam files.  Since the procedure is always performed
(but never returns because it has a GOBACK), it is going to be trivial to
impliment that new feature. If there were GO TO's, it could turn into a
nightmare.

Tina Hayworth wrote in message <375EA3B2.A714744@saif.com>...
>There has been much debate in our shop lately about the use of the GOTO
>and PERFORM THRU verbs.  At issues is weather they should be adopted as
…[32 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL Style Recommendations

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375FBB3E.BF5E9B50@NOSPAMhome.com>`
- **References:** `<375EA3B2.A714744@saif.com> <7jmsj1$8v8$1@news.igs.net>`

```
donald tees wrote:
> 
> Certainly, a GOTO a termination should NOT be allowed, even if you decide to
…[8 more quoted lines elided]…
> nightmare.

I agree with your other statements.  I prefer to design my code so that
there's no need for a GO TO EXIT.  But it seems a bit dishonest to
PERFORM ABORT-ROUTINE  or PERFORM GOBACK-ROUTINE.  While this is pretty
obvious, in general, dishonest code, or code which implies that it will
do one thing but which does another thing, should be avoided.

At any rate, I am very happy to approve any standard which proscribes GO
TO's, despite my misgiving here.  Then my goal is to teach people to
avoid replacing GO TO's with switches, but to structure their code
around the spirit of the standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
