[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is really wrong with all these Mainframe Systems?

_9 messages · 8 participants · 1998-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### What is really wrong with all these Mainframe Systems?

- **From:** "joseph cotton" <ua-author-15673199@usenetarchives.gap>
- **Date:** 1998-01-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34B05E44.43E8@erols.com>`

```

Well, folks, I went and did it. I told the head honcho at my client
(Fortune 500 - mainframe system) what was wrong with the way which they
run the shop. Here are a few of my comments:

1. Spagetti code. I recomend that all the programs be re-written in
structured COBOL. Apply rigorous naming conventions. All programs
should be structured in a similar manner, thus a programmer needs only
to study one program to know how most of the others work.

2. Testing. They seem to be lax in their testing. They do only a
third of what a good unit test should be, and as for system testing
"we'll test that in production". Needless to say, their programmers are
on 24 hour call with beepers, and get called frequently (in the wee
hours). The two main programmers are always "putting out fires" and
never seem to have time to do it right the first time.

3. Version control. I found out that the program on which I was
working, was also in the process of modification by a collegue. Then I
found out that Someone Else Also (a third person) was also In The
Process. Is it too much to ask, to do the work once, and test it once?
I never really had fond regard for programming reguritation.

Friends: I humbly ask your assistance. I am solicitating your ideas on
the "ideal" working situation. What else can I suggest to the BIG boss
about improving the way we run our shop?

Here is the kicker... I believe that the Y2K problem is only the tip of
the iceberg. There is so much to be desired in some of the shops in
which I have worked. What will be the next "Y2K-like"
mega-trillion-dollar-problem? Because there will be another one, I
predict!

(P.S. A good sign...the guy seemed to listen!)
```

#### ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1998-01-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34B05E44.43E8@erols.com>`
- **References:** `<34B05E44.43E8@erols.com>`

```

Before even a single line of code is touched .... how about a plan, how
about retraining, how about defining the changes to the staff? I'm not
really being flippant, please read on.

I love it when I see the term "Structured Programming" I'll bet you could
find at least as many definitions or understandings of the term as there are
participants in this newsgroup. I don't pretend to have any better idea than
anyone else, of course I have my own. What I am suggesting is that you and
your group decide what will constitute "Structured" in your shop and then
you write it down, include examples, then educate the staff. Include a
process for updating the standard and reintroducing everyone to the changes.
The standards that you arrive at will not be cast in concrete, they will
evolve.

Code Review.

I have been a COBOL head for 10 years and a C/VB/Pascal/REXX programmer for
about half of that time.A Consultant for about 7 years. In shops where the
work I did was in COBOL, not a single walk thru until something went really
wrong and then it was more like a witch hunt than a constructive learning
session.

In shops where the work I did was primarily C or VB, there were frequent
code reviews. At first I was a little standoffish and pissed because someone
was criticizing my work (my creation... ITS ALIVE!!!)... but like everyone
else, I got used to it and now I feel that my code is much tighter, less bug
prone and my ability and style has moved to a whole new level. Well worth it
IMHO....and I no longer carry a beeper.

If you are planning on deploying a structured methodology and strict naming
conventions, be prepared to enforce it, else you will never get it. I have
done this in the past. I introduced some scanning processes to the version
control system. Before I would allow someone to sign code back into the
source / version control tool, I scanned it to make sure it met standards.
This was not fool-proof or 100% accurate, but it did catch the lazy people.
If the code did not meet standards, it was not allowed into the version tool
and an email was sent to the person who attempted the signin and their
manager that detailed WHY it was not allowed into the version control
system. A bit draconian I admit, but it worked. So Verson Control will take
more time and resources than just a copy of PVCS

Re the spaghetti code... I'm sure I'll get publicly beat for this one.... so
go ahead take you best shot, but I have a more pragmatic view of the
situation. If the program works (I mean genuinely, honestly works, not just
hangs togther and barely makes it through the day or night without a lot of
manual intervention, I mean really , really works) I don't see the reason to
rewrite it, at least not right away. So what if its spaghetti instead of
lasagna? There are probably well written, structured, layered, OO, (whatever
the paradigm du jour is..) examples of what DOESN'T work in your shop. IMHO,
the programs causing the most amount of manual intervention, the programs
that do not work, should be re-written first. Free up the resources that
maintain the most troublesome programs.

Testing. We make it part of the programmers job to write a program to test
their program. Sounds like a lot, but it really saves time down the road
when you have to regression test. Of course the test program could have bugs
or not test the program adequately, but it can evolve. What is perfect on
the first pass?

Good luck...

John



Joseph Cotton wrote:

› Well, folks, I went and did it.  I told the head honcho at my client
› (Fortune 500 - mainframe system) what was wrong with the way which they
…[30 more quoted lines elided]…
› (P.S.  A good sign...the guy seemed to listen!)
```

#### ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "ge..." <ua-author-17072640@usenetarchives.gap>
- **Date:** 1998-01-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34B05E44.43E8@erols.com>`
- **References:** `<34B05E44.43E8@erols.com>`

```


› 1.  Spagetti code.  I recomend that all the programs be re-written in
› structured COBOL.  Apply rigorous naming conventions.  All programs
› should be structured in a similar manner, thus a programmer needs only
› to study one program to know how most of the others work.  

IMHO, and not knowing you, I do not want to tell you what you can do
with structured programming.

› 2.  Testing.  They seem to be lax in their testing.  They do only a
› third of what a good unit test should be, and as for system testing
…[3 more quoted lines elided]…
› never seem to have time to do it right the first time.

See reply above for any firm that does not do complete unit, system
and parallel testing in a test environment.

› 3.  Version control.  I found out that the program on which I was
› working, was also in the process of modification by a collegue.  Then I
› found out that Someone Else Also (a third person) was also In The
› Process.  Is it too much to ask, to do the work once, and test it once? 
› I never really had fond regard for programming reguritation.
 
› Who the hell is overseeing this project?
 
› Friends: I humbly ask your assistance.  I am solicitating your ideas on
› the "ideal" working situation.  What else can I suggest to the BIG boss
› about improving the way we run our shop?

The is no "ideal" working situation. Perhaps there could be a
resemblence of one if the the BIG bosses would keep there noses out
of things and let the pros do their job.

› Here is the kicker... I believe that the Y2K problem is only the tip of
› the iceberg.  There is so much to be desired in some of the shops in
› which I have worked.  What will be the next "Y2K-like"
› mega-trillion-dollar-problem?  Because there will be another one, I
› predict!

Amen!

Gene The Geek - Mainframe 26 years
----------------------------------------------------
PHM's - The following statement is for you:
----------------------------------------------------
Consistency is the last refuge of the unimaginative!
----------------------------------------------------
```

##### ↳ ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "joel brighton" <ua-author-17072267@usenetarchives.gap>
- **Date:** 1998-01-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a90afe3cf9-p3@usenetarchives.gap>`
- **References:** `<34B05E44.43E8@erols.com> <gap-a90afe3cf9-p3@usenetarchives.gap>`

```

ge··.@mai··e.com wrote:
› 
›› 1.  Spagetti code.  I recomend that all the programs be re-written in
…[6 more quoted lines elided]…
› 
I'd be interested in hearing what you have to say regarding Structured
programming. You're obviously not impressed but, would you care to
share the specifics of the reason why?


›› 2.  Testing.  They seem to be lax in their testing.  They do only a
›› third of what a good unit test should be, and as for system testing
…[14 more quoted lines elided]…
› Who the hell is overseeing this project? 

Quite. This kind of issue should be the responsibilty of Team/Project
leads to ensure that the 'correct' processes are in place and being
followed. Having said this, it is also the responsibility of each Team
member to bring the non-adherence to 'correct' processes to the
attention of the Team Leads. After all, we ALL have a responsibilty.
The problem often seems to be that Project leads either don't care, are
incompetant or are spending too much of their time working on the actual
project deliverables rather than managing the process.

› 
›› Friends: I humbly ask your assistance.  I am solicitating your ideas on
…[6 more quoted lines elided]…
› 
I agree that there is no 'ideal' - each site has it's own peculiarities
dependant upon everything from size of organisation to development
environment to staff skills. However, I believe there are several
'higher-level' factors for a successful IS organisation:

1) Process There should be a process for everything; the SEI model &
ISO-9000/BS-5750 should be familiar to everyone from the MD/VP to the
newest junior programmer. I know a lot of people dislike 'processes' as
being too rigid, stifling imagination, etc. This only happens if the
processes are poorly implemented or not properly understood.
Implemented correctly they actually leave more time for 'the good
stuff'. After all, how many projects have you worked on where everyone
is running about like a headless chicken, deliverables are produced
inconsistently across the project and no-one can find version 3 of the
Physical design for Component B1 of Phase II?

2) Quality and the constant striving for quality improvement. This
comes from the top-down as well as the bottom-up. Management has to
create the environment in which quality improvements can be made, but
everyone has a responsibilty to improve the quality of what they and
their colleagues are doing.

3) Training. This doesn't neccessarily have to be the (overly)
expensive course provided by the external training company. Harness the
resources you have on-site - if you have an expert in a particular field
then get them to give a class. Also, don't think of training purely in
terms of 'hard' technical skills. How many people have undergone
training in how to hold a meeting? Ridiculous you say, not when a 30
minute meeting on subject A consists of 10 minutes discussing vacations,
10 minutes discussing subject B2 and B3 and only 10 minutes discussion
subject A. I bet everyone has stories regarding bad meetings!

4) Communication. This has got to be one of the major success factors
for any project. Do whatever it takes - from team meetings, circulars,
minutes or just talking to people. Meetings should be at all levels,
e.g. a Project meeting once a month (40 people), a Team meeting once a
week (10 People). Get rid of those ridiculous partitioned desks - let
people in a sub-team see and talk to each other! Get the Managers, Team
Leads, anyone with something of interest to say, to hold discussion
sessions. What are they working on, how does it fit into the 'big
picture', etc, etc. Different approaches work at different sites - just
keep trying something new until you find an approach that works for
you. Not enough time? Then hold 'brown-bag' sessions!

5) Planning. I think this has already been discussed.


So how do you achieve the above? In short - one step at a time.
However, it's difficult enough when everyone agrees with the approach;
without management commitment its vitually impossible. All you can do
is identify a major problem area that is causing some major headaches,
document the problem and a list of solutions, and present it. You can
but try. If neccessary suggest a 'pilot' team (with less critical
timescales, maybe) tries the new approach.

Lack of commitment from the individual can be resolved by 'good'
management - some people will need to be cajouled, some will need to be
'ordered' to use the new approaches. The bottom line - keep pushing the
new approaches - keep selling and pushing until people start to listen.
Think of it as a massive propoganda campaign! This process NEVER
ends!





›› Here is the kicker... I believe that the Y2K problem is only the tip of
›› the iceberg.  There is so much to be desired in some of the shops in
…[11 more quoted lines elided]…
› ----------------------------------------------------

I have to disagree with your 'consistency' comment. You seem to be
implying that striving for consistency is in some way detrimental.
Achieving consistency has several benefits (of which I'm sure you are
aware):

1) Become familiar with the format of one program and you are instantly
familar with the format of every other program written in the same way.
'Boring'? No. This allows you to concentrate on the real logic of the
program not the quirks of a particular style. Personally I find this
the most challenging and interesting part of programming, not trying to
understand why someone is using a bazaar naming convention.

2) Consistency implies Standards; Standards (hopefully) imply that
someone has determined the best way of doing something and hence
everyone starts doing things in the 'best' way. OK, I realise that this
is not always the case - we've all come across Standards that leave a
lot to be desired. However, Standards should be evolutionary - if there
is a better way of doing something then get the standards
changed.

3) etc, etc. (the list goes on)


This most certainly doesn't preclude imaginative solutions from being
developed. In fact, being consistent leaves more time for being
imaginative, e.g. if 90% of a program is 'consistent' boilerplate then
you have more time to spend on the 10% of the program that requires a
challenging solution.


I'd be most interested in hearing your (or anone else's) arguments for
why consistency is unimaginative.
```

###### ↳ ↳ ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "ge..." <ua-author-17072640@usenetarchives.gap>
- **Date:** 1998-01-05T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a90afe3cf9-p4@usenetarchives.gap>`
- **References:** `<34B05E44.43E8@erols.com> <gap-a90afe3cf9-p3@usenetarchives.gap> <gap-a90afe3cf9-p4@usenetarchives.gap>`

```

Joel Brighton wrote:

› ge··.@mai··e.com wrote:
›› 
…[10 more quoted lines elided]…
› share the specifics of the reason why?  

First, I also do not care for or believe in spaghetti code, but it
exists and we have to live with it. As for structured code the same
rational applies, as far as I am concerned. I have seen modules with
so many layers of nested "if's" and 'perform's" it blew my mind.
Perhaps my mind is geared to straight line programming, ie: Assembler.
There are efficient ways to code in COBOL without extending code from
the left side of a printout or screen to the right side. This is my
opinion only. I know others will disagree me with me at that is fine.
Write yourself a medium size module in structured code only and the
same module in straight code (meaning "go to's") and limit the number
of "perform's". Compile both of them (with a pmap option) and take a
look at the pmap and study the assembler code generated.

›› 
›› Gene The Geek - Mainframe 26 years
…[4 more quoted lines elided]…
›› ----------------------------------------------------
 
› I have to disagree with your 'consistency' comment.  You seem to be
› implying that striving for consistency is in some way detrimental. 
› Achieving consistency has several benefits (of which I'm sure you are
› aware): 
 
› Clipped: Many arguments for consistency for which I agree.
 
› I'd be most interested in hearing your (or anone else's) arguments for
› why consistency is unimaginative.

Please analyze my statement 'Consistency is the last refuge of the
unimaginative' more closely and notice the words 'is the LAST REFUGE
of the'. My statement does not infer that 'consistency is
unimaginative'!!!!

Gene The Geek - Mainframe 26 years
----------------------------------------------------
PHM's - The following statement is for you:
----------------------------------------------------
Consistency is the last refuge of the unimaginative!
----------------------------------------------------
```

###### ↳ ↳ ↳ Re: What is really wrong with all these Mainframe Systems?

_(reply depth: 4)_

- **From:** "wesley c. martin" <ua-author-6307144@usenetarchives.gap>
- **Date:** 1998-01-05T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a90afe3cf9-p5@usenetarchives.gap>`
- **References:** `<34B05E44.43E8@erols.com> <gap-a90afe3cf9-p3@usenetarchives.gap> <gap-a90afe3cf9-p4@usenetarchives.gap> <gap-a90afe3cf9-p5@usenetarchives.gap>`

```

ge··.@mai··e.com wrote:
› 
› Joel Brighton  wrote:
…[20 more quoted lines elided]…
› look at the pmap and study the assembler code generated.

Took a job in 88 as a contract consultant at a Naval Air Station where
COBOL was used on a small Novell LAN for an aircraft parts inventory
system. Another "consultant" was hired a couple months later to be the
"lead" for both my site and our 'sister' site in Florida. He convinced
'higher-management' that the straight-through code they'd been using was
too hard to understand and should be re-coded in "structured" mode as
soon as possible. He accomplished that task in 7 months for the 234
programs running the system. In the process, every single task done by
the programs took longer when his "new" code was installed than the same
tasks had required with the old straight-through code. Turns out all
those PERFORMs he loved so much took 3 times as much processing power
for that small network system than the GOTOs he hated so much! I left
the job in early 90 and heard later that the entire system was scrapped
less than a year after I left because it took too much time just to
requisition a part through the system!! Sometimes, when it ain't broke
it shouldn't be fixed. ;-)
      Wes Martin        | Mail E-mail Address: 
Father, Husband, Author | Office E-mail Address: 
 LAN Tech, Vietnam Vet  |  Free E-mail Address: 
Title 47, Chapter 5, Section 227; spam is illegal and prosecutable.
```

#### ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "bryan souster" <ua-author-1490700@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<34B05E44.43E8@erols.com>`
- **References:** `<34B05E44.43E8@erols.com>`

```

Just a few humble thoughts:
Joseph Cotton wrote in message <34B··.@er··s.com>...
› Well, folks, I went and did it.  I told the head honcho at my client
› (Fortune 500 - mainframe system) what was wrong with the way which they
…[6 more quoted lines elided]…
› 

Realistically this is totally wishfull thinking. The reality is that this
will only produce more maintainable code and does not deliver any additional
functionality to the end-users or the business. Yes it will reap significant
future benefits in many areas, but as the end-user gets nothing out of it
(reduced future problems/failures in production is a requirement not a
benefit) the resources to do this will not be made available. The best you
can hope for is 'lets do this whenever we change the code' - the theory
being that as you work on code to deliver functionality enhancement you use
structured programming techniques. Even this has limits if using structured
techniques significantly increases the cost of the enhancement. So,
realistically, pessimism reigns....

› 2.  Testing.  They seem to be lax in their testing.  They do only a
› third of what a good unit test should be, and as for system testing
…[3 more quoted lines elided]…
› never seem to have time to do it right the first time.


There most certainly is a corollary (sp?) between thorough testing and
production failures. The more you do of the former the less of the latter
you get. The problem is that the connection between the two is an inexact
science because bugs that cause production failures will always get through
even the most rigorous testing. An example is a bug induced by timing holes
that only occur when the system is processing production-level transaction
volumes.

However there should be ways of justifying a bigger testing effort,
particularly if you factor in the business costs (not just dp) of production
failures. When a production failyure occurs, the cost factor of that bug
should not only include the cost of the maintenance programmer, testing
etc., but also whatever lost business or increased business costs the
failure caused.

› 
› 3.  Version control.  I found out that the program on which I was
…[4 more quoted lines elided]…
› 
This indicates that your shop lacks the most basic understanding of the
requirements of software development. About the best I can suggest is
publish details of what hardware/op system/cobol vendor you use and find out
what others with a similar mix do.

[snip]
› Here is the kicker... I believe that the Y2K problem is only the tip of
› the iceberg.  There is so much to be desired in some of the shops in
…[4 more quoted lines elided]…
› (P.S.  A good sign...the guy seemed to listen!)

So there is some hope!!! There are some shops that do not have major
backlogs, but they are in my (non-IBM) experience non-IBM shops. Having said
this, there are many ways of improving software development productivity.
Hopefully others more experienced in your environment might volunteer some
pointers.

Bryan Souster
To reply, replace 'dot' with '.'
```

##### ↳ ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a90afe3cf9-p7@usenetarchives.gap>`
- **References:** `<34B05E44.43E8@erols.com> <gap-a90afe3cf9-p7@usenetarchives.gap>`

```

Bryan Souster wrote:
› 
› Just a few humble thoughts:
…[5 more quoted lines elided]…
›› 1.  Spagetti code.  
 
›› [snip]
 
›› 2.  Testing.  They seem to be lax in their testing.  They do only a
›› third of what a good unit test should be, and as for system testing
›› "we'll test that in production".  
›› 
 
›› [snip]
 
›› 3.  Version control.  I found out that the program on which I was
›› working, was also in the process of modification by a collegue.  Then I
…[5 more quoted lines elided]…
› requirements of software development.

In the words of Ravi Shankar... 'close, but no sitar'. Consider the
above in light of this definition:

'The responsibility for allocation, motivation and *co-ordination*
(emphasis added) of personnel and resources towards the accomplishment
of a stated Executive goal is that of Management.'

In item 1) (los programmos de fettucini) re-structuring can be done by
hand (personnel) or by hand with the assistance of a restructuring
package (resources).

In item 2) (der Koden-chunk des Kerflooies)... well, to be truthful,
*any* piece of code can be used in situations which violate its original
specifications and conditions... but, in general, testing is also
personnel/resource allocation.

In item 3) (controlle` versione`) it is *purely* a matter of
co-ordination.

Next?

DD
```

#### ↳ Re: What is really wrong with all these Mainframe Systems?

- **From:** "gary drummond" <ua-author-7007584@usenetarchives.gap>
- **Date:** 1998-01-11T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a90afe3cf9-p9@usenetarchives.gap>`
- **In-Reply-To:** `<34B05E44.43E8@erols.com>`
- **References:** `<34B05E44.43E8@erols.com>`

```

Psychedelic Harry wrote:
› 
› In article <34B··.@er··s.com>, jco··.@er··s.com wrote:
…[20 more quoted lines elided]…
› Sorry, I just had to vent....
Let's see you pick up a 20 year old C program and correct a problem
before the AM shift shows up! Good or bad, a standard helps in
looking at code done by someone else. Of course, if it were C or C++
it wouldn't even produce the same code, or even compile without
changes....
Gary
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
