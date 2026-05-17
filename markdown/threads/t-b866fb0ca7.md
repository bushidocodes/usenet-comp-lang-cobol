[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Random cobol code generators

_17 messages · 6 participants · 2017-09_

---

### Random cobol code generators

- **From:** "pramodkdixit" <ua-author-14501826@usenetarchives.gap>
- **Date:** 2017-09-12T06:15:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com>`

```
Hello,

Like the C and the C++ where there is a random code generators, which based on a predefined algorithm, generates C code for various testing purposes,

Do we have something in COBOL where we can generate a cobol code randomly ?

Any help is appreciated.
```

#### ↳ Re: Random cobol code generators

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-09-12T08:10:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com>`

```
[posted and emailed]

In article ,
pramod kumar Dixit wrote:
› Hello, 
› 
…[4 more quoted lines elided]…
› Do we have something in COBOL where we can generate a cobol code randomly ?

Yes, it is called 'a programmer'.

Now please, do your own job.

DD
```

#### ↳ Re: Random cobol code generators

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2017-09-12T15:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com>`

```
On Tue, 12 Sep 2017 03:15:29 -0700 (PDT), pramod kumar Dixit
wrote:

› Hello, 
› 
…[4 more quoted lines elided]…
› Any help is appreciated.

Are you looking for the equivalent of something like this?

https://embed.cs.utah.edu/csmith/

Are you testing a COBOL compiler, or are you working on other tools
that read source code?

Louis
```

##### ↳ ↳ Re: Random cobol code generators

- **From:** "pramodkdixit" <ua-author-14501826@usenetarchives.gap>
- **Date:** 2017-09-13T05:41:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p3@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap>`

```
On Wednesday, September 13, 2017 at 1:07:58 AM UTC+5:30, Louis Krupp wrote:
› On Tue, 12 Sep 2017 03:15:29 -0700 (PDT), pramod kumar Dixit
›  wrote:
…[16 more quoted lines elided]…
› Louis

Thanks a lot Louis for getting the question and intent right.
Yes indeed. I was looking for something equivalent in the link.
I am testing cobol compiler and i need various instances of code with various combinations etc.

Do you have something like the above for cobol (irrespective of - in which language the code generator is written)

Thanks much in advance.
```

###### ↳ ↳ ↳ Re: Random cobol code generators

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2017-09-13T16:23:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p4@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap>`

```
On Wed, 13 Sep 2017 02:41:08 -0700 (PDT), pramod kumar Dixit
wrote:

› On Wednesday, September 13, 2017 at 1:07:58 AM UTC+5:30, Louis Krupp wrote:
›› On Tue, 12 Sep 2017 03:15:29 -0700 (PDT), pramod kumar Dixit
…[25 more quoted lines elided]…
› Thanks much in advance.

Unfortunately, I don't know of any random COBOL code generators. A
search for "cobol compiler test suite" did turn up these links, which
might be somewhat useful:

http://www.itl.nist.gov/div897/ctg/cobol_form.htm

http://www.tek-tips.com/viewthread.cfm?qid=260605

Out of curiosity, I downloaded csmith. It has about 43,000 lines of
C++ code.

One of the FAQs in its web page:

"Can Csmith be altered to emit programs in a language other than C or
C++? Not easily."

Are you working on a commercial compiler, or open-source?

Louis

Are you working on a commercial product (
Louis
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-09-14T10:46:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p5@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap>`

```
In article <1t0··8@4··.com>,
Louis Krupp wrote:
› On Wed, 13 Sep 2017 02:41:08 -0700 (PDT), pramod kumar Dixit
›  wrote:
…[11 more quoted lines elided]…
›››› Do we have something in COBOL where we can generate a cobol code randomly ?
 
› [snip]
 
› Are you working on a commercial product (

Someone who thought 'yes' might have responded with 'Please do your own
job.'

DD
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 5)_

- **From:** "pramodkdixit" <ua-author-14501826@usenetarchives.gap>
- **Date:** 2017-09-15T02:10:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p6@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap>`

```
On Thursday, September 14, 2017 at 8:16:35 PM UTC+5:30, doc··.@pa··x.com wrote:
› In article <1t0··8@4··.com>,
› Louis Krupp   wrote:
…[22 more quoted lines elided]…
› DD

Loius, Thanks for the info. Yes I do work for a commercial compiler on Nonstop platform.

Looks like I might need to start working on a code generator for cobol. Nonetheless, i was thinking not to reinvent the wheel and the world is so large.

DD - I am curious to know if you are always sarcastic or only when you reply to emails.
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-09-15T04:55:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p7@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap>`

```
On 15/09/2017 6:10 PM, pramod kumar Dixit wrote:
› On Thursday, September 14, 2017 at 8:16:35 PM UTC+5:30, doc··.@pa··x.com wrote:
›› In article <1t0··8@4··.com>,
…[30 more quoted lines elided]…
› 
LOL! You need to get to know the Doc; he has a heart of gold, and is a
valuable contributor to this community but sometimes he gets a bit
tetchy. His sardonic humour can be a bit off-putting to people who don't
know him; don't take it personally...

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 7)_

- **From:** "pramodkdixit" <ua-author-14501826@usenetarchives.gap>
- **Date:** 2017-09-21T13:18:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p8@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap> <gap-b866fb0ca7-p8@usenetarchives.gap>`

```
On Friday, September 15, 2017 at 2:25:21 PM UTC+5:30, pete dashwood wrote:
› On 15/09/2017 6:10 PM, pramod kumar Dixit wrote:
›› On Thursday, September 14, 2017 at 8:16:35 PM UTC+5:30, doc··.@pa··x.com wrote:
…[40 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

Thanks Pete. I am fine. You are right indeed!! Judging people by their email replies are wrong and more so without knowing whats running in their mind.
I Apologise for any hurt.
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 6)_

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2017-09-15T07:46:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p7@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap>`

```
On Thu, 14 Sep 2017 23:10:42 -0700 (PDT), pramod kumar Dixit
wrote:


› Loius, Thanks for the info. Yes I do work for a commercial compiler on Nonstop platform.
›
› Looks like I might need to start working on a code generator for cobol. Nonetheless, i was thinking not to reinvent the wheel and the world is so large.

Have you run your compiler on the NIST test suite?

If you absolutely have to have a COBOL equivalent of csmith, go for
it. If you don't have time to do that, and you're looking for
something where automation would make sense, I would consider
generating fields of varying PICTURE, USAGE and VALUE and verifying
that MOVE statements work as expected.

If I'm not mistaken, Nonstop is now an HP product, so my guess is that
you work for HP and you're trying to verify the COBOL compiler
mentioned here:

https://h20195.www2.hpe.com/V2/GetDocument.aspx?docname=4AA1-3643ENW

or you're working on a third-party product. In either case, you should
be able to get another compiler on a convenient platform to serve as a
reference.

Louis
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 7)_

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-09-16T20:27:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p10@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap> <gap-b866fb0ca7-p10@usenetarchives.gap>`

```
On 9/15/2017 6:46 AM, Louis Krupp wrote:
› On Thu, 14 Sep 2017 23:10:42 -0700 (PDT), pramod kumar Dixit
›  wrote:
…[25 more quoted lines elided]…
› 

Here's one place where you can download the NIST COBOL85 test suite.
It's about 26 megabytes when decompressed.

https://sourceforge.net/projects/open-cobol/files/nist/

I've run the NIST COBOL85 test suite several times when building
GnuCOBOL. The best results I've gotten are:

------ Directory Information ------- --- Total Tests Information ---
Module Programs Executed Error Crash Pass Fail Deleted Inspect Total
------ -------- -------- ----- ----- ----- ---- ------- ------- -----
NC 95 95 0 0 4393 0 4 1 4398
SM 17 17 0 0 291 0 2 1 294
IC 25 25 0 0 246 0 4 0 250
SQ 85 85 0 0 518 0 0 89 607
RL 35 35 0 0 1827 0 5 0 1832
ST 40 40 0 0 288 0 0 0 288
SG 13 13 0 0 310 0 0 0 310
OB 7 7 0 0 39 0 0 0 39
IF 45 45 0 0 733 0 0 0 733
DB 16 16 0 0 418 0 4 27 449
IX 42 42 0 0 507 0 1 0 508
------ -------- -------- ----- ----- ----- ---- ------- ------- -----
Total 420 420 0 0 9570 0 20 118 9708


There 420 test programs in 11 groups (for example, IX is for Indexed
Sequential files), and 9,708 test cases. GnuCOBOL 2.2 passes 9,570 of
9,708 test cases with no abends.

The problem is that it only tests for the 1985 COBOL Standard. I don't
believe it covers any of the Intrinsic Functions from the 1989 addendum,
nor any of the new features of the 2002 or 2014 COBOL standards.

But it might be a good place to start....

Kind regards,



http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-09-16T09:58:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p7@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap>`

```
In article ,
pramod kumar Dixit wrote:
› On Thursday, September 14, 2017 at 8:16:35 PM UTC+5:30, doc··.@pa··x.com wrote:
›› In article <1t0··8@4··.com>,
…[6 more quoted lines elided]…
›››››  wrote:
 
››››› [snip]
 
›››››› Do we have something in COBOL where we can generate a cobol code randomly ?
›› 
…[8 more quoted lines elided]…
› Nonstop platform.
 
› So... this is your job.
 
› Looks like I might need to start working on a code generator for cobol.
› Nonetheless, i was thinking not to reinvent the wheel and the world is
› so large.

That's strange. You are willing to let others duplicate your efforts so
you won't have to duplicate their efforts?

'I need to find (x) so I can do the job for which I am getting paid money,
please tell me, for free.'

'Did you look at (this)?'

'Yes, already looked, not a help.'

'Did you look at (that)?'

'Yes, already looked, not a help.'

'Did you look at (the other thing)?'

'Yes, already looked, not a help. How come so many people waste my time
with unhelpful answers?'

Compare that with:

'I need to find (x) so I can do the job for which I am getting paid money.
I have already done (this), (that) and (the other thing) and found them
unhelpful. Suggestions would be appreciated.'

› DD - I am curious to know if you are always sarcastic or only when you
› reply to emails.

When somebody (outside of merely asking the question) demonstrates
absolutely zero effort in ascertaining the solution I try to give back at
least double.

DD
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 7)_

- **From:** "pramodkdixit" <ua-author-14501826@usenetarchives.gap>
- **Date:** 2017-09-21T13:34:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p12@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap> <gap-b866fb0ca7-p12@usenetarchives.gap>`

```
On Saturday, September 16, 2017 at 7:28:13 PM UTC+5:30, doc··.@pa··x.com wrote:
› In article ,
› pramod kumar Dixit   wrote:
…[29 more quoted lines elided]…
› 
 
› DD

Hello Mr DD,

I am ready to take back double, and ofcourse got a few. I take your point below.

[SNIP]
› 'I need to find (x) so I can do the job for which I am getting paid money, 
› please tell me, for free.'
…[18 more quoted lines elided]…
› unhelpful.  Suggestions would be appreciated.'
[SNIP]

At the same time,
[snip]
› That's strange. You are willing to let others duplicate your efforts so
› you won't have to duplicate their efforts?
[snip]
Did I ever say "I shall NOT share" or has anyone asked if can share.

[snip]
› When somebody (outside of merely asking the question) demonstrates
› absolutely zero effort in ascertaining the solution I try to give back at
› least double.
[snip]
Just because I have not explained my past effort doesnt mean there hasnt been any and every one has to start from somewhere. I started here.
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 8)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-09-21T14:56:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p13@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p7@usenetarchives.gap> <gap-b866fb0ca7-p12@usenetarchives.gap> <gap-b866fb0ca7-p13@usenetarchives.gap>`

```
In article <25cdb178-24f1-4e15-bcc2-0b4··1@goo··s.com>,
pramod kumar Dixit wrote:
› On Saturday, September 16, 2017 at 7:28:13 PM UTC+5:30, doc··.@pa··x.com wrote:
 
› [snip]
 
›› That's strange.  You are willing to let others duplicate your efforts so 
›› you won't have to duplicate their efforts?
› [snip]
› Did I ever say "I shall NOT share" or has anyone asked if can share.

It has been said 'Actions speak louder than words'. Your actions showed
no inclination to letting people know what you'd already done and gave no
indication that this particular was anything other than one-way.

› 
› [snip] 
…[5 more quoted lines elided]…
› been any and every one has to start from somewhere. I started here.

Perhaps a lesson learned by doing so is that there are more fruitful ways
to order future searches.

DD
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-09-15T04:49:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p6@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap>`

```
On 15/09/2017 2:46 AM, doc··f@pa··x.com wrote:
› In article <1t0··8@4··.com>,
› Louis Krupp   wrote:
…[21 more quoted lines elided]…
› 

I was surprised at this, Doc.

Who you help or don't, is, of course, entirely a matter for you, but
this seems uncharacteristically ungenerous, to me.

The fact that somebody may be working on something that is (or will be )
commercial, doesn't necessarily mean they are already coining it and can
afford to pay for advice.

The days when kids came here looking for help with "homework" are pretty
much over, I think (haven't seen any such requests for over a decade now...)

He IS "doing his own job" by looking for help.

I do the same, and I try and help other people who need help that I can
provide. It isn't always about money.

I believe you Americans have a term for it, something about going around
and coming around... Perhaps I misunderstood it or it may have been lost
in translation...

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Random cobol code generators

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-09-16T10:33:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p15@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap> <gap-b866fb0ca7-p5@usenetarchives.gap> <gap-b866fb0ca7-p6@usenetarchives.gap> <gap-b866fb0ca7-p15@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 15/09/2017 2:46 AM, doc··f@pa··x.com wrote:
›› In article <1t0··8@4··.com>,
…[27 more quoted lines elided]…
› this seems uncharacteristically ungenerous, to me.

Zero effort shown, Mr Dashwood, at least double returned. How's that not
largesse?

› The fact that somebody may be working on something that is (or will be )
› commercial, doesn't necessarily mean they are already coining it and can
› afford to pay for advice.

The fact that someone's working on it shows that someone's boss assigned
the task... despite voluminous, vociferous protestations of 'I cannot do
this, I do not know how to do this, if you assign this to me you are
dooming this task to nigh-certain failure.'

Who am I to prove a boss wrong?

[snip]

› I believe you Americans have a term for it, something about going around
› and coming around... Perhaps I misunderstood it or it may have been lost
› in translation...

They certainly do speak an odd language in the Antipodes, Mr Dashwood...
how about 'Give a person a something in COBOL where we can generate code
randomly, feed them for a day... teach a person how to demonstrate effort
which deserves co-operation and get them to a position high enough so they
can sign off on invoices, feed more people for a longer time.'?

DD
```

###### ↳ ↳ ↳ Re: Random cobol code generators

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2017-09-19T10:24:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b866fb0ca7-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b866fb0ca7-p4@usenetarchives.gap>`
- **References:** `<f120c8ee-a4fb-493b-999a-3c6251199a3a@googlegroups.com> <gap-b866fb0ca7-p3@usenetarchives.gap> <gap-b866fb0ca7-p4@usenetarchives.gap>`

```
On Wednesday, September 13, 2017 at 7:41:10 PM UTC+10, pramod kumar Dixit wrote:
› On Wednesday, September 13, 2017 at 1:07:58 AM UTC+5:30, Louis Krupp wrote:
›› On Tue, 12 Sep 2017 03:15:29 -0700 (PDT), pramod kumar Dixit
…[23 more quoted lines elided]…
› Do you have something like the above for cobol (irrespective of - in which language the code generator is written)

George Marsaglia's algorithms might be of interest.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
