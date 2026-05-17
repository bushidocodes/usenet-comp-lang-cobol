[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Why are C and C++ so popular?

_9 messages · 9 participants · 1996-09_

---

### Why are C and C++ so popular?

- **From:** "wrow..." <ua-author-42018@usenetarchives.gap>
- **Date:** 1996-09-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50sm8f$rru@newsbf02.news.aol.com>`

```

Why are C and C++ so popular?

Even their best friends, of which I am one, do not consider C and C++
easy to learn or to use. And yet by any reasonable measure (ie actual
statistics, not personal anecdotes or isolated examples quoted without
basis for comparison) they are among the most widely used languages at the
present time. Take a look at the newsgroup ba jobs.offered. (jobs offered
in the California Bay Area).
What has led to their ascendancy? I would argue that they have become
popular for general use not in spite of their difficulty but paradoxically
because of it.

For a language to become successful, it must be attractive to project
managers and CIOs; it is not enough that programmers like it. For this to
be so, it must have a track record of success.

In 1993 Herrnstein and Murray published "The Bell Curve", which instantly
became notorious for its treatment of race and IQ. However, the
disregarded first 70% of the book does not touch on race explicitly and
presents some interesting results concerning, among other things, the
relationship between IQ and job performance.
H&M conclude, based on an analysis of the vast US Military training and
job performance database, that the principle factor (in the sense of
providing the highest percentage of "explained variation") in effective
job performance is intelligence, not training or experience. Other studies
they quote show that the best measure of a job applicant could be obtained
from an IQ test, not from references or interview or by considering
educational performance (in the US, IQ tests for job applicants have been
illegal since 1971). These results were found to apply even to occupations
that require low cognitive ability, but the correlation improved with jobs
of higher intellectual difficulty, of which programming is of course one.

C and C++ are inherently difficult languages. An average person could not
master them. But bright people can and some are attracted by the challenge
of using them.
Therefore a project manager s choice of C or C++ is equivalent to raising
the IQ threshold for entry into his project, whereas the choice of COBOL
or PL/I, which for business purposes can be easily mastered by almost
anyone, lowers it.
As a result, C and C++ projects have a higher concentration of brainpower,
and, because of the correlation between IQ and job performance, are
therefore more likely to be successful.

Bill Rowe.
```

#### ↳ Re: Why are C and C++ so popular?

- **From:** "soft..." <ua-author-6881452@usenetarchives.gap>
- **Date:** 1996-09-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<50sm8f$rru@newsbf02.news.aol.com>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com>`

```

WRowe0521 (wro··.@a··.com) wrote:
: Why are C and C++ so popular?

C came along at the time when people were looking for alternatives to
writing systems software in assembly language (because hardware was
getting very diverse -- you can't write everything in 360 assembler if
you have multiplatform workstations), and UNIX's penetration into the
universities created a bunch of C programmers. These came into the
work world at the time the PC took off, with its HUGE market for
software, creating a big demand for C compilers on the PC. With C's big
time penetration in the PC market, it spread to become the de facto
language for everything and migrated backwards to platforms like MVS. C
is probably the only language that has migrated *backwards* like that!
Others start on big platforms and work down (PL/I, REXX, etc).

: C and C++ are inherently difficult languages.

The fact about C is that systems programmers created it for systems
programming. It is very well suited for low-level programming. This
isn't for everyone, certainly, but if you have to do that sort of stuff
you need that kind of language. Other languages are too artificial and
not practical.

C isn't perfect or great for all applications, but it's so general
purpose and widely available on every platform the temptation is to use
it.

Scott
```

#### ↳ Re: Why are C and C++ so popular?

- **From:** "dma..." <ua-author-11660218@usenetarchives.gap>
- **Date:** 1996-09-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<50sm8f$rru@newsbf02.news.aol.com>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com>`

```

I think that what you are saying is partly true. But I think also
that project managers want to prove that they are "real men", or
in a few cases "real women", by selecting C/C++ as their project's
language. The project manager that chooses C/C++ gets to make a
name for himself by barking at other project managers that his system
is written in C or C++.

Also, C and C++ were helped a lot by Microsoft. In a few ways, Pascal
is an easier language to look at and work with, but 8 or so years
ago Borland already had a hot Pascal compiler out, and Microsoft
wanted to try to proove they were cool too by coming out with a really
great C compiler.

Take a look over in the Pascal language newsgroup. The people over
their regularly complain about C and C++'s success. It's: "our
language is better, so why is their language doing so much better ?"

Of course, COBOL is also a really great language, but it's not cool
enough for some project managers' tastes. The project manager that
says he's writing his new system in COBOL doesn't look so cool,
even if he has made a pretty good choice.

And then, as has been said before, a dozen times, C and C++ are
good for some things. And COBOL is good for some other things.

WRowe0521 (wro··.@a··.com) wrote:
› Why are C and C++ so popular?
 
› Even their best friends, of which I am one,  do not consider C and C++
› easy to learn or to use. And yet by any reasonable measure (ie actual
…[6 more quoted lines elided]…
› because of it.
 
› For a language to become successful, it must be attractive to project
› managers and CIOs; it is not enough that programmers like it. For this to
› be so, it must have a track record of success. 
 
› In 1993 Herrnstein and Murray published "The Bell Curve", which instantly
› became notorious for its treatment of race and IQ. However, the
…[12 more quoted lines elided]…
› of higher intellectual difficulty, of which programming is of course one.
 
› C and C++ are inherently difficult languages. An average person could not
› master them. But bright people can and some are attracted by the challenge
…[7 more quoted lines elided]…
› therefore more likely to be successful. 
 
› Bill Rowe.
```

##### ↳ ↳ Re: Why are C and C++ so popular?

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fa42bfbb8-p3@usenetarchives.gap>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com> <gap-1fa42bfbb8-p3@usenetarchives.gap>`

```

David Mazeau wrote:
: Of course, COBOL is also a really great language, but it's not cool
: enough for some project managers' tastes. The project manager that
: says he's writing his new system in COBOL doesn't look so cool,
: even if he has made a pretty good choice.

I like the challenge of doing 'C'-type things in C, and would just as
soon avoid doing that kind of thing in COBOL. But anytime I start
doing a job in C, I have to remind myself that I may spend hours chasing
a bad pointer, or implementing something that's a no-brainer in COBOL.
And I like Perl for a limited set of pattern-matching or text processing
jobs. There are some jobs I wouldn't think of doing in COBOL, or
wouldn't think of doing _again_ in COBOL.

Recently someone came to me for advice on the Unix 'sed', 'cut', 'paste',
and other shell-level commands by which he could convert one fixed format
into another. The data came from a COBOL system. I asked him, do you
have the FD for either of these files? (He was a seasoned Honeywell COBOL
programmer.) Within about 20 minutes I had introduced him to Micro Focus
on Unix, and we'd hacked out his solution.

...But when he took this back to the incredibly expensive consultant
company that has been "leading" our company into the client/server world
(at a substantial increase in staffing and equipment costs), they vetoed
his COBOL solution, saying they did not want to pollute the new
application. They scrapped it and helped him to re-implement in SQL.
It probably runs at 1/4 the speed of the COBOL.

But I've seen C run 5 times faster than COBOL for certain small tasks,
because simple C can translate into some very tight machine operations.
If response time and memory size were REALLY important, I'd tend to use C.
But I've only encountered one case where COBOL was too slow, and never has
it been too big. So I tend to choose COBOL by default, except for certain
little character-pushing tasks, and tasks where I'm using a lot of Unix
system calls -- in some of these cases C just "says it better" than COBOL
can. It's a very limited corner of the work that I do.

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

#### ↳ Re: Why are C and C++ so popular?

- **From:** "kalpataru barman" <ua-author-17071492@usenetarchives.gap>
- **Date:** 1996-09-09T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<50sm8f$rru@newsbf02.news.aol.com>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com>`

```

WRowe0521 wrote:
› 
› Why are C and C++ so popular?
…[5 more quoted lines elided]…
› present time.   ^^^^^^^^^^^^^

Is this true ?
```

#### ↳ Re: Why are C and C++ so popular?

- **From:** "alc..." <ua-author-17086161@usenetarchives.gap>
- **Date:** 1996-09-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p6@usenetarchives.gap>`
- **In-Reply-To:** `<50sm8f$rru@newsbf02.news.aol.com>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com>`

```

On Sep 07, 1996 16:34:23 in article ,
'wro··.@a··.com (WRowe0521)' wrote:
› For a language to become successful, it must be attractive to project
› managers and CIOs; it is not enough that programmers like it. For this to
› be so, it must have a track record of success.

If you have documented evidence that project managers and CIO's know
more about what works than programmers, please share it with us. Would
also enjoy hearing from those who, like myself, believe that sometimes the
higher-ups prevail more because of their immediate access to the checkbook
than because of their objective analysis of the most cost-effective
solution.

› H&M conclude, based on an analysis of the vast US Military training and 
› job performance database, that the principle factor (in the sense of 
› providing the highest percentage of "explained variation") in effective 
› job performance is intelligence, not training or experience. 

While not disputing the "vastness" of the military's database one could
easily observe that that their results are somewhat below the arrogance
of their assumptions.
On a related subject, one could ask which would impress Saddam more:
a "high percentage of 'explained variation'" , or a high kill ratio.

› C and C++ are inherently difficult languages. An average person could not
› master them. But bright people can and some are attracted by the challenge
 
› of using them.

Wielding a johnny-mop encrusted with dried excrement is an "inherently
difficult" way to clean a commode. But few would argue that it is the best
way, just because it is difficult. Bright people would choose an easier
way.
I have often seen, and used, programs which offer conclusive proof that
average persons think they have mastered C and C++, when in fact they
have not. That's the most fatal pitfall of all: people who could have done
a great job are doing a lousy job, simply because they're trying to do it
the
hardest way possible.
A word of warning to those who will now flame me: I smell really bad
when I burn (my wife says that isn't the only time).
David Webber

My opinions are disgustingly similarly to those of my employer, because
I own the company.
```

##### ↳ ↳ Re: Why are C and C++ so popular?

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1996-09-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fa42bfbb8-p6@usenetarchives.gap>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com> <gap-1fa42bfbb8-p6@usenetarchives.gap>`

```

› On Sep 07, 1996 16:34:23 in article ,
› 'wro··.@a··.com (WRowe0521)' wrote:
…[3 more quoted lines elided]…
› 
The first answer to this dilemma, as I perceive it, begins with the
incredible marketing hype in the magazines. They portray a kind of
magic world where all your business solutions can be solved for very
little cost. The second problem contributing to this situation is that
unqualified individuals have weaseled their way into ITS positions,
creating whole new lucrative careeres for themselves. Far too many of
these types have no conception or background in large-scale,
mission-critical systems development and deployment. Most of the time,
ITS staff do no respect these individuals who direct these activities
because they did not earn the position they 'politiced' their way into.
But, unfortunately, they can impress the people who approve the use of
(and fund) the technology.

Politics and technology are a disasterous combination. I have seldom
seen success (except a self-proclaimed one) come out of this. I believe
this trend to be the greatest threat to the quality and effectiveness of
IT in general. The entire process is being trivialized by too many
individuals who memorize a few buzzwords and sound like the departmental
genuis to the boss.

mike dodas
```

###### ↳ ↳ ↳ Re: Why are C and C++ so popular?

- **From:** "james m. vines" <ua-author-3284547@usenetarchives.gap>
- **Date:** 1996-09-15T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fa42bfbb8-p7@usenetarchives.gap>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com> <gap-1fa42bfbb8-p6@usenetarchives.gap> <gap-1fa42bfbb8-p7@usenetarchives.gap>`

```

Michael Dodas wrote:
› 
›› On Sep 07, 1996 16:34:23 in article ,
 
› Politics and technology are a disasterous combination.  I have seldom
› seen success (except a self-proclaimed one) come out of this.  I believe
…[5 more quoted lines elided]…
› mike dodas


I have heard that IT would benefit if a law was passed outlawing COOs,
CEOs and CIOÂs from reading magazines on airline flights. :)

Really I've seen UNIX and c/c++ fanatics claim great things for their
tech. One of my good friends who has never programmed in a large scale
environment, tell me that COBOL was inferior to C/C++ because it was not
suitable for writing TP programs(at the system not application area).

I believe another friend hit the problem with the observation that
management is looking for a magic bullet because they are desperate.
The work needed exceeds the available resources. When zealots claims
that they can do it and staff says that we are in deep trouble who do
you think will win the argument in today's environment.

I was mainframe IMS support, transferred to a C/C++ OO group, saw
millions of $ spend with no direction, lots of talk, promises of pay
raises and promotions. After two years, CIO left, the group was
disbanded, I took a buyout offer. I expect to become a COBOL
contractor.

I have training and experience in both the UNIX and Main Frame
universes. IÂve training and experience in C++ and COBOL. My view is
that if you want to do systems programming, then C++ is best. For
business apps, COBOL is best. Smalltalk and Vbasic have their
places. The problem is zealots that claim universal usage for their
object of affection.

IÂve read article in both Fortune and Harvard Management Review
magazines that state that management has become too dependent on
consultants to make decisions. Management is not taking responsibility
for their decisions. This may be root of the problem. No consult is
going to bet rich recommending status quo.


Regards


Jim

The problem is either caused by the software or the hardware.
```

#### ↳ Re: Why are C and C++ so popular?

- **From:** "h..." <ua-author-509909@usenetarchives.gap>
- **Date:** 1996-09-21T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fa42bfbb8-p9@usenetarchives.gap>`
- **In-Reply-To:** `<50sm8f$rru@newsbf02.news.aol.com>`
- **References:** `<50sm8f$rru@newsbf02.news.aol.com>`

```


In article <5187ag$d.··.@nnr··t.com>, Victor Odhner (vod··.@pri··t.com) writes:
› soon avoid doing that kind of thing in COBOL. But anytime I start
› doing a job in C, I have to remind myself that I may spend hours chasing
› a bad pointer, or implementing something that's a no-brainer in COBOL.

Funny, but I recently spent two days chasing a bad memory reference
in Cobol that crept in when I was trying to implement something
that would have been a no-brainer in Pascal.

I was passing a variable-occurrence data item in a procedure CALL in
order to write just one procedure that would apply to strings of
various sizes. The compiler manual boldly claimed the compiler
would be smart enough to do everything within the limits of the
current size of that data item, but (as I eventually found out) a
reference modification proved just a little too much for it.

I was imitating passing a Pascal-style string as in

procedure MyProc(var MyString: string);

using a technique that was actually suggested by the compiler manual,

linkage section.
var MyString-Size byte.
var MyString.
public MyString-Char char(1),
occurs 0 to 255 times depending on MyString-Size.

procedure division using MyString-Size, MyString.

The one statement that turned out to be the one wreaking havoc
read something like

move AnotherString to MyString(Pad + 1:);

and after I changed that to

move AnotherString to MyString(Pad + 1 : MyString-Size - Pad);

the procedure finally does its job.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
