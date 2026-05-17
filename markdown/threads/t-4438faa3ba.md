[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How important is speed?

_71 messages · 33 participants · 1997-11 → 1997-12_

---

### How important is speed?

- **From:** "bernard liengme" <ua-author-10711005@usenetarchives.gap>
- **Date:** 1997-11-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<347616F0.58BBCE18@stfx.ca>`

```

This is a multi-part message in MIME format.
--------------8260EDDAF82CE876370698A9
Content-Type: text/plain; charset=us-ascii
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Content-Transfer-Encoding: 7bit

A question from an academic to the front line workers. I sometimes refer
to a Cobol textbook written in 1991. While it answers many questions
that other books do not, the author seems to be very preoccupied by
speed. For example, he mentions that using INSPECT CONVERTING is 25%
slower on a PC that INSPECT REPLACING 'a' by 'A, 'b' by 'B' .... (Yes, I
know about the UPPER-CASE function). My question is: when you write a
data processing program to run on a modern computer how concerned are
you about speed? Does it really matter if it takes 10 mins or 12 mins to
generate a payroll check file when the printing will take hours? Now,
guys and gals, let's not have flaming. I just want info. to help me be a
better teacher.


--------------8260EDDAF82CE876370698A9
Content-Type: text/x-vcard; charset=us-ascii; name="vcard.vcf"
Content-Transfer-Encoding: 7bit
Content-Description: Card for Bernard V Liengme
Content-Disposition: attachment; filename="vcard.vcf"

begin: vcard
fn: Bernard V Liengme
n: Liengme;Bernard V
org: St Francis Xavier University
email;internet: bli··.@st··x.ca
x-mozilla-cpt: ;0
x-mozilla-html: TRUE
end: vcard


--------------8260EDDAF82CE876370698A9--
```

#### ↳ Re: How important is speed?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-20T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p2@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Bernard Liengme wrote:
› [snippage]
› My question is: when you write a
› data processing program to run on a modern computer how concerned are
› you about speed?

As concerned as the person who signs my timesheet is. As has been said
before, there is a tradeoff between speed of execution and
maintainability of code but... do you want the archetypical two-year
programmer maintaining a pentadimensional array? I have worked in shop
where I've been directly ordered to write records to a temporary VSAM
file because the project leader did not 'like' (read: understand) a
shell-sort loading a table to be addressed by a SEARCH ALL. Yes, it is
ugly, yes, it is foolish, yes, it is inefficient... yes, my timesheet
got signed that week.

In general the need for speed is directly proportional to transaction
volume and run-frequency... only 24 hours in a day, don'cha know.

DD
```

##### ↳ ↳ Re: How important is speed?

- **From:** "troxle..." <ua-author-8415077@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p2@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p2@usenetarchives.gap>`

```

Bill Lynch wrote:

› The Goobers wrote:
›› 
…[30 more quoted lines elided]…
› Bill Lynch

Good point. For mainframe applications, I've gotten much more
efficient execution process by making changes to the JCL and changing
VSAM or DB2 parameters than spending time trying to make a Cobol
program more efficient.


Tim Oxler
TEO Computer Technologies Inc.
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p3@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p2@usenetarchives.gap> <gap-4438faa3ba-p3@usenetarchives.gap>`

```

On Tue, 25 Nov 1997 16:11:35 GMT, tro··.@i··.net (Tim Oxler)
wrote:

› Bill Lynch  wrote:
› 
…[13 more quoted lines elided]…
› Tim Oxler

If you are using random VSAM access look up batch LSR pools. One
program I had cut down 1 hour to 30 mins by a simple JCL change.

Ken
```

#### ↳ Re: How important is speed?

- **From:** "david virgil" <ua-author-17071569@usenetarchives.gap>
- **Date:** 1997-11-20T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p5@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Speed is always important! Each process has several different ways that it
can be performed. If you choose the least efficient way each time, then
the program will be a real pig! Not any one will cause the problem, but
all of them combined.

Your particular example talks about printing checks for hours. When there
are faster ways, (laser printed checks) to print, do you want to wait on
the system instead of the printer?

Teach your student to always consider how long something will take to code,
maintain and run. Each is important. Sometimes one will out weight the
other.

In "Soul of a New Machine", Tom West from Data General said "Not everything
worth doing is worth doing well". Does that contradict my earlier
statement? No, as long as you always consider the performance issues.

David Virgil
Development Manager
Foxworth-Galbraith Lumber Co.
dvi··.@fox··l.com

Bernard Liengme wrote in article
<347··.@st··x.ca>...
› A question from an academic to the front line workers. I sometimes refer
› to a Cobol textbook written in 1991. While it answers many questions
…[10 more quoted lines elided]…
›
```

##### ↳ ↳ Re: How important is speed?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-21T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p5@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap>`

```

David Virgil wrote:
›
› In "Soul of a New Machine", Tom West from Data General said "Not
› everything worth doing is worth doing well".

I strongly disagree with this statement by Tom West. Everything WORTH doing
IS worth doing well. There is never a time when anything worth doing should
be done less than 'well'. But the parameters defining 'well' are not the
same for every task. Some tasks require a very narrow view of 'well',
virtual perfection (programming flight control systems). For other tasks,
'well' is defined much looser, even for some critical tasks (feeding a baby).
The need for being 'done well' is critical in both cases, but the definition
of 'done well' varies drastically. Nobody appreciates a job poorly done,
even if not important. There is a proverb "One who is unfaithful in little
things will be unfaithful in big things." If you pay careful attention to
people, you will see that this is true.

Of course, there are things people do which are not worth doing, but that is
a different issue.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-11-21T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p6@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap>`

```

Judson D. McClendon wrote in article
<01bcf6f3$a16a10e0$f7db45cf@juddesk>...
› David Virgil  wrote:
›› 
…[7 more quoted lines elided]…
› be done less than 'well'

If I need a small function/subroutine which is used only 1 to 3 percent of
the time, there's no way I'll spend too much time writing it to squeek out
another 10 to 20 percent speed efficiency as long as it works. I'll spend
my time tuning something that runs 20 to 30 percent of the time. That will
give a better payback for the time spent.

snip

Remove the '-glop-' for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-22T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p7@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap>`

```

Eugene A. Pallat wrote:
› 
› Judson D. McClendon  wrote:
…[14 more quoted lines elided]…
› give a better payback for the time spent.

Eugene, you missed my point (and snipped the text which expresses it). It is
not tradeoff decision such as you describe that I disagree with, but the
manner in which those decisions are viewed in Tom West's quote. When he says
"Not everything worth doing is worth doing well" he is looking at the issue
from the wrong perspective. It is the definition of 'doing well' which is
different for each task, not that some tasks need doing well, and some do
not. The low use routines in your example ARE 'done well', even without that
extra 10-20% efficiency, because, as you say, spending more time on them is
not justifiable. Doing a task to the proper degree of correctness,
precision, or extent *that the task merits*, IS 'doing it well'.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p8@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap> <gap-4438faa3ba-p8@usenetarchives.gap>`

```

My question goes back to the original thought for this thread concerning the need for efficency
and what makes for ease of maintance that is also the most efficient at execution.

Which of the following is the most effecient ?

Problem : Address Validation in a Merge/Match routine.
I coded my solution in 1 program as

EVALUATE TRUE
WHEN ADDRESS-LINE-1 NOT EQUAL NEW-ADDRESS-LINE-1
SET ADDRESS-NOT-MATCH-FLAG TO TRUE
WHEN ADDRESS-LINE-2 NOT EQUAL NEW-ADDRESS-LINE-2
SET ADDRESS-NOT-MATCH-FLAG TO TRUE
... 5 OR 6 MORE CONDITIONS
WHEN OTHER
EXECUTE ADDRESS-EQUAL CODE
END-EVALUATE
.....
LATER CHECK ADDRESS-NOT-MATCH-FLAG
EXECUTE ADDRESS-NOT-EQUAL CODE


My collegue coded his compare as a multi conditional IF

IF ADDRESS-LINE-1 = NEW-ADDRESS-LINE-1
AND ADDRESS-LINE-2 = NEW-ADDRESS-LINE-2
AND ... FOR THE REST OF THE CONDITIONS

EXECUTE ADDRESS=EQUAL CODE
ELSE
EXECUTE ADDRESS-NOT-EQUAL CODE
END-IF

My thoughts on the efficency, (and I am asking the Knowlagable Guru's that frequent this page
for a learned opinion on this. :) is that the EVALUATE checks each condition at the time of
execution of each seperate WHEN and executes the first that satisfies the BOOLIEAN Qulifiers.
The Multi-conditional IF on the other hand processes each = condition and then evaluates ALL the
BOOLIEAN Operators and then executes the IF or ELSE. Is this a correct assumption?

Thanks to all

Greg Amos
amo··.@x.n··M.com
Remove .NOSPAM to send E-MAIL
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p9@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap> <gap-4438faa3ba-p8@usenetarchives.gap> <gap-4438faa3ba-p9@usenetarchives.gap>`

```

In article <66ehm9$b.··.@sjx··m.com>,
Gregory Paul Amos wrote:
› 
› EVALUATE TRUE
…[16 more quoted lines elided]…
›       EXECUTE ADDRESS-NOT-EQUAL CODE

The WHEN phrases of an EVALUATE statement can be ORd together. If you
recode your EVALUATE like this:

EVALUATE TRUE

WHEN ADDRESS-LINE-1 NOT EQUAL NEW-ADDRESS-LINE-1
WHEN ADDRESS-LINE-2 NOT EQUAL NEW-ADDRESS-LINE-2
WHEN ...
EXECUTE ADDRESS-NOT-EQUAL CODE

WHEN OTHER
EXECUTE ADDRESS-EQUAL CODE

END-EVALUATE

you will find it of roughly the same efficiency to the equivalent IF-stmt
that I snipped. Some platforms will do one slightly better than the
other, but it is impossible to say which without testing the particular
program on the particular platform, which is hardly worth it.

Note further that you should have organized your DATA DIVISION with
sufficient levels so that you can test the address for equality in a
single relational, e.g., WHEN/IF ADDRESS = NEW-ADDRESS etc.


[...]
› My thoughts on the efficiency, (and I am asking the Knowledgeable
› Gurus that frequent this page for a learned opinion on this.  :) is
…[4 more quoted lines elided]…
› executes the IF or ELSE.  Is this a correct assumption?

No. CoBOL's evaluation of conditional expressions is actually rather
sensible and does not need a guru to understand or explain. The rules
for conditional expressions are the same whether they appear in EVALUATE,
IF, PERFORM, or SEARCH statements.

The conditions are evaluated from left to right (or according to the
parentheses in the expression). If the conditional expression becomes
TRUE at any point in the evaluation, the THEN statement, if any, is
executed without evaluating any further conditions, if any. If the
conditional expression becomes FALSE at any point in the evaluation, the
ELSE statement, if any, is executed without evaluating any further
conditions, if any.

This is what makes it possible to code protective conditions. For
example:

IF WS-COMP-3 IS NUMERIC AND WS-COMP-3 > WS-LOW-LIMIT THEN ...

If WS-COMP-3 is not numeric we do not want to evaluate the relational at
all, because it would abend!


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-12-07T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p9@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap> <gap-4438faa3ba-p8@usenetarchives.gap> <gap-4438faa3ba-p9@usenetarchives.gap>`

```

On Sun, 07 Dec 1997 12:13:02 GMT, Gregory Paul Amos
wrote:

› My question goes back to the original thought for this thread concerning the need for efficency
› and what makes for ease of maintance that is also the most efficient at execution.
…[35 more quoted lines elided]…
› BOOLIEAN Operators and then executes the IF or ELSE. Is this a correct assumption?

how about the following:

evaluate address-line1 = new-address-line1 also
add-line2 = add-line2 also
....
when true also true also true also true

when other
error message

end-evaluate

this may not go very fast... but it has the advantage of being able to
be *very* easily maintainable
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 7)_

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p11@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap> <gap-4438faa3ba-p8@usenetarchives.gap> <gap-4438faa3ba-p9@usenetarchives.gap> <gap-4438faa3ba-p11@usenetarchives.gap>`

```

In article <349··.@nnt··m.com>,
gvw··.@net··m.com (G Moore) wrote:
› 
› In article <66ehm9$b.··.@sjx··m.com>,
…[22 more quoted lines elided]…
›          execute address-equal code
 
›   when other
execute address-not-equal code
[...]
› end-evaluate

Now write the equivalent IF-statement so you can compare the two methods
as requested by the original poster.


PS: in the problem as stated your TRUEs are redundant:

evaluate address-line1 address-line2 ...

when new-address-line1 new-address-line2 ...
execute address-equal code

when other
execute address-not-equal code

end-evaluate


Christopher Westbury     You see things; and you say "Why?"
Midtown Associates       But I dream things that never
15 Fallon Place          were; and I say "Why not?"
Cambridge, MA 02138         --"Back To Methuselah" by George Bernard Shaw
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "bu..." <ua-author-969394@usenetarchives.gap>
- **Date:** 1997-11-23T01:51:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p7@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p5@usenetarchives.gap> <gap-4438faa3ba-p6@usenetarchives.gap> <gap-4438faa3ba-p7@usenetarchives.gap>`

```

In article <01bcf786$80ae5bc0$4ea036cf@alpha>,
"Eugene A. Pallat" wrote:
› 
› Judson D. McClendon  wrote in article
…[29 more quoted lines elided]…
› notice and will send a certified check forthwith.

i agree with Judson. IMHO, if you do it "well" the first time then there
won't be a lot of fine tuning to do later. and if you become used to
doing it that way then you really won't be spending "too much time
writing it to squeek out another 10 to 20 percent speed efficiency".

Rob Canuel

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: How important is speed?

- **From:** "mike salter" <ua-author-17071840@usenetarchives.gap>
- **Date:** 1997-11-20T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p14@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

When you're dealing with a Payroll System, as in your example, readability
and maintainability are much more important than speed. If you're writing
a game program, optimizing for speed becomes more of an issue.

all unsolicited e-mail will be sent to sp··.@pri··t.com
msalter


Bernard Liengme  wrote in article
<347··.@st··x.ca>...
> A question from an academic to the front line workers. I sometimes refer
> to a Cobol textbook written in 1991. While it answers many questions
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How important is speed?

- **From:** "bu..." <ua-author-969394@usenetarchives.gap>
- **Date:** 1997-11-23T01:35:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p14@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p14@usenetarchives.gap>`

```

i disagree about the point of speed in payroll systems or any system.
speed should always be a factor but has to be balanced out with the other
design factors like readability and maintainability. you don't want to
have nightly batch jobs causing delays with starting the online systems
in the morning, do you? you also don't want unmaintainable programs.
and, then, you have to have some extra time if, in case, jobs abend at
night. also, time is gold to companies who lease or are charged back
computer time and services. a 2-minute difference could be a lot. it
may not matter if you only have one program. imagine if you have 30
different programs consecutively running 12 minutes each instead of 10,
that's 1-hour of wasted time. now imagine a big company with a thousand
or more programs processing millions of records. i've worked on a
payroll system and we always try to look for ways to speed up things.
users don't get to request special jobs run at night if it's payroll
night because time is of the essence.

Rob Canuel

In article <01bcf6d7$40ee6ca0$f214a5ce@t4700cs>,
"Mike Salter" wrote:
› 
› When you're dealing with a Payroll System, as in your example, readability
…[21 more quoted lines elided]…
›› 

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "mike salter" <ua-author-17071840@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p15@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p14@usenetarchives.gap> <gap-4438faa3ba-p15@usenetarchives.gap>`

```


bu··.@bel··c.net wrote in article <880··.@dej··s.com>...
› i disagree about the point of speed in payroll systems or any system. 
› speed should always be a factor but has to be balanced out with the other
› design factors like readability and maintainability.  you don't want to
› have nightly batch jobs causing delays with starting the online systems
› in the morning, do you?  you also don't want unmaintainable programs. 

I didn't mean to imply that it's ok to write inefficient code, I just don't
believe that you should spend a lot of time pondering a pmap trying to
squeak out every cycle you can. I think establishing coding standards
based on efficiency are needed however. You can spend a lot of time
tweaking a program for efficiency, and have someone else apply a fix/update
which will blow your efficiency to hell.

› and, then, you have to have some extra time if, in case, jobs abend at
› night.	also, time is gold to companies who lease or are charged back
…[4 more quoted lines elided]…
› or more programs processing millions of records.  i've worked on a

Service bureaus charging for computer time are an antiquated way of doing
business IMHO. If you need Payroll processing services, flat fees are the
way to go. The service bureaus I have dealt with have always been a rip
off, charging high fees for the smallest modifications.

› payroll system and we always try to look for ways to speed up things.
› users don't get to request special jobs run at night if it's payroll
› night because time is of the essence.
›

When I was working on Payroll, I have had to make fixes 10 minutes prior to
a run, and have been glad for readable and easily maintainable code. I
agree with you in part, that it should be a balance, I just think that if
it has to lean one way or the other, I'd prefer it lean toward
maintainability.

Mike
all unsolicited e-mail will be sent to sp··.@pri··t.com
msalter
```

#### ↳ Re: How important is speed?

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-11-21T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p17@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

In article <347··.@st··x.ca>,
Bernard Liengme wrote:
› 
› A question from an academic to the front line workers.  I sometimes
…[6 more quoted lines elided]…
› computer how concerned are you about speed?

I think you will find the attitude of most large corporate data centers
is summed up in the saying: "First make it right, then make it fast".
There's actually a lot more speed retrofitting going on, even in the
stodgiest corporations, than one might think, because in a large
corporation every single job is charged back to some department.

I get two kinds of speed calls: cost reduction and time reduction. The
most common call is a department head, who might ask if I can do anything
about Report X, which is costing him $17,000 a month more than budgeted.
This is straight resource minimization. On the other hand, the nightly
batch might not be getting the ATM balances out there by 6AM on
high-volume days. In this case, they are willing to spend more money per
run to buy an earlier wall-clock completion time.

Now, as to your question, how concerned am I with speed when I write, it
comes down to this: I believe a professional should know what he's doing.

In most business situations there's no need to squeeze out the last
microsecond, but on the other hand, if two techniques take the same
effort to program, and one is more expensive than the other, why not use
the cheaper technique? The answer is, because today's students are not
allowed to know which is the cheaper technique.

Of course, if all you academics started teaching assembly language again,
there would no longer be such a lucrative advantage to being an
old-timer. But I'm betting that won't happen.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: How important is speed?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-22T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p17@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap>`

```

Chris Westbury wrote:
› 
› [snippage of some rather reasonable blathering]
…[4 more quoted lines elided]…
› allowed to know which is the cheaper technique.

Well, I agree with the first sentence (given two alternatives which are
otherwise equal choose the more efficient) but the second one... 'not
allowed to know'? This throws me a bit. Are you saying that beginning
students are not being taught the most advanced techniques... or that
the COBOL Illuminatti are our altering the manuscripts... or is there
something I am missing?

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p18@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap> <gap-4438faa3ba-p18@usenetarchives.gap>`

```

In article <347··.@er··s.com>,
The Goobers wrote:
› 
› In article <1997Nov22.200058.18444@giant>,
…[13 more quoted lines elided]…
› something I am missing?

Since the policy is not to teach students assembly language any more,
they have no way of evaluating the efficiency of a technique for
themselves, and since the tabu against the very mention of efficiency
("It makes no difference on modern machines") has been in effect for so
long that the teachers themselves don't know which technique is the most
efficient, even the rare student who is interested has nowhere to get
this information.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p19@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap> <gap-4438faa3ba-p18@usenetarchives.gap> <gap-4438faa3ba-p19@usenetarchives.gap>`

```

Chris Westbury wrote:
› 
› In article <347··.@er··s.com>,
…[24 more quoted lines elided]…
› this information.

I must humbly and respectfully disagree here... I recall my CICS
refbooks (left, sadly, at a client's site in Kansas City, MO), purchased
a scant two years ago which gave translations and speed-comparisons for
the various ASM breakdown on commands... it is where I learned that the
ratio between MVC and MVI is 3:1. Having not sat in on a class for a
while now I do not know how things are taught nor what is 'tabu' but I
*do* know that the materials are out there for even the most casual
researcher.

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p18@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap> <gap-4438faa3ba-p18@usenetarchives.gap>`

```



The Goobers wrote in article
<347··.@er··s.com>...
› Chris Westbury wrote:
›› 
…[14 more quoted lines elided]…
› 

What matters performance wise is what machine code the COBOL compiles into.
This differes on different platforms/compilers, but the ASM programmer is
taught the most efficient methods, and can actually read the machine code
generated, (or ASM as some compilers will do) to see which of several
methods is the most efficient.
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p21@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap> <gap-4438faa3ba-p18@usenetarchives.gap> <gap-4438faa3ba-p21@usenetarchives.gap>`

```

Thane Hubbell wrote:
...
› 
› What matters performance wise is what machine code the COBOL compiles into.
…[3 more quoted lines elided]…
› methods is the most efficient.

What you are describing here are primarily techniques for local code
optimization. A well designed optimizing compiler can do both local and
global code optimization, and while it may not be able to match an
experienced Assembly coder on local optimization of small code segments,
on a really large application they can potentially do a better job of
global optimization as overall logic flow and variable usage in a
complex, large program is very difficult to track and "understand" via
manual techniques.

Experience teaches that while code optimization improves performance,
some of the most dramatic performance improvements come not from code
optimization but by choice of a better algorithm. No amount of code
optimization will make a Order(n**2) algorithm run better than an
Order(n*log n) algorithm for sufficiently large n. No amount of code
optimization will make a random physical read from an external file run
faster than a random access of a table in real memory, and both are
slower than a record access which is completely avoided.

Given the availability of a number of compilers which can generate
fairly decent object code, you get the most "bang for the buck" by
addressing, in the order listed, (1) which algorithms to use and which
to avoid, (2) which language features should be used with caution
because they can't be optimized well (e.g, explicitly telling the
compiler to do unnecessary data type conversions), and (least important)
(3) those features which perform poorly in a specific compiler you are
forced to use today, but may replace tomorrow.

Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p22@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p17@usenetarchives.gap> <gap-4438faa3ba-p18@usenetarchives.gap> <gap-4438faa3ba-p21@usenetarchives.gap> <gap-4438faa3ba-p22@usenetarchives.gap>`

```

Excellent post, Joel!
```

#### ↳ Re: How important is speed?

- **From:** "frederick pierz" <ua-author-17072432@usenetarchives.gap>
- **Date:** 1997-11-21T19:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p24@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Speed becomes a concern in a professional situation as a product of
productivity. If it takes 12 minutes to produce one pay check and you have
to produce one thousand of them in a specific period of time a two minute
savings is significant. The amount of time it takes to finish a particular
task has a direct impact on the types and amounts of equipment you have
etc., all of which affect the profitability of a company, especially a data
processing service.
```

#### ↳ Re: How important is speed?

- **From:** "nancy mckellar" <ua-author-17072607@usenetarchives.gap>
- **Date:** 1997-11-21T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p25@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Bernard Liengme wrote:
› 
› A question from an academic to the front line workers. I sometimes refer
…[9 more quoted lines elided]…
› better teacher.

Not surprisingly, you're getting a lot of responses quickly. No facts
are needed, only opinions -- and everybody has an opinion.

I couldn't resist, either.

Naturally, the truest answer is: it depends. In some cases you have
to extract every microsecond: games, real-time systems, heavily-loaded
online systems, huge batch cycles which must fit within a narrow
processing window.

For these cases it may be useful to have the kind of exact timing
statistics you describe. However, the numbers are likely to be highly
dependent on the compiler and the system. In addition, they probably
don't belong in an introductory textbook, lest they encourage students
to overemphasize performance issues.

In all the systems I've ever worked on -- mostly batch systems, plus
one smallish CICS system -- raw performance has seldom been an issue.
Usually it's enough to get merely satisfactory performance. Avoiding
disaster is more important than attaining perfection.

Disasters usually come in the form of excessive IO. For example: my
old CICS application needed to produce reports, and the reports
required a sort, but you're not supposed to use the SORT verb within
CICS. My first idea was to write temporarily to a VSAM file, and
let VSAM sort the records as it added them. That was a disaster.
Depending on the number of records, a report might take half an hour
or more. I wound up writing batch jobs to an internal reader,
including the records as in-stream data.

Where IO is not involved, it's usually not worth agonizing over
machine cycles, but there are exceptions. For example: one of my
programs spent most of its time doing linear searches through a
WORKING-STORAGE table with 17,000 entries. I couldn't readily use
SEARCH ALL because the key wasn't unique. I rewrote it to use a
two-stage lookup with two tables. The first stage does a SEARCH
ALL on the first table, using a unique key, to get a subscript into
the second table. The second stage does a linear search through the
second table, starting from that subscript. This version runs much
faster.

(Actually IO was probably a factor here as well. Linear searches
through a big table probably cause a lot of paging.)

Most of us probably have similar war stories to tell.

As a teacher, I would emphasize maintainability, sound structure,
and sound algorithms rather than efficiency. At most I might mention
that IF performance is an issue, you might do some kinds of things
differently, and pay a price in a different coin.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: How important is speed?

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p25@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap>`

```


› Bernard Liengme wrote:
›› 
…[10 more quoted lines elided]…
›› better teacher.

depends on the application.

first of all, never ever, under any circumstances, use bubble sorts.
secondly, it's usually best to use indexed files with fixed field
sizes, because they are easy to collect garbage in.

speed rarely matters in other things... unless you have a technical
application. also, a profiler is very helpful, because, as they say,
10% of hte code takes up 90% of the operation time...
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p26@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap>`

```

G Moore wrote:
› 
›› Bernard Liengme wrote:
…[15 more quoted lines elided]…
› first of all, never ever, under any circumstances, use bubble sorts.

Even when sorting a table with a maximum of 8 to 10 entries? For a table
this small, not only can Bubble Sort be as fast as Quicksort or Shell Sort,
it can even be faster (less setup overhead), and is simpler to code. As you
said, it depends on the application. ;-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "je..." <ua-author-6589243@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p27@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap>`

```

"Judson McClendon" wrote:

› G Moore  wrote:
›› 
…[21 more quoted lines elided]…
› said, it depends on the application.  ;-)

There's a lot to be said for always using a bubble sort as the first
"pass" of the data, just in case it is in sequence already.. If it
is, then you skip any further sort phases.. IIRC heapsort is
actually quite a bit slower on ordered data than random..
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p27@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap>`

```

In article <01bcf8de$448dc0a0$4134b9ce@juddesk>,
Judson McClendon wrote:
› G Moore wrote:
››
›› first of all, never ever, under any circumstances, use bubble sorts.
›
› Even when sorting a table with a maximum of 8 to 10 entries?

Alright, then, let's nip this one in the bud and amend it to:

'First of all, never ever, under any circumstances, say 'never''.

There... everyone happy now?

.... or is it true that some folks... 'never' are?

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p29@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap>`

```

doc··.@cl··k.net wrote:
› 
› In article <01bcf8de$448dc0a0$4134b9ce@juddesk>,
…[12 more quoted lines elided]…
› 
...
If you want a trivial, simple sort for less than, say, 10 - 20 entries,
the Insertion Sort is easier to describe, as easy to implement, and
involves less data movement than a Bubble Sort. Even some of the
"snazzier" divide & conquer sorts fall back on the Insertion Sort once
they get down to short lists of that size. A Bubble Sort is the worst
of the "simple" sorts. The only reasonable exception to G. Moore's
"never" in the case of the bubble sort is when you want to give an
example of a bad algorithm! It should never be used in new production
code, or in sample code which might be cloned by a novice for new
production code. Unfortunately you can still find introductory
programming texts which illustrate sorting with a Bubble Sort,
encouraging those who fail to explore further to regard this as a
"reasonable" sort, which it is not.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p30@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap>`

```

Joel C. Ewing wrote:
› 
› doc··.@cl··k.net wrote:
…[30 more quoted lines elided]…
› Joel C. Ewing, Fort Smith, AR        jce··.@a··.org

Why would anyone code a table sort routine today, other than a student?
I wrote my last sort subroutine in 1975 in assembler and have been using
it ever since. Every shop that I have ever worked in had a general
purpose, efficient, table sort subroutine callable from COBOL.

Wayne L. Beavers         mailto:Way··.@Bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"Transforming Legacy Applications"
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 7)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p31@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p31@usenetarchives.gap>`

```

Wayne L. Beavers wrote:
›
› Why would anyone code a table sort routine today, other than a student?

I agree... but, if my enfeebled memory serves, this thread originated
with a question posed by an academician.

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 7)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p31@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p31@usenetarchives.gap>`

```

Wayne L. Beavers wrote:
› 
› Why would anyone code a table sort routine today, other than a student?
› I wrote my last sort subroutine in 1975 in assembler and have been using
› it ever since. Every shop that I have ever worked in had a general
› purpose, efficient, table sort subroutine callable from COBOL.

Why doesn't Cobol have:

SORT table-name [ASCENDING|DESCENDING [KEY] DATANAME] ...

In the simplest case -- SORT table-name -- the compiler would pick up
the key from the data definition. The table could be variable in size
(OCCURS DEPENDING).
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 8)_

- **From:** "trevor powdrell" <ua-author-17072182@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p33@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p31@usenetarchives.gap> <gap-4438faa3ba-p33@usenetarchives.gap>`

```

RandallBart wrote:
› 
› Wayne L. Beavers wrote:
…[12 more quoted lines elided]…
› (OCCURS DEPENDING).

I believe this is in the next Cobol standard.



› --
› I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
…[6 more quoted lines elided]…
› u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html

Trevor Powdrell
tpo··.@ker··r.net
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 8)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p33@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p31@usenetarchives.gap> <gap-4438faa3ba-p33@usenetarchives.gap>`

```



RandallBart wrote in article
<65ffen$k.··.@bgt··t.net>...
› Wayne L. Beavers wrote:
›› 
…[12 more quoted lines elided]…
› (OCCURS DEPENDING).


On the PC Micro Focus COBOL allows this and I have used it with great
success.
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p30@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap>`

```

Joel C. Ewing wrote:
› 
› doc··.@cl··k.net wrote:
…[25 more quoted lines elided]…
› "reasonable" sort, which it is not.

Joel, you are leaving out one important point. A simple bubble sort is the
easiest and simplest sort there is. Insertion sort is NOT as easy to
implement, but can be much trickier to code and debug. Especially for a
programmer who seldom writes sorts. I'll bet there isn't an experienced
programmer alive who hasn't over-run or under-run an array, or duplicated an
entry, while debugging an insertion sort. And I didn't say 10-20 entries, I
said MAX 8-10 entries. Figure it out sometime, or time it. If bubble sort
is not as fast (or faster) on < 10 entries, the difference is a non issue,
except in the most time critical situations. A 'bad algorithm' is an
algorithm which is poorly suited to the task. For a tiny sort like this, the
*simplest sort* is the best algorithm, because time and storage are
irrelevant. The reason introductory texts include bubble sort is because it
is the simplest sort there is, and it is intuitive. *This* is also the
reason programmers keep on using bubble sort, even when it is a terrible
choice. There's nothing wrong with showing it as a beginning example, so
long as you clearly point out how slow it is for anything but the smallest
sorts, and immediately move on to better algorithms.

I acknowledge that there are probably a few programming issues where you can
say "absolutely never", or "absolutely always". But in the vast majority of
programming issues, it is wiser to be more open minded. Even very weak tools
can be useful, and even excel, in the right situation. A "knee jerk"
reaction to totally reject any algorithm, simply means you miss the
opportunity to take advantage of it in those situations where it can be
beneficial. Why risk spending extra time and energy, simply because you have
blocked your thinking to a range of options? An open mind doesn't cost
anything. You might consider that one of the marks of genius is looking at
things in new ways, which most people have unconsciously blocked.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 7)_

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p36@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p36@usenetarchives.gap>`

```

Judson McClendon wrote:
› 
› Joel, you are leaving out one important point.  A simple bubble sort is the
…[4 more quoted lines elided]…
› entry, while debugging an insertion sort.  And I didn't say 10-20 entries, I

Admittedly a subjective judgement, but I think the only reason many
would think an insertion sort more complex is because it was not the
first sort to which they were introduced. A bubble sort has exactly the
same potential for messing up loop bounds (and I've seen it done), and
I've even seen beginning programmers mess up the interchange process.
Trying to explain the bubble sort interchange process and why it will
eventually give you a sorted array gets just as many blank stares from
someone who has never seen a sort algorithm before. What can be
conceptually simpler to describe for one pass than to "take the next
value and insert it into the correct place in your list of values sorted
so far". Trying to describe the array transformation resulting from one
pass of a bubble sort is complex by comparison.

› said MAX 8-10 entries.  Figure it out sometime, or time it.  If bubble sort
› is not as fast (or faster) on < 10 entries, the difference is a non issue,
…[9 more quoted lines elided]…
› 
...
I have seen too many cases where a programmer used a "quick & dirty"
approach because for the volume of data involved "it didn't matter".
Then the next month the end user's requirements or style of usage
changed and suddenly the number of entries increased and it did matter
-- but of course it's very difficult to get the code changed because it
"works" and now the deadline is on another project. Outside of an
academic environment, one must expect requirement creep over time and
should plan ahead for it where the cost is minimal.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 8)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p38@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p37@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p36@usenetarchives.gap> <gap-4438faa3ba-p37@usenetarchives.gap>`

```

Joel C. Ewing wrote:
› [snippage]
› I have seen too many cases where a programmer used a "quick & dirty"
…[6 more quoted lines elided]…
› should plan ahead for it where the cost is minimal.

Ding ding ding... now *here* is a problem! 'Requirement creep' happens,
granted; I always laugh when someone asks for a real q-n-d to be done
'just this once'... because I have seen too many 'just this onces' wind
up as daily prod jobs.

On the other hand... the structure of a program and the techniques used
*are*, I would say, dependent on expected transaction volume; different
amounts of data passing through some code demand different techniques of
handling them... *just* like one obtains a different vehicle for
transporting different numbers of people (VW beetle versus a bus, and
everything in-between). It is simple enough to see that after you are
regularly transporting a certain number of folks a certain vehicle will
no longer be appropriate... you gotta go from a sedan to a station-wagon
('estate wagon' for some).

So, then, since one size cannot fit all and there will come a point when
time must be set aside to redesign an application to fit new
circumstances... *whose* job does it become to deal with the situation?
The answer is, in my opinion, two-fold:

1) The programmer should always, as a matter of Good Practise, ask what
the anticipated transaction-volume is: how many people will we be
calculating payroll for? how many departments do we have to crunch a
budget for? how many widgets/day can we ship? ... and then code for a
system 50 - 75% larger than that. When, in the programmer's
professional opinion, the volume of data becomes inappropriate for the
present design of the system, it is time to notify the manager that the
tool (program) which sufficed up to this point is no longer appropriate
to the task and that (n) amount of time and money must be allocated to
redesign, test and install.

2) The manager then can do a variety of things... and most of the
managers I have seen will say 'yeas, sure, right right right, hey, it is
working *this* way, all-ya-gotta-do-is'... in short, the manager will
avoid a structured approach to redesigning the job, preferring to wait
until the thing blows up in Prod at 3:am and then criticizing the
programmer for sloppy work. (yes, I know that this is not necessarily
what happens; it is what I have *seen* happen, with dreary regularity...
your mileage may vary, of course).

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 8)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p39@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p37@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p25@usenetarchives.gap> <gap-4438faa3ba-p26@usenetarchives.gap> <gap-4438faa3ba-p27@usenetarchives.gap> <gap-4438faa3ba-p29@usenetarchives.gap> <gap-4438faa3ba-p30@usenetarchives.gap> <gap-4438faa3ba-p36@usenetarchives.gap> <gap-4438faa3ba-p37@usenetarchives.gap>`

```

Joel C. Ewing wrote:
› 
› I have seen too many cases where a programmer used a "quick & dirty"
…[6 more quoted lines elided]…
› should plan ahead for it where the cost is minimal.

Selecting a suitable algorithm is a design decision which must be made
appropriately. Would you exclude all algorithms which could be misused on
this premise? I believe labeling an algorithm as "quick & dirty" in a
general sense is inappropriate. That kind of judgment should only be made in
consideration of its suitability to a given task. Carrying your point to
it's logical conclusion, one must always choose the most robust solution
available, no matter the cost or forseeable need.

It is not specifically bubble sort which I am trying to defend, but I
disagree with the practice of excluding certain algorithms out of hand. I
personally don't use bubble sort, but use insertion sort, Shell sort, or
Quicksort, depending on table size and key characteristics. But I don't
agree with censuring some programmer who uses bubble sort for a very tiny
table.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: How important is speed?

- **From:** "the..." <ua-author-96015@usenetarchives.gap>
- **Date:** 1997-11-22T19:00:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p40@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

› Subject: How important is speed?
› From: Bernard Liengme 
…[13 more quoted lines elided]…
› better teacher

Several references on the subject from the ACM publications follow:

*** 1 ***

Impact of system response time on state anxiety

Jan L. Guynes


Communications of the ACM
Vol. 31, No. 3 (March 1988), Pages 342-347

[Index Terms] ..... [Review]



------------------------------------------------------------------------




General Terms

HUMAN FACTORS, PERFORMANCE

Categories and Subject Descriptors


H.1.2Information Systems, MODELS AND PRINCIPLES, User/Machine Systems, Human
factors.K.6.0Computing Milieux, MANAGEMENT OF COMPUTING AND INFORMATION
SYSTEMS, General.



------------------------------------------------------------------------




>From Computing Reviews



J. Fedorowicz


This paper reports on a study conducted to test the effect of system response
time on the state anxiety of the end user. The author predicts that type A
personalities, those "composed primarily of competitiveness, excessive drive,
and an enhanced sense of time urgency" (p. 342) would exhibit greater state
anxiety when encountering long or inconsistent system response times.

Eighty-six subjects participated in the experiments. Three treatment groups
completed tasks with good, variable, or poor response times. (The good response
times were defined as less than 5 seconds, which, with today's technology,
might be less than acceptable.)

Analysis of the data shows that there was a significant positive relationship
between response time and state anxiety, but personality type was not a
contributing factor toward this relationship. That is, type A personalities did
not exhibit a larger increase in state anxiety than type B personalities. In
addition, those subjects in the poor treatment group exhibited the largest
increase in state anxiety overall.

This study was designed and conducted well. The findings, although not
tremendously surprising, demonstrate that response time is a major concern for
all system users. It should therefore be a major issue for designers as well.

*** 2 ***

Lag as a determinant of human performance in interactive systems

I. Scott MacKenzie
Colin Ware

in: CHI '93. Conference proceedings on Human factors in computing systems,
pages 488-493


[Abstract] ..... [Index Terms]
[Full Text in PDF Format, 551 KB]



------------------------------------------------------------------------




Abstract




The sources of lag (the delay between input action and output response) and its
effects on human performance are discussed. We measured the effects in a study
of target acquisition using the classic Fitts' law paradigm with the addition
of four lag conditions. At the highest lag tested (225 ms), movement times and
error rates increased by 64% and 214% respectively, compared to the zero lag
condition. We propose a model according to which lag should have a
multiplicative effect on Fitts' index of difficulty. The model accounts for 94%
of the variance and is better than alternative models which propose only an
additive effect for lag. The implications for the design of virtual reality
systems are discussed.


------------------------------------------------------------------------




General Terms

DESIGN, HUMAN FACTORS, MEASUREMENT, PERFORMANCE

Categories and Subject Descriptors


H.1.2Information Systems, MODELS AND PRINCIPLES, User/Machine Systems, Human
factors.H.5.2Information Systems, INFORMATION INTERFACES AND PRESENTATION, User
Interfaces, Interaction styles.H.5.1Information Systems, INFORMATION INTERFACES
AND PRESENTATION, Multimedia Information Systems, Artificial, augmented, and
virtual realities.

*** 3 ***

Survey on user interface programming

Brad A. Myers
Mary Beth Rosson

in: CHI '92. Conference proceedings on Human factors in computing systems,
pages 195-202


[Abstract] ..... [Index Terms]
[Full Text in PDF Format, 1074 KB]



------------------------------------------------------------------------




Abstract




This paper reports on the results of a survey of user interface programming.
The survey was widely distributed, and we received 74 responses. The results
show that in today's applications, an average of 48% of the code is devoted to
the user interface portion. The average time spent on the user interface
portion is 45% during the design phase, 50% during the implementation phase,
and 37% during the maintenance phase. 34% of the systems were implemented using
a toolkit, 27% used a UIMS, 14% used an interface builder, and 26% used no
tools. This appears to be because the toolkit systems had more sophisticated
user interfaces. The projects using UIMSs or interface builders spent the least
percent of time and code on the user interface (around 41%) suggesting that
these tools are effective. In general, people were happy with the tools they
used, especially the graphical interface builders. The most common problems
people reported when developing a user interface included getting users'
requirements, writing help text, achieving consistency, learning how to use the
tools, getting acceptable performance, and communicating among various parts of
the program.


------------------------------------------------------------------------




General Terms

DESIGN, HUMAN FACTORS

Categories and Subject Descriptors


H.5.2Information Systems, INFORMATION INTERFACES AND PRESENTATION, User
Interfaces, User interface management systems (UIMS).H.5.2Information Systems,
INFORMATION INTERFACES AND PRESENTATION, User Interfaces, Interaction
styles.D.2.2Software, SOFTWARE ENGINEERING, Design Tools and Techniques, User
interfaces.
```

##### ↳ ↳ Re: How important is speed?

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p41@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p40@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p40@usenetarchives.gap>`

```

› Subject: How important is speed?
› From: Bernard Liengme 
…[13 more quoted lines elided]…
› better teacher

It's really a question of balance. Most of us work at sites where
there are predefined standards that we write to.

For various reasons (not necessarily valid ones) particular constructs
are encouraged or discouraged. Thus, efficiency considerations are
taken out of our hands to a greater or lesser degree.

Personally, I prefer to make a program as quick in execution as it can
be, without going too much out of my way. This is an instinctive
process (been doing it for a long time) where execution speed is only
one of the considerations, legibility and comprehension also being
major influences.

In addition to this, many of us work on large mainframe systems that
are executing countless (millions of?) programs every day. So, in
direct answer to your question, some of us still prefer our programs
to execute as rapidly as possible so that the system resources are not
put under undue stress.

The cheque file generator, that you illustrate your question with, may
run for 10-12 minutes and the print for hours but it is still
relatively important to get the generator off the machine as soon as
possible to make way for other processing. Much of this type of
program runs to a deadline (usually overnight to clear the system for
online processing during the daytime) and is not the only overnight
process.

The daytime online processing doesn't need to be slowed down by long
batch processes and it may actually rely on the overnight processes
being finished before it can be used. Much of this concept is being
minimised as we reduce the number of reports (i.e. any printing) that
are generated. Incidentally, the Y2K problem has provided a focus for
such an exercise where the _need_ for each report is being seriously
questioned.

To me, your cheque writing example is a classic case in point. In the
UK, as in many countries, large corporations rarely pay by cheque any
more. The cheque writing program will now generate electronic
payments which, because of the banking system works, are written to a
file that has to be transmitted before a certain time so that the
transfers can be effected that night. Transmission of these transfers
is not necessarily down the wire, either, but frequently by magnetic
tape that has to be hand carried to a specific location that may not
be five minutes away. So, in this case, we are probably running to an
even tighter deadline than we would have done with producing cheques
and getting them mailed; an hour's delay is not acceptable if it means
missing the banks' acceptance times, whereas an hour's delay in
mailing would not be so tragic. Anyway, the nett result is that more
batch processing is becoming time critical and the cost of hardware is
still significant.

Even on PCs, the efficiency question should be posed. How many of us
have a PC that is no larger than it was ten years ago? Not many
because of the additional demands made on it. Ten years ago, I had an
IBM AT/X with a 286 running at 8Mhz with 640K RAM and 32mb disk. On
the machine that I am using for this posting (yes I have more than
one) I have an AMD K6-PR233, 64mb RAM and 8+Gb disk space. Am I doing
more on it than I was ten years ago? Yes and no. I still do
development work but my C compiler now takes up almost 500mb on disk
with all of its bits and pieces. I still do the usual "office" things
but this now takes up many times the amount of disk space than it did
ten years ago, for various reasons. And the list goes on.

We are constantly told that hardware is cheap, memory is cheap, disks
are cheap. Put yourself in the position of the guy who has $200 to
spend on his PC. Your software upgrade runs a lot slower than the
previous release, it uses more disk space for the programs, and more
disk space for data storage. What do you upgrade? Obviously, you
can't do the memory and the disk and the processor - not on $200.

I think it our responsibility as programmers to make our software run
as fast as possible. We are constrained, however, by other factors
such as the pressure to get more done in less time. I think that,
when I win the Lottery, I might just sit down and develop a version of
Windows (for instance) that fulfils all the functionality of Windows
and yet takes up less disk space, less memory, less processor time and
takes less liberties with our systems. Why? Just to prove a point,
but then I'll be able to afford to. Whether I use C, COBOL or
Assembly for the job is a decison yet to be made.

Back to original question, how important is speed? I believe it to be
very important but there re many out there who don't. In practice, it
is only one of the factors in achieving a well balanced system.


Charles F Hankel
------------------------------------------------------
COBOLs: IBM D, E, F, ANS v4, VS, COBOL 2, LE/370, AIX
Honeywell GCOS, Burroughs 7000, Tandem, HP3000
all to varying degrees over the past 25 years
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p42@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p41@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p40@usenetarchives.gap> <gap-4438faa3ba-p41@usenetarchives.gap>`

```

On Sun, 30 Nov 1997 13:12:56 GMT, cha··.@han··o.uk
(Charles F Hankel) wrote:

› 
› We are constantly told that hardware is cheap, memory is cheap, disks
…[4 more quoted lines elided]…
› can't do the memory and the disk and the processor - not on $200.

actually, i think the *real* problem of software is to make it more
thread / memory oriented. speed is often hard to implement, but if you
can do tasks in the background, your *important* tasks get done right
away, while non-important ones are left to process later...

the tradeoff point i think is virtual memory. if you cannot control
directly which is and is not allowed to be paged to disk, you have
lost the battle.
```

##### ↳ ↳ Re: How important is speed?

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p43@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p40@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p40@usenetarchives.gap>`

```

› Subject: How important is speed?
› From: Bernard Liengme 
…[13 more quoted lines elided]…
› better teacher

It's really a question of balance. Most of us work at sites where
there are predefined standards that we write to.

For various reasons (not necessarily valid ones) particular constructs
are encouraged or discouraged. Thus, efficiency considerations are
taken out of our hands to a greater or lesser degree.

Personally, I prefer to make a program as quick in execution as it can
be, without going too much out of my way. This is an instinctive
process (been doing it for a long time) where execution speed is only
one of the considerations, legibility and comprehension also being
major influences.

In addition to this, many of us work on large mainframe systems that
are executing countless (millions of?) programs every day. So, in
direct answer to your question, some of us still prefer our programs
to execute as rapidly as possible so that the system resources are not
put under undue stress.

The cheque file generator, that you illustrate your question with, may
run for 10-12 minutes and the print for hours but it is still
relatively important to get the generator off the machine as soon as
possible to make way for other processing. Much of this type of
program runs to a deadline (usually overnight to clear the system for
online processing during the daytime) and is not the only overnight
process.

The daytime online processing doesn't need to be slowed down by long
batch processes and it may actually rely on the overnight processes
being finished before it can be used. Much of this concept is being
minimised as we reduce the number of reports (i.e. any printing) that
are generated. Incidentally, the Y2K problem has provided a focus for
such an exercise where the _need_ for each report is being seriously
questioned.

To me, your cheque writing example is a classic case in point. In the
UK, as in many countries, large corporations rarely pay by cheque any
more. The cheque writing program will now generate electronic
payments which, because of the banking system works, are written to a
file that has to be transmitted before a certain time so that the
transfers can be effected that night. Transmission of these transfers
is not necessarily down the wire, either, but frequently by magnetic
tape that has to be hand carried to a specific location that may not
be five minutes away. So, in this case, we are probably running to an
even tighter deadline than we would have done with producing cheques
and getting them mailed; an hour's delay is not acceptable if it means
missing the banks' acceptance times, whereas an hour's delay in
mailing would not be so tragic. Anyway, the nett result is that more
batch processing is becoming time critical and the cost of hardware is
still significant.

Even on PCs, the efficiency question should be posed. How many of us
have a PC that is no larger than it was ten years ago? Not many
because of the additional demands made on it. Ten years ago, I had an
IBM AT/X with a 286 running at 8Mhz with 640K RAM and 32mb disk. On
the machine that I am using for this posting (yes I have more than
one) I have an AMD K6-PR233, 64mb RAM and 8+Gb disk space. Am I doing
more on it than I was ten years ago? Yes and no. I still do
development work but my C compiler now takes up almost 500mb on disk
with all of its bits and pieces. I still do the usual "office" things
but this now takes up many times the amount of disk space than it did
ten years ago, for various reasons. And the list goes on.

We are constantly told that hardware is cheap, memory is cheap, disks
are cheap. Put yourself in the position of the guy who has $200 to
spend on his PC. Your software upgrade runs a lot slower than the
previous release, it uses more disk space for the programs, and more
disk space for data storage. What do you upgrade? Obviously, you
can't do the memory and the disk and the processor - not on $200.

I think it our responsibility as programmers to make our software run
as fast as possible. We are constrained, however, by other factors
such as the pressure to get more done in less time. I think that,
when I win the Lottery, I might just sit down and develop a version of
Windows (for instance) that fulfils all the functionality of Windows
and yet takes up less disk space, less memory, less processor time and
takes less liberties with our systems. Why? Just to prove a point,
but then I'll be able to afford to. Whether I use C, COBOL or
Assembly for the job is a decison yet to be made.

Back to original question, how important is speed? I believe it to be
very important but there re many out there who don't. In practice, it
is only one of the factors in achieving a well balanced system.


Charles F Hankel
--------------------------------------
Hapless FAQer on the Wirral peninsular
```

#### ↳ Re: How important is speed?

- **From:** "the..." <ua-author-96015@usenetarchives.gap>
- **Date:** 1997-11-22T19:00:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p44@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

› Subject: How important is speed?
› From: Bernard Liengme 
…[22 more quoted lines elided]…
› 

Back in the pre-Windows, pre-Client-Server days, when people used to actually
try to objectively measure usability, the Communications of the ACM published a
study that indicated that response time was the single most important
determinant in user satisfaction.

In your example, I really wouldn't sweat over a two minute difference in a
multi-hour process, but all things are relative and the importance of speed
certainly still holds true today.

For example, just being able to get a web page to load in 5 seconds instead of
8 was enough to motivate millions of people to upgrade their 33.6 Kb modems to
56Kb.

In many cases, vendors maintain that speed is unimportant to users when they
release early versions of their products. As their products' deficiencies are
addressed however, the boost in speed is prominently touted as a reason to
upgrade (e.g., VB 5.0, JAVA).
```

##### ↳ ↳ Re: How important is speed?

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p45@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p44@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap>`

```

I agree with the bulk of the posts on the value of speed.
Depends on the application, etc.
One factor of maintainability that should not be
overlooked is the avoidance of arcane or highly specialized
code that some byte-wizard demonstrates as cutting
processor time in half, or something. Everyone signs on
enthusiastically. Then the guru leaves for greener pastures
and no one else can decipher the code. Thus the original
savings of many, many nanoseconds is all wiped out in a
few days of down-time.
If you put in a replacement that runs more slowly, now
everyone is mad because they have been made aware that
there is a faster way. It would have been better to be
slow-running right from the start.
This risk should drive all Businesses to strive for simple and
easy code above speed or efficiency.
An Academic environment is quite different. There, the
objective should be to consider all possible ways, especially
the most elegant and/or interesting ways.
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p46@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p45@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap>`

```

Ross Klatte wrote:
› [snippage]
› One factor of maintainability that should not be
› overlooked is the avoidance of arcane or highly specialized
› code that some byte-wizard demonstrates as cutting
› processor time in half, or something.  

The technical term for this is 'Look, Ma, I'm a Programmer!' code... to
be avoided like the plague.

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-28T19:00:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p47@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p45@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap>`

```

Ross Klatte wrote:
› I agree with the bulk of the posts on the value of speed.  
› Depends on the application, etc.  
…[16 more quoted lines elided]…
› the most elegant and/or interesting ways.  

Ross, I agree with you. Interestingly, on occasion, clients have contacted
me specifically to request that I write such arcane or highly efficient
routines. Once I was asked to write a mainframe COBOL program to print
ultrasound graphs on an HP laser printer attached to a PC running terminal
emulation. The program ran on an EBCDIC mainframe, and the 8 bit graphics
data was sent over an ASCII 7 bit data line to the ASCII PC. Before writing
the application code, I first had to write a complete graphics package in
COBOL, including primitives like plot, draw line, draw character and shading.
Then I had to take the resultant graphics memory image, convert it into
strings of 7 bit and 8 bit binary graphics commands for the HP, split the 8
bit part of the data stream into 6 bit pieces, convert the 6 bit pieces into
printable EBCDIC characters which would translate during transmission into
printable ASCII characters that could be bit-shifted to produce the original
6 bit pieces, which could be assembled into the 8 bit binary graphics command
codes for the HP printer. The shift into and out of this mode had to be
signaled to the PC, because I also had to write a TSR printer driver on the
PC to intercept the data going to the printer. The driver recognized the
transition signals to know when to start shifting the characters into the 6
bit pieces and assembling them into the 8 bit binary data. In cases like
this, I write the code as simply and clearly as possible, and comment
profusely. That's about all you can do, because a task like this just cannot
be done without some arcanery and complexity. Doing it was fun, though. :-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p45@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap>`

```



Ross Klatte wrote in article
<01bcf8f7$c5933220$810··.@MIS··n.com>...
› One factor of maintainability that should not be 
› overlooked is the avoidance of arcane or highly specialized 
…[5 more quoted lines elided]…
› few days of down-time.  

Ross,

That brings up an interesting point. Of all the programmers here, I am the
most conversant with the Ansi 85 extensions to the language, and I make use
of them. The others stick generally with the old '74 methods, shun inline
performs and explicit scope terminators, use perform thru and like to use
GO TO. My style is different. I can crank out code very quickly, and it
works - for the most part - the firs time.

Now all that said, I also know some "tricks" that speed things up. These
are more design level issues than cryptic "stupid COBOL tricks", but I make
use of them.

Should I code for the least common denominator? Even some of the simple
Ansi '85 COBOL constructs (evaluate with ALSO for example) baffle some of
the staff. Should I not use them? Should I be restricted by the lack of
experience of the current staff? What do you think?
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p49@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

In article <01bcfe68$041b8ea0$4b752581@thane-hubbell>,
Thane Hubbell wrote:
›
› [snippage]
›
› Should I code for the least common denominator?

In a quite, understated way let me say... YES! Unless the situation
requires it (and very, very few do) one should *always* code for a
maintenance-programmer with two years' worth of experience.

I pride myself on writing code so straightforward, so simple, so elegantly
inelegant (!) that even a corner-office PHM who hasn't touched an ISPF
editor in a decade will look at it and say 'This is so *easy*... why are
we paying you all this money to write stuff that is so simple?'

... to which I respond 'Do you know how hard it is to write simple code?'

The acronym is KISS... Keep It Simple, Stupid.

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "han..." <ua-author-8441900@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p50@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p49@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p49@usenetarchives.gap>`

```

On 1 Dec 1997 16:08:49 GMT, doc··.@cl··k.net () dreamed up a
literary gem, but posted this instead:

› In article <01bcfe68$041b8ea0$4b752581@thane-hubbell>,
› Thane Hubbell  wrote:
…[16 more quoted lines elided]…
› The acronym is KISS... Keep It Simple, Stupid.

I'm inclined to go along with this view. Some of the more "modern"
constructs require rather more decoding in a maintenance environment
than is necessary.

For example, today I am looking at a program that uses all of the
features of end dlimiters, inline performs, etc. Sadly, there are no
comments at all within the PROCEDURE DIVISION, and only a brief intro
at the top of the prog. Therefore, readability of the code is more
important than my own preferred method.

There are several CALLs to I-O and other routines that require
checking a return code. This guy religiously uses EVALUATE for all of
his checking in the following manner:

CALL routine-x USING (parameter list).
EVALUATE return-code
WHEN SPACES
CONTINUE
WHEN OTHER
several lines of error message displays
CALL USERDUMP
END-EVALUATE.
XX-EXIT.
EXIT.

What I don't like about this is that I have to evaluate the entire
EVALUATE statement only to discover that SPACES are OK and everything
else is not. So, why not just say so in the program with something
like:

CALL routine-x USING (parameter list).
IF return-code = SPACES
GO TO XX-EXIT.
several lines of error message displays.
CALL USERDUMP.
XX-EXIT.
EXIT.

It tells me straight away that SPACES are OK and all else is not
desired for the continued well-being of the program's execution. I am
sure, also, that it is quicker in execution. A reasonable example of
efficiency and readability.

Charles

----------------
Old and past it?
Not any more
----------------
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p51@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p50@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p49@usenetarchives.gap> <gap-4438faa3ba-p50@usenetarchives.gap>`

```

On Tue, 02 Dec 1997 10:20:02 GMT, han··.@mis··o.uk (Charles F
Hankel) wrote (in reference to something else):

› There are several CALLs to I-O and other routines that require
› checking a return code.  This guy religiously uses EVALUATE for all of
…[4 more quoted lines elided]…
›     WHEN SPACES

I'm sorry, but it's right here that I give up on this dude's code
-- anybody who would return a space as a return code is an idiot!

›         CONTINUE
›     WHEN OTHER
…[22 more quoted lines elided]…
› efficiency and readability.

Huh? While the idiot used a SPACE as a return code, the EVALUATE
is crystal clear in its intention.

I am being churlish this evening.
Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p52@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› That brings up an interesting point.  Of all the programmers here, I am the
…[13 more quoted lines elided]…
› experience of the current staff?  What do you think?

That's an interesting point. As a consultant, I am faced with the same
decision. Fortunately, I am often in a position to define standards. But
the way I look at it, if you program too far beyond what the other staff
understands, it becomes a readability and maintainability issue. Even though
the 'fault' may be lack of knowledge in the other staff, you have to take
into consideration the 'target audience', just as you would for a user
interface. Perhaps a good compromise would be to use those advanced
constructs when needed, but also add comments to explain what each use does.
This way, the others can learn from it.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p53@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Ross Klatte  wrote in article
…[26 more quoted lines elided]…
› experience of the current staff?  What do you think?


I don't think that a programmer should refrain from using the new
features available in any new standard of COBOL just because others
haven't used them. It takes time (sometimes a lot) to see wide-use of a
new COBOL feature. Once an individual sees the merit of some of the
features, they generally use some of them. The whole purpose of
introducing new COBOL features is, many times, an attempt to reduce the
coding burden. One of the biggest examples I have noticed in years past
is how many programmers did not know about the existence of the
STRING/UNSTRING verbs. They wrote their own code for this. I have
converted many user-written routines to STRING/UNSTRING. I've also
introduced it to many programmers and none of them misunderstood the
merits of using it.

Some never progress beyond, for example, the '74 COBOL standard. I
don't think it's a good idea to not stay current, but to each his own.
It will take years to convert all of tye pre-85 COBOL stuff out there
(at least on the IBM mainframe). This will contribute to slowing people
down from investigating new COBOL standards. And, of course, your own
organization's support (or lack of) and efforts to promote new COBOL
standards affects the situation.

As for good programming habits, either you've got them or you don't. In
my experience, it's something like learning good manners at an early
age--sometimes very hard to change later in life (not to be confused
with getting more cranky and opinionated as you turn into a grey-haired
geek !!).


Mike Dodas

(Remove cutthejunk for e-mail replies)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p54@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p53@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p53@usenetarchives.gap>`

```

Michael Dodas wrote:
› 
› Thane Hubbell wrote:
…[42 more quoted lines elided]…
› 

Ahhhh, but here I must humbly and respectfully disagree...
STRING/UNSTRING have been in the compiler and the manual for a good bit
of time now, nothing new there; the *efficiency* with which these verbs
are implemented has changed. (same with INSPECT)
It might be that the programmers who 'did not know' them worked in shops
where Olde Standards were used... only got 8K of core and all that, but
this conclusion is conjectural. I would argue that there is a
difference between a textbook implementation of a standardised feature
and the sort of obscuranta called 'stupid COBOL tricks'... but I will
also agree that deciding *where* this Dividing Line lies is the subject
for many, many hours of beer-soaked debate.

DD
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p55@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

Thane Hubbell wrote in article
<01bcfe68$041b8ea0$4b752581@thane-hubbell>...
› 
› 
…[20 more quoted lines elided]…
› 

Yes, you should code for the least common denominator. But I don't
think you chose a good example.
Rookies coming out of tech school are probably more familiar with
COBOL 85 and GOTO-less programming than otherwise. I.e., 85 and
GOTO-less *is* the least common denominator.
The situation you describe is commonplace. Currently, I am
"upgrading" everything from COBOL68 to COBOL 74, as a
long-suffering Unisys has finally refused to support 68 one day more.
The difficult code parts are the old extensions which either no longer
work, or else work differently. I hate Extensions.

Ross

http://www.geocities.com/Hollywood/Set/7185/
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p56@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Should I code for the least common denominator?  Even some of the simple
› Ansi '85 COBOL constructs (evaluate with ALSO for example) baffle some of
› the staff.  Should I not use them?  Should I be restricted by the lack of
› experience of the current staff?  What do you think?

I think EVALUATE with ALSO is a potentially confusing syntax that should
be avoided. There are some uses for it, but they are rare. In most
cases, nested EVALUATEs (or IFs) would be easier to understand.

OTOH, never, ever, ever, use EVALUATE FALSE. That was added to the
language by a sadist.

BTW in the 1981 draft, multiple args in EVALUATE/WHEN were separated by
commas. Someone pointed out that commas are optional, and thus the
proposed syntax was imparsible. In the 1983 draft, the comma was
changed to ALSO.

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p57@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p48@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap>`

```

On 1 Dec 97 14:47:18 GMT, "Thane Hubbell" wrote:

› 
› 
…[27 more quoted lines elided]…
› experience of the current staff?  What do you think?

hmm. so does evaluate in the 74 version not have the also clause?

geez, i would probably use if/ then if it only have one variable you
can check....
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p58@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p57@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p57@usenetarchives.gap>`

```

G Moore wrote:
›
› hmm. so does evaluate in the 74 version not have the also clause?
›
› geez, i would probably use if/ then if it only have one variable you
› can check....

Cobol 74 doesn't have EVALUATE at all. It was new in Cobol 85.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p59@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p57@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p57@usenetarchives.gap>`

```

In article <34b··.@nnt··m.com>,
gvw··.@net··m.com (G Moore) wrote:
[...]
›
› hmm. so does evaluate in the 74 version not have the also clause?

Cobol-74 does not have the EVALUATE verb at all.
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p60@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p57@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p57@usenetarchives.gap>`

```



G Moore wrote in article
<34b··.@nnt··m.com>...
› On 1 Dec 97 14:47:18 GMT, "Thane Hubbell"  wrote:
› 
…[45 more quoted lines elided]…
› 

Ansi 74 COBOL has no evaluate statement.
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 6)_

- **From:** "pknu..." <ua-author-1468510@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p61@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p60@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p44@usenetarchives.gap> <gap-4438faa3ba-p45@usenetarchives.gap> <gap-4438faa3ba-p48@usenetarchives.gap> <gap-4438faa3ba-p57@usenetarchives.gap> <gap-4438faa3ba-p60@usenetarchives.gap>`

```

On 5 Dec 97 14:36:57 GMT, "Thane Hubbell" wrote:

›
› Ansi 74 COBOL has no evaluate statement.

And your point IS??????
Unsolicited e-mails are annoying, but not that big a deal.
I'd rather not get them, but they're easy enough to delete.
The flip side is that sometimes they actually are of interest.
It's just like junk mail, we all complain about it, but once
in a while there's something worth opening up and reading.
-Curt Shannon
```

#### ↳ Re: How important is speed?

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p62@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Bernard Liengme wrote:
›
› My question is: when you write a
› data processing program to run on a modern computer how concerned are
› you about speed?

IMHO - as a contract programmer, maintainability is usually the
preferred #1 priority. The bosses and especially the programmers who are
going to inherit my code are very happy if I use less complicated code
to perform a process (instead of the most efficient, but difficult to
understand/debug) set of lines. And if they can understand the many
comments to see what's going on.

It was not the situation in the mid-70's when we wrote the
most-exercised programs of a very complicated system in assembler
because they were the most efficient in runtime. A few years later they
were converted to COBOL because the machines had caught up, and there
was hardly anyone who would/could maintain the assembler.

If it's speedy, that's nice too, but it is not a showstopper in the
usual business situation. Of course, if you worked for American Express,
etc. (i.e., a zillion transactions a day) you might have more concern
about speed.

Of course, if one can write maintainable code that runs with speed,
that's the preferred combo.

As I have mentioned before in this NG, I think cuteness of the GUI is
now #1 in a lot of places. I predict that will get shoved back when they
begin to handle the standard situation where the user requests changes
to unmaintainable Java, C++, and VisualBasic code. It will take a few
years for places to figure that out.

John
```

#### ↳ Re: How important is speed?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p63@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```

Most of the time... IMHO.... 95% of the time, the speed, or lack there of for a
particular construct does not matter a bit. A given construct could be twice
as fast, or twice as slow and it wont matter most of the time.

Occasionally, i.e. inside of loops executed billions (yup billions of times)
per run, this may not be true. Usually this is more of a design problem as
opposed to a code problem.

Most of the time in routine COBOL based applications all of the significant
compute time is spent doing I/O or DBMS activities. Particular COBOL verbs do
not affect the performance of these components.

Perhaps 5% of applications contain particular constructs that should be
examined, maybe 1 or 2% require code changes. Most of the time performance
issues are DESIGN issues - i.e. making a decision too late in an algorithm.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive
in a legacy based world.
```

##### ↳ ↳ Re: How important is speed?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p64@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p63@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p63@usenetarchives.gap>`

```

You are only considering the impact on one program. If the average program
in a company takes 25% more CPU than necessary, the company has to pay for a
25% faster computer to get the same performance. This may or may not be cost
justifiable.
```

#### ↳ Re: How important is speed?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p65@usenetarchives.gap>`
- **In-Reply-To:** `<347616F0.58BBCE18@stfx.ca>`
- **References:** `<347616F0.58BBCE18@stfx.ca>`

```



Bernard Liengme wrote in article
<347··.@st··x.ca>...
› A question from an academic to the front line workers. I sometimes refer
› to a Cobol textbook written in 1991. While it answers many questions
…[10 more quoted lines elided]…
› 

Over the years I have seen speed DECREASE dramatically in applications.
Programmers get sloppier as more RAM and disk space is available. In
actuality, what has happened in some cases is that the Runtime Environment
has taken on the bloat.

I started writing PC applications in COBOL when the max ram was 512K and
the biggest hard drive was 10 meg. We made everything VERY tight. Speed
was important to the user and to us. Too often today the answer to a slow
application is to throw more hardware at it. I think that is a mistake.

Applications need to be written TIGHTLY, however NOT at the expense of
maintainability. We know now that applications have a long long life span.
In reference to your example, I would choose the slower method. However,
I would take the additional step of eliminating all computes that can be
replace with simple add/divide/multiply and subtract statements. I would
concentrate on the area where applications suffer most - I/O. As an
example, I have an application I wrote that is an Item Locator for a retail
store, part of the retail package my employer sells. Speed of lookup is
paramount. I could have just performed sequential reads till I found a
match. Instead I developed a fairly complex index structure and used
multiple START and READ statements. The code is still clear, and easy to
maintain, but the application is more complex than straight reads are. I
could have gotten away with the straight read method on todays 200MHZ
pentium machines, and had the same speed I have with the optimized version
on a 286. But just think how fast it is now on the newer hardware!

Speed is important.
```

##### ↳ ↳ Re: How important is speed?

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p66@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p65@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap>`

```

On 26 Nov 97 20:35:19 GMT, "Thane Hubbell" wrote:

› As an
› example, I have an application I wrote that is an Item Locator for a retail
…[7 more quoted lines elided]…
› on a 286.  But just think how fast it is now on the newer hardware!  

hmm. who would use a linked list for finding a single match anyways?
balanced b-trees are always the way to go when it comes to search
data. i agree about compilers getting slopier though. alot of new
development features are a pain to even have in the machine.
```

###### ↳ ↳ ↳ Re: How important is speed?

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p67@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p66@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap> <gap-4438faa3ba-p66@usenetarchives.gap>`

```

In article <347··.@nnt··m.com>,
gvw··.@net··m.com (G Moore) wrote:

› hmm. who would use a linked list for finding a single match anyways?
› balanced b-trees are always the way to go when it comes to search
…[3 more quoted lines elided]…
› 
I am a relative newcommer (7 months in the profession) and this may be a stupid question.
Could someone send me (or post) code for a balanced b-tree in cobol. I built one in C while
attending school and understand the logic and reasons but have to my knowledge, not seen one
implimented in COBOL. With C and the STRUCT concept it makes sence but with COBOL's file
handling I am having a tough time visualizing the set-up of one.
Thanks in Advance.
Greg
amo··g@ix.··m.nospam remove .nospam to reply
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p68@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p67@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap> <gap-4438faa3ba-p66@usenetarchives.gap> <gap-4438faa3ba-p67@usenetarchives.gap>`

```

[posted and mailed]

Gregory Paul Amos wrote:

[snip]

› I am a relative newcommer (7 months in the profession) and this may be a stupid question.
› Could someone send me (or post) code for a balanced b-tree in cobol.  I built one in C while
…[5 more quoted lines elided]…
› amo··g@ix.··m.nospam     remove .nospam to reply

The short answer is that you don't normally need to write a b-tree
in COBOL. Access to indexed files is built into the language. In C
you have to use somebody's library routines, or write your own.

The longer answer is that there's very little you can do in C that
you can't do, one way or another, in COBOL (depending somewhat on
the dialect). Some kinds of operations are clumsier in COBOL, such
as bit-twiddling. Other kinds are easier, like reading or writing
records with fixed-length fields. With a few exceptions, though,
either language can do anything the other can, however clumsily.

One exception is that COBOL has no equivalent to fseek(). It cannot
jump to an arbitrary position within an arbitrary file. (There may
be some dialects which can, but garden-variety COBOL cannot.) For
the equivalent functionality you have to define the file for random
access, using either relative record numbers or an index.

Another exception is that COBOL does not generally support recursion.
This omission makes it awkward to traverse any kind of tree. The
workaround is to build your own explicit stack in memory to keep
track of where you are. It's awkward, to be sure, but anyone who
could build a b-tree in the first place should have no trouble with
this additional convolution.

If you would be more explicit about what aspects of a b-tree would
be difficult in COBOL, someone in this news group can probably
suggest a way around it.

(Sorry, I don't have any b-tree code to offer.)

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 5)_

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p69@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p68@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap> <gap-4438faa3ba-p66@usenetarchives.gap> <gap-4438faa3ba-p67@usenetarchives.gap> <gap-4438faa3ba-p68@usenetarchives.gap>`

```

On Fri, 28 Nov 1997 08:17:05 -0600, "Michael C. Kasten"
wrote:

› 
› Another exception is that COBOL does not generally support recursion.
…[4 more quoted lines elided]…
› this additional convolution.

i have some C code which traverses a b-tree non-recursively. it can be
done, but as others have suggested an indexed file is much better,
with the quick dropping costs of memory
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p70@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p67@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap> <gap-4438faa3ba-p66@usenetarchives.gap> <gap-4438faa3ba-p67@usenetarchives.gap>`

```

Gregory Paul Amos wrote:
› 
› G Moore gvw··.@net··m.com wrote:
…[12 more quoted lines elided]…
› Thanks in Advance.

I don't have COBOL btree code for you, but logic is logic. If you think of
the COBOL record as a struct, you have the idea fairly close, except that the
COBOL record's hierarchical structure is more powerful than struct. Even
with combinations of struct and union, you can't quite do what the COBOL
record with redefines does easily.

But a better question is, if you are going to store the data in a file, why
not use an indexed file, and avoid having to write btree code altogether?
When using a given language, utilize its strengths.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How important is speed?

_(reply depth: 4)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4438faa3ba-p71@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4438faa3ba-p67@usenetarchives.gap>`
- **References:** `<347616F0.58BBCE18@stfx.ca> <gap-4438faa3ba-p65@usenetarchives.gap> <gap-4438faa3ba-p66@usenetarchives.gap> <gap-4438faa3ba-p67@usenetarchives.gap>`

```



Gregory Paul Amos wrote in article
<65latt$c.··.@sjx··m.com>...
› In article <347··.@nnt··m.com>,
› 	gvw··.@net··m.com (G Moore) wrote:
…[10 more quoted lines elided]…
› Greg  

Greg, not to sound ignorant - but I am - what is a Balanced B-Tree?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
