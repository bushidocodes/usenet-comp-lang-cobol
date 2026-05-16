[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Odd doings in California

_70 messages · 12 participants · 2008-09_

---

### Odd doings in California

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-09-04T23:17:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nq2wk.36210$Rs1.36033@newsfe08.iad>`

```
Interesting article in the Aug. 18 issue of E-week (I get it some weeks
late), page 47; seems that Arnie and State Controller Chiang are at odds:
Schwartzenegger recently signed an executive order cutting the pay of
200,000 state workers to minimum wage levels as a way of forcing the state
legislature to approve a budget (now more than a month into the fiscal
year).

Chiang has said it can't be done.  He isn't refusing, but says it's
impossible "because of the age of the state's payroll system which is based
on Cobol, it would take at least six months to reconfigure the system to
send out those new minimum-wage checks".

That's a bunch of bs and nonsense - or deliberate bafflegab.  The age of the
system per se has nothing to do with it: conceivably it is loaded with
bolt-ons and fixes, which is what he may really mean.  (Nor, of course, is
the language to blame).  But surely there have been mass rate changes in the
past - as in a new contract - and there must be people who work with the
code base.  Has he never heard of quick-&-dirty fixes?

He adds this: "then, when the order is reversed and those 200,000 can go
back to getting regular pay, it would take another 10 months or so to get
the system back to where it was".  Again - bs!  If it took 6 months to learn
the system well enough to do the first change, those involved would then
know enough to reverse the change in a much shorter period than 6 months:
unless they are all fired after the first change! If Arnie really believes
this he should farm out the entire system to somebody (who does payrolls?)
and fire Chiang and whoever is advising him!

The story concludes with a description of IBM's determination to train
this-generation programmers in its mainframe technologies, including Cobol.
They are doing much business on the mainframes and the figure is growing.

If anybody can reverse the decline of Cobol, it's IBM!

PL
```

#### ↳ Re: Odd doings in California

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-04T23:44:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad>`

```
On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <lacey@mts.net> wrote:

>Chiang has said it can't be done.  He isn't refusing, but says it's
>impossible "because of the age of the state's payroll system which is based
>on Cobol, it would take at least six months to reconfigure the system to
>send out those new minimum-wage checks".

Recruit, hire and train contractors: 30 days
Analysis: 30 days
Setup test environment: 30 days
Development -- change programs: 2 days
Unit testing: 28 days
System testing: 30 days
Regression testing: 14 days
Production build and deployment: 7 days
Dress rehersal and spot checks: 14 days
Obtain approvals:  7 days

Total 6.5 months
```

##### ↳ ↳ Re: Odd doings in California

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T09:58:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9qvrn$l8n$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>`

```
In article <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <lacey@mts.net> wrote:
>
…[8 more quoted lines elided]…
>Development -- change programs: 2 days

Not... really.  This is Payroll, remember... civil-service payroll, at 
that, and my own recent, small experience shows that there are intricacies 
which might be a bit more demanding than a universal MOVE LS-MIN-WAGE TO 
D431652-EMP-MSTR-PRIM-SAL.

For instance... what about savings-plans contributions?  It is not 
difficult to imagine that during a bout of contract-negotiations it was 
decided that if your salary grade is CS-12 or higher then you can opt to 
have $y/pay periodof your hour-rate equivalent put into the savings 
plan, not to exceed n%, a sort of minimum-participation amount of pre-tax 
income.

If the grade is high enough the minimum contribution can, quite easily, 
exceed the current minimum wage... so the situation arises where you are 
cut a negative-sum check.  True, a few folks might believe this is what 
many civil servants deserve... but there might be a law or two that stands 
in the way.

There are all kinds of 'if you are in this plan your participation must be 
at least (y%) or (WS-CODED-AMT) or a hardcoded figure'... AND the payroll 
system is not working in vacuo; files are sent to the local authorities, 
the Fed, savings/investment plan providers and each and any of those might 
have range checking to insure integrity of data... 'Hmmmmm, the delta on 
this guy's gross is -93.683%, that can't be right, let's call Jimmy and 
see if the file format changed'.

Then there are the 'gamings' of the system... is an employee's on-call 
rate the same as their new minimum-wage salary?  Some people are 
accustomed to carrying pagers and being ready, at a moment's notice, to 
wade into a 2:am ABEND... others, with a few years under their belts, may 
have negotiated a salary clause along the lines of 'unless I can be 
stinking, blind, passed-out drunk then I am on *your* time and you'll pay 
me at least ($z/hr or percentage of salary, whichever is greater) for 
it'... and I have seen timecards submitted showing forty hours of Annual 
Leave Taken along with 148 hours of On-Call Hours... because they were 
doing an upgrade, you know, and Linda - you know, the one the boss likes 
to watch as she passes? - Linda gets to bill for On-Call Hours during 
upgrades and nothing in the contract says she *can't* bill for them while 
she's on leave...

... and it goes on... and then there's the little matter of reversing and 
auditing the changes once the brou-ha-ha is over... *and* maintaining a 
full Production load while all this is going on.  The 'all ya gotta do is' 
approach is quite Managerial, I'll agree... and it might even be a good 
thing, in this case, since if God or the Devil or both are in the details 
then it looks like there's a healthy separation of Church and State.

Seems like I mentioned something about this a few years back... ahhhhh, 
there you go, from 
<http://groups.google.com/group/comp.lang.cobol/msg/2a6d8995317b7e78?dmode=source> 
(appropriately enough bearing the Subject: Re: Modernization of COBOL 
Applications)

--begin quoted text:

Let me sing this back to see if I'm learning the song.

1) Initiate customer update request.
    A) Does the initiating user have any customer update authority?
        i) No - send 'not you, buddy' notice and terminate transaction
        ii) Yes - CONTINUE.

2) Prepare to and accept user input to identify customer for update.

3) Validate input
    A) is input in valid format (all letters/numbers in the right places)?
        i) No - send 'bad format' message and GO TO 2)
        ii) Yes - see if customer exists in system
            a) No - send 'not here - re-enter or use A)dd function'
                    and GO TO 2)
            b) Yes - does user have auth to update this class of customer?
                1) No - send 'lowly peon' msg and GO TO 2
                2) Yes - CONTINUE

4) Prepare to and accept user input to modify identified customer.

5) Validate input
    A) is input in valid format (codes entered are valid update types)?
        i) No - send bad code(s) msg and GO TO 4)
        ii) Yes - are codes valid for this kind of customer?
            a) No - send 'not for this one, you don't' msg and GO TO 4)
            b) Yes - send 'are you sure?' msg and get response
                1) is response valid?
                    A) No - send 'Y/N, please?' msg and GO TO 5.A.ii.b
... etc.

Now... the question of 'the extraction of business rules' and 'the 
extraction of logic rules' is where it gets sticky.  Take the example of 
an insurance-claims system.  It seems logical and businesslike to allow 
for a claim to be made for the treatment of uterine infections... BUT NOT 
if the policy's group doesn't have a rider to cover such treatments...

... then it's OK... BUT NOT IF the claimant is a male...

... BUT IF the claimant is a male who has a female relative who is also 
covered by the policy then it's OK...

... BUT NOT IF the claimant is a male who has a female relative who is 
also covered who has had a hysterectomy...

... BUT IF the claimant is a male who has a female relative who is also 
covered who has had a hysterectomy AND the date of the hysterectomy is 
greater than the date of the uterine infection treatment (someone left the 
claim in a drawer for six months) then it's OK...

... BUT NOT IF the claimant is a male who has a female relative who is 
also covered who has had a hysterectomy AND the date of the hysterectomy 
is greater than the date of the uterine infection treatment (someone left 
the claim in a drawer for six months) AND the date of the uterine 
infection treatment precedes the effective date for policy's rider which 
covers such treatments...

... et and cetera.  I think I'll stop now.

(note to newbies - it might be helpful to keep situations like this in
mind the next time you ask 'why would *anyone* code an IF statement that
goes on for four-and-a-half pages of greenbar?')

(addendum to note to newbies - if you need to then ask a Local Geezer
'What is 'greenbar'?') 

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** donald tees <donaldtees@execulink.com>
- **Date:** 2008-09-05T08:06:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net>`
- **In-Reply-To:** `<g9qvrn$l8n$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>,
> Robert  <no@e.mail> wrote:
…[57 more quoted lines elided]…
>

You missed the 5000 lines of code dealing with specific amounts coming 
out of specific funds ... you know, where 3.75 an hour of Joe's salary 
is allocated to state funding, but 2.25 is federal program 167-A53-z, 
from back in 1915, and 1.50 an hour comes out of capital, because the 
1915 program is still considered new. And that those have to add up 
correctly to the contract amount ... which does not exist, but is still 
set to last years.

Donald
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-05T07:13:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net>`

```
"donald tees" <donaldtees@execulink.com> wrote in message 
news:PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net...
> docdwarf@panix.com wrote:
>> Then there are the 'gamings' of the system... is an employee's on-call 
>> rate the same as their new minimum-wage salary? [...]
>> 1915 program.....

So much concern about these details that nobody has identified the 
fundamental problem here:

Government is too big and simply has to pay too many people.

MCM
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-05T08:18:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u6a2c4p73t41c0v0s8ptsv97qeuq72anh5@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net> <2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com>`

```
On Fri, 5 Sep 2008 07:13:15 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:

>"donald tees" <donaldtees@execulink.com> wrote in message 
>news:PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net...
…[8 more quoted lines elided]…
>Government is too big and simply has to pay too many people.

Every industry goes through a consolidation phase in which stronger states acquire weaker
ones. Thus, governmental efficiency improves through elimination of redundant employees
and products. 

Texas governor Rick Perry announced the acquisition of California will be final 4Q 2008,
subject to FTC and taxpayer approval. He cited synergies between their scenery and his
state's capitalization. In a similar vein, New York has begun preliminary talks with
Florida.

To defend against predatory acquisition (hostile takeover), northeastern states will be
forming the New England Union in 2010. The sole holdout is maverick New Hampshire, which
is pursuing a joint venture with Montana. Industry analysts think such a partnership is
unlikely. Sensing vulnerability, Canada will soon open an embassy in Nashua. A Canadian
spokesman said, "It's a natural, given their high tech and our cheap labor."

Wyoming filed Chapter 7 bankruptcy last month.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2008-09-05T11:27:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45j2c4d2cesjv90nm66i5cuokmu6a4dajp@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net> <2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com> <u6a2c4p73t41c0v0s8ptsv97qeuq72anh5@4ax.com>`

```
On Fri, 05 Sep 2008 08:18:19 -0500, Robert <no@e.mail> wrote:

>On Fri, 5 Sep 2008 07:13:15 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:
>
…[27 more quoted lines elided]…
>Wyoming filed Chapter 7 bankruptcy last month. 

I doubt that.  Chapter 7 is for personal bankruptcy and  is total
bankruptcy which stays on your credit report for 10 years. Chapter 13
Bankruptcy, more like a payment plan, stays on your credit report for
7 years. Chapter 11 is more like a reorganization and is used by
corporations and sole proprietorships.  

Municipalities, i.e. cities and states, could file bankruptcy under
Chapter 9 only.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I'm addicted to placebos. I'd give them up, but it wouldn' make
any difference."
-- Steven Wright
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-05T08:15:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1nf2c41edit7uq3d4bmun9tnmjjqlh9183@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net> <2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com>`

```
On Fri, 5 Sep 2008 07:13:15 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>>> Then there are the 'gamings' of the system... is an employee's on-call 
>>> rate the same as their new minimum-wage salary? [...]
…[5 more quoted lines elided]…
>Government is too big and simply has to pay too many people.

How does that change how long it would take to implement a coding
change?
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T21:59:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sa34$a2j$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net> <2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com>`

```
In article <2m9wk.12276$vn7.5678@flpi147.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"donald tees" <donaldtees@execulink.com> wrote in message 
>news:PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net...
…[8 more quoted lines elided]…
>Government is too big and simply has to pay too many people.

Too big/too many as compared to a size determined by what method?

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T22:51:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sd62$mtb$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net>`

```
In article <PpKdnR5-U_d5vVzVnZ2dnUVZ_u6dnZ2d@golden.net>,
donald tees  <donaldtees@execulink.com> wrote:
>docdwarf@panix.com wrote:
>> In article <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>,
…[17 more quoted lines elided]…
>> For instance... what about savings-plans contributions?

[snip]

>> ... and it goes on... and then there's the little matter of reversing and 
>> auditing the changes once the brou-ha-ha is over... *and* maintaining a 
…[12 more quoted lines elided]…
>set to last years.

Mr Tees, I've tried to answer a couple of other posts on this matter... 
but I believe that I am seeing evidence of who, exactly, has spent much 
time dealing with actual Civil Service pay systems and who hasn't.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-05T08:14:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com>`

```
On Fri, 5 Sep 2008 09:58:15 +0000 (UTC), docdwarf@panix.com () wrote:

>Now... the question of 'the extraction of business rules' and 'the 
>extraction of logic rules' is where it gets sticky.  Take the example of 
…[4 more quoted lines elided]…
>... then it's OK... BUT NOT IF the claimant is a male...

Now why would a computer program need to disallow uterine treatments
for males?

I suppose fraud analysis can be done within the standard claim
programs, but is that a good design?
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-05T10:13:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X_bwk.12288$vn7.9024@flpi147.ffdc.sbc.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com>`

```
 "Howard Brazee" <howard@brazee.net> wrote in message 
news:3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com...
> On Fri, 5 Sep 2008 09:58:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[12 more quoted lines elided]…
> programs, but is that a good design?

Speaking from experience, this particular situation is treated as a "data 
entry error"  (procedure code inconsistent with the patient's gender, 
standard remittance adjustment reason code value =7), not as an attempt to 
defraud.   The claim is processed and paid less the charges submitted for 
this service line.

Also speaking from experience, fraud analysis is a whole 'nother thing, and 
at least where your tax dollars are concerned (Medicare), I will guarantee 
you fraud WILL be detected, but it takes a while.

If you want to commit Medicare fraud, you can depend on some time where 
things will be good for you, but you better have your travel plans ready to 
move somewhere without an extradition agreement.

MCM
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T22:32:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sc29$87u$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com>`

```
In article <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Fri, 5 Sep 2008 09:58:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[9 more quoted lines elided]…
>for males?

I don't recall seeing where it was stated that a computer program was 
allowing or disallowing the situation quoted above; the situation was 
given in order to show where things get sticky in the question of 'the 
extraction of business rules' and 'the extraction of logic rules'.

>
>I suppose fraud analysis can be done within the standard claim
>programs, but is that a good design?

That would depend on the criteria one uses for good, I would say... how 
much work does one want the machine to do versus how much work does one 
want a human being to do being one of the points of measure.

For example... in the case given above, males - usually - do not have 
female reproductive organs and, as such, usually require little treatment 
for them.  A design decision is made... if such a situation is encountered 
is it to be assumed to be correct - and passed along for payment - or 
considered to be in error, and sent to a supervisor/verifier/inspectrix 
for examination and over-ride?

As I was taught design... tests for the most common cases are first and 
the less common cases follow; this saves on both machine time and human 
time.  For example... since there aren't too many folks around who were 
born before 1850 (Gregorian calendar) it might be a Good Idea to have a 
data-entry system for driver's licenses throw an 'Invalid Date' if this is 
entered into a Date of Birth field.

The program is coded to disallow this as a transaction (without 
appropriate supervisory over-ride)... and this would seem to be good 
design as it would, most frequently, prevent a license being issued with a 
typo that would require a licensee to go through the issuing process again 
due to a simple typo.

It'd make it a bit more difficult for folks older than one hundred and 
fifty-seven years to get *their* licenses dealt with... but 
back-of-the-envelope calculations could show there is an acceptable 
cost/benefit ratio.

Names, on the other hand, are a whole 'nother kettle of fish... is 'John 
Simth' a typo?  Is 'Pat Yerbottom' male or female?  Is 'Talula Does The 
Hula From Hawaii' legal?  These questions are, I would say, qualitatively 
different than 'Should a request to issue a driver's license to someone 
born in 1850 be permitted without further question?'

These are things that Business Analysts used to... analyse.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-08T07:56:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hbac4pb95var93b2u25b322j8r2ctd0a2@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <g9qvrn$l8n$1@reader1.panix.com> <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com> <g9sc29$87u$1@reader1.panix.com>`

```
On Fri, 5 Sep 2008 22:32:41 +0000 (UTC), docdwarf@panix.com () wrote:

>As I was taught design... tests for the most common cases are first and 
>the less common cases follow; this saves on both machine time and human 
…[14 more quoted lines elided]…
>cost/benefit ratio.

I'm sure we have all read of cases which were exceptions to such
assumptions.   And they can be costly to correct.

I believe we often have more editing that makes sense in much
programming.   Editing can make change difficult without adding
significantly to fraud protection.    Editing because we can, or
because we have always done it that way should be re-thought.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T17:10:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga3ma8$njs$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com> <g9sc29$87u$1@reader1.panix.com> <4hbac4pb95var93b2u25b322j8r2ctd0a2@4ax.com>`

```
In article <4hbac4pb95var93b2u25b322j8r2ctd0a2@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Fri, 5 Sep 2008 22:32:41 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>It'd make it a bit more difficult for folks older than one hundred and 
>>fifty-seven years to get *their* licenses dealt with... but 
…[4 more quoted lines elided]…
>assumptions.   And they can be costly to correct.

There's the rub, Mr Brazee... determining what constitutes an 'acceptable 
cost/benefit ratio' for (machine and human time used in editing for a 
given combination of data) compared with (machine and human time used in 
correcting a situation which, while rare, passed through the edits and 
Cost the Company Money) is a delicate art.

(It is also something I've seen reduced to a Corner Office Idiot screaming 
'I don't care how it gets done, I just don't want to get another call like 
that from someone who reviews my perfomance Ever Again!')

>
>I believe we often have more editing that makes sense in much
>programming.   Editing can make change difficult without adding
>significantly to fraud protection.    Editing because we can, or
>because we have always done it that way should be re-thought.

Leaving aside who determines what 'makes sense' or what constitutes a 
'significant addition to fraud protection'... this brings things right 
back to where it all began.  Males, for the most part, do not have a 
uterus and, as such, should not be paid for having such infections of 
organs dealt with...

... BUT IF the claimant is a male who has a female relative who is also 
covered by the policy then it's OK...

... BUT NOT IF the claimant is a male who has a female relative who is 
also covered by the policy and said female has had a hysterectomy...

... et and cetera.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-09T07:32:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<skucc4pos37musbdich4g22c2d57su9f66@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <3if2c4pnfobqrjh02k6pjbk8o4hcb7r4dl@4ax.com> <g9sc29$87u$1@reader1.panix.com> <4hbac4pb95var93b2u25b322j8r2ctd0a2@4ax.com> <ga3ma8$njs$1@reader1.panix.com>`

```
On Mon, 8 Sep 2008 17:10:33 +0000 (UTC), docdwarf@panix.com () wrote:

> Males, for the most part, do not have a 
>uterus and, as such, should not be paid for having such infections of 
…[6 more quoted lines elided]…
>also covered by the policy and said female has had a hysterectomy...

I'm not sure whether any sex-changed men still have uteruses.   It may
be better to flag such a case for further review than to categorically
deny it.   Law suits cost.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-09T15:35:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga653s$d7s$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <4hbac4pb95var93b2u25b322j8r2ctd0a2@4ax.com> <ga3ma8$njs$1@reader1.panix.com> <skucc4pos37musbdich4g22c2d57su9f66@4ax.com>`

```
In article <skucc4pos37musbdich4g22c2d57su9f66@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 8 Sep 2008 17:10:33 +0000 (UTC), docdwarf@panix.com () wrote:
>
>> Males, for the most part, do not have a 
>>uterus and, as such, should not be paid for having such infections of 
>>organs dealt with...

[snip]

>I'm not sure whether any sex-changed men still have uteruses.   It may
>be better to flag such a case for further review than to categorically
>deny it.   Law suits cost.

Paying invalid claims cost, as well... hence the phenomenon of 
'cost/benefit analysis'.

In my experience a claim's being denied results in a review... and then 
another review... and then an audit and a review... and then a few other 
steps before a lawsuit is filed.  A major consideration often is 'good 
faith' and how a denied claim is treated by an insurer once it discovers 
that the denial occurred in an instance of a transgendered male's claim 
for treatment of a uterine infection being assigned an inappropriate 
status.

In a posting I made nigh a decade back descrbing a meeting I attended 
night a decade back 
<http://groups.google.com/group/comp.software.year-2000/msg/7b0f478783b66534?dmode=source> 
I related how I asked '... has anyone calculated how much it will cost to 
fix things when six months after cutover folks discover that they've been 
pumping out bad checks for the past half-year?'

Somehow it might just possibly be that a similar situation applies here, 
that it would be cheaper to initially demand supervisory review for a 
procedure determined as 'sex-inappropriate' (eg, uterine infections in 
males than to pay them off without further examination.

DD
```

##### ↳ ↳ Re: Odd doings in California

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-05T09:39:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>`

```
Robert wrote:
> On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <lacey@mts.net> wrote:
>
…[16 more quoted lines elided]…
> Total 6.5 months

Oh bother!

There's a field for hourly rate for every employee and virtually every 
employee has had their rate changed once upon a time.

So, call up an employee record. Change the hourly rate to the minimum wage. 
Punch the "save" button.

At 30 seconds for each employee, and using 50 trained monkeys, the task 
could be done in less than a week.
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-05T12:52:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>`

```
On Sep 6, 2:39 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Robert wrote:
> > On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <la...@mts.net> wrote:
…[28 more quoted lines elided]…
> could be done in less than a week.

While I may be further away than most here, I think that the problem
is not that at all. It is probably quite easy to change the rates.

The requirement is, AFAIK, that should the rates be reduced then this
may be later overturned, by an employment court eg, and the shortfall
over the period will need to be paid to the employees (possibly plus
interest). The system will need to keep _two_ sets of data. One for
the pay that they would have received and another for the minimum pay
that they did receive.

It may be that they could clone the system and modify the rates on one
of them.  They would still need a great deal of work for the input
data to be gathered and selectively processed by the 'shadow'.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T22:53:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sda3$173$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>`

```
In article <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>,
Richard  <riplin@azonic.co.nz> wrote:

[snip]

>While I may be further away than most here, I think that the problem
>is not that at all. It is probably quite easy to change the rates.

Mr Plinston, as both Mr Tees and I have tried to point out... paying Civil 
Service employees is not only a matter of rates.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-05T21:05:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g9sda3$173$1@reader1.panix.com...
> In article
<9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>,
> Richard  <riplin@azonic.co.nz> wrote:
>
…[6 more quoted lines elided]…
> Service employees is not only a matter of rates.

The particular situation in California, as I recall, falls under
the Governor's emergency powers and, as such, the solution
depends a great deal upon what may be suspended. Thus,
Mr Dwarf, it may not be as complex as regular payroll.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-06T01:35:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9smpd$67m$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>`

```
In article <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:g9sda3$173$1@reader1.panix.com...
…[15 more quoted lines elided]…
>Mr Dwarf, it may not be as complex as regular payroll.

I don't know how much of what Laws and the State Constitution the 
Governor's Emergency Powers can supersede... but your assumption 
was never disputed, Mr Smith.

In the admission that 'it may not be as complex as regular payroll' might 
lie the situation of 'it is less complex than regular payroll', 'it is 
more complex than regular payroll', 'it may not be at the moment but might 
when the next set of quarterly financials are generated'...

... in short, Mr Smith, this 'may be' encounters a variety of 
possibilities and until such time as the probability of outcome is 
determined it might - given that one is dealing with peoples' paychecks, 
often a rather emotion-laden issue - be best to dismiss any 'all ya gotta 
do is' with a politician's 'that's an interesting proposal... get me some 
resource estimates on that from three Approved Vendors and we'll discuss 
them at the next session.'

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-05T22:39:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <g9smpd$67m$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g9smpd$67m$1@reader1.panix.com...
> In article <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:g9sda3$173$1@reader1.panix.com...
> >> In article
> ><9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>,
…[7 more quoted lines elided]…
> >> Mr Plinston, as both Mr Tees and I have tried to point out... paying
Civil
> >> Service employees is not only a matter of rates.
> >
…[3 more quoted lines elided]…
> >Mr Dwarf, it may not be as complex as regular payroll.

[snip]

> In the admission that 'it may not be as complex as regular payroll' might
> lie the situation of 'it is less complex than regular payroll', 'it is
> more complex than regular payroll', 'it may not be at the moment but might
> when the next set of quarterly financials are generated'...

While I admit, Mr Dwarf, to being unfamiliar with all forms
of logic. A form with which I am familiar would preclude
any other than what I wrote.

Given that R is the complexity of regular payroll measured
by the number of rules and that S is the complexity of the
number of rules suspended; then R minus S 'may not be
as complex as' R, or ((R - S) <= R), seems to be the only
logical conclusion.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-06T13:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9u1fc$r95$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <g9smpd$67m$1@reader1.panix.com> <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet>`

```
In article <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:g9smpd$67m$1@reader1.panix.com...
…[38 more quoted lines elided]…
>logical conclusion.

Consider, Mr Smith, that persons earning only (salary) or greater are 
eligible )by law ) for participation in (program).  Several thousand 
people, due to a decrease in salary, are suddenly no longer eligible to 
participate and their previous participations are to be changed to a 
different status.

I would say that the change in salary, mandating this 'waterfall' of other 
changes, makes things more complex, not less.

In other words... Mr Smith, you seem to be stating that the change in 
salary is represented as the subtracting of S ( ' - S').  This is where we 
differ, perhaps, in that given a system as complex as a Civil Service 
payroll system a change in salary might well have results that are other 
than simply minus or plus... the delta's the thing.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-06T11:09:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CsydnUsqeJ9GAV_VnZ2dnUVZ_tPinZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <g9smpd$67m$1@reader1.panix.com> <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet> <g9u1fc$r95$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g9u1fc$r95$1@reader1.panix.com...
> In article <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:g9smpd$67m$1@reader1.panix.com...
> >> In article
<ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
> >> >
…[8 more quoted lines elided]…
> >> >> >While I may be further away than most here, I think that the
problem
> >> >> >is not that at all. It is probably quite easy to change the rates.
> >> >>
…[11 more quoted lines elided]…
> >> In the admission that 'it may not be as complex as regular payroll'
might
> >> lie the situation of 'it is less complex than regular payroll', 'it is
> >> more complex than regular payroll', 'it may not be at the moment but
might
> >> when the next set of quarterly financials are generated'...
> >
…[23 more quoted lines elided]…
> than simply minus or plus... the delta's the thing.

Consider that what was raised was a particular situation
in California; not a general case. While our understandings
may be quite different, my understanding of 'this situation'
is that salary, wage, benefits, etc., are not changed. What
does change is the amount to be paid until the budget is
approved.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T00:53:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga1t2q$k5a$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet> <g9u1fc$r95$1@reader1.panix.com> <CsydnUsqeJ9GAV_VnZ2dnUVZ_tPinZ2d@posted.mid-floridainternet>`

```
In article <CsydnUsqeJ9GAV_VnZ2dnUVZ_tPinZ2d@posted.mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:g9u1fc$r95$1@reader1.panix.com...
…[4 more quoted lines elided]…
>news:g9smpd$67m$1@reader1.panix.com...

[snip]

>> I would say that the change in salary, mandating this 'waterfall' of other
>> changes, makes things more complex, not less.
…[12 more quoted lines elided]…
>approved.

If a salary is an amount paid, Mr Smith, and you understand that salary 
does not change while the amount to be paid changes then it seems there's 
a violation of the Aristotelean Principle of Non-Contradiction... but be 
that as it may, what is being pointed out is that salary is but one part 
of a Civil Service compensation package and the changing of salary may, 
because of the way computer programs have been written and maintained over 
decades, may be a task a bit more complex with results far more profound 
than a mere 'all ya gotta do is get monkeys to pound keyboards.'

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-07T23:42:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<272dnfIf8vpwA1nVnZ2dnUVZ_vzinZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet> <g9u1fc$r95$1@reader1.panix.com> <CsydnUsqeJ9GAV_VnZ2dnUVZ_tPinZ2d@posted.mid-floridainternet> <ga1t2q$k5a$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ga1t2q$k5a$1@reader1.panix.com...
> In article <CsydnUsqeJ9GAV_VnZ2dnUVZ_tPinZ2d@posted.mid-floridainternet>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:g9u1fc$r95$1@reader1.panix.com...
> >> In article
<l7ednQVqPuS6cFzVnZ2dnUVZ_orinZ2d@posted.mid-floridainternet>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
> >> >
…[5 more quoted lines elided]…
> >> I would say that the change in salary, mandating this 'waterfall' of
other
> >> changes, makes things more complex, not less.
> >>
> >> In other words... Mr Smith, you seem to be stating that the change in
> >> salary is represented as the subtracting of S ( ' - S').  This is where
we
> >> differ, perhaps, in that given a system as complex as a Civil Service
> >> payroll system a change in salary might well have results that are
other
> >> than simply minus or plus... the delta's the thing.
> >
…[14 more quoted lines elided]…
> than a mere 'all ya gotta do is get monkeys to pound keyboards.'

It seems to me that an amount-paid almost never equals a salary
and the amount-paid may change without a change in salary by
making changes to deductions.

Consider this _simplified_ example for regular payroll:
    perform calculate-deductions
    compute amount-paid = salary
        - function sum (deduction-amount (all))

I see no violation. What I see in this case, is that certain
amounts will be deferred, thus making the amount-paid less
artificially (caused by sociopolitical forces), rather than by
the application of the normal rules.

I find no reason to disagree with the last of your statements,
Mr Dwarf. Upon reflection, it seems we may have had
different 'interpretations' of Mr Plinston's statement, "It is
probably quite easy to change the rates." I understood it
to be a simple statement of fact, much like "It is probably
quite easy to fall off a bike". Something I managed to
demonstrate a few months ago. That is, his statement was
not intended as a recommendation.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-06T00:23:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dJGdnQHgBPrvmF_VnZ2dnUVZ_qninZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <g9smpd$67m$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g9smpd$67m$1@reader1.panix.com...

[snip]

> ... in short, Mr Smith, this 'may be' encounters a variety of
> possibilities and until such time as the probability of outcome is
…[4 more quoted lines elided]…
> them at the next session.'

I would be remiss if I fail to mention that, for a payroll system.
'all ya gotta do is' follow the clerical paradigm; that is, do in
the program whatever a clerk would do to get the correct results.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-06T13:46:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9u1jj$jv5$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <g9smpd$67m$1@reader1.panix.com> <dJGdnQHgBPrvmF_VnZ2dnUVZ_qninZ2d@posted.mid-floridainternet>`

```
In article <dJGdnQHgBPrvmF_VnZ2dnUVZ_qninZ2d@posted.mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:g9smpd$67m$1@reader1.panix.com...
…[13 more quoted lines elided]…
>the program whatever a clerk would do to get the correct results.

It would be likewise remiss, Mr Smith, to fail to mention that a computer 
system should make it necessary for a clerk to do fewer things to get the 
correct results.  If 'doing things' requires an expenditure of energy and, 
by definition, an expenditure of energy is work... then let it be recalled 
that Machines Work, People Think.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** donald tees <donaldtees@execulink.com>
- **Date:** 2008-09-06T07:26:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E_OdnYVVIIpG9V_VnZ2dnUVZ_oDinZ2d@golden.net>`
- **In-Reply-To:** `<ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet>`

```
Rick Smith wrote:
> <docdwarf@panix.com> wrote in message news:g9sda3$173$1@reader1.panix.com...
>> In article
…[15 more quoted lines elided]…
> 
Then why use a computer?  If it is that simple, just withdraw a few 
million from a bank account, and start handing it out.

Donald
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-06T11:17:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y9OdnbsvlIQ6A1_VnZ2dnUVZ_s3inZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com> <g9sda3$173$1@reader1.panix.com> <ho6dnds1GsRlS1zVnZ2dnUVZ_o7inZ2d@posted.mid-floridainternet> <E_OdnYVVIIpG9V_VnZ2dnUVZ_oDinZ2d@golden.net>`

```

"donald tees" <donaldtees@execulink.com> wrote in message
news:E_OdnYVVIIpG9V_VnZ2dnUVZ_oDinZ2d@golden.net...
> Rick Smith wrote:
> > <docdwarf@panix.com> wrote in message
news:g9sda3$173$1@reader1.panix.com...
> >> In article
> > <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>,
…[6 more quoted lines elided]…
> >> Mr Plinston, as both Mr Tees and I have tried to point out... paying
Civil
> >> Service employees is not only a matter of rates.
> >
…[7 more quoted lines elided]…
> million from a bank account, and start handing it out.

As I understand the situation in California, a computer
must calculate total payroll 'as if' it were paid, but the
amounts actually paid could be nearly as simple as you
suggest.

Once the budget is approved, all amounts not paid previously
will be paid.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-05T23:36:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gYKdnV9EqfVdZ1zVnZ2dnUVZ_vninZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com>`

```

"Richard" <riplin@azonic.co.nz> wrote in message 
news:9bb64803-91f2-4cb0-bb67-bed24bec577e@v13g2000pro.googlegroups.com...
On Sep 6, 2:39 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Robert wrote:
> > On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <la...@mts.net> wrote:
…[29 more quoted lines elided]…
> could be done in less than a week.

While I may be further away than most here, I think that the problem
is not that at all. It is probably quite easy to change the rates.

The requirement is, AFAIK, that should the rates be reduced then this
may be later overturned, by an employment court eg, and the shortfall
over the period will need to be paid to the employees (possibly plus
interest). The system will need to keep _two_ sets of data. One for
the pay that they would have received and another for the minimum pay
that they did receive.

It may be that they could clone the system and modify the rates on one
of them.  They would still need a great deal of work for the input
data to be gathered and selectively processed by the 'shadow'.

[charlie]

The short article I read about this indicated that the very people with the 
experience needed to make the required changes were some on the ones laid 
off.
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T22:36:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sc8p$o9t$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>`

```
In article <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]

>So, call up an employee record. Change the hourly rate to the minimum wage. 
>Punch the "save" button.
>
>At 30 seconds for each employee, and using 50 trained monkeys, the task 
>could be done in less than a week. 

... proving, yet again, H L Mencken's assertion that 'For every complex 
problem, there is a solution that is simple, neat and wrong.'

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-05T19:48:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <g9sc8p$o9t$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[11 more quoted lines elided]…
>

And as Ronald Reagan said: "Those who think there are no simple answers just 
haven't tried hard enough."
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-06T01:39:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sn04$9ue$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <g9sc8p$o9t$1@reader1.panix.com> <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com>`

```
In article <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>,
…[15 more quoted lines elided]…
>haven't tried hard enough." 

It was not postulated that 'there are no simple answers'... it has been 
pointed out that dealing with Civil Service pay rates might not be as 
readily accomplished as those who've never read a few pages of OMB 
regulations (or similar documents which form the basis of Civil Service 
payroll systems code) would wish to believe.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-06T10:03:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <g9sc8p$o9t$1@reader1.panix.com> <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com> <g9sn04$9ue$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[25 more quoted lines elided]…
>

Oh. I thought H.L. Mencken postulated such and that by quoting him, you were 
offering that insight into the issue.

I suggest that your reliance on the complexity of civil service regulations 
as evidence sufficient that "simple" changes are impossible is worse than 
tunnel vision - it is blank-wall vision. OMB regulations are not a suicide 
pact.

For example, the first solution that comes to mind is "cashier the lot." Of 
course the millions of state employees could sue the state, but first they'd 
have to find a court that was open...

If that's too drastic, a more modest approach would be sequester the 
paychecks of the state legislators. Alternatively, pick a large, but 
sympathetic group (single mothers, handicapped children, disabled veterans, 
monkey farmers, etc.) and withhold their money.

Then, too, there's the Texas solution: Beat the leaders of the opposition so 
badly they're unable to even lie down. If that offends one's sensibilities, 
the opposition leaders could be disappeared.

These are solutions that take about, oh, a quarter-hour to implement. More 
responses would be available if you opened the window to an hour. Even more 
if you said "What can we do in a day?"
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T01:05:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga1tp5$ari$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com> <g9sn04$9ue$1@reader1.panix.com> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com>`

```
In article <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com>,
…[29 more quoted lines elided]…
>offering that insight into the issue.

Mr Mencken postulated that a complex problem has a simple solution which 
is wrong... he did not, to my knowledged of his works, postulate that no 
problem has a simple solution which is right or that all problems have a 
simple solution of any kind at all.

>
>I suggest that your reliance on the complexity of civil service regulations 
>as evidence sufficient that "simple" changes are impossible is worse than 
>tunnel vision - it is blank-wall vision. OMB regulations are not a suicide 
>pact.

The regulations are not a suicide pact and nowhere was it stated that they 
might be... the regulations, however, might have the force of Law and as 
much as he'd like to believe it the Governor's emergency powers might not 
extend to the ability to suspend such Law as immediately as he might 
desire.

>
>For example, the first solution that comes to mind is "cashier the lot." Of 
>course the millions of state employees could sue the state, but first they'd 
>have to find a court that was open...

That a court is not open does not prevent a judge from issuing a order... 
and it might be that more than one court has jurisdiction over the status 
of hire of the employees involved.  These are not simple situations.

>
>If that's too drastic, a more modest approach would be sequester the 
>paychecks of the state legislators. Alternatively, pick a large, but 
>sympathetic group (single mothers, handicapped children, disabled veterans, 
>monkey farmers, etc.) and withhold their money.

Selective enforcement of a law is - despite the unremarkably frequent 
occurrence thereof, as anyone who has been stopped 'for being in the wrong 
neighborhood' might know - not smiled upon during legal reviews, appeals 
and other bits of the Justice System as she is wrote.  'All ya gotta do 
is' might work as well in the bureaucracy of Government as it does in the 
bureaucracy of other Large Organisations.

>
>Then, too, there's the Texas solution: Beat the leaders of the opposition so 
>badly they're unable to even lie down. If that offends one's sensibilities, 
>the opposition leaders could be disappeared.

Ahhhhhh, the good old One Party Rule model... no need to change the United 
States to such a system, you can find like-minded practioners in Cuba or 
Beijing who might welcome those of their own political bent.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 8)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-07T20:40:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com> <g9sn04$9ue$1@reader1.panix.com> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com> <ga1tp5$ari$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
>
> The regulations are not a suicide pact and nowhere was it stated that
…[3 more quoted lines elided]…
> immediately as he might desire.

Wrong. All states, and the federal government, have laws that simply state 
the governor can suspend or modify any existing law or regulation in an 
emergency. Further, it is the governor who declares when something is an 
emergency. For example, here's California's:

Government Code 8571.  During a state of war emergency or a state of 
emergency the Governor may suspend any regulatory statute, or statute 
prescribing the procedure for conduct of state business, or the orders, 
rules, or regulations of any state agency, including subdivision (d) of 
Section 1253 of the Unemployment Insurance Code, where the Governor 
determines and declares that strict compliance with any statute, order, 
rule, or regulation would in any way prevent, hinder, or delay the 
mitigation of the effects of the emergency.

(There are other paragraphs expanding on the above. See: 
http://caselaw.lp.findlaw.com/cacodes/gov/8565-8574.html )




>
>>
…[7 more quoted lines elided]…
> simple situations.

As a connoisseur of quotes, I'm sure you'll recognize this one from Andrew 
Jackson: "John Marshall has made his decision, now let him enforce it."

>
>>
…[14 more quoted lines elided]…
>

It's not one-party rule. Any party is welcome to use the tactic. Of course 
those that don't like the idea are free to appeal. In a few years they might 
get a favorable decision.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-08T14:16:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ijg7gFqrhjpU1@mid.individual.net>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <mPidnc0hp6H0TlzVnZ2dnUVZ_t7inZ2d@earthlink.com> <g9sn04$9ue$1@reader1.panix.com> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com...
> docdwarf@panix.com wrote:
>>
<snip>>
>>>
>>> Then, too, there's the Texas solution: Beat the leaders of the
>>> opposition so badly they're unable to even lie down. If that offends
>>> one's sensibilities, the opposition leaders could be disappeared.

I liked the one about the monkeys beating the keyboards, not so sure about 
the keyboards being used to beat the monkeys... :-)

>>
>> Ahhhhhh, the good old One Party Rule model... no need to change the
…[7 more quoted lines elided]…
> might get a favorable decision.

Or a Civil War even... Ah, yes, I believe that option was exercised in the 
then disunited states of America, around the middle of the 19th century. 
Here we are racing towards the middle of the 21st century and, apparently, 
nothing has been learned... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T12:24:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga35i6$ife$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <6ijg7gFqrhjpU1@mid.individual.net>`

```
In article <6ijg7gFqrhjpU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
>"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
>news:doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com...

[snip]

>> It's not one-party rule. Any party is welcome to use the tactic. Of course 
>> those that don't like the idea are free to appeal. In a few years they 
…[3 more quoted lines elided]…
>then disunited states of America, around the middle of the 19th century. 

That it was, Mr Dashwood... and during as a part of that horrid conflict 
there was issued A Declaration of the Causes which Impel the State of 
Texas to Seced from the Federal Union. 

In this Declaration the State of Texas admitting to being unable to 
'protect the lives and property of the people of Texas against the Indian 
savages' and 'the murderous forays of banditti from the neighboring 
territory of Mexico'... but what seems to have gone beyond all bounds was:

'In all the non-slave-holding States, in violation of that good faith and 
comity which should exist between entirely distinct nations, the people 
have formed themselves into a great sectional party, now strong enough in 
numbers to control the affairs of each of those States, based upon an 
unnatural feeling of hostility to these Southern States and their 
beneficent and patriarchal system of African slavery, proclaiming the 
debasing doctrine of equality of all men, irrespective of race or color-- 
a doctrine at war with nature, in opposition to the experience of mankind, 
and in violation of the plainest revelations of Divine Law. They demand 
the abolition of negro slavery throughout the confederacy, the recognition 
of political equality between the white and negro races, and avow their 
determination to press on their crusade against us, so long as a negro 
slave remains in these States.'

(from http://www.yale.edu/lawweb/avalon/csa/texsec.htm )

>Here we are racing towards the middle of the 21st century and, apparently, 
>nothing has been learned... :-)

Texans complained that they could not protect themselves, Mr Dashwood... 
but they went to war because others were willing to fight against their 
beloved institution of chattel slavery and their interpretation of such 
slavery as in accord with 'the plainest revelations of Divine Law'.

It seems they do not seek the United States of America... they look for a 
slave-holding theocracy.  Expect from them logic in accord with such 
principles and you may not be very much disappointed.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-09T12:46:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ilvbnFqacaqU1@mid.individual.net>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <6ijg7gFqrhjpU1@mid.individual.net> <ga35i6$ife$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:ga35i6$ife$1@reader1.panix.com...
> In article <6ijg7gFqrhjpU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[53 more quoted lines elided]…
>
Very stirring stuff in the quotes you gave.

Don't be too hard on Texas, Doc. The steaks are great, the people are very 
kind to strangers (at least , I found them so...) and they do have a sense 
of humour that allows them to laugh at themselves. (A rare commodity in 
today's world...). I really enjoyed my time there and didn't meet anyone who 
was anxious to have negro slaves. I did meet good Christian people who 
thought that "negroes are a lower life form and God requires us to take care 
of them", but that was an isolated instance.

Nevertheless, it would not be good to repeat that former unpleasantness 
where so many good men on both sides died.

Redneckedness may be a proud tradition in Texas, buit even rednecks need 
common sense occasionally... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-09T01:04:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga4i2a$bnv$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <6ijg7gFqrhjpU1@mid.individual.net> <ga35i6$ife$1@reader1.panix.com> <6ilvbnFqacaqU1@mid.individual.net>`

```
In article <6ilvbnFqacaqU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[20 more quoted lines elided]…
>> Texas to Seced from the Federal Union.

[snip]

>> Texans complained that they could not protect themselves, Mr Dashwood...
>> but they went to war because others were willing to fight against their
…[8 more quoted lines elided]…
>Very stirring stuff in the quotes you gave.

I am not one who leaps quickly to emotion, Mr Dashwood... but when these 
tapeworm-ridden proud-of-their-ignorance fellow-citizens of mine - and 
note that while I disagree with them I acknowledge our equality of 
citizenship - speak of being Champions of Liberty while standing in the 
muck-filled stables of their past with nary a 'Gee, maybe we'd better 
watch out just in case we go down that road again'... well, rightly or 
wrongly, I believe it is time for another side to be heard, in this case 
the side that accepted the Surrender at Appomattox.

>
>Don't be too hard on Texas, Doc.

I don't believe I am too hard on Texas, Mr Dashwood... on the views given 
by a few individual Texans, perhaps, but I've been known to take folks of 
varying residence or nationality to task over what some see as the oddest 
of matters.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-09T07:35:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<goucc41cocj60fap578mpg82l27s29dkif@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <6ijg7gFqrhjpU1@mid.individual.net> <ga35i6$ife$1@reader1.panix.com> <6ilvbnFqacaqU1@mid.individual.net>`

```
On Tue, 9 Sep 2008 12:46:45 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

> I did meet good Christian people who 
>thought that "negroes are a lower life form and God requires us to take care 
>of them", but that was an isolated instance.

Better than some of the stories that my mother-in-law told me about
growing up in Missouri and being chided for bringing 3 drinks out to 3
workers - one of whom was black.    And churches that didn't give to
charity because the obvious recipients were black.  (Despite Jesus'
ï¿½Whatever you do to the least of these, you do to me.ï¿½ statement).
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T10:15:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga2tvo$1a8$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>`

```
In article <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>
…[17 more quoted lines elided]…
>rule, or regulation would in any way prevent, hinder, or delay the 
Newsgroups: comp.lang.cobol
Subject: Re: Odd doings in California
Summary: 
Expires: 
References: <nq2wk.36210$Rs1.36033@newsfe08.iad> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>
Sender: 
Followup-To: 
Distribution: 
Organization: Public Access Networks Corp.
Keywords: 
Cc: 

In article <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>
…[9 more quoted lines elided]…
>emergency.

Note while I, an admitted non-lawyer, used the phrase 'the Governor's 
emergency powers' there may well be a difference between what 'the 
Governor's powers are during what he calls an emergency' and 'the 
Governor's powers during a state of emergency'; it seems as though the 
latter are addressed below.

I don't believe a state of emergency has been declared in California, I 
believe the Governor has issued an Executive Order.  From 
http://www.sacbee.com/111/story/1132588.html :

--begin quoted text:

The Republican governor signed an executive order last week recommending 
the cut to minimum wage for most permanent state workers and terminating 
10,133 temporary and part-time employees.

[snip]

He (Chiang) disputes Schwarzenegger's legal interpretation of a 2003 
California Supreme Court decision, which the governor said mandates that 
the state pay only minimum wage to employees until a budget is passed.

--end quoted text

Now... the issuing of an Executive Order might be done in order to deal 
with a perceived Emergency, true, but said Emergency does not seem to fit 
any of the three conditions or degrees of emergency stated in Sec 8558:

a) enemy attack probable or imminent

b) duly proclaimed contions of disaster (air pollution, fire, flood, 
storm, epidemic, riot, drought, energy shortage, plant/animal infestation, 
earthquake, volcanic eruption, conditions resulting from a labor 
controversy or conditions 'causing a state of war emergency')

c) local emergency

(details at http://caselaw.lp.findlaw.com/cacodes/gov/8555-8561.html )

... so while - with some exceptions, such as seizure of firearms (8571.5) 
or commandeering newspapers (8572) - the Governor can, in fact, violate 
State Law or State Constitutional provisions... I do not believe that an 
Executive Order carries the same force and I do not believe the ability to 
come to a budget agreement is of the same magnitude.

If the inability to reach agreement *was* of that magnitude then it might 
be concluded that a State of Emergency would have been declared, not an 
Executive Order issued.

>>> For example, the first solution that comes to mind is "cashier the
>>> lot." Of course the millions of state employees could sue the state,
…[8 more quoted lines elided]…
>Jackson: "John Marshall has made his decision, now let him enforce it."

Quite similarly, 'Governor Schwarzenegger has decided people will get 
paid, now let him issue their checks'... it works both ways.

[snip]

>>> Then, too, there's the Texas solution: Beat the leaders of the
>>> opposition so badly they're unable to even lie down. If that offends
…[10 more quoted lines elided]…
>get a favorable decision. 

'It ain't against the law... see, it only took the court a few years to 
show that.'  If you want to live like a Cuban, get thee to Cuba.

'f there is no struggle there is no progress. Those who profess to favor 
freedom and yet depreciate agitation�want crops without plowing up the 
ground, they want rain without thunder and lightening. They want the ocean 
without the awful roar of its many waters' - Frederick Douglass

If you want a nice, quiet, 
do-what-we-tell-you-lest-your-party-gets-beaten... there's Cuba and China, 
just waiting for your citizenship request.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 10)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-08T09:13:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ueGdnbL-hPJEBl_VnZ2dnUVZ_ojinZ2d@earthlink.com> <ga1tp5$ari$1@reader1.panix.com> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
>>>
>>> The regulations are not a suicide pact and nowhere was it stated
…[19 more quoted lines elided]…
> http://www.sacbee.com/111/story/1132588.html :

Whether a state of emergency has been declared or whether the Indian carried 
home the meat in a handkerchief is irrelevant to your erroneous assumption 
that the governor might not have the authority to suspend the laws.

>
> If you want a nice, quiet,
…[3 more quoted lines elided]…
>

If you can't argue the facts, or get caught in ignorance or misapprehension, 
there's always the refuge of personal attacks, such as suggesting I, or 
presumably anyone who cites a law at variance with your un-tutored beliefs, 
might be more at home in a Communist country.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T17:15:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga3mjr$5rd$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com>`

```
In article <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>>>
…[23 more quoted lines elided]…
>that the governor might not have the authority to suspend the laws.

Unless one wishes to assert that a Governor can, at any time, invoke 
powers of office which are limited to time of a declared state of 
emergency then whether a state of emergency has been declared would most 
certainly seem to have relevance to a Governor's ability to invoke powers 
which are active only during a state of emergency... no declaration, no 
powers.

>
>>
…[8 more quoted lines elided]…
>might be more at home in a Communist country. 

There may be more than those few reasons for suggesting such a thing... 
but folks who feel they hit closely to home might have a desire to snip 
them out of a posting without any indication of having edited them.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 12)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-08T18:42:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[33 more quoted lines elided]…
> declaration, no powers.

As a (non-practicing) lawyer, I do so assert. The governor can declare an 
emergency or state of emergency at any time and for any reason, or no reason 
at all. Such declaration is not subject to judicial or legislative review.

>
>>
…[16 more quoted lines elided]…
>

If you're referring to me, I don't feel your accusations hit close to home. 
Rather, it seems to be are an ad hominem attack in a desperate attempt to 
avoid defeat at the hands of facts and logic.

To restate:
1. The governor may declare a state of emergency.
2. During this state, the governor may suspend any existing law or 
regulation or impose new ones.
3. Neither the declaration of emergency nor the governor's actions under the 
declaration may be gainsaid by anyone.

This is the law. Not only common law since the time of the Magna Carta, but, 
in the case of California, black-letter law. If you do not like the 
statutes, far be it from me to suggest you migrate to Canada or some other 
socialist state.

Instead, I suggest you lump it.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-09T00:49:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga4h6h$laq$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com>`

```
In article <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com>,
…[38 more quoted lines elided]…
>at all. Such declaration is not subject to judicial or legislative review.

On the UseNet nobody knows you're a (non-practising) lawyer, among other 
things... but an argumentum ad vericundiam remains just that.

As a non-practising lawyer you may wish to consider the difference between 
'declaring a state of emergency at any time' and 'invoking the powers of a 
state of emergency absent declaration of a state of emergency'; one 
requires adherance to the form of a declaration and the other just might 
not.

You may also wish to consider the validi

>>>>
>>>> If you want a nice, quiet,
…[21 more quoted lines elided]…
>1. The governor may declare a state of emergency.

1a. The Governor has not declared a state of emergency.

>2. During this state, the governor may suspend any existing law or 
>regulation or impose new ones.

2a. Until such a declaration the governor does not have the powers which 
are granted by said declaration... as without said declaration said state 
does not exist.

>3. Neither the declaration of emergency nor the governor's actions under the 
>declaration may be gainsaid by anyone.

3a. As no state of emergency has been declared no action can be said to be 
taking place under such a declaration.

>
>This is the law.

To assert '(action) can happen under a declaration' may or may not have 
anything whatsoever to do with what actions may or may not happen when 
such a declaration has not been made... and to the best of my knowledge no 
declaration of emergency has been made in the state of California.

>Not only common law since the time of the Magna Carta, but, 
>in the case of California, black-letter law.

In the case of California it is, most likely, black-letter law that a 
state of emergency does not exist until such is declared; were that not 
the case a constant state of emergency would exist and the need to 
differentiate permissible powers would be unnecessary.

If you believe that this is not the case - in other words, if you believe 
that a state of emergency has been declared in California which would 
allow for such powers to be exercised - then the onus is upon you, as 
making the assertion of existence, to demonstrate it.  The argument of 
'they can... when it happens' does not necessarily translate into 'they 
can before it happens'.

The table seems stout enough to withstand your poundings, Counsellor.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-09T07:37:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com>`

```
On Mon, 8 Sep 2008 18:42:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>To restate:
>1. The governor may declare a state of emergency.
…[3 more quoted lines elided]…
>declaration may be gainsaid by anyone.

So the law doesn't really matter to the governor.   Can he override
the state Constitution as well?
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 14)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-16T10:52:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 8 Sep 2008 18:42:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[9 more quoted lines elided]…
> the state Constitution as well?

Probably. It gets tricky.

First the law under which he can suspend other laws is presumed 
constitutional (as are all laws passed by a legislative body). Therefore, on 
its face, it is constitutional to suspend the constitution(!).

In order to challenge this, the "emergency declaration" law, itself, must be 
found unconstitutional. That requires an appellate court decision. If the 
governor has abolished or suspended the courts, there's no one in authority 
to make that decision!

There's another, more direct, possibility. The law itself can declare it is 
not reviewable by the courts, so even if the courts operate, they may not 
have jurisdiction. While generally rare, this feature is often used in 
appropriation and budget laws at the federal level, else people would 
forever be challenging, on constitutional grounds, funding for research into 
the Irish Potato Famine or building a bus stop in Little Rabbit, Oklahoma.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-17T11:51:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jav4oF2bbufU1@mid.individual.net>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com...
> Howard Brazee wrote:
>> On Mon, 8 Sep 2008 18:42:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
…[29 more quoted lines elided]…
> Oklahoma.

I bet you guys wish you had a King or Queen who could just rule arbitrarily 
on stuff like this... :-)

We can appeal stuff to the Privy Council and the Law Lords and NOBODY can 
(legally) override their decisions. They derive their power directly from 
the Head of State (Queen Elizabeth the Second). There would have to be a 
Civil War or Revolution (both of which would be deemed illegal actions) to 
override their decision. The ONLY thing the Law Lords cannot do is override 
an Act of Parliament. We can tahnk OliverCromwell for "keeping them 
honest"... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 16)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-17T06:15:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t06Ak.562$x%.313@nlpi070.nbdc.sbc.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com> <6jav4oF2bbufU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6jav4oF2bbufU1@mid.individual.net...
>
> I bet you guys wish you had a King or Queen who could just rule 
…[8 more quoted lines elided]…
> them honest"... :-)

Sounds like it beats the crap out of dealing with lawyers.

MCM
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 16)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-18T10:21:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KO6dnYPUtIyP70_VnZ2dnUVZ_rjinZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com> <6jav4oF2bbufU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com...
…[43 more quoted lines elided]…
>

Heck, this time around I was rooting for JEB Bush for president. Then that 
good-looking Hispanic nephew. By the end of his second term, the Bush 
dynasty would be firmly established. Then it's only a small step to a 
monarchy.

Oh well.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-20T08:05:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vqOdnV8DW5ode0nVnZ2dnUVZ_hydnZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com>`

```

"HeyBub" <heybub@NOSPAMgmail.com> wrote in message
news:afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com...
> Howard Brazee wrote:
> > On Mon, 8 Sep 2008 18:42:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
…[15 more quoted lines elided]…
> constitutional (as are all laws passed by a legislative body). Therefore,
on
> its face, it is constitutional to suspend the constitution(!).
>
> In order to challenge this, the "emergency declaration" law, itself, must
be
> found unconstitutional. That requires an appellate court decision. If the
> governor has abolished or suspended the courts, there's no one in
authority
> to make that decision!
>
> There's another, more direct, possibility. The law itself can declare it
is
> not reviewable by the courts, so even if the courts operate, they may not
> have jurisdiction. While generally rare, this feature is often used in
> appropriation and budget laws at the federal level, else people would
> forever be challenging, on constitutional grounds, funding for research
into
> the Irish Potato Famine or building a bus stop in Little Rabbit, Oklahoma.


< http://www.liu.edu/cwis/cwp/library/exhibits/constitution/quotes.htm >
-----
The Constitution of the United States is a law for rulers and people,
equally
in war and in peace, and covers with the shield of its protection all
classes
of men, at all times, and under all circumstances. No doctrine, involving
more pernicious consequences, was ever invented by the wit of man than
that any of its provisions can be suspended during any of the great
exigencies of government.

David Davis
(judge, 1815-1886)
-----
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 16)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-20T15:39:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SN2dnQrfWP4WwkjVnZ2dnUVZ_sDinZ2d@earthlink.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com> <vqOdnV8DW5ode0nVnZ2dnUVZ_hydnZ2d@posted.mid-floridainternet>`

```
Rick Smith wrote:
>>>> To restate:
>>>> 1. The governor may declare a state of emergency.
…[43 more quoted lines elided]…
> -----

Thanks for sharing. The link which you provided was filled with similar 
lofty ideals. Still, an oft-quoted maxim, attributed to Abraham Lincoln, 
states: "The Bill of Rights is not a suicide pact." In order to HAVE a 
Constitution, you've got to have a country.

It's common that, in times of trouble, individual liberties are constrained. 
When the threat passes, the leashes are loosed.

But not always.

I remind you that the Executive Order 9066, regarding internment of Japanese 
civilians from 1942 wasn't rescinded until 1976.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-20T18:28:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pLOdnXPrHZYh5UjVnZ2dnUVZ_srinZ2d@posted.mid-floridainternet>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <doOdndtsMLUJH1nVnZ2dnUVZ_srinZ2d@earthlink.com> <ga2tvo$1a8$1@reader1.panix.com> <CoCdnTI3jqNjr1jVnZ2dnUVZ_rXinZ2d@earthlink.com> <ga3mjr$5rd$1@reader1.panix.com> <mdSdnS5nG8b9JVjVnZ2dnUVZ_jqdnZ2d@earthlink.com> <9vucc41n27pjhofjaqth99g4fuk2tqborg@4ax.com> <afydnXQCEuXOS1LVnZ2dnUVZ_jidnZ2d@earthlink.com> <vqOdnV8DW5ode0nVnZ2dnUVZ_hydnZ2d@posted.mid-floridainternet> <SN2dnQrfWP4WwkjVnZ2dnUVZ_sDinZ2d@earthlink.com>`

```

"HeyBub" <heybub@NOSPAMgmail.com> wrote in message
news:SN2dnQrfWP4WwkjVnZ2dnUVZ_sDinZ2d@earthlink.com...
> Rick Smith wrote:

[snip]

> > <
> > http://www.liu.edu/cwis/cwp/library/exhibits/constitution/quotes.htm
…[17 more quoted lines elided]…
> Constitution, you've got to have a country.

Interestingly, Judge Davis was appointed an associate
justice of the Supreme Court by Abraham Lincoln and
served from 1862 to 1877.

> It's common that, in times of trouble, individual liberties are
constrained.
> When the threat passes, the leashes are loosed.

<
http://www.sscnet.ucla.edu/southasia/History/Current_Affairs/musharraf.html
>
titled, "Musharraf's Lincoln, Bush's Musharraf", discusses
how Musharraf and Bush use Lincoln to justify suppression
of liberties.

> But not always.
>
> I remind you that the Executive Order 9066, regarding internment of
Japanese
> civilians from 1942 wasn't rescinded until 1976.

With reparations and, I believe, an apology!
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-05T18:28:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com>`

```
On Fri, 5 Sep 2008 09:39:11 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>Robert wrote:
>> On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <lacey@mts.net> wrote:
…[28 more quoted lines elided]…
>could be done in less than a week. 

This sounds like an 'all ya gotta do' solution. One SQL statement (with appropriate ODBC
driver) could change everyone's rate to the minimum. It would take milliseconds per
employee.  

Consider 1.5 overtime pay mandated by the Fair Labor Standards Act (FLSA). IT workers are
exempt if they make over $27.63/hr; managers are always exempt. Nearly all payroll systems
make the decision based on an Indicator, not the hourly rate. There is no way to make the
correct decision with program logic. A human, not a trained monkey, must decide whether a
team lead is a programmer or manager.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-06T01:48:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9snhq$lkq$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com>`

```
In article <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 5 Sep 2008 09:39:11 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

[snip]

>>There's a field for hourly rate for every employee and virtually every 
>>employee has had their rate changed once upon a time.
…[11 more quoted lines elided]…
>employee.  

If the system supports SQL, perphaps so... on the other hand I've run 
across a payroll system - not too large, around 60K employees every two 
weeks - that runs primarily on flat files.  Documentation and research are 
accomplished by a combination of file searches and prayers.

>
>Consider 1.5 overtime pay mandated by the Fair Labor Standards Act
>(FLSA). IT workers are
>exempt if they make over $27.63/hr; managers are always exempt.

I believe FLSA mandatory-overtime exemption is not only for IT workers, it 
is for *any* worker whose base rate is more than (y) times the current 
Federal minimum wage... I think y = 5 but my memory is, admittedly, 
porous.

Calling someone a Manager is a recent (recent = past twenty-five years or 
so) way to get around overtime payments, as well... there have been a few 
lawsuits about this.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-06T00:48:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <SPOdnTAMp_QP2VzVnZ2dnUVZ_j-dnZ2d@earthlink.com> <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com> <g9snhq$lkq$1@reader1.panix.com>`

```
On Sat, 6 Sep 2008 01:48:42 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com>,
>Robert  <no@e.mail> wrote:
…[22 more quoted lines elided]…
>accomplished by a combination of file searches and prayers.

The Windows machine before you contains a Microsoft ODBC driver for Flat Files. Just go to
Control Panel\Admin\Data Sources. I used it to compare before and after files from a
mainframe regression test on the payroll of a major retailer with 400,000 active
employees. It was pretty fast. The mainframers couldn't believe their eyes.

>>Consider 1.5 overtime pay mandated by the Fair Labor Standards Act
>>(FLSA). IT workers are
…[5 more quoted lines elided]…
>porous.

The test is based on wage rate ONLY for IT workers. For others, it is based on vagueries.

>Calling someone a Manager is a recent (recent = past twenty-five years or 
>so) way to get around overtime payments, as well... there have been a few 
>lawsuits about this.

It is NOT based on job title. It is based on whether the worker exercises independent
judgement. Who are they kidding? Middle managers are more constrained than the people
above OR below them.

It's a cultural thing. First Responders (firemen and policemen), who exercise lots of
independent judgement, are never exempt.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T01:16:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga1udo$1ab$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com> <g9snhq$lkq$1@reader1.panix.com> <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com>`

```
In article <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 6 Sep 2008 01:48:42 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[31 more quoted lines elided]…
>employees. It was pretty fast. The mainframers couldn't believe their eyes.

The payroll system I mentioned did not run on a Windows machine, either 
before, beside or after me.  Primarily flat files and handcrafted COBOL 
code... no SQL, no ODBC.  Internal sorts, MOVE CORR, paragraph names like 
NAY-NAY, NAY-YEA, YEA-NAY and YEA-YEA all implemented into Prod and all 
running for a quarter-century.

To praphrase Edward G Robinson's question to Charleton Heston... 'Where's 
ya partitioned database now, Moses?'

>
>>>Consider 1.5 overtime pay mandated by the Fair Labor Standards Act
…[9 more quoted lines elided]…
>based on vagueries.

Perhaps it is time to refamiliarise myself with the statute.... 
naaaaahhhhh, there's better ways to spend my time.

>
>>Calling someone a Manager is a recent (recent = past twenty-five years or 
…[3 more quoted lines elided]…
>It is NOT based on job title.

That's what how some of the lawsuits have been decided... when people have 
the time and resources to file and persue them, that is.  Did you know 
that there are parts of the USA where people seem to believe that 'I don't 
care what the law says' is pronounced 'so sue me'?

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-08T01:07:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <p3f3c4lb9ppa404mudo5hmhk88e8h7dtij@4ax.com> <g9snhq$lkq$1@reader1.panix.com> <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com> <ga1udo$1ab$1@reader1.panix.com>`

```
On Mon, 8 Sep 2008 01:16:40 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com>,
>Robert  <no@e.mail> wrote:
…[35 more quoted lines elided]…
>The payroll system I mentioned did not run on a Windows machine,

Neither did the mainframe payroll system. But its flat files could be accessed with SQL,
guided by a hand crafted schema that was itself a flat file. Old timers didn't believe it
until they saw it.

> Primarily flat files and handcrafted COBOL 
>code... no SQL, no ODBC.  Internal sorts, MOVE CORR, paragraph names like 
>NAY-NAY, NAY-YEA, YEA-NAY and YEA-YEA all implemented into Prod and all 
>running for a quarter-century.

Don't be so confident. Flat files are a very soft target.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T12:31:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga35uu$lel$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com> <ga1udo$1ab$1@reader1.panix.com> <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com>`

```
In article <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 8 Sep 2008 01:16:40 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[42 more quoted lines elided]…
>didn't believe it until they saw it.

I believe you could run a compare just as you said, Mr Wagner... can you 
believe that there might, possibly, be something other to running an 
active payroll system than just 'comparing before and after files from a 
mainframe regression test'?

(for running such compares I usual use SuperC... but some folks like 
sending files back-and-forth)


>
>> Primarily flat files and handcrafted COBOL 
…[4 more quoted lines elided]…
>Don't be so confident. Flat files are a very soft target. 

Quite the reverse, Mr Wagner... my experience has taught me that 
confidence can decrease caution and I find approaching peoples' paychecks 
with caution to be a Good Thing, indeed.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-08T12:34:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpnac4dshbn362hpek5h9d5doffir2i0i6@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <ui54c4dmhuga1qe3jg4iqa0v5i4l3ubit1@4ax.com> <ga1udo$1ab$1@reader1.panix.com> <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com> <ga35uu$lel$1@reader1.panix.com>`

```
On Mon, 8 Sep 2008 12:31:26 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com>,
>Robert  <no@e.mail> wrote:
…[49 more quoted lines elided]…
>mainframe regression test'?

I ran both the payroll system before and after.

>(for running such compares I usual use SuperC... but some folks like 
>sending files back-and-forth)

They did not have SuperC. I heard installing new mainframe software required an Act of
Congress and a bucket of money. Congress was not in session.

>>> Primarily flat files and handcrafted COBOL 
>>>code... no SQL, no ODBC.  Internal sorts, MOVE CORR, paragraph names like 
…[7 more quoted lines elided]…
>with caution to be a Good Thing, indeed.

When they had a production problem, they deleted the offending time card and reran. The
first time I saw that, I suggested writing down the employee number so a hand check could
be issues. They said they didn't have time.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T18:29:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga3qtf$du4$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com> <ga35uu$lel$1@reader1.panix.com> <bpnac4dshbn362hpek5h9d5doffir2i0i6@4ax.com>`

```
In article <bpnac4dshbn362hpek5h9d5doffir2i0i6@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 8 Sep 2008 12:31:26 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>>>>Robert  <no@e.mail> wrote:

[snip]

>>>>>The Windows machine before you contains a Microsoft ODBC driver for Flat
>>>>>Files. Just go to
…[17 more quoted lines elided]…
>I ran both the payroll system before and after.

Now I am confused, Mr Wagner... a few postings back you said ran a 
compare on a Windows box for a mainframe system and when I mention I did 
the compare before-and-after on the mainframe you say 'I rean both the 
payroll system before and after'... I am not sure what to make of this.

>
>>(for running such compares I usual use SuperC... but some folks like 
…[4 more quoted lines elided]…
>Congress and a bucket of money. Congress was not in session.

I did not know that VMS lacked a native file-compare utility.  I spend my 
Big Iron contracts on MVS systems and have never run across a box where 
ISRSUPC was not available.

>
>>>> Primarily flat files and handcrafted COBOL 
…[14 more quoted lines elided]…
>be issues. They said they didn't have time.

Perhaps, Mr Wagner, that is an indication as to why they do what they 
do... and I do what I do.  I had a similar situation and was advised to 
behave identically ('edit the data and resubmit, we got a window to meet') 
and I wrote down an SSN on a piece of scrap pape and said 'I think I can 
get it straightened out in twenty minutes... do you really want me to 
ignore the payroll data for this person?'

It was the Department Manager's number... I was given twenty minutes, 
fixed it in five and later heard my tech lead boasting about how he had 
corrected the run so we didn't lose the card.

He got to brag, I got my paycheck... we make our choices.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-08T22:14:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v9fbc416904djp8kukrk0k6t4l6teulel5@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <rof9c454bbnkmajcdlls1vgpb1smblio8e@4ax.com> <ga35uu$lel$1@reader1.panix.com> <bpnac4dshbn362hpek5h9d5doffir2i0i6@4ax.com> <ga3qtf$du4$1@reader1.panix.com>`

```
On Mon, 8 Sep 2008 18:29:03 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <bpnac4dshbn362hpek5h9d5doffir2i0i6@4ax.com>,
>Robert  <no@e.mail> wrote:
…[35 more quoted lines elided]…
>payroll system before and after'... I am not sure what to make of this.

When you said there might be something other than just comparing files, I thought you were
referring to running the two systems. If not, what is the other?

>>>(for running such compares I usual use SuperC... but some folks like 
>>>sending files back-and-forth)
…[7 more quoted lines elided]…
>ISRSUPC was not available.

I already had a schema written to use for research. For example, see whether anyone will
have a review scheduled in the next century before June. Using it to compare two files was
very easy.

>>>>> Primarily flat files and handcrafted COBOL 
>>>>>code... no SQL, no ODBC.  Internal sorts, MOVE CORR, paragraph names like 
…[26 more quoted lines elided]…
>He got to brag, I got my paycheck... we make our choices.

My client's managers didn't submit time cards, they were salaried. 

Thursday night we ran half the payroll in Dallas and half in Chicago. Checks were printed
in Atlanta. Airplanes took them to 50 states, to be handed out Friday. If we had missed
the four hour window, heads would have rolled and chartered planes rolled out.

The check run took two hours. It was replaced by Peoplesoft on Unix in 1999. The first
mock run would have taken 36 hours, had it run to completion. Mainframers were all grins.
Then DBAs split the database into 35 partitions. The second mock run took 1.5 hours. Net
savings: $200M per year. IBM Global (formerly Advantis, formerly Prodigy) dumped its
mainframe service center to AT&T, which dumped it to someone else.
```

##### ↳ ↳ Re: Odd doings in California

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-09-05T11:27:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u6dwk.30047$Fr1.3715@newsfe03.iad>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com>`

```
Why use contractors?  There must be people maintaining the system.

Select workers for the task - 1 week
Analysis - 1 week because they know the system
Set up test environment - 1 day, because it already exists
Development - change programs - 2 days
Unit testing (presumably the changed programs - can't be many if the changes
only take 2 days) - 1 week
System & regression testing - 30 days
Production build - 1 day.  This is only the 10,000th time they've done this.
Dress rehearsals and spot checks - ??? - no different from any other rate
change scenario
Approvals - 1 week.

Total,  6 weeks.

It looks to me as though the I/T people, particularly management, just don't
want to do it because of the messes that will result - not programming
messes, but personal, institutional, and political.

PL

Robert <no@e.mail> wrote in message
news:gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com...
> On Thu, 4 Sep 2008 23:17:59 -0500, "tlmfru" <lacey@mts.net> wrote:
>
> >Chiang has said it can't be done.  He isn't refusing, but says it's
> >impossible "because of the age of the state's payroll system which is
based
> >on Cobol, it would take at least six months to reconfigure the system to
> >send out those new minimum-wage checks".
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-05T23:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9sdlt$apo$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <u6dwk.30047$Fr1.3715@newsfe03.iad>`

```
In article <u6dwk.30047$Fr1.3715@newsfe03.iad>, tlmfru <lacey@mts.net> wrote:

[snip]

>It looks to me as though the I/T people, particularly management, just don't
>want to do it because of the messes that will result - not programming
>messes, but personal, institutional, and political.

Remember, once again, that Civil Service pay is *not* only a matter of 
rates... there are a few other factors which come into play, as Mr Tees 
and I have tried to point out.

This is Civil Service pay folks are talking about... I don't know about 
California but I have been told that there are certain aspects of 
remuneration for New York State civil service employees which are a matter 
of the State Constitution... the Law.  Nothing I know of law - admittedly, 
a few thimblefuls or less - prevents similar situations from being the 
case in California.

If you change code so that you are no longer in compliance with the Law 
some people may rather unhappy with you... and some of those unhappy 
people may be lawyers.

I've seen a few folks who have been deterred from acting precipitously 
because they are concerned that lawyers might become unhappy with them.

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-08T08:05:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7cac49nqbli420l63b0qsp083mmv49khu@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <u6dwk.30047$Fr1.3715@newsfe03.iad> <g9sdlt$apo$1@reader1.panix.com>`

```
On Fri, 5 Sep 2008 23:00:14 +0000 (UTC), docdwarf@panix.com () wrote:

>This is Civil Service pay folks are talking about... I don't know about 
>California but I have been told that there are certain aspects of 
…[3 more quoted lines elided]…
>case in California.

That can be a problem.   How often do programmers consult lawyers when
our bosses have us make changes to our code?   At least we are being
told some of our new privacy and security needs, but the law is big
and complex.
```

###### ↳ ↳ ↳ Re: Odd doings in California

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-08T17:20:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ga3mtd$n3k$1@reader1.panix.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <u6dwk.30047$Fr1.3715@newsfe03.iad> <g9sdlt$apo$1@reader1.panix.com> <c7cac49nqbli420l63b0qsp083mmv49khu@4ax.com>`

```
In article <c7cac49nqbli420l63b0qsp083mmv49khu@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Fri, 5 Sep 2008 23:00:14 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[10 more quoted lines elided]…
>and complex.

That 'the law is big and complex' what I've been trying to express, Mr 
Brazee... and the responses from those purporting to be Professional 
Programmers that boil down to 'all ya gotta do is' have been a bit 
disheartening.  I've sat in meetings where Corner Office Idiots have said 
'We're getting complaints from users about (situation)' and a business 
analyst has retorted with 'If they complain then show them this bulletin 
from Legal saying these are the new regs; if the supervisors want to do 
manual overrides and violate these regs remind them there are audit 
trails.'

DD
```

###### ↳ ↳ ↳ Re: Odd doings in California

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-05T18:48:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<big3c4pm3c8eks3gchi1pckuqhms4n1sjc@4ax.com>`
- **References:** `<nq2wk.36210$Rs1.36033@newsfe08.iad> <gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com> <u6dwk.30047$Fr1.3715@newsfe03.iad>`

```
On Fri, 5 Sep 2008 11:27:41 -0500, "tlmfru" <lacey@mts.net> wrote:

>Why use contractors?  There must be people maintaining the system.

Their time is committed to meetings (LOTS of meetings), long lunches, personal days off,
seminars, mandatory process training, etc. They don't have time to do real work. Why do
you think anyone hires contractors?

>Select workers for the task - 1 week
>Analysis - 1 week because they know the system
…[10 more quoted lines elided]…
>Total,  6 weeks.

No no. You start with the timeframe, say six months. Apply the front-end and back-end
activities. Whatever is left in the middle is the budget for development. Complexity has
nothing to do with it. A one line change gets the same budget as a rewrite. I've even seen
the development budget go negative. When that happens, they shrink the 'formal' plan to
show one week for development while leaving the 'working' plan negative. 

>It looks to me as though the I/T people, particularly management, just don't
>want to do it because of the messes that will result - not programming
>messes, but personal, institutional, and political.

Politics in a state agency? Sacre bleu, bite your tongue.

>Robert <no@e.mail> wrote in message
>news:gnd1c4trsc8kgqg6po1vrnj5ffvtuussen@4ax.com...
…[22 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
