[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# XP: Extreme Programming

_43 messages · 14 participants · 2000-03_

---

### XP: Extreme Programming

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C0AFCB.1B6B5249@home.com>`

```
Now Ken,

Here's one to whet your appetite. Was browsing Chapters our big-box book
store this evening and lo and behold - "Extreme Programming" Addison and
Wesley, damn forgotten author's name, Ken ?, Brent ? something or other.
Bit of a guru on XP and has also written books on Smalltalk.

Guess which chapter I looked at first, "When not to use Extreme
Programming " :-). Having written the bloody book here was a chapter
devoted to not using it. Seems its OK for about 4 programmers and he
says definitely don't use it where you have 100 - I would have thought
that was EXACTLY where you would WANT to use the methodology.

So intrigued, nearly bought a copy for you - but at $44.95 CDN for
something only as thick as a monthly copy of Reader's Digest, thought,
to hell with it, let that bloody Aussie buy his own copy if he's
interested :-)

On a slightly different topic - but one that came up here recently, as I
was browsing above book - I was looking at a bookcase stashed with
copies of books devoted to writing effective resumes/CVs/who-you-are
etc. What a load of BS !

Jimmy, Calgary AB
```

#### ↳ Re: XP: Extreme Programming

- **From:** peter12@globalnet.co.uk (Peter Morris)
- **Date:** 2000-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c0d4b7.4728806@news.globalnet.co.uk>`
- **References:** `<38C0AFCB.1B6B5249@home.com>`

```
Interesting you should state "Seems its OK for about 4 programmers". I
used to work for a company where I was one of 4 people in the
department. 2 programmers, an ops manager and the director. We ALL
coded, when we needed to and we used to churn out programs fast. We
had to. We had problems, but they were fixable and it was "easier" to
use the production system to "test" in.
I can't believe I just said that!

The benefits were that we were one of the fastest reacting companies
in our field. Unfortunately, at our site, the documentation sufferred
and all of us 4 have left, leaving 4 newbies in the roles, which
doesn't help them. 

I guess by my experience at XP I can understand why they say it's ok
for 4 programmers but not 100. However, with the right
documentation...etc I can't see that it would be much of a problem
either. Perhaps because it increases the size of the project/system
and therefore the number of bugs going into it.

PAM.

__________ "James J. Gavan" <jjgavan@home.com> __________
>Now Ken,
>
…[21 more quoted lines elided]…
>Jimmy, Calgary AB
```

##### ↳ ↳ Re: XP: Extreme Programming

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C1C5CC.1498F222@melbpc.org.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk>`

```
The previous posting is a classic misunderstanding of XP. XP is
*not* 'code and fix'. It is a whole set of principles that when
combined allow to you build fast, reliable software that is
maintainable. 

Let's test if you were really doing XP

- did you do pair programming (noone codes alone, you always code
withsomeone sitting next to you)
- did you have test cases for every method, and were you able to
run all the test cases in under 10 minutes
- did you document requirements in smallcards, do estimates and
break u anything that would be longer than 3 weeks, then
negotiate with the users on priorities
- weekly reviews of progress in a stand up meeting?
- did you remove someone from a task if they did not finish it in
3 weeks
- did you constantly refactor as you went, to keep the system in
good shape. 

Can I suggest people actually read the material before assuming
they know what XP means?

Tim Josling

Peter Morris wrote:
> 
> Interesting you should state "Seems its OK for about 4 programmers". I
…[10 more quoted lines elided]…
> PAM.
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1kt5cskrjqukac5n3ot52hhnscn727efgn@4ax.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au>`

```
Tim Josling <tej@melbpc.org.au> wrote:

>Let's test if you were really doing XP

>- did you do pair programming (noone codes alone, you always code
>withsomeone sitting next to you)
>- did you have test cases for every method, and were you able to
>run all the test cases in under 10 minutes

i hope you are kidding. some problems can't be solved in 10 minutes.

>- did you document requirements in smallcards, do estimates and
>break u anything that would be longer than 3 weeks, then
…[3 more quoted lines elided]…
>3 weeks

oh yes, this is a great idea. explaining it to every new person if
they don't solve it in 3 weeks. sometimes, it takes 3 weeks just to
come up with a solution (this is true in scientific fields alot more
than data processing though).

>- did you constantly refactor as you went, to keep the system in
>good shape. 

if it ain't broke, don't fix it.

>Can I suggest people actually read the material before assuming
>they know what XP means?


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C39838.9A2804B@zip.com.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <1kt5cskrjqukac5n3ot52hhnscn727efgn@4ax.com>`

```
G Moore wrote:
> 
> >- did you have test cases for every method, and were you able to
> >run all the test cases in under 10 minutes
> 
> i hope you are kidding. some problems can't be solved in 10 minutes.

No, he is not.  There are sometimes two classes of test cases,
thorough and fast when this cannot be achieved.  Some people tend to
confuse volume testing with quality testing though.  Do not forget
that if you test every permutation of file open for an object, a
higher level object does not need to define that many extra test cases
to show that it's particular incantation is correct, it 'knows' the
subordinate object is correct.

My make file for Unix now has a 'testrig' program that runs before I
link my mainline program.  It must be successful before I can create
my mainline program.  I know very quickly if I have made a mistake in
any subroutines.

When I make a change I add a test to the test suite that shows what I
am doing that is different.  This is another requirement.  When I do a
bug fix, I first code a test that shows the bug, then I fix it.

When I first designed my tests it took about 2 hours to run the
testing and longer to check it.  Now I have a baseline output, I know
what I want to change and everything else checks against baseline in
about 10 minutes (7,000,000 records about 5 different ways on a PC).

> >- did you remove someone from a task if they did not finish it in
> >3 weeks
…[4 more quoted lines elided]…
> than data processing though).

The tasks are broken down into small workable chunks.  Some people
have daily check in.  All tests must run in order to be able to check
it in.

Since XP also proposes a bull pen where all the programmers sit and
exchange ideas and also pair programming (the pairs swap regularly)
this sort of communication has already happened.

> >- did you constantly refactor as you went, to keep the system in
> >good shape.
> 
> if it ain't broke, don't fix it.

A classic quality problem.  I have a shell script that drives all
customers (a central point of failure) every new product you add for a
customer has to have this central script modified.  One slip up (a
missed end-if equivalent) can disable many clients.   We can test this
script and prove that it works, but is it a quality solution?  I say
no because the script must be modified.  Extract the logic and make
the script automatically pick up new products for a client from a
database. The result is the same!

When I put this to management, the answer is simple.  You can tested
it and it works, leave it alone:  i.e. if it aint broke don't fix it.

Case 2:  There are times you can make a fix in two lines of code but
you should do much more.  The flow of the program will be interrupted
by the fix that is defined.  A sample of this logic is 'if line of
page is ten' in the read routine, it is a fast simple fix that works. 
It is also flawed.  The logic might easily be factored out into the
'new page routine' but cause a more complex change, it might handle
lines 9-15 specially.  Doing this work today will make the next
problem (such as process line 11) easier to implement.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 5)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r098cs80u4vom1aij6g0ir8unqiq16hj0u@4ax.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <1kt5cskrjqukac5n3ot52hhnscn727efgn@4ax.com> <38C39838.9A2804B@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>G Moore wrote:
>> 
…[11 more quoted lines elided]…
>subordinate object is correct.

that is nice and all, but what happens when you come across bad code?
i suppose xp works when you are in the development phase, but, hell,
most software doesn't start from the hardware up. they start from the
os, and probably previous data from a business startup. and if you get
a line where you don't know what it does, figuring out the code in 3
weeks is unlikely. in y2k, this was especially a problem, because all
the code was being remediated. can you test y2k fixes in 10 minutes?

show me an xp project without data-backups.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C4F668.7F6D6462@zip.com.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <1kt5cskrjqukac5n3ot52hhnscn727efgn@4ax.com> <38C39838.9A2804B@zip.com.au> <r098cs80u4vom1aij6g0ir8unqiq16hj0u@4ax.com>`

```
G Moore wrote:
> 
> Ken Foskey <waratah@zip.com.au> wrote:
…[24 more quoted lines elided]…
> 10 minutes?

Firstly the problem you discuss is merging a non-XP product into an XP
framework.  You are changing the framework to prove your point.

If I have an XP project then I know that the code has a complete test
bed at my finger tips and I can make changes safely.  Because it is OO
and refactored savagely I can be sure that the Y2K problem resides in
a single object.  I first highlight the bug with an extra test case
and make my change ensuring that the new code works correctly.  Five
minutes work I would say.

> show me an xp project without data-backups.

I do not understand your point.  XP is a programming methodology you
still need to support it with all the peripheral configuration
management, backup and environment stuff that is everyday in
programming.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 7)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o9ebcscl3auk6rjbaar07p90ijsegliaup@4ax.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <1kt5cskrjqukac5n3ot52hhnscn727efgn@4ax.com> <38C39838.9A2804B@zip.com.au> <r098cs80u4vom1aij6g0ir8unqiq16hj0u@4ax.com> <38C4F668.7F6D6462@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>G Moore wrote:

>> that is nice and all, but what happens when you come across bad code?
>> i suppose xp works when you are in the development phase, but, hell,
…[5 more quoted lines elided]…
>> 10 minutes?

>Firstly the problem you discuss is merging a non-XP product into an XP
>framework.  You are changing the framework to prove your point.

you are, of course, correct. but i have yet to find a new project
which was built from the ground-up. they usually start with the os.
and when it hits the user, you add on any number of other programs
running simultaneously.

>If I have an XP project then I know that the code has a complete test
>bed at my finger tips and I can make changes safely.  Because it is OO
…[3 more quoted lines elided]…
>minutes work I would say.

i can deal with threads, i can deal with events and i can deal with
modular code, but i have no idea what this oo or xp stuff is.

>> show me an xp project without data-backups.

>I do not understand your point.  XP is a programming methodology you
>still need to support it with all the peripheral configuration
>management, backup and environment stuff that is everyday in
>programming.

i guess i am too old to learn new paradigms.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C1EDBD.8F2F7B44@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au>`

```


Tim Josling wrote:
> 
> The previous posting is a classic misunderstanding of XP. XP is
…[18 more quoted lines elided]…
> 

OK Tim, I accept your summary above. But here we get into "buzz-words,
"buzz methodology". What above, with perhaps the exception of pairing,
is new from what I was doing over 30 years ago as a systems manager. I
did it nicely, but if you didn't perform, I eased you out the door
without using the word "fired".

I've been around long enough now to be jaundiced - my generation (teens
just after W.W.II), saw the introduction of all the new management
techniques, (not just in EDP), and surprise, surprise, how many
companies fell flat on their faces even though they had bright-eyed
bushy-tailed young graduates steeped in all this management crap.

My point is don't ignore something like XP, but truly some smart ass has
latched on to a set of common sense ideas and christened them with the
name "XP". It is a shabby, constantly recurring theme in our modern
society where sincere hard workers get sucked into some newly coined
management technique.

PS: So how's XP working out with GNU COBOL :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89u2eq$431$1@news.inet.tele.dk>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com>`

```
Being the same age, I believe, I think I can supply with some info.

System development is a very fine art, where talent undoubtable is a very
strong factor.

Regretably the business is disturbed by loudspeaking oracles and from time
to time we need to take a few days off, to go fishing just to be close to
the real values of life.

I think I could paint the inside of a rubber cell with all the good efforts
this business has made to secure 'that the user gets what he wants'. XP,
RAD. Prototyping, Pseudo-Code, Jackson, Yourdon, James Martin (is he back
from the Y2K-shelter).

What I am trying to say is that we have seen many names and methods in a
long life of programming. Only very few qualities in this world will last.
Delivering high quality is something old craftsmen and old programmers know
about. You cannot put commitment into manuals, but manuals can explain the
secret to youngsters who went for the money.

So, dear professors, gurus and smart asses all over the world. back in the
sixties we learned that Analysis, Programming, Testing and Implementation
was the phases - tell me, what's new - except for the names of the gurus.

Regards
Ib


James J. Gavan skrev i meddelelsen <38C1EDBD.8F2F7B44@home.com>...
>
>
…[43 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C2AD54.4EE746F6@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk>`

```


Ib Tanding wrote:
> 
> Being the same age, I believe, I think I can supply with some info.
 
> So, dear professors, gurus and smart asses all over the world. back in the
> sixties we learned that Analysis, Programming, Testing and Implementation
> was the phases - tell me, what's new - except for the names of the gurus.

Well that was reassuring to know that I wasn't the only old codger who
felt that way. And as regards Martin, just think, if I hadn't wasted my
time learning to program I could have waltzed around numerous EDP sites
asking the guys what they were doing - and then lay on frequent seminars
at $1,000 a crack for each dumb attendee.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 6)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a16i8$9kj$1@news.inet.tele.dk>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com>`

```
Yeah, but you wouldn't be happy. I think that the business is divided into
several groups of people.

A small group of people, who will never know what it's all about. The only
way to stay in this progressive business  for them is to become managers or
to write books.

Heavily serious people. The know every detail and can see every angle of the
IT-industry. They are stucked away in large organisations or waste their
time with research in the universities. From time to time they write
something very clever that very few people want to read.

A very large group of people is what I call the autumn leaves. They fly with
the wind. The major problem for them is to find the time to know enough
about the trendy stuff to act  clever at parties. They read the concepts and
discuss pros and cons with equal minded, hoping eventually to be called an
expert.

The last group is people like us. We are just making all the impossible
applications. It is very essential to us, that the customer is satisfied. It
is very important to us that QA and QC is a very natural part of the
application. Testing is an art, and we know the importance of a good
testcase.

I love to be in this last group, and I think that you and many other good
men and women in this NG are happy to be there. We are not blind to new
ideas - we just cannot be excited about things, that has been done for years
or proven useless years back.

We are not grumpy - but very selective to excitement.

This is fun

Ib



James J. Gavan skrev i meddelelsen <38C2AD54.4EE746F6@home.com>...
>
>
…[4 more quoted lines elided]…
>> So, dear professors, gurus and smart asses all over the world. back in
the
>> sixties we learned that Analysis, Programming, Testing and Implementation
>> was the phases - tell me, what's new - except for the names of the gurus.
…[7 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 6)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com>`

```
I noticed that James J. Gavan as jjgavan@home.com said...
> 
> 
…[12 more quoted lines elided]…
> at $1,000 a crack for each dumb attendee.

You and me both, but we weren't canny enough.  I too am pretty hostile to 
methodologies for their own sake, having suffered a few of them over the 
years.  I guess that some of them work, OS/2 for instance is entirely OO, 
but my take is that you have to follow them totally to prove them and I 
don't see this happening in (m)any commercial environments because you 
really need a clean sheet to start from, as well as the dogma.
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C33D10.947C4AB@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk>`

```


Charles F Hankel wrote:
> 
> I noticed that James J. Gavan as jjgavan@home.com said...
…[22 more quoted lines elided]…
> 
Fortunately that's not the case with OO COBOL. You can happily mix and
match. Say given a system of 100 programs, number crunching, editing,
printing etc. You can pick and choose between structured and OO. The
only catch is that if you are going to invoke something, then obviously
it has to be in a source file which is in OO Class syntax.

In my own case, just for consistency of style, all my programs are OO
classes, the only program which is 'structured' being the trigger
program which kick-starts the application. In truth I could make my
print programs structured, but I'd have to include file syntax - then
I'd lose the benefit of what I'm doing with OO, using only one class to
access each file.

PS: I love it, I love it. The spellchecker suggested "kicks tarts" for
"kick-starts" - now I betcha Michael Matthias can make something of that
one :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com>`

```
James J. Gavan wrote in message <38C33D10.947C4AB@home.com>...
>
>PS: I love it, I love it. The spellchecker suggested "kicks tarts" for
>"kick-starts" - now I betcha Michael Matthias can make something of that
>one :-)
>


Kicks tarts, huh? Sounds like the answer to, "Name a popular pastime for a
sadist."

Michael Mattias  << correct spelling
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C3ED78.6361E631@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net>`

```


Michael Mattias wrote:
> 
> James J. Gavan wrote in message <38C33D10.947C4AB@home.com>...
…[9 more quoted lines elided]…
> Michael Mattias  << correct spelling

I knew you wouldn't disappoint me :-)

Correct spelling noted; mea culpa. Just out of curiosity how does your
last name come across phonetically - I aint got a problem with your
first name.

Jimmy
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com>`

```
James J. Gavan wrote in message <38C3ED78.6361E631@home.com>...
>Correct spelling noted; mea culpa. Just out of curiosity how does your
>last name come across phonetically - I aint got a problem with your
>first name.
>


"Mattias" is pronounced, "mah-tie'-ass"  (accent on second syllable)

"Michael" is pronounced, "john"

MCM
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 11)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C50F93.8075DD58@cusys.edu>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote:
> 
> "Michael" is pronounced, "john"
> 

Silent "h"?
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C5485F.86A33371@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net> <38C50F93.8075DD58@cusys.edu>`

```


Howard Brazee wrote:
> 
> Michael Mattias wrote:
…[4 more quoted lines elided]…
> Silent "h"?

Your note reminded me I wanted to comment. I had to grin the other day,
I got into Merant's Answerlab which is a bit of a 'triumvirate' - Pat
Magee giving main support from Philly, folks like Steve Biggs jumping in
from Newbury, UK and Monsieur Jean Villeneuve from Quebec - latter was a
separate company but now part of Merant.

Can't remember the gent's name, but he was of Asian origin, so obviously
some of the nuances of English were lost on him. He raised a query in
Answerlab to which Jean replied. The enquirer subsequently referred to
Jean's reply as, "When Jean said that, SHE..... was referring to....".

Pat in Philly politely pointed out that 'she' was 'he', that Jean =
John, and that the support guy was French/Canadian.  Serves him right
for being a Quebecois :-) 

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 13)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C56FBC.3823AFE3@cusys.edu>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net> <38C50F93.8075DD58@cusys.edu> <38C5485F.86A33371@home.com>`

```
"James J. Gavan" wrote:
> 
> Pat in Philly politely pointed out that 'she' was 'he', that Jean =
…[3 more quoted lines elided]…
> Jimmy, Calgary AB

I've done the same thing on on the other COBOL newsgroup.  Or at least I
was taken aback by someone mentioning that Cheesle was a "he", I had
assumed differently.

With different languages, we can't control things.  Robert E. Lee and
Huey Long are not oriental...   But parents should decide whether they
want their children to have androgynous or unfamiliar names.  If they
do, people will guess at their gender.  Maybe that's what they want.  
My wife could have decided she wanted to be called Patricia or Patty
instead of Pat.  (As a young child she thought the Patty Cake rhyme was
about baking her in an oven).
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qMex4.5482$5Y2.75915@news3.mia>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net> <38C50F93.8075DD58@cusys.edu> <38C5485F.86A33371@home.com> <38C56FBC.3823AFE3@cusys.edu>`

```
Howard Brazee wrote:
>
>But parents should decide whether they
>want their children to have androgynous or unfamiliar names.

I used to have a (male) boss named Sandy.  Once when he attended an
out of town business meeting the company reserved a room for him and
a woman.  Both were surprised. :-)  Does this fit under 'Extreme
Programming'?
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C57FAE.5D4AD3B2@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net> <38C50F93.8075DD58@cusys.edu> <38C5485F.86A33371@home.com> <38C56FBC.3823AFE3@cusys.edu> <qMex4.5482$5Y2.75915@news3.mia>`

```


Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[7 more quoted lines elided]…
> Programming'?

No, but it sure as hell shows you the flexibility of how different
objects can be paired for a particular 'method'  :-)

Jimmy
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 14)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C57901.1F143793@cusys.edu>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <89u2eq$431$1@news.inet.tele.dk> <38C2AD54.4EE746F6@home.com> <MPG.132d3a132f3ab57b98994b@news.mersinet.co.uk> <38C33D10.947C4AB@home.com> <BlOw4.117$DB1.26941@dfiatx1-snr1.gtei.net> <38C3ED78.6361E631@home.com> <TKZw4.689$DB1.214658@dfiatx1-snr1.gtei.net> <38C50F93.8075DD58@cusys.edu> <38C5485F.86A33371@home.com> <38C56FBC.3823AFE3@cusys.edu>`

```


Howard Brazee wrote:
> 
> "James J. Gavan" wrote:
…[9 more quoted lines elided]…
> assumed differently.

Oops, it was this newsgroup.   Oh well.  As a child, the only "Andre" I
had heard of was the author Andre Norton.  Her real name was Alice or
something, but it never struck me that someone would have a pen name to
disguise one's gender (and then put your face on the jacket) - and I
assumed "Andre" was feminine!
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C22D56.6792F50D@melbpc.org.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com>`

```
(there have been many charlatans pushing useless fads in the
computer industry)

Fair comment. I can't do pair programming but I do have tests for
everything. And I only build as I need. I think it XP a good
thing. Yes a lot of things have been mutton dressed as lamb. OO
being a classic example - the supposed benefits are very limited
(at least with C++ - with true OO languages it may be a different
story)

I don't actually think Kent Beck is a charlatan, the exact
opposite in fact. I do think with XP that the whoile is greater
than the sum of the parts. Eg if you don't do testing it's just
good ol' "code and fix".

I am still working on the COBOL compiler (23,000 lines of code
and counting). Just a few minutes ago I actually got the GCC back
end to generate some code for me - a major breakthrough after 10
weeks work. I am celebrating by doing some 'fun' surfing for a
while. It is all downhill from here. I have solved all the
horrible problems I encountered

- how to process the ugly cobol copy and replace verbs
- how to parse the very non-LALR language cobol
- how to hook into the gcc back end

So, watch this space!

Tim Josling
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 5)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.132d382459732d2598994a@news.mersinet.co.uk>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au>`

```
I noticed that Tim Josling as tej@melbpc.org.au said...
> 
> I am still working on the COBOL compiler (23,000 lines of code
…[8 more quoted lines elided]…
> - how to hook into the gcc back end

Do you mean to say that you're not writing the compiler in COBOL?  A 
compiler-writer friend of mine says that the only cool way to write a 
compiler is in the language that it's supposed to compile and that the 
first compilation is itself.  IIRC this is how the product now sold as 
Merant/MicroFocus was initially developed.

Don't take this to heart BTW, if I could get the time to do a compiler, I 
doubt that I'd have the inclination now.
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c3ef55.92912956@news.cox-internet.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au> <MPG.132d382459732d2598994a@news.mersinet.co.uk>`

```
On Mon, 6 Mar 2000 04:00:05 -0000, Charles F Hankel
<charles@hankel.mersinet.co.uk> wrote:

>I noticed that Tim Josling as tej@melbpc.org.au said...
>> 
…[18 more quoted lines elided]…
>doubt that I'd have the inclination now.

GCC actually supports other languages.  For example, Assembler.  I
think Tim's project is going to convert COBOL source to C, which is
then compiled by GCC.  I don't have a problem with that approach at
all!  The intermediate steps don't interest me so much as that the
source is COBOL and the object executes!
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C4046B.8FE8385C@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au> <MPG.132d382459732d2598994a@news.mersinet.co.uk> <38c3ef55.92912956@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> On Mon, 6 Mar 2000 04:00:05 -0000, Charles F Hankel
…[28 more quoted lines elided]…
> source is COBOL and the object executes!

Agree with you the result is what we are after. Not suggesting Tim
should divert to doing it, but it would be real nice if we had a COBOL
virtual machine. And I'll respond to Tim in some detail about his query
on OO - chances are he would find that a COBOL VM coupled with OO COBOL
would really give him the cat's whiskers to develop his compiler ! (Pure
conjecture, but I'm guessing the ramifications of a COBOL VM would have
an enormous impact on future COBOL development).

Just think Tim, you could put all those reserved words, (great gnashing
of teeth from Down Under), into an  OO collection to parse for validity
- with no restriction on the size of your collection - just making it as
big or as small as you want.

Interestingly enough, the above is not just an idle thought. My system
contains some 950 descriptions of items being inspected, which I
intended to include in a listbox for selection. But what if that list
grows to 1,500 or 2,000 OR MORE? Paranoia set in about going belly-up on
memory, (i.e. 2,000 x 40 chars, an object reference for the collection
and another 2,000 object references for the individual entries in the
collection).

Yes it can be done in procedural, but I've used OO to generate
descriptions from mnemonics, rather than hold a superfluous 40
characters in each record which would contain repetitive descriptions.
I'm able to "localize" the working-storage section to each method -
which makes the logic of the whole thing much easier to read - as
opposed to a humungous global working-storage, where you constantly find
yourself jumping to the top of your source to see "what did I call that
field ?". 

Jimmy
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 7)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C40AA9.751BE5D0@melbpc.org.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au> <MPG.132d382459732d2598994a@news.mersinet.co.uk> <38c3ef55.92912956@news.cox-internet.com>`

```
The core of the compiler is in C - but see later. This is because
there are no free tools that I am aware of for lexcial analysis
(eg flex), parsing (eg bison), or code generation (eg the GCC
back end) that support cobol. 

However my plan is to write a core in C and then bootstrap so I
can write much of the rest in cobol. Maybe other cobol
programmers will help when the time comes!

Someone assumed because of my association with GNU COBOL2C that I
am generating C for compilation into assembler/object code.
Actually I am generating assembler directly, using the GCC back
end. This makes for faster code and better debugging, but more
headaches!

Nothing usable as yet but when I reach that point I will post
here.

Tim Josling

Thane Hubbell wrote:
> 
> On Mon, 6 Mar 2000 04:00:05 -0000, Charles F Hankel
> <charles@hankel.mersinet.co.uk> wrote:
> > ...
> >Do you mean to say that you're not writing the compiler in COBOL?
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C41DE6.2C171843@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au> <MPG.132d382459732d2598994a@news.mersinet.co.uk> <38c3ef55.92912956@news.cox-internet.com> <38C40AA9.751BE5D0@melbpc.org.au>`

```


Tim Josling wrote:
> 
> The core of the compiler is in C - but see later. This is because
…[3 more quoted lines elided]…
> 
Tim,

Just for clarification - are you still on Tiny COBOL or is it the GNU
COBOL that Laura was associated with, or are they both now one and the
same thing ?

Jimmy
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 9)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C65197.EE88853C@melbpc.org.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com> <38C22D56.6792F50D@melbpc.org.au> <MPG.132d382459732d2598994a@news.mersinet.co.uk> <38c3ef55.92912956@news.cox-internet.com> <38C40AA9.751BE5D0@melbpc.org.au> <38C41DE6.2C171843@home.com>`

```
None of the above. I will advise when I have something to report,
to this newsgroup. TIny COBOL is still pretty active. GNU COBOL
is pretty quiet. I am still working on my own for now, until I
have a critical mass of function.

Tim Josling

"James J. Gavan" wrote:
> Tim,
> 
…[4 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#2c0gErh$GA.209@cpmsnbbsa03>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:38C1EDBD.8F2F7B44@home.com...
>
>
…[5 more quoted lines elided]…
>
The term extreme programming will probably cause some managers to shy away
from the concepts. If Rapid Application Development hadn't already been
spoken for, it would have been a better term.

Some of us have already been using SOME of the techniques on an informal
basis for years.
Loosely defined specifications. Incremental development, and (user) testing.
Leaving performance optimization until last. Automation of testing. Detailed
test plans.

I work in an IBM Mainframe environment: Batch, CICS, DB2, VSAM, etc.
One of hardest things to sell is automation of testing, and recognition of
the fact that the automated testing is on the same level as the production
code itself. I constantly hear that we don't have the time to write QA type
programs. It seems that we do have the time to fix errors after the fact
when the cost is sometimes enormous. i.e. A daily JOB wipes out numeric
data, and the bug isn't discovered until month-end when the data is next
used.

If the acceptance of XP concepts allow me to do what I need to do to produce
solid, dependable systems, then I'm all for it.
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C39A09.77D4E42D@zip.com.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c0d4b7.4728806@news.globalnet.co.uk> <38C1C5CC.1498F222@melbpc.org.au> <38C1EDBD.8F2F7B44@home.com>`

```
"James J. Gavan" wrote:
> 
> My point is don't ignore something like XP, but truly some smart ass
…[3 more quoted lines elided]…
> coined management technique.

Jimmy,

Most developments in this world are built upon what we know.  M$
windows was built from Mac, Mac was from Parc, etc.  The interesting
thing with XP is the synergy of the whole thing.

An quick look at XP does lead to this sort of dismissive approach.  I
personally am in 'watch this space' mode.  I hate waterfall,
incremental development has merit but problems, quality systems are
mostly documentation and very little quality.

There is no pretence that the whole package is made up of new tinsel. 
Rather they are proud that they have brought together old elements in
a new way. Kent Beck is credited with some early small talk
development. This guy has a long term standing in the OO community.

I am actively searching for 'the answer' on quality.  How do I convey
what I mean by quality to a non technical person?  How do I convey
these concepts to a new programmer just started work with me, even if
they have 10 years experience?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Extreme Programming

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ow98Qreh$GA.258@cpmsnbbsa05>`
- **References:** `<38C0AFCB.1B6B5249@home.com>`

```
I remembered that Ken Foskey had posted a web site on XP in a previous
thread:
http://www.extremeprogramming.org/

James J. Gavan <jjgavan@home.com> wrote in message
news:38C0AFCB.1B6B5249@home.com...
> Now Ken,
>
…[10 more quoted lines elided]…
>
I took a look. It seems that they recommend teams with 4-10 members.
After reading awhile, it appears that the approach would not be suited to
large teams because of the continual upgrading and testing. Administration
of the system would not be easier with a large team.

I once worked for a software firm where projects which were behind schedule
would cut resources.
The reason this works is that there are normally some people on a project
who do not understand what they are doing. They make negative contributions
to productivity. i.e. you can do it yourself in 5 minutes, but it takes you
30 minutes to explain it to someone else so that they can do it in 2 days.

PS: I liked NO OVERTIME.
```

#### ↳ Re: Extreme Programming

- **From:** "Stephen Thomas" <talkingcats@gobble.clara.co.uk>
- **Date:** 2000-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zygw4.1383$7F3.32005@nnrp4.clara.net>`
- **References:** `<38C0AFCB.1B6B5249@home.com>`

```
James J. Gavan wrote in message <38C0AFCB.1B6B5249@home.com>...
>Now Ken,
>
…[21 more quoted lines elided]…
>Jimmy, Calgary AB
What is 'Extreme Programming'?  I've never heard of it!
```

##### ↳ ↳ Re: Extreme Programming

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C1B31A.D66BA1CB@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <zygw4.1383$7F3.32005@nnrp4.clara.net>`

```


Stephen Thomas wrote:
> What is 'Extreme Programming'?  I've never heard of it!

Nor had I until the Aussie mentioned it. There's a net site. As I
understand it from Ken, this could be one aspect :-

	Evaluate true
	  when mynumber = 1 perform Para-1
	  when mynumber = 2 perform Para-2
	  when mynumber = 3 perform Para-3
	End-evaluate

Now what happens in your program if the number is zero or greater than
3 ? At least that's my initial understanding from Ken (????). I suppose
another of way of putting it would be to call it 'destruction testing'.

Note : No response from the Aussie yet so 'spose he must be spending the
weekend in the Outback on a walkabout with his favourite dingo :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Extreme Programming

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C1E02E.3B54ED0C@zip.com.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <zygw4.1383$7F3.32005@nnrp4.clara.net> <38C1B31A.D66BA1CB@home.com>`

```
"James J. Gavan" wrote:
> 
> Stephen Thomas wrote:
…[18 more quoted lines elided]…
> :-)

No I was down at the opera house underneath the coat hanger (Sydney
harbour bridge) busking by playing the digerydoo.

Extreme programming is the process of doing some up front analysis and
then working on the product using fast cycles giving workable results
as early as possible.  It achieves a quality product by supporting
this with some extensive testing allowing the programmer to safely
rebuild bad design decisions by having an extensive (and I mean
extensive) testing system. There are other things that go into making
an XP development but this is what attracted me.

One of the other things are pair programming, using two programmers on
a terminal.  This takes a fair amount of selling but studies have
shown this to be better.  This type of programming replaces extensive
inspection and is probably 100% better than what most people call
inspection due to lack of understanding.

The thing that attracted me is documentation less programming.  This
is not as simple a definition as it seems.  There is a heavy
responsibility to write excellent code which acts as the
documentation.  We all know how useful system documentation is after a
short period of time in all but the most pedantic of shops.

Finally it is about doing what the customer wants you to do.  This is
surprisingly radical.  A 'customer' is resident on the XP team so that
they maintain contact with the business.

XP appears to rely more on the discipline of the individuals rather
than the process and procedures.  How to do XP is very well documented
as Tim Josling pointed out and all (most) elements must be satisfied
before you can claim to be 'XP compliant'.


Regarding some of the other stuff.  I am interested in software
engineering.  Some of the tools I raise are from many sources,
software tools by Kernighan (that's the one Jimmy raised).  I am
extremely fortunate that I learned to code by reading this book, it
taught me how to program, not how to create compilable syntax.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

The more I learn, the less I know.
```

#### ↳ Re: XP: Extreme Programming

- **From:** mike_myers@bellsouth.net (Mike Myers)
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c5e713.5637531@news.clt.bellsouth.net>`
- **References:** `<38C0AFCB.1B6B5249@home.com>`

```
Can XP work for COBOL?

I have been studying XP for some time but seems all real world usage
has been Smalltalk related. The idea of a minimal methodology has
a lot of appeal to me and I have been involved in some informal
pair programming using a 4GL. I am not sure that XP  would
apply to COBOL easily due to (dare I say it?) the verbose nature
of COBOL? I really do like COBOL for business apps but having
2 programmers sit side by side while coding a bunch of WS areas or
FDs does not *seem* productive. Procedure division stuff can be 
about the same as any other language.

Also some of the OO analysis does not seem to have direct relationship
to the structured environment that I am used to. Can CRC cards and
these other  techniques be applied to COBOL applications?

Do the simplest thing that will work and constant refactoring make
so much sense to me. Refactoring is not breaking something that
works but making the code simpler while doing the same thing. We've
all seen code that is more complex than it should be. Now we can 
have *permission* to refactor it and with 2 pair of eyes looking at 
the code and with a test case that will take less than 10 min. to 
execute then we can procede with confidence with the refactoring.

Anybody using anything like XP in a COBOL environment?

Thanks,
Mike Myers
```

##### ↳ ↳ Re: XP: Extreme Programming

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C605F0.17C04B6B@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net>`

```


Mike Myers wrote:
> 
> Can XP work for COBOL?
…[14 more quoted lines elided]…
> 

I think a lot of what you say is true about some of this stuff being
overblown, and in a sense it doesn't apply to a structured businesslike
language such as COBOL. But I do see some advantages in that pairing,
though I agree with you, not when you are generating your W/S entries. 
I would see the paring more as critiquing the finished goods and making
suggestions.

Hell, Ken and I have done exactly that - where I sent him code from here
in the Great White North so that he could peruse it on Bondai beach
while gawking at the sheilas :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C64B85.7DFD9F6C@zip.com.au>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net> <38C605F0.17C04B6B@home.com>`

```
"James J. Gavan" wrote:
> 
> Mike Myers wrote:
…[28 more quoted lines elided]…
> beach while gawking at the sheilas :-)

Mike,

Small talk is supported by an amazing programming editor.  It allows
you to pull out a method out of the middle of a stream of code
AUTOMATICALLY including parameters.   It also allows you to move a
method from object 1 to object 2 (say it should be pushed down, all
pets take a walk and then you introduce fish).

I think most people are looking at XP and using the testing framework
even in OO projects.  This is what I have done. I was taught
scaffolding many years ago by an old programmer, now I religiously do
this testing and it saves time.  Yes I write extra code to save time!

Jimmy,

That's Bondi...

You are talking about Fagan's inspections, refer to a book by Tom
Gilb. I am a great support of formal inspection but...

Inspections works in arrears.  The author does the work and invest a
little of themselves in the outcome.  If someone says it is not quite
right defences tend to come up.

The other alternative is worse.  'Yep had a quick look mate, she'll be
right throw it in and see if it works.'  Formal inspection is about an
investment in time, often this is not understood. I took time to
really go over your code, even then it was faster than what I would do
for an system that was built for my company.  I would not have
necessarily critiqued the same thing, the purpose of my look at your
code was focused on form not functionality which is what an inspection
is truly about.

The pair programming invests both people, immersing them directly in. 
Those tricky discussions are nutted out on the spot (have you ever
worked alone without a partner at all, bloody hard work).  It can save
time eliminating those off by one errors.  You are working together to
remove those ego problems.  You pair old and new to get the new person
up to speed faster and give the old dog new ideas.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** mike_myers@bellsouth.net (Mike Myers)
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c6874b.13023511@news.clt.bellsouth.net>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net> <38C605F0.17C04B6B@home.com> <38C64B85.7DFD9F6C@zip.com.au>`

```
On Wed, 08 Mar 2000 23:45:57 +1100, Ken Foskey <waratah@zip.com.au>
wrote:

>"James J. Gavan" wrote:
<snip>
>
>The pair programming invests both people, immersing them directly in. 
…[5 more quoted lines elided]…
>

That's the way that I understand it Ken, two brains, two sets of eyes
working on the same code. Each catching errors that the other would
have missed. Each contributing ideas realtime that the other would 
not have considered. It is a whole lot easier to suggest another 
approach when the other person has not invested hours doing it
their way. The two help keep each other focused on the task at
hand.

The XP folks claim that they produce higher quality code faster
this way and when completed two beople already understand the
code. On some projects I understand that they have a rule that
no solo produced code goes into production, they are that comitted
to the concept.

I can just see my CIO's face when I tell him I want to 
get rid of half of the work stations <g> and half of the staff is
going to be "sitting there" watching the others code <big grin>.

This does not work with two workstations side-by-side but what
about a workstation designed for pair programming? One monitor
but two keyboards/mice. This would make the handoff quicker, now
they say passing the keyboard is better than changing chairs. What
if you could say "Hey there's a typo, I'll get it, you keep coding."?
Would that help or hinder pair programming?

I've seen similar techniques work where the code/compile/test cycles
are short but can this work for COBOL? Seems to me that if we have
to wait a couple of minutes for a compile/link and 5-10 minutes for a
test run then you will quickly lose half of the pair?

Mike Myers
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C6AD3E.587EE34C@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net> <38C605F0.17C04B6B@home.com> <38C64B85.7DFD9F6C@zip.com.au> <38c6874b.13023511@news.clt.bellsouth.net>`

```


Mike Myers wrote:
> 
> This does not work with two workstations side-by-side but what
…[4 more quoted lines elided]…
> Would that help or hinder pair programming?

That's not a daft idea. Not something I do, but even on one screen I
think I can load two versions of the source. So, we are back to your two
monitors - but not impossible for both to have access to the one source,
albeit they are separate versions. And given an editor which logs timed
backups - the idea might work quite effectively.....? 

A parallel to the above is that NetExpress from the IDE lets me load the
source. Then I can jump into Microsoft Programmer's Workbench (DOS text
based) where I do 90% of my work. Then I 'save' in PWB and return to N/E
which shows me its version - and prompts "program changed outside N/E -
do you want to re-load ?"
 
Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c73300.8113954@news.cox-internet.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net> <38C605F0.17C04B6B@home.com> <38C64B85.7DFD9F6C@zip.com.au> <38c6874b.13023511@news.clt.bellsouth.net>`

```
On Wed, 08 Mar 2000 17:32:49 GMT, mike_myers@bellsouth.net (Mike
Myers) wrote:

>That's the way that I understand it Ken, two brains, two sets of eyes
>working on the same code. Each catching errors that the other would
…[5 more quoted lines elided]…
>

I really wasn't going to get in on this thread - I promise.  I have
done this at the DESIGN stage quite often. And do today with my boss.
But if the design is properly handled, the coding is simply clerical.
I don't think what I do fits the XP paradigm, but I ALWAYS see the
benefits.
```

###### ↳ ↳ ↳ Re: XP: Extreme Programming

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C6AA0B.34FE6117@home.com>`
- **References:** `<38C0AFCB.1B6B5249@home.com> <38c5e713.5637531@news.clt.bellsouth.net> <38C605F0.17C04B6B@home.com> <38C64B85.7DFD9F6C@zip.com.au>`

```


Ken Foskey wrote:
> 
> Small talk is supported by an amazing programming editor.  It allows
…[3 more quoted lines elided]…
> pets take a walk and then you introduce fish).

Ken, sounds interesting this one - so can you illustrate it with COBOL
pseudo code - now remember - "What did Horace say Winnie ?".

>Jimmy,

>That's Bondi...

Close - but no cigar. But at least I didn't write Bonzai Beach :-) Is
that one of the beaches where your sheilas go topless. I might be
getting my pension cheque - but I can still look and enjoy, can't I ?
What was it Jimmy Carter said "You can sin/lust with the mind".. Come on
Judson, I betcha can give me the correct quote on that one.

> The pair programming invests both people, immersing them directly in.
> Those tricky discussions are nutted out on the spot (have you ever
> worked alone without a partner at all, bloody hard work).

Amen. I'm doing it all the time - and it is @$$!!@# hard. Living in this
EDP focal point I don't know one single COBOL hot-shot in downtown
Calgary - noticed how many people from Calgary have joined CLC - moi !
AND - that's why you got my source, so I could get some comment.

Still testing that dialog bit on one more program - then will send it.
Now that Thane's getting into the foray on OO, I'll include him too.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
