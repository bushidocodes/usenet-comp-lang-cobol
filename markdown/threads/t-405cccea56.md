[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL interview tests

_19 messages · 9 participants · 2006-12_

---

### COBOL interview tests

- **From:** "krewser" <wkrusinski@yahoo.com>
- **Date:** 2006-12-24T21:02:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com>`

```
I interviewed with an organization 18 months ago.  During the interview
I was asked to take a COBOL programming test.  I've been programming
exclusively in COBOL for 20+ years and the first question threw me for
a loop.  Write a program from scratch to merge two files.  That was
easy enough but I have never written a COBOL program from scratch since
I studied it in school.  I never found out the results of this test.  I
didn't get the position and I was never informed as to why but I
believe that it may have been because of this test.

Another position with this organization might be opening up after the
1st of the year and I want to be better prepared for this test.  Does
anyone have any information on these types of tests?  Such as what are
the questions?  What results are they looking for?

Thanks for any help,
Bill
```

#### ↳ Re: COBOL interview tests

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-24T23:37:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ouotdhihfa3ef@news.supernews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com>`

```
krewser wrote:
> I interviewed with an organization 18 months ago.  During the
> interview I was asked to take a COBOL programming test.  I've been
…[12 more quoted lines elided]…
>

Take with you an example program that you did write and offer that as a 
substitute for their silly test. If that won't work...

I've found the following program more than adequate for these questions:

PROCEDURE DIVISION.
   CALL 'GET'
   CALL 'MULL'
   CALL 'PUT'
   STOP RUN.
```

#### ↳ Re: COBOL interview tests

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-26T23:23:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2aikh.152992$b%6.23128@fe10.news.easynews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com>`

```
Did you use the MERGE statement or write your own "merge logic"?  Other than 
that, I can't really imagine that "test" being very useful.
```

##### ↳ ↳ Re: COBOL interview tests

- **From:** "krewser" <wkrusinski@yahoo.com>
- **Date:** 2006-12-26T17:19:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167182376.588677.12330@73g2000cwn.googlegroups.com>`
- **In-Reply-To:** `<2aikh.152992$b%6.23128@fe10.news.easynews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <2aikh.152992$b%6.23128@fe10.news.easynews.com>`

```
I wrote my own merge logic.

I was wondering if anyone else ever ran into this test and what their
thoughts on it were.

Bill



William M. Klein wrote:
> Did you use the MERGE statement or write your own "merge logic"?  Other than
> that, I can't really imagine that "test" being very useful.
…[3 more quoted lines elided]…
>  wmklein <at> ix.netcom.com
```

##### ↳ ↳ Re: COBOL interview tests

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-27T11:57:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rctkh.2715$sR.286@newssvr29.news.prodigy.net>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <2aikh.152992$b%6.23128@fe10.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:2aikh.152992$b%6.23128@fe10.news.easynews.com...
> Did you use the MERGE statement or write your own "merge logic"?  Other 
> than that, I can't really imagine that "test" being very useful.

I don't know about that, Bill... if I used the word "merge" in my "story 
problem" and the prospective employee/contractor did not automatically reach 
for the COBOL 'MERGE' verb, I think I'd be at least a tad chary of ascribing 
COBOL expertise to that candidate.....

MCM
```

###### ↳ ↳ ↳ Re: COBOL interview tests

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-27T08:32:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lc45p25vhknn63n75lni5ue9klf0t0e20m@4ax.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <2aikh.152992$b%6.23128@fe10.news.easynews.com> <Rctkh.2715$sR.286@newssvr29.news.prodigy.net>`

```
On Wed, 27 Dec 2006 11:57:37 GMT, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>> Did you use the MERGE statement or write your own "merge logic"?  Other 
>> than that, I can't really imagine that "test" being very useful.
…[4 more quoted lines elided]…
>COBOL expertise to that candidate.....

I've written lots of match and merge programs where the MERGE verb
wasn't appropriate.    I expect anybody I hire to be able to do the
same.    If I was taking this interview, I would mention that
possibility and ask for more information.   Getting more information
is what good programmers do.
```

#### ↳ Re: COBOL interview tests

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2006-12-26T20:42:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com>`

```
I've interviewed Cobol programmers back when I was in a Cobol shop.

We used to give tests like this ("write a program that <insert simple task 
here> ....").  What the programs had to do was really irrelevent.  It didn't 
even matter to us whether or not the program actually worked - it just had 
to come close.  We only gave a few hours to get it done.  (On the other 
hand, we weren't hiring people with 20+ years experience either at what we 
were paying.)

We gave a sheet with instructions on where to put the source and how to 
compile and run it.  The tests were done under Windows, so we assumed 
everyone was familiar with Notepad and the basics of navigating Windows. 
(Our actual development environment was on Unix, but Windows was the common 
denominator.)

In our case, the tests were really just to see if the person knew more than 
just how to do well in an interview (or maybe didn't do so well in 
interviews, but were proficient programmers).  Could they actually write a 
Cobol program?  You'd be suprised at how many people we interviewed for a 
Cobol programming position who didn't know Cobol other than from a few 
classes, couldn't write a program, and gave up without anything.  Could they 
follow instructions to compile and run the program?  Could they identify 
compile errors and correct them?  What would they do to test their program?

No one could really tell you what we were looking for - the programming task 
we had people do was just thought up at the time we were hiring and there 
was no set "answer" that we were looking for.

As for your situation, where you said you never wrote a program from 
scratch - I know what you mean.  We usually started with a template, rarely 
a blank slate.  But when we had people do a test like this, we always 
allowed them to use the help file that contained the Cobol manual.  I 
figured, heck, I had been programming in Cobol for 20+ years and I still 
occasionally used the manual, so there's no reason this person shouldn't be 
able to also.  It was a programming skills test, not a memory test.

"krewser" <wkrusinski@yahoo.com> wrote in message 
news:1167022974.195881.14990@i12g2000cwa.googlegroups.com...
>I interviewed with an organization 18 months ago.  During the interview
> I was asked to take a COBOL programming test.  I've been programming
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL interview tests

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-12-26T20:08:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a940d$4591d576$454920f8$31278@KNOLOGY.NET>`
- **In-Reply-To:** `<pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`

```
JJ wrote:
> As for your situation, where you said you never wrote a program from 
> scratch - I know what you mean.  We usually started with a template, rarely 
…[4 more quoted lines elided]…
> able to also.  It was a programming skills test, not a memory test.

I was curious about this.  Are you not allowed to use a manual?  I've 
been at this nearly a decade now, but I still rely on my manual, 
probably on a weekly basis.  From the "how do you" questions, to the 
"what does this do" stuff, the manual is an invaluable tool.

With the one question that's been mentioned - a merge.  I've *never* 
done a merge.  Never.  Never studied it in class, never written it 
myself, never encountered it during maintenance.  I'd need the manual 
for that question.  :)

Without a manual, I'd take a stab at the syntax...

MERGE file-1  file-2
   GIVING file-3

Ah - but I have a COBOL manual on my computer.  Let's see...  Looks like 
I'm missing a "USING" clause...

MERGE file-1  USING file-2  GIVING file-3

How about that - I learned something!  :)
```

###### ↳ ↳ ↳ Re: COBOL interview tests

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-26T21:51:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12p3rdva2dvi2f0@news.supernews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET>`

```
LX-i wrote:

>
> Without a manual, I'd take a stab at the syntax...
…[9 more quoted lines elided]…
> How about that - I learned something!  :)

Yeah, but at what cost. You had to make room for something your experience 
says will probably never be used.

Say goodbye to the fifth grade.
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-12-27T11:00:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67526$4592a69b$454920f8$26583@KNOLOGY.NET>`
- **In-Reply-To:** `<12p3rdva2dvi2f0@news.supernews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET> <12p3rdva2dvi2f0@news.supernews.com>`

```
HeyBub wrote:
> LX-i wrote:
> 
…[5 more quoted lines elided]…
> Say goodbye to the fifth grade. 

Not necessarily.  Granted, today I could probably write a MERGE without 
looking at a manual - but three weeks from now, I'd probably forget the 
syntax and have to look it up again.  Rather than try to memorize every 
possible option, I instead like to dedicate a portion of my memory store 
to knowing *where* things are documented.  That keeps me from having to 
memorize the manuals, leaving room for lots of 5th grade memories - even 
the one about the girl that wouldn't go out with me.

(On second thought, maybe I *should* study this MERGE thing a little bit 
more...)
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-27T10:19:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ja5p217depjjd1ch0h76mlb5069n05pgf@4ax.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET> <12p3rdva2dvi2f0@news.supernews.com> <67526$4592a69b$454920f8$26583@KNOLOGY.NET>`

```
On Wed, 27 Dec 2006 11:00:28 -0600, LX-i <lxi0007@netscape.net> wrote:

>Not necessarily.  Granted, today I could probably write a MERGE without 
>looking at a manual - but three weeks from now, I'd probably forget the 
…[4 more quoted lines elided]…
>the one about the girl that wouldn't go out with me.

I'm like that with most computer languages.   And most languages I am
familiar with.   But CoBOL has become native to me - I could leave it
for a decade and come back without having to re-learn old stuff. Sure,
there are occasions when I need to pull out my English language
dictionary with my native English - but CoBOL isn't a big language.
(Now I would have to pull out the manual to do OO CoBOL - not my
manual though which doesn't have any of that).
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-12-27T11:53:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d8fb$4592b31c$454920f8$30927@KNOLOGY.NET>`
- **In-Reply-To:** `<9ja5p217depjjd1ch0h76mlb5069n05pgf@4ax.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET> <12p3rdva2dvi2f0@news.supernews.com> <67526$4592a69b$454920f8$26583@KNOLOGY.NET> <9ja5p217depjjd1ch0h76mlb5069n05pgf@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 27 Dec 2006 11:00:28 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[14 more quoted lines elided]…
> manual though which doesn't have any of that).

That last part bring up another conflict I have - I could probably put 
forth the effort to learn OO COBOL, and make some small application with 
it.  I'm sure I would learn a lot along the way.  But would it benefit 
me past the "gee-whiz" of being able to say that I did it?  (Granted, 
the "gee-whiz" pull is pretty strong - but I've got some other stuff to 
do with already-deployed applications too.)
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-27T11:46:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1if5p2p6bduca1qpvv2jf6878erlmn6lpp@4ax.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET> <12p3rdva2dvi2f0@news.supernews.com> <67526$4592a69b$454920f8$26583@KNOLOGY.NET> <9ja5p217depjjd1ch0h76mlb5069n05pgf@4ax.com> <7d8fb$4592b31c$454920f8$30927@KNOLOGY.NET>`

```
On Wed, 27 Dec 2006 11:53:49 -0600, LX-i <lxi0007@netscape.net> wrote:

>That last part bring up another conflict I have - I could probably put 
>forth the effort to learn OO COBOL, and make some small application with 
…[3 more quoted lines elided]…
>do with already-deployed applications too.)

In my environment OO is limited to the user interface side.   If all
I'm doing is accessing the database (or screen scraping), and
providing XML for the web services - Java works quite nicely - but not
particularly because Java is OO.

I'm seeing a separation of business rules and user interfaces which is
getting wider.   Moving the business rules more into the database
realm is what is finally making CoBOL less pervasive.
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 7)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-27T18:10:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12p62s7qv2a1g85@news.supernews.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET> <12p3rdva2dvi2f0@news.supernews.com> <67526$4592a69b$454920f8$26583@KNOLOGY.NET> <9ja5p217depjjd1ch0h76mlb5069n05pgf@4ax.com> <7d8fb$4592b31c$454920f8$30927@KNOLOGY.NET>`

```
LX-i wrote:
> That last part bring up another conflict I have - I could probably put
> forth the effort to learn OO COBOL, and make some small application
…[3 more quoted lines elided]…
> other stuff to do with already-deployed applications too.)

You're flirting with the 4th grade not even being a memory...
```

###### ↳ ↳ ↳ Re: COBOL interview tests

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-27T23:44:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vf14cF1bt24kU1@mid.individual.net>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <a940d$4591d576$454920f8$31278@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:a940d$4591d576$454920f8$31278@KNOLOGY.NET...
> Without a manual, I'd take a stab at the syntax...
>
…[8 more quoted lines elided]…
> How about that - I learned something!  :)

Yeah, but a REAL programmer would write a 3 way split... :-)

Pete.
```

##### ↳ ↳ Re: COBOL interview tests

- **From:** "krewser" <wkrusinski@yahoo.com>
- **Date:** 2006-12-27T02:42:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167216178.220918.86610@n51g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`

```
This test was a little different.  It had four or five questions.  The
first was writing the merge program.  The second one contained some
code that needed to be desk checked to find an error.  I don't recall
the other questions.

The interviewer sat me at an empty cubicle with the test, paper and a
pencil.  No computer or manuals were involved.

JJ wrote:
> I've interviewed Cobol programmers back when I was in a Cobol shop.
>
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL interview tests

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-12-27T03:08:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167217714.110186.220900@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1167216178.220918.86610@n51g2000cwc.googlegroups.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <1167216178.220918.86610@n51g2000cwc.googlegroups.com>`

```

How would you get on if you said they should use the system sort
utility instead?
```

###### ↳ ↳ ↳ Re: COBOL interview tests

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-27T11:57:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rctkh.2716$sR.799@newssvr29.news.prodigy.net>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com> <1167216178.220918.86610@n51g2000cwc.googlegroups.com> <1167217714.110186.220900@i12g2000cwa.googlegroups.com>`

```
"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1167217714.110186.220900@i12g2000cwa.googlegroups.com...
> How would you get on if you said they should use the system sort
> utility instead?

I would point out that in the professional software development arena, 
clients/users are responsible for defining the what" but the developer is 
responsible for the "how."

If it's some kind of anal PHB I might go so far as to point out that the 
COBOL MERGE verb **IS** using the system sort utility anyway.

Being an opportunist, I might even suggest I provide a (paid) training 
session in 'merge techniques' for the rest of the staff, showing how there 
are at least two ways to skin this cat.

But regardless of path I think it likely that if really pressed on this 
point I'd probably end up making some smartasss comment vis-a-vis paying for 
assembly-line labor vs. paying for Real World Results and as a result be 
excused from further consideration.

Then again, I don't really need the work.

MCM
```

##### ↳ ↳ Re: COBOL interview tests

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-27T08:34:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uh45p299kncpob88l1jueql50ht55v1jh5@4ax.com>`
- **References:** `<1167022974.195881.14990@i12g2000cwa.googlegroups.com> <pcmdnewY1J36UgzYnZ2dnUVZ_qmpnZ2d@comcast.com>`

```
On Tue, 26 Dec 2006 20:42:00 -0500, "JJ" <jj@nospam.com> wrote:

>As for your situation, where you said you never wrote a program from 
>scratch - I know what you mean.  We usually started with a template, rarely 
…[4 more quoted lines elided]…
>able to also.  It was a programming skills test, not a memory test.

Back when the SELECT / ASSIGN statement syntax was more meaningful - I
didn't really know the syntax, I just knew which programs to clone
them from.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
