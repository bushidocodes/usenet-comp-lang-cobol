[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migrating COBOL batch & CICS off mainframe

_8 messages · 5 participants · 2005-04_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Migrating COBOL batch & CICS off mainframe

- **From:** "TM" <tmiller16@yahoo.com>
- **Date:** 2005-04-21T19:43:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<116gek9j1o0qvb3@corp.supernews.com>`

```
Greetings, all.  I am new here.

I am a mainframe systems programmer/Unix SA.  Our m/f environment is small 
and static, and will eventually disappear, but not for a few years at least. 
Meanwhile, I'm contemplating the merits of migrating our COBOL/VSE apps, 
both batch and CICS/VSE 2.3, to another platform.  We also have Win2K3, 
Solaris and AIX in our shop.

After a small amount of research, it seems that there are mainly two ways I 
can go:  Micro Focus or IBM.  Does anyone have first-hand experience with a 
COBOL mainframe-to-whatever migration?  Pros & cons of the IBM and Micro 
Focus routes?

Cost is a major factor in this (not yet a) project.  Our current m/f 
environment is inexpensive to maintain.  If it would cost $100,000 to 
migrate, I should stop right now.  $40K might even be too much... I'm just 
at the 'thinking about it stage', so I don't have any ROI numbers at all.

Thanks,
TM

P.S. I notice there are Micro Focus employees on this lists.  I welcome your 
input, but please don't send any canned sales pitches or ask for my phone 
number.  I will call you if & when the time is right.  As I said, I'm just 
thinking about it and my management doesn't even know about it.  Thanks 
again.

P.P.S.  Converting the apps to another language is not an option.
```

#### ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2005-04-21T22:10:24-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cr16dF6phi6fU1@uni-berlin.de>`
- **In-Reply-To:** `<116gek9j1o0qvb3@corp.supernews.com>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com>`

```
TM wrote:

> Greetings, all.  I am new here.
> 
…[27 more quoted lines elided]…
> 
I agree with reducing the number of operating environments but 
consolidating load from one or more of the other environments into 
either VSE or an upgrade to z/OS might also be worthwhile.  Migration of 
appropriate workload to Linux also might save money if AIX, Solaris or 
Window server can be eliminated completely.
```

##### ↳ ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** TM <tmiller16@yahoo.com>
- **Date:** 2005-04-21T21:47:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<116gls7qsqhq081@corp.supernews.com>`
- **In-Reply-To:** `<3cr16dF6phi6fU1@uni-berlin.de>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com> <3cr16dF6phi6fU1@uni-berlin.de>`

```
Clark F. Morris, Jr. wrote:

> I agree with reducing the number of operating environments but 
> consolidating load from one or more of the other environments into 
> either VSE or an upgrade to z/OS might also be worthwhile.  Migration of 
> appropriate workload to Linux also might save money if AIX, Solaris or 
> Window server can be eliminated completely.

Thanks for the very good suggestion.  I probably should have added that 
the I.S. manager is in her mid-30's and all she knows about mainframes 
is that they are something you move things off of.  The Network manager, 
my boss, is a MS guy, but is reasonable and open-minded.

Windows & Solaris won't go away, but AIX might.  The attitude towards 
Linux is 'watch, wait and see', but I'm trying to train myself on it. 
Since IBM is actively promoting it, it might be a good fit in our shop, 
especially if AIX sticks around.  We have a pair of p660's(?) that may 
become available in a year or two, which have more than enough power to 
handle our mainframe apps.

-TM
```

##### ↳ ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** TM <tmiller16@yahoo.com>
- **Date:** 2005-04-21T21:57:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<116gmev8qh6pked@corp.supernews.com>`
- **In-Reply-To:** `<3cr16dF6phi6fU1@uni-berlin.de>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com> <3cr16dF6phi6fU1@uni-berlin.de>`

```
Clark F. Morris, Jr. wrote:
> I agree with reducing the number of operating environments but 
> consolidating load from one or more of the other environments into 
> either VSE or an upgrade to z/OS might also be worthwhile.  Migration of 
> appropriate workload to Linux also might save money if AIX, Solaris or 
> Window server can be eliminated completely.

I'd love to get a z900 and carve it up into umpteen LPARs.  It could 
probably run our whole shop, but that kind of centralized system and 
so-called 'single point of failure' is too foreign to the youngsters I 
work for.  I may try to sneak some Linux into the shop, since it will 
run on any IBM platform, and can be supported by IBM.  We'll see.

-TM

P.S. I'm not using my name only because of the off chance that someone 
from my shop might see this thread.  There's not that many VSE shops 
around these days.
```

###### ↳ ↳ ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-04-22T10:01:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cslfbF6o7phlU3@individual.net>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com> <3cr16dF6phi6fU1@uni-berlin.de> <116gmev8qh6pked@corp.supernews.com>`

```
FWIW, we're a VSE shop also.  But, unlike you (it appears) we have a large
amount (in my opinion) of new mainframe COBOL development.  We've been
considering (for several years) a move to z/OS, but it seems (to me) that it
would be a pretty large effort, especially since we'd continue developing at
the same time.  Plus z/OS is about 4 times more expensive...

We also have Windows, Solaris and Linux, and Netware servers all over the
place (they're trying to move off of Solaris and just use Linux (and Netware
under Linux)).

The interesting thing about the move from Solaris to Linux is they would
still rather a lot of Intel boxes to run Linux instead of putting it on the
mainframe.  The "single point of failure" you talk about is a big part of
that reasoning.  So now the mainframe people are trying to find a business
case for running Linux on the mainframe.  Haven't really figured one out
yet!

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> TM<tmiller16@yahoo.com> 4/21/2005 7:57:32 PM >>>
Clark F. Morris, Jr. wrote:
> I agree with reducing the number of operating environments but 
> consolidating load from one or more of the other environments into 
> either VSE or an upgrade to z/OS might also be worthwhile.  Migration of 
> appropriate workload to Linux also might save money if AIX, Solaris or 
> Window server can be eliminated completely.

I'd love to get a z900 and carve it up into umpteen LPARs.  It could 
probably run our whole shop, but that kind of centralized system and 
so-called 'single point of failure' is too foreign to the youngsters I 
work for.  I may try to sneak some Linux into the shop, since it will 
run on any IBM platform, and can be supported by IBM.  We'll see.

-TM

P.S. I'm not using my name only because of the off chance that someone 
from my shop might see this thread.  There's not that many VSE shops 
around these days.
```

###### ↳ ↳ ↳ Re: Migrating COBOL batch & CICS off mainframe

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-04-25T19:15:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31a3$426d883b$45491c57$29333@KNOLOGY.NET>`
- **In-Reply-To:** `<3cslfbF6o7phlU3@individual.net>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com> <3cr16dF6phi6fU1@uni-berlin.de> <116gmev8qh6pked@corp.supernews.com> <3cslfbF6o7phlU3@individual.net>`

```
Frank Swarbrick wrote:
> 
> The interesting thing about the move from Solaris to Linux is they would
…[4 more quoted lines elided]…
> yet!

It's been my experience that having a "single point of failure" is only 
a concern if, politically, the system isn't desired.  Yes, if a 
mainframe were as flaky as an Intel box, I'd agree with them.  However, 
with the enterprise-class power also comes enterprise-class stability - 
mainframe vendors' customers demand no less.  :)

(Throw the word "assured computing" at 'em - there's your business case. 
  You have one ramped-up mainframe where you do your actual process, 
along with a hot mirror that has very few MIPS, but enough disk to 
mirror the prime.  The prime goes down, you key-up the backup (or 
MIPS-on-demand, if that's an option), change a DNS record, and the 
customer never knows the difference.)
```

#### ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** "Andy Sinclair" <andy.sinclair@microfocus.com>
- **Date:** 2005-04-22T11:42:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4ajjv$cah$1@hyperion.microfocus.com>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com>`

```
TM,

Both the Micro Focus and the IBM solutions are technically sound, offering a 
technology to move the COBOL/CICS/BMS elements of applications unchanged. 
Micro Focus is also working on adding VSE (and MVS) JCL support to its 
engine so that the JCL can be moved "as is". This is useful if there is a 
lot of JCL as it lowers the risk and effort of converting JCL to script.

If there is not a lot of JCL and you can convert to script then the 
migration is fairly straightforward with either technology and so its going 
to come down to cost of the CICS engines on the target platform, conversion 
services for any other languages (like Assembler routines) and any other 
services you need.

The cost of engines will be based on the number of users or the number of 
CPUs on the machine you are migrating to. The number of CPUs will depend on 
how many MIPS you are using on the mainframe today. A rough estimate is 1 
CPU on Windows/UNIX/Linux deliver approximately 100 MIPS.

If there are under 100 users, a user licence will typically work out cheaper 
than a CPU based license.

You will also need development products for the developers who will be 
maintaining the system once it's on the new platform.

So if you only have 1 developer, the application is used by less than 25 
users, you have no Assembler, and very little JCL then the technology costs 
are OK and it would really come down to the services. For a small system 
with few users and few developers you definitely can come in well under the 
$100K mark. Whether your can get it all done for as little as $40K is 
debatable but it would be worthwhile asking both IBM and Micro Focus if they 
can review your application details and provide a ball park figure.

If you would like to contact me directly, reply to 
andy.sinclair@microfocus.com.

Best regards,

Andy Sinclair
Senior Director, Product Management
Micro Focus



"TM" <tmiller16@yahoo.com> wrote in message 
news:116gek9j1o0qvb3@corp.supernews.com...
> Greetings, all.  I am new here.
>
…[26 more quoted lines elided]…
>
```

#### ↳ Re: Migrating COBOL batch & CICS off mainframe

- **From:** TM <tmiller16@yahoo.com>
- **Date:** 2005-04-22T20:10:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<116j4hmtcvg6q3c@corp.supernews.com>`
- **In-Reply-To:** `<116gek9j1o0qvb3@corp.supernews.com>`
- **References:** `<116gek9j1o0qvb3@corp.supernews.com>`

```
TM wrote:

> Cost is a major factor in this (not yet a) project.  Our current m/f 
> environment is inexpensive to maintain.  If it would cost $100,000 to 
> migrate, I should stop right now.  

Perhaps I was too hasty when I wrote that.  Our production box is 
inexpensive to maintain, but DR is proving more difficult.  Our current 
DR solution is maintaining our old IBM ES/9000 as a DR box, but old 
hardware is expensive to maintain and there are many other problems with 
this solution.  Purchasing a matching xServer/FLEX box would be very 
costly.  I don't want to spawn a discussion about DR (believe me, I have 
examined every possibility).  The point is that DR makes the current 
production box significantly more expensive to maintain.  I don't yet 
know what the cost limit to migrate would be, and my management would 
welcome any opportunity to consolidate platforms.

-TM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
