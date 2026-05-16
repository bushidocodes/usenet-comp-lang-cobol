[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Changing the CPU Regression Test

_8 messages · 6 participants · 2005-03_

---

### [OT] Changing the CPU Regression Test

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-03-02T17:11:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`

```
All.

Just a dumb question.

I work in an environement where they do somewhat silly things.  As an 
example : the code freeze.  This a period in the year around financial 
reporting where they "freeze" any code changes without special exemptions 
even code fixes that may prevent some problem from occurring. Ironically, 
this is a _good_ time to upgrade O/S, DBMS and CICS.

I have rationalized and accepted this.

But now I have a new one:
We are undergoing a CPU upgrade. The business group wants to run a pre and 
post test using the prior months data to validate that the same amounts and 
financial figures are calculated to ensure that a CPU upgrade didn't affect 
the output.
Now, I know that Intel had some floating point math errors - but what are 
the chance? Anyone have any idea why a CPU upgrade what affect COBOL math ?

This is Z/OS batch JCL environment....they also want to prove that the 
number of datasets produced before and after is the same......this one I'm 
_really_ struggling with.   I can only imagine that somewhere along the line 
that a SOX audit had left a comment on a dataset creation somewhere.  I'm 
beginning to really wonder whether the right people drive SOX into technical 
environments - I'm not sure how a finance graduate working for KPMG or the 
like understands an operating environment.

JCE
```

#### ↳ Re: [OT] Changing the CPU Regression Test

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-02T19:13:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JfoVd.3862239$f47.692287@news.easynews.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`

```
If in the change of CPU's they *also* change release levels of z/OS (or even 
POSSIBLY "maintenance" levels of z/OS) this can impact LE and LE run-time 
options.  Therefore, some of what they are talking about MIGHT change - if the 
upgrade was not done "correctly".

That's the best that I can think of.

P.S.  even the number of datasets could change if they don't keep the same 
CBLQDA run-time setting.
```

##### ↳ ↳ Re: [OT] Changing the CPU Regression Test

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-03-03T07:02:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rEyVd.98501$pc5.80299@tornado.tampabay.rr.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com> <JfoVd.3862239$f47.692287@news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:JfoVd.3862239$f47.692287@news.easynews.com...
> If in the change of CPU's they *also* change release levels of z/OS (or 
> even POSSIBLY "maintenance" levels of z/OS) this can impact LE and LE 
> run-time options.  Therefore, some of what they are talking about MIGHT 
> change - if the upgrade was not done "correctly".

This was one of my concerns, but a source tells me that this is _just_ a 
processor.  The z/OS upgrades are scheduled for later.
And, the chances of "correctly" are slim - at one point the "plan" was to 
switch the machine off, replace it, turn it on.

They didn't consider any of the implications of _just_ switching it off.

This may have answered my question: maybe the level of trust they have in 
the support team is the same as mine :-)

I feel better now though because if there were weird "math" options that had 
processor dependencies, you, of all people, would have pointed this out :-)

> That's the best that I can think of.
>
> P.S.  even the number of datasets could change if they don't keep the same 
> CBLQDA run-time setting.
They are talking of "real" output datasets created and part of our asset 
list.  I'm not sure how they fathom this would change.

JCE

> -- 
> Bill Klein
…[32 more quoted lines elided]…
>> JCE
```

#### ↳ Re: [OT] Changing the CPU Regression Test

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-03-03T12:45:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38n1g5F5on4a4U1@individual.net>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`

```
I don't think this is 'silly'...

Whether there is minimal or no technical risk involved or not, it will
simply make everybody feel better. How can that be bad?

Of course, if it involves setting up hundreds of datasets and a lot of
effort, then I can see how you might baulk a bit.

Why not take an image backup of the current datasets (you probably have
anyway), restore last month's environment, re-run on the new processor, get
the outputs, then restore the current environment?

It's a lot of work, but the system (not you... :-)) has to do it (mainly as
batch), and some of it has probably already been done as part of SOP.

Good chance to test disaster recover procedures while you're at it :-)

Pete.

TOP POST no more below.

"jce" <defaultuser@hotmail.com> wrote in message
news:7tmVd.123989$qB6.32044@tornado.tampabay.rr.com...
> All.
>
…[12 more quoted lines elided]…
> post test using the prior months data to validate that the same amounts
and
> financial figures are calculated to ensure that a CPU upgrade didn't
affect
> the output.
> Now, I know that Intel had some floating point math errors - but what are
> the chance? Anyone have any idea why a CPU upgrade what affect COBOL math
?
>
> This is Z/OS batch JCL environment....they also want to prove that the
> number of datasets produced before and after is the same......this one I'm
> _really_ struggling with.   I can only imagine that somewhere along the
line
> that a SOX audit had left a comment on a dataset creation somewhere.  I'm
> beginning to really wonder whether the right people drive SOX into
technical
> environments - I'm not sure how a finance graduate working for KPMG or the
> like understands an operating environment.
…[4 more quoted lines elided]…
>
```

#### ↳ Re: [OT] Changing the CPU Regression Test

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-03-02T19:08:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2e665$42266386$45491f85$9532@KNOLOGY.NET>`
- **In-Reply-To:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`

```
jce wrote:
> We are undergoing a CPU upgrade. The business group wants to run a pre and 
> post test using the prior months data to validate that the same amounts and 
…[11 more quoted lines elided]…
> like understands an operating environment.

I've never worked in that environment, but I have a feeling that if I 
had, it wouldn't change the speculative nature of my reply.  :)

One thing we found when we place our system on different hardware is 
that the slowness of our hardware actually allowed us to get away with 
things that the new hardware, being fast and all, didn't.  It's not a 
bad idea - unless you're not paid by the hour.  ;)
```

##### ↳ ↳ Re: [OT] Changing the CPU Regression Test

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-03-02T22:31:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<112d4oderk0gk8e@news.supernews.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com> <2e665$42266386$45491f85$9532@KNOLOGY.NET>`

```
LX-i wrote:
>
> I've never worked in that environment, but I have a feeling that if I
…[5 more quoted lines elided]…
> bad idea - unless you're not paid by the hour.  ;)

I once heard about an engineer who had a piddly Fortran program he needed to 
run about once a week. It only took two minutes, but without its output he 
was dead in the water.

Thing was, since his job was so insignificant, he kept getting automatically 
pushed to the back of the queue. Sometimes it was DAYS before his little job 
was done.

He created a subprogram to compute the inverse of a giant matrix. Burned up 
an immense amount of CPU cycles. This had the amazing effect of bumping his 
job to the head of the queue! Other engineers wondered how he was able to 
get such high priority. He began to share his subprogram. Soon all the 
engineers were happy, but management was going nuts, what with all the 
increased computer demands.

Management ordered a newer, faster computer.

Shortly it arrived and there were CPU cycles for everyone. The engineers, no 
longer having a need for a cycle-eater, removed the subprogram from all 
their submission. CPU time and wall-clock time plummeted.

The computer manufacturer re-wrote their sales brochures for the new machine 
(and raised the price).

Everyone was happy.
```

##### ↳ ↳ Re: [OT] Changing the CPU Regression Test

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-03-03T07:02:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qEyVd.98500$pc5.28504@tornado.tampabay.rr.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com> <2e665$42266386$45491f85$9532@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:2e665$42266386$45491f85$9532@KNOLOGY.NET...

> One thing we found when we place our system on different hardware is that 
> the slowness of our hardware actually allowed us to get away with things 
> that the new hardware, being fast and all, didn't.  It's not a bad idea - 
> unless you're not paid by the hour.  ;)

This happened our last upgrade - turns out that somewhere we had code 
generating unique keys from the full timestamp.  The new cpu let us get two 
to three of the same generated key per transaction.  I hope that the 
solution that someone added was not to add an extra PERFORM 
DO-STUFF-TO-WASTE, but in this world, who knows?  :-)

But nice idea, and may have been a consideration

JCE
```

#### ↳ Re: [OT] Changing the CPU Regression Test

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2005-03-04T11:27:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<na0Wd.28990$7K3.4928@fe08.lga>`
- **In-Reply-To:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`
- **References:** `<7tmVd.123989$qB6.32044@tornado.tampabay.rr.com>`

```
An interesting position. Between a rock and a hard place.
Internal audits prevent failures by external auditors. They
seem costly, and unnecessary.]

I remember one time when an employee did an audit on the incentive
calculation to verify a paycheck.

Short story, the payroll program had been making this mistake for
years. It was not a simple task to go back, and re-calculate the
correct amount for everyone under that plan, and clean up the
books by paying everyone what they should have.  All because,---
who do you point to here? The IE's created the rate tables,
the systems turned it into a program, and many people were paid
wrong for a long time. The  internal auditors had not caught it.
Extreme caution seems silly, but......  calculate the cost of
not doing the audit in the first place.

Warren


jce wrote:

> All.
> 
…[28 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
