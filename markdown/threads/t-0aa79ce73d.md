[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol code assessment

_37 messages · 15 participants · 2006-01 → 2006-02_

---

### cobol code assessment

- **From:** "apple.time@yahoo.com" <apple.time@yahoo.com>
- **Date:** 2006-01-27T18:52:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```
My boss just asked me to do a Cobol code assessment for our company.
He has given me no guidelines on what is expected of me.  I have worked
with cobol for 20 years, so I know it quite well.  I am not to use any
'tools' for creating metrics on the code.  I guess the company is
trying to decide if our programs are 'good enough', or whether we
should be rewriting them in some newer technology.  We have both
on-line systems for data entry and batch processing.  They want me to
have an analysis for them in a week.  HELP!  What do I do?  fyi... I
plan to talk to everyone on the team.... from programmers, system
analysts, data base administrators, help desk, users, etc.  But, they
want me to examine the CODE itself as well.  This is the piece that I
am unsure of.  If you have any web addresses of how to do this, it
would be MOST appreciated.  Also, if any of you have done this, if you
could show me your final analysis (without the company identifying
information, of course!)  THANKS
```

#### ↳ Re: cobol code assessment

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-01-28T00:04:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0ccb$43dafb6f$453db2dd$12500@FUSE.NET>`
- **In-Reply-To:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```
apple.time@yahoo.com wrote:
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[13 more quoted lines elided]…
> 
It might help if we knew what platform, operating system, etc. your 
application are using...?  Do you really have no idea what the 
objectives are for this study?
```

#### ↳ Re: cobol code assessment

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-28T07:17:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drf5qi$e6p$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```
In article <1138416722.370897.6450@f14g2000cwb.googlegroups.com>,
apple.time@yahoo.com <apple.time@yahoo.com> wrote:
>My boss just asked me to do a Cobol code assessment for our company.
>He has given me no guidelines on what is expected of me.

Sounds like there'll be nothing to judge the results of your efforts by, 
then.

>I have worked
>with cobol for 20 years, so I know it quite well.  I am not to use any
…[4 more quoted lines elided]…
>have an analysis for them in a week.  HELP!  What do I do?

Exactly what has been asked of you... assess the code.  Does it do what is 
required of it?  If so, then say so... if no, then don't.

>fyi... I
>plan to talk to everyone on the team.... from programmers, system
>analysts, data base administrators, help desk, users, etc.  But, they
>want me to examine the CODE itself as well.  This is the piece that I
>am unsure of.

This is the easiest part.  In absence of a different task-requirement it 
may be best to use a metric that's been valid for the past 20 years and 
more:

IF PROGRAM-RUNS
    PERFORM NEXT-ASSIGNMENT
ELSE
    PERFORM CODE-LIKE-HELL
     UNTIL DAMNED-THING-WORKS.

See how easy?  As mentioned above, determine if the code does what is 
required of it... if you want to get fancy, ask 'how does the code 
*prevent* the performance of something that is required of it?'.

Piece o' cake... there's no need to ask anyone else to do your job for you 
at all.

DD
```

#### ↳ Re: cobol code assessment

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2006-01-28T08:07:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43db262d$0$27884$ed9e5944@text-readers.news.pipex.net>`
- **In-Reply-To:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```
Top post:

You might like to look at the frequency/severity of faults it's exhibited.
Also, the ease or otherwise of diagnosing faults, including how it 
handles (run-time, obviously) errors, how informative/accurate/complete 
the error-reports are, do they get logged automatically (by the code).

otoh, perhaps you might like to get involved in style warfare?
Are just sections - correctly sized! - used; are there any "go to's"; 
are the programs overloaded with functionality; is there decent comment 
in the source?
Can you actually understand the code without tearing out your hair?
Are there any non-supported techniques/features in use (non-supported by 
the compiler supplier)?
(Or even by operating system supplier).
Does the code depend on specific hardware being used (e.g. terminal 
screens)?

Or is the code an absolute peach & everyone loves & respects it?

Is your compiler within a maintenance agreement?

Best of luck

Michael
apple.time@yahoo.com wrote:
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: cobol code assessment

- **From:** "apple.time@yahoo.com" <apple.time@yahoo.com>
- **Date:** 2006-01-28T09:12:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138468379.257965.162950@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<43db262d$0$27884$ed9e5944@text-readers.news.pipex.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <43db262d$0$27884$ed9e5944@text-readers.news.pipex.net>`

```
Michael, THANK YOU so much for your response!  It is most helpful!
Can you please provide examples of non-supported techniques/features so
I know what to look for?  THANKS!
```

###### ↳ ↳ ↳ Re: cobol code assessment

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2006-01-28T19:15:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43dbc2c8$0$27881$ed9e5944@text-readers.news.pipex.net>`
- **In-Reply-To:** `<1138468379.257965.162950@g47g2000cwa.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <43db262d$0$27884$ed9e5944@text-readers.news.pipex.net> <1138468379.257965.162950@g47g2000cwa.googlegroups.com>`

```
apple.time@yahoo.com wrote:
> Michael, THANK YOU so much for your response!  It is most helpful!
> Can you please provide examples of non-supported techniques/features so
> I know what to look for?  THANKS!
>
>   
Thanks for the invitation to expound, however, (how shall I phrase this? 
hmm ..)
"Having been offered directions, it's now up to you yourself to begin 
the walking!"

(I wonder what Docdwarf would say?)

Good luck.

Michael
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-28T23:47:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drgvq9$711$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <43db262d$0$27884$ed9e5944@text-readers.news.pipex.net> <1138468379.257965.162950@g47g2000cwa.googlegroups.com> <43dbc2c8$0$27881$ed9e5944@text-readers.news.pipex.net>`

```
In article <43dbc2c8$0$27881$ed9e5944@text-readers.news.pipex.net>,
Michael Russell  <Michael.Russell@msn.com> wrote:
>apple.time@yahoo.com wrote:
>> Michael, THANK YOU so much for your response!  It is most helpful!
…[9 more quoted lines elided]…
>(I wonder what Docdwarf would say?)

Depends on who's listening... since this is a Family Forum I'll limit it 
to 'please do your own job or hire someone who knows how to'.

DD
```

#### ↳ Re: cobol code assessment

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-01-28T04:01:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138449707.309435.254550@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```

apple.time@yahoo.com wrote:
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[12 more quoted lines elided]…
> information, of course!)  THANKS

As well as the other suggestions posted, your company's inventory of
COBOL programs probably contains several suites of COBOL programs for
separate though linked functions such as payroll, order processing,
inventory, purchasing, etc, written at different times by different
groups/teams.  Some will be better designed and written than others.
You probably won't have time to examine all the programs so you could
take samples from each suite, based perhaps on the advice of the people
usually working on them.  Some suites might be better suited to
replacement by other technologies than others (or just being redone
again in COBOL to a better plan), so you must be careful not to tar
everything with the same brush.

You might produce a plan of how you intend to do the analysis for your
boss to review before you proceed, as he/she might have useful
suggestions for the plan details and will then be less able to say that
it didn't meet the expectations.

With regard to assessing the styles of program coding and irrespective
of your installation's standards and personal preferences, you must try
to assess whether the code is easily readable (with or without
comments), easily maintainablem, reasonably efficient and does what it
is supposed to do.

Your intention to include users is commendable and should include both
trainees and experienced users, an assessment of how long it takes to
learn how to use the system could be helpful as would an assessment of
the user documentation.

The presence or absence of audit trails should be considered.

Good luck, Robert
```

##### ↳ ↳ Re: cobol code assessment

- **From:** "apple.time@yahoo.com" <apple.time@yahoo.com>
- **Date:** 2006-01-28T09:15:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138468550.572994.174240@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1138449707.309435.254550@f14g2000cwb.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138449707.309435.254550@f14g2000cwb.googlegroups.com>`

```
Robert, thanks for your input!  I really do appreciate your advise!
Can you please expound on what audit trails I should look for?  We have
a great 'change management' system that logs every change in the
system.  Other than that, are there other audit trails to look at?
THANKS!
```

###### ↳ ↳ ↳ Re: cobol code assessment

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-01-28T11:25:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138476307.718488.315960@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1138468550.572994.174240@z14g2000cwz.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138449707.309435.254550@f14g2000cwb.googlegroups.com> <1138468550.572994.174240@z14g2000cwz.googlegroups.com>`

```

apple.time@yahoo.com wrote:
> Robert, thanks for your input!  I really do appreciate your advise!
> Can you please expound on what audit trails I should look for?  We have
> a great 'change management' system that logs every change in the
> system.  Other than that, are there other audit trails to look at?
> THANKS!

Audit trails can be of a variety of types and I don't claim to know
them all or which are best, however, I shall have a go at a brief
simplistic overview.

Online programs should ideally log all changes to files and database
tables, especially those with financial implications, this doesn't
necessarily mean one record per change per file, but  might take the
form of a pseudo transaction file from which the relevant changes can
be identified and conceivably reapplied or backed out in the event of
system errors or crashes.  Such changes should include the identity of
the terminal and user making them, plus the timestamp.  CICS provides
journalling systems with which I am not familiar, but you may consider
looking at or for them if applicable.

Batch systems should ideally retain the transaction files, again so
they can also be reapplied or backed out.  Batch systems should also
contain backup master files (or database backups) which can be related
to the relevant transaction files.  I am now really getting into the
realm of JCL validation, which isn't quite what you were asking, but it
is a part of the operational system.  If the transaction files are
generated online by manual input, then again terminal and user
identities plus timestamps/dates are highly desirable, if they come
from external sources, e.g. BACS tapes then their source should be
identifiable.

Databases do tend to have some form of change log, but you would have
to investigate how it is used, whether it is turned on, who can
authorise it being turned off, how it is backed up and retained, and
how easy it is to extract the desired information.

Your company presumably has external auditors who would be able to tell
you what they would expect to see and may be able to offer advice.

Robert
```

#### ↳ Re: cobol code assessment

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-01-28T09:11:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138468312.922876.159130@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```

apple.time@yahoo.com wrote:
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[12 more quoted lines elided]…
> information, of course!)  THANKS

Just in case others have missed it:

Perhaps you could analyse the number of lines, the number of programs
and the systems which use those programs. Differentiate between batch
and online code. If you had the time (and you haven't) you could have
done some kind of function point analysis which would give you a
measure of size and complexity of any one system.

Others have commented about ease of maintenance but how about asking
just how much work is there outstanding which the users would like to
have done. A difficult-to-maintain system might have no work
outstanding and may be 100% reliable whereas an easy-to-maintain system
might be bug-ridden with tons of outstanding work. The latter might be
a good case for re-writing or replacing but the former would be a good
candidate for leaving alone.

I suspect that your boss wants to know how much Cobol code you have, in
which systems it resides, how reliable it is and what kind of workload
is outstanding on it. He probably wants to replace it with a
language-du-jour or flavour of the month OO system.


Finally, unless your boss gives you a proper scope statement (ie
details his requirements and criteria for success) then you are on a
losing sticky wicket.
```

##### ↳ ↳ Re: cobol code assessment

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-01-28T21:17:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11toctdlbds81ec@news.supernews.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com>`

```
Alistair wrote:
>
> Just in case others have missed it:
…[23 more quoted lines elided]…
> losing sticky wicket.

Be sure to include the "skill inventory" of the staff. For example:

Average experience
Senior programmers - 12.
  COBOL: 17.2 years
  Assembly: 3.3 years
  JAVA: 0.4 years
  RPG: 0.3 years
  FORTRAN: 0.1 years
  Other (all): 0.3 years

Junior programmers - 4.
  COBOL: 2.6 years
  Assembly: 0.2 years
  JAVA: 0.6 years

etc.

With a view toward emphasizing the human investment in the existing 
methodology.
```

###### ↳ ↳ ↳ Re: cobol code assessment

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2006-01-28T22:44:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11tolhiaurgtc36@corp.supernews.com>`
- **In-Reply-To:** `<11toctdlbds81ec@news.supernews.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com>`

```
HeyBub wrote:
[snip]

> Be sure to include the "skill inventory" of the staff. For example:
> 
…[17 more quoted lines elided]…
> methodology.

Slightly OT, but is average experience necessarily a meaningful metric? 
  Are ten people who can claim a year each of COBOL experience really 
equivalent to one person who can claim ten years, or two people who can 
claim five each?  Is ten years' experience worth twice as much as five 
years, or is there a point of diminishing returns?

This question calls for some handwaving:  I would sum a*log(b*e + 1) 
over the whole team, where 'e' is years of experience and 'a' and 'b' 
are constants of your choice, and use the result as a measure of 
available skill.  'a' and 'b' could be different for different skills; 
for years spent writing spaghetti COBOL with ALTER statements or FORTRAN 
with arithmetic IFs and Hollerith editing descriptors, 'b' could be very 
small or even zero while 'a' could be zero or even negative.

(That's what happens when I drink coffee.)

Louis
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-29T14:37:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drik06$epe$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com>`

```
In article <11tolhiaurgtc36@corp.supernews.com>,
Louis Krupp  <lkrupp@pssw.nospam.com.invalid> wrote:
>HeyBub wrote:
>[snip]
…[5 more quoted lines elided]…
>>   COBOL: 17.2 years

[snip]

>> etc.
>> 
…[3 more quoted lines elided]…
>Slightly OT, but is average experience necessarily a meaningful metric? 

Meaning is the result of interpretation, Mr Krup... or so Wittgenstein 
might have it.

>  Are ten people who can claim a year each of COBOL experience really 
>equivalent to one person who can claim ten years, or two people who can 
>claim five each?  Is ten years' experience worth twice as much as five 
>years, or is there a point of diminishing returns?

There is, according to the calendar, no difference whatsoever between 
someone who has ten years' experience and someone who has one year ten 
times over... but there seem to be things in just about any field that 
many appear to learn only over time and with repeated exposure; I know of 
no discipline that is obtained perfectly and instantaneously.

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-01-30T10:42:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<444r6iFda84U1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <drik06$epe$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:drik06$epe$1@reader2.panix.com...
> In article <11tolhiaurgtc36@corp.supernews.com>,
> Louis Krupp  <lkrupp@pssw.nospam.com.invalid> wrote:
…[32 more quoted lines elided]…
> DD
Puttng on a hat? :-)

Pete.
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-30T01:57:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drjrqg$es0$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <11tolhiaurgtc36@corp.supernews.com> <drik06$epe$1@reader2.panix.com> <444r6iFda84U1@individual.net>`

```
In article <444r6iFda84U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:drik06$epe$1@reader2.panix.com...

[snip]

>> There is, according to the calendar, no difference whatsoever between
>> someone who has ten years' experience and someone who has one year ten
…[5 more quoted lines elided]…
>Puttng on a hat? :-)

E'en something so simple, Mr Dashwood... for example, from what I've seen 
it takes years of work to be able to don and wear a straw fedora without 
looking like... well, like a kid trying to don and wear a straw fedora.

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-01-29T07:27:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138548428.909665.291230@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<11tolhiaurgtc36@corp.supernews.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com>`

```

Louis Krupp wrote:
> HeyBub wrote:
> [snip]
…[13 more quoted lines elided]…
> Louis

Back in Doc Dwarf's Golden Days of Yore I read an article in a
computing journal which concluded that a trainee programmer would
improve their productivity up to a maximum level at two years.
Thereafter, their productivity declined somewhat but would not reach
the two year maxima.

So five people with two years experience each would definitely be
better than one person with ten years experience. Of course, DD would
posit that, like a good wine, he improves with age.
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-01-30T10:47:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<444rg9Fd28oU1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1138548428.909665.291230@g49g2000cwa.googlegroups.com...
>
> Louis Krupp wrote:
…[26 more quoted lines elided]…
>
Not ALL good wines improve with age (though I have no doubt the Doc has done 
so). But I wouldn't take the findings of a Computer Journal form the "Good 
old daze" as Gospel, either :-).  In the "Good old daze" we thought it was 
OK to solve problems by making little holes in cardboard...  :-)

As a manager, I'd rather have 1 person with 10 years than 5 with 2 years, 
but only because it would be cheaper :-). If someone else is paying for it, 
I'll take the 5 people gladly...:-)

Pete.
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-30T02:01:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drjs11$nto$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com>`

```
In article <1138548428.909665.291230@g49g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>So five people with two years experience each would definitely be
>better than one person with ten years experience.

Perhaps, Mr Maclean, in the same way that nine women can gestate a zygote 
to full term in a single month?

>Of course, DD would
>posit that, like a good wine, he improves with age.

Hmmmmm... leaving aside matters of taste I can say that with age I do not 
make the same old mistakes... I manage to make newer mistakes that seem to 
be more difficult to find.

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 6)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-01-30T08:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com> <drjs11$nto$1@reader2.panix.com>`

```
On Mon, 30 Jan 2006 02:01:05 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <1138548428.909665.291230@g49g2000cwa.googlegroups.com>,
>Alistair <alistair@ld50macca.demon.co.uk> wrote:
…[14 more quoted lines elided]…
>be more difficult to find.
hummmm ..... could we also argue that a common age memory overload
problem is taking its toll and making them look like they are harder
to find now... :>)



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-30T10:14:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drkouu$ha3$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com> <drjs11$nto$1@reader2.panix.com> <sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com>`

```
In article <sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com>,
Frederico Fonseca  <real-email-in-msg-spam@email.com> wrote:
>On Mon, 30 Jan 2006 02:01:05 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[19 more quoted lines elided]…
>to find now... :>)

That argument might be made, Mr Fonesca... and tested by having other 
programmers who are younger (and, perhaps, less prone towards 'a common 
age memory overload problem') search for the errors.

It takes them longer, as well... but perhaps this memory-difficulty is 
contagious.

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 8)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-01-31T14:01:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138744909.698008.44930@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<drkouu$ha3$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com> <drjs11$nto$1@reader2.panix.com> <sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com> <drkouu$ha3$1@reader2.panix.com>`

```

docdwarf@panix.com wrote:
> In article <sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com>,
> Frederico Fonseca  <real-email-in-msg-spam@email.com> wrote:
…[30 more quoted lines elided]…
> DD

I find that the youngsters are all too ready to give up and pass the
problem on to others just when I'm getting to grips with it.
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-31T22:31:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<droofi$pot$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <sejrt15e8kfv1gs0jfvj9rqh56lndjhhmb@4ax.com> <drkouu$ha3$1@reader2.panix.com> <1138744909.698008.44930@f14g2000cwb.googlegroups.com>`

```
In article <1138744909.698008.44930@f14g2000cwb.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>I find that the youngsters are all too ready to give up and pass the
>problem on to others just when I'm getting to grips with it.

... an' don't get me started on what they're callin' 'music' nowadays, 
neither... buncha durned noise, if ya ask me... an' what's with all this 
mumblin', can't those kids speak up so's a body can hear?  Why, I remember 
when *I* was a lad we were taught to speak up... an' show respect, too... 
zzzzzz....

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 5)_

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2006-01-29T21:22:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.01.30.04.22.50.957770@starband.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com>`

```
On Sun, 29 Jan 2006 07:27:08 -0800, Alistair wrote:
> 
> So five people with two years experience each would definitely be
> better than one person with ten years experience. Of course, DD would
> posit that, like a good wine, he improves with age.


Since there is only so much work that an individual can do, I would always
take the 5 people with two years over one with ten WHEN doing development
work.

That said, Given that that work will undoubtedly create more work down the
road with bugs and maintenance coding, I would much rather the experience
of ten years of analysis and trouble shooting than 5x2 years of raw coding.  

In other word, as with all things, it depends.....depends on the job, what
sort of analysis required, what sort of maintenance anticipated. 
Experience and product knowledge beats the crap out of raw  heads to do
work.

Ideally, then I want one person with ten years, one with 5 and any number
of a team with 2 or less.

Chris
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 6)_

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2006-01-29T21:40:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.01.30.04.40.18.575020@starband.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com> <pan.2006.01.30.04.22.50.957770@starband.net>`

```
On Sun, 29 Jan 2006 21:22:54 -0700, Christopher Pomasl wrote:

> On Sun, 29 Jan 2006 07:27:08 -0800, Alistair wrote:
>> 
…[4 more quoted lines elided]…
> Chris

BTW, It also depends on the project size, but I have a product with about
600 COBOL programs +30 ASM and Ideally it should have the team described
above to upgrade against the changing environment(s) under which it must
run.  I am the sole developer and maintainer.

Product requires OS390, Z/os, CICS, TSO, SPF, IMS, DB2, +other MVS
utilities and subsystems.  And must support all current versions.

I could do a lot more with a larger team, but I get by with just myself.

Chris
22 years COBOL
20 years 360 assembler
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-02-01T02:42:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4497r1F11i4iU1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <1138548428.909665.291230@g49g2000cwa.googlegroups.com> <pan.2006.01.30.04.22.50.957770@starband.net> <pan.2006.01.30.04.40.18.575020@starband.net>`

```

"Christopher Pomasl" <pomasl-NOSpam@starband.net> wrote in message 
news:pan.2006.01.30.04.40.18.575020@starband.net...
> On Sun, 29 Jan 2006 21:22:54 -0700, Christopher Pomasl wrote:
>
…[16 more quoted lines elided]…
> I could do a lot more with a larger team, but I get by with just myself.

Your comment reminded me of a man I once contracted for. He got very rich 
from the efforts of our team but was loath to share any of this bounty. I 
refused to do further work for him when the job finished, and we parted, not 
amicably, but civilly.

Some years later I bumped into him in a bar in London and his scathing 
greeting (in a loud voice, for the benefit of the people I was with) was: 
"Oh, Hello, Peter... still a one man band are we?"

Without hesitation I replied: "Well, actually, X, I find it impossible to 
get by with any less..."  There was general laughter all round and he beat a 
hasty retreat. I've never seen him since and never mourned the loss.

Pete.
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-01-29T14:52:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11tqap5m38e274@news.supernews.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com>`

```
Louis Krupp wrote:

>
> Slightly OT, but is average experience necessarily a meaningful
>  metric?

It's considerably more meaninful than not mentioning the skill sets at all.

> Are ten people who can claim a year each of COBOL experience
> really equivalent to one person who can claim ten years, or two
…[10 more quoted lines elided]…
> negative.

"Average" is probably understandable by the factotum who assigned this 
absurd exercise. I'll wager "Median" is beyond his grasp and regression 
analysis (or, for that matter, your in-depth study) is an example of the 
perfect being the enemy of the good.

Hell, I bet he couldn't even grasp
   Ln(e) = Sum(1/n**2) + (sin**2 (theta) + cos**2 (theta))
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 5)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2006-01-29T18:22:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11tqqh96md92r8f@corp.supernews.com>`
- **In-Reply-To:** `<11tqap5m38e274@news.supernews.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <1138468312.922876.159130@g47g2000cwa.googlegroups.com> <11toctdlbds81ec@news.supernews.com> <11tolhiaurgtc36@corp.supernews.com> <11tqap5m38e274@news.supernews.com>`

```
HeyBub wrote:
[snip]

> Hell, I bet he couldn't even grasp
>    Ln(e) = Sum(1/n**2) + (sin**2 (theta) + cos**2 (theta))

It's just as well.  I can't remember what that series converges to (it's 
been a *long* time), but ln(e) is 1, and (sin(theta)**2 + cos(theta)**2) 
is 1, so unless I'm mistaken, you probably want to leave the series out 
of the equation entirely.

(I've had three bosses who had PhDs in physics.  One of them was ... 
interesting, but all of them were better than I was at math.)

Louis
```

#### ↳ Re: cobol code assessment

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-01-30T10:35:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<444qp3Fcv74U1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```

<apple.time@yahoo.com> wrote in message 
news:1138416722.370897.6450@f14g2000cwb.googlegroups.com...
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[13 more quoted lines elided]…
>
I browsed through the thread and you have received some excellent responses 
and advice.

However, I have the following observations:

1. Managers who can't communicate clear requirements need to be "trained" by 
the people who work for them. Instead of posting to a forum saying you have 
no idea what is wanted and requesting help, I would suggest sitting down 
with your boss and asking him to clarify what exactly he wants and what his 
goals are. Tell him you need some direction. (It is ostensibly his job to 
give it to you...). Tell HIM you have no idea what is wanted or how to go 
about delivering what he needs. Get HIM to think about what he actually 
wants, so that neither your time nor his is wasted.
2. What kind of manager asks you to do a job, then says you can't use tools? 
:-) Managers who set their staff up to fail are best avoided...
3. Find out exactly what HE means by "assessment". There are many possible 
assessments you could make of the code and some very useful ones have been 
pointed out right here. But which of them is what he requires?
4. Managers have a right to manage, but staff have a right not to accept 
tasks that are not properly defined or simply pointless. Tell him you don't 
feel able to provide what he wants or needs without further clarification. 
In order to provide something of value, you need to understand what  aspects 
of the code need to be assessed, and how the assessment will be used.

Using metrics is a very good way to avoid bias and opinion affecting the 
outcome. Why would he NOT want you to do this?

It is easy to speculate on why this assessment is being made, but it would 
be a lot simpler to just ask him.

If I were you, I wouldn't undertake this without a much clearer picture of 
what you are supposed to be assessing.

Far too often, people just do what they are told (or attempt to...) and this 
doesn't help bad managers get to be better ones.

Pete.
```

##### ↳ ↳ Re: cobol code assessment

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2006-01-29T15:35:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11tqgpprq6nmb29@corp.supernews.com>`
- **In-Reply-To:** `<444qp3Fcv74U1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <444qp3Fcv74U1@individual.net>`

```
Pete Dashwood wrote:
> <apple.time@yahoo.com> wrote in message 
> news:1138416722.370897.6450@f14g2000cwb.googlegroups.com...
…[52 more quoted lines elided]…
> doesn't help bad managers get to be better ones.

As an alternative, the OP might want to spend a short time coming up 
with a plausible assessment strategy, see if it meets the boss's 
approval, and then if it doesn't, ask for clarification.  It can't hurt 
to treat the boss as if he were a reasonable person who just needs a 
little guidance on *how* to think about the problem.  If "metrics" is a 
bad word, then talk about counting lines of code or something without 
using the word "metrics."

(Yes, I have reported to people with whom this approach wouldn't have 
worked for various reasons, all of which are reasons to consider finding 
another job.)

Louis
```

##### ↳ ↳ Re: cobol code assessment

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-01-31T17:49:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44aet1F1882lU1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <444qp3Fcv74U1@individual.net>`

```
Pete Dashwood<dashwood@enternet.co.nz> 01/29/06 2:35 PM >>>
>If I were you, I wouldn't undertake this without a much clearer picture of

>what you are supposed to be assessing.
>
>Far too often, people just do what they are told (or attempt to...) and
this 
>doesn't help bad managers get to be better ones.


I have a somewhat relevant "motto".  I never ask a question without first
asking *why* the question is being asked.  Much too often people ask a
specific question that they *think* will solve the issue at hand, but in
fact they're just "asking the wrong question".  I much prefer someone to say
"here is my issue; what can you tell me that will help me solve it / make a
decision."

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: cobol code assessment

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-01T01:13:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drp1vv$s2s$1@reader2.panix.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <444qp3Fcv74U1@individual.net> <44aet1F1882lU1@individual.net>`

```
In article <44aet1F1882lU1@individual.net>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>Pete Dashwood<dashwood@enternet.co.nz> 01/29/06 2:35 PM >>>
>>If I were you, I wouldn't undertake this without a much clearer picture of
…[8 more quoted lines elided]…
>asking *why* the question is being asked.

I agree... and yet disagree.  Rather than 'why' - which can, under the 
wrong circumstances, have an almost adolescent poutiness to it - I will 
try to encourage Rational Discourse by furrowing my brow and saying 'I do 
not understand the reasons for doing this, are you able to explain them to 
me?'... or something like that, the main point to make it a discussion of 
Reason, not of Desire.

Then again... I've been told 'No, I can't... now go do what I mean.'

DD
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-02-01T12:41:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44ch7gF1hj3kU1@individual.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <444qp3Fcv74U1@individual.net> <44aet1F1882lU1@individual.net> <drp1vv$s2s$1@reader2.panix.com>`

```
<docdwarf@panix.com> 01/31/06 6:13 PM >>>
>In article <44aet1F1882lU1@individual.net>,
>Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>>Pete Dashwood<dashwood@enternet.co.nz> 01/29/06 2:35 PM >>>
>>>If I were you, I wouldn't undertake this without a much clearer picture
of
>>
>>>what you are supposed to be assessing.
>>>
>>>Far too often, people just do what they are told (or attempt to...) and
this 
>>>doesn't help bad managers get to be better ones.
>>
…[7 more quoted lines elided]…
>not understand the reasons for doing this, are you able to explain them to

>me?'... or something like that, the main point to make it a discussion of 
>Reason, not of Desire.
>
>Then again... I've been told 'No, I can't... now go do what I mean.'

Well, when I say I ask "why" the question is being asked, I don't actually
phrase it that way.  More like I ask what problem they are trying to solve. 
Based on that I then answer the question they *should* have been asking.

I don't recall anyone ever refusing to tell me what they're really looking
for...
Frank
```

###### ↳ ↳ ↳ Re: cobol code assessment

_(reply depth: 4)_

- **From:** berlutte@hotmail.com
- **Date:** 2006-02-02T10:29:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga94u1duau13m2rbtquesm5fbe1c91urhp@4ax.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <444qp3Fcv74U1@individual.net> <44aet1F1882lU1@individual.net> <drp1vv$s2s$1@reader2.panix.com>`

```
On Wed, 1 Feb 2006 01:13:36 +0000 (UTC), docdwarf@panix.com () wrote:
>
>I agree... and yet disagree.  Rather than 'why' - which can, under the 
…[4 more quoted lines elided]…
>Reason, not of Desire.

Balderdash old turkey!

I seem to remember how *utterly* impervious to reason you were in the
Olden Days when presented with clear evidence on how your thouroughly
rotten market was swindling honest folks.

I can see lotsa pimps (heavily decked in gold jewelery), offerin'
canned eel as pay to codin' fools like you in the near future..

By the by, how does it feel to live in a fascist state, if I may be so
bold to ask? 

So long sucker...

Bwaaaa haha, realllly!


Amanda Lito



http://groups.yahoo.com/group/gata/message/3634

9:06p ET Wednesday, February 1, 2006

Dear Friend of GATA and Gold:

Cheuvreux, the equity brokerage house of Credit
Agricole, the huge French bank, today distributed
a 56-page report that completely endorses in detail
the findings of the Gold Anti-Trust Action Committee
that the price of gold has been surreptitiously
suppressed by Western central banks and that
those banks do not have the gold they claim to
have.

The report, written by Cheuvreux's mining sector
analyst in London, Paul Mylchreest, is titled
"Remonetization of Gold: Start Hoarding." It
repeatedly cites GATA by name and foresees an
"unprecedented" rise in the gold price, possibly
accompanied by a spike to as much as $2,000.
 
The report's executive summary says:

"We are raising our mid-cycle gold price estimate
to USD900/oz from USD750/oz and see the
possibility of a spike to USD2,000, or higher. Covert
selling (via central bank lending) has artificially
depressed the price for a decade.
```

#### ↳ Re: cobol code assessment

- **From:** "Grzegorz Mazur" <news@gregu.ihateunwantedmail.cjb.net>
- **Date:** 2006-02-01T20:32:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drr5v0.3cg.1@hamster.gregu.cjb.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com>`

```
<apple.time@yahoo.com wrote:
> My boss just asked me to do a Cobol code assessment for our company.
> He has given me no guidelines on what is expected of me.  I have worked
…[12 more quoted lines elided]…
> information, of course!)  THANKS

I hope this will help you slightly. I am now working on a project in a major 
bank, programming in Cobol like hell. The whole system we are implementing 
is written in Cobol and since the amount of people involved is great, the 
system was initially written in mid-90's in another country, etc., several 
rules have been established. Another problem is that many (like myself for 
example) are beginners to Cobol / mainframe programming, so extra checks are 
useful.

The set of rules is extensive, but they contain a lot of issues related to 
both SQL code and Cobol code itself. While I cannot remember them all, here 
are some examples of critical rules (i.e. you cannot promote your code above 
development tests if they are not followed):

1). In cursors, ALWAYS state "FOR FETCH ONLY" or "FOR UPDATE OF".
2). NEVER do "SELECT * ...."
3). When doing "SELECT ..... INTO", ALWAYS specify the separate variables, 
not just the copybook.
4). Use "WITH UR" whenever possible. In other cases use "WITH CS". Only in 
critical cases go higher than that (i.e. rule can be relaxed on an 
individual basis).

(they are all SQL-related, since I work with queries a lot and remember them 
better than others)

Some other issues could be:

1). Multiple "MOVE xxx TO yyy" lines should be aligned so that "TO" is in 
one column, for code readability. (this one is pretty weak in terms of 
evaluation of the code, I think)
2). All "IF"s, "PERFORM UNTIL"s, "EVALUATE"s MUST have a proper "END-" bit.
3). You should not use "DISPLAY" in batch programs. (we have a special 
routine to write to sysout from batch programs, thus the rule)

You can easily see the logic here - if there is "ALWAYS", "MUST" or "CANNOT" 
in the rule, this is critical and will cause the code to be non-promotable. 
All other will generate warnings and your code will promote fine, but your 
ego will be impacted ;)

The technical team gathers statistics periodically for all teams involved. 
They also penalize not keeping to naming rules (not specified above, since 
they are rather system/situation specific) etc.

If you want, I can ask whether this information is in any way confidential 
to my company and perhaps I can share the list of errors produced by the 
verification script. While the usability of this information for you might 
be minimal, it still may help.

Good luck :)

Greg.
```

##### ↳ ↳ Re: cobol code assessment

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-01T12:40:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ei32u15t37rvul3mrq5lajqmnjndcp8cii@4ax.com>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <drr5v0.3cg.1@hamster.gregu.cjb.net>`

```
On Wed, 1 Feb 2006 20:32:34 +0100, "Grzegorz Mazur"
<news@gregu.ihateunwantedmail.cjb.net> wrote:

>3). You should not use "DISPLAY" in batch programs. (we have a special 
>routine to write to sysout from batch programs, thus the rule)

This is implementation specific.   Some places have the system set up
so that DISPLAY works as desired.
```

###### ↳ ↳ ↳ Re: cobol code assessment

- **From:** "Grzegorz Mazur" <news@gregu.ihateunwantedmail.cjb.net>
- **Date:** 2006-02-02T20:19:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drtph2.20o.1@hamster.gregu.cjb.net>`
- **References:** `<1138416722.370897.6450@f14g2000cwb.googlegroups.com> <drr5v0.3cg.1@hamster.gregu.cjb.net> <ei32u15t37rvul3mrq5lajqmnjndcp8cii@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 1 Feb 2006 20:32:34 +0100, "Grzegorz Mazur"
> <news@gregu.ihateunwantedmail.cjb.net> wrote:
…[5 more quoted lines elided]…
> so that DISPLAY works as desired.

That's why the special comment is there :)

Actually most of these rules are implementation specific, i.e. on small 
dedicated systems a full table scan could be no problem, but in banking you 
tend to avoid situations, where you scan a table with half a billion rows...

Greg.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
