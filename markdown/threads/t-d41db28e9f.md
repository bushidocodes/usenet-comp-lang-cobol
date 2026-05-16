[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Shared" procedure division code

_401 messages · 21 participants · 2005-07 → 2005-09_

---

### "Shared" procedure division code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-20T22:23:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
As a follow up on another thread ....

It seems to me that the most common place where I *used* to see the same source 
code (paragraph/section) repeated within a single program was in OLDER (IBM) 
CICS code where "locality of code" was an issue.  That was that it was important 
that the application not need to "page in and out" sections of machine code 
depending upon application logic flow. Although this is still a MINOR 
consideration in that (and possibly other) environments, I don't know where it 
happens with NEW code today.  However, in that older code, it was (medium) 
common to see the same (differently named) paragraph/section "near" multiple 
places in the program logic where it could be needed.

This was also one of the few places that I have ever seen (again infrequent - 
but occasionally) COPY statements within a paragraph, e.g.  (CAPS and '74 
Standard code)

PARA1.
    IF XYZ
       PERFORM PARA2
    ELSE
       PERFORM PARA3
     .
     PERFORM PARA4
     PERFORM WINDUP
       .
PARA2.
    lots of logic here
    IF XXX
        PERFORM PARA5-1
     .
    more logic
      .
PARA5-1.
       COPY P5LOGIC.
           .
PARA3.
     some logic - more than "one page" of memory required
       .
PARA4.
    lots of logic here
    IF XXX
        PERFORM PARA5-2
     .
    more logic
      .
PARA5-2
       COPY P5LOGIC.
           .

***

With this "copy in procedure division" approach one could "physically" store 
common source code in a single place - but also have "locality of code" for the 
generated machine code.

I neither recommend this approach nor (personally) know of any reason to use it 
in today's computing environment, but did think it was worth mentioning (both 
for the "use of duplicated code" and the solution to "maintenance of such code")
```

#### ↳ Re: "Shared" procedure division code

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-07-21T13:32:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EtNDe.143758$tt5.85215@edtnps90>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:T9ADe.499087$3V6.422305@fe04.news.easynews.com...
> As a follow up on another thread ....
>
…[6 more quoted lines elided]…
> environments, I don't know where it happens with NEW code today.

    With regard to "new code" (and not nescessarily just COBOL, but for 
programming in genenral), the advice I typically hear is don't try to 
outsmart the compiler. Rather, one should write their code in such a way as 
to make it as easy to understand as possible so that the compiler itself can 
figure out what you're trying to do, and optimize appropriately (of course, 
this assumes you're programming in some language for which code analysis is 
easier ;)).

    A lot of people who claim to optimize don't bother to actually profile 
their code to find out what parts of the program are running slowly, or even 
whether or not their "optimizations" haven't actually made the program run 
MORE slowly.

    If it turns out you ARE smarter than the compiler, you should contribute 
your ideas to the compiler developers (this is easier if you're using an 
open source compiler), so that you can then write your code clearly, and 
still have it perform just as fast as had you optimized it directly.

    The only situations I can think of where it might be desirable to do 
manual optimizations is for environments where the compilers haven't matured 
enough to actually accept optimization contributions even if you had them 
(e.g. compilers for cell phone, or "smart refrigerators", and things that 
have only recently become programmable).

    - Oliver
```

#### ↳ Re: "Shared" procedure division code

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-07-21T19:37:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11e0fton1de7137@news.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
William M. Klein wrote:
> As a follow up on another thread ....
> This was also one of the few places that I have ever seen (again
> infrequent - but occasionally) COPY statements within a paragraph,
> e.g.  (CAPS and '74 Standard code)

We have a fair-sized DECLARATIVES section to handle file error conditions.

Otherwise, your point is well taken.
```

#### ↳ Re: "Shared" procedure division code

- **From:** "Caederus" <davidburnham@gmail.com>
- **Date:** 2005-07-26T09:17:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122394642.142312.250340@o13g2000cwo.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
> I neither recommend this approach nor (personally) know of any reason to use it
> in today's computing environment, but did think it was worth mentioning (both
> for the "use of duplicated code" and the solution to "maintenance of such code")

Maintenance of the code is the big reason to use such code.

If you have a routine that works and is used by a number of different
programs, putting it in a copybook is the quickest and easiest way to
stream line the maintenance. However If it starts getting to big there
is the question of making it it's own sub program.
```

##### ↳ ↳ Re: "Shared" procedure division code

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-07-26T21:51:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfyFe.133371$HI.42698@edtnps84>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1122394642.142312.250340@o13g2000cwo.googlegroups.com>`

```

"Caederus" <davidburnham@gmail.com> wrote in message 
news:1122394642.142312.250340@o13g2000cwo.googlegroups.com...
>> I neither recommend this approach nor (personally) know of any reason to 
>> use it
…[10 more quoted lines elided]…
> is the question of making it it's own sub program.

    I think the issue Bill was trying to point out was that the code was 
inlined, or COPYed in two (or more) locations. If it were merely an issue of 
having correct code, and not wanting to touch that code for fear of breaking 
it, the code could have been put in a paragraph, and COPYed onced, and to 
simply PERFORM that paragraph.

    - Oliver
```

#### ↳ Re: "Shared" procedure division code

- **From:** "Caederus" <davidburnham@gmail.com>
- **Date:** 2005-07-26T09:17:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122394648.666152.313740@f14g2000cwb.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
> I neither recommend this approach nor (personally) know of any reason to use it
> in today's computing environment, but did think it was worth mentioning (both
> for the "use of duplicated code" and the solution to "maintenance of such code")

Maintenance of the code is the big reason to use such code.

If you have a routine that works and is used by a number of different
programs, putting it in a copybook is the quickest and easiest way to
stream line the maintenance. However If it starts getting to big there
is the question of making it it's own sub program.
```

#### ↳ Re: "Shared" procedure division code

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-07-27T23:34:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3kp9r4Fvcc0pU2@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com>`

```
 

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:T9ADe.499087$3V6.422305@fe04.news.easynews.com...
> As a follow up on another thread ....
>
…[68 more quoted lines elided]…
>

Bill, I know you don't condone this and I don't want to shoot the messenger, 
but this is the biggest load of bollocks I have ever seen posted here, and I 
have seen some good ones...

There is not and never has been any way you  can guarantee 'locality of 
code' by duplicating procedure code, whether you copy it or not. You cannot 
know where the page boundaries are in generated code, by looking at source 
code, without a huge amount of effort, and even if you did, the first time 
you amend it, they are likely to change. The best you can hope for is to 
increase the probability of code sharing a virtual page, and even if you do, 
it doesn't matter by any amount of significance.

It is based on an assumption that was 'urban myth' when Virtual Storage was 
first invented. Prior to VS it was common practice for COBOL programmers to 
write their main line and place performed code into subroutines after the 
mainline. (Some people still do this; it doesn't impact performance and it 
never has...)

The 'myth' seemed quite logical and I was persuaded by it at the time. If 
the new Virtual system was paging the code into 4K blocks it would have to 
do a heap of paging to get to the subroutines that were physically removed 
from the mainline. The theory was that the system would encounter a perform 
and start paging through the mainline to get to the subroutines. It would be 
much more efficient if the performed code was somewhere near to the place it 
was performed. (Less paging). Some people went even further and started 
duplicating code using COPY, exactly as you describe (I saw it too, in the 
late 60s/early 70s after VS was released.) The reasoning was that this would 
minimise paging. But the reasoning was flawed for the following reasons:

1. If there was memory available NO paging took place even in a VS 
environment. (So the duplicated code simply gave you less chance of getting 
your program loaded in the first place.)
2. The paging algorithm was not sequential and did NOT page through the 
program to get to virtual addresses that were already resident. In fact, the 
algorithm was much smarter than us COBOL programmers, and once something was 
resident it stayed there until it really needed to go. (I once had it 
explained to me by a Hungarian Mathematician who was also a Chess Grand 
Master. It wasn't even as simple as 'least frequently used' being paged out 
(which I believe is how the Windows Swap File works...))
3. The duplicated code was more problematic in increasing load time (and 
paging) than it was succesful in optimizimg performance.
4. As much faster paging devices became available, the whole question became 
more academic and these days it would be rare (and, in my opinion, stupid) 
to see people in CICS environments still using this practice.

I realise you were documenting something that is historic fact, but it would 
be wrong for people reading this to think it is good practice and 
reincarnate a stupid practice that was buried in the 70s. In today's 
environment this is irrelevant.

My personal preference is to encapsulate functionality into components that 
can be shared from one location (by a .dll, suitably wrapped for the 
environment). In environments that don't support this (like the mainframe), 
called subroutines have to be a better solution than duplicated source.

I covered all of this in:  http://66.152.52.10/archives/v3/v30201.asp and 
http://66.152.52.10/archives/v5/v50101.asp where I also discuss the pros and 
cons of called modules vs components.

Pete.
```

##### ↳ ↳ Re: "Shared" procedure division code

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-07-27T08:10:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dc8854$4gp$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3kp9r4Fvcc0pU2@individual.net...

> It is based on an assumption that was 'urban myth' when Virtual Storage
was
> first invented.

From the Unisys History Newsletter, Vol. 3 #5 (10/1999), available through a
search of "Burroughs virtual memory" on the internet:

"IBM's 1972 announcement of virtual storage for its large 370 series
machines was taken by Burroughs as validation of the virtual memory concept.
The company held a well-publicized tenth birthday party for the B5000 at the
old ElectroData plant in Pasadena, where a B5500 (which had been rebuilt
from a B5000) was still in operation. By the early 1970s, both the large and
medium Burroughs computers had inspired a high degree of loyalty among their
users, who were proud of the advanced features incorporated in the Burroughs
architecture. It would still be several more years before IBM really moved
into multiprocessing, while it was commonplace to Burroughs users. "

Have you checked your forehead lately?  Sounds to me like a blue-ink tattoo
of three block letters thereupon might be starting to show through!    ;-)

>Prior to VS it was common practice for COBOL programmers to
> write their main line and place performed code into subroutines after the
> mainline.

It was common practice on the B5000 and is still common practice on its
descendants, if you're talking about paragraphs and sections, as distinct
from ANSI-85 "nested programs", which of course weren't available in
standard COBOL until something like thirteen years after the introduction of
Virtual Memory on the IBM S/370 (and twenty-three or more years after the
introduction of Virtual Memory on the Burroughs B5000).

>(Some people still do this; it doesn't impact performance and it
> never has...)

Some people do this, and whether it impacts performance or not depends on
the architecture of the system and where the code segment boundaries fall.

It may never have impacted performance on the systems with which you are
most familiar, but because something is true for a subset of the universe
does not make it universally true; ditto for false!

> The 'myth' seemed quite logical and I was persuaded by it at the time.

I still am, actually, to a degree, particularly if a segment boundary falls
within a critical path in the program.

> If
> the new Virtual system was paging the code into 4K blocks it would have to
> do a heap of paging to get to the subroutines that were physically removed
> from the mainline.

Our experiments showed that in an era in which memory was a precious
commodity arbitrary-length data paging combined with unmodifiable object
code led to a *much* higher virtual-to-real ratio than was practical on
fixed-page virtual memory architectures.   I am not convinced that what you
describe as the "new Virtual system" is somehow more advanced or
fundamentally more efficient than what the B5000 had a decade before.

> The theory was that the system would encounter a perform
> and start paging through the mainline to get to the subroutines. It would
be
> much more efficient if the performed code was somewhere near to the place
it
> was performed. (Less paging).

That may be the theory on certain Virtual Memory systems, but it does not
apply to all.

> 1. If there was memory available NO paging took place even in a VS
> environment. (So the duplicated code simply gave you less chance of
getting
> your program loaded in the first place.)

If there was -- and is -- memory available, a code segment is loaded when it
is first touched, just as is true when memory is not available.  If there
isn't memory available there's a good chance the code will be marked absent
and will have to be reloaded.

> I realise you were documenting something that is historic fact, but it
would
> be wrong for people reading this to think it is good practice and
> reincarnate a stupid practice that was buried in the 70s. In today's
> environment this is irrelevant.

While I understand your arguments about repeating code in a program, in the
broader sense there are practices that you might deem irrelevant in the
machines *you* work on, but that might have significant benefit for machines
*others* work on.  To dismiss out of hand that with which you are not
familiar because it is irrelevant *to you* is one thing; to proclaim it more
universally irrelevant quite another.

> My personal preference is to encapsulate functionality into components
that
> can be shared from one location (by a .dll, suitably wrapped for the
> environment). In environments that don't support this (like the
mainframe),
> called subroutines have to be a better solution than duplicated source.

By "called subroutines" do you mean nested programs, separately-compiled
programs, or PERFORMed paragraphs/sections?

> I covered all of this in:  http://66.152.52.10/archives/v3/v30201.asp and
> http://66.152.52.10/archives/v5/v50101.asp where I also discuss the pros
and
> cons of called modules vs components.

Ah.  That puts us into the OO model, and I don't have a quarrel with that
approach to application design.  I think it more an efficient approach to
the *design* process (just as Structured Programming is viewed as an
improvement over "spaghetti") bement , but I think it more than anything
else an appropach  to *design* for its own sake than an approach that will
always and everywhere produce applications that consume fewer resources at
execution time compared to all competitive design approaches.

But have you verified the efficacy of all of these conclusions on, oh, say,
a large Unisys ClearPathPlus Libra 580 system?   On such a system, it's
probable that a monolithic one-megaline COBOL program will outperform a
hundred 10K-line COBOL programs doing the same thing (regardless of whether
memory is constrained on the system or not).  And how code is arranged in
the program may impact its efficiency, whether it's one of the 10K line
programs or the monolithic monster.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-07-29T00:45:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ks2bvF100lu4U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com>`

```
 
Oh Dear! I pressed a button... sorry Chuck.

Yes, my post was intended for IBMers. In future I'll make that clear.

And, within THAT universe my comments were general.

It was implicit  (I thought) because I was responding to a post from Bill 
Klein.

I did not mean to denigrate Unisys by implication and if Burroughs were into 
virtual storage 10 years sooner than IBM, well , good for them. I worked on 
B500 which did not employ it.

Probably because of your annoyance, you seem to have missed what I was 
getting at in places, but I have no intention of labouring it. Suffice to 
say I am aware that on occasions, large monolithic programs can run faster 
than many smaller ones; that is why I was careful to specify the environment 
I'm talking about. (The discussion was specific to CICS and IBM environments 
that are doing online processing, not batch...)

Everything I want to say about this I said already in the two linked 
articles.

If you have issues with what is stated there, I might be prepared to 
respond... (then again, I might not... I'm getting pretty laid back about 
programming these days...:-))

Pete.

TOP POST No more below.

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dc8854$4gp$1@si05.rsvl.unisys.com...
>
>
…[147 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-07-28T13:35:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcbfk4$2gbb$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ks2bvF100lu4U1@individual.net...

> Oh Dear! I pressed a button... sorry Chuck.

Well, yeah; the question is what does that button imply?

> Yes, my post was intended for IBMers. In future I'll make that clear.

I think it goes deeper than that.  You used phrases like "urban myth",
"reincarnate a stupid practice that was buried in the '70's" and "in today's
environment this is irrelevant".   Such categorizations *encourage others*
to limit their views to the IBM environment *and* to hold all other
environments in similar contempt.

> And, within THAT universe my comments were general.

Well, that's part of the problem.  Planetary system, maybe.  Galaxy,
arguably.  By definition there is but *one* universe, and the Unisys MCP
environment is part of that universe.

How do such things strike me?  Try this as a *reductio ad absurdum* example,
tongue planted firmly in cheek:

"After all, everybody who's anybody knows that there's been no excuse for
operating in any environment  in which it's inappropriate to align a packed
field (at either end) on anything but an 8-bit boundary, or to declare such
a field as unsigned, for at least 35 years.  Machines that impose or even
endorse such stupid practices and limitations should have been consigned to
the trash heap of history and are certainly irrelevant to any well-informed
professional in today's computer science environment, and any programmer who
thinks such conventions have any value whatever is clearly a dinosaur ... "

It's not just the fact that your remarks didn't include the explicit caveat
that they were limited *strictly* to a particular environment, it's the
categorical nature of your characterizations that bothered me, in and of
itself.  We've been through this a while back with Other Folk on this forum,
and I had some hope you wouldn't descend to that level of contemptuous
categorizations, particularly when there are clear exceptions ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-07-29T11:10:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3kt6vbFvvrqoU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com>`

```
 

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dcbfk4$2gbb$1@si05.rsvl.unisys.com...
>
>
…[14 more quoted lines elided]…
> environments in similar contempt.

That's just silly. I already said my comments applied to the IBM 
environment. There is no question of contempt for other environments  (or 
even for the IBM one) and I believe you are so oversensitized on this issue 
it is affecting your judgement. I am not the enemy of Unisys (or any other 
company) and I have worked in most environments. I stand by the quoted 
comments above, within the stated context.
>
>> And, within THAT universe my comments were general.
…[4 more quoted lines elided]…
>

It isn't if I choose to limit my comments to a particular environment. I 
would suggest that the Unisys MCP is your WHOLE universe and you are 
absolutely as quilty of what you accuse me of.

> How do such things strike me?  Try this as a *reductio ad absurdum* 
> example,
…[16 more quoted lines elided]…
>
I have never written anything even approaching that.

> It's not just the fact that your remarks didn't include the explicit 
> caveat
…[8 more quoted lines elided]…
>
I do not have contempt for ANY environment. My post was strongly condemning 
a practice that was based on urban myth on the sites where I encountered it. 
It is personal experience. Everyone, including myself, accepted it. It 
wasn't until I was sat down with someone who knew the reality that the 
scales fell from my eyes.

I wouldn't like to see this practice resurging. That was the only reason I 
posted.

Interestingly, no one from ICL or Honeywell or NCR or any other major 
company that was around at the time has taken offence at this or considered 
my post contemptuous. Not even the IBMers who know what I'm talking about. 
That's because it wasn't.

It is very wrong of you to take anything I post as a personal attack or to 
conclude that I am showing contempt for anybody or anything.

I don't come here to denigrate companies or environments; not even by 
omission.

Think about your position.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-07-29T11:25:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcdsbv$stj$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3kt6vbFvvrqoU1@individual.net...

> That's just silly. I already said my comments applied to the IBM
> environment. There is no question of contempt for other environments  (or
> even for the IBM one) and I believe you are so oversensitized on this
issue
> it is affecting your judgement. I am not the enemy of Unisys (or any other
> company) and I have worked in most environments. I stand by the quoted
> comments above, within the stated context.

I wear two hats:  one in support of the Unisys MCP COBOL environments, and
one in support of the enhancement of the standard for COBOL.

One of the ways in which I believe users, and customers, can protect their
investment in their COBOL code is to do what they can to ensure that the
coding conventions in it are *not* specific to a particular vendor.  That's
one of the big reasons I choose to be involved with the standardization
process.  Coding conventions may be obviously vendor-specific, but sometimes
standard code can be written in such a way that it presumes a particular
implementation.  The latter can be very subtle.

> It isn't if I choose to limit my comments to a particular environment.

Well, you did that after the fact.  More importantly, although you responded
to a post that had a mention of "older (IBM) CICS code", your post limited
the context to IBM environments only in a few details.

I know you didn't use the following phrases, and I'm not accusing you of
that.  These are *my* examples of categorizations.  There's a big difference
among "everybody knows that ...", "everybody knows that in an <xyz>
environment  ..."  and "everybody in an <xyz> environment knows that ...".
The first two *invite* counterexamples which can almost certainly be found.
The third might actually be true (although I suspect counterexamples might
exist there as well), but if I am not a member of the specified subset I am
not qualified to know one way or another.

Although the first two aren't quite so bad as saying "When I wrote 'all
mainframes' I really meant 'all real mainframes' " or "When I wrote
'everybody knows' I should have written 'everybody who's anybody knows' ",
I'm not convinced any such generalizations are *entirely* and *inherently*
devoid of an edge of categorical contempt, intentional or otherwise.

> I
> would suggest that the Unisys MCP is your WHOLE universe and you are
> absolutely as quilty of what you accuse me of.

No; in fact I would argue that I tend more toward
*implementation-nonspecific* recommendations far more than Unisys
MCP-specific recommendations in this forum, precisely because the
Unisys-specific ones are implementation-specific and thus run counter to the
goal of protecting client investment.

To my intentionally absurd example, you responded:

> I have never written anything even approaching that.

And I don't think the phrases I cited earlier from your posting like "urban
myth", "doesn't impact performance and never has", "stupid practice that was
buried in the 70's" and "in today's environment this is irrelevant"  differ
all *that* much in categorical dismissiveness from phrases like "everybody
who's anybody", "no excuse", "stupid practices", "trash heap of history" and
so forth that I chose in that *reductio ad absurdum*.

The problem is, that example isn't all that absurd:  I have heard its almost
exact *opposite* from highly-paid (albeit newly-hired) and highly-placed
system analysts at a Unisys MCP site ("packed fields are always signed
internally and are always aligned at both ends on byte boundaries for
anything approaching reasonable performance, so that's why we changed all
our programs, and that means it's the fault of the Unisys MCP environment
that our programs use more memory and take more processor resources than
they used to before we changed it.").    See below for further discussion on
this particular case.

> I do not have contempt for ANY environment. My post was strongly
condemning
> a practice that was based on urban myth on the sites where I encountered
it.
> It is personal experience. Everyone, including myself, accepted it. It
> wasn't until I was sat down with someone who knew the reality that the
> scales fell from my eyes.

> I wouldn't like to see this practice resurging. That was the only reason I
> posted.

Actually, I don't think you *do* have contempt for particular environments.
But you have used what I believe is contemptuous terminology for practices
that, while of dubious merit in the environments in which you currently
operate, might be of less dubious -- or even positive -- merit in other
environments.  It's not that you don't like the practices, it's that you
dismissed their value in general (and then subsequently limited the
context).

> Interestingly, no one from ICL or Honeywell or NCR or any other major
> company that was around at the time has taken offence at this or
considered
> my post contemptuous. Not even the IBMers who know what I'm talking about.
> That's because it wasn't.

It may also be that the people who support ICL or Honeywell or NCR COBOL
compilers and support software aren't active participants in this forum.   I
have no say over the actions or inactions of those who do not make
themselves visible.

Moreover, I don't think you were contemptuous toward Unisys.  That wasn't my
point.  I think you used contemptuous language about practices that others
might find of positive merit on grounds which might, or might not, have
anything to do with the operating environment (IBM, Unisys, or anyone else).

Note that I maintain several software products whose origins lie firmly in
the era when appropriate code was as clever, and as obtuse, as possible.
These products remain very, very widely used.  Do I argue that they need to
be replaced by the latest technology?  No, I don't; that's not going to
happen.  I try to slay the dragons I find as I find them and bring pieces of
the code up to a modicum of legibility as I have time and resources to do
so.  Interestingly, I often do so with significant risk to the stability of
the products, which causes our customers grief.   The *product*, as far as
its end users go, was often better off before I modernized it until we got
it stable again.    Maintainability is but *one* aspect of a given piece of
software that might be considered in whether it is useful or not.

> It is very wrong of you to take anything I post as a personal attack or to
> conclude that I am showing contempt for anybody or anything.

I did not take it as a personal attack; I took it as an unqualified
expression of contempt against certain programming practices.  Words and
phrases like "stupid practice" and "irrelevant" *express* contempt.

> I don't come here to denigrate companies or environments; not even by
> omission.

That's good; I'm glad you clarified your intent.

> Think about your position.

I do that all the time, and in this instance I'm taking a position that
designing for portability, and for optimal performance on the widest
possible variety of platforms, is a primary goal.

Going back to my packed-decimal example, one of the biggest performance
problems that our client encountered was the result of changing a whole
passel of PIC 9 PACKED-DECIMAL items that were used solely as Boolean flags
to PIC S9 PACKED-DECIMAL.  Comparisons of the former could reasonably be
done "bitwise" in our environment; the latter were handled numerically and
were quite a bit less efficient.    My recommendation, *in the interests of
portability as well as maximized performance on the widest variety of
platforms*, was to switch to PIC 9 DISPLAY or even PIC X DISPLAY, neither of
which occupied any more (or less) space than the signed PACKED-DECIMAL
encoding.  I do not know whether the client followed my recommendation.  My
"Unisys-only" position would probably have been that expressed in my absurd
example -- "Why on *earth* would *anyone* want to put a sign on a four-bit
flag?  Why would anyone think a 4-bit numeric item really occupies eight
bits?  Tell whoever's insisting on this that they're stuck in the late
1960's!"  However, I  *do* recognize that not all environments allow
single-digit unsigned packed-decimal data items to occupy exactly 4 bits,
nor do all such environments allow them to be aligned on 4-bit boundaries in
memory.  More importantly, I also understand the reasons *why* this is the
case -- just as, for example, I understand that if the basic Unisys MCP
floating-point format were to be designed from scratch *today* it would
almost certainly use a different encoding format, even if it remained at 48
bits.

The position I am coming from is much more closely related to my
standardization concerns than it is to compatibility with the Unisys MCP
environment.  In many ways the IBM and the MCP environments are *so*
different that my concerns are more about finding a way toward reasonable
efficiency on *both* (as for my example above).

One of the arguments *it seems to me* you are making in favor of a "modular"
approach (which I take to be OO-related) is that the association of data
with code in the system's memory always leads to more efficient utilization
of virtual memory. and the approach facilitates that association and allows
optimization of the size of each of the "modules" to make memory swaps more
efficient.   While I have no problem with the idea of taking a modular
approach to application design, that defense is implementation dependent and
is not universal.  It may be more efficient, it may be much less efficient.
Other reasons to use -- or not to use -- such an approach may well be of
overriding importance to the end user -- *including* in the very environment
to which you now limit your categorizations.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-07-31T02:13:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3l1g7qFvs80mU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com>`

```
 

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dcdsbv$stj$1@si05.rsvl.unisys.com...
>
>
…[13 more quoted lines elided]…
> one in support of the enhancement of the standard for COBOL.

Two two hat hats? Why why then then you you must must have have two two head 
heads... I guess that accounts for why you say things twice :-)

Remember that they are YOUR hats. The trouble with hats is that sometimes 
they don't fit as well as they might, and often other people think they look 
silly on us, when we can't see it ourselves...

It's a personal thing. If you feel comfoprtable in your hat(s) then that's 
fine. But it wouldn't do to think that everyone else should adopt a similar 
chapeau, or even admire yours. Diversity is one of the great things about 
life on this planet.
>
> One of the ways in which I believe users, and customers, can protect their
> investment in their COBOL code is to do what they can to ensure that the
> coding conventions in it are *not* specific to a particular vendor.

Now, see, that is a very understandable viewpoint for a man with either of 
your hats. But those of us who go around hatless  really don't care. In 
fact. my experience has been that programmers working on the shop floor 
NEVER refer to the COBOL standard (most sites don't even have a copy); 
instead they refer to the manuals provided by their vendor which tend to 
relate to the particular implementation in use in that shop. Makes sense to 
me, and I agree with it.

It isn't religion; it is computer programming.

Now, you will argue that I am making sweeping contemptuous generalizations 
and I haven't qualified my statement to specific platforms that don't 
include Unisys. I'm not. As always, I'm simply calling what I see or have 
seen.

I don't KNOW whether they have standards manuals available on every Unisys 
site and whether programmers are required to recite the syntax as prescribed 
in the 2020 standard (which might be released in 2050, if it gets through 
enough committees) of a different COBOL verb every morning, just like the 
Oath of Allegiance... Neither do I care. Is that contemptuous? No. Not at 
all. I respect the right of people outside my experience to do whatever they 
want to; I just don't include them in my discussions because my discussions 
are based on personal experience and I haven't any in Unisys. It isn't 
personal. It certainly shouldn't spark a long diatribe about the alignment 
of 8 bit bytes...(Man, you need some serious holiday...honestly)

If you are offended because the world at large does not embrace your ideals, 
whose problem is that, Chuck?

> one of the big reasons I choose to be involved with the standardization
> process.  Coding conventions may be obviously vendor-specific, but 
> sometimes
> standard code can be written in such a way that it presumes a particular
> implementation.  The latter can be very subtle.

And many people see nothing wrong with that. It bugs you, personally. Deal 
with it.
>
>> It isn't if I choose to limit my comments to a particular environment.
>
> Well, you did that after the fact.

No, when I realised you had taken offense where none was intended I 
apologised (I never do that unless I'm sorry...) and set the record straight 
by YOUR requirements, rather than mine. Instead of accepting that I hadn't 
meant to offend you, you persisted, so now I'm retaliating. That's life in 
CLC... (gotta love it... :-))

> More importantly, although you responded
> to a post that had a mention of "older (IBM) CICS code", your post limited
> the context to IBM environments only in a few details.

It was implicit. And yes, the practise is bad on other platforms on which I 
have worked also. What is your point here? That it is a good thing to 
duplicate code in order to gain locality of reference on a Unisys machine? 
Say that and we'll close the discussion. I won't believe you, but it really 
doesn't matter; I don't work with Unisys. I DO care about the environments I 
HAVE worked with. More importantly, I care about newcomers seeing something 
that Bill was documenting as a matter of record, and thinking it's a good 
idea. It isn't, and I explained why.


>
> I know you didn't use the following phrases, and I'm not accusing you of
…[15 more quoted lines elided]…
> devoid of an edge of categorical contempt, intentional or otherwise.

I mean exactly what I say (well, most of the time...sometimes I pretend I'm 
experiencing an emotion just for effect...:-)) and I absolutely say exactly 
what I mean. There are no hidden inferences, suggestions, sniping, cheap 
shots, or anything other than what I wrote. You have been coming here long 
enough to know that, and, frankly, I'm surprised at you. I put it down to 
your passion for your work, your demonstrated over-sensitivity and 
protectiveness of Unisys (they don't need it; they're a good company...), 
and being due for some serious R & R. Don't look for trouble where there 
isn't any...

There are things you and I will never agree on. That doesn't mean I will 
treat you with contempt. And if I have issues with what you say, you'll know 
about it, directly, as in this post.

>
>> I
…[23 more quoted lines elided]…
> so forth that I chose in that *reductio ad absurdum*.

Well, there we differ.  The practise was an "urban myth" because almost 
everybody believed it and many still do. I did.  I see no emotional 
overtones in "urban myth" other than something that is generally accepted 
and probably isn't true. The other phrases were simply my opinion, 
emphatically expressed. There is a huge difference between expressing an 
opinion emphatically, and seeking to dismiss with scorn and implied 
criticism. I think the flaw in your argument is that not all 'categorical 
dismissiveness' implies contempt or scorn. I did categorically dismiss the 
practice, still do, but there was no implicit criticism of people who bought 
it, or of Unisys, or COBOL or anything or anybody.  I do not use the phrases 
you mention and I try to avoid pomposity ("everybody who's anybody" is just 
not something I would even think...)
>
> The problem is, that example isn't all that absurd:  I have heard its 
…[10 more quoted lines elided]…
>
Do I HAVE to... :-)

>> I do not have contempt for ANY environment. My post was strongly
> condemning
…[18 more quoted lines elided]…
>
Well, put it down to writing style and accept that my intentions were 
pure... :-)

>> Interestingly, no one from ICL or Honeywell or NCR or any other major
>> company that was around at the time has taken offence at this or
…[9 more quoted lines elided]…
> themselves visible.

Or over those who do. Like everybody here, the best you can do is express an 
opinion. Different people do it in different ways. That's diversity...
>
> Moreover, I don't think you were contemptuous toward Unisys.  That wasn't 
…[4 more quoted lines elided]…
> else).

Well, we know whnere we disagree, then.

>
> Note that I maintain several software products whose origins lie firmly in
…[14 more quoted lines elided]…
>
All well and good but nothing to do with what we are discussing...

>> It is very wrong of you to take anything I post as a personal attack or 
>> to
…[3 more quoted lines elided]…
> expression of contempt against certain programming practices.

Well it wasn't. And you shouldn't have.

Words and
> phrases like "stupid practice" and "irrelevant" *express* contempt.

No they don't. I can say something is a stupid practice without having 
contempt for the practitioners of it. It may be a statement of fact. It may 
be a statement of the facts as I see them, with no other consideration 
implicit. If I say:" I think that's stupid." Would you think that is 
offensive? Would you still think so if I went to pains to explain WHY I 
thought it was stupid?

How is it different if  I state: ""I think that's a stupid practice."?  It 
isn't. If I look at things I've done in the past and say: "That was stupid." 
How is it offensive? That is exactly what I said here. I was talking about a 
past practice and I dismissed it as stupid. Because it was. NO other reason.

If something is irrelevant, then it is irrelevant. There are no emotional 
overtones attached to this word that I know of.
>
>> I don't come here to denigrate companies or environments; not even by
>> omission.
>
> That's good; I'm glad you clarified your intent.

I'm sorry I had to.
>
>> Think about your position.
…[3 more quoted lines elided]…
> possible variety of platforms, is a primary goal.

I disagree. It can be a goal, but it is nowhere near a primary goal in my 
book.

Now, did I say that to offend you or dismiss you with scorn? No. I said it 
because it is what I think. I know you disagree and i respect your right to 
do so. No problem.
>
<snipped tedious discussion that is irrelevant to locality of reference or 
emotional implications when expressing things forcefully>>
>
> The position I am coming from is much more closely related to my
…[3 more quoted lines elided]…
> efficiency on *both* (as for my example above).

Don't sweat it. The world is running fine on both these platforms.

>
> One of the arguments *it seems to me* you are making in favor of a 
…[11 more quoted lines elided]…
> is not universal.

I should have snipped the above because it is irrelevant too, but it is so 
dear to my heart (you are not the only one who cares about what he does, 
Chuck :-)), that I really couldn't let it go by...

The point was entirely missed. I have not argued for modular programming in 
anything other than a specific environment: online processing in 
multitasking environments (excluding Unisys whose architecture is apparently 
not of this  world :-)).

It all comes down to the three factors in my article. Small optimizes those 
factors better than large. (But capture time is the most important as Rick 
reminded me... so a very large module with a small capture time COULD do 
well.) The generalization is exactly that, general... and. like most rules 
of thumb it is adequate for most situations.

One of the things I really love about this forum is that you can make a 
generalization (with the intention of providing something simple that might 
actually be of use to people who haven't been programming for centuries...), 
and instantly it is like a red rag to a bull, and exceptions will be 
immediately contrived purely for the sake of argument. Not because they're 
even important or should be flagged, but because imprecision cannot be 
tolerated (even when  it is stated to be imprecise). It is a pedant thing... 
:-) I've come to a point now where I just smile at it, but it used to bother 
me. Not that I'm imprecise when I write code; my stuff works (well, it does 
for the most part...:-)), but I'm kind of glad I got older and wiser and 
more relaxed so I don't get burned up about COBOL, or ASP, or Java  or 
anything else computer related. Caring is one thng; obsession is quite 
another...

>It may be more efficient, it may be much less efficient.
> Other reasons to use -- or not to use -- such an approach may well be of
> overriding importance to the end user -- *including* in the very 
> environment
> to which you now limit your categorizations.

Nope. I know how it works on the platforms I have experience with. Small is 
beautiful in online environments for the reasons I have expounded at length, 
and it is still beautiful whether it is stack based, register based, time 
sliced, or interrupt driven. (as a general rule, of course... er, not on 
Unisys... for the most part...in general... probably not on Fridays...etc.)

You are simply hoping it isn't for the sake of an argument... :-)

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 8)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-07-30T17:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31PGe.44139$t43.19225@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net>`

```
Liberally snipping without mention.  This may have been better as a private 
posting between the two of you, but as I'm allowed to participate I thought 
what the hey....

One of you may have been wrong in the eyes of the other and was big enough 
to apologize - as an innocent bystander I think that both of you should kiss 
and make up  :-)

>>"Chuck Stevens"
>"Pete Dashwood"

> Now, see, that is a very understandable viewpoint for a man with either of 
> your hats. But those of us who go around hatless  really don't care. In 
…[4 more quoted lines elided]…
> to me, and I agree with it.

I'd go one further and say that most people don't even refer to the manual 
for COBOL.  With "newer" languages the API's the libraries are quickly 
expanding - someone somewhere has done what you want before and hopefully 
it's free.  I'm afraid that once someone has been coding COBOL for 5+ years 
there's two general methods of making changes - (1) Done it before or (2) 
Someone I work with has...and sometimes (3) Implementation manual.

When I say most people - I mean most people that I have had the pleasure of 
dealing with at some level.

I would buy the argument that not enough was done to make the standards 
flexible and current enough for modern tasks - and that's where your <Chuck> 
efforts are appreciated.

> If you are offended because the world at large does not embrace your 
> ideals, whose problem is that, Chuck?
Depends on the ideals.  Whether embraced or not doesn't determine the right 
or wrong.  I think we've seen that on here at great lengths on everything 
from GOTO's, PERFORM THRUS, Components, OO, Abortion,  and the use of 
dialogue as a verb.  The problem is _obviously_ Microsoft.

>> one of the big reasons I choose to be involved with the standardization
>> process.  Coding conventions may be obviously vendor-specific, but 
…[4 more quoted lines elided]…
> with it.
It's a problem when migrating from one platform / vendor to another. 
Typically I believe these are handled by very  underpaid staff so the hours 
are irrelevant, or very highly paid individuals in which case the difficulty 
is irrelevant.

>>> It isn't if I choose to limit my comments to a particular environment.
>> Well, you did that after the fact.
…[4 more quoted lines elided]…
> That's life in CLC... (gotta love it... :-))
As an innocent bystander, it's relatively amusing (but I probably shouldn't 
say so).


> More importantly, I care about newcomers seeing something that Bill was 
> documenting as a matter of record, and thinking it's a good idea. It 
> isn't, and I explained why.
It isn't a good idea in your _realm_.  I think you would have been wise to 
point out that your _realm_ will take into account both more platforms and * 
rather more importantly * more programming paradigms ;-)
Are newcomers entering <fortress cobol>?

> Well, there we differ.  The practise was an "urban myth" because almost 
> everybody believed it and many still do. I did.  I see no emotional 
> overtones in "urban myth" other than something that is generally accepted 
> and probably isn't true.
"Urban myths" have no basis in truth (a half truth at most).  They are 
specifically associated with attempts to deceive. It is easy to infer some 
"contempt"

>> phrases like "stupid practice" and "irrelevant" *express* contempt.
> No they don't. I can say something is a stupid practice without having 
> contempt for the practitioners of it.
Many people working for many companies do stupid things regardless of their 
IQ.
Though I don't  think I'd hear the phrase "You're very smart but what you do 
is stupid"

I think it's deuce, if you're keeping score


JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-07-31T14:26:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3l2r7eF10g4cnU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net> <31PGe.44139$t43.19225@tornado.tampabay.rr.com>`

```
 

"jce" <defaultuser@hotmail.com> wrote in message
news:31PGe.44139$t43.19225@tornado.tampabay.rr.com...
>
> Liberally snipping without mention.  This may have been better as a
> private posting between the two of you, but as I'm allowed to participate
> I thought what the hey....
>

That's the joy of a public forum... :-)

> One of you may have been wrong in the eyes of the other and was big enough
> to apologize - as an innocent bystander I think that both of you should
> kiss and make up  :-)
>

Despite the impression Chuck gained, I don't have contempt for anyone when
it comes to IT. It's an emotion I reserve for bottom feeders and people who
behave dishonourably or renege on their word and such, and even then I try
to understand them before allowing contempt to rise. I certainly don't bandy
it about in public forums and if I was that pissed off about something I'd
say so up front and have done. Actually, I think Chuck knows that and he
hinted  at it in some of his correspondence...)

>>>"Chuck Stevens"
>>"Pete Dashwood"
…[18 more quoted lines elided]…
>

So you don't include the people you have never met? What about COBOL
programmers on Unisys sites in Ulan Bator? Or Bendix in Chatanooga?  Funny,
I never thought you did. It's kind of implicit...(at least it is to me; but
I'm not sensitive about my company or paranoid that people are out to get
me...)

> I would buy the argument that not enough was done to make the standards
> flexible and current enough for modern tasks - and that's where your
…[4 more quoted lines elided]…
> Depends on the ideals.

No, it depends on how you feel about the ideals. If you are OK with the 
reaction there is no problem. If you are not OK, then it is a problem, for 
you.

>Whether embraced or not doesn't determine the
> right or wrong.

Agreed.(Don't think I suggested otherwise...)

>  I think we've seen that on here at great lengths on
> everything from GOTO's, PERFORM THRUS, Components, OO, Abortion,  and the
> use of dialogue as a verb.  The problem is _obviously_ Microsoft.
>
ROFL! yeah, that's right... :-)

>>> one of the big reasons I choose to be involved with the standardization
>>> process.  Coding conventions may be obviously vendor-specific, but
…[9 more quoted lines elided]…
>
Yes. And like many problems in busy IT departments it gets dealt with when 
it HAS to be dealt with. I don't disagree with Chuck trying to nip it in the 
bud by writing platform independent standardised code, I just don't think 
that is a viable "primary priority".

What if you invest all that time and effort in raising standards awareness 
and enforcing standardised code, no vendor extensions or liberal 
interpretations of the standard, and then the world goes and decides COBOL 
is no longer relevant anyway because there are better and faster tools 
available? Or you NEVER transport the code to any other platform? Or you 
realise that you could have spent the money on better hardware or some other 
priority? Or the whole lot gets replaced by SAP?

>>>> It isn't if I choose to limit my comments to a particular environment.
>>> Well, you did that after the fact.
…[7 more quoted lines elided]…
>
Innocent? Pshaw! NOBODY here is innocent... :-) (another generalization that 
demonstrates my contempt for the frequenters of this forum...or is it just 
innocent fun? I realize it's tough when people have to think about what they 
read.... :-))
>
>> More importantly, I care about newcomers seeing something that Bill was
…[5 more quoted lines elided]…
> Are newcomers entering <fortress cobol>?
Man, I hope not... :-)

>> Well, there we differ.  The practise was an "urban myth" because almost
>> everybody believed it and many still do. I did.  I see no emotional
…[5 more quoted lines elided]…
>
Then perhaps your usage of this term differs from mine. Taking inferences is 
always a risky business,
 and particularly so when the statement is made by someone who has implied 
nothing and stated what was intended.
Nothing more, nothing less.

>>> phrases like "stupid practice" and "irrelevant" *express* contempt.
>> No they don't. I can say something is a stupid practice without having
…[5 more quoted lines elided]…
>
I have actually said to a Senior Manager: "For a team of very smart people, 
there are some really stupid things going on here." No offense was implied 
or taken. We fixed it.

> I think it's deuce, if you're keeping score
>
Hahaha! Wimbledon is over... Thank you for having us tied; I felt, as I 
often do here, that I was losing the rally.

Pete (who has now left Centre Court for more important business...).
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-01T15:14:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcm6sh$2smh$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net>`

```
I think the following points are key to our mutual miscommunications:

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3l1g7qFvs80mU1@individual.net...

> If I say:" I think that's stupid." Would you think that is
> offensive? Would you still think so if I went to pains to explain WHY I
> thought it was stupid?

Much less offensive than "That's stupid."  Even less so if you explained how
you came to that particular *opinion*, precisely because you made it clear
from the outset that it was a statement of opinion and not an *ex cathedra*
pronouncement of universal and incontrovertible truth.

> How is it different if  I state: ""I think that's a stupid practice."?  It
> isn't.

From "That's a stupid practice?"  Oh, yes, it is, by the rules of English.
Saying "That's a stupid practice" to someone or some group is hugely
different in a number of ways from saying "I think that's a stupid practice"
to that person.   The former is an assertion of absolute fact; the latter is
a clear expression of opinion.

> If I look at things I've done in the past and say: "That was stupid."

Then you are characterizing *your* actions based on *your* experience in
*your* environment.   Given that specific context, it's a "transform" from
"[I think] that was [a] stupid [action on my part]."   That's quite
different from "That is/was/would be [a] stupid [action on your part]".

I note that the Webster's Ninth entry for "stupid" includes such shadings as
"slow of mind; given to unintelligent decisions or act; acting in an
untelligent or careless manner; marked by or resulting from unreasoned
thinking."  The synonym list notes that the term "stupid" implies
slow-wittedness.  To use the term "stupid" to describe the actions of
another person, the clear implication is that the actions being described
are the actions to be expected *of a slow-witted person*.  That's quite
different from terms like "suboptimal" or even "ill-advised".

Moreover, I have no problem with just about anything prefixed by "I think
... " or even "My experience leads me to believe ...", and I try to ensure
that I don't omit such qualifications.  When I do, it's usually because I
provide documentation for my view on the subject (as for example the summary
of the dictionary entry above!).

> How is it offensive? That is exactly what I said here. I was talking about
a
> past practice and I dismissed it as stupid. Because it was. NO other
reason.
>
> There are no emotional overtones attached to this word that I know of.

Which word?  I think I've provided sufficient documentation to support my
contention that there are *indeed* a number of emotional overtones attached
to the word "stupid" that don't apply to the likes of "irrelevant",
"ill-advised", "suboptimal", "counterproductive" or even "wrong-headed" in
the same context.

Statements like "Doing <x> is stupid" strike me as carrying a whole lot more
semantic baggage and implicit categorization than "I have found doing <x> to
be a bad idea" or even "I think doing <x> is a bad idea."   It doesn't
matter what <x> is.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-02T13:53:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3l8212F11cvb0U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com>`

```
 
OK.

Your issue is with me expressing opinion as if it was "fact", right?

Whatever I write is my opinion, just as whatever you write is your opinion, 
and whatever anyone posts is their opinion.

Keep that in mind when you read my posts and you will feel better about 
them.

I believe what I write, so, for me, it is a fact. If I express it forcefully 
that may reflect that I feel strongly about it.

The truth or otherwise of what I write is not affected by how it is 
expressed.

Don't be offended by my certainty about something.

If you disagree, fine. Make your case or choose not to; it's up to you.

I was interested in your expression "absolute fact" below. My experience is 
that there is no such thing. There are "facts" that many people agree to be 
so, and that makes them real. I do not ascribe to Newton's view of the 
Universe, where there are absolutes that provide the canvas for the events 
of our lives. So you and I will disagree upon what "fact" or "truth" is...

Take a look at this link: 
http://www.spaceandmotion.com/Philosophy-Absolute-Truth-Space.htm

As always, I call 'em like I see 'em.

Pete.

TOP POST no more below.


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dcm6sh$2smh$1@si05.rsvl.unisys.com...
>
> I think the following points are key to our mutual miscommunications:
…[76 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T05:11:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcndb5$9c9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <3l8212F11cvb0U1@individual.net>`

```
In article <3l8212F11cvb0U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>OK.
…[4 more quoted lines elided]…
>and whatever anyone posts is their opinion.

Is that a fact?

[snip]

>I was interested in your expression "absolute fact" below. My experience is 
>that there is no such thing.

Ahhhhh... so 'everything is relative'... and that's absolutely true!

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-02T12:45:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ev8ogi1354seb@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcndb5$9c9$1@panix5.panix.com...
> In article <3l8212F11cvb0U1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> >Whatever I write is my opinion, just as whatever you write is your
opinion,
> >and whatever anyone posts is their opinion.
>
…[4 more quoted lines elided]…
> >I was interested in your expression "absolute fact" below. My experience
is
> >that there is no such thing.
>
> Ahhhhh... so 'everything is relative'... and that's absolutely true!

H'm! I see that Mr Dashwood referred to 'fact' and 'experience'
and not to 'everything'. David Hume in "An Enquiry Concerning
Human Understanding" seems to suggest that matters of fact are
related to one's experience.

See < http://etext.library.adelaide.edu.au/h/hume/david/h92e >
for complete text.
< http://etext.library.adelaide.edu.au/h/hume/david/h92e/sec04.html >
---- begin quoted material
SECTION IV: SCEPTICAL DOUBTS CONCERNING THE
OPERATIONS OF THE UNDERSTANDING, PART I

If we would satisfy ourselves, therefore, concerning the nature
of that evidence, which assures us of matters of fact, we must
enquire how we arrive at the knowledge of cause and effect.

I shall venture to affirm, as a general proposition, which admits
of no exception, that the knowledge of this relation is not, in any
instance, attained by reasonings a priori; but arises entirely from
experience, ....

This proposition, that causes and effects are discoverable, not
by reason but by experience, will readily be admitted with
regard to such objects, as we remember to have once been
altogether unknown to us; since we must be conscious of the
utter inability, which we then lay under, of foretelling what
would arise from them. ....
----- end quoted material
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T13:09:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco9cg$adr$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com>`

```
In article <11ev8ogi1354seb@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcndb5$9c9$1@panix5.panix.com...
…[20 more quoted lines elided]…
>and not to 'everything'.

Mr Dashwood refers to 'my experience'; I do not see how this differs from 
'everything in my experience'... but I could be wrong.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-02T15:22:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11evi2pqvqd0cf0@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dco9cg$adr$1@panix5.panix.com...
> In article <11ev8ogi1354seb@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcndb5$9c9$1@panix5.panix.com...
> >> In article <3l8212F11cvb0U1@individual.net>,
> >> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> >> >Whatever I write is my opinion, just as whatever you write is your
opinion,
> >> >and whatever anyone posts is their opinion.
> >>
…[4 more quoted lines elided]…
> >> >I was interested in your expression "absolute fact" below. My
experience is
> >> >that there is no such thing.
> >>
…[6 more quoted lines elided]…
> 'everything in my experience'... but I could be wrong.

Mr Dwarf, I hope you are not 'wrong' since that may imply
a moral failing; perhaps you are mistaken, which does not
imply a moral failing.

David Hume, at the beginning of Section IV, wrote,

"ALL the objects of human reason or enquiry may naturally be
divided into two kinds, to wit, Relations of Ideas, and Matters
of Fact. Of the first kind are the sciences of Geometry, Algebra,
and Arithmetic; and in short, every affirmation which is either
intuitively or demonstratively certain. That the square of the
hypothenuse is equal to the square of the two sides, is a
proposition which expresses a relation between these figures.
That three times five is equal to the half of thirty, expresses a
relation between these numbers. Propositions of this kind are
discoverable by the mere operation of thought, without
dependence on what is anywhere existent in the universe.
Though there never were a circle or triangle in nature, the truths
demonstrated by Euclid would for ever retain their certainty
and evidence.

"Matters of fact, which are the second objects of human
reason, are not ascertained in the same manner; nor is our
evidence of their truth, however great, of a like nature with the
foregoing. The contrary of every matter of fact is still possible;
because it can never imply a contradiction, and is conceived
by the mind with the same facility and distinctness, as if ever so
conformable to reality. That the sun will not rise to-morrow is
no less intelligible a proposition, and implies no more
contradiction than the affirmation, that it will rise. We should
in vain, therefore, attempt to demonstrate its falsehood. Were
it demonstratively false, it would imply a contradiction, and
could never be distinctly conceived by the mind."

Hume seems to be saying that the universe of reason ("ALL
the objects" seems to be a universe, or 'everything') consists
of Ideas and Facts ("Relations of Ideas, and Matters of Fact");
that (from the snipped quote) facts are related to experience,
but not so ideas since facts "are not ascertained in the same
manner" as ideas; therefore, when speaking, as Mr Dashwood
did, of 'fact' and 'experience', 'facts are relative', but not
'everthing is relative', since 'everything' includes ideas, which
Mr Dashwood did not mentioned; I too could be mistaken,
but I am definitely not wrong.
```

###### ↳ ↳ ↳ Wrong

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T19:40:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcoi7o$fc9$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com>`

```

On  2-Aug-2005, "Rick Smith" <ricksmith@mfi.net> wrote:

> Mr Dwarf, I hope you are not 'wrong' since that may imply
> a moral failing; perhaps you are mistaken, which does not
> imply a moral failing.
...
>  I too could be mistaken,
> but I am definitely not wrong.

You could infer that he was using this definition of "wrong".   But here are
some other ways that word is used:

# adjective:   not correct; not in conformity with fact or truth (Example: "The
report in the paper is wrong")
# adjective:   not appropriate for a purpose or occasion (Example: "Said all the
wrong things")
# adjective:   badly timed (Example: "It was the wrong moment for a joke")
# adverb:   in an incorrect manner (Example: "She guessed wrong")

Going the wrong way can be a simple mistake.
```

###### ↳ ↳ ↳ Re: Wrong

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-02T16:42:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11evmmviarbqm5b@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcoi7o$fc9$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:dcoi7o$fc9$1@peabody.colorado.edu...
>
> On  2-Aug-2005, "Rick Smith" <ricksmith@mfi.net> wrote:
…[8 more quoted lines elided]…
> You could infer that he was using this definition of "wrong".   But here
are
> some other ways that word is used:
>
> # adjective:   not correct; not in conformity with fact or truth (Example:
"The
> report in the paper is wrong")

This could be a moral failing on the part of the author, if the fact
or truth could have been ascertained with 'reasonable' effort.

> # adjective:   not appropriate for a purpose or occasion (Example: "Said
all the
> wrong things")

This could be a moral failing on the part of the speaker, if the
speaker had not given due consideration before speaking.

> # adjective:   badly timed (Example: "It was the wrong moment for a joke")

The same as the preceding.

> # adverb:   in an incorrect manner (Example: "She guessed wrong")

Irrelevant, in this case, because the 'wrong' on which I
remarked was used as an adjective.

> Going the wrong way can be a simple mistake.

But driving a car (going) the wrong way on a one-way street
is still treated as an offense against society. Going the wrong
way on an escalator may be considered offensive to those
going the right way, even if the offender mistaken failed to
complete a task before getting on the escalator.
```

###### ↳ ↳ ↳ Re: Wrong

_(reply depth: 16)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-02T14:19:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcoo25$1cnj$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcoi7o$fc9$1@peabody.colorado.edu> <11evmmviarbqm5b@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:11evmmviarbqm5b@corp.supernews.com...

> Going the wrong
> way on an escalator may be considered offensive to those
> going the right way ...

Referring back to an earlier thread:  regardless of *offensiveness*, is
there ever a case in which it might *not* be considered *stupid* to go the
wrong way on an escalator?       ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Wrong

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-02T18:51:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11evuaa8gtgr36c@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcoi7o$fc9$1@peabody.colorado.edu> <11evmmviarbqm5b@corp.supernews.com> <dcoo25$1cnj$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:dcoo25$1cnj$1@si05.rsvl.unisys.com...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[8 more quoted lines elided]…
> wrong way on an escalator?       ;-)

A person on an escalator notices another in danger and
goes the wrong way for the purpose of assisting that other.
Those unaware of the circumstances might consider this
going the wrong way as 'stupid'. Those aware, or who
become aware, of the circumstances might consider this
going the wrong way to be part of 'heroism' and,
therefore, not 'stupid'. I am assuming that heroism and
stupidity are mutually exclusive; that is, there are no stupid
heroes even though some acts taken out of the context of
heroism may seem stupid.

"You're saying he ran into a burning building. That's stupid!"
"He saved a child. That makes him a hero!"

"What? A Dutch boy stuck his finger in a dike. That's stupid!"
"He saved a village. That makes him a hero!"
```

###### ↳ ↳ ↳ Re: Wrong

_(reply depth: 18)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-03T09:18:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqqpt$2lfn$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l8212F11cvb0U1@individual.net> <dcndb5$9c9$1@panix5.panix.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcoi7o$fc9$1@peabody.colorado.edu> <11evmmviarbqm5b@corp.supernews.com> <dcoo25$1cnj$1@si05.rsvl.unisys.com> <11evuaa8gtgr36c@corp.supernews.com>`

```
By George, I think he's got it!

Characterizing an actual or potential action taken by someone as "stupid"
carries implications about the fundamental capabilities of the person taking
that action that differ significantly from those implicit in characterizing
the actions as, for example, "inappropriate", "ill-advised", "suboptimal",
"inefficient", or even "bad practice".

    -Chuck Stevens

<top post, no more below>


"Rick Smith" <ricksmith@mfi.net> wrote in message
news:11evuaa8gtgr36c@corp.supernews.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
…[10 more quoted lines elided]…
> > there ever a case in which it might *not* be considered *stupid* to go
the
> > wrong way on an escalator?       ;-)
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T19:29:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcovjs$lmh$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com>`

```
In article <11evi2pqvqd0cf0@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dco9cg$adr$1@panix5.panix.com...
…[32 more quoted lines elided]…
>imply a moral failing.

Implication is in the mind of the beholder, of course... but be that as it 
may...

>
>David Hume, at the beginning of Section IV, wrote,
…[11 more quoted lines elided]…
>dependence on what is anywhere existent in the universe.

Mr Hume appears to be saying that 'the operation of thought' does not 
exist anywhere in the universe ('discoverable by... operation of thought, 
without dependence on what is anywhere existent') or he posits a universe 
without thought... which cannot be occupied by sentient beings.

>Though there never were a circle or triangle in nature, the truths
>demonstrated by Euclid would for ever retain their certainty
>and evidence.

Students of Lobachevski might just possibly disagree... but once again, 
how does one know what a universe without Euclid would look like?

(oh... and as for 'wrong' versus 'mistaken' I was using 'wrong' in the 
sense of 
http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=wrong&x=0&y=0 , 
3a: 'the state of being mistaken or incorrect')

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-02T20:58:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f05ngte0rirf2@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11ev8ogi1354seb@corp.supernews.com> <dco9cg$adr$1@panix5.panix.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcovjs$lmh$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcovjs$lmh$1@panix5.panix.com...
> In article <11evi2pqvqd0cf0@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
[snip]
> >David Hume, at the beginning of Section IV, wrote,
> >
…[15 more quoted lines elided]…
> without thought... which cannot be occupied by sentient beings.

Much of science fiction is 'operation of thought', independent
of the existence of aliens, monsters, etc. Mr Hume appears to
be saying that things need not exist for people to think about them.

> >Though there never were a circle or triangle in nature, the truths
> >demonstrated by Euclid would for ever retain their certainty
…[3 more quoted lines elided]…
> how does one know what a universe without Euclid would look like?

I am not certain that one would know, but one could imagine,
by 'mere operation of thought', a universe with the same
knowledge presented by a person with a different name.
How about non-Dwarfian geometry, as an alternative to truths
demonstrated by Dwarf?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:20:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp652$l32$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcovjs$lmh$1@panix5.panix.com> <11f05ngte0rirf2@corp.supernews.com>`

```
In article <11f05ngte0rirf2@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcovjs$lmh$1@panix5.panix.com...
…[24 more quoted lines elided]…
>be saying that things need not exist for people to think about them.

Mr Hume's next sentence appears to say the exact opposite, Mr Dashwood.

>
>> >Though there never were a circle or triangle in nature, the truths
>> >demonstrated by Euclid would for ever retain their certainty
>> >and evidence.

To paraphrase: Euclidean truths would for ever retain their certainty and 
evidence in a universe where circles or triangles do not exist.

What would demonstrate this assertion I do not know since the only 
universe I know of has circles and triangles - or reasonable facsimiles 
thereof - in it.

>>
>> Students of Lobachevski might just possibly disagree... but once again,
…[6 more quoted lines elided]…
>demonstrated by Dwarf?

I did not know I've been demonstrating truths... but thanks for the 
warning, I'll try not to do such things in public.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:23:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp6av$f0l$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcovjs$lmh$1@panix5.panix.com> <11f05ngte0rirf2@corp.supernews.com>`

```
In article <11f05ngte0rirf2@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcovjs$lmh$1@panix5.panix.com...
…[24 more quoted lines elided]…
>be saying that things need not exist for people to think about them.

Mr Hume's next sentence appears to say the exact opposite, Mr Smith

>
>> >Though there never were a circle or triangle in nature, the truths
>> >demonstrated by Euclid would for ever retain their certainty
>> >and evidence.

To paraphrase: Euclidean truths would for ever retain their certainty and 
evidence in a universe where circles or triangles do not exist.

What would demonstrate this assertion I do not know since the only 
universe I know of has circles and triangles - or reasonable facsimiles 
thereof - in it.

>>
>> Students of Lobachevski might just possibly disagree... but once again,
…[6 more quoted lines elided]…
>demonstrated by Dwarf?

I did not know I've been demonstrating truths... but thanks for the 
warning, I'll try not to do such things in public.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-03T01:08:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f0khe8tp1jccb@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11evi2pqvqd0cf0@corp.supernews.com> <dcovjs$lmh$1@panix5.panix.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcp6av$f0l$1@panix5.panix.com...
> In article <11f05ngte0rirf2@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcovjs$lmh$1@panix5.panix.com...
> >> In article <11evi2pqvqd0cf0@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[16 more quoted lines elided]…
> >> exist anywhere in the universe ('discoverable by... operation of
thought,
> >> without dependence on what is anywhere existent') or he posits a
universe
> >> without thought... which cannot be occupied by sentient beings.
> >
…[4 more quoted lines elided]…
> Mr Hume's next sentence appears to say the exact opposite, Mr Smith

Well, Mr Dwarf, it does seem reasonable for me to disagree.

> >
> >> >Though there never were a circle or triangle in nature, the truths
…[4 more quoted lines elided]…
> evidence in a universe where circles or triangles do not exist.

Replace 'in a universe where circles or triangles do not exist'
with 'even if there never were a circle or triangle in nature'.

Hume wrote 'without dependence on what is anywhere existent
in the universe' in the sentence preceding his remark about Euclid.
In my opinion, Hume is saying that Euclidean truths do not
*depend* upon the existence of circles and triangles in nature;
that is, if Euclid invented circles and triangles and demonstrated
truths about these inventions, the truths would for ever retain
their certainty and evidence. It is not 'a universe where circles
and triangles do not exist'; but rather need not have existed for
Euclid to think about them.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T05:31:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcq2u1$cht$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com> <11f0khe8tp1jccb@corp.supernews.com>`

```
In article <11f0khe8tp1jccb@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcp6av$f0l$1@panix5.panix.com...
…[33 more quoted lines elided]…
>Well, Mr Dwarf, it does seem reasonable for me to disagree.

Oh good... if I wanted only agreement I would speak only with my mirror, 
you know.

>> >> >
>> >> >Though there never were a circle or triangle in nature, the truths
…[15 more quoted lines elided]…
>their certainty and evidence.

Ahhhh... if Euclid had invented circles and triangles then it would no 
longer be a universe in which circles and triangles do not exist, Euclid's 
actions would have changed things... but even without the invention the 
truths retain their certainty.

>It is not 'a universe where circles
>and triangles do not exist'; but rather need not have existed for
>Euclid to think about them.

I disagree, as above, in that Hume refers to the conclusions (truths) and 
not the processes which generated them.  No matter how those conclusions 
came about (fully-formed from the forehead) their 'certainty and evidence'
would be retained.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T14:04:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqisr$jve$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> Oh good... if I wanted only agreement I would speak only with my mirror,
> you know.

If you spoke only with your mirror, would you succeed in finding only agreement?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T10:18:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqjnu$9qu$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <dcqisr$jve$1@peabody.colorado.edu>`

```
In article <dcqisr$jve$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>agreement?

I'm not sure that is an absolute fact... I avoid mirrors, the psychopath 
who lives in them frightens me.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T02:38:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lc370F11nl7gU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <dcqisr$jve$1@peabody.colorado.edu> <dcqjnu$9qu$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcqjnu$9qu$1@panix5.panix.com...
>
> In article <dcqisr$jve$1@peabody.colorado.edu>,
…[12 more quoted lines elided]…
>
Hahaha! Snap! (I didn't read this until after I posted to Howard...)

Obviously, the Dwarf mirror is a lot more direct than the Dashwood one...:-)

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T02:36:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lc32qF125qdgU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <dcqisr$jve$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dcqisr$jve$1@peabody.colorado.edu...
>
>
…[7 more quoted lines elided]…
>
My mirror has a very limited vocabulary; the only thing it ever says is: 
"You're not getting any better looking..."

(Of course, I know it is only the mirror's opinion and not "absolute 
fact"... :-))

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-03T21:31:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<669fe$42f17def$45491c57$30222@KNOLOGY.NET>`
- **In-Reply-To:** `<dcqisr$jve$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <dcqisr$jve$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  3-Aug-2005, docdwarf@panix.com wrote:
> 
…[5 more quoted lines elided]…
> If you spoke only with your mirror, would you succeed in finding only agreement?

........must.......not.......jump.....on.......straight......line..........

*whew*  that was close...
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-03T10:54:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f1mngaduglp71@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f05ngte0rirf2@corp.supernews.com> <dcp6av$f0l$1@panix5.panix.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcq2u1$cht$1@panix5.panix.com...
> In article <11f0khe8tp1jccb@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcp6av$f0l$1@panix5.panix.com...
> >> In article <11f05ngte0rirf2@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[20 more quoted lines elided]…
> >> >> Mr Hume appears to be saying that 'the operation of thought' does
not
> >> >> exist anywhere in the universe ('discoverable by... operation of
thought,
> >> >> without dependence on what is anywhere existent') or he posits a
universe
> >> >> without thought... which cannot be occupied by sentient beings.
> >> >
…[16 more quoted lines elided]…
> >> To paraphrase: Euclidean truths would for ever retain their certainty
and
> >> evidence in a universe where circles or triangles do not exist.
> >
…[14 more quoted lines elided]…
> truths retain their certainty.

Perhaps you overlooked 'and demonstrated truths about these
inventions' ... had these truths not been demonstrated there
would be no truths to retain.

> >It is not 'a universe where circles
> >and triangles do not exist'; but rather need not have existed for
…[5 more quoted lines elided]…
> would be retained.

Hume referred to the process earlier in the paragraph as
'operations of thought' which is reflected in 'demonstrated';
that is Euclid's 'demonstrated truths' are the result of Euclid's
'operations of thought'.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T11:04:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqmee$nra$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <11f1mngaduglp71@corp.supernews.com>`

```
In article <11f1mngaduglp71@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcq2u1$cht$1@panix5.panix.com...
…[69 more quoted lines elided]…
>would be no truths to retain.

That is not how I read it; I read 'Though there never were a circle or 
triangle in nature, the truths demonstrated by Euclid would for ever 
retain their certainty and evidence' as a postulating of a Platonic 
Universe of Forms, where the truths demonstrated by Euclid would retain 
their certainty whether Euclid demonstrated them or not.
>
>> >It is not 'a universe where circles
…[11 more quoted lines elided]…
>'operations of thought'.

Said 'operations of thought', however, occurred in a universe where 
circles and triangles already existed.  Hume's positing a universe where 
truths exist without their objects smacks, as mentioned earlier, of the 
Platonic.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T15:33:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqo3r$mp5$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> That is not how I read it; I read 'Though there never were a circle or
> triangle in nature, the truths demonstrated by Euclid would for ever
> retain their certainty and evidence' as a postulating of a Platonic
> Universe of Forms, where the truths demonstrated by Euclid would retain
> their certainty whether Euclid demonstrated them or not.

The ancient Greeks tended to favor logical constructs over observable results.
They aren't alone (Descartes was good at this).   I think we all have some
biases of how things "should be", even if these biases can be contradictory.

But we can't test "should be".   We can argue about it, "prove" it, and we can
kill and die for it.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T11:48:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqovs$7e6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com> <dcqo3r$mp5$1@peabody.colorado.edu>`

```
In article <dcqo3r$mp5$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>The ancient Greeks tended to favor logical constructs over observable results.

Some did, some didn't.  Socrates (via Plato) and Aristotle seem to fall in 
the camp you mention, Archimedes and Eratosthenes seem to fall in 
another... and then there's Ptolemy, worthy of Much Study.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-04T10:24:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f49d4jh9pqg99@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcqmee$nra$1@panix5.panix.com...
> In article <11f1mngaduglp71@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcq2u1$cht$1@panix5.panix.com...
> >> In article <11f0khe8tp1jccb@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[15 more quoted lines elided]…
> >> >> >> >of Fact. Of the first kind are the sciences of Geometry,
Algebra,
> >> >> >> >and Arithmetic; and in short, every affirmation which is either
> >> >> >> >intuitively or demonstratively certain. That the square of the
> >> >> >> >hypothenuse is equal to the square of the two sides, is a
> >> >> >> >proposition which expresses a relation between these figures.
> >> >> >> >That three times five is equal to the half of thirty, expresses
a
> >> >> >> >relation between these numbers. Propositions of this kind are
> >> >> >> >discoverable by the mere operation of thought, without
> >> >> >> >dependence on what is anywhere existent in the universe.
> >> >> >>
> >> >> >> Mr Hume appears to be saying that 'the operation of thought' does
not
> >> >> >> exist anywhere in the universe ('discoverable by... operation of
thought,
> >> >> >> without dependence on what is anywhere existent') or he posits a
universe
> >> >> >> without thought... which cannot be occupied by sentient beings.
> >> >> >
> >> >> >Much of science fiction is 'operation of thought', independent
> >> >> >of the existence of aliens, monsters, etc. Mr Hume appears to
> >> >> >be saying that things need not exist for people to think about
them.
> >> >>
> >> >> Mr Hume's next sentence appears to say the exact opposite, Mr Smith
…[3 more quoted lines elided]…
> >> Oh good... if I wanted only agreement I would speak only with my
mirror,
> >> you know.
> >>
> >> >> >> >
> >> >> >> >Though there never were a circle or triangle in nature, the
truths
> >> >> >> >demonstrated by Euclid would for ever retain their certainty
> >> >> >> >and evidence.
> >> >>
> >> >> To paraphrase: Euclidean truths would for ever retain their
certainty and
> >> >> evidence in a universe where circles or triangles do not exist.
> >> >
…[12 more quoted lines elided]…
> >> longer be a universe in which circles and triangles do not exist,
Euclid's
> >> actions would have changed things... but even without the invention the
> >> truths retain their certainty.
…[9 more quoted lines elided]…
> their certainty whether Euclid demonstrated them or not.

Well, I don't know nuthin' about that Platonic Universe
of Forms. The sentence preceding the quote begins
"Propositions of this kind are discoverable ..."; I suppose
one could speculate that Hume was saying that such
propostions are eternal whether discovered or not; but
I've seen nothing elsewhere to warrant such speculation.
Hume also discusses matters of fact and their relation to
experience; but I've seen nothing to suggest an intent that
matters of fact exist whether experienced or not. I think
Hume was saying that truths (about circles and triangles)
demonstrated by Euclid would retain their certainty
whether circles or triangle existed in nature or not.

> >> >It is not 'a universe where circles
> >> >and triangles do not exist'; but rather need not have existed for
> >> >Euclid to think about them.
> >>
> >> I disagree, as above, in that Hume refers to the conclusions (truths)
and
> >> not the processes which generated them.  No matter how those
conclusions
> >> came about (fully-formed from the forehead) their 'certainty and
evidence'
> >> would be retained.
> >
…[8 more quoted lines elided]…
> Platonic.

Negative and imaginary numbers, to the best of my
knowledge, do not exist in *nature*, yet, there are truths
(about these) demonstrated by their discovers using, as
Hume suggests, "mere operation of thought, without
dependence on what is anywhere existent in the universe."
[Hume used 'universe' in one sentence and 'nature' in the
following. I maintain the distinction here because I think
Hume is claiming that "relations of ideas" extend beyond
the (physical) universe; but "matters of fact" are limited to
man's experiences with nature. I find no reason to disagree.]
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T15:06:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctat8$7gi$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f0khe8tp1jccb@corp.supernews.com> <dcq2u1$cht$1@panix5.panix.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com> <11f49d4jh9pqg99@corp.supernews.com>`

```

On  4-Aug-2005, "Rick Smith" <ricksmith@mfi.net> wrote:

> Negative and imaginary numbers, to the best of my
> knowledge, do not exist in *nature*,

What numbers *do* exist in nature?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T11:11:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctb6q$q9p$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com> <11f49d4jh9pqg99@corp.supernews.com>`

```
In article <11f49d4jh9pqg99@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcqmee$nra$1@panix5.panix.com...
…[83 more quoted lines elided]…
>of Forms.

Mr Hume, having a goal of becoming 'a Scholar & Philosopher', most likely 
did.

>The sentence preceding the quote begins
>"Propositions of this kind are discoverable ..."; I suppose
>one could speculate that Hume was saying that such
>propostions are eternal whether discovered or not; but
>I've seen nothing elsewhere to warrant such speculation.

In that the word 'discovered' was used, and not 'invented', it appears to 
be a reasonable conclusion.

>Hume also discusses matters of fact and their relation to
>experience; but I've seen nothing to suggest an intent that
…[3 more quoted lines elided]…
>whether circles or triangle existed in nature or not.

This was not contested; as I stated above: To paraphrase: Euclidean truths 
would for ever retain their certainty and evidence in a universe where 
circles or triangles do not exist.
>
>> >> >It is not 'a universe where circles
…[22 more quoted lines elided]…
>dependence on what is anywhere existent in the universe."

Negative numbers are a shorthand for the process of subtraction... now 
whether arithmetic processes exist in absence of humans to perform them is 
another matter, entire.  (Hume, in accord with the Platonic model, appears 
to say that they do; how this would be corroborated is, as noted above, 
uncertain.)  As for imaginary numbers there is a variation of Kronecker: 
'In nature lies the integers, all the rest is the work of man.'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T16:10:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctelj$9ht$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com>`

```

On  4-Aug-2005, docdwarf@panix.com wrote:

> As for imaginary numbers there is a variation of Kronecker:
> 'In nature lies the integers, all the rest is the work of man.'

What do integers look like?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T13:23:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctiu7$eh1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com> <dctelj$9ht$1@peabody.colorado.edu>`

```
In article <dctelj$9ht$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  4-Aug-2005, docdwarf@panix.com wrote:
…[4 more quoted lines elided]…
>What do integers look like?

I'd imagine that it depends on who is doing the looking.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-05T12:13:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lfp9bF12otbdU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com> <dctelj$9ht$1@peabody.colorado.edu> <dctiu7$eh1$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dctiu7$eh1$1@panix5.panix.com...
>
> In article <dctelj$9ht$1@peabody.colorado.edu>,
…[10 more quoted lines elided]…
>

Precisely like receiving a grain of sand, really...

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T06:28:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvf19$7ht$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctelj$9ht$1@peabody.colorado.edu> <dctiu7$eh1$1@panix5.panix.com> <3lfp9bF12otbdU1@individual.net>`

```
In article <3lfp9bF12otbdU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[15 more quoted lines elided]…
>Precisely like receiving a grain of sand, really...

This seems a reasonable conclusion, Mr Dashwood... but I am willing to 
consider other options, when they are presented.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-04T15:25:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f4r0kga57eda3@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f1mngaduglp71@corp.supernews.com> <dcqmee$nra$1@panix5.panix.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dctb6q$q9p$1@panix5.panix.com...
> In article <11f49d4jh9pqg99@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcqmee$nra$1@panix5.panix.com...
> >> In article <11f1mngaduglp71@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[19 more quoted lines elided]…
> >> >> >> >> >divided into two kinds, to wit, Relations of Ideas, and
Matters
> >> >> >> >> >of Fact. Of the first kind are the sciences of Geometry,
Algebra,
> >> >> >> >> >and Arithmetic; and in short, every affirmation which is
either
> >> >> >> >> >intuitively or demonstratively certain. That the square of
the
> >> >> >> >> >hypothenuse is equal to the square of the two sides, is a
> >> >> >> >> >proposition which expresses a relation between these figures.
> >> >> >> >> >That three times five is equal to the half of thirty,
expresses a
> >> >> >> >> >relation between these numbers. Propositions of this kind are
> >> >> >> >> >discoverable by the mere operation of thought, without
> >> >> >> >> >dependence on what is anywhere existent in the universe.
[snip]
> >> >> >> >> >Though there never were a circle or triangle in nature, the
truths
> >> >> >> >> >demonstrated by Euclid would for ever retain their certainty
> >> >> >> >> >and evidence.
> >> >> >>
> >> >> >> To paraphrase: Euclidean truths would for ever retain their
certainty and
> >> >> >> evidence in a universe where circles or triangles do not exist.
> >> >> >
…[11 more quoted lines elided]…
> >> >> Ahhhh... if Euclid had invented circles and triangles then it would
no
> >> >> longer be a universe in which circles and triangles do not exist,
Euclid's
> >> >> actions would have changed things... but even without the invention
the
> >> >> truths retain their certainty.
> >> >
…[14 more quoted lines elided]…
> did.

Having waded through a wee bit of Philosophy, I'm glad it was
never my goal.

> >The sentence preceding the quote begins
> >"Propositions of this kind are discoverable ..."; I suppose
…[16 more quoted lines elided]…
> circles or triangles do not exist.

I've noticed that philosophers tend to be very selective in
the words they choose and how they use them ... sort of
like: When I use a word, it means exactly what I choose it
to mean, neither more nor less; and I have tried to
understand Hume with that in mind. Hume treats 'truth' as
something distinct from 'fact', while the dictionary I use
defines one in terms of the other. He also seems to use
'universe' as something distinct from 'nature'. Mr Dwarf, it
seems that you substituted 'universe' where Hume used
'nature' and I am sensitive to that substitution; it confuses
me because it is not what Hume wrote, and to my mind
changes his meaning.

Hume divides 'objects of human reason or enquiry' into
two kinds: relations of ideas and matters of fact; and
associates nature with matters of fact. In the clause
'Though there never were a circle or triangle in nature,'
Hume is denying that 'truths demonstrated by Euclid'
could be matters of fact and does so by making nature
irelevant to these truths. This places Geometry into the
kind: relations of ideas. Subtituting 'universe' for 'nature'
confuses that denial since Hume does not associate
universe with matters of fact; this changes the meaning.

If I am mistaken in any of this of if it my OCD, I
apologize. [mistake: an error caused by a lack of skill,
attention, knowledge, etc. -- RHCD]
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T06:35:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvfct$kpv$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com> <11f4r0kga57eda3@corp.supernews.com>`

```
In article <11f4r0kga57eda3@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dctb6q$q9p$1@panix5.panix.com...
>> In article <11f49d4jh9pqg99@corp.supernews.com>,
>> Rick Smith <ricksmith@mfi.net> wrote:

[snip]

>> >Well, I don't know nuthin' about that Platonic Universe
>> >of Forms.
…[5 more quoted lines elided]…
>never my goal.

Not to have included at least a passing reference to concept of eidos 
(translated as 'form')... a 'wee bit' it seems to have been.

[snip]

>> This was not contested; as I stated above: To paraphrase: Euclidean truths
>> would for ever retain their certainty and evidence in a universe where
…[13 more quoted lines elided]…
>changes his meaning.

My error and apology, Mr Smith; it my intention was neither to confuse you 
nor change Hume's meaning.  By 'universe', above, I intended to convey the 
sense of 'all conditions where nature might be found to exist'.

[snip]

>If I am mistaken in any of this of if it my OCD, I
>apologize. [mistake: an error caused by a lack of skill,
>attention, knowledge, etc. -- RHCD]

Not to worry, Mr Smith; now that I am aware of this condition I shall do 
my best to avoid intentionally stimulating or invoking it.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-07T23:00:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fdiopk2atsqbe@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f49d4jh9pqg99@corp.supernews.com> <dctb6q$q9p$1@panix5.panix.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcvfct$kpv$1@panix5.panix.com...
> In article <11f4r0kga57eda3@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dctb6q$q9p$1@panix5.panix.com...
> >> In article <11f49d4jh9pqg99@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[6 more quoted lines elided]…
> >> Mr Hume, having a goal of becoming 'a Scholar & Philosopher', most
likely
> >> did.
> >
…[4 more quoted lines elided]…
> (translated as 'form')... a 'wee bit' it seems to have been.

"There is no reason for studying philosophy--so Hume
maintains--except that, to certain temperaments, this is
an agreeable way of passing the time." -- Bertrand
Russell, "A History of Western Philosophy"

Having now read two similar descriptions of Plato's
Forms, I find that further study of Plato would not be
an agreeable way of my passing the time.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T01:36:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd6r12$i7v$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com> <11fdiopk2atsqbe@corp.supernews.com>`

```
In article <11fdiopk2atsqbe@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dcvfct$kpv$1@panix5.panix.com...
…[25 more quoted lines elided]…
>Russell, "A History of Western Philosophy"

The abovenoted quotation seems not to mention whether Hume believed that 
he had such a temperament... that's one of the problems with secondary 
sources.

>
>Having now read two similar descriptions of Plato's
>Forms, I find that further study of Plato would not be
>an agreeable way of my passing the time.

How interesting... was one of those descriptions Nietzsche's 'Christianity 
is Platonism for the masses'?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-08T08:08:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11feisrmpuo4s3e@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd6r12$i7v$1@panix5.panix.com...
> In article <11fdiopk2atsqbe@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dcvfct$kpv$1@panix5.panix.com...
> >> In article <11f4r0kga57eda3@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[11 more quoted lines elided]…
> >> >> Mr Hume, having a goal of becoming 'a Scholar & Philosopher', most
likely
> >> >> did.
> >> >
…[5 more quoted lines elided]…
> >
[snip]
> >
> >Having now read two similar descriptions of Plato's
…[4 more quoted lines elided]…
> is Platonism for the masses'?

No, in fact, I had neither read Nietzsche nor about him.

I got the distinct impression that Plato's Forms are
inextricably linked to his monotheism. Take away that
belief and his system collapses; not that I claim to
understand Plato, but only that it is the impression
I got.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T08:45:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7k5p$qbp$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com> <11feisrmpuo4s3e@corp.supernews.com>`

```
In article <11feisrmpuo4s3e@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dd6r12$i7v$1@panix5.panix.com...
…[36 more quoted lines elided]…
>No, in fact, I had neither read Nietzsche nor about him.

What a Wonderful World it is that has new things to learn in it... ol' 
Friederich was quite a character.

>
>I got the distinct impression that Plato's Forms are
…[3 more quoted lines elided]…
>I got.

Now there's an interesting concept... Plato's monotheism?  Most text I'm 
familiar with indicate that both Plato and Socrates were fairly 
comfortable with the then-current polytheism in Athens; could you be so 
kind to direct me towards the source which related the Forms to this 
monotheism?

(I tride to find it on my own... but 
<http://www.google.com/search?sourceid=navclient&ie=UTF-8&rls=RNWE,RNWE:2004-33,RNWE:en&q=%22plato%27s+monotheism%22> 
didn't give too much to go on.)

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-08T10:02:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fephkks48so70@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd7k5p$qbp$1@panix5.panix.com...
> In article <11feisrmpuo4s3e@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dd6r12$i7v$1@panix5.panix.com...
> >> In article <11fdiopk2atsqbe@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[16 more quoted lines elided]…
> >> >> >> Mr Hume, having a goal of becoming 'a Scholar & Philosopher',
most likely
> >> >> >> did.
> >> >> >
…[3 more quoted lines elided]…
> >> >> Not to have included at least a passing reference to concept of
eidos
> >> >> (translated as 'form')... a 'wee bit' it seems to have been.
> >> >
…[6 more quoted lines elided]…
> >> How interesting... was one of those descriptions Nietzsche's
'Christianity
> >> is Platonism for the masses'?
> >
…[16 more quoted lines elided]…
> monotheism?

From Bertrand Russell, "A History of Western Philosophy",
page 122,
"In the last book of the Republic, ..., there is a very clear
exposition of the doctrine of ideas or forms.
"Here Plato explains that, whenever a number of individuals
have a common name, they have also a common 'idea' or
'form.' For instance, though there are many beds, there is
only one 'idea' or 'form' of a bed. Just as a reflection of a
bed in a mirror is only apparent and not 'real,' so the various
particular beds are unreal, being only copies of the 'idea,'
which is the one real bed, and is made by God. Of this one
bed, made by God, there can be knowledge, but in respect
of the many beds made by carpenters there can be only
opinion."

Antony Flew, "A Dictionary of Philosophy," does not mention
Plato's theism in the article on Plato; but monotheism is
discussed in the article "Platonism," page 256,
"... Characteristic features of Platonism in the intervening
three centuries, sometimes called 'Middle Platonism', are the
concepts of Ideas as 'thoughts in the mind of God', the moral
idea of 'assimilation to God', and the elaborate doctrine of
demons as intermediaries between the divine and the human."

Russell suggests monotheism, directly, and the followers of
Plato suggest monotheism, indirectly;.thus it is my 'impression'
that 'Plato's Forms are inextricably linked to his monotheism.'
The accuracy of my stating 'his monotheism' depends, it
would seem, on the contents of the last book of the Republic.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T11:42:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7uho$neu$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com> <11fephkks48so70@corp.supernews.com>`

```
In article <11fephkks48so70@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dd7k5p$qbp$1@panix5.panix.com...
…[4 more quoted lines elided]…
>news:dd6r12$i7v$1@panix5.panix.com...

[snip]

>> Now there's an interesting concept... Plato's monotheism?  Most text I'm
>> familiar with indicate that both Plato and Socrates were fairly
…[17 more quoted lines elided]…
>opinion."

(sources given farther down)

'... made by God'.  My guess is that Russell was using Jowett's 1901 
translation.  The Greek shows 597B as having the text 'theon ergasasthai' 
(theta-epislon-omicron-nu 
epsilon-rho-gamma-alpha-sigma-alpha-sigma-theta-alpha-iota), without a 
definite article, capitalisation or any indication that the god who made 
(worked) is any different from other members of the pantheon.

In support of Socrates' polytheism one might wish to take a look at the 
Cratylus - also by Jowett - where Socrates states things like 'Yes, 
indeed, Hermogenes; and there is one excellent principle which, as men of 
sense, we must acknowledge,--that of the Gods we know nothing, either of 
their natures or of the names which they give themselves; but we are sure 
that the names by which they call themselves, whatever they may be, are 
true.  And this is the best of all principles; and the next best is to 
say, as in prayers, that we will call them by any sort or kind of names or 
patronymics which they like, because we do not know of any other.'

... and, referring to a singular, 'And he is the God who presides over 
harmony, and makes all things move together, both among Gods and among 
men.'

(Also consider Phaedrus, which, while making use of the capitalised 'God' 
also contains lines like:

 'Zeus, the mighty lord, holding the reins of a winged chariot, leads the 
way in heaven, ordering all and taking care of all; and there follows him 
the array of gods and demigods, marshalled in eleven bands; Hestia alone 
abides at home in the house of heaven; of the rest they who are reckoned 
among the princely twelve march in their appointed order.' ...

... and the Timaeus, where Socrates states 'I see that I shall receive in 
my turn a perfect and splendid feast of reason. And now, Timaeus, you, I 
suppose, should speak next, after duly calling upon the Gods.' ... and 
then later mentions 'But the father and maker of all this universe is past 
finding out; and even if we found him, to tell of him to all men would be 
impossible'... but these are the words of Timaeus, not Socrates... and 
there are questions about how this 'I shall' should be translated, 
especially in the presence of an iota, indicating the optative mood...

... so there may, indeed, be a primus inter deis... but there most 
certainly appear to be other divinities acknowledged as existing.

(note - Jowett's capital G is not mirrored (in the texts with which I am 
familiar) by a capital theta)

>
>Antony Flew, "A Dictionary of Philosophy," does not mention
…[6 more quoted lines elided]…
>demons as intermediaries between the divine and the human."

This starts to sound like Platonism for the Masses, yes... but Socrates 
freely confessed to having a daimon.

>
>Russell suggests monotheism, directly, and the followers of
…[3 more quoted lines elided]…
>would seem, on the contents of the last book of the Republic.

... and, in particular, a specific translation of the last book of the 
Republic, said translation not reflecting the punctuation of the 
original... and this might be why a Scholar of Oldene Dayse paid 
attention to 'the last iota' lo, such as *ten* Scholars cannot, today!

(well... also, they didn't have television...)

Sources: Jowett's translation of The Republic: 

http://www.ilt.columbia.edu/publications/plato_republic.htm

Original text of Books IX - X:

http://lightning.prohosting.com/~flea333/resp9_10.zip

Jowett's Cratylus:

http://www.gutenberg.org/dirs/etext99/crtls10.txt

Jowett's Phaedrus:

<http://www.ilt.columbia.edu/publications/Projects/digitexts/plato/phaedrus/phaedrus.html>

Jowett's Timaeus:

http://www.piney.com/DocPlatoTim.html

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 31)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T08:59:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7vic$1flp$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com> <11fephkks48so70@corp.supernews.com> <dd7uho$neu$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd7uho$neu$1@panix5.panix.com...
> In article <11fephkks48so70@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dd7k5p$qbp$1@panix5.panix.com...
> >> In article <11feisrmpuo4s3e@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[6 more quoted lines elided]…
> >> Now there's an interesting concept... Plato's monotheism?  Most text
I'm
> >> familiar with indicate that both Plato and Socrates were fairly
> >> comfortable with the then-current polytheism in Athens; could you be so
…[106 more quoted lines elided]…
>
<http://www.ilt.columbia.edu/publications/Projects/digitexts/plato/phaedrus/
phaedrus.html>
>
> Jowett's Timaeus:
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 32)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T16:26:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HILJe.39437$iG6.7625@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com> <11fephkks48so70@corp.supernews.com> <dd7uho$neu$1@panix5.panix.com> <dd7vic$1flp$1@si05.rsvl.unisys.com>`

```
Answering a question with nothing at all is not an answer at all!
JCE

(or did I miss it?)
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 31)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-08T14:58:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ffasfnirr28cd@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com> <11fephkks48so70@corp.supernews.com> <dd7uho$neu$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd7uho$neu$1@panix5.panix.com...
> In article <11fephkks48so70@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:dd7k5p$qbp$1@panix5.panix.com...
> >> In article <11feisrmpuo4s3e@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[6 more quoted lines elided]…
> >> Now there's an interesting concept... Plato's monotheism?  Most text
I'm
> >> familiar with indicate that both Plato and Socrates were fairly
> >> comfortable with the then-current polytheism in Athens; could you be so
…[26 more quoted lines elided]…
>
[snip]
>
> ... and the Timaeus, where Socrates states 'I see that I shall receive in
…[10 more quoted lines elided]…
>
[snip]
> >
> >Russell suggests monotheism, directly, and the followers of
…[8 more quoted lines elided]…
> attention to 'the last iota' lo, such as *ten* Scholars cannot, today!

So ... if I understand correctly, 'monotheism' is not accurate;
but (translating 'primus inter deis' to 'first among gods') Plato
may have been referring to a single god (the one that Timaeus
called 'the father and maker of all this universe') ... and this
inextricably links Forms to a single god theism, just not
monotheism, exactly.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T19:36:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8c7t$1an$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11feisrmpuo4s3e@corp.supernews.com> <dd7k5p$qbp$1@panix5.panix.com> <11fephkks48so70@corp.supernews.com> <dd7uho$neu$1@panix5.panix.com> <11ffasfnirr28cd@corp.supernews.com>`

```

On  8-Aug-2005, "Rick Smith" <ricksmith@mfi.net> wrote:

> So ... if I understand correctly, 'monotheism' is not accurate;
> but (translating 'primus inter deis' to 'first among gods') Plato
…[3 more quoted lines elided]…
> monotheism, exactly.

Of course, the Bible mentions multiple gods.   We are only supposed to worship
the One, and discard the false ones.   Dictionary definitions of monotheism tend
to be on the line of "belief in a single god", and tend to apply to religions of
the book.   It is not clear by reading scripture though that "false" gods didn't
(or don't) exist, nor what their nature is (or are).

So there's some evidence that we can apply monotheism (also in the case of
ancient Egypt), in such a way as to have one dominant God - that doesn't
preclude other divine creatures.    Not that it makes a significant difference
in modern worship - but historically, that difference is more significant.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T17:44:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8jnm$c89$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11fephkks48so70@corp.supernews.com> <dd7uho$neu$1@panix5.panix.com> <11ffasfnirr28cd@corp.supernews.com>`

```
In article <11ffasfnirr28cd@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dd7uho$neu$1@panix5.panix.com...
…[75 more quoted lines elided]…
>monotheism, exactly.

'Monotheism', according to 
http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=monotheism&x=0&y=0 , 
appears to be completely *in*accurate... unless one can, somehow, say that 
one can simultaneously hold 'the doctrine or belief that there is but one 
God' and say things like ''And he is the God who presides over harmony, 
and makes all things move together, both among Gods and among men' or 
'Timaeus, you, I suppose, should speak next, after duly calling upon the 
Gods'.

It is not that there is a single god; it seem the case of 'that which is 
god-made/worked' ('worked' might be a better translation given that the 
root is erg- and not poei-), in this case a bed, partakes more of the Form 
(eidos) of bed than that which a human might make.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T08:49:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7kco$ah7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com> <11feisrmpuo4s3e@corp.supernews.com>`

```
In article <11feisrmpuo4s3e@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:dd6r12$i7v$1@panix5.panix.com...
…[36 more quoted lines elided]…
>No, in fact, I had neither read Nietzsche nor about him.

What a Wonderful World it is that has new things to learn in it... ol' 
Friederich was quite a character.

>
>I got the distinct impression that Plato's Forms are
…[3 more quoted lines elided]…
>I got.

Now there's an interesting concept... Plato's monotheism?  Most text I'm 
familiar with indicate that both Plato and Socrates were fairly 
comfortable with the then-current polytheism in Athens; could you be so 
kind to direct me towards the source which related the Forms to this 
monotheism?

(I tride to find it on my own... but 
<http://www.google.com/search?sourceid=navclient&ie=UTF-8&rls=RNWE,RNWE:2004-33,RNWE:en&q=%22plato%27s+monotheism%22> 
didn't give too much to go on.)

(Come to think of - and look for - it... 
<http://www.google.com/search?hl=en&lr=&rls=RNWE%2CRNWE%3A2004-33%2CRNWE%3Aen&q=%22plato%27s+polytheism%22> 
doesn't give too much to go on, either.)

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-08T20:37:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BoPJe.959452$pI6.36867@fe06.news.easynews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com>`

```
I have HEARD (or read) that there is an (unwritten?) rule that when somone 
(naturally) brings Hitler into a thread in a newsgroup, that it is supposed to 
kill off (end) that thread.

I seem to remember (although certainly will not stake my life and liberty on it) 
that I have actually seen this happen.

My best guess (far from a certainty) is that this will NOT happen with this 
thread - knowing (or thinking I know) CLC and those who have posted comments so 
far.

I would HOPE (but also doubt this) that those who want to discuss "philosophy" 
"truth" "word origins" etc within the CLC newsgroup, would add "OT" to the 
subject line and otherwise indicate in the subject exactly what they are talking 
about - and/or replying to.

As the originator of this thread, I am certain that there are still perceptions, 
impressions, and thoughts  about

    "Shared" procedure division code

that have not yet been recorded, but I certainly don't perceive the current 
thread dealing with it - but that certainly may be just my understanding of the 
points being made.
```

###### ↳ ↳ ↳ [OT] Hitler was Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T21:06:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EPPJe.83204$t43.13354@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com> <BoPJe.959452$pI6.36867@fe06.news.easynews.com>`

```
Perhaps one should have added [OT] to his post  :-)
I think that perhaps shared procedure division code just isn't that 
interesting anymore.

Oh, and on the subject of Hitler....

http://www.faqs.org/faqs/usenet/legends/godwin/

Apparently you couldn't be wronger :-)

JCE

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:BoPJe.959452$pI6.36867@fe06.news.easynews.com...
>I have HEARD (or read) that there is an (unwritten?) rule that when somone 
>(naturally) brings Hitler into a thread in a newsgroup, that it is supposed 
…[25 more quoted lines elided]…
> wmklein <at> ix.netcom.com
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-12T22:06:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-0BF8B2.22065512082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11f4r0kga57eda3@corp.supernews.com> <dcvfct$kpv$1@panix5.panix.com> <11fdiopk2atsqbe@corp.supernews.com> <dd6r12$i7v$1@panix5.panix.com> <BoPJe.959452$pI6.36867@fe06.news.easynews.com>`

```
Bill, if it will help, I have on hand my copy of the excellent Shirer 
work -- The Rise and Fall of the Third Reich.

He clearly details the Hitlerian opinion of Konrad Zeus and shared code 
decades before Cobol or procedure divisions were invented.

I hope this will kill the thread...

Top Post Only

In article <BoPJe.959452$pI6.36867@fe06.news.easynews.com>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> I have HEARD (or read) that there is an (unwritten?) rule that when somone 
> (naturally) brings Hitler into a thread in a newsgroup, that it is supposed 
…[28 more quoted lines elided]…
> points being made.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-13T08:55:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddkqj9$gdm$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd6r12$i7v$1@panix5.panix.com> <BoPJe.959452$pI6.36867@fe06.news.easynews.com> <joe_zitzelberger-0BF8B2.22065512082005@ispnews.usenetserver.com>`

```
In article <joe_zitzelberger-0BF8B2.22065512082005@ispnews.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>Bill, if it will help, I have on hand my copy of the excellent Shirer 
>work -- The Rise and Fall of the Third Reich.
…[4 more quoted lines elided]…
>I hope this will kill the thread...

Thanks much for... sharing this procedure.

>
>Top Post Only

Likewise... all right, move along, show's over, g'wan home, nothin' more 
t' see here, move along, let's go...

DD

>
>In article <BoPJe.959452$pI6.36867@fe06.news.easynews.com>,
…[32 more quoted lines elided]…
>> points being made.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T14:40:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco0l7$60r$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com>`

```

On  1-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> From "That's a stupid practice?"  Oh, yes, it is, by the rules of English.
> Saying "That's a stupid practice" to someone or some group is hugely
> different in a number of ways from saying "I think that's a stupid practice"
> to that person.   The former is an assertion of absolute fact; the latter is
> a clear expression of opinion.

True - but unless we have footnotes and references supporting what we say -
*everything* we post is opinion.

There is no *real* difference between those two statements, but one comes across
as a bit less rude.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T11:17:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco2qp$dgq$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu>`

```
In article <dco0l7$60r$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
…[8 more quoted lines elided]…
>*everything* we post is opinion.

Is that a fact?  Plural majestatus est, Mr Brazee... and I believe that 
statements like 'Bismarck is the capital of North Dakota' and 'in base ten 
five times five is twenty-five' belong to the set of 'everything'.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T15:45:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco4eq$7tn$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> >True - but unless we have footnotes and references supporting what we say -
> >*everything* we post is opinion.
…[3 more quoted lines elided]…
> five times five is twenty-five' belong to the set of 'everything'.

I believe you believe this.


If you added "I believe" to the above, it wouldn't have changed its validity one
iota.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T12:26:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco6r9$3hl$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <dco4eq$7tn$1@peabody.colorado.edu>`

```
In article <dco4eq$7tn$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
>I believe you believe this.

Do you believe that... or do you just believe that you believe that?

> 
> 
>If you added "I believe" to the above, it wouldn't have changed its validity one 
>iota.

I do not understand what you are calling 'validity' or how it can be 
applied differently to opinions.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T16:52:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco8co$a29$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> >If you added "I believe" to the above, it wouldn't have changed its validity
> >one
…[3 more quoted lines elided]…
> applied differently to opinions.


Except for trolls - what a poster post is what he believes.   It may be
something that can be checked easily (the capital of North Dakota), or one which
is harder to quantify "that process is stupid".

Occasionally, adding a confidence factor is meaningful.   "If things haven't
changed, the company I worked for 5 years ago still uses CoBOL".

But I can say:

"I believe Bismark is the capital of North Dakota"
or
"I believe the "C" is the capital of Colorado".
or
"I believe CoBOL is a dead language"
or
"I believe GO TO is harmful".
or
"I believe Connecticut is the capital of North Dakota".


But my "I believe" didn't really add anything.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T13:12:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dco9h7$ci4$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu>`

```
In article <dco8co$a29$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>Except for trolls - what a poster post is what he believes.

Leaving aside that I barely know what *I* believe, let alone anyone 
else... assuming this to be true it begs the question: believes to be 
belief or believes to be fact?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T17:51:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcobr4$bu0$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> Leaving aside that I barely know what *I* believe, let alone anyone
> else... assuming this to be true it begs the question: believes to be
> belief or believes to be fact?

Are you using the common definition of "begs the question" or the classical one?


But "belief" isn't about whether something is objectively determinable to be
fact.   If you perceive things to be one way, then that's what you believe.

If you tell me you're hungry, or you tell me you believe you're hungry - you can
be lying or you can be telling the truth.

I believe Pluto orbits around the sun.

Belief doesn't have to be without compelling evidence.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T14:34:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcoec5$hsl$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu>`

```
In article <dcobr4$bu0$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[6 more quoted lines elided]…
>classical one?

Answering a question with a question is no answer at all.

>
>
>But "belief" isn't about whether something is objectively determinable to be
>fact.   If you perceive things to be one way, then that's what you believe.

'Belief' is one of those funny, murky yet commonly-used words - like 
'know' or 'understand' - that, every so often, it might be good to dust 
off and re-examine.  I alluded to Wittgenstein earlier with a mathematical 
reference; he asked something along the lines of:

'What is the function of 'belief' in the following exchange:

'What's five times five?'

'Twenty-five... I believe.'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T19:03:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcog1h$e84$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> >> Leaving aside that I barely know what *I* believe, let alone anyone
> >> else... assuming this to be true it begs the question: believes to be
…[5 more quoted lines elided]…
> Answering a question with a question is no answer at all.

It can be, but in this case it wasn't meant to be an answer.  It was meant to be
a question.   And your statement of fact did not answer my question at all.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T19:33:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcovt5$arh$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <dcog1h$e84$1@peabody.colorado.edu>`

```
In article <dcog1h$e84$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>It can be, but in this case it wasn't meant to be an answer.

'Meaning' is the result of interpretation, as Wittgenstein had it.

>It was meant to be
>a question.

As it was something done 'to speak or write in reply' it is, by 
definition, answering.

>And your statement of fact did not answer my question at all.

That is because you left the FIFO answer-queue filled with my question, 
having provided no answer at all.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-05T13:35:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HWJIe.158898$HI.67263@edtnps84>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <dcog1h$e84$1@peabody.colorado.edu> <dcovt5$arh$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcovt5$arh$1@panix5.panix.com...
> That is because you left the FIFO answer-queue filled with my question,
> having provided no answer at all.

For most of the question/answer sessions I've participated it, I believe 
they tend to work better as LIFO stacks; e.g.:

Person A: How do I set the wallpaper on my desktop?
Person B: Are you using Windows?

If this were FIFO, it'd probably result in deadlock, with Person A waiting 
for the answer from person B and person B waiting for the answer from Person 
A. This problem goes away if it's LIFO;

Person A: Yes.
Person B: Try right clicking on your desktop and choosing "Properties".

The main weakness I can think of as implementing a question/answer session 
as a LIFO stack is that it's suceptible to "Denial of Service" attacks, 
though it's possible to detect and try to handle those situations:

Person A: How do I set the wallpaper for my desktop?
Person B: What's the weather like outside?
Person A: A bit of overcast.
Person B: How are you kids doing?
Person A: Fine, thank you.
Person B: Do you like tennis?
Person A: Hey, answer my question!
Person B: Oh sorry, what was the question again?
Person A: How do I set the wallpaper for my desktop?
Person B: Are you using Windows?
...

    - Oliver
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T12:14:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd03a2$5bt$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcog1h$e84$1@peabody.colorado.edu> <dcovt5$arh$1@panix5.panix.com> <HWJIe.158898$HI.67263@edtnps84>`

```
In article <HWJIe.158898$HI.67263@edtnps84>,
Oliver Wong <owong@castortech.com> wrote:
><docdwarf@panix.com> wrote in message news:dcovt5$arh$1@panix5.panix.com...
>> That is because you left the FIFO answer-queue filled with my question,
…[6 more quoted lines elided]…
>Person B: Are you using Windows?

Ummmm... with all due respect, Mr Wong, you speak of 'question/answer 
sessions' and then post an example of a question/question session... and 
aswering a question with a question is, of course, no answer at all.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-05T17:38:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cuNIe.158926$HI.90607@edtnps84>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcog1h$e84$1@peabody.colorado.edu> <dcovt5$arh$1@panix5.panix.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd03a2$5bt$1@panix5.panix.com...
> In article <HWJIe.158898$HI.67263@edtnps84>,
> Oliver Wong <owong@castortech.com> wrote:
…[8 more quoted lines elided]…
> sessions' and then post an example of a question/question session...

You actually didn't quote the full text of the example I gave. Here it is 
again, with some of the comments I made in the middle omitted:

Person A: How do I set the wallpaper on my desktop?
Person B: Are you using Windows?
Person A: Yes.
Person B: Try right clicking on your desktop and choosing "Properties".

The "/" operator in "question/answer" was supposed to mean "and/or", as in 
the "inclusive or" operator, meaning that the participants in the session 
were free to send questions or answers or both.

The point I was trying to make is that if all the participants are willing 
to answer questions when provided enough information, then a question/answer 
sessions which behaves as a LIFO stack is more robust than one which behaves 
as a FIFO queue.

    - Oliver
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T13:59:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd09eg$pa5$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com> <cuNIe.158926$HI.90607@edtnps84>`

```
In article <cuNIe.158926$HI.90607@edtnps84>,
Oliver Wong <owong@castortech.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dd03a2$5bt$1@panix5.panix.com...
…[18 more quoted lines elided]…
>Person B: Try right clicking on your desktop and choosing "Properties".

You prove my point, Mr Wong; the queue continues to fill until there is a 
question that is answered (A's second response).  Consider:

A: How do I set the wallpaper on my desktop?
B: Are you using Windows?
A: Does it make a difference?
B: Do you think it is the same for all operating systems?
A: What do I know about operating systems?
B: Are they all the same to you?
A: How should I know what makes a difference?
B: If you don't know what makes a difference how do you know that setting 
the wallpaper will make a difference?

... etc.

>
>The "/" operator in "question/answer" was supposed to mean "and/or", as in 
>the "inclusive or" operator, meaning that the participants in the session 
>were free to send questions or answers or both.

Meaning, as Wittgenstein has it, is the result of interpretation; thank 
you for supplying Author's Intent.

>
>The point I was trying to make is that if all the participants are willing 
>to answer questions when provided enough information, then a question/answer 
>sessions which behaves as a LIFO stack is more robust than one which behaves 
>as a FIFO queue.

As shown above, Mr Wong, the behavior of the session seems dependent on 
the participants' inputs; once a participant stops answering a question 
with a question - which, of course, is no answer at all - the stack might 
clear more readily.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-05T18:46:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3uOIe.158935$HI.17704@edtnps84>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com> <cuNIe.158926$HI.90607@edtnps84> <dd09eg$pa5$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd09eg$pa5$1@panix5.panix.com...
> In article <cuNIe.158926$HI.90607@edtnps84>,
> Oliver Wong <owong@castortech.com> wrote:
…[24 more quoted lines elided]…
> question that is answered (A's second response).  Consider:

    I wasn't arguing with the assumption that at least one answer must exist 
in a question/answer session. What I was arguing with is your assumption 
that it should behave like a FIFO queue. As you can see, the answers are 
actually given in the reverse order compared to the questions asked, which 
shows the LIFO stack like nature of question/answer sessions. If we were to 
follow a FIFO model, that dialog might look like:

>>Person A: How do I set the wallpaper on my desktop?
>>Person B: Are you using Windows?
>>Person B: Try right clicking on your desktop and choosing "Properties".
>>Person A: Yes.

    Which is very unusual from my experiences.

> A: How do I set the wallpaper on my desktop?
> B: Are you using Windows?
…[8 more quoted lines elided]…
> ... etc.

    This goes into the "denial of service" attack which I've also addressed 
in my earlier post, which I'll repeat here for your benefit (with slight 
modification of the ending because it's being posted in a different 
context).

The main weakness I can think of as implementing a question/answer session
as a LIFO stack is that it's suceptible to "Denial of Service" attacks,
though it's possible to detect and try to handle those situations:

Person A: How do I set the wallpaper for my desktop?
Person B: What's the weather like outside?
Person A: A bit of overcast.
Person B: How are you kids doing?
Person A: Fine, thank you.
Person B: Do you like tennis?
Person A: Hey, answer my question!
Person B: Oh sorry, what was the question again?
Person A: How do I set the wallpaper for my desktop?
Person B: Are you using Windows?
Person A: Yes.
Person B: Try right clicking on your desktop and choosing "Properties".

> As shown above, Mr Wong, the behavior of the session seems dependent on
> the participants' inputs; once a participant stops answering a question
> with a question - which, of course, is no answer at all - the stack might
> clear more readily.

    I agree with "the behavior of the session seems dependent on the 
participants' inputs" and with "once a participant sends a message which is 
an answer (as opposed to a question) the stack might clear more readily." 
(the latter of which is a slightly reworded version of what you said). I 
merely disagree with the statement you made in an earlier post, in which you 
refer to answer-queues (what I call question/answer sessions) as being FIFO 
queues.

    I also disagree with the idea that answering a question with a question 
is "of course", no answer at all, but that may be due to differing 
interpretations of certain words like "is" (which I interpret to mean 
equivalence in the above usage).

    - Oliver
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T15:08:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd0der$afg$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <cuNIe.158926$HI.90607@edtnps84> <dd09eg$pa5$1@panix5.panix.com> <3uOIe.158935$HI.17704@edtnps84>`

```
In article <3uOIe.158935$HI.17704@edtnps84>,
Oliver Wong <owong@castortech.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dd09eg$pa5$1@panix5.panix.com...
…[30 more quoted lines elided]…
>that it should behave like a FIFO queue.

I don't recall stating what it should behave like, Mr Wong; I believe I 
stated what, in this instance, it appeared to behave like.

>As you can see, the answers are 
>actually given in the reverse order compared to the questions asked, which 
…[8 more quoted lines elided]…
>    Which is very unusual from my experiences.

Good of you to generate an example unusual to you... but perhaps I was 
unclear.  First question in is first question out when it is answered; 
since answering a question with a question is no answer at all Person B 
did not empty the queue with the response 'Are you using Windows?'.

>
>> A: How do I set the wallpaper on my desktop?
…[14 more quoted lines elided]…
>context).

How very generous of you.

>
>The main weakness I can think of as implementing a question/answer session
…[4 more quoted lines elided]…
>Person B: What's the weather like outside?

Hmmmmm... granted that B has responded with a question; in this case the 
question does not appear to follow logically from what was previously said 
it is not only non-answer (in that it is a question) it is non-sequitur.

>Person A: A bit of overcast.
>Person B: How are you kids doing?
>Person A: Fine, thank you.
>Person B: Do you like tennis?

See above about the appearance of following logically.

>Person A: Hey, answer my question!
>Person B: Oh sorry, what was the question again?
…[16 more quoted lines elided]…
>queues.

As stated previously... in the case it appeared to behave as FIFO.

>
>    I also disagree with the idea that answering a question with a question 
>is "of course", no answer at all, but that may be due to differing 
>interpretations of certain words like "is" (which I interpret to mean 
>equivalence in the above usage).

That, too, has been addressed in other postings... a search of this 
newsgroup for "question with a question" +avoid/evade might turn up a few 
results.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-05T17:42:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a767b$42f3eb60$45491c57$14973@KNOLOGY.NET>`
- **In-Reply-To:** `<dd03a2$5bt$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcog1h$e84$1@peabody.colorado.edu> <dcovt5$arh$1@panix5.panix.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <HWJIe.158898$HI.67263@edtnps84>,
> Oliver Wong <owong@castortech.com> wrote:
…[15 more quoted lines elided]…
> aswering a question with a question is, of course, no answer at all.

So, you believe that Mr. Wong's full example (of which the first part is 
shown above, but I've reposted below) does not represent reasoned discourse?

[quote]
Person A: How do I set the wallpaper on my desktop?
Person B: Are you using Windows?
Person A: Yes.
Person B: Try right clicking on your desktop and choosing "Properties".
[/quote]

To me, that's a whole lot *more* reasoned than the following...

[more reasoned?]
Person A: How do I set the wallpaper on my desktop?
Person B: Are you using Windows?
Person A: Just answer the question!
Person B: How can I answer the question until you clarify?
Person A: There you go again!  That's *doubly* not an answer at all!
[/more reasoned?]

Or, when asking for directions...

[scene 1]
A: How do I get to your house?
Me: Do you know where Congressman Dickinson Blvd is?
A: No.
Me: Okay - are you coming from downtown or Wetumpka?
A: I'll be coming from downtown.
Me: Okay - turn left off Madison onto Federal Drive - that turns into 
Dickinson when you pass the Hardee's.  Then, after you go past Alabama 
Power, you'll see the base on the right.  Come in by the blue sign, and 
tell the guard you're here to visit me.
[/scene 1]

...or, is this more reasoned?

[scene 2]
A: How do I get to your house?
Me: Come on base, and they'll call me up to the gate to get you.
A: Well, where is the base?  I don't know how to get there.
Me: It's off Congressman Dickinson, on the left.
A: Where's Congressman Dickinson?
Me: It's off the Wetumpka Highway - when 231 turns left, just go straight.
A: But I'm not coming from Wetumpka - I work downtown!
Me: Well, then turn on Federal.
A: Okay - and then you're on the left?
Me: Oh no; then, it's on the right.
[/scene 2]

I've really, really tried not to get involved in these types of 
discussions, but I truly don't see how Mr. Wong's example and my first 
example are less reasoned than my second examples.  In both his and my 
first scenarios, the second person shows a willingness to impart valid 
information, realizing that without further clarification, the 
information may be just flat wrong (turn left vs. turn right in scene 2, 
for example).  In Mr. Wong's example, if the person is a Mac or Linux 
user, they might get downright pissy if he assumed that they were using 
Windows - his clarification actually avoided potential offense!

Or should that have gone something like this...

[scene 3]
A: How do I get to your house?
Me: I cannot tell you how to get to my house until I ascertain your 
knowledge of Montgomery's streets, as well as the direction from which 
you'll be coming.
A: Well, I'll be coming from downtown, but I'm not really familiar with 
your part of town.
Me: From downtown, make a right turn off Congressman Dickinson Blvd into 
the base, at the blue sign.
A: I cannot come to your house because I do not know where Congressman 
Dickinson Blvd is.
Me: Turn on Coliseum Blvd off the Northern Bypass, then turn left at the 
Hardee's.
A: But I'm not coming from the Northern Bypass, I'm coming up Madison.
Me: Then turn left on Federal Drive, which turns into Dickinson when you 
pass the Hardee's.
[/scene 3]

Maybe some folks have the time for that, but scene 1 is lot closer to 
reality.  And I still bet that "A" isn't offended, and will still come 
see me!  :)
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T20:39:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd10so$pvo$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET>`

```
In article <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <HWJIe.158898$HI.67263@edtnps84>,
…[19 more quoted lines elided]…
>shown above, but I've reposted below) does not represent reasoned discourse?

I believe that it indicates answering a question with a question, hence my 
response.

The reasons I give for attempting to avoid such a construct have been 
given again and again... do you need me to repost the URLs?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-05T20:50:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1871$42f4177f$45491c57$5646@KNOLOGY.NET>`
- **In-Reply-To:** `<dd10so$pvo$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET>,
> LX-i  <lxi0007@netscape.net> wrote:
…[32 more quoted lines elided]…
> given again and again... do you need me to repost the URLs?

No - I'm just, like Mr. Brazee, having a hard time believing that you're 
completely serious about this.  It's not necessarily "answering" a 
question with a question, as the question is *not* meant to delay, 
obfuscate, or change the subject.  (1 - "What do you think?"  2 - "Well, 
what do *you* think?" - it's not that sort of thing)

I thought you only did that with me, but I've seen you reply to nearly 
every other person in this discussion with you "not an answer at all" 
cookie-cutter response.  This, to me, seems to be hampering reasoned 
discourse *much* more than their attempts at clarification - and, as the 
discussion has shifted from shared procedure division code to your 
debating techniques, you've changed the subject - one of the things you 
claim your "reasoned discourse" avoids!

I don't know if I've got this word for word, but there's a saying that 
lawyers have that goes something like...
   - If the law is on your side, pound on the law.
   - If the facts are on your side, pound on the facts.
   - If neither is on your side, pound on the table.

Your refusal to continue discourse when asked to clarify questions *you* 
posited in the course of said discussion seems to be little more than 
pounding on the table.  Just as you take great pride in saying that you 
barely know what you know, much less anyone else, your refusal to 
clarify anything you've said in the form of a question deprives others 
from determining just what the point is that you're trying to get 
across.  We scarcely know what we know, much less what you do!  :)

To me, the point seems to be "don't question the Doc."
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-06T09:29:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd2e0j$1qn$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com> <c1871$42f4177f$45491c57$5646@KNOLOGY.NET>`

```
In article <c1871$42f4177f$45491c57$5646@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET>,
…[36 more quoted lines elided]…
>completely serious about this.

That might make it a bit more difficult to categorise, then, and require a 
bit more thought on the matter... how horrid!

>It's not necessarily "answering" a 
>question with a question, as the question is *not* meant to delay, 
>obfuscate, or change the subject.

As Wittgenstein has it, meaning is the result of interpretation... 'I 
cannot know what you mean, only what you say.'  What is said is answering 
a question with a question.

>(1 - "What do you think?"  2 - "Well, 
>what do *you* think?" - it's not that sort of thing)

Do tell... how is one to know this?

>
>I thought you only did that with me, but I've seen you reply to nearly 
>every other person in this discussion with you "not an answer at all" 
>cookie-cutter response.

What, you think you're special?  I do my best to treat folks equally... 
I'll admit to admixing a bit more gentility and tenderness when dealing 
with what used to be called 'the handicapped'... but I haven't seen too 
many of those posting here.

>This, to me, seems to be hampering reasoned 
>discourse *much* more than their attempts at clarification - and, as the 
>discussion has shifted from shared procedure division code to your 
>debating techniques, you've changed the subject - one of the things you 
>claim your "reasoned discourse" avoids!

My memory is, admittedly, porous... but I do not recall stating that 
avoiding answering a question with a question will prevent UseNet thread 
drift.

>
>I don't know if I've got this word for word, but there's a saying that 
…[7 more quoted lines elided]…
>pounding on the table.

How interesting that you see it this way.  I see it that not answering 
questions is the 'refusal to continue discourse', you see that my pointing 
this out is the refusal.  This seems, to me, like believing that a 
program's throwing a non-numeric divide error is the fault of the user 
entering bad data, not the coder's lack of numeric testing.

>Just as you take great pride in saying that you 
>barely know what you know, much less anyone else, your refusal to 
>clarify anything you've said in the form of a question deprives others 
>from determining just what the point is that you're trying to get 
>across.

I do not 'take great pride' in this, I state it as a matter of fact when I 
am asked to posit the thinking or knowledge of others.  I do not know what 
you are trying to say when you refer to my 'refusal to clarify anything 
(I've) said in the form of a question'... when asked a question I do my 
best to supply an answer, when I ask of others it would be nice were they 
to do the same.

>We scarcely know what we know, much less what you do!  :)
>
>To me, the point seems to be "don't question the Doc."

This appears a rather... curious interpretation of 'answering a question 
with a question is no answer at all'.

'This person, upon seeing a question responded-to with another question, 
points out that 'answering a question with a question is no answer at 
all'... the point of this seems to be 'don't question him'.'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-07T21:07:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET>`
- **In-Reply-To:** `<dd2e0j$1qn$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com> <c1871$42f4177f$45491c57$5646@KNOLOGY.NET> <dd2e0j$1qn$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <c1871$42f4177f$45491c57$5646@KNOLOGY.NET>,
> LX-i  <lxi0007@netscape.net> wrote:
…[48 more quoted lines elided]…
> bit more thought on the matter... how horrid!

Well, if you are serious, you don't want to know the thoughts I'm 
having.  It doesn't require any more - I've already had them.

>>It's not necessarily "answering" a 
>>question with a question, as the question is *not* meant to delay, 
…[4 more quoted lines elided]…
> a question with a question.

And as you've repeated (in this thread, no less), that nothing is 
absolute.  Yet, you treat any response ending in a question mark to an 
original question as a stalling tactic.  You've said yourself that you 
find that that's what people *usually* do, but you treat it as if that's 
what people are *always* trying to do.

>>(1 - "What do you think?"  2 - "Well, 
>>what do *you* think?" - it's not that sort of thing)
> 
> Do tell... how is one to know this?

How is one to know it *is* that?  (for those keeping score at home, yes, 
that's a question in response to a question)  You *assume* that any 
question as a response is an attempt to delay.

>>I don't know if I've got this word for word, but there's a saying that 
>>lawyers have that goes something like...
…[12 more quoted lines elided]…
> entering bad data, not the coder's lack of numeric testing.

You refuse to attribute even a smidgen of pure motives to those with 
whom you are discussing.  To some observers (and as has been evidenced 
in this thread, it's not just me), it looks like *you* don't want to 
answer the question.  Rather than clarify your statement (which would 
require to answering a question posed as a response to a question with a 
real answer, instead of the auto-responder), you trot out your standard 
reply.

There's no really good way to take it, either.  If you're trying to 
delay, you get miffed that you were called on it.  If you just wanted 
clarification, it comes across as either *you* trying to delay; or an 
attempt to claim some sort of high ground based on technique; or just 
flat condescending.  In all but the first, it hampers the discourse, not 
enhances it.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T02:08:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd6stj$nit$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <c1871$42f4177f$45491c57$5646@KNOLOGY.NET> <dd2e0j$1qn$1@panix5.panix.com> <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET>`

```
In article <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <c1871$42f4177f$45491c57$5646@KNOLOGY.NET>,
>> LX-i  <lxi0007@netscape.net> wrote:

[snip]

>>>No - I'm just, like Mr. Brazee, having a hard time believing that you're 
>>>completely serious about this.
…[6 more quoted lines elided]…
>having.  It doesn't require any more - I've already had them.

Then it might be wise to question your beliefs a bit more, to see if any 
thoughts of value arise.

>
>>>It's not necessarily "answering" a 
…[8 more quoted lines elided]…
>absolute.

I do not recall making such a statement and I would be very interested to 
see a quoting of my writing in which I assert such.  Mr Dashwood is, as I 
recall, the one who has asserted an absolute belief that there are no 
absolute facts.

>>Yet, you treat any response ending in a question mark to an 
>original question as a stalling tactic.  You've said yourself that you 
>find that that's what people *usually* do, but you treat it as if that's 
>what people are *always* trying to do.

Once again, I would be interested your supplying a quotation which 
supports this assertion.  I have posted, I believe, something entirely 
alternate at least three times and URLs to those postings several more 
times... do I need to yet again?  Try searching on the text:

--begin quoted text:

This having been said - that in the overwhelming majority of cases it is
used as an evasion instead of an answer and that there are, as noted
above, structures readily available to render its use unnecessary - then
the conclusion is that the technique of answering a question with a
question is treated as an ALTER and should be structured out of
existence. 

--end quoted text

... and see if you can find statement where, clearly and unambiguously, I 
draw attention to the fact that I refer to 'an overwhelming majority' and 
not 'all'.

>
>>>(1 - "What do you think?"  2 - "Well, 
…[6 more quoted lines elided]…
>question as a response is an attempt to delay.

That has been addressed in the quotations and URLs given repeatedly, as 
mentioned above.  Now, please be so kind as to answer my question of 'Do 
tell... how is one to know this?' ('this' referring to 'it's not that sort 
of thing')

>>>I don't know if I've got this word for word, but there's a saying that 
>>>lawyers have that goes something like...
…[15 more quoted lines elided]…
>whom you are discussing.

If that were the case I might be loth to resume discourse once the form of 
answering a question with a question has been changed... and this is not, 
in my experience, the case.

>To some observers (and as has been evidenced 
>in this thread, it's not just me), it looks like *you* don't want to 
>answer the question.

I cannot be held responsible for their interpretations... as noted above, 
once a non-answer is changed to an answer things can continue along on 
their merry way.

>Rather than clarify your statement (which would 
>require to answering a question posed as a response to a question with a 
>real answer, instead of the auto-responder), you trot out your standard 
>reply.

There's a reason for my doing that... and it has been posted and reposted, 
repeatedly, to the point where at least one reader has reconsidered his 
behavior in light of it.  Have you read it, perchance?

>
>There's no really good way to take it, either.  If you're trying to 
…[4 more quoted lines elided]…
>enhances it.

The first few times, being a non-standard response, there might be a bit 
of stumbling... or for pettifogging, niggling, legalistic sticklers there 
might be a bit of a delay - 'Well, what about if it is Tuesday in Estonia 
and the local scissors-grinder has just celebrated his daughter's 
betrothal to the brewer's left-handed middle son... might not *then* be a 
time when answering a question with a question is, truly, an answer? - 
(the answer, of course, is 'no')... but I have found that with a bit of 
time it facilitates things.

This is, of course, only my experience.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-09T01:51:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lp6apF13loqhU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <c1871$42f4177f$45491c57$5646@KNOLOGY.NET> <dd2e0j$1qn$1@panix5.panix.com> <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET> <dd6stj$nit$1@panix5.panix.com>`

```
 
Gross misrepresentation corrected below...

<docdwarf@panix.com> wrote in message news:dd6stj$nit$1@panix5.panix.com...
>
> I do not recall making such a statement and I would be very interested to
> see a quoting of my writing in which I assert such.  Mr Dashwood is, as I
> recall, the one who has asserted an absolute belief that there are no
> absolute facts.

I asserted no such thing and this is just a deliberate misrepresentation of 
what I DID assert. Qualifying it with 'as I recall' and then admitting later 
to a 'porous memory' does not disguise the mischievous intention behind it. 
Before  assigning assertions to people, a simple search of the thread would 
reveal how incorrect this is.

For the last time...

I DO believe there are no "absolute facts".

I do NOT , and have never asserted, that belief to be ABSOLUTE.

My position is therefore non contradictory and follows logically, unlike the 
tautological representation of it above.

[Here are a series of quotes from a number of posts in this thread, which 
show I have NEVER considered this belief to be absolute, despite the Doc 
consistently representing that I do...]
----------------------------- quote 1 ------------------------------------
DASHWOOD:
This is where we come back to "absolute fact".  Is our individual perception
of reality simply belief or is it fact? (I believe facts are what we agree
to be true; but I don't believe they are absolute.) Can there be anything
outside of our perception that is a fact? Is  "absolute fact"  simply tiny
strings of energy oscillating in different ways through eleven dimensions,
understandable by us as being subject to the laws of probability, but not
necessarily so? Maybe. Can our perception change this reality? Maybe.
Indications are that observing experiments may change the outcome of them.

Has anybody seen the film "What the bleep do we know?". I found it enjoyable
but irritating in places because people who should know better were not
telling the whole story or were putting their own spin it. But that's
reality. It is all about getting agreement on what each of us perceive.

When I post to this forum you are getting a glimpse of my universe. When you
post, I am getting a glimpse of yours. If our perceptions tally, we are in
agreement and share a reality; if they don't, then we get irritated with
each other... :-) But none of it has anything to do with "absolute fact".
------------------------------ end quote 1 ---------------------------------

------------------------------start quote 
2 ---------------------------------
DASHWOOD:
The bottom line is that observing things in this universe may well change 
the
way they behave. Nobody knows what energy and particles are doing when they
are not observed, and when they ARE observed they behave in a way that is
logically inconsistent [like being in two places at once, or being
simultaneously a wave and a particle, and a whole lot of  other weird
shit...).  Our Common Sense gives us the same view as Newton's idea of God
winding up the clock and letting it tick at a standard rate throughout the
Cosmos. An "absolute" background of space and time on which events happen.
Where "absolute facts" are a reality.

I don't ascribe to it, and anyone who has dabbled in modern Physics is
unlikely to, either. The universe confounds our common sense and is far more
complex than our three dimensional brains can easily perceive. Space and
time vary with relative location and acceleration; there is no "absolute
fabric" for "absolute facts" to be painted on.
------------------------------ end quote 2 ---------------------------------

------------------------------start quote 3---------------------------------
DWARF:
> 'There are no "absolute facts" is absolutely true'... how many variations
> of this are you going to offer, Mr Dashwood?
>
DASHWOOD:
I have offered NO variations on it because I never said it. It is YOUR
quote, repeated to the point of being tiresome.

In my universe there are no absolutes, only probabilities. I have been clear
on that on every occasion.
------------------------------ end quote 3 ---------------------------------

------------------------------start quote 4---------------------------------
DWARF:
> Once again this curious 'we'... I ask you to speak for yourself, Mr
> Dashwood: in the universe *you* inhabit is 'NOTHING is absolute'
> absolutely true?
>
DASHWOOD:
It is of an extremely high probability... close to, but not touching,
certainty. Get over it.
------------------------------ end quote 4 ---------------------------------

Pete.
<snip>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T10:19:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7pkk$ihe$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET> <dd6stj$nit$1@panix5.panix.com> <3lp6apF13loqhU1@individual.net>`

```
In article <3lp6apF13loqhU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>Gross misrepresentation corrected below...
…[9 more quoted lines elided]…
>what I DID assert.

Mr Dashwood, according to 
<http://groups-beta.google.com/group/comp.lang.cobol/msg/b181d45236e25b10?dmode=source&hl=en> 
you state, without restriction, exception or qualification:

--begin quoted text:

In my universe there are no absolutes, only probabilities.

--end quoted text

So... in this universe of yours either there are absolutes or not.

In that you state 'there are no' then if even one absolute exists your 
assertion is incorrect.

If there are no absolutes then your universe has an absolute freedom from 
absolutes... and an absolute exists and your assertion is incorrect.

I hope that makes clear at least one difficulty I seem to be having with 
what is being presented here as logic... now pardon me whilst I adjust my 
logical foundation garments, my Goedel is killing me.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T07:55:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7rpi$1d6e$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET> <dd6stj$nit$1@panix5.panix.com> <3lp6apF13loqhU1@individual.net> <dd7pkk$ihe$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd7pkk$ihe$1@panix5.panix.com...

> I hope that makes clear at least one difficulty I seem to be having with
> what is being presented here as logic... now pardon me whilst I adjust my
> logical foundation garments, my Goedel is killing me.

I trust you haven't injured your Bach in the process ...     ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T11:44:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7uli$s15$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lp6apF13loqhU1@individual.net> <dd7pkk$ihe$1@panix5.panix.com> <dd7rpi$1d6e$1@si05.rsvl.unisys.com>`

```
In article <dd7rpi$1d6e$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dd7pkk$ihe$1@panix5.panix.com...
…[5 more quoted lines elided]…
>I trust you haven't injured your Bach in the process ...     ;-)

Not so much that I cannot go up and down stairs at the same time, Mr 
Stevens.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T14:55:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1oKJe.85771$mC.65879@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <8f14c$42f6be5f$45491c57$28129@KNOLOGY.NET> <dd6stj$nit$1@panix5.panix.com> <3lp6apF13loqhU1@individual.net> <dd7pkk$ihe$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd7pkk$ihe$1@panix5.panix.com...
> In article <3lp6apF13loqhU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
snip

> --begin quoted text:
>
…[9 more quoted lines elided]…
> absolutes... and an absolute exists and your assertion is incorrect.

What if there was a probabilistic method to determine the likelihood of 
finding an absolute and that the limits of said equation were 0 and 1?
I believe that all conditions would be satisfied.

> I hope that makes clear at least one difficulty I seem to be having with
> what is being presented here as logic... now pardon me whilst I adjust my
> logical foundation garments, my Goedel is killing me.

I cannot find a commonly accepted source that describes a common basis for 
using the words Goedel in this context.
Neither can I find reference to "logical foundation garments"

http://www.google.com/search?hl=en&lr=&q=%22logical+foundation+garments%22

I'm not sure how I am to make use of the words here.

> DD

Perhaps a relational quantum mechanics approach to text and its 
interpretation would be beneficial at this juncture in clc history.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T12:02:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7vmc$fk7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lp6apF13loqhU1@individual.net> <dd7pkk$ihe$1@panix5.panix.com> <1oKJe.85771$mC.65879@tornado.tampabay.rr.com>`

```
In article <1oKJe.85771$mC.65879@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dd7pkk$ihe$1@panix5.panix.com...
…[19 more quoted lines elided]…
>I believe that all conditions would be satisfied.

I believe I'll worry about that when it happens.

>
>> I hope that makes clear at least one difficulty I seem to be having with
…[9 more quoted lines elided]…
>I'm not sure how I am to make use of the words here.

Goedel is accredited with formulating the Incompleteness Theorems, which 
appear to both apply and not-apply, simultaneously and in regard to the 
same aspect, to Mr Dashwood's logical system.

One of the points of difficulty between Mr Dashwood and me seems to be 
that of definition, a foundation for logic.

'Goedel' is a homonym of 'girdle', which belongs to a class of 
garments referred to, e'er-so-long ago, as 'foundation garments'.  

'My girdle is killing me' was an advertising slogan for such garments a 
few decades back...

... proving, yet again, that a joke explained is a joke lost.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 31)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T16:34:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oQLJe.77314$t43.9487@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lp6apF13loqhU1@individual.net> <dd7pkk$ihe$1@panix5.panix.com> <1oKJe.85771$mC.65879@tornado.tampabay.rr.com> <dd7vmc$fk7$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dd7vmc$fk7$1@panix5.panix.com...
> In article <1oKJe.85771$mC.65879@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[48 more quoted lines elided]…
> garments referred to, e'er-so-long ago, as 'foundation garments'.

> 'My girdle is killing me' was an advertising slogan for such garments a
> few decades back...
For those of old enough to enjoy such advertising I'm sure this was not 
lost.
Proving once again that context is important.

> ... proving, yet again, that a joke explained is a joke lost.
Oh, I'm _so_ sorry.  I thought, not understanding the "joke" that I could 
use commonly accepted sources such as used extensively in this thread to 
determine the meaning.  I didn't anticipate anything to be such a mildly 
amusing quip or play on words.

It was not a joke lost as now in future I will understand that perhaps some 
of your posts are "not entirely serious".

[I did actually find it amusing which I loathe to admit ;-) ]

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T13:36:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8579$gmj$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1oKJe.85771$mC.65879@tornado.tampabay.rr.com> <dd7vmc$fk7$1@panix5.panix.com> <oQLJe.77314$t43.9487@tornado.tampabay.rr.com>`

```
In article <oQLJe.77314$t43.9487@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dd7vmc$fk7$1@panix5.panix.com...
>> In article <1oKJe.85771$mC.65879@tornado.tampabay.rr.com>,
…[3 more quoted lines elided]…
>>>news:dd7pkk$ihe$1@panix5.panix.com...

[snip]

>>>> I hope that makes clear at least one difficulty I seem to be having with
>>>> what is being presented here as logic... now pardon me whilst I adjust 
…[22 more quoted lines elided]…
>lost.

Or for those who, while not paying attention to it during its 
introduction, learned about it through other means... one might not need 
to be as old as Beethoven would be to have familiarity with or enjoyment 
of his music.

>Proving once again that context is important.

Shared experience as a necessary, but not unique, basis for humor... now 
there's yet another possible subject for a dissertation.  How something 
goes from being considered idiosyncratic-to-the-point-of-psychotic to an 
'in reference' to 'moderately esoteric' to 'widely accepted' to 
'*everyone* knows'... then again, sometimes letting academicians write 
about humor causes it to stop partaking of the Form of the Funny.

>
>> ... proving, yet again, that a joke explained is a joke lost.
…[3 more quoted lines elided]…
>amusing quip or play on words.

Some might argue that it didn't exist as a 'done thing' until two-or-more 
folks agreed that it did, as well.

>
>It was not a joke lost as now in future I will understand that perhaps some 
>of your posts are "not entirely serious".

Haw... any less serious and I would be all-too-doggedly Polaris!

(serious is a homonym of Sirius, sometimes referred to as... oh, never 
mind)

>
>[I did actually find it amusing which I loathe to admit ;-) ]

Pfoo... you'se jes' easily amused.  Glad you enjoyed.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T13:58:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7odl$k29$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <HWJIe.158898$HI.67263@edtnps84> <dd03a2$5bt$1@panix5.panix.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com>`

```

On  5-Aug-2005, docdwarf@panix.com wrote:

> I believe that it indicates answering a question with a question, hence my
> response.
>
> The reasons I give for attempting to avoid such a construct have been
> given again and again... do you need me to repost the URLs?

No.

Our responses have been repeated, expanded upon, and illustrated.   But they
aren't as funny as your running gag.

That non-sequitur fails to solve the original need for more information much
more than a request for more information does.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T10:22:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7prf$aj6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com> <dd7odl$k29$1@peabody.colorado.edu>`

```
In article <dd7odl$k29$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  5-Aug-2005, docdwarf@panix.com wrote:
…[13 more quoted lines elided]…
>more than a request for more information does.

Mr Brazee, I do not understand what you are calling a non-sequitur.  In 
that what is previously said before 'answering a question with a question 
is no answer at all' is the answering of a question with a question how 
are you seeing it as not following from what is previously said?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T16:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7vid$nsr$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <a767b$42f3eb60$45491c57$14973@KNOLOGY.NET> <dd10so$pvo$1@panix5.panix.com> <dd7odl$k29$1@peabody.colorado.edu> <dd7prf$aj6$1@panix5.panix.com>`

```

On  8-Aug-2005, docdwarf@panix.com wrote:

> >That non-sequitur fails to solve the original need for more information much
> >more than a request for more information does.
…[4 more quoted lines elided]…
> are you seeing it as not following from what is previously said?


It works if we are discussing language, as it makes a point about how language
is used and contributes to the discussion of questions and answers.

But in more real discussions - such as the example of asking how to set one's
computer resolution, It is takes the discussion away from the original problem.

We are no longer talking about shared procedure division code, nor even what
coding practices are stupid.   If I program the way we are contributing to the
original problem, I should be fired.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T12:11:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8084$7a0$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7odl$k29$1@peabody.colorado.edu> <dd7prf$aj6$1@panix5.panix.com> <dd7vid$nsr$1@peabody.colorado.edu>`

```
In article <dd7vid$nsr$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  8-Aug-2005, docdwarf@panix.com wrote:
…[11 more quoted lines elided]…
>is used and contributes to the discussion of questions and answers.

I disagree, of course; in that the discussion occurs in language and 
occurs, one hopes, towards the answering of questions then it might be 
concluded that indicating what might be an obstacle is appropriate.

>
>But in more real discussions - such as the example of asking how to set one's
>computer resolution, It is takes the discussion away from the original problem.

I do not know what you are calling 'more real discussions', outside of the 
example you give here... but I have seen discussions take the form of:

A: 'What are the suppositions and logic you employed in reaching this 
conclusion?' 

B: 'What suppositions and logic would *you* employ to reach this 
conclusion?' 

A: 'I cannot see *any* set of suppositions and logic which might be 
employed to reach this conclusion, hence my asking you this.' 

B: 'Well don't blame *me* because *you* can't see things... you must be a 
poopie-head, nyah nyah nyah!' 

... and I do my best to avoid them by pointing out that answering a 
question with a question is no answer at all.

>
>We are no longer talking about shared procedure division code, nor even what
>coding practices are stupid.   If I program the way we are contributing to the
>original problem, I should be fired.

Others have noticed a phenomenon called 'thread drift' as well, Mr Brazee.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T16:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd81dv$oue$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7odl$k29$1@peabody.colorado.edu> <dd7prf$aj6$1@panix5.panix.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com>`

```

On  8-Aug-2005, docdwarf@panix.com wrote:

> >It works if we are discussing language, as it makes a point about how
> >language
…[4 more quoted lines elided]…
> concluded that indicating what might be an obstacle is appropriate.

Interesting disagreement to what I said above.   I'm not sure that I quite
follow it though.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T13:38:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd85ba$1pl$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com> <dd81dv$oue$1@peabody.colorado.edu>`

```
In article <dd81dv$oue$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  8-Aug-2005, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>follow it though.

You state that the observation 'works (whatever that is seen to be) if we 
are discussing language'; I attempted to show how the usefulness might be 
extended to discussions of other subjects.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T18:04:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd86rh$roq$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com> <dd81dv$oue$1@peabody.colorado.edu> <dd85ba$1pl$1@panix5.panix.com>`

```

On  8-Aug-2005, docdwarf@panix.com wrote:

> >> >It works if we are discussing language, as it makes a point about how
> >> >language
…[11 more quoted lines elided]…
> extended to discussions of other subjects.

I agree that it can be extended, but didn't see how extensibility is of a form
of disagreement. (with an "of course").

Kind of like saying "CoBOL works for some accounts receivable needs".   "I
disagree of course, it can also be used for accounts payable needs".

Unless the "of course" implies - "I always disagree, even when it looks to all
the world that I am agreeing".
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T14:15:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd87fn$gj1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd81dv$oue$1@peabody.colorado.edu> <dd85ba$1pl$1@panix5.panix.com> <dd86rh$roq$1@peabody.colorado.edu>`

```
In article <dd86rh$roq$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  8-Aug-2005, docdwarf@panix.com wrote:
…[17 more quoted lines elided]…
>of disagreement. (with an "of course").

My error and apologies, Mr Brazee; I took the following sentence (which I 
edited out) of 'But in more real discussions - such as the example of 
asking how to set one's computer resolution, It is takes the discussion 
away from the original problem.' as your way of saying 'it works if we are 
discussing language but in more real discussions it doesn't.'
>
>Kind of like saying "CoBOL works for some accounts receivable needs".   "I
>disagree of course, it can also be used for accounts payable needs".

More like 'COBOL works for some accounts receivable needs but in more real 
environments it doesn't'; my apologies for my lack of precision.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T17:56:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1NJe.85896$mC.11841@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7odl$k29$1@peabody.colorado.edu> <dd7prf$aj6$1@panix5.panix.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com>`

```


<docdwarf@panix.com> wrote in message news:dd8084$7a0$1@panix5.panix.com...
> In article <dd7vid$nsr$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[44 more quoted lines elided]…
> question with a question is no answer at all.

W.H. Auden said that : "History is, strictly speaking, the study of 
questions; the study of answers belongs to anthropology and sociology. "

I guess that you are undertaking the historiography of the history of lack 
of sociology or somesuch...

You ignore the cases where a question is not an answer but a seeking of 
clarification before answering the wrong question.  This could all get 
rather silly.

A: 'Are you gay?'
B: 'Which definition of gay are referring to?'
A:'Answering a question with a question is no answer at all'

What about the following?

A: 'Are you gay?'
B: 'I prefer not to answer unless you clarify which definition of gay are 
referring to'
A:'I'm talking about the "happy, merry" one
B: 'Answering an answer that is not a question is not an answer at all'

I guess we should all be much more explicit.  I don't understand why I don't 
see more of the following:

A:'Can anyone help me here with my COBOL problem, I have to .......'
B: Of course someone can.  Please rephrase your question in the form of a 
request for specific information at which point we will provide a list of 
rates....

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T14:09:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd875f$k45$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com> <g1NJe.85896$mC.11841@tornado.tampabay.rr.com>`

```
In article <g1NJe.85896$mC.11841@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
>
><docdwarf@panix.com> wrote in message news:dd8084$7a0$1@panix5.panix.com...
>> In article <dd7vid$nsr$1@peabody.colorado.edu>,
>> Howard Brazee <howard@brazee.net> wrote:

[snip]

>>>It works if we are discussing language, as it makes a point about how 
>>>language
…[34 more quoted lines elided]…
>of sociology or somesuch...

I'm trying to be more measured and not indulge in such histrionics... but 
some might say that I succeed only in being trying, aye.

>
>You ignore the cases where a question is not an answer but a seeking of 
>clarification before answering the wrong question.

As stated previously:  'Note that I said 'overwhelming majority of cases', 
not 'all'... but I have *never* found a case where the answering question 
could not be phrased in a manner that would turn the dialogue away from 
the seriocomic interchange you posted into something a bit closer to what 
I would call 'rational discourse'.'

>This could all get 
>rather silly.

With a bit of practise a lot of things can, sure.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T18:20:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd87q9$sci$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd7vid$nsr$1@peabody.colorado.edu> <dd8084$7a0$1@panix5.panix.com> <g1NJe.85896$mC.11841@tornado.tampabay.rr.com> <dd875f$k45$1@panix5.panix.com>`

```

On  8-Aug-2005, docdwarf@panix.com wrote:

> As stated previously:  'Note that I said 'overwhelming majority of cases',
> not 'all'... but I have *never* found a case where the answering question
> could not be phrased in a manner that would turn the dialogue away from
> the seriocomic interchange you posted into something a bit closer to what
> I would call 'rational discourse'.'

Obviously switching the conversation into a discussion based upon "answering a
question with a question..." is more fun, even if it is quite a bit further to
what I would call "rational discourse" about the original topic.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T14:46:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd89a2$7n7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <g1NJe.85896$mC.11841@tornado.tampabay.rr.com> <dd875f$k45$1@panix5.panix.com> <dd87q9$sci$1@peabody.colorado.edu>`

```
In article <dd87q9$sci$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  8-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>what I would call "rational discourse" about the original topic.

Obvious is in the mind of the beholder, Mr Brazee... but if others feel 
more comfortable in addressing 'answering a question with a question' or 
in generating 'But what about...' scenaria than they do in examining how 
the matter at hand then it might be best that they are given an easy way 
out.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T19:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcogep$ebu$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> 'Belief' is one of those funny, murky yet commonly-used words - like
> 'know' or 'understand' - that, every so often, it might be good to dust
…[7 more quoted lines elided]…
> 'Twenty-five... I believe.'

It's possible that you are saying that you're not confident of the results.  
But we see many cases where if you accuse a True Believer of not being confident
in his Belief that he will deny it.

Or it could be that the "I believe" adds nothing at all to the content of the
statement.   That does happen.

This sub-thread started with the observation that one should say "I believe this
is stupid" instead of "this is stupid".

What would the function of "I believe" be in that observation?   To indicate (as
in one of my guesses to your question), that his belief isn't strong?    That's
pretty presumptuous.

It seems to me that it might be more of a "if you say anything that might be
deemed insulting, cover your buttocks with extraneous words to blunt your
desired effect".
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T19:37:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp045$oc9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <dcogep$ebu$1@peabody.colorado.edu>`

```
In article <dcogep$ebu$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[17 more quoted lines elided]…
>statement.   That does happen.

Those are starters, Mr Brazee... but one must begin somewhere.

>
>This sub-thread started with the observation that one should say "I believe this
>is stupid" instead of "this is stupid".
>
>What would the function of "I believe" be in that observation?

There might have been no 'the function', there might have been a few... 
one of which would have been to spare me someone else's quoting Davey 
Hume.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T12:11:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lagdmF11gr30U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcoec5$hsl$1@panix5.panix.com...
>
> In article <dcobr4$bu0$1@peabody.colorado.edu>,
…[12 more quoted lines elided]…
>
Maybe not, Doc, but it is a fair way to seek clarification before embarking 
on discussion.

The response could vary here, depending on your answer to the question.

>>
>>But "belief" isn't about whether something is objectively determinable to 
…[3 more quoted lines elided]…
>

That is also my belief. :-)

> 'Belief' is one of those funny, murky yet commonly-used words - like
> 'know' or 'understand' - that, every so often, it might be good to dust
…[8 more quoted lines elided]…
>

Covered in a previous response in this thread.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:28:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp6jc$od9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net>`

```
In article <3lagdmF11gr30U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[17 more quoted lines elided]…
>on discussion.

Mr Dashwood, how is it more 'fair' than responding 'I cannot answer until 
you clarify (x).  If you intend (x1) then a conclusion might be (y1), if 
you intend (x2) then (y3).

Yes, it takes more words than answering a question with a question... but 
just about anything worthwhile takes a bit of effort and avoiding giving 
no answer at all might be worthwhile.

>
>The response could vary here, depending on your answer to the question.

Or the response is one of answering a question with a question, seeking to 
dodge and obfuscate.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-03T05:20:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<juYHe.59920$mC.8865@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcp6jc$od9$1@panix5.panix.com...
> In article <3lagdmF11gr30U1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[20 more quoted lines elided]…
> you intend (x2) then (y3).
Why waste time discussing (y3) if you intended (x1)?

I thought that lazy if evaluation was a "good thing".  One option is to 
discuss the litany of available options with an unclear question.

Imagine the following: "What do you think life is about?"

"Well if you mean <your> life.....but if you mean <my> life....but then if 
you mean <general life> ...."

I suppose the correct answer is here:  "Depends on what you mean, I guess. 
But that's merely my non Unisys bases opinion."

How does taking an interrogative phrase 'do you mean (x is x1) or (x is 
x2)?' and rephrasing it as an declarative phrase 'I cannot answer until you 
clarify if  (x is x1) or (x is x2)' make any difference?  Other than in the 
first there is a request for information to continue, and the latter is just 
a statement and has the potential to end the sorry discussion.

> Yes, it takes more words than answering a question with a question... but
> just about anything worthwhile takes a bit of effort and avoiding giving
> no answer at all might be worthwhile.

>>The response could vary here, depending on your answer to the question.
>
> Or the response is one of answering a question with a question, seeking to
> dodge and obfuscate.
If the question is non specific.  The question was specific - do you mean x1 
or x2?  This is not dodging or obfuscating.  In fact, I would say that this 
would appear to be _seeking_ further conversation - not a dodging.

> DD

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T07:48:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqauo$pj5$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com> <juYHe.59920$mC.8865@tornado.tampabay.rr.com>`

```
In article <juYHe.59920$mC.8865@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dcp6jc$od9$1@panix5.panix.com...
>> In article <3lagdmF11gr30U1@individual.net>,
…[22 more quoted lines elided]…
>Why waste time discussing (y3) if you intended (x1)?

The intention is not apparent, hence the demonstration.

[snip]

>How does taking an interrogative phrase 'do you mean (x is x1) or (x is 
>x2)?' and rephrasing it as an declarative phrase 'I cannot answer until you 
>clarify if  (x is x1) or (x is x2)' make any difference?  Other than in the 
>first there is a request for information to continue, and the latter is just 
>a statement and has the potential to end the sorry discussion.

The reformulation avoids answering a question with a question... which, of 
course, is no answer at all.

>
>> Yes, it takes more words than answering a question with a question... but
…[9 more quoted lines elided]…
>would appear to be _seeking_ further conversation - not a dodging.

What Mr Brazee continued with ('I noticed you did not answer my question') 
appears to me to be more in line with an objection and explanation I 
posted a while back... interestingly enough, also in an exchange with Mr 
Brazee, from

<http://groups-beta.google.com/group/comp.lang.cobol/msg/c5ffed30915f7f6b?dmode=source&hl=en>

--begin quoted text:

It is possible, in my experience, to determine further data without 
answering a question with a question... which is, as noted above, no 
answer at all.  The reasons I use in considering it as such I posted a 
while back... ah:

<http://groups-beta.google.com/group/comp.lang.cobol/msg/967c9d77a4959544?dmode=source&hl=en>

--begin quoted text:

I thought I'd addressed this here but perhaps not, it might have been in 
another venue.

Quite openly and honestly: I find that for the overwhelming majority of 
cases answering a question with a question is a stall, a dodge or some way 
to avoid/evade the original query; the 'air' that it carries is 'I cannot 
answer your question so... I'll ask one of you and if you cannot answer it 
then in some way we'll both be even and our arguments will cancel each 
other out, maybe I can even assume a bit of smug superiority by having 
posed the last, unanswerable question.'

Note that I said 'overwhelming majority of cases', not 'all'... but I have 
*never* found a case where the answering question could not be phrased in 
a manner that would turn the dialogue away from the seriocomic interchange 
you posted into something a bit closer to what I would call 'rational 
discourse'.  Consider the differences between:

'Yeah?  Well, what about (condition)?'
'Whaddaya mean, (condition)?'

... and ...

'Yeah?  Well, what about (condition)?'
'I cannot address that until you make it clear what criteria you are using 
to establish the existence of (condition)?'

Now turning the discord of Duelling Interrogatories into the harmony of 
Rational Discourse might require something called 'honesty' and 
'integrity' as the tactics involve using such phrases as 'I don't know' or 
'I cannot address that' or 'I cannot see the relationship'... but if such 
things are uncomfortable they can, with a bit of practise, be hidden 
without forcing folks to fall back into mutual queries.

This having been said - that in the overwhelming majority of cases it is 
used as an evasion instead of an answer and that there are, as noted 
above, structures readily available to render its use unnecessary - then 
the conclusion is that the technique of answering a question with a 
question is treated as an ALTER and should be structured out of existence.

('Yeah?  What about replacing it with a called Assembley module?' 'I don't 
know what I would say about that without reading the code; if you have it 
available I would be most interested in reading it *first* and *then* 
rendering an opinion... but I *do* know that replacing things in such 
manner usually does not eliminate the structural flaws, it merely shifts 
them.')

--end quoted text

(note - in quoting this I noticed an error in my punctuation, ''I cannot 
address that until you make it clear what criteria you are using to 
establish the existence of (condition)?'' should have been rendered as ''I 
cannot address that until you make it clear what criteria you are using to 
establish the existence of (condition).'')

But wait... there's more!  From even longer back, in another forum:

<http://groups-beta.google.com/group/comp.software.year-2000/msg/34b3233328d534e1?dmode=source&hl=en>

--begin quoted text:

Different folks enjoy, appreciate and benefit from different styles of 
interaction, of course... one size fits none and all that; it is good that 
you enjoy this sort of interaction and find benefit in it.

Me, I've found that not everyone is a rabbi (what a surprise!) and that 
the tactic of answering a question with a question is employed less often 
to teach and more often to dodge... this observation is not, granted, 
universally true (no observation is, of course... including this one) but 
I've found it often enough to be the case.  At times, of course, it can 
get downright infantile:

A: 'What are the suppositions and logic you employed in reaching this 
conclusion?'

B: 'What suppositions and logic would *you* employ to reach this
conclusion?'

A: 'I cannot see *any* set of suppositions and logic which might be 
employed to reach this conclusion, hence my asking you this.'

B: 'Well don't blame *me* because *you* can't see things... you must be a 
poopie-head, nyah nyah nyah!'


... and such a situation, at time, might just possibly be avoided by the 
judicious invoking of 'Answering a question with a question is no answer 
at all; please be so kind as to address the query.'

--end quoted text

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T00:45:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lbsjuF122al4U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com> <juYHe.59920$mC.8865@tornado.tampabay.rr.com> <dcqauo$pj5$1@panix5.panix.com>`

```
 
Hmm...

An excellent exposition and I see your point.

I'm still not persuaded that it is really that serious in debate, but I have 
moved closer to your position after reading this.

(Close enough to make me aware that if I employ this device (and I do so 
rarely...) it will not be to deflect or prevaricate.)

Pete.

TOP POST - nothing more below.

<docdwarf@panix.com> wrote in message news:dcqauo$pj5$1@panix5.panix.com...
>
> In article <juYHe.59920$mC.8865@tornado.tampabay.rr.com>,
…[175 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T09:06:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqfgn$q8a$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <juYHe.59920$mC.8865@tornado.tampabay.rr.com> <dcqauo$pj5$1@panix5.panix.com> <3lbsjuF122al4U1@individual.net>`

```
In article <3lbsjuF122al4U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>Hmm...
>
>An excellent exposition and I see your point.

Shucks... I'd blush, were I able to remember how.

>
>I'm still not persuaded that it is really that serious in debate, but I have 
>moved closer to your position after reading this.

All I hoped to present was something that could be read and generate a 
response of 'I'm not sure I agree... but it seems reasonable enough'; that 
you found it 'moving' is high praise, indeed.

>
>(Close enough to make me aware that if I employ this device (and I do so 
>rarely...) it will not be to deflect or prevaricate.)

E'en better... it might make you more aware of what *others* could be 
doing when *they* employ that device.

>
>Pete.
>
>TOP POST - nothing more below.

All right, show's over, nothin' more to see, move along now.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-03T21:24:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e2fa2$42f17c74$45491c57$30222@KNOLOGY.NET>`
- **In-Reply-To:** `<juYHe.59920$mC.8865@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com> <juYHe.59920$mC.8865@tornado.tampabay.rr.com>`

```
jce wrote:
>>>The response could vary here, depending on your answer to the question.
>>
…[5 more quoted lines elided]…
> would appear to be _seeking_ further conversation - not a dodging.

Ah - but there's the rub.  You *can't* reply to a question with a 
question without it being interpreted as an answer.  So, you answer, 
then are deluged with things that contradict your answer, a lot having 
to do with the differing suppositions upon which they are based.  Then, 
you clarify, and are heartily accused of waffling, backing down, etc.

But hey, it's the CLC way...  (It's also why I rarely express any OT 
opinions in here anymore.)
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T23:35:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lboh5F121qr8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcp6jc$od9$1@panix5.panix.com...
>
> In article <3lagdmF11gr30U1@individual.net>,
…[37 more quoted lines elided]…
>
I agree that that COULD be the case, but I still think far too much is made 
of "answering a question with a question." If the dialogue stopped there, I 
would agree that is bad, but if the dialogue continues, I can't see the 
harm.

To some extent it depends on the person you asked the question of. If the 
respondent has established credentials and you know they can be trusted NOT 
to simply prevaricate or obfuscate, then, (in my opinion, and not wishing to 
offend anybody, and comments may not apply on Unisys sites...) I believe 
there is a case for "cutting them slack". Howard has demonstrated by 
frequent posts here that he is serious about discussion and argument and is 
not likely to use devices to deflect or prevaricate. (Of course that is my 
opinion, and I respect totally your right not to share it; whether you do or 
not, I still feel it is worth looking again at how seriously answering a 
question with a question demeans the quality of debate.)

For me, it isn't such a terrible sin, and it certainly doesn't mean the 
person's argument is "disqualified" or their case is lost.

Pete.
```

###### ↳ ↳ ↳ Begs the question

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T14:14:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqjh3$k9g$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> >>>Are you using the common definition of "begs the question" or the
> >>>classical one?

Since I did continue to answer your question - and this question was just an
aside which you chose not to answer, I thought it might be better off in a
thread of its own, so you cannot construe it as being an attempt to answer a
question with a question.

What do you mean when you say "begs the question"?   My impression of your other
posts would lead to the classical definition, but that didn't seem to fit the
context.
```

###### ↳ ↳ ↳ Re: Begs the question

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T10:49:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqli1$5md$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com> <dcqjh3$k9g$1@peabody.colorado.edu>`

```
In article <dcqjh3$k9g$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
>
>> >>>Are you using the common definition of "begs the question" or the
>> >>>classical one?

This seems a misattribution; I may have posted this question but I believe 
I was quoting it, not originating it.

[snip]

>What do you mean when you say "begs the question"?   My impression of your other
>posts would lead to the classical definition, but that didn't seem to fit the
>context.

In this instance I was using 
http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=begs , 
3b, 'to pass over or ignore by assuming to be established or settled'.

DD
```

###### ↳ ↳ ↳ Re: Begs the question

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T15:01:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqm97$lr5$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lagdmF11gr30U1@individual.net> <dcp6jc$od9$1@panix5.panix.com> <dcqjh3$k9g$1@peabody.colorado.edu> <dcqli1$5md$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> In this instance I was using
> http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=begs ,
> 3b, 'to pass over or ignore by assuming to be established or settled'.

I expect that meaning to wither and die, but it hasn't quite died yet.
```

###### ↳ ↳ ↳ Re: Begs the question

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T11:40:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqoh2$oj7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqjh3$k9g$1@peabody.colorado.edu> <dcqli1$5md$1@panix5.panix.com> <dcqm97$lr5$1@peabody.colorado.edu>`

```
In article <dcqm97$lr5$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>I expect that meaning to wither and die, but it hasn't quite died yet.

Hasn't quite died?  I didn't even know it was ill!

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T14:11:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqja5$k95$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <3lagdmF11gr30U1@individual.net>`

```

On  2-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> >>Are you using the common definition of "begs the question" or the
> >>classical one?
…[4 more quoted lines elided]…
> on discussion.

Some of us value such clarification more than jumping into a discussion.   In
programming, it is quite possible to create a program that works quite well at
solving what I assume to be the needs of the users.

It's not easy to understand how someone who appears to be as knowledge at
programming as DD does, can repeatedly use that statement.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-03T04:57:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O8YHe.31403$iG6.5769@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcoec5$hsl$1@panix5.panix.com...
> In article <dcobr4$bu0$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[10 more quoted lines elided]…
> Answering a question with a question is no answer at all.

But it scores you points on Jeopardy.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T07:49:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqb0h$469$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <O8YHe.31403$iG6.5769@tornado.tampabay.rr.com>`

```
In article <O8YHe.31403$iG6.5769@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dcoec5$hsl$1@panix5.panix.com...
>> In article <dcobr4$bu0$1@peabody.colorado.edu>,
…[13 more quoted lines elided]…
>But it scores you points on Jeopardy.

I'll try to keep that in mind when I find myself addressing matters in 
that partiular venue, thanks.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-03T21:17:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bb621$42f17acc$45491c57$29980@KNOLOGY.NET>`
- **In-Reply-To:** `<O8YHe.31403$iG6.5769@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <dcobr4$bu0$1@peabody.colorado.edu> <dcoec5$hsl$1@panix5.panix.com> <O8YHe.31403$iG6.5769@tornado.tampabay.rr.com>`

```
jce wrote:
> <docdwarf@panix.com> wrote in message news:dcoec5$hsl$1@panix5.panix.com...
> 
…[16 more quoted lines elided]…
> But it scores you points on Jeopardy.

No, that's answering answers with a question.  :)
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T12:08:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lag8eF11lcrdU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dco9h7$ci4$1@panix5.panix.com...
>
> In article <dco8co$a29$1@peabody.colorado.edu>,
…[18 more quoted lines elided]…
>

This is where we come back to "absolute fact".  Is our individual perception 
of reality simply belief or is it fact? (I believe facts are what we agree 
to be true; but I don't believe they are absolute.) Can there be anything 
outside of our perception that is a fact? Is  "absolute fact"  simply tiny 
strings of energy oscillating in different ways through eleven dimensions, 
understandable by us as being subject to the laws of probability, but not 
necessarily so? Maybe. Can our perception change this reality? Maybe. 
Indications are that observing experiments may change the outcome of them.

Has anybody seen the film "What the bleep do we know?". I found it enjoyable 
but irritating in places because people who should know better were not 
telling the whole story or were putting their own spin it. But that's 
reality. It is all about getting agreement on what each of us perceive.

When I post to this forum you are getting a glimpse of my universe. When you 
post, I am getting a glimpse of yours. If our perceptions tally, we are in 
agreement and share a reality; if they don't, then we get irritated with 
each other... :-) But none of it has anything to do with "absolute fact".

And that's a fact. :-)

Pete.

> DD
>
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:38:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp764$4l3$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <3lag8eF11lcrdU1@individual.net>`

```
In article <3lag8eF11lcrdU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[23 more quoted lines elided]…
>This is where we come back to "absolute fact".

I noticed that a while back, Mr Dashwood... hence my assertion that 
''everything is relative' is absolutely true'.

>Is our individual perception 
>of reality simply belief or is it fact?

To posit a reality which one perceives assumes an answer to this.

>(I believe facts are what we agree 
>to be true; but I don't believe they are absolute.)

Ummmmmm... for centuries, Mr Dashwood, many 'we' agreed with Aristotle 
that heavier things fell faster than lighter ones.

[snip]

>When I post to this forum you are getting a glimpse of my universe. When you 
>post, I am getting a glimpse of yours.

That's poetic, Mr Dashwood... but I cannot agree.  It might be that when 
you/I post a glimpse of a universe is *given*... what is gotten might be 
entirely different.

(consider this in light of the aphorism 'a joke explained is a joke 
lost'... or 'to see the universe in a grain of sand'.  in the latter what 
is given is a bit of silicon, what is gotten is a glimpse of totality)

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T00:23:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lbrb2F11snk8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco8co$a29$1@peabody.colorado.edu> <dco9h7$ci4$1@panix5.panix.com> <3lag8eF11lcrdU1@individual.net> <dcp764$4l3$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcp764$4l3$1@panix5.panix.com...
>
> In article <3lag8eF11lcrdU1@individual.net>,
…[42 more quoted lines elided]…
>

Then that was a good enough working hypothesis for those people. Obviously, 
their lives were not materially affected by the weight of falling objects, 
or else they would have done more careful observation. It was left to the 
enquiring intellect of Galileo (who obviously DID care about falling 
objects, and objects in motion in general) to provide a correction to this 
careless observation.  I wonder if, like Newton, Galileo's insight stemmed 
from seeing something fall (or maybe having it land on his foot :-)).  Your 
statement is incorrect anyway (but I "cut you some slack" because I know 
what you are getting at... :-)); it only applies if the objects are falling 
in a vacuum. It is easily demonstrable that if you release a feather and a 
lead weight in the atmosphere of planet Earth the lead will hit the ground 
before the feather, so Aristotle's observation was perfectly adequate for 
everyday life. And it remained so for a couple of thousand years.

In the same way, Newton's laws of motion are adequate for most purposes 
(NASA uses them for space shots and they took men to the moon and back), but 
it took a young man in a Swiss Patents office to show they were actually 
flawed. He disagreed. At the moment he disagreed he could be considered 
insane, but he made a case and persuaded people to agree with his 
hypothesis. (As it was able to predict with incredible accuracy effects that 
could not even be demonstrated until technology caught up, and as it 
explained a puzzling creeping shift in the orbit of Mercury which had been 
put down to incorrect observation, because Newton couldn't be wrong, it 
became a better hypthesis. But Newton was simpler, and adequate for local 
space travel.)

All of which goes to show that when it comes to "absolute fact" there may be 
no such thing.
> [snip]
>
…[7 more quoted lines elided]…
>

That is a very astute (and fair) comment, Doc. My remark is predicated on 
the fact that you are able to duplicate the particles I send to you.  (If I 
send "Send reinforcements, we are going to advance", and you receive it as 
"Send three and fourpence, we are going to a dance", then I agree completely 
with your comment.)  And that I duplicate exactly what emanated from you in 
return.

Given that we communicate accurately, then I believe my statement to be 
true.

> (consider this in light of the aphorism 'a joke explained is a joke
> lost'... or 'to see the universe in a grain of sand'.  in the latter what
> is given is a bit of silicon, what is gotten is a glimpse of totality)

Hmmm... that's a bit more dodgy. The reason I say that is because what is 
passed is NOT a grain of silicon.

In Blake's poem he is not passing sand or wildflowers or anything else to 
us, other than the IDEA of an innocence that can see 'The Makers mark' in 
all things...

'To see a World in a grain of sand,
And a Heaven in a wild flower,
Hold Infinity in the palm of your hand
And Eternity in an hour.'

Still, I take your point that if what arrives at the effect point is NOT 
what what was sent from the cause point, then the communication breaks down, 
and, consequently, agreement is no longer possible...

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T09:33:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqh3m$pq2$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lag8eF11lcrdU1@individual.net> <dcp764$4l3$1@panix5.panix.com> <3lbrb2F11snk8U1@individual.net>`

```
In article <3lbrb2F11snk8U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[3 more quoted lines elided]…
>> Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>>>This is where we come back to "absolute fact".
>>
…[15 more quoted lines elided]…
>Then that was a good enough working hypothesis for those people.

It might have been, Mr Dashwood... but what was questioned was not a 
matter of 'a working hypothesis' but a credo (in the radical sense) of 
'facts are what we agree to be true'.

[snip]

>Your 
>statement is incorrect anyway (but I "cut you some slack" because I know 
>what you are getting at... :-)); it only applies if the objects are falling 
>in a vacuum.

Actually it applies to objects falling unopposed by other forces, of which 
air resistance is but one... a one-gram iron pellet will fall, in vacuo, 
more slowly than a two-gram lead pellet given a certain application of a 
magnetic field.

[snip]

>All of which goes to show that when it comes to "absolute fact" there may be 
>no such thing.

Hence the cautioning against presenting situations as 'absolute fact'... 
funny how it can work that way!

>> [snip]
>>
…[17 more quoted lines elided]…
>true.

We may believe that we communicate accurately, Mr Dashwood... but what do 
we know, anyhow?

>
>> (consider this in light of the aphorism 'a joke explained is a joke
…[17 more quoted lines elided]…
>and, consequently, agreement is no longer possible...

... and there lies the rub.  Take the grain of sand example, once again, 
in the sense of giving and getting: if one can see a World in it then what 
does one receive when one is given such a grain?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T02:56:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lc48jF11jpnuU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lag8eF11lcrdU1@individual.net> <dcp764$4l3$1@panix5.panix.com> <3lbrb2F11snk8U1@individual.net> <dcqh3m$pq2$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcqh3m$pq2$1@panix5.panix.com...
>
> In article <3lbrb2F11snk8U1@individual.net>,
…[33 more quoted lines elided]…
>

Everyone agreed with Aristotle on this until Galileo showed otherwise. 
Therefore it was an accepted "fact".

> [snip]
>
…[9 more quoted lines elided]…
> magnetic field.

Ah, it's all very well to be accurate NOW :-)
>
> [snip]
…[7 more quoted lines elided]…
>

I contend that I never did any such thing. I explained my reasoning 
elsewhere. If I state that somethig is a stupid practice, that is NOT an 
"absolute fact" even though Chuck chose to interpret it as if I was saying 
it was. That is the whole nub of this conversation. As I don't even believe 
in "absolute fact", and as my statements are implicitly limited to my own 
experience and imagination, I could not possibly be presenting something as 
"absolute fact", and anyone who thought I was, is in error.

(But that might not be a fact... :-))

>>> [snip]
>>>
…[24 more quoted lines elided]…
>

Precisely.

>>
>>> (consider this in light of the aphorism 'a joke explained is a joke
…[24 more quoted lines elided]…
>

One probably  receives a physical grain of sand. (Heisenberg shows that it 
isn't guaranteed.) What one makes of it, is entirely a matter of  one's 
perception.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T11:18:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqn7m$59c$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lbrb2F11snk8U1@individual.net> <dcqh3m$pq2$1@panix5.panix.com> <3lc48jF11jpnuU1@individual.net>`

```
In article <3lc48jF11jpnuU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[38 more quoted lines elided]…
>Everyone agreed with Aristotle on this until Galileo showed otherwise. 

'Everyone'?  It would be interesting to see the Opinion Polls behind that 
one!

>Therefore it was an accepted "fact".

Now there's a new qualifier... accepted.  Are there facts outside of the 
accepted?  If so then the assertion of 'facts are what we agree to be 
true' is disproven.

>
>> [snip]
…[12 more quoted lines elided]…
>Ah, it's all very well to be accurate NOW :-)

Better than never, some say.

>>
>> [snip]
…[12 more quoted lines elided]…
>it was.

In that the statement 'something is a stupid practise' has no restriction, 
exception or qualification it is, by definition, absolute.  In that 
'something' is 'a thing done' it describes a fact.

In that it is a statement of 'a thing done which has no restriction, 
exception or qualification' it is a statement of 'absolute fact', at least 
according to definitions available in a commonly-accepted source.

>That is the whole nub of this conversation. As I don't even believe 
>in "absolute fact", and as my statements are implicitly limited to my own 
>experience and imagination, I could not possibly be presenting something as 
>"absolute fact", and anyone who thought I was, is in error.

If they are in error, Mr Dashwood, then it might be due to your using the 
words idiosyncratically (as noted by the definitions above).

[snip]

>>>Still, I take your point that if what arrives at the effect point is NOT
>>>what what was sent from the cause point, then the communication breaks 
…[8 more quoted lines elided]…
>One probably  receives a physical grain of sand.

Says the giver... the recipient says what was received was a view of the 
World.  Whose word has greater sway?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T06:31:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xDiIe.35066$iG6.10400@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lbrb2F11snk8U1@individual.net> <dcqh3m$pq2$1@panix5.panix.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com>`

```
>docdwarf@panix.com
>> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> according to definitions available in a commonly-accepted source.

>>That is the whole nub of this conversation. As I don't even believe
>>in "absolute fact", and as my statements are implicitly limited to my own
…[5 more quoted lines elided]…
> words idiosyncratically (as noted by the definitions above).
I wouldn't describe the words as being used in a peculiar manner.   I think 
that it is more likely to be idiosyncratic that members of the group take 
such literal readings of what amounts to a free form unedited textual 
tete-a-tete.

I do believe that the interpretation of the word "fact" that I have seen in 
here make the following sentence impossible...
"This forum is full of mistaken facts".  The fact is that the status of 
facts is changeable based on what has been observed which would make that 
sentence viable.

>>>>Still, I take your point that if what arrives at the effect point is NOT
>>>>what what was sent from the cause point, then the communication breaks
…[12 more quoted lines elided]…
> World.  Whose word has greater sway?
I don't believe that the fact that the receiver "sees" a view of the world 
changes the fact that he received a grain of sand.  It's probably just worth 
more than other grains of sand without the view; however, I'm not sure if I 
like Blakes view that much...


JCE

> DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T07:51:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcsvgi$np4$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com>`

```
In article <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>>docdwarf@panix.com
>>> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[22 more quoted lines elided]…
>tete-a-tete.

I'm not sure what you are calling 'literal readings' here... but I find 
that I get confused so easily that I try to specify, especially with 
multivalent words, the sense/definition in which I am using them.  I do 
not expect any others to do as I do, of course... but I do not see how 
anyone can be faulted for either using words as they are defined in 
commonly-accepted sources or being confused when another uses words in 
manners different than those found in commonly-accepted sources.

>
>I do believe that the interpretation of the word "fact" that I have seen in 
…[3 more quoted lines elided]…
>sentence viable.

I am not sure how to read '(t)he fact is that the status of facts is 
changeable based on what has been observed' and it might be useful to 
re-state it.  Some facts do not seem to change ('I was born on 04 Aug 
1895') and others do ('Today is my 100th birthday'); how does this bear on 
your assertion?

[snip]

>>>> Take the grain of sand example, once again,
>>>> in the sense of giving and getting: if one can see a World in it then 
…[9 more quoted lines elided]…
>changes the fact that he received a grain of sand.

Seeing that the recipient says what was received was a view of the world 
how do you come to the conclusion that it is '... fact that he received a 
grain of sand'?  Are there reasons for aligning your belief with that of 
the giver... or are you asserting a sort of 'credo' and should it be left 
alone?

(extra credit: compare and contrast the exchange of:

A: 'I gave B a grain of sand.'
B: 'I received from A a view of the world.'

... with Kurosawa's film 'Rashomon'.  Use both sides of the posting if 
necessary.)

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T14:17:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lspIe.60126$mC.23648@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcsvgi$np4$1@panix5.panix.com...
> jce <defaultuser@hotmail.com> wrote:
snip

> Seeing that the recipient says what was received was a view of the world
> how do you come to the conclusion that it is '... fact that he received a
…[12 more quoted lines elided]…
> DD
Here is your text:

"... and there lies the rub.  Take the grain of sand example, once again,
in the sense of giving and getting: if one can see a World in it then what
does one receive when one is given such a grain?"

Your statement asserts that 'One can see a world in *it*' ..I think *it* 
refers to a grain of sand.   I don't believe it is either safe to presume or 
inferr or assume that one receives an absolute "view of the world" [such as 
would be found in space] - using your description of events not solely the 
descriptions provided by A and B.

A says I gave sand.
B says I received a view.

DD says a piece of sand with a view was given by A to B.  It seems that in 
describing the problem you have "asserted" would the situation was.  The 
answer would have been *mightily* changed had you reversed your statement of 
events - even it is a little less poetic.

......to see a grain of sand in a view then what does one receive when 
presented with a view.......

 The act of observation has broken the analogy.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T10:40:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dct9d5$s8u$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <lspIe.60126$mC.23648@tornado.tampabay.rr.com>`

```
In article <lspIe.60126$mC.23648@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dcsvgi$np4$1@panix5.panix.com...
>> jce <defaultuser@hotmail.com> wrote:
…[24 more quoted lines elided]…
>refers to a grain of sand.

That is correct; what I refer to is the that-which-was-given.  My question 
is 'for what reason(s) do you say a particular thing happened?'

>I don't believe it is either safe to presume or 
>inferr or assume that one receives an absolute "view of the world" [such as 
>would be found in space] - using your description of events not solely the 
>descriptions provided by A and B.

I don't recall saying anything about an absolute.

>
>A says I gave sand.
>B says I received a view.
>
>DD says a piece of sand with a view was given by A to B.

No.  I said 'A said I gave... B said I received'.

>It seems that in 
>describing the problem you have "asserted" would the situation was.  The 
>answer would have been *mightily* changed had you reversed your statement of 
>events - even it is a little less poetic.

I tried to follow chronology (rather difficult to receive something before 
it is given, last I looked) but I do not see your distinction; see below.

>
>......to see a grain of sand in a view then what does one receive when 
>presented with a view.......
>
> The act of observation has broken the analogy.

I am not sure I am making sense of this in the manner you intend.  Using 
the reversal you suggest:

B: 'I received a view of the World from A.'
A: 'I gave a grain of sand to B.'

... the question still appears to stand: Seeing that the recipient says 
what was received was a view of the world how do you come to the 
conclusion that it is '... fact that he received a grain of sand'?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T14:31:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dcsvgi$np4$1@panix5.panix.com...
> jce <defaultuser@hotmail.com> wrote:
snip
>>> If they are in error, Mr Dashwood, then it might be due to your using 
>>> the
…[12 more quoted lines elided]…
> manners different than those found in commonly-accepted sources.
I don't recall ever stating that you should be faulted.  I stated that it be 
idiosyncractic.

>>I do believe that the interpretation of the word "fact" that I have seen 
>>in
…[6 more quoted lines elided]…
> re-state it.
Facts are - using one definition (AH) - "Something believed to be true or 
real".  Occasionally what was "thought" a fact, was not a fact after all! It 
was a mistake, an error, a lapse of judgment or even something else.

> Some facts do not seem to change ('I was born on 04 Aug
> 1895') and others do ('Today is my 100th birthday'); how does this bear on
> your assertion?
I know someone who's birthday _did_ change.  For the first 25 years they 
celebrated it late so it would not be clear that he was conceived in a 
manner unsuitable to his upbringing.
What if you were a replicant and your memories were all implanted.  Now 
what's fact?

I will do you the service of saying....Not ALL facts are undisputed 
eternally.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T11:19:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctbl4$3f9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>`

```
In article <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dcsvgi$np4$1@panix5.panix.com...
…[18 more quoted lines elided]…
>idiosyncractic.

It is idiosyncratic to use commonly-accepted sources for the definitions 
of words or to be confused when another uses words in manners different 
than those found in commonly-accepted sources?  

In that 'idiosyncratic' is an antonym of 'conformity' it appears you are 
stating a contradiction.

>
>>>I do believe that the interpretation of the word "fact" that I have seen 
…[10 more quoted lines elided]…
>was a mistake, an error, a lapse of judgment or even something else.

This makes for a difficulty, also.  If the condition of belief makes for 
the condition of fact and the belief continues... how does the factuality 
end?

>
>> Some facts do not seem to change ('I was born on 04 Aug
…[4 more quoted lines elided]…
>manner unsuitable to his upbringing.

That's not the crowd *I* hang out with, certainly.

>What if you were a replicant and your memories were all implanted.  Now 
>what's fact?

I'll worry about that when it happens... right now I have enough 
difficulty dealing with 'what is' so that I try to avoid 'what if'.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T16:07:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H2rIe.60131$mC.17758@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctbl4$3f9$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dctbl4$3f9$1@panix5.panix.com...
> In article <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[23 more quoted lines elided]…
>>idiosyncractic.

> It is idiosyncratic to use commonly-accepted sources for the definitions
> of words or to be confused when another uses words in manners different
> than those found in commonly-accepted sources?

Not really - I'm just not careful enough in what I say.

It is idiosyncratic to use these definitions as the sole criteria for making 
a judgment on the meaning of a sentence and to be confused by context where 
_most_ (as determined by me in a proprietary manner) people.  I have yet to 
meet anyone who talks and writes with perfectly standard grammar as defined 
by your particular commonly-accepted-source.

The main purpose of the dictionary was to "standardize" the way that people 
talk.  Noah Webster, for example, tried to create a uniform dialect where 
multiple existed in various parts of the country even going so far as 
changing some words to match his ideal.  It was also, I believe, a statement 
against the "English" whose language dominated dictionaries at the time. 
Given his goa, I think it is safe to assume therefore, that he didn't 
succeed, and as such his dictionary in its  updated form (and other 
dictionaries of course) should be used used as a "tool" to communicate 
versus a definitive source of "this is the way it is".
I think that Pete as the owner of his words has attempted to clarify his 
"intent" and differentiate his "intent" from the over use of an incomplete 
tool.

Having said that - in this particular instance, I failed to qualify what I 
found to by idiosyncratic - the literal readings -and not the use of 
commonly-accepted sources.  For that I apologize.

> In that 'idiosyncratic' is an antonym of 'conformity' it appears you are
> stating a contradiction.
Not really.  See above.

 >>>>I do believe that the interpretation of the word "fact" that I have 
seen
>>>>in
>>>>here make the following sentence impossible...
…[14 more quoted lines elided]…
> end?
It doesn't.

>>> Some facts do not seem to change ('I was born on 04 Aug
>>> 1895') and others do ('Today is my 100th birthday'); how does this bear 
…[6 more quoted lines elided]…
> That's not the crowd *I* hang out with, certainly.
Glad to hear it.

>>What if you were a replicant and your memories were all implanted.  Now
>>what's fact?
> I'll worry about that when it happens... right now I have enough
> difficulty dealing with 'what is' so that I try to avoid 'what if'.
> DD
Do you mean "when it happens" or "if and when it happens?"  It is unclear to 
me from your use whether you anticipate this event or not.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T13:45:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctk78$44m$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctbl4$3f9$1@panix5.panix.com> <H2rIe.60131$mC.17758@tornado.tampabay.rr.com>`

```
In article <H2rIe.60131$mC.17758@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dctbl4$3f9$1@panix5.panix.com...
>> In article <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>,
…[30 more quoted lines elided]…
>Not really - I'm just not careful enough in what I say.

Such things happen to the best of folks... even *me*, sometimes!

>
>It is idiosyncratic to use these definitions as the sole criteria for making 
…[3 more quoted lines elided]…
>by your particular commonly-accepted-source.

Proprietary standards have, at times, caused incompatibilities to the 
point where entire systems crash... gotta watch out for those.  The 
definitions should not be considered the 'sole criteria (sic)' used to 
make a judgement... but they're not a bad place to start.

[snip]

>I think that Pete as the owner of his words has attempted to clarify his 
>"intent" and differentiate his "intent" from the over use of an incomplete 
>tool.

... and e'er-so-generous he was in doing so.

>
>Having said that - in this particular instance, I failed to qualify what I 
>found to by idiosyncratic - the literal readings -and not the use of 
>commonly-accepted sources.  For that I apologize.

Most gracious of you.

[snip]

>>>>>I do believe that the interpretation of the word "fact" that I have seen
>>>>>in
…[16 more quoted lines elided]…
>It doesn't.

Gah... my error and apologies, it is *my* turn to correct my sloppy 
writing.  I reversed a condition; my question should have read 'If the 
condition of belief makes for the condition of fact and the belief 
discontinues... how does the factuality end?'

>
>>>> Some facts do not seem to change ('I was born on 04 Aug
…[8 more quoted lines elided]…
>Glad to hear it.

I think that the crowd might be, as well.

>
>>>What if you were a replicant and your memories were all implanted.  Now
…[5 more quoted lines elided]…
>me from your use whether you anticipate this event or not.

I anticipate it sufficiently so that I do not worry about it until (when) 
it happens.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-05T13:34:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lfu0pF122ameU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctbl4$3f9$1@panix5.panix.com> <H2rIe.60131$mC.17758@tornado.tampabay.rr.com> <dctk78$44m$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dctk78$44m$1@panix5.panix.com...
>
> [snip]
…[6 more quoted lines elided]…
>
I honestly don't know what you are saying here, Doc. Can you clarify, or was 
it a shot best left in passing...:-)?

Pete

[snip]
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T06:42:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvfr8$jfp$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <H2rIe.60131$mC.17758@tornado.tampabay.rr.com> <dctk78$44m$1@panix5.panix.com> <3lfu0pF122ameU1@individual.net>`

```
In article <3lfu0pF122ameU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[11 more quoted lines elided]…
>it a shot best left in passing...:-)?

I am saying, Mr Dashwood, that you were generous in your attempts to 
clarify your intent earlier on in this thread.  I've seen interchanges 
along the lines of:

A: 'Doing (x)?  That is stupid!'

B: '(x) appears to be a reasonable series of actions under condition (y); 
for what reason are you calling it universally stupid?'

A: 'I have no experience with condition (y) and anyone who's read my 
postings should be able to conclude that; I was saying 'it is stupid' to 
relate that 'it is stupid according to my experience'.

B: 'Mightn't you have specified that you were making a statement of 
experience instead of a statement of absolute fact?'

A: '*All* statements made by all people at all times are statements of 
experience, there are no statements of absolute fact.  To think otherwise 
is stupid... and *that's* an absolute fact!'

... and your postings, here, did not appear, to me, to have this kind of 
antagonistic terseness.

DD
```

###### ↳ ↳ ↳ Perceived dates

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T15:51:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctdhh$907$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com>`

```

On  4-Aug-2005, "jce" <defaultuser@hotmail.com> wrote:

> > Some facts do not seem to change ('I was born on 04 Aug
> > 1895') and others do ('Today is my 100th birthday'); how does this bear on
> > your assertion?

Perception will change the latter when people read it tomorrow.

> I know someone who's birthday _did_ change.  For the first 25 years they
> celebrated it late so it would not be clear that he was conceived in a
> manner unsuitable to his upbringing.

My daughter shares a birthday with  Kareem Abdul-Jabbar, except she was born
right before Ferdinand Lewis Alcindor Jr. changed his name.

What did people do when calendars changed?   I suppose some adjusted their
birthdays by changing the date to the new format, others adjusted by having a
short year.

Leap year babies celebrate birthdays every year - my grandkids spread out their
birthday celebrations (3 of them were born on December 21, 26, & 29).

My favorite calendar story concerns a couple I knew in the USAF.   It seems that
he had his permanent station in Hawaii while serving temporarily in Korea.   If
he got married, his salary would go up, and he would have married people's
quarters.   So he married his fiance via the phone with her in Hawaii and him in
Korea.   When he got back home a couple of months later, they had a big church
wedding with all of their relatives enjoying a Hawaii vacation.

But with the international dateline between Hawaii and Korea, every year they
celebrate his anniversary, her anniversary, and their anniversary.

Cool.
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T16:13:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcteqp$9ma$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctdhh$907$1@peabody.colorado.edu>`

```
Also, there is some confusion about when certain events occur.   What date was
the Christmas tsunami?  What time did Armstrong first step on the moon?
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T13:47:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctkcb$5fh$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctdhh$907$1@peabody.colorado.edu> <dcteqp$9ma$1@peabody.colorado.edu>`

```
In article <dcteqp$9ma$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>Also, there is some confusion about when certain events occur.   What date was
>the Christmas tsunami?

That depends on which calendar one uses.

>What time did Armstrong first step on the moon?

When his boot first touched the lunar soil... see how easy?

('When does the 8:15 bus leave the station?  When it pulls out.')

DD
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T17:59:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctl2p$crg$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctdhh$907$1@peabody.colorado.edu> <dcteqp$9ma$1@peabody.colorado.edu> <dctkcb$5fh$1@panix5.panix.com>`

```

On  4-Aug-2005, docdwarf@panix.com wrote:

> >Also, there is some confusion about when certain events occur.   What date
> >was
> >the Christmas tsunami?
>
> That depends on which calendar one uses.

Also on where the observer is.

> >What time did Armstrong first step on the moon?
>
> When his boot first touched the lunar soil... see how easy?

When I was watching it on TV, I could have looked at my wall clock to see this?


> ('When does the 8:15 bus leave the station?  When it pulls out.')
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T14:16:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctm2g$7f9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcteqp$9ma$1@peabody.colorado.edu> <dctkcb$5fh$1@panix5.panix.com> <dctl2p$crg$1@peabody.colorado.edu>`

```
In article <dctl2p$crg$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  4-Aug-2005, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>Also on where the observer is.

Einstein stated that motion depends on where the observer is; since the 
tsunami is, by definition, a matter of motion this was assumed.

>
>> >What time did Armstrong first step on the moon?
…[4 more quoted lines elided]…
>see this?

Ansering a question with a question is no answer at all, Mr Brazee.

DD
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 29)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T19:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PouIe.35753$iG6.2651@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcteqp$9ma$1@peabody.colorado.edu> <dctkcb$5fh$1@panix5.panix.com> <dctl2p$crg$1@peabody.colorado.edu> <dctm2g$7f9$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dctm2g$7f9$1@panix5.panix.com...
> In article <dctl2p$crg$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[13 more quoted lines elided]…
> tsunami is, by definition, a matter of motion this was assumed.

As the tsunami was a matter of motion we assumed that Einstein stated that 
motion depends on where the observer is? My God! I didn't even realize the 
man was still alive.

>>> >What time did Armstrong first step on the moon?
>>> When his boot first touched the lunar soil... see how easy?
I believe Armstrong was actually riding in France for the last few weeks and 
hasn't had time to go to the moon yet.  In fact, I'm not sure that 
travelling to the moon is really possible - after all the current set of 
astronauts might have all the duct tape.

>>When I was watching it on TV, I could have looked at my wall clock to
>>see this?
>
> Ansering a question with a question is no answer at all, Mr Brazee.
> DD
Nor is answering a question with a non sequitur

JCE

JCE
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T06:45:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvfvu$krv$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctl2p$crg$1@peabody.colorado.edu> <dctm2g$7f9$1@panix5.panix.com> <PouIe.35753$iG6.2651@tornado.tampabay.rr.com>`

```
In article <PouIe.35753$iG6.2651@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dctm2g$7f9$1@panix5.panix.com...
…[19 more quoted lines elided]…
>man was still alive.

He isn't alive?  I didn't even know he was sick.

>
>>>> >What time did Armstrong first step on the moon?
…[11 more quoted lines elided]…
>Nor is answering a question with a non sequitur

This might be a reason why I attempt to avoid such things, aye... or it 
might be a reason for keeping a full refrigerator under the crescent moon 
while the striated insects fill the tuba.

DD
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 27)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-04T11:31:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctmu2$1bns$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctdhh$907$1@peabody.colorado.edu> <dcteqp$9ma$1@peabody.colorado.edu> <dctkcb$5fh$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dctkcb$5fh$1@panix5.panix.com...

> >What time did Armstrong first step on the moon?
>
> When his boot first touched the lunar soil... see how easy?

Actually I would have said the moment his *other* boot first touched the
lunar soil.

Had the question been either "What time did Armstrong first step onto the
moon?" or "What time did Armstrong first set foot on the moon?", I might
more readily agree with your answer!      ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T14:50:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcto17$t8n$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcteqp$9ma$1@peabody.colorado.edu> <dctkcb$5fh$1@panix5.panix.com> <dctmu2$1bns$1@si05.rsvl.unisys.com>`

```
In article <dctmu2$1bns$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dctkcb$5fh$1@panix5.panix.com...
…[10 more quoted lines elided]…
>more readily agree with your answer!      ;-)

Mr Stevens, I am unsure of what bearing this '*other*' boot has on the 
differentiation you make; using http://www.m-w.com for step(verb) gives me 
'3 : to press down with the foot' and unless his first boot ceased all 
downward motion after contacting the soil this seems to apply.

DD
```

###### ↳ ↳ ↳ Re: Perceived dates

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-05T13:36:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lfu50F126pbbU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <eFpIe.35082$iG6.14436@tornado.tampabay.rr.com> <dctdhh$907$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dctdhh$907$1@peabody.colorado.edu...
>
>
…[42 more quoted lines elided]…
>
Yes, really cool.

Is there no end to human ingenuity when it comes to "working the system"... 
:-)?

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-05T13:25:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lftfrF10nd9jU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc48jF11jpnuU1@individual.net> <dcqn7m$59c$1@panix5.panix.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com>`

```
 
PMFJI - it is easier to join this argument here, rather than respond 
directly to the Doc. Besides, I agree with what you are posting, 'jce', so I 
can support your argument here as well.

<docdwarf@panix.com> wrote in message news:dcsvgi$np4$1@panix5.panix.com...
>
> In article <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com>,
…[40 more quoted lines elided]…
>

As Doc is easily confused, he probably hasn't noticed that the context in 
which words are used often clarifies which particular meaning is intended.

"Common sources" (as noted elsewhere) often disagree in the finer shades of 
meaning. Context is a better indicator of what was intended, for a specific 
instance.

>>
>>I do believe that the interpretation of the word "fact" that I have seen 
…[5 more quoted lines elided]…
>
Agreed. A fact is a fact as long as people agree to it. When observations 
extend the information, the agreement changes. And so does the fact.

> I am not sure how to read '(t)he fact is that the status of facts is
> changeable based on what has been observed' and it might be useful to
…[3 more quoted lines elided]…
>

'I was born on 04 Aug 1895' is not a statement of fact. Even if it had my 
actual birthday substituted in it, it is only a "fact" because there were 
other people involved who can corroborate it (agree to it). As it is a past 
event there is no possible way to verify the truth of it. We are dependent 
on recordings made at the time, by observers, who could be seeing universes 
or grains of sand...or anything at all.

Yet most of us believe there is an absolute reality that must reflect what 
happens, whether we perceive it or agree to it or not.  It seems like Common 
Sense.  (The old chestnut that if a tree falls in the forest and no-one is 
there to hear it, does it make a sound? Most people think it does, yet some 
very learned  and intelligent minds are persuaded that it doesn't. Some 
arguments revolve on the definition of 'sound' and 'hearing', other 
arguments are much more esoteric and resort to the Anthropic Principle. The 
bottom line is that observing things in this universe may well change the 
way they behave. Nobody knows what energy and particles are doing when they 
are not observed, and when they ARE observed they behave in a way that is 
logically inconsistent [like being in two places at once, or being 
simultaneously a wave and a particle, and a whole lot of  other weird 
shit...).  Our Common Sense gives us the same view as Newton's idea of God 
winding up the clock and letting it tick at a standard rate throughout the 
Cosmos. An "absolute" background of space and time on which events happen. 
Where "absolute facts" are a reality.

I don't ascribe to it, and anyone who has dabbled in modern Physics is 
unlikely to, either. The universe confounds our common sense and is far more 
complex than our three dimensional brains can easily perceive. Space and 
time vary with relative location and acceleration; there is no "absolute 
fabric" for "absolute facts" to be painted on.

We can philosophize and argue, resort to all the Dictionaries and treatises 
in all the libraries of the Earth, it does not change anything. The universe 
is complex and weird.  There are no "absolute facts", and when I express an 
opinion, it is just that: my opinion. Reading more into it, being offended 
by it, or deciding it was meant to wound, may result in unnecessary 
discomfort and very long threads in CLC...


> [snip]
>
…[10 more quoted lines elided]…
>>> World.  Whose word has greater sway?

This was answered in the original post by the sentences which followed the 
above. Doc snipped it because it didn't allow him to continue with his 
argument that the effect has more validity than the cause, or vice versa.

Here's the full text:

"One probably  receives a physical grain of sand. (Heisenberg shows that it
 isn't guaranteed.) What one makes of it, is entirely a matter of  one's
 perception."

>>I don't believe that the fact that the receiver "sees" a view of the world
>>changes the fact that he received a grain of sand.

Neither do I.
>
> Seeing that the recipient says what was received was a view of the world
> how do you come to the conclusion that it is '... fact that he received a
> grain of sand'?

The recipient can say (and perceive) whatever he likes. This is rubbish 
anyway because the action of seeing the universe in a grain of sand does NOT 
preclude the recognition that it is still a grain of sand.  There is nothing 
in Blake's poem to suggest that the grain of sand has been mystically 
transformed into a view of the universe; it is more that the innocence of 
the receiver has "added value" to the grain of sand and extended the 
perception of it.(and if what was perceived was the "universe", that would 
necessarily INCLUDE the grain of sand in the recipient's palm....)

If we are talking about "absolute fact" (and that was what I have 
consistently disputed in this thread) then Heisenberg has some critical 
things to say on  the matter. Not being Philosophy, these have been 
conveniently ignored and were snipped.

It would seem that in the universe which we inhabit, NOTHING is absolute; 
there are only probabilities that events and the consequent phenomena  may 
occur.

Leaving physics for a moment and coming back to the grain of sand....

If I transmit to you a grain of sand and you see ONLY a view of the universe 
that does not include the grain of sand you were given, then your perception 
needs adjustment. Some helpful person would need to direct your attention to 
what was in your palm (without actually TELLING you it was a grain of 
sand...) and keep on doing so until you were able to perceive it. When we 
agree you have a grain of sand, it is a "fact".

I believe Dr. Freud invented an entire branch of medicine dedicated to 
helping people in this way.

> Are there reasons for aligning your belief with that of
> the giver... or are you asserting a sort of 'credo' and should it be left
> alone?
>
Neither is required.

> (extra credit: compare and contrast the exchange of:
>
> A: 'I gave B a grain of sand.'
> B: 'I received from A a view of the world.'
>
Or...
B: 'I received a grain of sand in which I can see a view of the world'
B: 'I want my Teddy...'

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T07:47:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvjkv$gap$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net>`

```
In article <3lftfrF10nd9jU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>PMFJI - it is easier to join this argument here, rather than respond 
…[49 more quoted lines elided]…
>which words are used often clarifies which particular meaning is intended.

As Doc has been easily confused by context, as well, he is in the habit of 
asking authors, directly - when available - their intention and how they 
were attempting to convey this intention by the words they use.

(Oh... and sometimes he refers to himself in the third person, too.)

>
>"Common sources" (as noted elsewhere) often disagree in the finer shades of 
>meaning. Context is a better indicator of what was intended, for a specific 
>instance.

What was intended, Mr Dashwood, and what was interpreted are not always 
the same... this might cause many enjoyable interchanges instead of a 
series of:

A: (g)

B: Ahhhhh, it is so.  (r)

A: Ahhhhh, it is so.  (3)

B: Ahhhhh, it is so.  (XIV)

... etc.

>
>>>
…[8 more quoted lines elided]…
>extend the information, the agreement changes. And so does the fact.

So, Mr Dashwood, it seems that we live in a rather Malleable Place, where 
one day heavier objects fall faster than lighter ones and the next day 
they don't, or one day spontaneous generation works and the next Pasteur 
is right, Spallanzani wrong.

>
>> I am not sure how to read '(t)he fact is that the status of facts is
…[6 more quoted lines elided]…
>'I was born on 04 Aug 1895' is not a statement of fact.

No matter who makes it?

>Even if it had my 
>actual birthday substituted in it, it is only a "fact" because there were 
>other people involved who can corroborate it (agree to it).

I have no idea, Mr Dashwood, how you are differentiating between a fact 
and a "fact".

>As it is a past 
>event there is no possible way to verify the truth of it.

Is this an absolute fact you're asserting?

>We are dependent 
>on recordings made at the time, by observers, who could be seeing universes 
>or grains of sand...or anything at all.

This reminds me of the old 'a fact is a fact only by consensus' argument.  
Thirty-odd years ago I remember encountering this from a college sophomore 
as we were motoring about, driving somewhere; he asserted that something 
was true if two or more people agreed to it.  I mentioned a few 
widely-held beliefs which seemedto oppose such an assertion (bubonic 
plague is spread by Jews poisoning wells, hysterical behavior is caused by 
a wandering uterus... things like that) and he grew silent... and then 
looked out the window and said 'It's starting to rain.'

My response was 'Is it?'

>
>Yet most of us believe there is an absolute reality that must reflect what 
>happens, whether we perceive it or agree to it or not.  It seems like Common 
>Sense.

It certainly seems to explain a lot of things to a lot of folks... two 
people walk in a desert; B steps behind A, produces a silenced pistol and 
shoots A in the back of the head.  A dies because of something of which he 
had no awareness.

That of which one is not aware has readily determinable effects... seems 
to say that awareness is not necessary for the existence of a fact.

>(The old chestnut that if a tree falls in the forest and no-one is 
>there to hear it, does it make a sound? Most people think it does, yet some 
…[4 more quoted lines elided]…
>way they behave.

See above about the Malleable Place theory.

>Nobody knows what energy and particles are doing when they 
>are not observed, and when they ARE observed they behave in a way that is 
>logically inconsistent [like being in two places at once, or being 
>simultaneously a wave and a particle, and a whole lot of  other weird 
>shit...).

When it comes to actions on the atomic (or sub-atomic) level, Mr Dashwood, 
this might be a concern... but the quantum variations in a thrown baseball 
seem to be a bit less significant.  

It might be that effects are more statistical in their observability... 
when one applies energy to a single gas particle the resulting direction 
it takes is, in terms of physics, defined as 'random'; when one applies 
energy to a larger collection of gas particles which can contact a 
liquid-based thermometer the direction the liquid goes is, by most 
accounts, 'up'... the gas gets hotter.

On the individual level, random direction... on the collective level, 
predictable heating.

>Our Common Sense gives us the same view as Newton's idea of God 
>winding up the clock and letting it tick at a standard rate throughout the 
…[4 more quoted lines elided]…
>unlikely to, either.

As mentioned earlier in the thread, Mr Dashwood: ''Everything is relative' 
is absolutely true!'

>The universe confounds our common sense and is far more 
>complex than our three dimensional brains can easily perceive. Space and 
>time vary with relative location and acceleration; there is no "absolute 
>fabric" for "absolute facts" to be painted on.

Absolutely so... it seems.

>
>We can philosophize and argue, resort to all the Dictionaries and treatises 
>in all the libraries of the Earth, it does not change anything. The universe 
>is complex and weird.  There are no "absolute facts", and when I express an 
>opinion, it is just that: my opinion.

'There are no "absolute facts" is absolutely true'... how many variations 
of this are you going to offer, Mr Dashwood?

[snip]

>>>>>> Take the grain of sand example, once again,
>>>>>> in the sense of giving and getting: if one can see a World in it then
…[12 more quoted lines elided]…
>argument that the effect has more validity than the cause, or vice versa.

No, Mr Dashwood, my motive was otherwise... Doc snipped it because he saw 
it as having no bearing on the discussion he was having... whoops, there's 
that third person reference again.

>
>Here's the full text:
…[3 more quoted lines elided]…
> perception."

'What one makes of it', Mr Dashwood, in the case of the post to I was 
responding, was 'probably a physical grain of sand'.  The person posting 
this (most probably not Heisenberg) made an assertion and I wished to 
examine the reasoning behind that; my apologies if my motive was 
insufficiently clear.

>
>>>I don't believe that the fact that the receiver "sees" a view of the world
>>>changes the fact that he received a grain of sand.
>
>Neither do I.

As above, Mr Dashwood... you agree with the giver, A, who says 'I gave a 
grain of sand.'  For what reason(s) do you take this observation as fact 
and not the observation of the recipient ('I received a view of the 
World'?)

>>
>> Seeing that the recipient says what was received was a view of the world
…[3 more quoted lines elided]…
>The recipient can say (and perceive) whatever he likes.

And this does not apply to the giver because... because you, Mr Dashwood, 
do not believe it to be such?

>This is rubbish 
>anyway because the action of seeing the universe in a grain of sand does NOT 
>preclude the recognition that it is still a grain of sand.

What makes it 'still a grain of sand', Mr Dashwood, and not 'a view of the 
World'?  Repeating your assertion appears to add little validity.

[snip]

>If we are talking about "absolute fact" (and that was what I have 
>consistently disputed in this thread) then Heisenberg has some critical 
>things to say on  the matter. Not being Philosophy, these have been 
>conveniently ignored and were snipped.

I am asking the reasons one takes a particular view, Mr Dashwood... you 
seem to have offered beliefs, nothing more.

>
>It would seem that in the universe which we inhabit, NOTHING is absolute; 
>there are only probabilities that events and the consequent phenomena  may 
>occur.

Once again this curious 'we'... I ask you to speak for yourself, Mr 
Dashwood: in the universe *you* inhabit is 'NOTHING is absolute' 
absolutely true?

>
>Leaving physics for a moment and coming back to the grain of sand....
…[3 more quoted lines elided]…
>needs adjustment.

That is interesting, Mr Dashwood... a grain of sand which exists outside 
of the universe.  Any idea what its mailing-address might be?

>Some helpful person would need to direct your attention to 
>what was in your palm (without actually TELLING you it was a grain of 
>sand...) and keep on doing so until you were able to perceive it. When we 
>agree you have a grain of sand, it is a "fact".

"Fact" (whatever that is) by consensus again... is it raining?

>
>I believe Dr. Freud invented an entire branch of medicine dedicated to 
…[6 more quoted lines elided]…
>Neither is required.

Nobody said they were, Mr Dashwood, and nobody said those are the only two 
possibilities... but to align one's belief without reason is to do so, by 
definition, irrationally, and to assert a 'credo' is, likewise, to align 
belief without reason...

... it is is nice to know, in my experience, if one with whom is 
discussing things is aware of their irrationality.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-05T14:19:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GzKIe.60350$mC.52641@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcvjkv$gap$1@panix5.panix.com...
> In article <3lftfrF10nd9jU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
<SNIPPED>

>>>>I do believe that the interpretation of the word "fact" that I have seen
>>>>in
…[12 more quoted lines elided]…
> is right, Spallanzani wrong.

No. I believe we were clear on this.  No one stated that one day heavier 
objects fall faster than lighter ones and the next day they don't.  Once it 
was a fact that spontaneous generation was true...Then it was proved that 
spontaneous generation would not work without air....then finally Pasteur 
improved the experiment suffiiciently to allow air into the mix and still 
not have spontaneous combustion.   I think that your assertion that each of 
these events were separated by days is incorrect...I believe it was many a 
year.  The facts changed and were developed.  Some facts are a product of 
the sum of knowledge and experience...all facts are based on some level of 
belief.  I cannot prove WITHOUT a doubt that I was even alive yesterday.  I 
assume I was.


>>> I am not sure how to read '(t)he fact is that the status of facts is
>>> changeable based on what has been observed' and it might be useful to
…[5 more quoted lines elided]…
> No matter who makes it?

>>Even if it had my
>>actual birthday substituted in it, it is only a "fact" because there were
…[3 more quoted lines elided]…
> and a "fact".
By the use of quotes, I believe.  Or are you asking how he is 
differentiating between the meaning and his intent of the use of <fact> and 
<"fact"> ?

>>As it is a past
>>event there is no possible way to verify the truth of it.
…[13 more quoted lines elided]…
> looked out the window and said 'It's starting to rain.'
So I need some clarity.

I don't believe that anyone believed Jews were poisoning wells...I mean 
wells are inanimate objects!
I think if I was wandering about and came across a uterus, I'm not sure 
hysteria would follow - but I might be a little shocked you know.
Anyway, what were you trying to contradict? He stated that two people have 
to agree before something is fact..not that two people agreeing on something 
made it a fact.

> My response was 'Is it?'
I would have died (not literally of course) laughing if I could have been 
there.

<snip>

>>Nobody knows what energy and particles are doing when they
>>are not observed, and when they ARE observed they behave in a way that is
…[5 more quoted lines elided]…
> seem to be a bit less significant.

I'm not sure I trust the smarty pants who come up with this stuff to believe 
them anyway.
All we have is the human ability to make <shit> up to make it do sort of 
what we want it to do.
Mathematics is the basis for most of the arguments and also measurements. 
Two things strike me as odd: firstly mathematics is a branch invented by 
people to describe things for them.  Second, everything is measured, and as 
we have stated that measuring changes things, I am at a loss to clearly 
understand how measuring anything solves anything.

I believe that science gets as weird as we let people get it.  I don't know 
many people that can verify anything that any of these people does.  And a 
theory based on conjecture does not a theory make in my book - but that is 
sometimes how things work.

That poor guy who "proved" Fermat was just "proved" wrong.....geez...what a 
waste of 10 years

> It might be that effects are more statistical in their observability...
> when one applies energy to a single gas particle the resulting direction
…[14 more quoted lines elided]…
>>unlikely to, either.

And 200 years from now modern physics is classical physics.

<snip>

>>We can philosophize and argue, resort to all the Dictionaries and 
>>treatises
…[7 more quoted lines elided]…
> of this are you going to offer, Mr Dashwood?
And that's absolutely a fact !

<snip>

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T12:44:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd0528$3jc$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <GzKIe.60350$mC.52641@tornado.tampabay.rr.com>`

```
In article <GzKIe.60350$mC.52641@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dcvjkv$gap$1@panix5.panix.com...
>> In article <3lftfrF10nd9jU1@individual.net>,
…[24 more quoted lines elided]…
>not have spontaneous combustion.

I believe that you intended 'generation', and not combustion.

>I think that your assertion that each of 
>these events were separated by days is incorrect...I believe it was many a 
>year.  The facts changed and were developed.

So instead of taking days it took years... the malleability still is 
asserted to exist.  It would make it kind of difficult to demonstrate 
experiments of days gone by, certainly.

>Some facts are a product of 
>the sum of knowledge and experience...all facts are based on some level of 
>belief.

The conclusion of 'all facts are based on some level of belief' appears to 
be that if the belief changes, the fact changes.  A malleable *and* 
democratic universe... if enough folks believe it then it seems that ice 
will occupy the same volume as the water which was cooled to make it.

>I cannot prove WITHOUT a doubt that I was even alive yesterday.  I 
>assume I was.

'Proof' is another concept, entire, and has shown to generate much 
discussion amongst Very Learned Folks... what constitutes such a thing has 
been debated a fair amount.

>
>
…[17 more quoted lines elided]…
><"fact"> ?

I am asking what Mr Dashwood believes to be the difference between what he 
labels as a fact and what he labels as a "fact".

>
>>>As it is a past
…[18 more quoted lines elided]…
>wells are inanimate objects!

Nobody said the wells suffered any ill-effects from the action... but in 
that poisoning is defined as 'to treat, taint, or impregnate with or as if 
with poison' it was believed.

>I think if I was wandering about and came across a uterus, I'm not sure 
>hysteria would follow - but I might be a little shocked you know.

You think that's bad... imagine coming across a baseball-game judge whose 
existence at that time was entirely one of going from one place to another 
without purpose or direction... you'd have found a wholly roaming umpire.

>Anyway, what were you trying to contradict? He stated that two people have 
>to agree before something is fact..not that two people agreeing on something 
>made it a fact.

In the case of my friend, no... as stated above, '... he asserted that 
something was true if two or more people agreed to it.'

>
>> My response was 'Is it?'
>I would have died (not literally of course) laughing if I could have been 
>there.

His response was similar, aye.

>
><snip>
…[18 more quoted lines elided]…
>understand how measuring anything solves anything.

Proper measuring can make for pants that are rather smartly cut... see how 
easy?

>
>I believe that science gets as weird as we let people get it.  I don't know 
…[5 more quoted lines elided]…
>waste of 10 years

Everyone needs a hobby, sure.

[snip]

>>>I don't ascribe to it, and anyone who has dabbled in modern Physics is
>>>unlikely to, either.
>
>And 200 years from now modern physics is classical physics.

I'll worry about that when it happens.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-06T14:29:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lilk7F12k3erU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <GzKIe.60350$mC.52641@tornado.tampabay.rr.com> <dd0528$3jc$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dd0528$3jc$1@panix5.panix.com...
>
<snip>. you'd have found a wholly roaming umpire.
:-) Good one, Doc...
>
>>Anyway, what were you trying to contradict? He stated that two people have
…[6 more quoted lines elided]…
>
If two people agree on something it is true FOR THEM.

I did not intend to imply that agreement by itself makes things true.

JCE's interpretation of what I said is the one I intended: For something to 
be a fact, two or more people must agree to it. NOT that two or more people 
agreeing makes something a fact. Subtle but important.


<snip>

I take JCE's point that there is much that is 'unprovable' or 'unobservable' 
(except by the analog of mathematics) in our understanding of the universe. 
However, I have seen enough, read enough and done enough to give me the 
world view which I have exposed here.

I return to the original point:

In the case which prompted this discussion, I was expressing an opinion. 
Whenever I post to CLC I am expressing an opinion. As I don't believe in 
"absolute fact" I can do nothing OTHER than express an opinion. I do not 
believe that adding "I believe" to my commnets would make them any more or 
less valuable, or more or less true.

I have already posted to Chuck and explained this.

If you are offended by something being stated strongly and  feel it has 
contemptuous (or any other negative) implications, then please don't read or 
respond to my posts. It has never been my purpose (except where explicitly 
stated as such, or unambiguous offensive statements were made :-)) to offend 
by posting here. If I am pissed off about something I will say so without 
implication or innuendo. Otherwise, my posts should be taken at face value.

That's it on this from me.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-06T09:59:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd2foa$jp6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <GzKIe.60350$mC.52641@tornado.tampabay.rr.com> <dd0528$3jc$1@panix5.panix.com> <3lilk7F12k3erU1@individual.net>`

```
In article <3lilk7F12k3erU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[3 more quoted lines elided]…
>:-) Good one, Doc...

Glad you enjoyed.

>>
>>>Anyway, what were you trying to contradict? He stated that two people have
…[7 more quoted lines elided]…
>If two people agree on something it is true FOR THEM.

That is not what my friend said, no... but are you saying that '... it is 
true FOR THEM' is an absolute fact?

>
>I did not intend to imply that agreement by itself makes things true.
…[3 more quoted lines elided]…
>agreeing makes something a fact. Subtle but important.

And as pointed out... one day Galileo, alone, disagrees with Aristotle and 
the next day both Galileo and his buddy, Giuseppe, both disagree.  A 
rather... malleable universe.

[snip]

>In the case which prompted this discussion, I was expressing an opinion. 

In that it was stated in the form of absolute fact this is to be known 
only in retrospect and with clarification.

>Whenever I post to CLC I am expressing an opinion.

Now that some are aware of this it might be kept in mind.

>As I don't believe in 
>"absolute fact" I can do nothing OTHER than express an opinion.

Is that an absolute fact, now?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-06T14:03:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lik42F12ra7rU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcvjkv$gap$1@panix5.panix.com...
>
> In article <3lftfrF10nd9jU1@individual.net>,
…[103 more quoted lines elided]…
>
<DISCLAIMER - Pete's opinion follows. Usual rules apply... no offense, 
Unisys sites excluded, yadayadayada...>
Yes, Doc. That is a fair summation. Only it isn't 'malleable' because it 
obeys the laws of physics in this universe. They tend to be inviolate... 
Those same laws also guarantee a degree of uncertainty which often conflicts 
with 'common sense'. The universe is unknowable, not by the decree of a 
Supreme Being, but by the behaviour of energy and particles at a quantum 
level. It is very unwise to believe that "absolute fact" is attainable. The 
best we can hope for is to agree on the current apparency, so we can jointly 
deal with it.
</DISCLAIMER>

>>
>>> I am not sure how to read '(t)he fact is that the status of facts is
…[9 more quoted lines elided]…
> No matter who makes it?

Nope. No matter who makes it. The past is no longer verifiable with absolute 
certainty. Only a degree of certainty (which may be very close to 100%...)

>
>>Even if it had my
…[9 more quoted lines elided]…
> Is this an absolute fact you're asserting?

No. But it has a high probably of being true... That probably is lessened if 
you disagree or increased if you agree.
>
>>We are dependent
…[28 more quoted lines elided]…
>

No, the above example simply shows that B's reality continues while A's 
stops. A is no longer aware of the bullet so it is unreal for him. 
Physically, the kinetic energy of the bullet damaged a part of A that was 
necessary for continued perception and survival. If it had been a meteorite 
that did it, A might still have died, unaware of what killed him. But there 
is no GUARANTEE (or absolute certainty) that he would.

Even the bullet does not provide certainty; there is a small, but finite 
chance, that the bullet could pass through A's head doing no damage at all, 
not even leaving a scratch (if the atoms of the bullet aligned with the 
spaces between the atoms of A's head...)

In all cases above there IS an awareness (observer) present; that of B. 
Therefore the events are "real" ... for B.

The assertion that 'awareness is not necessary for the existence of fact' is 
therefore unproven.

When Einstein was confronted with this same argument he laughingly replied: 
"You don't really think the moon disappears when you are not looking at it?"

It is a good response from a revered authority, but modern research is 
showing more and more that he may have been wrong . The detailed response to 
this is too intricate and requires too much effort to go into here, but if 
you accept that the moon is there and the earth is here, how can you be sure 
that they don't just exist in your imagination? Because other people share 
that reality with you. Agreement makes things real. The moon doesn't 
disappear because it is part of a collective reality. (that's the best I can 
do in the limited time and space I have available here, and it is an 
inadequate attempt, but hopefully the  concept is clear.)





>>(The old chestnut that if a tree falls in the forest and no-one is
>>there to hear it, does it make a sound? Most people think it does, yet 
…[18 more quoted lines elided]…
> seem to be a bit less significant.

That depends on who or what is viewing the baseball.
>
> It might be that effects are more statistical in their observability...
…[5 more quoted lines elided]…
>
Yes, that is a workable hypthesis. Yet we know that SOME of the gas DOESN'T 
go up...

> On the individual level, random direction... on the collective level,
> predictable heating.

Certainly predictable, but only within the realms of probablity. Not 
certain; not absolute. Hence I refute "absolute fact".
>
>>Our Common Sense gives us the same view as Newton's idea of God
…[9 more quoted lines elided]…
>
It is true, but NOT absolutely.

>>The universe confounds our common sense and is far more
>>complex than our three dimensional brains can easily perceive. Space and
…[4 more quoted lines elided]…
>
:-) Your irony is wasted on us fanatics, Doc...
>>
>>We can philosophize and argue, resort to all the Dictionaries and 
…[9 more quoted lines elided]…
>

I have offered NO variations on it because I never said it. It is YOUR 
quote, repeated to the point of being tiresome.

In my universe there are no absolutes, only probabilities. I have been clear 
on that on every occasion.

> [snip]
>
…[21 more quoted lines elided]…
> that third person reference again.

Well, then I could be forgiven for letting him have that dicussion on his 
own... If you wish to discuss statements I made, removed from the context in 
which I made them, why would you expect me to respond?
>
>>
…[11 more quoted lines elided]…
> insufficiently clear.

OK.
>
>>
…[9 more quoted lines elided]…
> World'?)

Because the giver's answer does not preclude the fact that I gave him a 
grain of sand. You have changed the wording again; it isn't "World" it is 
"universe", and universe includes the grain of sand.

>>>
>>> Seeing that the recipient says what was received was a view of the world
…[15 more quoted lines elided]…
> World'?  Repeating your assertion appears to add little validity.

About as much as you repeating yours... :-) (And getting it wrong...)

Again, you snipped my reference to Blake's poem which clarified this. Your 
selective removal of contexts which answer your question or refute your 
argument leads me to question whether you are serious about this whole 
discussion.

I have no problem with you not being, but perhaps my time could be better 
employed...
>


> [snip]
>
…[7 more quoted lines elided]…
>

Beliefs may be all there is.

>>
>>It would seem that in the universe which we inhabit, NOTHING is absolute;
…[6 more quoted lines elided]…
>

It is of an extremely high probability... close to, but not touching, 
certainty. Get over it.

>>
>>Leaving physics for a moment and coming back to the grain of sand....
…[9 more quoted lines elided]…
>

Read what I said. IF YOU PERCEIVE the universe not to include the grain of 
sand...

>>Some helpful person would need to direct your attention to
>>what was in your palm (without actually TELLING you it was a grain of
…[4 more quoted lines elided]…
>
My contention is, and has been all along, that there are no facts except by 
consensus.
>>
>>I believe Dr. Freud invented an entire branch of medicine dedicated to
…[16 more quoted lines elided]…
>
Yes, isn't it  :-)?

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-06T10:18:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd2gsa$1j3$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net>`

```
In article <3lik42F12ra7rU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[3 more quoted lines elided]…
>> Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>>>Agreed. A fact is a fact as long as people agree to it. When observations
>>>extend the information, the agreement changes. And so does the fact.
…[9 more quoted lines elided]…
>obeys the laws of physics in this universe.

Mr Daswhwood, that seems to be a contradiction.  If 'it seems that we live 
in a rather Malleable Place, where ond day heavier objects fall faster 
than lighter ones and the next day they don't' is 'a fair summation'... 
but 'it isn't malleable' because it obeys the laws of physics in this 
universe' (never mind the question of these laws being absolute facts')

... then in one sentence you say that the laws of physics change from day 
to day, in that the laws governing the acceleration of falling bodies are 
the result of such laws, while in the next you say these laws are 
immutable (in the given universe).

Given that 'a thing cannot both be, and yet not be, the same thing in 
regards to the same aspect at the same time' (Aristotle) it would seem 
that you have broken the Law of Non-Contradiction.

>They tend to be inviolate... 

'Tend to be', Mr Dashwood?  'Half dead' is still very much alive... either 
the laws to which you refer get violated or they don't... which is it?

>Those same laws also guarantee a degree of uncertainty which often conflicts 
>with 'common sense'. The universe is unknowable, not by the decree of a 
>Supreme Being, but by the behaviour of energy and particles at a quantum 
>level.

That a measurement of an electron, necessarily made with light, makes one 
of its aspects (eg, location) unknowable with respect to another (eg, 
speed) in no wise makes it impossible for a skilled hunter to determine 
both aspects well enough to put a duck on the table, Mr Dashwood.

[snip]

>>>'I was born on 04 Aug 1895' is not a statement of fact.
>>
…[3 more quoted lines elided]…
>certainty. Only a degree of certainty (which may be very close to 100%...)

Wow... must have been a dull day on the obstetrics ward, nobody was born 
on 04 Aug 1895... sorry, could not resist.

Verification was not asked for, Mr Dashwood... but in that being born is a 
'thing done' it appears that your definition of 'fact' is different from 
that which appears in a commonly-accepted source which I have cited here, 
repeatedly 
(http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=fact&x=0&y=0 , 1).

It might be that our disagreement arises from using different definitions; 
would you be so kind as to provide the definition you are using for 'fact' 
so that this possibility might be addressed or dismissed?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-06T12:13:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123355630.959750.293010@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dd2gsa$1j3$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <dd2gsa$1j3$1@panix5.panix.com>`

```
> If 'it seems that we live
> in a rather Malleable Place, where ond day heavier objects fall faster
> than lighter ones and the next day they don't' is 'a fair summation'...

It seems to me that a lead weight does actually fall faster than a
feather. always has done (in this place), and continues to do so.  Your
claim was never a 'fair summation'.

> but 'it isn't malleable' because it obeys the laws of physics in this
> universe' (never mind the question of these laws being absolute facts')

Those objects do obey the laws of physics, or those we use as
simplifications, it is only the explanations of why things happen that
change, not the observable facts.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-06T20:37:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c9Je.61802$mC.10721@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <dd2gsa$1j3$1@panix5.panix.com> <1123355630.959750.293010@g14g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1123355630.959750.293010@g14g2000cwa.googlegroups.com...
>> If 'it seems that we live
>> in a rather Malleable Place, where ond day heavier objects fall faster
…[11 more quoted lines elided]…
> change, not the observable facts.

Was there not an implied, "in my opinion it is...."

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-06T16:44:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123371868.830664.94460@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1c9Je.61802$mC.10721@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <dd2gsa$1j3$1@panix5.panix.com> <1123355630.959750.293010@g14g2000cwa.googlegroups.com> <1c9Je.61802$mC.10721@tornado.tampabay.rr.com>`

```
> Was there not an implied, "in my opinion it is...."

What part of "It seems to me .." did you fail to notice ?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-07T05:08:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sHgJe.62663$mC.54807@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <dd2gsa$1j3$1@panix5.panix.com> <1123355630.959750.293010@g14g2000cwa.googlegroups.com> <1c9Je.61802$mC.10721@tornado.tampabay.rr.com> <1123371868.830664.94460@g47g2000cwa.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1123371868.830664.94460@g47g2000cwa.googlegroups.com...
>> Was there not an implied, "in my opinion it is...."
>
> What part of "It seems to me .." did you fail to notice ?

It appears my highlight / delete failed...

It should have read:
<begin>
>> If 'it seems that we live
>> in a rather Malleable Place, where ond day heavier objects fall faster
…[4 more quoted lines elided]…
> claim was never a 'fair summation'.

Was there not an implied, "in my opinion it is....[a fair summation]"
<end>

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-06T21:00:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd3meo$5bn$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lik42F12ra7rU1@individual.net> <dd2gsa$1j3$1@panix5.panix.com> <1123355630.959750.293010@g14g2000cwa.googlegroups.com>`

```
In article <1123355630.959750.293010@g14g2000cwa.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>> If 'it seems that we live
>> in a rather Malleable Place, where ond day heavier objects fall faster
…[4 more quoted lines elided]…
>claim was never a 'fair summation'.

Mr Plinston, the question of opposing forces was covered previously and 
responded-to by Mr Dashwood in 
<http://groups-beta.google.com/group/comp.lang.cobol/msg/83b819eae988603c?dmode=source&hl=en> 
; I was not aware that there were those who required the shorthand of 
'heavier objects fall faster than lighter ones' to be expanded to 'heavier 
objects fall faster than lighter ones under conditions where both are 
unopposed by other forces'.

As far as calling my claim a 'fair summation'... as I read 
<http://groups-beta.google.com/group/comp.lang.cobol/msg/b181d45236e25b10?dmode=source&hl=en> 
the text of:

--begin quoted text:

> So, Mr Dashwood, it seems that we live in a rather Malleable Place, where
> one day heavier objects fall faster than lighter ones and the next day
> they don't, or one day spontaneous generation works and the next Pasteur
> is right, Spallanzani wrong.
>
<DISCLAIMER - Pete's opinion follows. Usual rules apply... no offense, 
Unisys sites excluded, yadayadayada...>
Yes, Doc. That is a fair summation. 

--end quoted text

... the label of 'a fair summation' is applied by Mr Dashwood.  If you 
disagree with it you might mention that to him.

>
>> but 'it isn't malleable' because it obeys the laws of physics in this
…[4 more quoted lines elided]…
>change, not the observable facts.

I am not sure how Mr Dashwood considers observation in the scheme of 
things... but I recall his asserting that 'I was born on 04 Aug 1895' is 
not a statement of fact... As it is a past event there is no possible way 
to verify the truth of it.'  That being the case it might be readily 
concluded that observed facts, being past events, are equally impossible 
to verify... but that might not matter so much as we seem to live in such 
a Malleable Place.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-08T21:49:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sQJe.192230$tt5.56640@edtnps90>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3lik42F12ra7rU1@individual.net...
> if you accept that the moon is there and the earth is here, how can you be 
> sure that they don't just exist in your imagination? Because other people 
> share that reality with you. Agreement makes things real. The moon doesn't 
> disappear because it is part of a collective reality.

    What if I were imagining those "other people" as well?

    I don't remember who said it, but someone said something along the lines 
of "if two peopel agree to something, then it is real to them." As an 
open-ended and undirected question to ponder, what if person A pereceived 
(either via reality or imagination, person A cannot distinguish between the 
two) persons B and C. Person C only perceives person B. Person A claims that 
it is raining, and claims that person B agrees with him. Person C claims 
that it is not raining and person B doesn't exist. Does this means it's 
raining?

    Person A might believe it's raining, having agreement from person B, and 
simply assume person C is insane.
    Person C might believe it's not raining, and assume A is insane.

    To make things more interesting, perhaps we can throw in a person D who 
agrees with C that it is not rainning, but whom person A cannot perceive.

    - Oliver
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T18:29:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8md7$qbs$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90>`

```
In article <7sQJe.192230$tt5.56640@edtnps90>,
Oliver Wong <owong@castortech.com> wrote:
>
>"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[6 more quoted lines elided]…
>    What if I were imagining those "other people" as well?

Well, I'd *hope* you'd be able to make them a bit more interesting!

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-09T15:11:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lql6iF12jsntU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90>`

```
 

"Oliver Wong" <owong@castortech.com> wrote in message 
news:7sQJe.192230$tt5.56640@edtnps90...
>
>
…[7 more quoted lines elided]…
>    What if I were imagining those "other people" as well?

There is some evidence to suggest that you are :-), but it is way beyond 
this discussion...

>
>    I don't remember who said it, but someone said something along the 
…[14 more quoted lines elided]…
>

You might also ponder that any of the 4 of them who cannot perceive that he 
is wet,  would be unlikely to agree that it is raining... :-)

The arguments about perception and reality have persisted for centuries. All 
of your points above are very good ones. Agreeing to share a reality is a 
workable hypothesis for  dealing with what is perceived.

I cannot 'know' that what you call 'red' is exactly what I call 'red'. But 
we can agree that whatever it is that each of us perceives as 'red' can be 
labelled as such, and that enables us to deal with it. If you then ask me to 
pass you the can of red paint I will pass you something we both agree is 
red. (please don't deluge the thread with examples of red-green colour 
blindness and exceptions of that nature; I am painting with broad strokes 
here... :-)

Thus words are symbols that allow us to share perception and 'create' 
reality. The danger is that the "word authority" (Dictionaries) become an 
end in themselves and become the dog instead of the tail (maybe that's where 
'dogma' comes from :-))  The tail does not wag the dog. Dictionaries are 
intended to help communication, not to restrict meaning to whatever their 
definitions cover. That is why there is a wide diversity of such references. 
But, if you look across all of them for a given word, you will derive a 
'concept' that is agreed by all of them. Selecting any given one as "The 
Authority" is risky at best.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-09T05:24:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd9so2$eql$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net>`

```
In article <3lql6iF12jsntU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>Thus words are symbols that allow us to share perception and 'create' 
>reality. The danger is that the "word authority" (Dictionaries) become an 
>end in themselves and become the dog instead of the tail (maybe that's where 
>'dogma' comes from :-))  The tail does not wag the dog.

The arguments of 'proscriptive versus descriptive' aside... the tail does 
not wag the dog?  Is that an absolute fact, now?  In terms of Einsteinian 
motion everything is relative, you know...

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-09T13:16:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p02Ke.90338$mC.89151@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <dd9so2$eql$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dd9so2$eql$1@panix5.panix.com...
> In article <3lql6iF12jsntU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> DD

In my f-o-r, I've never met a tail strong enough to wag the earth.

By the way, I think Einstein was somewhat against the Nazis.....I also think 
he aimed to disprove Quirk's exception.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-09T09:26:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddaatk$f6b$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <dd9so2$eql$1@panix5.panix.com> <p02Ke.90338$mC.89151@tornado.tampabay.rr.com>`

```
In article <p02Ke.90338$mC.89151@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dd9so2$eql$1@panix5.panix.com...
>> In article <3lql6iF12jsntU1@individual.net>,
…[16 more quoted lines elided]…
>In my f-o-r, I've never met a tail strong enough to wag the earth.

It's been said that there are things in Heaven and on Earth not dreamt of 
in your philosophies, Horatio... tune in next week when, perhaps, we might 
deal with events preceding their causes!

>
>By the way, I think Einstein was somewhat against the Nazis.....I also think 
>he aimed to disprove Quirk's exception.

Curious how you think his goal was to disprove something that happened 
some decades after his demise... maybe we are dealing with 'events 
preceding their causes' before we have cause to deal with such an event.

DD
```

###### ↳ ↳ ↳ [OT] Quirks Exception and Einstein

_(reply depth: 31)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-09T14:55:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lt3Ke.90347$mC.2836@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <dd9so2$eql$1@panix5.panix.com> <p02Ke.90338$mC.89151@tornado.tampabay.rr.com> <ddaatk$f6b$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:ddaatk$f6b$1@panix5.panix.com...
> In article <p02Ke.90338$mC.89151@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[36 more quoted lines elided]…
>
I didn't say what universe was in play. Quantum immortality RULZ!
In this universe, his bagels are great.

JCE
```

###### ↳ ↳ ↳ Re: [OT] Quirks Exception and Einstein

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-09T11:32:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddaia5$kfv$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <p02Ke.90338$mC.89151@tornado.tampabay.rr.com> <ddaatk$f6b$1@panix5.panix.com> <lt3Ke.90347$mC.2836@tornado.tampabay.rr.com>`

```
In article <lt3Ke.90347$mC.2836@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:ddaatk$f6b$1@panix5.panix.com...
>> In article <p02Ke.90338$mC.89151@tornado.tampabay.rr.com>,
>> jce <defaultuser@hotmail.com> wrote:

[snip]

>>>By the way, I think Einstein was somewhat against the Nazis.....I also 
>>>think he aimed to disprove Quirk's exception.
…[5 more quoted lines elided]…
>I didn't say what universe was in play.

No need to, it was already known... just as it is already known which 
people equate 'it is' with 'I believe it is'.

>Quantum immortality RULZ!

Them as says 'RULZ' usually droolz.

>In this universe, his bagels are great.

To paraphrase Callimachus, then... mega bagelion, mega kalon.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T13:20:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lt32tF13uqsrU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <dd9so2$eql$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dd9so2$eql$1@panix5.panix.com...
> In article <3lql6iF12jsntU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[12 more quoted lines elided]…
>
Funny you should say that, Doc...

Exactly that thought occurred to me when I wrote it... :-)

For the purpose of this discussion, I let it stand...:-) (I think it is fair 
to assume that the consciousness resides in the dog and not in its tail, so 
the the dog's frame of reference is the important one here.)

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T05:07:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddcg3r$scd$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <dd9so2$eql$1@panix5.panix.com> <3lt32tF13uqsrU1@individual.net>`

```
In article <3lt32tF13uqsrU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:dd9so2$eql$1@panix5.panix.com...
…[17 more quoted lines elided]…
>Exactly that thought occurred to me when I wrote it... :-)

Oh good... some say that self-awareness and acknowledgment are a first 
step!

>
>For the purpose of this discussion, I let it stand...:-) (I think it is fair 
>to assume that the consciousness resides in the dog and not in its tail, so 
>the the dog's frame of reference is the important one here.)

I think it is fair to assume as little as possible, since assumptions can 
lead to agreement and thence to facts (or so some say)... and who wants 
too many of those cluttering up the landscape?

DD
```

###### ↳ ↳ ↳ OT: Authorities

_(reply depth: 28)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-09T13:33:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddabak$581$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net>`

```

On  8-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> Thus words are symbols that allow us to share perception and 'create'
> reality. The danger is that the "word authority" (Dictionaries) become an
…[6 more quoted lines elided]…
> Authority" is risky at best.

Some people prefer the function of dictionaries to act as authorities.   Heck,
at least one country does this.

Authorities are comfortable - if you know what is right, you don't have to
think, and certainly don't need to understand.

One trouble with dictionaries is that they don't adequately show context - look
up "database" and see what the general public thinks of this word compared to
what programmers use.   Or learn why someone says "evolution is only a theory".
  Authority has scope, and authoritarians don't want scope.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 29)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-09T15:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddabak$581$1@peabody.colorado.edu...
>
> On  8-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[15 more quoted lines elided]…
> at least one country does this.
One president was famous for trying his luck with with this.

"I did not have sexual relations with that woman, Ms. Lewinsky." 
(Washington, D.C., January 26, 1998)"

I have never checked before but I think we would find him vindicated if we 
used m-w as the authority...but then what fun would that be.

http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=sexual+relations&x=18&y=19

> Authorities are comfortable - if you know what is right, you don't have to
> think, and certainly don't need to understand.
…[5 more quoted lines elided]…
> what programmers use.
I'll never forget the Dilbert when the pointy haired boss wanted a 
blindingly super database..."what color do you want that database?"

"...I think mauve has the most RAM"

Point is, I don't even have to look as far as the general public ;-)

>  Or learn why someone says "evolution is only a theory".
>  Authority has scope, and authoritarians don't want scope.

People can say evolution is only a theory, because it is a theory.  People 
say it because of the other scope creep...we as a group generally cannot 
separate evolution from "in the beginning...."

JCE
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T13:55:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lt540F14aoejU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message 
news:gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com...
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:ddabak$581$1@peabody.colorado.edu...
…[29 more quoted lines elided]…
>

I was stunned at this...

Using that definition, what he said was true. (I owe him an apology; always 
considered he simply lied. Now it turns out he was using MW as his 
authority...)

But the general consensus is that "sexual relations" includes more than 
"physical union of male and female genitalia accompanied by rhythmic 
movements usually leading to the ejaculation of semen from the penis into 
the female reproductive tract; also : INTERCOURSE 3 -- compare ORGASM"

So, it could be argued that if the movement is not rhythmic, no "sexual 
relations" occurred... or if the semen end up on the blue dress, or 
somewhere else :-)

Could a rapist use authority to get off in this way? It is a frightening 
thought.

When meaning is restricted to authority only, and context is ignored, 
loopholes become apparent.


>> Authorities are comfortable - if you know what is right, you don't have 
>> to
>> think, and certainly don't need to understand.
>>
I agree.

>> One trouble with dictionaries is that they don't adequately show 
>> context - look
…[13 more quoted lines elided]…
> People can say evolution is only a theory, because it is a theory.

Yes, inserting 'only' into the statement weakens it considerably. A theory 
may be well proven, and may never have failed to accurately predict 
phenomena, but saying it is 'only' a theory, diminishes it.

> say it because of the other scope creep...we as a group generally cannot 
> separate evolution from "in the beginning...."
>
> JCE
>
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-10T11:57:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dddio3$1qma$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3lt540F14aoejU1@individual.net...

> I was stunned at this...
>
> Using that definition, what he said was true. (I owe him an apology;
always
> considered he simply lied. Now it turns out he was using MW as his
> authority...)

Hm.  I always understood "engaging in sexual activity" or "having sex" with
someone as being quite a bit broader and less specific than "having sexual
relations" with someone.  Both the Eighth and Ninth M-W  New CollegiateS
simply have "coitus" as the sole definition for "sexual relations", and such
I have always understood it.   I happen to think he did "have sex with that
woman", but did not "have sexual relations with that woman".   Does that
mean he was faithful to his wife?  Uh ... no ... I don't think so, not in
the sense I understand it.  But I think he told the *precise* truth.

> But the general consensus is that "sexual relations" includes more than
<substitute the definition from "coitus"> ...

Well, that's where we differ.  There are lots of euphemisms for various
specific sexual activities, and lots of euphemisms for sexual activity taken
as a category, and I have always understood the term "sexual relations" to
fall into the former category and not the latter.

> Could a rapist use authority to get off in this way? It is a frightening
> thought.

Might, if the law were written such that *only* forcing someone to engage in
"sexual relations" was forbidden, rather than a broader term.

> When meaning is restricted to authority only, and context is ignored,
> loopholes become apparent.

It's not a matter of authority, it's a matter of taking the trouble to use a
term in a way that is best understood by the broadest audience.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-10T12:02:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dddj1b$1qq9$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <dddio3$1qma$1@si05.rsvl.unisys.com>`

```
Pete wrote:

> > Could a rapist use authority to get off in this way? It is a frightening
> > thought.

I responded:

> Might, if the law were written such that *only* forcing someone to engage
in
> "sexual relations" was forbidden, rather than a broader term.

A broader term, perhaps, but more likely a list of specific terms for
various sexual activities, which is, I believe, the way most such laws are
written.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T19:19:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dddk0a$288$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <dddio3$1qma$1@si05.rsvl.unisys.com>`

```

On 10-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> Hm.  I always understood "engaging in sexual activity" or "having sex" with
> someone as being quite a bit broader and less specific than "having sexual
…[5 more quoted lines elided]…
> the sense I understand it.  But I think he told the *precise* truth.

Interesting.  My use of those words are just the opposite of yours.   Which
means that definitions need to be agreed upon (even if people laugh at such when
the President did so).


> > Could a rapist use authority to get off in this way? It is a frightening
> > thought.
>
> Might, if the law were written such that *only* forcing someone to engage in
> "sexual relations" was forbidden, rather than a broader term.

Speaking of language again - there's a common practice of expanding a word to
include what we want included.    One word that becomes weakened this way is
"rape".   Another is "terrorism".


> It's not a matter of authority, it's a matter of taking the trouble to use a
> term in a way that is best understood by the broadest audience.

Don't assume that any particular individual or subgroup understands though.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-10T19:15:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET>`
- **In-Reply-To:** `<3lt540F14aoejU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net>`

```
Pete Dashwood wrote:
> "jce" <defaultuser@hotmail.com> wrote in message 
> news:gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com...
…[15 more quoted lines elided]…
> authority...)

He *did* lie - don't let him off that easily...  His trashing of many 
decent things in this country, just to try to prove his innocence when 
he was, in fact, guilty, is something from which our culture will never 
recover.

"That depends on what the meaning of 'is' is" - ridiculous!  Own up to 
the fact that you got head from someone and move on.  When he started 
lying about it, while under oath, he crossed into the realm of perjury, 
which is an impeachable offense.

His legacy won't be rehabilitated that easily...
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-11T04:21:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET>`

```
"LX-i" <lxi0007@netscape.net> wrote in message 
news:c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET...
> Pete Dashwood wrote:
>> "jce" <defaultuser@hotmail.com> wrote in message 
…[21 more quoted lines elided]…
> recover.

We've recovered from world wars, civil wars, racism, assassinations. We've 
blown up Iraq, we've blown up Hiroshima, we've had planes crash into 
buildings....but never will we culturally recover from the indignity of a 
man getting a blow job.

He *did* lie...I think there is precedence for lying in the whitehouse.

JCE
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T19:04:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b18df$42fd3912$45491c57$20026@KNOLOGY.NET>`
- **In-Reply-To:** `<7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET> <7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>`

```
jce wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET...
…[32 more quoted lines elided]…
> man getting a blow job.

Did I say anything about the blow job?  He basically snubbed his nose at 
the very law that he was sworn to protect.  And, remember, it's not like 
he was the president of some po-dunk 5th world country - he was the POTUS!

> He *did* lie...I think there is precedence for lying in the whitehouse.

And continuing to lie?  Frittering away taxpayer money by lying in 
defense of yourself?  The 5th Amendment says you can't be compelled to 
incriminate yourself - it doesn't say you get to make something else up 
instead.  That's got its own name - perjury.  And *that* is the negative 
angle that I feel our culture will have a tough time recovering from.

And, not to revamp the whole political thing, but we didn't have to 
*recover* from Hiroshima - it saved lives.  Ditto for Iraq.  We're 
*still* not over the planes crashing into the buildings.  Did you hear 
this week that now we find out that folks in DoD *knew* that Mohammed 
Atta and four other 9/11 terrorists were part of a Brooklyn al-Qaeda 
cell, but couldn't share that info with the FBI because of a Clinton-era 
"wall of separation"?

But hey - Romans 8:28 is still in the book.  Because of this failure, 
and the resultant strike, there are two terror strongholds gone, and the 
remainder of the international Islamic terrorist network is on the run. 
  They're desperate, they're losing, and they know it.  Maybe I 
shouldn't have used the word "never," but it's still going to be a long, 
long time recovering from that.

Your view may vary...
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-14T12:27:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-4FC2D1.12270614082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET> <7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>`

```
In article <7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>,
 "jce" <defaultuser@hotmail.com> wrote:

> > He *did* lie - don't let him off that easily...  His trashing of many 
> > decent things in this country, just to try to prove his innocence when he 
…[10 more quoted lines elided]…
>jce

Other presidents have committed perjury when indicted under laws they 
themselves lobbied for and signed?

Which presidents prior to WJB Clinton established such a precedent?
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-14T19:12:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xIMLe.14374$Oy2.7696@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <3lt540F14aoejU1@individual.net> <c0ab8$42fa98aa$45491c57$7260@KNOLOGY.NET> <7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com> <joe_zitzelberger-4FC2D1.12270614082005@ispnews.usenetserver.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-4FC2D1.12270614082005@ispnews.usenetserver.com...
> In article <7nAKe.6473$dJ5.4325@tornado.tampabay.rr.com>,
> "jce" <defaultuser@hotmail.com> wrote:
…[19 more quoted lines elided]…
> Which presidents prior to WJB Clinton established such a precedent?
All I said was that as a president he lied.  I said he wasn't the first.

On a tombstone:
"Here lies Richard Nixon (so, what else is new?)"

JCE
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 30)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-11T16:23:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123802638.351773.266220@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com>`

```
Or perhaps we could say that the entirety of the Bible is theory?

A recent Guardian article points out that the Intelligent Designer, so
beloved of GWB, was not overly intelligent in it's designs (after all,
why design the human being as an imperfectly evolved creature poorly
suited to bipedal gaits?).
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T19:11:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e6a4$42fd3a9e$45491c57$20026@KNOLOGY.NET>`
- **In-Reply-To:** `<1123802638.351773.266220@o13g2000cwo.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <gO3Ke.41155$iG6.9102@tornado.tampabay.rr.com> <1123802638.351773.266220@o13g2000cwo.googlegroups.com>`

```
Alistair wrote:
> Or perhaps we could say that the entirety of the Bible is theory?
> 
…[3 more quoted lines elided]…
> suited to bipedal gaits?).

If you read the Good Book, you'll see that this wasn't the original 
state of the creation...
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 29)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-09T14:00:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123621207.166429.68760@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<ddabak$581$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu>`

```
> Or learn why someone says "evolution is only a theory".

That is like saying "Gravity is only a theory".

Evolution is observable (except to those that seek 'enlightenment' on
their knees with their eyes closed), 'Natural Selection as the main
driving force of evolution' is a theory, 'Sexual selection as the main
driving force of evolution' is a theory. 'Neanderthals were a
sub-species of Homo Erectus' is a theory.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-09T17:12:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3084$42f92a35$45491c57$13663@KNOLOGY.NET>`
- **In-Reply-To:** `<1123621207.166429.68760@g49g2000cwa.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com>`

```
Richard wrote:
>>Or learn why someone says "evolution is only a theory".
> 
…[3 more quoted lines elided]…
> Evolution is observable

How so?  I've observed gravity many times, and I've observed the slow 
animal being eaten.  It doesn't mean I extrapolate that to come up with 
my own ideas of how this world came to be - especially since all the 
"proof" I've ever seen for that theory is based on shoddy or 
now-discredited science (aka "junk science").
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T14:02:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lt5gsF145mpmU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:b3084$42f92a35$45491c57$13663@KNOLOGY.NET...
> Richard wrote:
>>>Or learn why someone says "evolution is only a theory".
…[10 more quoted lines elided]…
> science (aka "junk science").

Dan, I know this is sensitive and I have utmost respect for your beliefs and 
your right to believe them. But I feel pretty strongly about the Scientific 
approach so I would be very interested to see what, in your opinion, 
constitutes "junk science". Not looking for trouble, have no intention of 
starting another religious debate, but, if you have the same respect for my 
beliefs that I have for yours, you might post a link. Do it privately, if 
you'd prefer.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 31)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-09T20:46:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123645561.235262.32580@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<b3084$42f92a35$45491c57$13663@KNOLOGY.NET>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET>`

```
>> Evolution is observable

> How so?

It is observable by anyone who's mind is not shut tight and locked up.

For example a few thousand years ago there were only a very small
number of breeds of dog. Now there are hundreds of them.  That is
evolution, but it is not 'natural selection' because it is primarily
'artificial selection'.

> It doesn't mean I extrapolate that to come up with
> my own ideas ....

I very much doubt that you have _any_ 'my own ideas', you seem to only
have ideas that you have been indoctrinated with and by reading 'the
book'.

> all the "proof" I've ever seen for that theory ..

Demonstrating that you completely fail to understand what science is
and what 'theory' is and what would happen if there was 'proof'.

> is based on shoddy or now-discredited science
> (aka "junk science").

And your thoughts on 'creation science' [sic] would be ?
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 32)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-10T06:41:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3khKe.4343$dJ5.2758@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <1123645561.235262.32580@g49g2000cwa.googlegroups.com>`

```
I _may_ be wrong...it happens less in real life than it appears in CLC...but 
nonetheless

<DISCLAIMER - this has the potential to be all completely bullshit. Best 
case is just an opinion>

I think my other post stands...

The failure of discussion with evolution is that we as a group of 
ape-descended humans cannot separate evolution from "in the beginning...."

Evolution <> Anti-Creationism......Why can't there be many theories....Why 
does it matter what was there before the beginning?  As a famous voice box 
said once...it's like asking what's north of the north pole.

Despite what "anti creationists" say, creationism is not your apple pie view 
of: there was Adam and there was Eve and there were many incestuous unions 
leading to you and I.....there are Gap Creationists, and Old Earth, Flat 
Earthers and even Progressive Creationists (I kid you not).

Similarly, despite what "anti evolutionarists" say there is evidence to 
support the theory that has been seen in a single generation. I don't 
understand why we cannot just say God invented evolution and it's not 
random..and just all get along.

I do suggest you go to Talk.Origins if you want to continue the debate 
though...they have forums to discuss this kind of crap.

Besides, the proof for God is far more solid than the junk science proving 
...well, pretty much anything else actually - I read it somewhere...the name 
of the book escapes me.  It's either Old something or New something, I 
forget.

JCE

Top Post Only

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1123645561.235262.32580@g49g2000cwa.googlegroups.com...
>>> Evolution is observable
>
…[24 more quoted lines elided]…
> And your thoughts on 'creation science' [sic] would be ?
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 33)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-10T01:13:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123661617.794438.163150@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3khKe.4343$dJ5.2758@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <3khKe.4343$dJ5.2758@tornado.tampabay.rr.com>`

```
> there are Gap Creationists, and Old Earth, Flat
> Earthers and even Progressive Creationists (I kid you
> not).

And Brahmans, and Maidu Indian Wonomians, and Chiminigaguans, and
Awonawilonans and Gaiaists, and dozens or hundreds of other myth
believers. Or perhaps it was Xenu and the Thetans.

> the proof for God is far more solid ...

Oh I believe in gods, all of them (well most anyway), Khonvum, Chin,
Herohito, Zeus, Rama, ... I just don't deify them, they were chiefs,
warlords, generals. It is very likely that some Moses met some Jehovah
maybe even on a mountain. Jehovah was the local warlord and granted the
Jews some land.

Interestingly, Jehovah (or Yehwah) was, according to the Caananites,
the son of their 'god' El and brother to Baalim, the first of the
dynasty of the Baal family (of which Baal Zebub was one).

> I don't understand why we cannot just say God invented
> evolution and it's not random.

No, you probably don't understand that.

Why don't we all just say: "Before anything , there existed Shuzanghu
and his wife, Zumaing-Nui. In time she gave birth to a girl (earth) and
a boy (sky). Sky and earth mated and gave birth to the mountains. Then
they produced two frogs who married and made the first humans. These
humans were covered with thick hair, but when they mated they produced
people as they are now." and just all get along ?

> I read it somewhere...the name of the book escapes me.

Perhaps you should read somewhat wider.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T05:18:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddcgq1$6c9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com>`

```
In article <1123661617.794438.163150@g43g2000cwa.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:

[snip]

>Why don't we all just say: "Before anything , there existed Shuzanghu
>and his wife, Zumaing-Nui.

Ummmmm... because it posits a conditon prior to existence ('before 
anything') when things existed?  Because it posits time ('before') in 
the absence of the possibility of motion?  Because 'we all' don't share a 
common language and a bit of a racket might result?

Oh... you're talking about *religion*, here, not logic... sorry, my 
apologies... I'll go back to pondering how it is that a reptile without 
voice-mechanisms can speak - and share a common language with - human 
beings.

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-10T02:33:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123666388.477013.136680@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<ddcgq1$6c9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com> <ddcgq1$6c9$1@panix5.panix.com>`

```
> I'll go back to pondering how ...
> and share a common language with - human beings.

Was that some pre-Babel language or is it that "If English was good
enough for Jesus, it's good enough for Texas."* ?

That would of course be the King's English as spoken by 'The King of
England'.




* Texas governor Miriam "Ma" Ferguson picked up a Bible and famously
declared, "If
English was good enough for Jesus Christ, it's good enough for Texas."
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T05:42:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddci6b$pa2$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com> <ddcgq1$6c9$1@panix5.panix.com> <1123666388.477013.136680@f14g2000cwb.googlegroups.com>`

```
In article <1123666388.477013.136680@f14g2000cwb.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>> I'll go back to pondering how ...
>> and share a common language with - human beings.
>
>Was that some pre-Babel language or is it that "If English was good
>enough for Jesus, it's good enough for Texas."* ?

I wasn't dere, Charlie... but the earliest versions I've see report it in 
some form of proto-Aramaic.

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-10T13:59:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2LnKe.3899$Oy2.3795@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <3khKe.4343$dJ5.2758@tornado.tampabay.rr.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1123661617.794438.163150@g43g2000cwa.googlegroups.com...
>> there are Gap Creationists, and Old Earth, Flat
>> Earthers and even Progressive Creationists (I kid you
…[12 more quoted lines elided]…
> Jews some land.
Well that's one view....just as Jesus was a prophet who stained his 
sheets...

> Interestingly, Jehovah (or Yehwah) was, according to the Caananites,
> the son of their 'god' El and brother to Baalim, the first of the
…[5 more quoted lines elided]…
> No, you probably don't understand that.
I'm glad you understood the words "I don't understand".  I hope you didn't 
need a commonly accepted source of information to help you there :-)

> Why don't we all just say: "Before anything , there existed Shuzanghu
> and his wife, Zumaing-Nui. In time she gave birth to a girl (earth) and
…[3 more quoted lines elided]…
> people as they are now." and just all get along ?
Exactly!  Now you're getting it. It's amazing how hard this concept is for 
some to grasp.

>> I read it somewhere...the name of the book escapes me.
> Perhaps you should read somewhat wider.
Perhaps.

JCE
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T14:33:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd37n$moh$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com>`

```

On 10-Aug-2005, "Richard" <riplin@Azonic.co.nz> wrote:

> > the proof for God is far more solid ...
>
…[4 more quoted lines elided]…
> Jews some land.

Just show me proof that the Hindus (or even Muslims) are wrong.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-11T16:32:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123803120.381308.170190@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1123661617.794438.163150@g43g2000cwa.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <3khKe.4343$dJ5.2758@tornado.tampabay.rr.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com>`

```
I could almost swallow this theory but for the incestuous aspect of it.
What religion do Zumaing-Nui, etc., derive from?
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-11T17:52:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123807962.998060.115160@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123803120.381308.170190@z14g2000cwz.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <3khKe.4343$dJ5.2758@tornado.tampabay.rr.com> <1123661617.794438.163150@g43g2000cwa.googlegroups.com> <1123803120.381308.170190@z14g2000cwz.googlegroups.com>`

```
> Zumaing-Nui

Non Hindu northern India.

The point being that american fundementalists seem to consider that
'creationism' is only that of the bible and everyone else's are just
ignorant pagan myths. All these myths are very territorial with the
biblical one coming from a small area at the eastern end of the med.,
other territories have their own, probably based on deification of
their own charasmatic leaders of the past.

The process can be identified quite easily: see how locals write about
Idi Amin, or the Kim dynasty, or Pol Pot. These too may one day become
gods just as Chin and Herohito did.

I was stuuned to see in a documentary about 'the unnamable German
leader' with film and writings of the time how he was regarded as
god-like, even with comments that 'he created the world'.

It seems that people will believe almost anything, especially if they
are indoctrinated at an early age, or there is a purported benefit. If
you really believe in the Tooth Fairy or in Santa Claus, and are good,
then you will get a reward later. Well Santa Claus is just a deified
Saint Nicolas, Bishop of Myra, given supernatural powers and painted by
CocaCola.

I've been reading up about the Rastafarians recently. My grandfather
was in the Indian Army and in 1922 was presented with a Lion skin in
Aden by Tafari Makonnen which my father remembers as hanging on the
wall in the house. That would be valuable now, but it was thrown out as
being moth eaten decades ago.

"""According to Rastafarian belief the only true God is the late
Ethiopian emperor Haile Selassie (originally known as Ras Tafari), and
Ethiopia is the true Zion."""

I see little or no difference between Rastafarians deifying one leader
and Jews 3 and a half thousand years ago doing that to theirs.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 36)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-12T13:41:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddi8v1$nf9$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com>`

```

On 11-Aug-2005, "Richard" <riplin@Azonic.co.nz> wrote:

> The point being that american fundementalists seem to consider that
> 'creationism' is only that of the bible and everyone else's are just
…[3 more quoted lines elided]…
> their own charasmatic leaders of the past.

There is a subset of American fundamentalists who point to the fact that a wide
variety of peoples have legends of great floods as support of the Noah story.
The problem with this is that it is evidence of a wide variety of peoples
*surviving* great flood(s).  This means (if those floods are, in fact THE
FLOOD), that the Noah flood did *not* kill everybody in the world except for one
Jewish family - at least not by the definition of "world" that the literalists
demand that we accept.

So many people know that their interpretation of the Scriptures is correct, and
that others are manifestly wrong, that they only read to confirm what they
already Know and are unwilling to learn what God wants.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 37)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-12T08:55:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddigoi$1ou6$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:ddi8v1$nf9$1@peabody.colorado.edu...

> There is a subset of American fundamentalists who point to the fact that a
wide
> variety of peoples have legends of great floods as support of the Noah
story.
> The problem with this is that it is evidence of a wide variety of peoples
> *surviving* great flood(s).  This means (if those floods are, in fact THE
> FLOOD), that the Noah flood did *not* kill everybody in the world except
for one
> Jewish family - at least not by the definition of "world" that the
literalists
> demand that we accept.

See the article at http://en.wikipedia.org/wiki/Black_Sea_deluge_theory .  I
recall an expedition to detect evidence of human habitation at the old
shoreline (supporting the idea that this was really Noah's Flood, covering
all the world the tellers of the story knew about),, but it came up empty.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 38)_

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-08-12T11:32:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in
news:ddigoi$1ou6$1@si05.rsvl.unisys.com: 

> 
> "Howard Brazee" <howard@brazee.net> wrote in message
…[26 more quoted lines elided]…
> 

    	If you want a world wide flood, how about the end of the last ice 
age, when the ocean rose as the ice melted.  All of the people that lived 
close to the ocean would have seen this as a flood, albeit a slow flood.

    	And for local floods, they say that their was a huge lake, west of 
the current great lakes and much larger that was created by a great ice 
dam.  When the ice dam broke, their was one of the largest floods in known 
history.

    	I am sure that their must be many other examples.  Was the 
mediterranean sea ever dry?  There is some evidence that it might have been 
dry at one time.  Might have been a LONG time ago though.

    	I do agree that the black sea flood has the best chance of being the 
biblical flood - it happened in the right place at the right time, and 
would have been very fast, but not so fast that you could not survive.  As 
with most "Holy books", it is ultimately local, not global.  Without modern 
communications, this is not surprising.  

    	If you want a non survivable flood in that era and area, I believe 
that an island blew up a la Krakatoa.  Destroyed a nice civilization.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 39)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-12T16:49:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddijun$t4e$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com> <Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`

```

On 12-Aug-2005, Russell <rws0203nospam@comcast.net> wrote:

>     	If you want a non survivable flood in that era and area, I believe
> that an island blew up a la Krakatoa.  Destroyed a nice civilization.

The point isn't whether or not there was a Noah's flood - it's that some people
want to have it's definition of destroying everybody except Noah's family to be
everybody on the planet Earth.   So evidence of partial floods and remembered
floods doesn't support their pre-conceived beliefs.   Which doesn't matter if
their beliefs are strong enough.    These don't seek Truth,they already Know it.

On the other hand, there are many people who believe there is Truth in the
Scriptures - but don't have the conceit that they have the One True
Interpretation of how to read everything in the Bible - which parts don't matter
anymore - which parts are literal.  These people are willing to learn.


Same thing happens with other religions such as Islam and Patriotism.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 39)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-12T12:59:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123876774.923643.248360@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com> <Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`

```
> If you want a non survivable flood in that era and
> area, I believe that an island blew up a la Krakatoa.
> Destroyed a nice civilization.

Thera, now called Santorini.  It blew up around 1650 BCE several times
larger than Krakatoa. We have a large picture of it on the wall since
my daughter did her Greek Islands trip. The island is just a crater rim
now.

It has nothing to do with floods. However, it is estimated that the 70
km high blast would have been visible from northern Egypt as a 'pillar
of fire' and the ash and dust clouds would have given several days of
dark, though I doubt the 'sun stood still'. The ash fallout would have
turned water red and killed fish in the rivers and streams and lots of
dead fish would have led to much more than usual fly breeding which, in
turn, would have been food for an abundance of frogs (also the fish
were not there to eat the tadpoles).

It is also likely that this is Plato's Atlantis, not 9000 years before
500 BCE but 900 (or so).

As for the flood there are many examples of local flooding that may be
dragged in. However it is more likely that it was an exlanation of the
world as they found it. In the moutains one can find fossils of fish
and, especially, shell fish. We now know that this is the result of
tectonic plates meeting and scraping the seabed into piles, and
especially at subduction zones. As The African plate moves north into
Europe it pushes up the Alps and causes volcanoism through Italy,
Greece and Turkey.

The peoples of the time had no idea about plate techtonics so, instead
of the land now being pushed up above sea level, their explanation was
that sea level must have been somewhere up the mountains at some point
so that the fish as shell fish could be buried there.

That is: they came up with an early scientific theory to explain the
evidence of the fossils they saw about how they came to be there. As
often happens some stories were woven from local flood experiences and
new ideas.

The theory changed when more detailed studies showed that over millions
of years the land moved and folded. Tectonic plates were shown to be
one of the mechanisms involved, I recall following the arguments each
way in New Scientist in the 60s. Now they can measure the movements in
millimetres.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 40)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-12T14:43:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddj56m$250s$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com> <Xns96B07FA08B030rws0203comcastnet@216.196.97.131> <1123876774.923643.248360@g47g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1123876774.923643.248360@g47g2000cwa.googlegroups.com...

> The theory changed when more detailed studies showed that over millions
> of years the land moved and folded.

Impossible!  *Everybody* knows the Universe was created at what would have
correspond to the nightfall immediately preceding Sunday, October 23, 4004BC
had there been light (or, for that matter, days and nights) at the time.
;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 41)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-13T00:04:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WNaLe.7449$dJ5.6627@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com> <Xns96B07FA08B030rws0203comcastnet@216.196.97.131> <1123876774.923643.248360@g47g2000cwa.googlegroups.com> <ddj56m$250s$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:ddj56m$250s$1@si05.rsvl.unisys.com...
>
> "Richard" <riplin@Azonic.co.nz> wrote in message
…[11 more quoted lines elided]…
>    -Chuck Stevens

Actually, *everybody* knows that it would have been exactly 10^-43 seconds 
after that moment you specify. And not a smidgeon sooner.

JCE
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 39)_

- **From:** icycalmca@yahoo.com
- **Date:** 2005-08-12T15:59:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123887571.727888.133420@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <ddigoi$1ou6$1@si05.rsvl.unisys.com> <Xns96B07FA08B030rws0203comcastnet@216.196.97.131>`

```

Russell wrote:
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in
> news:ddigoi$1ou6$1@si05.rsvl.unisys.com:
<snip>
> > See the article at
> > http://en.wikipedia.org/wiki/Black_Sea_deluge_theory .  I recall an
…[4 more quoted lines elided]…
> >     -Chuck Stevens

  Not "empty" at first announcement, but soon after
the National Geographic trumpeted their supposed success.

  Note that that National Geographic site has not
been updated for about five years,
e.g. no mention of the refutations of the hypothesis,
and no mention of the disappointing 200-year-old date
for the supposed "habitation site", and no mention
that Ballard didn't revisit the site when he went
back to the Black Sea to look at submerged shipwrecks
again.

http://www.nationalgeographic.com/blacksea/ax/frame.html

>     	If you want a world wide flood, how about the end of the last ice
> age, when the ocean rose as the ice melted.  All of the people that lived
> close to the ocean would have seen this as a flood, albeit a slow flood.

  Agreed.

>     	And for local floods, they say that their was a huge lake, west of
> the current great lakes and much larger that was created by a great ice
> dam.  When the ice dam broke, their was one of the largest floods in known
> history.

  That would be one of the (recurrent) floods that carved
the Channelled Scablands in Washington, as Glacial Lake Missoula
broke through the glacial ice tongue damming its outlet valley:

http://www.sentex.net/~tcc/scabland.html

http://users.aber.ac.uk/daa04/scab.htm

http://www.talkorigins.org/faqs/icr-visit/bartelt5.html

>     	I am sure that their must be many other examples.  Was the
> mediterranean sea ever dry?  There is some evidence that it might have been
> dry at one time.  Might have been a LONG time ago though.

  The last time was 5.4 million years ago:

http://earth.leeds.ac.uk/tectonics/messinian/history.htm

>     	I do agree that the black sea flood has the best chance of being the
> biblical flood - it happened in the right place at the right time, and
…[5 more quoted lines elided]…
> that an island blew up a la Krakatoa.  Destroyed a nice civilization.

  That was Santorini:

http://www.geology.sdsu.edu/how_volcanoes_work/santorini.html

  Re: the BSFloode, please allow me to grace you with
my standard rant on this subject:


  Those who came up with the claim of catastrophic flooding
of the Black Sea have retreated from that claim.
  It was based on the "sudden" appearance of salt-water shelly
organisms deep in the Black Sea, but the claimants now agree
that the "sudden" immigration of such shells just marks a change
from freshwater to salty water deep below the surface of the Black
Sea, and didn't involve any change in the level of the surface of
the Black Sea, i.e. it does not mark any "flooding" of the Black
Sea at all. And there is abundant evidence that at the time of
the supposed "BSFlood" the level of the Black Sea was the same as,
or higher than, the level of the Mediterranean Sea (which was
supposed to have broken through an imaginary dam in the Bosphorus
and overflowed into the Black sea basin). Ergo, the Black Sea was
overflowing into the Mediterranean Sea at the time of the supposed
"catastrophic flood", i.e., the water was actually flowing in the
opposite direction.
  Ryan and Pitman got it backwards. At best.

<ENGAGE RANT MODE>

  Sorry, there was no sudden flood in the Black Sea basin.
It was all a publicist's dream.

  Parts of the modern Black Sea Flood claim are total
fantasy, like the imaginary dam that supposedly broke
7500 years ago. Somebody wrote that down, and suddenly
it was established as a "fact".

  The trouble is, altogether too many people have the
mistaken idea that a catastrophic flood in the Black
Sea was the inspiration for the Noah's Flood story in
the Bible.
  The TV programs on that topic are outdated and overly
sensational and can be safely ignored.

  Sadly, you, and maybe millions of other people,
have been misled on this subject.

  Alas, there was no "Noachian" Black Sea Flood, and
the science in William Ryan's and Walter Pitman's book
"Noah's Flood: the event that changed history" has in
several cases been superceded by better information that
indicates that there was no such event, and was in most
cases preceded by evidence that indicated that there was
no such event.
  Ryan and Pitman set out to overturn the orthodox view
of the history of the Black Sea, but they have apparently
abandoned their hypothesis, if more recent articles
co-authored by Ryan are any indication.
  The orthodox view has prevailed, subject to some recent
modifications.

  There is evidence that there was an _outflow_ southward
from the Black Sea through the Bosphorus into the
Mediterranean from more than 10000 years ago
(well before Ryan and Pitman's initial 5600 BCE flood date),
continuously until the present day, though there may have
been a relatively short interruption.
  And evidence from the south shore of the Black sea shows
that the level of the Black Sea was only 18 m below the
present level at the time of the supposed flood.
  The more recent claim by Ryan puts the flood date at
8400 BP, or about 9000 years ago, but then the "floodwaters"
through the Bosphorus channel would have been only about
5 metres deep.   9000 years ago is when everybody else
always thought that Mediterranean saltwater first entered
the Black Sea. At about that time, the last phase of
Glacial Lake Agassiz, in central Canada, finally found an
outlet to the sea through or under the remnants of the
Laurentide Ice Sheet, and so out into the North Atlantic,
raising sea level an appreciable amount, and _perhaps_
triggering a sudden inflow of saltwater into the Black Sea
basin.
  But probably not sudden or great enough to inspire a
Noachian Flood myth.
  Better candidates are widespread inundation of low-lying
parts of the Persian Gulf associated with the final draining
of Glacial Lake Agassiz, and similar flooding of the Tigris-
Euphrates delta, and (most likely) simultaneous flooding of
the Tigris and Euphrates, which would have looked like a
flooding of the entire world from the viewpoint of a person
near present-day Baghdad. These candidates could each or all
have inspired the flood myth in the epic of Gilgamesh, which
predates the first known appearance of the Noachian Flood myth.

  Check this out, for a layman-friendly synopsis of the
refutation:

http://home.entouch.net/dmd/bs⑬⑬⑬eaflod.htm

  On the draining of Glacial Lake Agassiz:

http://tinyurl.com/csmaq

  And here's a fairly recent news item on refutation of
Ryan's and Pitman's hypothesis:

<BEGIN QUOTE>
January 14, 2003

Scientists are seriously challenging a recent, fascinating
proposal that Noah's epic story -- setting sail with an ark
jam-full of animal couples -- was based on an actual
catastrophic flood that suddenly filled the Black Sea 7,500
years ago, forcing people to flee.

In a detailed new look at the rocks, sediments, currents
and seashells in and around the Black Sea, an international
research team pooh-poohs the Noah flood idea, arguing that
all the geologic, hydrologic and biologic signs are wrong.

Little that the earth can tell us seems to fit the Noah story,
they say. The new research takes direct aim at the work of
two Columbia University geologists -- William Ryan and Walter
Pitman -- whose proposal in 1997 ignited much new interest,
and much new research, into Middle East history and geology.

<END QUOTE>

  Also, Ballard did not find Noah's House, and he has recently
admitted that he didn't find any evidence of human occupation
of the Black Sea continental shelf, let alone any support for
the BSFlood hypothesis.
  Here is another recent news article telling you about that
(please be warned that several statements in the article
are erroneous, e.g.
"Scholars agree the Black Sea flooded when
rising world sea levels caused the Mediterranean to
burst over land and fill the then-freshwater lake."):

"Black Sea Trip Yields No Flood Conclusions"

http://tinyurl.com/eylm8

  There was no actual ruined building found by Ballard,
but rather just a partly rectangular outline of raised
bed on the continental shelf, that might even be
the outline of
the wheelhouse of a modern freighter.
  To the northwest the outline continues, and narrows to a point.
  To the southeast, the outline continues for a shorter distance,
and ends in a rounded curve.
  Just what you'd expect when a sunken ship's hull is covered with
sediment.
  The wood didn't necessarily contaminate the site, it might have
been part of the ship, and so accurately dates the site.
  The roughly-worked stones could have been the ship's ballast.

  If you wish, I can supply links to the writeups on Ballard's
finds in professional journals.

  And here are a couple of scientific papers:

"Is the abrupt drowning of the Black Sea shelf at
7150 yr BP a myth?"

http://tinyurl.com/blart

"Persistent Holocene Outflow from the Black Sea to the Eastern
Mediterranean Contradicts Noah's Flood Hypothesis"

http://tinyurl.com/65yxu

  And there's lots more, but you'd need access to scientific journals
to read it, but you could ask me for more details if you want them.
  Some of the articles are available on the Web.

<DISENGAGE RANT MODE>

  Sorry to splash water in the frying pan. 

Daryl Krupa
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 37)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-08-12T20:06:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kospf1hvfol2efbtt36dtvl04j87fr1n5p@4ax.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>There is a subset of American fundamentalists who point to the fact that a wide
>variety of peoples have legends of great floods as support of the Noah story.
…[3 more quoted lines elided]…
>Jewish family....

If it did, we're all horribly inbred... Which may account for a lot.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 38)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-13T00:05:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BPaLe.6069$Yx1.3473@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123807962.998060.115160@g44g2000cwa.googlegroups.com> <ddi8v1$nf9$1@peabody.colorado.edu> <kospf1hvfol2efbtt36dtvl04j87fr1n5p@4ax.com>`

```
"Jeff York" <ralf4@btinternet.com> wrote in message 
news:kospf1hvfol2efbtt36dtvl04j87fr1n5p@4ax.com...
> "Howard Brazee" <howard@brazee.net> wrote:
>
…[9 more quoted lines elided]…
> If it did, we're all horribly inbred... Which may account for a lot.

I never even thought of myself as Jewish even though I have been known to 
answer a question with a question.

JCE
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T14:31:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd343$ml6$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com>`

```

On  9-Aug-2005, "Richard" <riplin@Azonic.co.nz> wrote:

> For example a few thousand years ago there were only a very small
> number of breeds of dog. Now there are hundreds of them.  That is
> evolution, but it is not 'natural selection' because it is primarily
> 'artificial selection'.

This assumes that human action is not part of nature.   I've never been able to
separate our actions from those of other animals the way many people do.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 33)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T11:24:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd684$89o$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu>`

```
In article <ddd343$ml6$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  9-Aug-2005, "Richard" <riplin@Azonic.co.nz> wrote:
…[7 more quoted lines elided]…
>separate our actions from those of other animals the way many people do.

Hmmmmm... not too many other species I know of have managed to change 
their longevity like them human-being type folks have.

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T15:58:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd87u$p8t$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com>`

```

On 10-Aug-2005, docdwarf@panix.com wrote:

> >This assumes that human action is not part of nature.   I've never been able
> >to
…[3 more quoted lines elided]…
> their longevity like them human-being type folks have.

One way to change longevity is to become a pet or prey of people.  The basic way
is to either die or survive.   Some do this individually, and some do it
collectively.

Sure I can find characteristics that make humans unique.   But I can find
characteristics that make beavers unique as well.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T12:09:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd8r5$jt1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu>`

```
In article <ddd87u$p8t$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 10-Aug-2005, docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
>One way to change longevity is to become a pet or prey of people.

It would seem, by this, that it is people who are changing longevity of 
the pet/prey species.

>The basic way
>is to either die or survive.

Ummmmm... given that 'longevity' is 'the length of life' then dying or 
surviving might have something to do with it, aye.

>Some do this individually, and some do it
>collectively.
>
>Sure I can find characteristics that make humans unique.   But I can find
>characteristics that make beavers unique as well.

Oh, those beavers... may all their habitats be dammed!

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 36)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-10T12:21:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123701695.906884.54600@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<ddd8r5$jt1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <ddd8r5$jt1$1@panix5.panix.com>`

```
> It would seem, by this, that it is people who are changing longevity of
> the pet/prey species.

It seems to me that cats (the ones that live in my house) view their
relationship with man as one of master/slave with the cats being the
master.

There are ants that 'farm' aphids. They keep them as domestic animals
to be milked and protect them. This may be viewed as the aphids paying
for protection or as ants enslaving the aphids. In either case both
probably live longer.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 37)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T21:12:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dde8la$sug$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd87u$p8t$1@peabody.colorado.edu> <ddd8r5$jt1$1@panix5.panix.com> <1123701695.906884.54600@o13g2000cwo.googlegroups.com>`

```
In article <1123701695.906884.54600@o13g2000cwo.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:

[snip]

>It seems to me that cats (the ones that live in my house) view their
>relationship with man as one of master/slave with the cats being the
>master.

You feed a dog, the dog thinks you are God.  You feed a cat, the cat 
thinks *it* is God.'

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 38)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-08-11T14:07:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cajmf1hin56bgo72of49edasqtjmag53fg@4ax.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd87u$p8t$1@peabody.colorado.edu> <ddd8r5$jt1$1@panix5.panix.com> <1123701695.906884.54600@o13g2000cwo.googlegroups.com> <dde8la$sug$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <1123701695.906884.54600@o13g2000cwo.googlegroups.com>,
>Richard <riplin@Azonic.co.nz> wrote:
…[8 more quoted lines elided]…
>thinks *it* is God.'

"Oy loike pigs...  Dogs looks up to you... Cats look down on you...
But pigs is equal."  (Old, anon, country saying..)   :-)
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 39)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-11T09:31:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddfk09$au6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123701695.906884.54600@o13g2000cwo.googlegroups.com> <dde8la$sug$1@panix5.panix.com> <cajmf1hin56bgo72of49edasqtjmag53fg@4ax.com>`

```
In article <cajmf1hin56bgo72of49edasqtjmag53fg@4ax.com>,
Jeff York  <ralf4@btinternet.com> wrote:
>docdwarf@panix.com wrote:
>
…[13 more quoted lines elided]…
>But pigs is equal."  (Old, anon, country saying..)   :-)

McAfferty got high and he fell into a sty,
And the parson-priest walked by and then did say:
'You can tell a man who boozes by the company he chooses.'
... and the pig got up and slowly walked away.

(as heard from Benny Hill)

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T09:49:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvb3bF14a4nfU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddd87u$p8t$1@peabody.colorado.edu...
>
>
…[16 more quoted lines elided]…
> characteristics that make beavers unique as well.

Dammit! You reminded me that one of the things on my "to do" list (before I 
die...) is to see beavers in the wild. My experience of beavers, while 
pleasant enough, has been limited to an alternative meaning for the word.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 36)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-10T20:57:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-55DA48.20570310082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> "Howard Brazee" <howard@brazee.net> wrote:
> > Sure I can find characteristics that make humans unique.   But I can find
…[6 more quoted lines elided]…
> Pete.

Must....Resist....Temptation....Must....Resist.....

Oh, well, I was never strong willed.  Here you go:

   http://www.girlsgonewild.com
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T13:05:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvmiaF14ibt8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net> <joe_zitzelberger-55DA48.20570310082005@ispnews.usenetserver.com>`

```
 

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-55DA48.20570310082005@ispnews.usenetserver.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[17 more quoted lines elided]…
>   http://www.girlsgonewild.com

ROFL! Thanks Joe, made my day... :-)

Pete.
>
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 36)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-11T13:37:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddfkap$85o$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net>`

```

On 10-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> Dammit! You reminded me that one of the things on my "to do" list (before I
> die...) is to see beavers in the wild. My experience of beavers, while
> pleasant enough, has been limited to an alternative meaning for the word.

Let me guess:

# noun:   a hat made of beaver fur or similar material
# noun:   a movable piece of armor on a medieval helmet used to protect the
lower face
# noun:   a full beard
# noun:   the soft brown fur of the beaver
# noun:   a man's hat with a tall crown; usually covered with beaver or silk
# verb:   work hard on something
# name:  A surname (common: 1 in 14285 families; popularity rank in the U.S.:
#1757)

Maybe Don Adam's son-in-law.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-12T14:50:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m2h47F14m9f8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net> <ddfkap$85o$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddfkap$85o$1@peabody.colorado.edu...
>
> On 10-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[21 more quoted lines elided]…
> Maybe Don Adam's son-in-law.

None of the above... :-)

I think (from memory) Don Adams was Maxwell Smart? I have no idea who his 
son-in-law was... can you clarify, please?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 38)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-12T13:43:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddi91d$nfa$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net> <ddfkap$85o$1@peabody.colorado.edu> <3m2h47F14m9f8U1@individual.net>`

```

On 11-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> None of the above... :-)
>
> I think (from memory) Don Adams was Maxwell Smart? I have no idea who his
> son-in-law was... can you clarify, please?

http://imdb.com/name/nm0064769/
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 39)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-13T10:47:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m4n84F15hg37U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <ddd87u$p8t$1@peabody.colorado.edu> <3lvb3bF14a4nfU1@individual.net> <ddfkap$85o$1@peabody.colorado.edu> <3m2h47F14m9f8U1@individual.net> <ddi91d$nfa$1@peabody.colorado.edu>`

```
Ah, clear now, thanks.

(Interesting site as well...)

Pete.

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddi91d$nfa$1@peabody.colorado.edu...
>
> On 11-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> http://imdb.com/name/nm0064769/
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-10T20:54:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com>`

```
In article <ddd684$89o$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <ddd343$ml6$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[15 more quoted lines elided]…
> DD

One could argue that common household pets have managed to do so.

Dogs and cats, by being cute and cuddly, have convinced a very dangerous 
predator (man) to give them protection, shelter and sustenance.  This 
allows them healthy and happy geriatric years they would not enjoy 
living with their own kind in the wild.

(I took my nine year old tom for his first geriatric physical this 
morning.  In the wild he would be long dead at the claws of a young 
upstart or a dread disease)

Cows, on the other hand...
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T21:26:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dde9gh$3sf$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com>`

```
In article <joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <ddd684$89o$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[18 more quoted lines elided]…
>One could argue that common household pets have managed to do so.

One has... and it has been countered that the humans make the animals live 
longer.

>
>Dogs and cats, by being cute and cuddly, have convinced a very dangerous 
>predator (man) to give them protection, shelter and sustenance.

Dogs and cats, by having traits that can be reinforced by human 
manipulation of their breeding, have shown that they can be of use to 
humans without being too much of a drain on resources.

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-11T04:28:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UtAKe.6485$dJ5.1564@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com...
> In article <ddd684$89o$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[25 more quoted lines elided]…
> living with their own kind in the wild.
In the West.
I guess the dumb dogs live in Asia?

> (I took my nine year old tom for his first geriatric physical this
> morning.  In the wild he would be long dead at the claws of a young
> upstart or a dread disease)
>
> Cows, on the other hand...
In the West.
I guess the smart cows live in Asia?

JCE
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 35)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-11T04:28:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UtAKe.6486$dJ5.4692@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123645561.235262.32580@g49g2000cwa.googlegroups.com> <ddd343$ml6$1@peabody.colorado.edu> <ddd684$89o$1@panix5.panix.com> <joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-B7190B.20542210082005@ispnews.usenetserver.com...
> In article <ddd684$89o$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[25 more quoted lines elided]…
> living with their own kind in the wild.
In the West.
I guess the dumb dogs live in Asia?

> (I took my nine year old tom for his first geriatric physical this
> morning.  In the wild he would be long dead at the claws of a young
> upstart or a dread disease)
>
> Cows, on the other hand...
In the West.
I guess the smart cows live in Asia?

JCE
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 31)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T14:29:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd30j$mf4$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET>`

```

On  9-Aug-2005, LX-i <lxi0007@netscape.net> wrote:

> > That is like saying "Gravity is only a theory".
> >
> > Evolution is observable
>
> How so?  I've observed gravity many times,

What does gravity look like?   I've never observed it myself, only its effects.

> and I've observed the slow
> animal being eaten.  It doesn't mean I extrapolate that to come up with
> my own ideas of how this world came to be - especially since all the
> "proof" I've ever seen for that theory is based on shoddy or
> now-discredited science (aka "junk science").

I expect gravity has more to do with how this world came to be than evolution.
But at any rate, the discussion is about semantics - the word "theory" means
different things in different contexts.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T02:56:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3luismF133cplU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddd30j$mf4$1@peabody.colorado.edu...
>
>
…[9 more quoted lines elided]…
> effects.

Huge amounts of money are being spent even as we speak to try and detect 
"gravity waves" and gravitons (the theoretical -that word again :-) - 
particle which exchanges the gravitational force. So far, no dice. To be 
fair, it is extremely hard to detect as there is nowhere you can go that is 
outside the field. I believe there are some underground experiments being 
carried out in the US which have a chance of doing it. The theory is that 
the exchange of gravitons between two bodies causes them to be attracted 
towards each other. I doubt it, myself, but if it proves to be so, it will 
cause a number of other puzzles to fall into place. Superstring theory 
predicts the existence of the graviton as a complex vibration of a string, 
described by Euler's equations.

I'll believe it when I see it... :-)

>
>> and I've observed the slow
…[10 more quoted lines elided]…
>

Very succinct, Howard. I think you are right on both counts.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 32)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T18:29:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<619cc$42fd30d6$45491c57$3415@KNOLOGY.NET>`
- **In-Reply-To:** `<ddd30j$mf4$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  9-Aug-2005, LX-i <lxi0007@netscape.net> wrote:
> 
…[7 more quoted lines elided]…
> What does gravity look like?   I've never observed it myself, only its effects.

Okay - amend that to say "...gravity in action many..."

(don't worry, we're not in for a re-run of the abortion thread...)
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 33)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-13T00:22:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu> <619cc$42fd30d6$45491c57$3415@KNOLOGY.NET>`

```
Funny that, because some people would argue that they've observed evolution 
also.  Some people even have documented their findings in a book - but I'm 
not sure that I believe everything written in a book.

I'm also at a loss to understand why there is a fear of Avian flu.  I mean 
how on earth would it get from chickens to people?


JCE

"LX-i" <lxi0007@netscape.net> wrote in message 
news:619cc$42fd30d6$45491c57$3415@KNOLOGY.NET...
> Howard Brazee wrote:
>> On  9-Aug-2005, LX-i <lxi0007@netscape.net> wrote:
…[25 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-12T17:27:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123892856.422346.113130@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu> <619cc$42fd30d6$45491c57$3415@KNOLOGY.NET> <P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`

```
> I'm also at a loss to understand why there is a fear of Avian flu.  I mean
> how on earth would it get from chickens to people?

By evolving.
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T19:56:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76af7$42fd4544$45491c57$9105@KNOLOGY.NET>`
- **In-Reply-To:** `<P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu> <619cc$42fd30d6$45491c57$3415@KNOLOGY.NET> <P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`

```
jce wrote:
> 
> I'm also at a loss to understand why there is a fear of Avian flu.  I mean 
> how on earth would it get from chickens to people?

By people eating the chickens?  By people "catching" a contagious 
disease from another creature?  There are lots of "hows"...
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-12T21:11:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddjhcj$4qa$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddd30j$mf4$1@peabody.colorado.edu> <619cc$42fd30d6$45491c57$3415@KNOLOGY.NET> <P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>`

```
In article <P2bLe.10069$Oy2.8110@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:

[snip]

>I'm also at a loss to understand why there is a fear of Avian flu.  I mean 
>how on earth would it get from chickens to people?

A wrong turn at Albuquerque, perhaps.

DD
```

###### ↳ ↳ ↳ Re: OT: Authorities

_(reply depth: 33)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-15T14:21:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddq8d5$f80$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <1123621207.166429.68760@g49g2000cwa.googlegroups.com> <b3084$42f92a35$45491c57$13663@KNOLOGY.NET> <ddd30j$mf4$1@peabody.colorado.edu> <619cc$42fd30d6$45491c57$3415@KNOLOGY.NET>`

```

On 12-Aug-2005, LX-i <lxi0007@netscape.net> wrote:

> >>>That is like saying "Gravity is only a theory".
> >>>
…[9 more quoted lines elided]…
> (don't worry, we're not in for a re-run of the abortion thread...)

The point is, we can't observe theories.  Theories work at explaining processes
we do observe.  And they aren't absolute - we can still use Newton to explain
the path of a baseball, even though Einstein has superseded Newton for some more
precise needs.    We do see that speciation exists.   We can explain our
observation as a miracle - and we can explain gravity as a miracle.   The Bible
doesn't discuss speciation, and Genesis 1 and Genesis 2 have enough conflicts
that it's obvious that the lessons we should learn from them are deeper than to
assume we know everything about creation, God, nor the universe.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T13:36:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lt40aF14658jU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddabak$581$1@peabody.colorado.edu...
>
> On  8-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[26 more quoted lines elided]…
>  Authority has scope, and authoritarians don't want scope.

During the course of this debate I have come to realise how important 
context is. It was only when the Doc started removing it (not from mischief, 
but because he honestly considered it irrelevant, or simply didn't want it 
to be considered in the argument) that I had a flash of insight about it. We 
do communicate in shades of grey. Context, including body language and 
expression, tone of voice, etc. are all important to the message.

One of the reasons Chuck was offended by my original post is because he 
believed I  was stating matters of opinion as matters of fact. That was fair 
enough, but he then went further and decided that there was implicit 
contempt in the posts. None of that was ever intended by me. I am forced to 
wonder whether he would have had the same opinion if we had been sitting in 
a bar discussing it over a beer. Would my body language and tone of voice 
have made a difference to his interpretation of my meaning?

I'm inclined to believe it would have. (But, obviously, I can't prove it...)

Are we so conditioned by the adversarial approach to argument that we always 
expect the worst? Is it always a contest? I honestly don't know.

I do know that relying only on rigid definitions is limiting and risky.

Context is much more important than I realised previously.

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 30)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-10T00:11:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net>`

```
In article <3lt40aF14658jU1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:ddabak$581$1@peabody.colorado.edu...
…[23 more quoted lines elided]…
> Context is much more important than I realised previously.

Context is everything.

It is what allows Daniel to see evolution as only a "theory" while 
Richand can see it as a Theory.  It is what allows DD to see unions as a 
helpful protection for the worker while I see them as nothing more that 
legal extortion and a threat to my kneecaps.  It allows Bill Clinton to 
consider a blow job "not sexual relations" while my wife has a very 
different view.

We are all waaaayyy coloured by our experiences and that alters the 
context from which we view things.

My wife, Tracy, likes to say that email always sounds 10 times worse 
than the writer intended.  But I was trained in the 15-user BBS 'if your 
post doesn't stir some controversy then the thread dies' school of 
online chatting.

It is almost impossible to get a clear indication of a posters emotion 
or any form of subtly in a media that allows less that 100 displayable 
characters.  Efforts to try are invariably going to be badly mistaken.

So don't worry about it.  Have another beer and appreciate that you live 
in one of the coolest places in the world...live is good...you can 
ski...then go to the beach...then ski....

Why read so much into a 300-iteration post/repost issue that started 
from a misunderstanding?
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T05:40:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddci2m$6f7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com>`

```
In article <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:

[snip]

>Why read so much into a 300-iteration post/repost issue that started 
>from a misunderstanding?

Besides the fact that one might learn things in the oddest of places... 
hey, everyone needs a hobby!

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T23:05:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lu5c8F14g648U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com>`

```
 

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com...
>
> In article <3lt40aF14658jU1@individual.net>,
…[47 more quoted lines elided]…
> context from which we view things.

I'm coming to this point of view. I think we all realize it intuitively and 
intellectually, but it is only very recently that I have actually realized 
HOW much it colours the way we communicate. ( I'm not sure I agree it is 
everything, but it is way more important than I previously thought.) 
Removing the explicit stated contexts from a communication certainly changes 
the intended meaning, and that is before you even begin to consider the 
implicit contexts, like tone of voice, body language, etc.

>
> My wife, Tracy, likes to say that email always sounds 10 times worse
> than the writer intended.  But I was trained in the 15-user BBS 'if your
> post doesn't stir some controversy then the thread dies' school of
> online chatting.

I too, spent many happy hours on BBSs before the Internet was available, and 
understand whereof you speak...:-)

>
> It is almost impossible to get a clear indication of a posters emotion
…[6 more quoted lines elided]…
>

Another 20 cms of fresh snow fell on the Ski fields today...:-) As a result 
the overnight temperature has dropped to around 5 degrees Centigrade here in 
the Bay (some 200 KM from the snow). But we had brilliant sunshine today 
(18C) and I had the roof off the car... Still a bit too cold for the beach, 
though (at least for a pussy like me - people were surfing in wetsuits)...

I gave up some time back actually worrying about offence I may have given 
here; I do the best I can.

I said I'm sorry, have taken on board the objection, and attempted to 
clarify my position. I can't do much more.

The whole question of communication and meaning and the respective 
approaches to it, is a lot more fun than shared procedure division code, 
anyway, and that's why I am still here :-)

Some good has come out of it (I learned a few things) and some very 
interesting ideas have been presented and debated.

> Why read so much into a 300-iteration post/repost issue that started
> from a misunderstanding?

Thanks. I appreciate your plain common sense. And you are right; the thread 
generated is way out of proportion to the importance of the matter that 
started it, but that is the nature of CLC... :-) I'm honestly not upset by 
it any more.

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T08:07:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddcqmp$7m7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com> <3lu5c8F14g648U1@individual.net>`

```
In article <3lu5c8F14g648U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>I'm honestly not upset by it any more.

Great value can be found after taking offense, Mr Dashwood... it might be 
that 'what causes upset' has something to do with 'what is taken 
seriously'.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T03:00:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3luj3qF146q80U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com> <3lu5c8F14g648U1@individual.net> <ddcqmp$7m7$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:ddcqmp$7m7$1@panix5.panix.com...
>
> In article <3lu5c8F14g648U1@individual.net>,
…[9 more quoted lines elided]…
>

Probably. Either way, it doesn't bother me. But that doesn't mean I'm not 
serious about the discussion... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T11:26:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd6bc$hk2$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu5c8F14g648U1@individual.net> <ddcqmp$7m7$1@panix5.panix.com> <3luj3qF146q80U1@individual.net>`

```
In article <3luj3qF146q80U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[15 more quoted lines elided]…
>serious about the discussion... :-)

... and any more sirius and you'd be... oh, never mind.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-10T20:35:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-03954F.20354310082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <joe_zitzelberger-873DF1.00110810082005@ispnews.usenetserver.com> <3lu5c8F14g648U1@individual.net>`

```
In article <3lu5c8F14g648U1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> Another 20 cms of fresh snow fell on the Ski fields today...:-) As a result 
> the overnight temperature has dropped to around 5 degrees Centigrade here in 
> the Bay (some 200 KM from the snow). But we had brilliant sunshine today 
> (18C) and I had the roof off the car... Still a bit too cold for the beach, 
> though (at least for a pussy like me - people were surfing in wetsuits)...

I'm in the wrong place...I need to find a gig there.  Dive or ski on a 
lunch break.  

Why do I even bother with Georgia?
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T05:39:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddchvk$pj4$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net>`

```
In article <3lt40aF14658jU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>During the course of this debate I have come to realise how important 
>context is.

Have a care, Mr Dashwood... next thing you know you'll be saying things 
like 'the meaning of a word is in its use'.

>It was only when the Doc started removing it (not from mischief, 
>but because he honestly considered it irrelevant, or simply didn't want it 
>to be considered in the argument) that I had a flash of insight about it.

At times, to learn of a building one might do well to strip away externals 
and examine the structural steel... there are things to be learned, and 
unlearned, from such an approach.

>We do communicate in shades of grey.

Well, there it is... in 'black-and-white', as it were.

>Context, including body language and 
>expression, tone of voice, etc. are all important to the message.

It has been said that the one who talks to the spirit-world is the 
underlying theme or idea... or that the medium is the message.  (sorry, 
couldn't resist)  What you mention above seems to be a subject of study in 
a field called 'semiotics'.

[snip]

>I do know that relying only on rigid definitions is limiting and risky.

... and on the other hand constantly having to clarify idiosyncratic uses 
can make for a weary, weary time, Mr Dashwood... as some who have read my 
postings might point out.  As has been said about thighs, 'In media 
felicitas est.'

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T22:32:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lu3d7F13e2alU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:ddchvk$pj4$1@panix5.panix.com...
>
> In article <3lt40aF14658jU1@individual.net>,
…[9 more quoted lines elided]…
>

No, I don't think so. Context is important but it isn't everything. Neither 
is dictionary definition. They are all useful in arriving at meaning, but 
none of them alone is the full story.  It's as if there is a cloud of 
possible meaning and parts of it are more probable than other parts... Until 
understanding is attempted, all meanings are possible, but once a particular 
meaning is seized upon, the wave collapses and no other meanings are then 
possible.

But then, perhaps I am spending too much time considering Young's 
experiment, EPR, and Quantum Mechanics in general :-)

>>It was only when the Doc started removing it (not from mischief,
>>but because he honestly considered it irrelevant, or simply didn't want it
…[8 more quoted lines elided]…
> Well, there it is... in 'black-and-white', as it were.

Hahaha!  Absolutely... :-)

>
>>Context, including body language and
…[4 more quoted lines elided]…
> couldn't resist)

That just sounds like MacLuhanacy to me...

>What you mention above seems to be a subject of study in
> a field called 'semiotics'.

I claim no expertise in this field but I have a passing acquaintance with 
it. (mainly gained from reading the  fictional works of Professoer Umberto 
Eco who holds the chair of semiotics at the University of Bologna.)  My 
understanding, (which may be flawed) is that it is about subliminal 
symbology and the meaning ascribed to symbols in different cultures. I guess 
that could be an area of context exploration, as you suggest.

>
> [snip]
…[7 more quoted lines elided]…
>

et in vino veritas...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T07:26:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddco9e$qin$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <3lu3d7F13e2alU1@individual.net>`

```
In article <3lu3d7F13e2alU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[14 more quoted lines elided]…
>No, I don't think so.

At one point, Mr Dashwood, some people thought they'd always be sopranos 
with hairless axillae... funny how things can change.

>Context is important but it isn't everything. Neither 
>is dictionary definition. They are all useful in arriving at meaning, but 
…[7 more quoted lines elided]…
>experiment, EPR, and Quantum Mechanics in general :-)

Sounds more like Schroedinger's cat, I'd say... but in that you posit 'a 
cloud of possible meaning' (which I translate as 'a variety of possible 
interpretations') it may be more like kittens.

[snip]

>>>We do communicate in shades of grey.
>>
>> Well, there it is... in 'black-and-white', as it were.
>
>Hahaha!  Absolutely... :-)

Glad you enjoyed, old man.

>
>>
>>>Context, including body language and
>>>expression, tone of voice, etc. are all important to the message.

[snip]

>>What you mention above seems to be a subject of study in
>> a field called 'semiotics'.
…[3 more quoted lines elided]…
>Eco who holds the chair of semiotics at the University of Bologna.)

One might do well to be careful about what one learns from novels, lest 
one learn that the Earth is hollow and inside there is a wond'rous 
civilisation from the Oldene Dayse.

>My 
>understanding, (which may be flawed) is that it is about subliminal 
>symbology and the meaning ascribed to symbols in different cultures. I guess 
>that could be an area of context exploration, as you suggest.

Perhaps there's something new to learn, Mr Dashwood... at least one can 
find the mistakes others have made before one goes about making ones of 
one's own.

(A few decades back, when I would have long, passionate, nightlong 
discusions about Truth and Falsity with other inebriated Kollidj Kidz I 
recall - vaguely - batting back-and-forth with a lad a concept along these 
lines.  His assertion was that learning from others in this way was a sort 
of subordination, in that one took the Truths of Old Authorities over 
one's own discoveries.  My question was 'Which is better... to have 
someone else's Actual Truths or to have My Very Own Mistakes?'; his 
response was 'Well... at least they're *mine*, doesn't that count for 
something?'

This was before I knew to respond with 'answering a question with a 
question is no answer at all' so I replied 'Not if the bridge falls down, 
no.')

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T14:25:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd2ns$mer$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com>`

```

On 10-Aug-2005, docdwarf@panix.com wrote:

> (A few decades back, when I would have long, passionate, nightlong
> discusions about Truth and Falsity with other inebriated Kollidj Kidz I
…[10 more quoted lines elided]…
> no.')

On the other hand, if we have to make our own ethical decisions, we don't feel
good about having an authority send our kids to kill.

Some compromise seems to be in order here.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T11:30:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd6j4$f79$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <ddd2ns$mer$1@peabody.colorado.edu>`

```
In article <ddd2ns$mer$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 10-Aug-2005, docdwarf@panix.com wrote:
…[16 more quoted lines elided]…
>good about having an authority send our kids to kill.

Plural majestatus est, Mr Brazee... I barely know what makes *me* feel 
good, let alone others.

>
>Some compromise seems to be in order here.

... and on that point there can be no negotiation!

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T03:40:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lulggFt0olcU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:ddco9e$qin$1@panix5.panix.com...
>
> In article <3lu3d7F13e2alU1@individual.net>,
…[38 more quoted lines elided]…
> interpretations') it may be more like kittens.

Schroedinger's cat is very apposite and the idea is exactly that of his 
famous thought experiment.

>
> [snip]
…[26 more quoted lines elided]…
>

Jules Verne I think... Edgar Rice Burruoghs used it for Tarzan as well (The 
lost land of Pellucidar - I seem to recall it was in 'Tarzan at the Earth's 
Core' , but I was 10 when I read it so I could be mistaken...)

>>My
>>understanding, (which may be flawed) is that it is about subliminal
…[7 more quoted lines elided]…
>

Ah, I would stake money there isn't a parent alive who has not wished their 
kids could learn by the parent's mistakes. When I look back across my life 
at all the good and sage advice I received and was unable/unwilling to 
assimilate, I realise I could have saved a large amount of time, effort and 
pain. I can't speak for others, but I fancy I'm not alone in this... :-)

It seems to me that the REALLY smart people ARE able to learn from the 
mistakes of others, but the majority of us can't or won't.

Experience is certainly the best teacher, as the old adage goes, but her 
fees are sometimes very high...


> (A few decades back, when I would have long, passionate, nightlong
> discusions about Truth and Falsity with other inebriated Kollidj Kidz I
…[7 more quoted lines elided]…
>
I understand his feeling.

> This was before I knew to respond with 'answering a question with a
> question is no answer at all' so I replied 'Not if the bridge falls down,
> no.')
>

It is true that when it comes to the lives of others (like a bridge tragedy) 
we cannot allow the engineer to say: "Oops! Chalk that one up to 
experience...", so we put checks and balances in place to ensure that the 
risks are minimised and the responsibility is shared by people qualified to 
do so. But few of us engineer our lives. And even fewer would be prepared to 
share the responsibility for their personal growth and development with 
others, no matter how well qualified. (It is one thing to learn a subject 
from a tutor as part of the paper chase, it is quite another to do the same 
with your personal life, even if you could....)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T15:54:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd7up$p5a$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net>`

```

On 10-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> Ah, I would stake money there isn't a parent alive who has not wished their
> kids could learn by the parent's mistakes. When I look back across my life
> at all the good and sage advice I received and was unable/unwilling to
> assimilate, I realise I could have saved a large amount of time, effort and
> pain. I can't speak for others, but I fancy I'm not alone in this... :-)

Sometimes it works, and the kids find their own mistakes to make.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T12:21:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd9hp$n53$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net>`

```
In article <3lulggFt0olcU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[10 more quoted lines elided]…
>>>> Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>>>Until
>>>understanding is attempted, all meanings are possible, but once a 
…[12 more quoted lines elided]…
>famous thought experiment.

That's what it 'smelled' like, aye... but I recall learning about the cat 
and thinking 'How does putting the box on a weight-scale change this?'

[snip]

>>>>What you mention above seems to be a subject of study in
>>>> a field called 'semiotics'.
…[12 more quoted lines elided]…
>Core' , but I was 10 when I read it so I could be mistaken...)

Authors can be like musicians who, upon hearing 'a right tasty lick', 
miraculously change from appropriators to originators... but lo, there is 
nothing new under the sun, said a Preacher.

>
>>>My
…[14 more quoted lines elided]…
>pain. I can't speak for others, but I fancy I'm not alone in this... :-)

On the other hand... perhaps that cloud's lining is a bunch of Fine 
Stories to relate at the oddest of times...

... which might, indeed bore the youngsters to tears.

>
>It seems to me that the REALLY smart people ARE able to learn from the 
>mistakes of others, but the majority of us can't or won't.

Perhaps it happens more often, and more subtley, than one might think; 
consider 'I'll never forget the time I saw (person) do (activity) and have 
it blow all to Hades and beyond... I never tried doing *that* again!'

>
>Experience is certainly the best teacher, as the old adage goes, but her 
>fees are sometimes very high...

At times one gets what one pays for.

[snip]

>> My question was 'Which is better... to have
>> someone else's Actual Truths or to have My Very Own Mistakes?'; his
…[14 more quoted lines elided]…
>do so. But few of us engineer our lives.

There's that pesky third person plural again... see above about learning 
from others.

kDD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T10:15:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvckjF14bnkqU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:ddd9hp$n53$1@panix5.panix.com...
>
> In article <3lulggFt0olcU1@individual.net>,
…[37 more quoted lines elided]…
>

It doesn't. That was a different thought experiment  ('the clock in a box') 
devised by Einstein to show it was possible to measure both energy and time 
together. Unfortunately (for Einstein) the paraphenalia needed to make the 
experiment practicable (weights, springs, etc) always make it impossible to 
remove the uncertainty from the measurement. It was part of the 'battle' 
between Einstein and Bohr to confirm or discredit quantum theory. This 
'battle raged from 1927 until Einstein's death in 1955. Bohr won 
(convincingly); Einstein lost, and quantum mechanics is one of the most 
successful (in that it successfully predicts events within probabilistic 
limits) theories in the history of mankind.

> [snip]
>
…[46 more quoted lines elided]…
>

Yes, there is that... Living a full life ensures there are many experiences 
and memories for the long winter nights. Now, in my dotage :-), I am 
attempting to write some of them down and create fiction based on real 
people and events (who are often much stranger than the wildest fiction) and 
the exercise fo attempting it is a wrthwhile (and entertaining) one.

> ... which might, indeed bore the youngsters to tears.
>
My experience is, that as long as you don't enforce stories on kids they are 
very happy to listen and will actually 'reach' for campfire tales, once 
they've had one or two good ones... :-)

>>
>>It seems to me that the REALLY smart people ARE able to learn from the
…[5 more quoted lines elided]…
>

Maybe.

>>
>>Experience is certainly the best teacher, as the old adage goes, but her
…[29 more quoted lines elided]…
>

OK. In my experience, I don't see people engineering their lives. (Did I 
really need to qualify that? Obviously, you thought I did...)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T21:32:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dde9s2$hgp$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net>`

```
In article <3lvckjF14bnkqU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[46 more quoted lines elided]…
>remove the uncertainty from the measurement.

Really?  I thought Schroedinger's cat was supposed to be two cats, one 
living and one dead, until the box was opened.  Both cats would have 
masses detectable by rather common weight-scales; when one 'disappeared' 
where would all that mass go?

[snip]
>>>Ah, I would stake money there isn't a parent alive who has not wished 
>>>their
…[14 more quoted lines elided]…
>the exercise fo attempting it is a wrthwhile (and entertaining) one.

An Italian to the key?  No, sorry, that's a Roman a clef.

[snip]

>>>It seems to me that the REALLY smart people ARE able to learn from the
>>>mistakes of others, but the majority of us can't or won't.
…[6 more quoted lines elided]…
>Maybe.

What is Life without a bit of Uncertainty?

[snip]

>>>It is true that when it comes to the lives of others (like a bridge 
>>>tragedy)
…[11 more quoted lines elided]…
>really need to qualify that? Obviously, you thought I did...)

Then our experiences are different; I have known a few folks who have told 
me 'Nope, I don't (x); I once saw a guy try it and (horrible thing) 
resulted.'

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-12T00:38:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m0v5kF14ua6bU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dde9s2$hgp$1@panix5.panix.com...
>
> In article <3lvckjF14bnkqU1@individual.net>,
…[62 more quoted lines elided]…
>
No Doc, it is one cat in two states simultaneously. More correctly, it is in 
an infinite number of states (Feynman's sum over histories), some of which 
are more probable than others. When the box is opened the probability wave 
"collapses" into the most likely possibility, and the cat is found to be 
alive or dead.

This is obviously complete nonsense when viewed as a description of the 
world we live in, and that is what most of these 'thought experiments' were 
designed for: to show that quantum theory just couldn't possibly be true. 
The trouble is that all of them are attempts to model something in terms we 
can grasp and deal with. They are not what truly happens in the quantum 
world. Niels Bohr refuted them within the terms they used; that is why he 
insisted on meticulous detail when describing the experiments, right down to 
the dials, springs, weights, indicators even the nuts and bolts used to 
construct the boxes.

The 'clock in a box' experiment is ingenious (as you might expect from 
Einstein) but Bohr nevertheless refuted it, and did so in terms that were no 
more than those used to describe the experiment. I had a look around the Net 
to see if I could find anything on it and the following link seems to cover 
quite a bit of what I have been arguing over the last few days, including a 
good description of the clock in a box: 
http://www-groups.dcs.st-and.ac.uk/~history/HistTopics/Time_2.html

We COULD affix the box  rigidly, in such a way that its exact location was 
known. But then it would be impossible to know its mass.(You can't weigh it 
unless it can move...) Quantum Theory wins every time.


> [snip]
>>
…[3 more quoted lines elided]…
>

Heisenberg probably said that... :-)

> [snip]

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 38)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-11T08:56:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddfhtr$8p6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com> <3m0v5kF14ua6bU1@individual.net>`

```
In article <3m0v5kF14ua6bU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[66 more quoted lines elided]…
>No Doc, it is one cat in two states simultaneously.

Ahhhhh, there it is... and since attributes can shift between states only 
one of those states needs to have the attribute of mass.

[snip]

>http://www-groups.dcs.st-and.ac.uk/~history/HistTopics/Time_2.html

Thanks much... good to review such things, every once in a while, I'd 
say... if only as an exercise in humility; long ago I generated the 
formulation that ''Time' is the label applied to the purported 
sequentiality of events' and I now see this as an echo/restatement of 
Mach's '... time is an abstraction, at which we arrive by means of the 
changes of things.'

[snip]

>> What is Life without a bit of Uncertainty?
>>
>
>Heisenberg probably said that... :-)

I came to from a variety of diverse sources, from a gambler's 'A 'sure 
thing' ain't no fun' to what I remember to be Schopenhauer's 'Man is a 
creature of curious wants and needs.  If these are not met he is 
dissatisfied, if these are met then he is bored.'

DD
```

###### ↳ ↳ ↳ OT: Quantum [was: Re: Authorities]

_(reply depth: 38)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-11T15:16:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CZJKe.216325$on1.123069@clgrps13>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com> <3m0v5kF14ua6bU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3m0v5kF14ua6bU1@individual.net...
>
>
…[11 more quoted lines elided]…
> is found to be alive or dead.

    It doesn't *always* collapse into the most likely possibility; that's 
just what happens most of the time (by definition of "most likely 
possibility"). It's conceivable (though highly improbable) that all of the 
mass (or matter) in the cat had spontaneously converted into energy. The law 
of "conservation of mass" was eventually replaced with the law of 
"conservation of energy and mass", which was later shortened to the law of 
"conservation of energy" when the equivalence of mass and energy (e=mc^2) 
was shown.

    But it turns out that the conservation of energy isn't nescessarily true 
for extremely short time scales (10^-43 seconds).

http://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat
http://en.wikipedia.org/wiki/Conservation_law
http://en.wikipedia.org/wiki/Conservation_of_energy
http://www.physlink.com/Education/AskExperts/ae281.cfm

    - Oliver
```

###### ↳ ↳ ↳ Re: Quantum [was: Re: Authorities]

_(reply depth: 39)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-12T15:17:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m2im7F14skccU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com> <3m0v5kF14ua6bU1@individual.net> <CZJKe.216325$on1.123069@clgrps13>`

```

"Oliver Wong" <owong@castortech.com> wrote in message 
news:CZJKe.216325$on1.123069@clgrps13...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[18 more quoted lines elided]…
> possibility").

OK, I agree the above should be amended to:

"When the box is opened the probability wave  USUALLY "collapses" into the 
most likely possibility, and the cat
is found to be alive or dead."

A small but important point.


> It's conceivable (though highly improbable) that all of the mass (or 
> matter) in the cat had spontaneously converted into energy. The law of 
…[7 more quoted lines elided]…
>

Certainly particles can 'borrow' energy from virtuality while the 'universe 
isn't looking', but these borrowings must be repaid, and usually within the 
very short time scales you mentioned. (I suspect you have been studying 
electron tunnelling, right :-)?)Some people believe this is why there is 
such frenetic activity ('quantum foam') on the Planck length horizon as 
particles and energy pop in and out of reality.

I'm not writing a treatise here on Quantum Theory, Oliver. Just providing 
enough information for people to assimilate easily and think about, so that 
these ideas can be included in a primarily 'philosophical' discussion.

> http://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat
> http://en.wikipedia.org/wiki/Conservation_law
> http://en.wikipedia.org/wiki/Conservation_of_energy
> http://www.physlink.com/Education/AskExperts/ae281.cfm
>

I thought your links were excellent and I read them all. Thanks.

Pete.
```

###### ↳ ↳ ↳ [OT] Schrodinger's Cat Straight Doped

_(reply depth: 40)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-12T05:35:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HyWKe.7701$Oy2.3445@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com> <3m0v5kF14ua6bU1@individual.net> <CZJKe.216325$on1.123069@clgrps13> <3m2im7F14skccU1@individual.net>`

```
For the geeks amongst us:

Schroedinger, Erwin! Professor of physics!
Wrote daring equations! Confounded his critics!
(Not bad, eh? Don't worry. This part of the verse
Starts off pretty good, but it gets a lot worse.)
Win saw that the theory that Newton'd invented
By Einstein's discov'ries had been badly dented.
What now? wailed his colleagues. Said Erwin, "Don't panic,
No grease monkey I, but a quantum mechanic.
Consider electrons. Now, these teeny articles
Are sometimes like waves, and then sometimes like particles.
If that's not confusing, the nuclear dance
Of electrons and suchlike is governed by chance!
No sweat, though--my theory permits us to judge
Where some of 'em is and the rest of 'em was."
Not everyone bought this. It threatened to wreck
The comforting linkage of cause and effect.
E'en Einstein had doubts, and so Schroedinger tried
To tell him what quantum mechanics implied.
Said Win to Al, "Brother, suppose we've a cat,
And inside a tube we have put that cat at--
Along with a solitaire deck and some Fritos,
A bottle of Night Train, a couple mosquitoes
(Or something else rhyming) and, oh, if you got 'em,
One vial prussic acid, one decaying ottom
Or atom--whatever--but when it emits,
A trigger device blasts the vial into bits
Which snuffs our poor kitty. The odds of this crime
Are 50 to 50 per hour each time.
The cylinder's sealed. The hour's passed away. Is
Our pussy still purring--or pushing up daisies?
Now, you'd say the cat either lives or it don't
But quantum mechanics is stubborn and won't.
Statistically speaking, the cat (goes the joke),
Is half a cat breathing and half a cat croaked.
To some this may seem a ridiculous split,
But quantum mechanics must answer, "Tough @#&!
We may not know much, but one thing's fo' sho':
There's things in the cosmos that we cannot know.
Shine light on electrons--you'll cause them to swerve.
The act of observing disturbs the observed--
Which ruins your test. But then if there's no testing
To see if a particle's moving or resting
Why try to conjecture? Pure useless endeavor!
We know probability--certainty, never.'
The effect of this notion? I very much fear
'Twill make doubtful all things that were formerly clear.
Till soon the cat doctors will say in reports,
"We've just flipped a coin and we've learned he's a corpse."'
So saith Herr Erwin. Quoth Albert, "You're nuts.
God doesn't play dice with the universe, putz.
I'll prove it!" he said, and the Lord knows he tried--
In vain--until fin'ly he more or less died.
Win spoke at the funeral: "Listen, dear friends,
Sweet Al was my buddy. I must make amends.
Though he doubted my theory, I'll say of this saint:
Ten-to-one he's in heaven--but five bucks says he ain't."

--CECIL ADAMS

TOP POST ONLY

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3m2im7F14skccU1@individual.net...
>
> "Oliver Wong" <owong@castortech.com> wrote in message 
…[66 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Schrodinger's Cat Straight Doped

_(reply depth: 41)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-12T22:27:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m3bt4F13getdU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <dde9s2$hgp$1@panix5.panix.com> <3m0v5kF14ua6bU1@individual.net> <CZJKe.216325$on1.123069@clgrps13> <3m2im7F14skccU1@individual.net> <HyWKe.7701$Oy2.3445@tornado.tampabay.rr.com>`

```
 
ROFL! Excellent! Thanks :-).

Pete.

Top Post NO MORE.

"jce" <defaultuser@hotmail.com> wrote in message 
news:HyWKe.7701$Oy2.3445@tornado.tampabay.rr.com...
>
> For the geeks amongst us:
…[135 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 36)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T18:44:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4067$42fd3443$45491c57$5127@KNOLOGY.NET>`
- **In-Reply-To:** `<3lvckjF14bnkqU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net>`

```
Pete Dashwood wrote:
>  
> 
…[17 more quoted lines elided]…
> really need to qualify that? Obviously, you thought I did...)

It depends on what level of conversation you're using, and whether you 
want to amend what you say until it's crafted to their exacting 
specifications.  I had no problems at all with your third person plural, 
and I understood exactly what you meant.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-13T12:10:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m4s38F1560rqU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:a4067$42fd3443$45491c57$5127@KNOLOGY.NET...
> Pete Dashwood wrote:
>>  <docdwarf@panix.com> wrote in message 
…[24 more quoted lines elided]…
>

Thank you, Daniel. Sometimes I really wonder if it is me or CLC... or just 
some people in CLC.

Nevertheless, as long as it is fun (and on the off-chance of actually 
learning something) I'll continue to come here...

As the Doc remarked a few days ago; everyone needs a hobby... :-)

Exchanging ideas with intelligent people is not a bad one, even if there is 
sometimes a smokescreen of pedantry and intolerance.

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 38)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-13T00:38:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VhbLe.10073$Oy2.4925@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3m4s38F1560rqU1@individual.net...
> Exchanging ideas with intelligent people is not a bad one, even if there 
> is sometimes a smokescreen of pedantry and intolerance.
>
> Pete.
It's not a smokescreen of pedantry and intolerance, it was right asking over 
and over and over and over for clarification on how you could possibly 
understand what you meant to say when other sources _clearly_ indicate you 
don't!

No more required from me on *this* thread :-)

JCE
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 38)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-12T21:14:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddjhia$5ap$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net>`

```
In article <3m4s38F1560rqU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>Exchanging ideas with intelligent people is not a bad one, even if there is 
>sometimes a smokescreen of pedantry and intolerance.

Oooooohh, intelligent people?  In the words of that wise philosopher, Moe 
Howard, in response to the greeting of 'Gentlemen!': (looking over 
shoulder) 'Who walked in?'  If you meet some of these intelligent people 
would you be so kind as to arrange an introduction for me?

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 39)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-15T14:05:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddq7fh$ekf$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net> <ddjhia$5ap$1@panix5.panix.com>`

```

On 12-Aug-2005, docdwarf@panix.com wrote:

> >Exchanging ideas with intelligent people is not a bad one, even if there is
> >sometimes a smokescreen of pedantry and intolerance.
…[4 more quoted lines elided]…
> would you be so kind as to arrange an introduction for me?

I've found that I can learn more from people who do think than from people who
can think.   Intelligence is over-rated.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 40)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-15T10:37:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddq9am$2bk$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3m4s38F1560rqU1@individual.net> <ddjhia$5ap$1@panix5.panix.com> <ddq7fh$ekf$1@peabody.colorado.edu>`

```
In article <ddq7fh$ekf$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 12-Aug-2005, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>can think.   Intelligence is over-rated.

Perhaps so... but I'll try to wait at least until the introductions before 
I start coming to conclusions.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 40)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-16T12:02:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3mcoo6F15srvmU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net> <ddjhia$5ap$1@panix5.panix.com> <ddq7fh$ekf$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddq7fh$ekf$1@peabody.colorado.edu...
>
>
…[14 more quoted lines elided]…
>
Yeah, all us dumbasses say that... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 38)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-08-16T09:06:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cg73g19t71crp8i35om84p7mecsk8umf9b@4ax.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote:

>Exchanging ideas with intelligent people is not a bad one, even if there is 
>sometimes a smokescreen of pedantry and intolerance.

I can assure you sir, that my pedantry and intolerance is *no*
smokescreen!   :-)
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 39)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-17T01:50:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3me999F16huggU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lu3d7F13e2alU1@individual.net> <ddco9e$qin$1@panix5.panix.com> <3lulggFt0olcU1@individual.net> <ddd9hp$n53$1@panix5.panix.com> <3lvckjF14bnkqU1@individual.net> <a4067$42fd3443$45491c57$5127@KNOLOGY.NET> <3m4s38F1560rqU1@individual.net> <cg73g19t71crp8i35om84p7mecsk8umf9b@4ax.com>`

```
 

"Jeff York" <ralf4@btinternet.com> wrote in message 
news:cg73g19t71crp8i35om84p7mecsk8umf9b@4ax.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[6 more quoted lines elided]…
>
Hahaha! Good one, Jeff... :-)

Pleased to see there are people who cling to the REAL values  back in the 
U.K.... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-08-10T11:33:18+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ksljf1lo95id0a5r8dj0gn28hkh927ih0s@4ax.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3lt40aF14658jU1@individual.net>,
>Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>like 'the meaning of a word is in its use'.

"'When I use a word' said Humpty Dumpty, 'it means exactly what I
intend it to... Neither more, nor less.'".
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T07:28:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddcoct$eli$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <ksljf1lo95id0a5r8dj0gn28hkh927ih0s@4ax.com>`

```
In article <ksljf1lo95id0a5r8dj0gn28hkh927ih0s@4ax.com>,
Jeff York  <ralf4@btinternet.com> wrote:
>docdwarf@panix.com wrote:
>
…[12 more quoted lines elided]…
>intend it to... Neither more, nor less.'".

Now one must consider what is more worthy as a basis for action... an 
aphorism by a fellow whose history was described in a book-review in The 
Economist as 'Lifestyle of the Profound and Potty' or a fictional, talking 
egg?

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T13:25:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddcv82$kij$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com>`

```

On 10-Aug-2005, docdwarf@panix.com wrote:

> >We do communicate in shades of grey.
>
> Well, there it is... in 'black-and-white', as it were.

As programmers, we are comfortable with unambiguous interpretation of what we
code.   And are frustrated when the users are upset when they get what they
asked for instead of what they want after seeing what they got.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T10:03:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd1f8$bvp$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <ddcv82$kij$1@peabody.colorado.edu>`

```
In article <ddcv82$kij$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 10-Aug-2005, docdwarf@panix.com wrote:
…[6 more quoted lines elided]…
>code.

That, for me, is one of the delights of coding... the translating of the 
swirling greys of 'the world out there' into the Aristotelean 'the bit is 
on or the bit is off'.

>And are frustrated when the users are upset when they get what they
>asked for instead of what they want after seeing what they got.

'I know it's what I told you but it's not what I want.'

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T14:22:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd2if$mbc$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com>`

```

On 10-Aug-2005, docdwarf@panix.com wrote:

> >We do communicate in shades of grey.
>
> Well, there it is... in 'black-and-white', as it were.

Let me adjust my monitor to look at it in green and yellow.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-10T11:32:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddd6m6$li1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lt40aF14658jU1@individual.net> <ddchvk$pj4$1@panix5.panix.com> <ddd2if$mbc$1@peabody.colorado.edu>`

```
In article <ddd2if$mbc$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 10-Aug-2005, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>Let me adjust my monitor to look at it in green and yellow.

Be careful... twiddle the knob the wrong way and Mr Zitzelberger might not 
be able to help agree it into fact.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 30)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-10T11:32:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dddh8d$1pnh$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3lt40aF14658jU1@individual.net...

> One of the reasons Chuck was offended by my original post is because he
> believed I  was stating matters of opinion as matters of fact. That was
fair
> enough, but he then went further and decided that there was implicit
> contempt in the posts.

Just to be clear, I believe that to describe an action as "stupid", based on
the common understanding of the meaning of the word (as well as the M-W
definition) as dim-witted or having characteristics of the actions expected
of a dim-witted person, carries implications about the person taking those
actions.  There are a wide variety of other equally-pejorative adjectives
one could use that don't carry the pejorative characterization of the
*person* taking the action that "stupid" does.

M-W Ninth Collegiate lists the synonyms "STUPID, DULL, DENSE, CRASS, DUMB
mean lacking in power to absorb ideas or impressions.  STUPID implies a
slow-witted or dazed state of mind that may be either congenital or
temporary ... ".  *All* these terms have implications directed toward
people.  If you didn't *mean to communicate* what the term "stupid"
communicates, then perhaps another term that more accurately reflected your
intent might have been more suitable!

< None of that was ever intended by me.

Yes, I understand that now, and have for a while.  What you intended wasn't
as accurately reflected in what you actually wrote as you might have hoped.

> I am forced to wonder whether he would have had the same opinion if we had
been sitting in
> a bar discussing it over a beer.

Yes, I think I would have, if (as appeared to be the case in the course of
the thread) the insistence that there is no possible context in which the
described actions could be described as anything but "stupid".  And if you
think I've been overly sensitive about the use of "stupid" you should have
seen how I'd have reacted back when I still was doing stuff like "sitting in
a bar discussing it over a beer"!   I tend to stay out of bars and pubs and
the like these days.  "Over coffee", maybe!

> Would my body language and tone of voice have made a difference to his
interpretation of my meaning?
> I'm inclined to believe it would have. (But, obviously, I can't prove
it...)

Might well have; I do think I'd have at least responded with something like
"Stupid is a pretty harsh word, don't you think?"

I might even have gone on to amplify it with an example like:   What if the
*reason* a particular person did it that way was that that's the way the
application architect told him he wanted it, and that if he didn't do it
that way he was going to lose his job, and along with that the medical
benefits he was planning on to cover the upcoming birth of his child?  I'd
contend the behavior of a person who stomped out of the office in a huff
Never To Dark On Their Door Again rather than offend his own sensibilities
would objectively be considered at least as unreasonable as the behavior of
a person who did what his employer told him to do!  Which one's taking the
"stupid" action?

> Are we so conditioned by the adversarial approach to argument that we
always
> expect the worst? Is it always a contest? I honestly don't know.

It certainly wasn't my intent here.  But as I'm sure you've seen in another
current thread (about whether unsigned items always have an *explicit* sign
on all meaningful architectures) I will question a categorical statement
when I see that there's a "local" truth, and not a "universal" one,
underlying the statement.!

> I do know that relying only on rigid definitions is limiting and risky.

True enough, but as others have pointed out when I use a word the way *I*
define it, rather than the way I have good reason to believe *others
understand* the word, it is *I* that am failing to communicate my intent,
not my audience that is failing to make the proper assumptions.

> Context is much more important than I realised previously.

So, I would argue, is ensuring that we don't use terms "idiopathically"
(taken in its non-pejorative current dictionary sense, rather than its
etymological one), particularly for terms that others might find pejorative!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-10T19:27:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dddkek$2ep$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com>`

```

On 10-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> So, I would argue, is ensuring that we don't use terms "idiopathically"
> (taken in its non-pejorative current dictionary sense, rather than its
> etymological one), particularly for terms that others might find pejorative!

Still, changing "this is stupid" to "I think this is stupid" does not change
what we think the word means. Also, nobody reading that post would believe that
when you said "this is stupid", you found some objective measure that we all
agree upon to determine this, and thus was something greater than your opinion.
 In fact, telling you to add "I believe" is implying strongly that they know
better.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-10T13:32:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123705926.849716.295840@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dddkek$2ep$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com> <dddkek$2ep$1@peabody.colorado.edu>`

```
> nobody reading that post would believe that
> when you said "this is stupid",

Maybe, but some would think that what was said was: "You are stupid
(for having said/done this)".
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T11:18:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvga0F144ieuU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com> <dddkek$2ep$1@peabody.colorado.edu> <1123705926.849716.295840@g47g2000cwa.googlegroups.com>`

```
 

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1123705926.849716.295840@g47g2000cwa.googlegroups.com...
>> nobody reading that post would believe that
>> when you said "this is stupid",
…[3 more quoted lines elided]…
>
Yes, I can see that.

But would a reasonable person continue to believe that, long after it was 
clarified that no such implication was intended?
(Smart people sometimes do stupid things, etc...)

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 33)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T18:39:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11d56$42fd331b$45491c57$3415@KNOLOGY.NET>`
- **In-Reply-To:** `<1123705926.849716.295840@g47g2000cwa.googlegroups.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com> <dddkek$2ep$1@peabody.colorado.edu> <1123705926.849716.295840@g47g2000cwa.googlegroups.com>`

```
Richard wrote:
>>nobody reading that post would believe that
>>when you said "this is stupid",
…[3 more quoted lines elided]…
> (for having said/done this)".

And some would misinterpret.  There is a difference between saying

"That was stupid!"

and

"You are stupid!"

Intelligent people can still do stupid things, and using the word with 
them may be a way to get their attention when they've lost their focus.  :)
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-12T21:50:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddjjke$2kc$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dddkek$2ep$1@peabody.colorado.edu> <1123705926.849716.295840@g47g2000cwa.googlegroups.com> <11d56$42fd331b$45491c57$3415@KNOLOGY.NET>`

```
In article <11d56$42fd331b$45491c57$3415@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>Richard wrote:
>>>nobody reading that post would believe that
…[12 more quoted lines elided]…
>"You are stupid!"

Not, perhaps, to those who know that 'stupid is as stupid does'.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 35)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T22:18:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c88f5$42fd6666$45491c57$4393@KNOLOGY.NET>`
- **In-Reply-To:** `<ddjjke$2kc$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dddkek$2ep$1@peabody.colorado.edu> <1123705926.849716.295840@g47g2000cwa.googlegroups.com> <11d56$42fd331b$45491c57$3415@KNOLOGY.NET> <ddjjke$2kc$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <11d56$42fd331b$45491c57$3415@KNOLOGY.NET>,
> LX-i  <lxi0007@netscape.net> wrote:
…[18 more quoted lines elided]…
> Not, perhaps, to those who know that 'stupid is as stupid does'.

Now we're getting life philosophy from Forrest Gump?  The tendency to 
people to think that *they* are being called stupid, when it is their 
*actions* that are being called stupid, is rooted in insecurity.  I can 
make a really bad mistake in code, and I can admit "Wow, I really boned 
that one up - that was stupid!"  Of course, I'm thick-skinned these 
days, and I've never been one to tiptoe around those who are easily 
offended.  One of the signs of the weakness of our culture is the 
constant drumbeat for apologies from anyone who is the least bit 
offended by the least little thing.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-13T09:15:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddkrqe$7gv$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <11d56$42fd331b$45491c57$3415@KNOLOGY.NET> <ddjjke$2kc$1@panix5.panix.com> <c88f5$42fd6666$45491c57$4393@KNOLOGY.NET>`

```
In article <c88f5$42fd6666$45491c57$4393@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <11d56$42fd331b$45491c57$3415@KNOLOGY.NET>,
…[21 more quoted lines elided]…
>Now we're getting life philosophy from Forrest Gump?

I don't know what 'we' are getting... but 'handsome is as handsome does' 
is an aphorism which antedates that particular film by a few centuries.  
Would you have found it more tasteful were I to have cited Goldsmith's 
'The Vicar of Wakefield' (1766) use of 'Handsome is that handsome does' 
(http://www.bartleby.com/100/273.85.html)... or are you the sort of 
well-read type who'd place the origin with Chaucer's 'The Tale of the Wife 
of Bath', as in 'That he is gentil that doth gentil dedis'?

>The tendency to 
>people to think that *they* are being called stupid, when it is their 
>*actions* that are being called stupid, is rooted in insecurity.

I barely know how *I* think, let alone 'people'... but the tradition of 
'you are what you do' seems to be a moderately well-established one.

>I can 
>make a really bad mistake in code, and I can admit "Wow, I really boned 
>that one up - that was stupid!"  Of course, I'm thick-skinned these 
>days, and I've never been one to tiptoe around those who are easily 
>offended.

As my sainted Paternal Grandfather - may he sleep with the angels! - used 
to say, 'Never use yourself as a comparative... you'll only be 
disappointed.'

>One of the signs of the weakness of our culture is the 
>constant drumbeat for apologies from anyone who is the least bit 
>offended by the least little thing.

How interesting... you do realise, of course, that many Arab cultures have 
it that offering an apology is a sign of weakness; it is my experience 
that those people who have confidence are more than willing, right off the 
bat, to say 'Oh, sorry, didn't mean to offend'.

But perhaps you are right... one must be very careful of this 'cultural 
weakness', one never knows when it will give rise to works of 'degenerate 
art'.

DD
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 36)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-14T13:07:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fuukmojakes39@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dddkek$2ep$1@peabody.colorado.edu> <1123705926.849716.295840@g47g2000cwa.googlegroups.com> <11d56$42fd331b$45491c57$3415@KNOLOGY.NET> <ddjjke$2kc$1@panix5.panix.com> <c88f5$42fd6666$45491c57$4393@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message
news:c88f5$42fd6666$45491c57$4393@KNOLOGY.NET...
> docdwarf@panix.com wrote:
> > In article <11d56$42fd331b$45491c57$3415@KNOLOGY.NET>,
> > LX-i  <lxi0007@netscape.net> wrote:
[snip]
> >>  There is a difference between saying
> >>
…[8 more quoted lines elided]…
> Now we're getting life philosophy from Forrest Gump?

I wonder whether the source is all that important. The
following seems to be along the lines of 'not casting the
first stone'.

"You know ... we all do stuff ... stupid stuff, but we learn
... and ... and ... we learn ... and we don't do it again.
...  Ok, so, ... you know ... who are we to be all judgy!"
-- Buffy Summers, "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T11:14:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvg2pF14ptmgU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com>`

```
 

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dddh8d$1pnh$1@si05.rsvl.unisys.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
…[14 more quoted lines elided]…
> actions.

Not for me. I can see an action as being stupid without making any judgement 
about the person doing it. Smart people often do stupid things. But I 
explained that. And I said then and say now, no contempt was intended.

How does something written in a dictionary change that? Why would you cling 
to the 'meaning' in your authority, when I have clarified exactly how I was 
using the word and what I intended by it? Doesn't it strike you as a 
pointless exercise...?

"MW says 'stupid' means...."
"Yes, but I used it in a slightly different way from that..."
"But MW says...."

ad nauseum...

UNTIL, I clarified my meaning, your point was valid. After that it is just 
silly...

> There are a wide variety of other equally-pejorative adjectives
> one could use that don't carry the pejorative characterization of the
> *person* taking the action that "stupid" does.

The above appears to contradict itself; how can something be equally 
pejorative and not carry a pejorative characterization? It is just playing 
with words, Chuck. What you are saying is I should choose some other 
derogatory term to express my disapproval because you don't like 'stupid'.

As I am not psychic, I really can't know what terms you will be offended by, 
so I take the line of least resistance and use the words I want to. I don't 
think that is unreasonable in a public forum. I'm certainly not going to 
filter and censor everything I write because someone may understand it 
differently than I intended, or may read more into it than I intended, or 
may be using an authority for a definition that I don't have or use, or may 
be upset by what I wrote.

I sometimes find your posts pompous and pedantic (not so much of late - 
maybe we're all getting mellower...). But I don't take you to task over it 
or get offended by it. I respect your right to express yourself how you see 
fit. I also accept that there are fundamantal issues you and I will never 
agree on, but that doesn't cause me to see you as the 'enemy' or set out to 
offend you.

Your reaction to what you encounter here is your reaction to what you 
encounter here.

>
> M-W Ninth Collegiate lists the synonyms "STUPID, DULL, DENSE, CRASS, DUMB
…[6 more quoted lines elided]…
> intent might have been more suitable!

No, I believe the action described was stupid. I'm not going to consult MW 
(or any other authority)before I post here.  It is CLC, not the Supreme 
Court. I clarified and qualified my use of the term 'stupid'.
>
> < None of that was ever intended by me.
…[5 more quoted lines elided]…
>

Well, it certainly wasn't as far as your concerned. For that I am sorry. But 
I call 'em like I see 'em.

>> I am forced to wonder whether he would have had the same opinion if we 
>> had
…[11 more quoted lines elided]…
> the like these days.  "Over coffee", maybe!

OK, in a friendly environment, then...
>
>> Would my body language and tone of voice have made a difference to his
…[7 more quoted lines elided]…
>
Fair enough. I could have picked up on your sensitivity to the word and may 
have substituted another on the spot, or clarified that there was no 
implication in my use of it. So context definitely has an important effect 
on communication.

> I might even have gone on to amplify it with an example like:   What if 
> the
…[10 more quoted lines elided]…
>
Check the meaning of 'darken' as opposed to 'dark on'... Even with MW 
readily available, in the hands of a highly qualified Linguist, sometimes 
the wrong word gets used. Nevertheless, from the context, and being a person 
of goodwill, I grasped your meaning. :-)

>> Are we so conditioned by the adversarial approach to argument that we
> always
…[9 more quoted lines elided]…
>
Good for you. This is a public unmoderated forum. One of the last bastions 
of Free Speech left on the planet...I treasure it, even though it irritates 
me sometimes (I'm learning to deal with that... :-)) People SHOULD post 
their opinions here.

>> I do know that relying only on rigid definitions is limiting and risky.
>
…[3 more quoted lines elided]…
> not my audience that is failing to make the proper assumptions.

I take full responsibility for people failing to understand what I write. 
Fortunately, it doesn't happen very often.

>
>> Context is much more important than I realised previously.
…[4 more quoted lines elided]…
> pejorative!

Sorry, Chuck, it's too much trouble. I can't filter everything I write 
because someone might find it pejorative. By far the majority of people here 
had no problem with it and accepted it was simply my opinion. I don't write 
to wound. I do have a strong opinion about what I perceive to be stupid 
practices.

I believe you over reacted. The only thing I'm sorry about is that you took 
offense where none was intended. I understand why you did, but there is 
little I can do about that.

I will consider in future HOW strong I want to be about something, but I 
have no intention of watering down or stifling the opinions I express here, 
or the way in which I express them. Don't read my posts if they upset you.(I 
know you have to read them before you can decide your reaction, but let's 
say if you consistently find reading my posts to be an unpleasant 
experience, then, for you, it is probably best avoided...)

Nevertheless some worthwhile things have come out of this experience and, if 
nothing else, it has caused me to re-examine the whole business of 
communication.

Let's move on.

Pete.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-11T04:40:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hFAKe.6507$dJ5.1949@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com> <3lvg2pF14ptmgU1@individual.net>`

```
I believe responding here is stupid but I'm not offended easily so I shall 
continue.

>> Would my body language and tone of voice have made a difference to his
>> interpretation of my meaning?
> I'm inclined to believe it would have. (But, obviously, I can't prove 
> it...)

A written explanation - which I believe to be more definitive than tone - 
didn't do the trick.

I think it's high time someone started comp.lang.cobol.moderated.....now 
there's an idea.

JCE
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 31)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-10T19:36:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fl41pf0gito51@corp.supernews.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:dddh8d$1pnh$1@si05.rsvl.unisys.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3lt40aF14658jU1@individual.net...
…[7 more quoted lines elided]…
> Just to be clear, I believe that to describe an action as "stupid", based
on
> the common understanding of the meaning of the word (as well as the M-W
> definition) as dim-witted or having characteristics of the actions
expected
> of a dim-witted person, carries implications about the person taking those
> actions.  There are a wide variety of other equally-pejorative adjectives
…[8 more quoted lines elided]…
> communicates, then perhaps another term that more accurately reflected
your
> intent might have been more suitable!
>
> < None of that was ever intended by me.
>
> Yes, I understand that now, and have for a while.  What you intended
wasn't
> as accurately reflected in what you actually wrote as you might have
hoped.
>
> > I am forced to wonder whether he would have had the same opinion if we
had
> been sitting in
> > a bar discussing it over a beer.
…[5 more quoted lines elided]…
> seen how I'd have reacted back when I still was doing stuff like "sitting
in
> a bar discussing it over a beer"!   I tend to stay out of bars and pubs
and
> the like these days.  "Over coffee", maybe!
>
…[5 more quoted lines elided]…
> Might well have; I do think I'd have at least responded with something
like
> "Stupid is a pretty harsh word, don't you think?"
>
> I might even have gone on to amplify it with an example like:   What if
the
> *reason* a particular person did it that way was that that's the way the
> application architect told him he wanted it, and that if he didn't do it
…[4 more quoted lines elided]…
> would objectively be considered at least as unreasonable as the behavior
of
> a person who did what his employer told him to do!  Which one's taking the
> "stupid" action?
…[5 more quoted lines elided]…
> It certainly wasn't my intent here.  But as I'm sure you've seen in
another
> current thread (about whether unsigned items always have an *explicit*
sign
> on all meaningful architectures) I will question a categorical statement
> when I see that there's a "local" truth, and not a "universal" one,
…[13 more quoted lines elided]…
> etymological one), particularly for terms that others might find
pejorative!

One problem I have seen in Merriam-Webster Online is
that it sometimes does not carry the same sense of words
as when I learned them and, therefore, how I understand
them. The Random House College Dictionary, Revised
Edition, I use is from 1975 and more closely reflects my
understanding, when I read a word, and my intent, when
I use one.

Though the term, 'value judgment', did not occur to me until
yesterday, I had recognized that, when Mr Dashwood used
'stupid', it was an opinion, a 'value judgment', and not an
'absolute fact'. Merriam-Webster Online provides a
'technical' definition of 'value judgment' but the RHCD met
my expectations.

<
http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=value+judgment&x=22
&y=17 >
value judgment:: a judgment assigning a value (as good or bad)
to something

Random House College Dictionary, 1975
value judgment : an estimate of the worth or goodness of
something or someone.

Usage for 'stupid' : Stupid implies natural slowness or dullness
of intellect, or sometimes, a benumbed or dazed state of mind;
it is also used to mean foolish or silly : well-meaning but stupid;
rendered stupid by a blow; It is stupid to do such a thing.

Mr Stevens, that '[stupid] is also used to mean foolish or silly',
as in 'It is stupid to do such a thing', simply reflects usage as
it was in, perhaps, the late 60's and early 70's. For my part,
I can think of no way to unlearn the past, it seems contrary
to the leaning process. Having said that, I do agree that using
words that more accurately reflect such 'value judgments' is
a good thing to learn.
```

###### ↳ ↳ ↳ Re: Authorities

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T13:10:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvmrcF148ia8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <ddabak$581$1@peabody.colorado.edu> <3lt40aF14658jU1@individual.net> <dddh8d$1pnh$1@si05.rsvl.unisys.com> <11fl41pf0gito51@corp.supernews.com>`

```
 
Duly noted. Thanks.

Pete.

TOP POST no more below.

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:11fl41pf0gito51@corp.supernews.com...
>
>
…[147 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-09T23:48:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net>`

```
In article <3lql6iF12jsntU1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> I cannot 'know' that what you call 'red' is exactly what I call 'red'. But 
> we can agree that whatever it is that each of us perceives as 'red' can be 
…[4 more quoted lines elided]…
> here... :-)


I know you don't want this thread deluged with these...but I can't 
resist.

I was out of my single-cup coffee pods this weekend -- so I went to our 
local retailer, Target`, to get some more.

I selected a nice Columbian Roast in a silver box, with the label and 
text written on an orange band around the center of the box.

Imagine my surprise when I opened the box and took the first 
individually wrapped pod out to find that it clearly stated in Black 
letters on Silver background that it was "Decaf Columbian Roast".  My 
wife is still laughing -- she could clearly see the green "decafinated" 
letters above the "Columbian Roast" on the orange background, but I 
still cannot.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-10T22:40:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lu3t5F14com8U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com>`

```
 

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com...
>
> In article <3lql6iF12jsntU1@individual.net>,
…[16 more quoted lines elided]…
>

No, Joe, that was a very fair exception. I enjoyed your story. Thanks.
(At least it wasn't simply contrived for the sake of argument... :-))

> I was out of my single-cup coffee pods this weekend -- so I went to our
> local retailer, Target`, to get some more.
…[10 more quoted lines elided]…
>
I find that fascinating. I always understood that people with this type of 
colour blindness saw grey instead of red or green. You are saying it is 
literally invisible to you? How do you deal with that? Do you know the 
traffic light is red because the other lights are not lit?  What other 
impacts has it had on your life? (Sorry... my interest is causing me to 
forget my manners... it may be a sensitive/personal thing; don't respond 
unless you are OK with it.)

Pete.
```

###### ↳ ↳ ↳ OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 30)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-10T17:49:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O6rKe.173554$9A2.118337@edtnps89>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3lu3t5F14com8U1@individual.net...
> I find that fascinating. I always understood that people with this type of 
> colour blindness saw grey instead of red or green. You are saying it is 
…[4 more quoted lines elided]…
> unless you are OK with it.)

    I'm not colour blind (as far as I know), but my understanding of 
red/green colour-blindness is that it results from the red light and green 
light receptors in one's eyes being indistinguishable to their brain.

    That is to say, typically a person's eyes has three kinds of receptors, 
one for measuring brightness of red, green and blue light respectively. 
Also, typically the brain can tell which signal is coming from which type of 
receptor, and is able to use this information to build a 3 channeled (RGB) 
image in their mind.

    If the brain can't differentiate between the red receptor and the green 
receptor, then I'd imagine it'd be like taking an RGB image and, for every 
pixel, replacing the values of R and G with the average of those two values. 
So if a pixel had the value (2,4,6), for example, it would be perceived as 
(3,3,6).

    With this information a red/green colour blind person could distinguish 
between (what a non-colour blind person would see as) grey and red in that 
grey (128,128,128) would map to (128,128,128) for a colour blind person, 
while red (255,0,0) would map to (128,128,0) for a colour blind person.

    There also exist people who are completely colour blind, in that they 
can't distinguish between information sent from all three of their 
receptors. To simulate this, you could just average out all three channels; 
so as in the example earlier, (2,4,6) would map to (4,4,4), which is indeed 
a shade of grey for us. It might be misleading to call what they see "grey" 
though. If you use the HSL colour space (Hue Saturation Lightness) instead 
of RGB (Red Green Blue), basically these people can perceive Lightness 
normally, but have no Hue or Saturation information. To say that they see 
grey implies that they always see saturation as being zero.

    As for traffic lights, I think if I were colour blind (either red/green 
or all 3), I'd mainly infer the colour of the light from the position of the 
light (in the vertical traffic lights, top is always red and bottom is 
always green; in the horizontal one, the outer ones are red, but I forget 
which is yellow and which is green - though in the horizontal ones they also 
use shapes, and round is green).

    I also heard that most traffic lights now colour the "green" light as 
being blue-green. So a red/green colour blind person would be able to detect 
that the "green" light is one by the presence of blue, but perhaps wouldn't 
be able to differentiate between yellow and red.

    - Oliver
```

###### ↳ ↳ ↳ Re: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-11T11:25:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lvgnhF14d9hgU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89>`

```
 
A very interesting analogy with computer technology. Not sure how accurate 
it is, but it sounds plausible...

Pete.

TOP POST.
"Oliver Wong" <owong@castortech.com> wrote in message 
news:O6rKe.173554$9A2.118337@edtnps89...
>
>
…[56 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 31)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-11T16:16:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123802211.132493.44710@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<O6rKe.173554$9A2.118337@edtnps89>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89>`

```

Oliver Wong wrote:

>     I'm not colour blind (as far as I know), but my understanding of
> red/green colour-blindness is that it results from the red light and green
…[40 more quoted lines elided]…
>

I understand that there are about 6 different forms of colour blindness
and the info I place here is relevant to the one that I suffer from
(red/green I think).

As fas as I know it is not a failure of the brain to distinguish
between the signals coming from the colour receptors (rods or cones but
which I can not remember) but a failure of the specific cells to
distinguish between the wavelengths of light. In my case I am capable
of distinguishing between red and green colours where the colour is
strong (eg when viewing traffic lights or flashing lights on vehicles
from close range) but am less able to differentiate where the colours
are subtle (olive drab as opposed to olive green) or at some
considerable distance (flashing vehicle lights at 400 yards (metres to
DD)). I do not see grey instead of the red or green.

As to lettering, I am amazed at the number of publishers (web and
printed material) who choose colour combos such as lime green and pink
for backgrounds and lettering. I have certainly encountered unreadable
text on packages and leaflets (I could see the text, tell the colour of
it and knew that it was lettering but was unable to read the letter
edges and could not define the letters).

I have a friend who is more disabled wrt colour blindness than myself.
Britannia Music use him to proof read their brochures.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-12T15:27:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m2j97F150rseU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1123802211.132493.44710@z14g2000cwz.googlegroups.com...
<snip>>
> I understand that there are about 6 different forms of colour blindness
> and the info I place here is relevant to the one that I suffer from
…[5 more quoted lines elided]…
> distinguish between the wavelengths of light.

When you consider the TINY difference in frequency between red and green, I 
think it is a miracle that any of us can see them...

> In my case I am capable
> of distinguishing between red and green colours where the colour is
…[5 more quoted lines elided]…
>

So what exactly do you see? Is it just all red or all green? If you were 
looking at a coloured bar with alternating red and green blocks on it, how 
would it appear? Presumably, you still see the bar itself?

> As to lettering, I am amazed at the number of publishers (web and
> printed material) who choose colour combos such as lime green and pink
…[3 more quoted lines elided]…
> edges and could not define the letters).

Ah, so it appears as a blur to you? But not a grey blur?
>
> I have a friend who is more disabled wrt colour blindness than myself.
> Britannia Music use him to proof read their brochures.
>

Thanks very much for this insight, Alistair. It is fascinating. I've often 
wondered about what colour blind people actually 'see' but until now never 
had the opportunity to ask.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 33)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5d7Le.131042$wr.90036@clgrps12>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m2j97F150rseU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3m2j97F150rseU1@individual.net...
>> In my case I am capable
>> of distinguishing between red and green colours where the colour is
…[7 more quoted lines elided]…
> So what exactly do you see? Is it just all red or all green?

    Assuming a person who's completely red/green colour blind (Alistair 
seems to be saying he can sometimes distinguish between the two depending on 
the subtlety of the change), they wouldn't be able to differentiate between 
red and green, and so the question "Do you see red or do you see green?" is 
kind of meaningless to them.

    It's probably a very difficult question to answer in that one does not 
know if the colour one sees is the same as the colour that you call "red".

> Ah, so it appears as a blur to you? But not a grey blur?

    While in an eye-doctor's office (optometrist?) I saw a pamphlet that was 
to help one self-diagnose if they were colour blind. The test was 
surprisingly hard (I checked if my mother found it hard as well; she did, 
which implies either I'm not colour blind, or we're both coloru blind). It 
mainly consisted of very faint yellow text on very faint orange background. 
With (0,0,0) being black and (255,255,255) being white, something like text 
of colour (255,243,204) on background colour (255,230,204). It wasn't that 
the text was blurry (which would imply that I need stronger glasses), but 
that the lighting condition and the angle of viewing had to be just right to 
be able to see the boundaries where the colour-change was occuring.

    - Oliver
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 34)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-13T10:57:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m4nr0F15l7peU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m2j97F150rseU1@individual.net> <5d7Le.131042$wr.90036@clgrps12>`

```

"Oliver Wong" <owong@castortech.com> wrote in message 
news:5d7Le.131042$wr.90036@clgrps12...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:3m2j97F150rseU1@individual.net...
…[15 more quoted lines elided]…
> green?" is kind of meaningless to them.

Well it's just as well it wasn't addressed to you then, isn't it?

There is no need to assume anything. Alistair already said he can see 
red/green when the colours are strong.

I am not wasting his time with meaningless questions, I am trying to 
understand how his perception differs from mine.


>
>    It's probably a very difficult question to answer in that one does not 
> know if the colour one sees is the same as the colour that you call "red".
>
That is not what we are discussing here and has been covered elsewhere.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 35)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-12T21:55:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddjjtt$lnh$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m4nr0F15l7peU1@individual.net>`

```
In article <3m4nr0F15l7peU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>I am not wasting his time with meaningless questions, I am trying to 
>understand how his perception differs from mine.

How his perceptions differ from yours, Mr Dashwood, might just possibly 
not be the same as what he tells you his perceptions are... what his 
perceptions 'are' just might not be the same as what he tells you he 
believes them to be.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 35)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-25T09:40:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124988042.723860.318560@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3m4nr0F15l7peU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m2j97F150rseU1@individual.net> <5d7Le.131042$wr.90036@clgrps12> <3m4nr0F15l7peU1@individual.net>`

```
Sorry about leaving this thread for so long.

My difficulty with colours means that I see neither green or red as
being distinct and identifiably green or red unless I have the other
colour close by as well. I definitely don't see in greys or black and
white just in not very distinguishable colours (when there is a
contrasting colour then the problem resolves itself).

I do use the test for traffick lights (is the light at the top or the
bottom of the lamp) to help at a distance. Unfortunately, in France
this doesn't work as they use such weak lights that I can not see them
until about five feet away. I also have a tendency for slowing for tow
trucks in the mistaken belief that the police are up ahead/behind me.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 36)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-25T16:54:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dekt4s$883$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com>`

```

On 25-Aug-2005, "Alistair" <alistair@ld50macca.demon.co.uk> wrote:

> I do use the test for traffick lights (is the light at the top or the
> bottom of the lamp) to help at a distance

In New Mexico, traffic lights are often horizontal.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-26T10:38:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3n6virF6henU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dekt4s$883$1@peabody.colorado.edu...
>
>
…[6 more quoted lines elided]…
>
I'm stunned. Given that this isn't a joke, can you offer any suggestion as 
to why that would be so?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 38)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-08-26T02:57:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<3n6virF6henU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net>`

```

Pete Dashwood wrote:
>  
> 
…[16 more quoted lines elided]…
> Pete.

The only place I have ever seen horizontal traffic signals was at the 
intersection of Lingbergh boulevard and Missouri Bottom Road.  It may 
not have been a coincidence that this was at the west end of of the 
main runways of Lambert Saint Louis International Airport (STL). 
There was a viewing area on the northwest corner of this intersection 
and planes on landing approach usually passed over at altitudes of 
less than 500 feet.

You may remember that we colonials drive on the righthand side of the 
road.  If I remember correctly, the red light was leftmost, amber in 
the middle, and green was on the right.

Sadly, or perhaps fortunately, the intersection no longer exists.  A 
couple of years ago Lingbergh was re-routed for an airport expansion, 
and it now in a tunnel underneath the new runways being built.

On the other hand, I have never seen a traffic circle or roundabout, 
so perhaps I should count my blessings.

I also have some red/green weakness.  There are some test charts that 
just look like a blob of randomly colored dots to me, with no number 
in the center.  But I have never noticed a problem distinguishing 
between red lights and green lights.  Sometimes I have been unsure of 
flashing amber lights versus flashing red lights.

Of course I have had the experience of shopping with my GF/SO and 
saying, "That's a pretty blue dress in the window", and she might say,
"You idiot, that's Periwinkle!" (or Aqua, or Turquoise).  Whatever it 
is, my perceptions are obviously not sufficiently discriminating.

With kindest regards,
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 39)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T05:19:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<demmqh$o3$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>Of course I have had the experience of shopping with my GF/SO and 
>saying, "That's a pretty blue dress in the window", and she might say,
>"You idiot, that's Periwinkle!" (or Aqua, or Turquoise).  Whatever it 
>is, my perceptions are obviously not sufficiently discriminating.

Not to worry, Mr Trembley... with diligence and practise one might, some 
day, learn to differentiate between beige and taupe.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 40)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-26T13:45:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<den6ef$i50$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net> <demmqh$o3$1@panix5.panix.com>`

```

On 26-Aug-2005, docdwarf@panix.com wrote:

> Not to worry, Mr Trembley... with diligence and practise one might, some
> day, learn to differentiate between beige and taupe.

The other day, I mentioned to a female co-worker that guys often (and myself in
specific) don't know what color "taupe" is.    The first thing she did was
mention how well I illustrated my statement - I did not pronounce the word
correctly.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 41)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T10:03:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<den7fs$lt7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net> <demmqh$o3$1@panix5.panix.com> <den6ef$i50$1@peabody.colorado.edu>`

```
In article <den6ef$i50$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 26-Aug-2005, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>correctly.

This brings to mind an interesting possibility... categorising not by 
color-name but by light-wavelength, in the usual 400 - 700nm range.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 42)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-26T16:19:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denfek$mvp$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net> <demmqh$o3$1@panix5.panix.com> <den6ef$i50$1@peabody.colorado.edu> <den7fs$lt7$1@panix5.panix.com>`

```

On 26-Aug-2005, docdwarf@panix.com wrote:

> This brings to mind an interesting possibility... categorising not by
> color-name but by light-wavelength, in the usual 400 - 700nm range.

That works for "pure" colors.   Where is brown in the rainbow?
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 43)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T12:53:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denhee$jc8$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <den6ef$i50$1@peabody.colorado.edu> <den7fs$lt7$1@panix5.panix.com> <denfek$mvp$1@peabody.colorado.edu>`

```
In article <denfek$mvp$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 26-Aug-2005, docdwarf@panix.com wrote:
…[4 more quoted lines elided]…
>That works for "pure" colors.   Where is brown in the rainbow?

At the feet of it, where it hits the mud.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 44)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-26T17:35:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denjsm$pe8$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <den6ef$i50$1@peabody.colorado.edu> <den7fs$lt7$1@panix5.panix.com> <denfek$mvp$1@peabody.colorado.edu> <denhee$jc8$1@panix5.panix.com>`

```

On 26-Aug-2005, docdwarf@panix.com wrote:

> >That works for "pure" colors.   Where is brown in the rainbow?
>
> At the feet of it, where it hits the mud.

That Leprechaun lied to me!
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 45)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T17:07:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<deo0b2$6r7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <denfek$mvp$1@peabody.colorado.edu> <denhee$jc8$1@panix5.panix.com> <denjsm$pe8$1@peabody.colorado.edu>`

```
In article <denjsm$pe8$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 26-Aug-2005, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>That Leprechaun lied to me!

He probably thought you were after his Lucky Charms.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 46)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-27T06:33:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <denfek$mvp$1@peabody.colorado.edu> <denhee$jc8$1@panix5.panix.com> <denjsm$pe8$1@peabody.colorado.edu> <deo0b2$6r7$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:deo0b2$6r7$1@panix5.panix.com...
> In article <denjsm$pe8$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[11 more quoted lines elided]…
> DD

Well they're Magically Delicious.

JCE
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 47)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-27T04:16:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dep7hf$mma$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <denjsm$pe8$1@peabody.colorado.edu> <deo0b2$6r7$1@panix5.panix.com> <1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com>`

```
In article <1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:deo0b2$6r7$1@panix5.panix.com...
>> In article <denjsm$pe8$1@peabody.colorado.edu>,
…[13 more quoted lines elided]…
>Well they're Magically Delicious.

They might be... but there's only one Breakfast of Champions.

(no, not the cereal... an unfiltered Camel cigarette and a cup of black 
coffee with a healthy jolt o' Scotch in it... ahhhhhh, for the Oldene 
Dayse!)

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 48)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-29T14:54:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dev7jk01uql@news2.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <denjsm$pe8$1@peabody.colorado.edu> <deo0b2$6r7$1@panix5.panix.com> <1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com> <dep7hf$mma$1@panix5.panix.com>`

```

In article <dep7hf$mma$1@panix5.panix.com>, docdwarf@panix.com writes:
> They might be... but there's only one Breakfast of Champions.
> 
> (no, not the cereal... an unfiltered Camel cigarette and a cup of black 
> coffee with a healthy jolt o' Scotch in it... ahhhhhh, for the Oldene 
> Dayse!)

"Talking, drinking, and smoking go better together than any three
other pleasant things on this earth."  -- Arthur Ransome, _Bohemia
in London_, 1907.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 49)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-29T11:47:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<devan8$sf2$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com> <dep7hf$mma$1@panix5.panix.com> <dev7jk01uql@news2.newsguy.com>`

```
In article <dev7jk01uql@news2.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>In article <dep7hf$mma$1@panix5.panix.com>, docdwarf@panix.com writes:
…[8 more quoted lines elided]…
>in London_, 1907.

Hmmmmm... obviously he didn't encounter the time when I was with those two 
college-lasses who were interested in some... experiments in human 
engineering, as it were...

... oh... he said '*three* pleasant things', the two lasses plus me 
wouldn't total that... as you were, gentlemen and others...

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 50)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-30T18:12:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df27iv0669@news3.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1PTPe.86300$dJ5.29213@tornado.tampabay.rr.com> <dep7hf$mma$1@panix5.panix.com> <dev7jk01uql@news2.newsguy.com> <devan8$sf2$1@panix5.panix.com>`

```

In article <devan8$sf2$1@panix5.panix.com>, docdwarf@panix.com writes:
> In article <dev7jk01uql@news2.newsguy.com>,
> Michael Wojcik <mwojcik@newsguy.com> wrote:
…[13 more quoted lines elided]…
> engineering, as it were...

At the time, poor Arthur's romantic adventures had not turned out
well, on the whole.  Indeed, it wasn't until he slipped into post-
revolution Russia and smuggled out Evgenia Petrovna, Trotsky's
personal secretary, that he found lasting happiness in female
companionship.  They didn't become acquainted until some ten years
after he wrote _Bohemia_.  But then as he notes in the final
chapter of that book, Bohemia is but a stage in a man's life, and
perhaps talking, drinking, and smoking may in later days sometimes
take a back seat.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 51)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-31T05:11:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df3s8g$bpr$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dev7jk01uql@news2.newsguy.com> <devan8$sf2$1@panix5.panix.com> <df27iv0669@news3.newsguy.com>`

```
In article <df27iv0669@news3.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>In article <devan8$sf2$1@panix5.panix.com>, docdwarf@panix.com writes:
…[25 more quoted lines elided]…
>take a back seat.

There's always hope for change, aye... one can get tired even of 
butter-cookies.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 42)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-26T18:03:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denlhu01oqe@news2.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net> <demmqh$o3$1@panix5.panix.com> <den6ef$i50$1@peabody.colorado.edu> <den7fs$lt7$1@panix5.panix.com>`

```

In article <den7fs$lt7$1@panix5.panix.com>, docdwarf@panix.com writes:
> In article <den6ef$i50$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[7 more quoted lines elided]…
> color-name but by light-wavelength, in the usual 400 - 700nm range.

That's not sufficient information.  Color is composed of three
attributes (in the standard models): hue, saturation, and
reflectivity.  Hue describes the dominant wavelength of reflected
(or transmitted) light; saturation the "purity" of that hue (ie
the signal/noise ratio of the color, or what fraction of the total
reflected light is actually of that frequency); and reflectivity
(or transmissivity, or emissivity, depending on where the light is
coming from) is how much of the incident light is reflected (or
transmitted or emitted).

All color models have to accomodate this information in some fashion.
Some, like HLS (hue/lightness/saturation) capture it directly, with
three real-valued numbers between 0 and 1.  Others, like RGB or CMYK
(which is the complement of RGB, and is typically used for reflected
colors where RGB is generally used for transmitted ones), do so
indirectly; the hue, saturation, and reflectivity are functions of
the color components.  (If all of R, G, and B are 0, then
reflectivity is 0; if they're all 1, then saturation is 0; and so
forth.)  Still others, like Pantone, basically just label a whole
bunch of reference colors; the reference colors themselves embody
the hue/saturation/reflectivity information.

One common-sense description of the three: if you have a paint that's
has only one pigment which reflects a single wavelength, then that's
your hue, and saturation and reflectivity are both 1 (maximum).  Add
white paint to it and you reduce saturation; add black paint and you
reduce reflectivity.

Taupe is defined by one online dictionary I checked as "an orange of
low and brightness and saturation", for example.  Orange is the hue
(that is, the hue falls somewhere in the part of the spectrum that's
traditionally called "orange" by people who speak English and are
interested in defining such things), the "low brightness" means it's
not particularly light, and the "low saturation" means it's more of
a pastel or even grey color.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 43)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T17:11:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<deo0h7$5su$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <den6ef$i50$1@peabody.colorado.edu> <den7fs$lt7$1@panix5.panix.com> <denlhu01oqe@news2.newsguy.com>`

```
In article <denlhu01oqe@news2.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>In article <den7fs$lt7$1@panix5.panix.com>, docdwarf@panix.com writes:
…[11 more quoted lines elided]…
>That's not sufficient information.

By ignorance my suggestion might be... colored.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 39)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-26T23:33:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3n8cvkFbm9oU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>`

```
 
Thanks Arnold. Interesting.

This whole idea of "what do you see, and is it the same as what I see?" is 
really fascinating and it is no surprise it has kept, not just medical 
practitioners occupied for centuries, but also philosophers and scientists.

Maybe someday we'll be able to connect ourselves directly to each other 
(like Spock's Vulcan mind probe :-)) and truly 'see' what others perceive.

Hey, imagine a 'human LAN' with people sharing each other's sensory organs 
(lust like a LAN shares printers or hard drives) and being able to transfer 
their thoughts instantly to anyone on the network...

I wonder... :-)

Pete.

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net...
>
> Pete Dashwood wrote:
…[53 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 40)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-26T16:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denfd9$mta$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net> <3n8cvkFbm9oU1@individual.net>`

```

On 26-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> This whole idea of "what do you see, and is it the same as what I see?" is
> really fascinating and it is no surprise it has kept, not just medical
> practitioners occupied for centuries, but also philosophers and scientists.

As a kid I was amused by that concept.   But as an adult I realized that it only
mattered if it mattered.   That is if to someone pink wasn't a whitish red. 
Might as well say that there's no guarantee that we both see the same thing when
we look at a building or when we feel a heavy weight or when we smell sulfur.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 39)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-26T12:27:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<den1rh01ksh@news4.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>`

```

In article <iyvPe.674979$cg1.49606@bgtnsc04-news.ops.worldnet.att.net>, Arnold Trembley <arnold.trembley@worldnet.att.net> writes:
> 
> On the other hand, I have never seen a traffic circle or roundabout, 
> so perhaps I should count my blessings.

They're really not that bad.  Once the locals learn how to use them,
they usually offer somewhat better throughput and much lower latency
than light-controlled intersections, and less potential for confusion
than all-way stops.

A few have gone in around here (the East Lansing area) in the past
few years, and after some initial suspicion local drivers have found
they prefer them, and now the preferred routes take the circles and
avoid the lights.

I learned to drive in Massachusetts, which has some of the worst
traffic circles ("rotaries" in local parlance) in the nation: ones
with light controls at some entrances and a parking lot in the middle
(Salem, now replaced with light-controlled intersections); ones with
multiple conjoined circles (East Longmeadow); ones with lights and
obscured visibility and roads cutting through the center of the
circle (Revere).  (Yes, I know about Swindon's Magic Roundabout,[1]
and I don't think it's in the running here.  In fact, I think it's a
fairly good idea.)

All of those, while bad, were usable.  In Salem's case (Washington
Square), I've been able to compare the traffic circle approach with
the light-controlled intersection approach, since they changed it.
The latter may be less confusing for out-of-town drivers (we towed
many a visitor's car from there back in the traffic circle days), but
it's not any better at getting traffic through, as far as I can tell.


1. http://www.swindonweb.com/life/lifemagi0.htm
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 38)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-26T12:13:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<den11c01utd@news1.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net>`

```

In article <3n6virF6henU1@individual.net>, "Pete Dashwood" <dashwood@enternet.co.nz> writes:
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:dekt4s$883$1@peabody.colorado.edu...
…[9 more quoted lines elided]…
> to why that would be so?

They're mostly horizontal in various other places, too, such as
Lincoln, Nebraska.  (Yet Another reason to avoid Lincoln, Nebraska.)
And one color-blind acquaintance had the unpleasant experience of
driving through a small city somewhere in Mississippi that had
vertical traffic lights with red at the bottom.

Traffic lights aren't standardized in the US.  They're left to the
whims of local traffic engineers and transportation bureaucrats.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 38)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-26T13:43:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<den697$i4j$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net>`

```

On 25-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> > In New Mexico, traffic lights are often horizontal.
> >
> I'm stunned. Given that this isn't a joke, can you offer any suggestion as
> to why that would be so?

Not where I've seen it.   I could see it in hurricane country, but (giving room
for an obvious joke), why in Roswell?
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 39)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-08-26T10:02:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MhFPe.1750$Rc.511543@news20.bellglobal.com>`
- **In-Reply-To:** `<den697$i4j$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <3n6virF6henU1@individual.net> <den697$i4j$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 25-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
> 
…[9 more quoted lines elided]…
> for an obvious joke), why in Roswell?

Obviously a joke that fell flat.

Donald
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 37)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-26T08:34:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125070471.094290.166980@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dekt4s$883$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu>`

```
Another part of the US that I won't be visiting.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 38)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-26T19:06:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<denp6q07st@news3.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <1125070471.094290.166980@g43g2000cwa.googlegroups.com>`

```

In article <1125070471.094290.166980@g43g2000cwa.googlegroups.com>, "Alistair" <alistair@ld50macca.demon.co.uk> writes:
> Another part of the US that I won't be visiting.

What is?  You didn't quote any antecedent.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 39)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-26T14:49:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125092970.092558.104830@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<denp6q07st@news3.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <1125070471.094290.166980@g43g2000cwa.googlegroups.com> <denp6q07st@news3.newsguy.com>`

```
It seems that my missive has been separated from the item to which it
referred. I think it might have referred to the Mississippi but then
most of the US is of no interest for me (I do like the idea of visiting
the French Quarter of New Orleans, though).
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 40)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-28T14:29:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<desho10261j@news2.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <1125070471.094290.166980@g43g2000cwa.googlegroups.com> <denp6q07st@news3.newsguy.com> <1125092970.092558.104830@g14g2000cwa.googlegroups.com>`

```

In article <1125092970.092558.104830@g14g2000cwa.googlegroups.com>, "Alistair" <alistair@ld50macca.demon.co.uk> writes:
> It seems that my missive has been separated from the item to which it
> referred.

Usenet is a nondeterministic medium.  Some readers may see your
article before the one you respond to; some may never see the one you
respond to.  Some may see yours after their server has already
expired the one you're responding to, so even if they have read it,
they'll no longer have it for reference.

Also, not everyone uses threading readers.  (I don't, because I don't
think the advantages of a threaded view are worth the additional
overhead of downloading the References headers for all the messages
and sorting them before presenting the message list for a group, and
because I don't particularly care for the visual presentation of
threads in any of the readers I've used.)

In short, if you want all of your readers to know what you're
referring to, you need to quote the relevant part of the original
message.  I see you're using Google Groups, which unfortunately has
many misfeatures and a brain-dead interface.  (Google's self-
promotion notwithstanding, they have some really poor software
development practices, and their "motto" is a load of marketing
hooey.)  Several people like to cite Keith Thompson's advice for
Google users, originally posted to comp.lang.c:

   If you want to post a followup via groups.google.com, don't use 
   the broken "Reply" link at the bottom of the article.  Click on 
   "show options" at the top of the article, then click on the 
   "Reply" at the bottom of the article headers.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 41)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-09-09T10:41:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126287711.968227.178520@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<desho10261j@news2.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988042.723860.318560@g49g2000cwa.googlegroups.com> <dekt4s$883$1@peabody.colorado.edu> <1125070471.094290.166980@g43g2000cwa.googlegroups.com> <denp6q07st@news3.newsguy.com> <1125092970.092558.104830@g14g2000cwa.googlegroups.com> <desho10261j@news2.newsguy.com>`

```

Michael Wojcik wrote:
> In article <1125092970.092558.104830@g14g2000cwa.googlegroups.com>, "Alistair" <alistair@ld50macca.demon.co.uk> writes:
> > It seems that my missive has been separated from the item to which it
…[11 more quoted lines elided]…
> chemistry of HS + N{_2}O(n,1,0) using stimulated Raman excitation".

Google is definitely a pain. I used to use a package from Demon which
was brilliant but in upgrading to broadband that got junked. Hence the
infrequent use of Google.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 36)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-26T10:37:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3n6vgrF6csmU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m2j97F150rseU1@individual.net> <5d7Le.131042$wr.90036@clgrps12> <3m4nr0F15l7peU1@individual.net> <1124988042.723860.318560@g49g2000cwa.googlegroups.com>`

```
 
Thanks very much for that insight, Alistair.

Pete.

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1124988042.723860.318560@g49g2000cwa.googlegroups.com...
> Sorry about leaving this thread for so long.
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 33)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-25T09:44:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124988242.853921.324230@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3m2j97F150rseU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <3m2j97F150rseU1@individual.net>`

```
As an aside, I remember reading a book (Biggles or Gimlet) in which a
colour blind Japanese sniper was allowed, by the hero, to run through
the jungle using a red handkerchief instead of a white surrender flag.
With the result that he was shot by his own side. Dashed unsporting.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-25T12:51:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<deksuq$in1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <1124988242.853921.324230@g14g2000cwa.googlegroups.com>`

```
In article <1124988242.853921.324230@g14g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>As an aside, I remember reading a book (Biggles or Gimlet) in which a
>colour blind Japanese sniper was allowed, by the hero, to run through
>the jungle using a red handkerchief instead of a white surrender flag.
>With the result that he was shot by his own side. Dashed unsporting.

His run might have been a dash, certainly... but 'unsporting'?  Wasn't 
there an Auld Blighter who coined a phrase about what is fair in love and 
war?

(Stratford-upon-Avon Rules of Engagement: First, all challenges must be 
issued in iambic pentameter...)

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 35)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-26T08:30:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125070229.530132.144090@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<deksuq$in1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <1124988242.853921.324230@g14g2000cwa.googlegroups.com> <deksuq$in1$1@panix5.panix.com>`

```
I do not expect childhood heroes to behave in such an underhand
fashion. I was not at that stage aware of being colourblind but I took
the action as being tantamount to murder.

We haven't used Iambic Pentameter since Bill Wagglestaffs' days.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-26T12:05:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<deneka$fg7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988242.853921.324230@g14g2000cwa.googlegroups.com> <deksuq$in1$1@panix5.panix.com> <1125070229.530132.144090@g43g2000cwa.googlegroups.com>`

```
In article <1125070229.530132.144090@g43g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>I do not expect childhood heroes to behave in such an underhand
>fashion.

Blessed is one who has few expectations; disappointments might be less 
frequent.  Feats of glory and honor might be accomplished by those who 
have feets of clay.

>I was not at that stage aware of being colourblind but I took
>the action as being tantamount to murder.

Oh, come now... one murders, usually, people; didn't everyone in those 
days accept it as fact that Enemies of a Differing Race just weren't human 
beings?

>
>We haven't used Iambic Pentameter since Bill Wagglestaffs' days.

And look what's happened since... ahhhhhh, for the Oldene Dayse, when an 
iamb could be pentametered such as *ten* iambs cannot, today!

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 37)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-26T14:52:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125093133.044861.206160@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<deneka$fg7$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1124988242.853921.324230@g14g2000cwa.googlegroups.com> <deksuq$in1$1@panix5.panix.com> <1125070229.530132.144090@g43g2000cwa.googlegroups.com> <deneka$fg7$1@panix5.panix.com>`

```
I thought it was five iambs not ten to a Penatemeter, unless bloody
Europe has gone and decimalised Iambic Pentameter too!
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 38)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-27T04:19:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dep7mt$nqk$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1125070229.530132.144090@g43g2000cwa.googlegroups.com> <deneka$fg7$1@panix5.panix.com> <1125093133.044861.206160@g49g2000cwa.googlegroups.com>`

```
In article <1125093133.044861.206160@g49g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>I thought it was five iambs not ten to a Penatemeter, unless bloody
>Europe has gone and decimalised Iambic Pentameter too!

That might be why *an* iamb could be pentametered such as *ten* cannot, 
today... or maybe it was something in the water.

DD
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-12T13:44:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddi94m$nfg$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123802211.132493.44710@z14g2000cwz.googlegroups.com>`

```

On 11-Aug-2005, "Alistair" <alistair@ld50macca.demon.co.uk> wrote:

> As to lettering, I am amazed at the number of publishers (web and
> printed material) who choose colour combos such as lime green and pink
> for backgrounds and lettering.

That could work as long as they also vary the greyness of the pigments.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 33)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-08-26T14:53:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125093203.322423.79950@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<ddi94m$nfg$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1123802211.132493.44710@z14g2000cwz.googlegroups.com> <ddi94m$nfg$1@peabody.colorado.edu>`

```
Greyness does not enter into it. I see greens and reds but just not so
emphatically.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 31)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-15T15:53:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddqdqb0b1l@news3.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89>`

```

In article <O6rKe.173554$9A2.118337@edtnps89>, "Oliver Wong" <owong@castortech.com> writes:
> 
>     That is to say, typically a person's eyes has three kinds of receptors, 
…[3 more quoted lines elided]…
> image in their mind.

It's my understanding that this theory has largely fallen out of
favor, due to the lack of physiological evidence to support it.  Of
course there are many ways to encode a color signal; three-channel
RGB has precedents in some technologies, but there's no reason to
believe that's how the human eye works.

There are *two* distinct structures in the retina, "rods" and
"cones".  They have different sensitivity functions to light by
frequency.  The difference in response between the rods and the
cones is sufficient information to derive the frequency, so it's
quite plausible that that's how human color vision works.

Since cones are overall less sensitive than rods (they have a higher
excitation threshold), in low light color vision is diminished - the
brain doesn't get enough of a signal from the cones to find the
delta, and hence the frequency.

People with diminished color vision in well-lit environments seem to
have a cone response curve that's insufficiently different from the
rod response curve for certain frequencies.  That problem is
aggravated by color input that's not highly saturated, because
there's less of a frequency-specific component to create the
different response levels.

Thus the typical "color-bind" individual actually has a specific
condition such as "reduced green response", where the regions of
the two receptor types' response curves for greens and some
neighboring red hues are mostly parallel - so there is little
information for the brain to distinguish among frequencies in that
region.

There are also rare cases of complete color blindness, usually caused
by brain damage.  Oliver Sacks documents one; the patient could see
no color at all, following an automobile accident (which may have
been caused by a small stroke).  Everything appears to be some shade
of grey.  In this case I suspect that the area of the visual cortex
which processes the difference between the rod and cone signals was
itself damaged.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 32)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-15T19:02:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qF5Me.179168$9A2.83625@edtnps89>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <ddqdqb0b1l@news3.newsguy.com>`

```

"Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
news:ddqdqb0b1l@news3.newsguy.com...
>
> In article <O6rKe.173554$9A2.118337@edtnps89>, "Oliver Wong" 
…[12 more quoted lines elided]…
> favor, due to the lack of physiological evidence to support it.

    I thought "3 kinds of receptors" (I didn't know the technical terms when 
I made that first post) was the current most popular theory. From Wikipedia 
(http://en.wikipedia.org/wiki/Color_vision):

Perception of color is achieved in mammals through color receptors 
containing pigments with different spectral sensitivities. In most Old World 
primates there are three types of color receptors, known as cone cells, that 
are maximally receptive to short, medium, and long wavelengths of light 
(known as S-, M-, and L-cones and roughly corresponding to blue, green, and 
yellow), allowing for trichromatic color vision.

Of course, Wikipedia may be wrong and/or out of date, but I had heard from 
another source (I think it was around 3 or 4 years ago from a university 
professor doing research in robot/AI vision) that this was the currently how 
human vision is understood to work.

> Of
> course there are many ways to encode a color signal; three-channel
> RGB has precedents in some technologies, but there's no reason to
> believe that's how the human eye works.

    I don't know the timelines, but if human vision was "understood" before 
cathode ray tubes were develop, one could imagine how CRTs might have been 
designed to use RGB specifically to establish a compatible interface with 
the human eye.

    But if CRTs were develop before human vision was understood, then I 
don't know. =)

    - Oliver
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 33)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-15T13:02:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124135699.086092.317370@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<qF5Me.179168$9A2.83625@edtnps89>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <ddqdqb0b1l@news3.newsguy.com> <qF5Me.179168$9A2.83625@edtnps89>`

```
> but if human vision was "understood" before cathode ray tubes were develop,

Why does this need to be CRTs ?  RGB may be based on observations with
'Magic Lantens' or even coloured glass windows.
```

###### ↳ ↳ ↳ Re: OT: Colour blindness [Was: Re: "Shared" procedure division code]

_(reply depth: 33)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-17T20:11:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<de05l201tah@news4.newsguy.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net> <O6rKe.173554$9A2.118337@edtnps89> <ddqdqb0b1l@news3.newsguy.com> <qF5Me.179168$9A2.83625@edtnps89>`

```

In article <qF5Me.179168$9A2.83625@edtnps89>, "Oliver Wong" <owong@castortech.com> writes:
> "Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
> news:ddqdqb0b1l@news3.newsguy.com...
…[11 more quoted lines elided]…
> I made that first post) was the current most popular theory.

Hmm.  Maybe the article I read wasn't as mainstream as I thought.
I'll have to track it down and take another look.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-08-12T21:38:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-04CD31.21382312082005@ispnews.usenetserver.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <xDiIe.35066$iG6.10400@tornado.tampabay.rr.com> <dcsvgi$np4$1@panix5.panix.com> <3lftfrF10nd9jU1@individual.net> <dcvjkv$gap$1@panix5.panix.com> <3lik42F12ra7rU1@individual.net> <7sQJe.192230$tt5.56640@edtnps90> <3lql6iF12jsntU1@individual.net> <joe_zitzelberger-5B05B4.23484309082005@ispnews.usenetserver.com> <3lu3t5F14com8U1@individual.net>`

```
In article <3lu3t5F14com8U1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> > Imagine my surprise when I opened the box and took the first
> > individually wrapped pod out to find that it clearly stated in Black
…[11 more quoted lines elided]…
> unless you are OK with it.)

If I hold the silver box with broad orange band in bright light AND I 
tilt it just so, I can pick up a glimmer of some small, rectangular area 
that might be text centered above the line of black letters that say  
"Columbian Roast".

But I cannot read it at all.  It looks like a printer error.  Looking 
straight on, or with any sort of less-than-super-bright light, all I see 
is orange.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-08-02T17:56:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QsOHe.322$9U3.315@newssvr24.news.prodigy.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:dco8co$a29$1@peabody.colorado.edu...
> But I can say:
>
…[5 more quoted lines elided]…
> "I believe Connecticut is the capital of North Dakota".

Sadly, your geography skills are all too representative of  "Da Yoot of
America."

MCM
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T14:36:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcoefu$7n1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <QsOHe.322$9U3.315@newssvr24.news.prodigy.net>`

```
In article <QsOHe.322$9U3.315@newssvr24.news.prodigy.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
>"Howard Brazee" <howard@brazee.net> wrote in message
>news:dco8co$a29$1@peabody.colorado.edu...
…[10 more quoted lines elided]…
>America."

Leaving aside that Mr Brazee was not confessing belief but merely stating 
what he is capable of saying...

... ahhhhh, for the Oldene Dayse, when a youth could have geography skills 
such as *ten* youths cannot, today!

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-02T19:16:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcogqk$eij$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <QsOHe.322$9U3.315@newssvr24.news.prodigy.net> <dcoefu$7n1$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> Leaving aside that Mr Brazee was not confessing belief but merely stating
> what he is capable of saying...

Of course being semantically correct can get one misunderstood or in trouble -
such as demanding that my teacher give me an "A" for answering every question
correctly (if that's what she promised), and I correctly answer "I don't know"
to each answer.

Some of the answers and questions on Jeopardy could be like this.    Reverse
them and you will rarely get full credit for knowing the answer:

Question: Who was Abraham Lincoln?    Answer: Winston Churchill reported seeing
his ghost in the bedroom.

Semantically one can reply "What is a Jeopardy answer".   But that "correct"
answer won't get any money.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T19:40:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp09d$lbl$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <QsOHe.322$9U3.315@newssvr24.news.prodigy.net> <dcoefu$7n1$1@panix5.panix.com> <dcogqk$eij$1@peabody.colorado.edu>`

```
In article <dcogqk$eij$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>to each answer.

Doing or not-doing anything can have identical results; as my Sainted 
Mother - may she sleep with the angels! - told me when I started my first 
job 'When it comes to work just remember two things: you can be wrong 
about something... and be fired for it, you can be right about 
something... and be fired for it.'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T12:15:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lagkcF11qlvhU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <QsOHe.322$9U3.315@newssvr24.news.prodigy.net> <dcoefu$7n1$1@panix5.panix.com> <dcogqk$eij$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dcogqk$eij$1@peabody.colorado.edu...
>
>
…[12 more quoted lines elided]…
>

ROFL! This is superb! I don't know whether you originated that, Howard, but 
it sure made me laugh. It is so good I shall definitely steal it.

> Some of the answers and questions on Jeopardy could be like this. 
> Reverse
…[9 more quoted lines elided]…
>
Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-03T05:26:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DAYHe.31404$iG6.17081@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco6r9$3hl$1@panix5.panix.com> <dco8co$a29$1@peabody.colorado.edu> <QsOHe.322$9U3.315@newssvr24.news.prodigy.net> <dcoefu$7n1$1@panix5.panix.com> <dcogqk$eij$1@peabody.colorado.edu> <3lagkcF11qlvhU1@individual.net>`

```
This goes with the famous scene from Grange Hill (for those not english here 
it was a "soap" set in a high school)
They released the new "rule book" among them was the gem:

"Children must walk in the corridors at all times".

JCE

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3lagkcF11qlvhU1@individual.net...
>
>
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T11:54:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lafd0F11uiclU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dco6r9$3hl$1@panix5.panix.com...
>
> In article <dco4eq$7tn$1@peabody.colorado.edu>,
…[15 more quoted lines elided]…
> Do you believe that... or do you just believe that you believe that?

I believe you are being deliberately obtuse and you said the above with 
tongue in cheek :-)
>
>>
…[4 more quoted lines elided]…
>

Precisely. Howard is right. (I should have said: "I believe Howard is 
right." to avoid offending certain sensibilities; doing that makes him no 
more or less right.)

> I do not understand what you are calling 'validity' or how it can be
> applied differently to opinions.

Hahaha! Doc, you know as well as anyone here the difference between truth 
and validity. This is a wind up... :-)

Pete
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:40:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp7at$6nl$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <3lafd0F11uiclU1@individual.net>`

```
In article <3lafd0F11uiclU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[21 more quoted lines elided]…
>tongue in cheek :-)

Who said we must speak of truth and not smile? - Cicero

>>
>>>
…[14 more quoted lines elided]…
>and validity. This is a wind up... :-)

I barely know what I know, Mr Dashwood, let alone anyone else... and I 
still do not understand what Mr Brazee was calling 'validity' or how it 
can be applied differently to opinions.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T14:47:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqleg$l7e$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com>`

```

On  2-Aug-2005, docdwarf@panix.com wrote:

> >If you added "I believe" to the above, it wouldn't have changed its validity
> >one
…[3 more quoted lines elided]…
> applied differently to opinions.

I'm interested that these aren't worded as questions, so you are not literally
"answering a question with a question".

But I fail to see that the difference is significant.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T10:54:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqlrt$irv$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco4eq$7tn$1@peabody.colorado.edu> <dco6r9$3hl$1@panix5.panix.com> <dcqleg$l7e$1@peabody.colorado.edu>`

```
In article <dcqleg$l7e$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  2-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>"answering a question with a question".

How pleasant that you find something of interest, certainly.

>
>But I fail to see that the difference is significant.

Perhaps once I better understand what is being called 'validity' this 
might be examined.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T11:48:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3laf38F11smc5U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dco2qp$dgq$1@panix5.panix.com...
>
> In article <dco0l7$60r$1@peabody.colorado.edu>,
…[19 more quoted lines elided]…
> five times five is twenty-five' belong to the set of 'everything'.

<DISCLAIMER - following is Pete's opinion: not intended to offend anyone, 
forgive any perceived rudeness, observations may not apply to Unisys sites>

Ah, but are they "absolute facts"?  So long as everyone who experiences them 
agrees they are, then they can be admitted to be "real", but that doesn't 
make them "absolute". We require an agreed reality in order to interact with 
other human beings. If you lived alone in the world the capital of North 
Dakota could be anything you chose it to be, assuming you elected to even 
have a State of North Dakota. While there is no denying that in base ten we 
all agree "five times five is twenty-five", this is simply an idea. The 
Uncertainty Principle tells us that in the physical universe there is only a 
probability that taking five groups of five things will result in twenty 
five things.

</DISCLAIMER>

Pete.


> DD
>
>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-02T21:49:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcp7qp$sd2$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <3laf38F11smc5U1@individual.net>`

```
In article <3laf38F11smc5U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[27 more quoted lines elided]…
>Ah, but are they "absolute facts"?

In that they are 'having no restriction, exception or qualification' they 
appear to be asserted as absolutes 
(http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=absolute&x=0&y=0) as 
Mr Stevens observed.

>So long as everyone who experiences them 
>agrees they are, then they can be admitted to be "real", but that doesn't 
>make them "absolute".

So long as a commonly-accepted source of use indicates a definition which 
seems to fit, Mr Dashwood, then the misunderstanding might be seen as 
easily achieved.

'I have a radical idea!'

'You have an idea that relates to a root?'

'No, I have an idea that's marked by a considerable departure from the 
usual or traditional... what's this about 'roots'?  That's stupid!'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T00:35:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lbs0rF11m239U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <3laf38F11smc5U1@individual.net> <dcp7qp$sd2$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcp7qp$sd2$1@panix5.panix.com...
>
> In article <3laf38F11smc5U1@individual.net>,
…[39 more quoted lines elided]…
>

As things that are outside my experience cannot be part of my experience, 
there is qualification, may well be exception, and may also be restriction. 
My comments were limited (as they always are) to things within my 
experience. Anyway, I don't accept this definition so it is moot... (it 
isn't even real for me if I disagree with it...:-))

>>So long as everyone who experiences them
>>agrees they are, then they can be admitted to be "real", but that doesn't
…[11 more quoted lines elided]…
> usual or traditional... what's this about 'roots'?  That's stupid!'

If one party uses radical in one sense and the other party's understanding 
does not include that sense, then a misunderstanding may well occur. Reading 
the above, a reasonable person would accept that the second exclamation is 
true for the person making it. If the excalmation had been qualified as "I 
think that's stupid!" it would be no more or less true.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T09:40:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqhgt$1pp$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3laf38F11smc5U1@individual.net> <dcp7qp$sd2$1@panix5.panix.com> <3lbs0rF11m239U1@individual.net>`

```
In article <3lbs0rF11m239U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[7 more quoted lines elided]…
>>>news:dco2qp$dgq$1@panix5.panix.com...

[snip]

>>>> Is that a fact?  Plural majestatus est, Mr Brazee... and I believe that
>>>> statements like 'Bismarck is the capital of North Dakota' and 'in base 
…[18 more quoted lines elided]…
>isn't even real for me if I disagree with it...:-))

... and when you use a word it means what you want it to, no more, no 
less?

>>>So long as everyone who experiences them
>>>agrees they are, then they can be admitted to be "real", but that doesn't
…[16 more quoted lines elided]…
>true for the person making it.

Ahhhh, there's the nub... 'a reasonable person' would supply the 
qualifications of experience to all statements made by another; I have to 
disagree.  I barely know what *I* am qualifying, let alone anyone else; 
the statements of another stand as the originator/author made them.

>If the excalmation had been qualified as "I 
>think that's stupid!" it would be no more or less true.

You seem to be saying 'that is' can be universally semantically equated to 
'I think that is'... am I correct in concluding this?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T03:17:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lc5fkF11uur6U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3laf38F11smc5U1@individual.net> <dcp7qp$sd2$1@panix5.panix.com> <3lbs0rF11m239U1@individual.net> <dcqhgt$1pp$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcqhgt$1pp$1@panix5.panix.com...
>
> In article <3lbs0rF11m239U1@individual.net>,
…[44 more quoted lines elided]…
>
I'm not quite as bad as Humpty Dumpty, and I try to stick to accepted 
definitions (the "facts"), but I would not be above defining a word in the 
sense in which I am using it. Sometimes culture differences require it. I 
have already seen from this forum that the meaning of "urban myth" in 
America is quite different from the same term in New Zealand or England. In 
my experience it has no associated implications of conveying contempt, yet 
two American based posters here say it has. I believe them (they are 
honourable men) but it doesn't gel with my experience or what I intended 
when I used the term.


>>>>So long as everyone who experiences them
>>>>agrees they are, then they can be admitted to be "real", but that 
…[7 more quoted lines elided]…
>>>
There are many "commonly accepted" sources and they often disagree in 
details. The argument from Authority is refuted by a different Authority.

>>> 'I have a radical idea!'
>>>
…[21 more quoted lines elided]…
>
I wouldn't presume to make such a generalization. I can only say that when 
_I_ say: "that is" it is because I believe it to be so.

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T11:38:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqoe5$lip$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lbs0rF11m239U1@individual.net> <dcqhgt$1pp$1@panix5.panix.com> <3lc5fkF11uur6U1@individual.net>`

```
In article <3lc5fkF11uur6U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
><docdwarf@panix.com> wrote in message news:dcqhgt$1pp$1@panix5.panix.com...

[snip]

>> You seem to be saying 'that is' can be universally semantically equated to
>> 'I think that is'... am I correct in concluding this?
>>
>I wouldn't presume to make such a generalization. I can only say that when 
>_I_ say: "that is" it is because I believe it to be so.

Mr Dashwood, not everyone is aware of the particular beliefs of another; 
this might be a good reason to be explicit in applying 'restriction, 
exception and qualification'.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T15:57:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqphm$ndb$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lbs0rF11m239U1@individual.net> <dcqhgt$1pp$1@panix5.panix.com> <3lc5fkF11uur6U1@individual.net> <dcqoe5$lip$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> >I wouldn't presume to make such a generalization. I can only say that when
> >_I_ say: "that is" it is because I believe it to be so.
…[3 more quoted lines elided]…
> exception and qualification'.

Where does the confusion lie here?

If Mr. Dashwood says "That is stupid", and if my beliefs are different, how
would my understanding of what he meant be more clear if he said "I believe that
is stupid"?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T12:32:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqrii$1f0$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc5fkF11uur6U1@individual.net> <dcqoe5$lip$1@panix5.panix.com> <dcqphm$ndb$1@peabody.colorado.edu>`

```
In article <dcqphm$ndb$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
>Where does the confusion lie here?

The difference between 'is' and 'I believe it is'.

>
>If Mr. Dashwood says "That is stupid", and if my beliefs are different, how
>would my understanding of what he meant be more clear if he said "I believe that
>is stupid"?

The difference might not be one of belief but one of the definition of 
stupid used.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T16:50:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqske$p49$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lc5fkF11uur6U1@individual.net> <dcqoe5$lip$1@panix5.panix.com> <dcqphm$ndb$1@peabody.colorado.edu> <dcqrii$1f0$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> >Where does the confusion lie here?
>
> The difference between 'is' and 'I believe it is'.

Obviously we aren't arguing about how long the sentence is.   So there must be
some real difference.   Is there a possibility that someone reading Mr.
Dashwood's quote might be confused as to whether he believes a practice is
stupid, or whether there is some objectively defined definition of "is stupid"
that can be applied here where "I believe" would not work?


> >If Mr. Dashwood says "That is stupid", and if my beliefs are different, how
> >would my understanding of what he meant be more clear if he said "I believe
…[4 more quoted lines elided]…
> stupid used.

That could be.   But "I believe" does not clarify which definition is being
used.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T13:18:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqu9i$ngk$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqphm$ndb$1@peabody.colorado.edu> <dcqrii$1f0$1@panix5.panix.com> <dcqske$p49$1@peabody.colorado.edu>`

```
In article <dcqske$p49$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>that can be applied here where "I believe" would not work?

I barely know what *I* might be confused about, Mr Brazee, let alone what 
others might be confused about.

>
>
…[9 more quoted lines elided]…
>used.

One is a statement about what stupidity is, Mr Brazee, and one is a 
statement about belief; direction of further queries might be different 
depending on this.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T19:08:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcr4nd$3t$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqphm$ndb$1@peabody.colorado.edu> <dcqrii$1f0$1@panix5.panix.com> <dcqske$p49$1@peabody.colorado.edu> <dcqu9i$ngk$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> >Obviously we aren't arguing about how long the sentence is.   So there must
> >be
…[7 more quoted lines elided]…
> others might be confused about.

Still, a suggestion that adding "I believe" to a "is stupid" clause should be
accompanied by a statement of purpose - what benefit is gained.   If it happens
to be, "to reduce confusion", an example would be useful illustrating how that
extra information makes the statement more clear.


> >> The difference might not be one of belief but one of the definition of
> >> stupid used.
…[5 more quoted lines elided]…
> statement about belief;

It appears you agree with me then.

> direction of further queries might be different depending on this.

If "on this" is on the definition of "is stupid", I agree.   But that is
separate from whether he said "I believe" in front of his "is stupid".
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T20:22:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcrn3i$r6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqske$p49$1@peabody.colorado.edu> <dcqu9i$ngk$1@panix5.panix.com> <dcr4nd$3t$1@peabody.colorado.edu>`

```
In article <dcr4nd$3t$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[13 more quoted lines elided]…
>accompanied by a statement of purpose - what benefit is gained.

That depends on who is evaluating the benefit, Mr Brazee; some might say 
that more precise speech is, in and of it'sself, a benefit.

[snip]

>> >> The difference might not be one of belief but one of the definition of
>> >> stupid used.
…[7 more quoted lines elided]…
>It appears you agree with me then.

It appears that you interrupted me mid-sentence, Mr Brazee, and that doing 
so might alter the context of the statement.

>
>> direction of further queries might be different depending on this.
>
>If "on this" is on the definition of "is stupid", I agree.   But that is
>separate from whether he said "I believe" in front of his "is stupid".

If the sentence is addressed without interruption, Mr Brazee, you might be 
able to see your question answered.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T13:56:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dct6pu$5bf$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqske$p49$1@peabody.colorado.edu> <dcqu9i$ngk$1@panix5.panix.com> <dcr4nd$3t$1@peabody.colorado.edu> <dcrn3i$r6$1@panix5.panix.com>`

```

On  3-Aug-2005, docdwarf@panix.com wrote:

> >Still, a suggestion that adding "I believe" to a "is stupid" clause should be
> >accompanied by a statement of purpose - what benefit is gained.
>
> That depends on who is evaluating the benefit, Mr Brazee; some might say
> that more precise speech is, in and of it'sself, a benefit.

Precision isn't measured by the number of words being passed - it's measured by
how effectively the data gets understood.   Extra words do not make something
precise unless more information was added.   My argument is that no more
information was added.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T10:11:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dct7mu$kf9$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcr4nd$3t$1@peabody.colorado.edu> <dcrn3i$r6$1@panix5.panix.com> <dct6pu$5bf$1@peabody.colorado.edu>`

```
In article <dct6pu$5bf$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>information was added.

It appears that 'no more information was added' when one equates 'It is' 
with 'I believe it is'; I do not believe that this equating is, by any 
means, a universal phenomenon.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T15:54:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctdof$929$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcr4nd$3t$1@peabody.colorado.edu> <dcrn3i$r6$1@panix5.panix.com> <dct6pu$5bf$1@peabody.colorado.edu> <dct7mu$kf9$1@panix5.panix.com>`

```

On  4-Aug-2005, docdwarf@panix.com wrote:

> >Precision isn't measured by the number of words being passed - it's measured
> >by
…[6 more quoted lines elided]…
> means, a universal phenomenon.

I never claimed it was universal.  I claimed that in this particular case no
further information was added.

The main exception is when "I believe" doesn't really mean "I believe", but
means "I could be wrong, but".
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T13:51:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctkj6$63q$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dct6pu$5bf$1@peabody.colorado.edu> <dct7mu$kf9$1@panix5.panix.com> <dctdof$929$1@peabody.colorado.edu>`

```
In article <dctdof$929$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  4-Aug-2005, docdwarf@panix.com wrote:
…[12 more quoted lines elided]…
>further information was added.

The condition of 'no further information was added' is predicated on the 
condition of equating 'It is' with 'I believe it is'.

>
>The main exception is when "I believe" doesn't really mean "I believe", but
>means "I could be wrong, but".

Meaning is the result of interpretation, as Wittgenstein had it; a red 
banner can be interpreted as 'Long Live the Glorious Socialist 
Revolution!' or 'Happy Wedding-Day!'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T18:08:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctljq$d64$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dct6pu$5bf$1@peabody.colorado.edu> <dct7mu$kf9$1@panix5.panix.com> <dctdof$929$1@peabody.colorado.edu> <dctkj6$63q$1@panix5.panix.com>`

```

On  4-Aug-2005, docdwarf@panix.com wrote:

> >> It appears that 'no more information was added' when one equates 'It is'
> >> with 'I believe it is'; I do not believe that this equating is, by any
…[6 more quoted lines elided]…
> condition of equating 'It is' with 'I believe it is'.

In this case, yes.


> >The main exception is when "I believe" doesn't really mean "I believe", but
> >means "I could be wrong, but".
…[3 more quoted lines elided]…
> Revolution!' or 'Happy Wedding-Day!'

OK.   Let's look at the possibilities we have discussed:

It is stupid.
I believe it is stupid.

If they are synonyms, then "I believe" doesn't add anything.   Why should I tell
him to add that to what he said?

or
It is stupid.
I believe it is stupid.

If "I believe it is stupid" means "I'm not really sure", then they are not
synonyms.   If so, why should I be presumptuous enough to tell him that he
didn't mean what he said?

Do you have any alternative scenarios for this particular instance?
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 28)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T14:20:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctmab$kd1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctdof$929$1@peabody.colorado.edu> <dctkj6$63q$1@panix5.panix.com> <dctljq$d64$1@peabody.colorado.edu>`

```
In article <dctljq$d64$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  4-Aug-2005, docdwarf@panix.com wrote:
…[11 more quoted lines elided]…
>In this case, yes.

And what criteria are being used to differentiate this case from other 
cases?

>
>
…[13 more quoted lines elided]…
>him to add that to what he said?

Predicated on 'It is' being equal to 'I believe it is', as you agreed to 
above.

>
>or
…[5 more quoted lines elided]…
>didn't mean what he said?

Meaning is the result of interpretation, Mr Brazee... or so Wittgenstein 
tells us.

>
>Do you have any alternative scenarios for this particular instance?

I have several... but all of them end with the Sweepstakes Notification 
Team showing up at my house and presenting me with a check.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 29)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-04T18:44:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctnlm$eae$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctdof$929$1@peabody.colorado.edu> <dctkj6$63q$1@panix5.panix.com> <dctljq$d64$1@peabody.colorado.edu> <dctmab$kd1$1@panix5.panix.com>`

```

On  4-Aug-2005, docdwarf@panix.com wrote:

> >> >I never claimed it was universal.  I claimed that in this particular case
> >> >no
…[8 more quoted lines elided]…
> cases?

There are times when I can tell by tone of voice that the person who says "I
believe..." isn't sure.

In this case, I cannot judge that way and wouldn't want to presume he means
anything except what he said.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 30)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-04T14:54:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcto8u$eq4$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctljq$d64$1@peabody.colorado.edu> <dctmab$kd1$1@panix5.panix.com> <dctnlm$eae$1@peabody.colorado.edu>`

```
In article <dctnlm$eae$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  4-Aug-2005, docdwarf@panix.com wrote:
…[17 more quoted lines elided]…
>anything except what he said.

In this case, Mr Brazee, Mr Dashwood seems to have made a statement which 
had 'no restriction, exception or qualification' about 'a thing done'; by 
these definitions he made a statement of absolute fact.  To conclude that 
he made a statement of belief appears to require an addition on the part 
of the reader; that would be other than 'what he said'.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-05T14:07:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lfvvnF12eps7U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctljq$d64$1@peabody.colorado.edu> <dctmab$kd1$1@panix5.panix.com> <dctnlm$eae$1@peabody.colorado.edu> <dcto8u$eq4$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcto8u$eq4$1@panix5.panix.com...
>
> In article <dctnlm$eae$1@peabody.colorado.edu>,
…[3 more quoted lines elided]…
>>
<snip>
> In this case, Mr Brazee, Mr Dashwood seems to have made a statement which
> had 'no restriction, exception or qualification' about 'a thing done'; by
> these definitions he made a statement of absolute fact.

No I didn't. Even 'by these definitions' which are NOT a definition of 
"absolute fact". (There is nothing in either of your authorities that claims 
them to be definitions of "absolute fact"). You are making it up, presumably 
because you enjoy the argument.

Howard has presented a series of statements that totally accurately reflect 
what my intentions were at the time I wrote the statements I did. (So much 
so, that I feel no compulsion to modify or extend anything he has said.)

He has covered exactly how my statement would have been weakened and open to 
an interpretation I did not intend, by adding the words '"I believe" to it. 
Neither he, nor myself, nor anyone else has disputed that there may be cases 
where adding "I believe" may not be exactly equivalent to not adding it, but 
that is not THIS case. You have consistently ignored the case in point, and 
tried to push the argument to the general, for purposes which I cannot begin 
to imagine. What exactly are you trying to achieve here?

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 32)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T08:04:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcvkl2$g7o$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctnlm$eae$1@peabody.colorado.edu> <dcto8u$eq4$1@panix5.panix.com> <3lfvvnF12eps7U1@individual.net>`

```
In article <3lfvvnF12eps7U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[12 more quoted lines elided]…
>No I didn't.

Yes, you did... see how easy?

>Even 'by these definitions' which are NOT a definition of 
>"absolute fact". (There is nothing in either of your authorities that claims 
>them to be definitions of "absolute fact"). You are making it up, presumably 
>because you enjoy the argument.

Mr Dashwood, I have attempted to show the sources of my definitions, the 
processes by which I relate these definitions and the conclusions which 
arise out of my relatings.  If you see an error I have made then please, 
by all means, point out where the error lies.  Once again:

Mr Dashwood stated, of something that was done, 'It is stupid'.

According to 
http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=fact&x=0&y=0 a 
definition of fact is 'a thing done'.

'It is stupid' is a statement of equality, containing no restrictions, 
exceptions or qualifications.

According to 
http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=absolute+&x=0&y=0 
a definition of absolute is 'having no restriction, exception, or 
qualification'.

In that Mr Dashwood made a statement (having no restriction, exception or 
qualification) of (a thing done) Mr Dashwood, by definition, made a 
statement (absolute) of (fact).

>
>Howard has presented a series of statements that totally accurately reflect 
…[4 more quoted lines elided]…
>an interpretation I did not intend, by adding the words '"I believe" to it. 

Mr Brazee stated that he supplied the conditionals which your statement 
did not contain; I responded that when the author is present I try to rely 
more on the word of the author than on my own interpretations.

>Neither he, nor myself, nor anyone else has disputed that there may be cases 
>where adding "I believe" may not be exactly equivalent to not adding it, but 
>that is not THIS case. You have consistently ignored the case in point, and 
>tried to push the argument to the general, for purposes which I cannot begin 
>to imagine. What exactly are you trying to achieve here?

A bit of clarity, if only for myself... how is it that someone can make a 
statement of absolute fact and then demand the reader supply the 
qualification?

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 33)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-05T13:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_WJIe.51709$t43.44783@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctnlm$eae$1@peabody.colorado.edu> <dcto8u$eq4$1@panix5.panix.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dcvkl2$g7o$1@panix5.panix.com...

<snip>

>>Neither he, nor myself, nor anyone else has disputed that there may be 
>>cases
…[12 more quoted lines elided]…
> DD

Answering a question with a question......oh never mind.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T12:47:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd057g$95f$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <_WJIe.51709$t43.44783@tornado.tampabay.rr.com>`

```
In article <_WJIe.51709$t43.44783@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:dcvkl2$g7o$1@panix5.panix.com...
>
…[17 more quoted lines elided]…
>Answering a question with a question......oh never mind.

My error and my apologies for my sloppy punctuation to all... now it might 
be clearer why I try to avoid the formulation of 'I do not do it' and 
admit my limitations by saying 'I do my best to avoid doing it'.  

The sentence(s) should have been written 'A bit of clarity, if only for 
myself.  How is it that someone can make a statement of absolute fact and 
then demand the reader supply the qualification?'

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 35)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-05T17:12:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd06lt$tj$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <_WJIe.51709$t43.44783@tornado.tampabay.rr.com> <dd057g$95f$1@panix5.panix.com>`

```

On  5-Aug-2005, docdwarf@panix.com wrote:

> My error and my apologies for my sloppy punctuation to all... now it might
> be clearer why I try to avoid the formulation of 'I do not do it' and
…[4 more quoted lines elided]…
> then demand the reader supply the qualification?'

It doesn't matter how you formulate it.   Sometimes it is appropriate to ask a
question before or while answering a question.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T13:35:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd0804$9v0$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <_WJIe.51709$t43.44783@tornado.tampabay.rr.com> <dd057g$95f$1@panix5.panix.com> <dd06lt$tj$1@peabody.colorado.edu>`

```
In article <dd06lt$tj$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  5-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>It doesn't matter how you formulate it.

What 'matters', Mr Brazee, is often dependent on who is considering the 
situation; in this case it mattered enough to me for me to admit my error 
and correct it.

>Sometimes it is appropriate to ask a
>question before or while answering a question.

The propriety of not answering a question was not addressed, Mr Brazee; 
what is pointed out is that answering a question with a question is no 
answer at all.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 37)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-05T17:50:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd08u2$24q$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <_WJIe.51709$t43.44783@tornado.tampabay.rr.com> <dd057g$95f$1@panix5.panix.com> <dd06lt$tj$1@peabody.colorado.edu> <dd0804$9v0$1@panix5.panix.com>`

```

On  5-Aug-2005, docdwarf@panix.com wrote:

> >Sometimes it is appropriate to ask a
> >question before or while answering a question.
…[3 more quoted lines elided]…
> answer at all.

I guess this is a running gag that you interject for humor in the middle of
discussions.   Sometimes I take what you say seriously, such as with the
discussion about requiring "I believe" in front of "is stupid".    This might be
a failing on my side, but I cannot get your tone of voice in this medium.

You have given us plenty of opportunity to know that you are, in fact,
intelligent, so I shouldn't expect that when you continue with these arguments
that you are serious.

Now that I have belatedly "got it", I have to decide whether to smile, continue
to get frustrated at the non-sequitur nature of your humor, or continue posting
for the sake of people who are new to the forum and don't recognize that you are
joking.

I wish that after you add your gag - you would take our questions seriously and
add to the discussion at hand though.    You have good stuff to contribute that
isn't as much fun (for you) than changing the topic with a joke.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 38)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-05T14:45:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd0c4j$gl1$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dd06lt$tj$1@peabody.colorado.edu> <dd0804$9v0$1@panix5.panix.com> <dd08u2$24q$1@peabody.colorado.edu>`

```
In article <dd08u2$24q$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  5-Aug-2005, docdwarf@panix.com wrote:
…[9 more quoted lines elided]…
>discussions.

I believe it was Cicero who said something along the lines of 'Who is it 
who says we must speak of truth and not smile?'

[snip]

>I wish that after you add your gag - you would take our questions seriously and
>add to the discussion at hand though.    You have good stuff to contribute that
>isn't as much fun (for you) than changing the topic with a joke.

Mr Brazee, I have posted and re-posted my views on this, in a variety of 
threads... views which were originally posted in response to you, among 
others:

<http://groups-beta.google.com/group/comp.lang.cobol/msg/967c9d77a4959544?dmode=source&hl=en?

<http://groups-beta.google.com/group/comp.lang.cobol/msg/c5ffed30915f7f6b?dmode=source&hl=en>

<http://groups-beta.google.com/group/comp.lang.cobol/msg/8842d15897621daf?dmode=source&hl=en>

... so it might be readily apparent that when a question is asked and not 
answered I have difficulties which I am not loth to express.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-06T14:35:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lilvhF131g2nU1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dctnlm$eae$1@peabody.colorado.edu> <dcto8u$eq4$1@panix5.panix.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dcvkl2$g7o$1@panix5.panix.com...
>
> In article <3lfvvnF12eps7U1@individual.net>,
…[38 more quoted lines elided]…
> definition of fact is 'a thing done'.

I dispute that definition so what is the point of discussing it?

>
> 'It is stupid' is a statement of equality, containing no restrictions,
> exceptions or qualifications.

Apart from the context in which it was made.

>
> According to
…[7 more quoted lines elided]…
>

You can obviously believe whatever you want to.

>>
>>Howard has presented a series of statements that totally accurately 
…[26 more quoted lines elided]…
>
I really have no idea. It is not my nature to demand anything of anybody, 
and, as, discussed here to the point of tedium, I don't believe in "absolute 
facts". I expressed an opinon. I stand by it.

Pete.



Pete.

>
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 34)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-06T10:36:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd2hsn$3q6$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net>`

```
In article <3lilvhF131g2nU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[43 more quoted lines elided]…
>I dispute that definition so what is the point of discussing it?

Mr Dashwood, as noted in an earlier post working from different 
definitions for a given word - English being a language where words are 
admitted to having more than one definition - can generate difficulties 
based solely on definition.

I have supplied the definition upon which I based my conclusions, well and 
good... would you be so kind as to supply the one you are using, so that 
it might be seen whence arise these differences?

>
>>
…[3 more quoted lines elided]…
>Apart from the context in which it was made.

It was made in the context of the English language, Mr Dashwood, for which 
there are commonly-accepted sources of definition.
>
>>
…[10 more quoted lines elided]…
>You can obviously believe whatever you want to.

Mr Dashwood, I have attempted to show the definitions from which I began, 
the way in which I related them and the conclusions to which I came... a 
form of demonstration which seems to work fairly well in resolving matters 
of disagreement.

Your responses, in this case, are along the lines of 'I dispute that' and 
'you can believe what you want to'... how is anyone to see or learn 
anything beyond the statements of your disagreement?

A: 'Given (x) under condition (y) result (z) appears to be reasonable.'
B: 'You can obviously believe whatever you want to.'

If that is all you wish to supply, Mr Dashwood, it would seem that your 
desire is something I suggested as a possibility in an earlier posting:

A: (g)

B: Ahhhhh, it is so.  (r)

A: Ahhhhh, it is so.  (3)

B: Ahhhhh, it is so.  (XIV) 

... and it just might be that I am not sufficiently... 'enlightened' to 
appreciate such a thing.

(Oblique reference to a joke about Buddhists: There are two Perfect 
Masters, each sitting on his own mountaintop.  One calls over to the other 
'How is the weather over there?'

A hundred years pass.

The second calls back to the first 'Do you want to fight about it?')

(Now, all together: 'Ahhhhh, it is so.')

[snip]

>>>What exactly are you trying to achieve here?
>>
…[6 more quoted lines elided]…
>facts". I expressed an opinon. I stand by it.

As shown by the definitions above, Mr Dashwood, you may have intended to 
express an opinion... but it seems to have appeared in the form of a 
statement of absolute fact.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-07T14:53:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3llbdcF134ai5U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com>`

```

> [snip]
>
…[15 more quoted lines elided]…
>
Only to you, Doc.

Hence my statement: "You can believe whatever you want to".

And you can provide all the definitions and logic you like; it doesn't 
change what I was doing. It only explains why YOU view what I was doing the 
way you do.

You can accept a dictionary definition that tells you what a fact is; I 
can't.

You have deliberately excluded contexts that were very important to this 
argument, and you refuse to accept that they were.

Even above (in the area I snipped) you see the only context as being "the 
English Language".  Check your dictionary for the meaning of 'context', and 
consider how it affects meaning.  You might consider also that Wittgenstein 
may not have had the whole story and it could be risky to build your 
understanding of 'meaning' on the writings of  someone who did not live in 
today's world, and was not privy to the understandings acquired in the last 
twenty years. (Or not... it really doesn't matter. My point is that rather 
that trot out the same old cliches, why not consider if they are still 
applicable? Some re-evaluation is often good, even if you come to the same 
conclusion...)  He died in 1951; the world has changed considerably since 
then and the understanding we have now about the nature of things is far 
different from that which we had then.

You have played your broken record of "Is that absolute?" even after I have 
genuinely explained why I do not believe in "absolute fact". You just keep 
re-iterating your dictionary definitions to support your argument that my 
expression of opinion was one of absolute fact. It wasn't. As the originator 
of it, I believe I am better placed to know what was intended than you are. 
It is just tiresome and silly. No progress is possible because you are not 
listening to what I'm saying, and I won't accept your argument from 
Authoriity. We have fundamental differences of opinion about this that will 
not be resolved by debate. So I say, with all goodwill and absence of 
petulance: "Believe whatever you want to."

As I am not accountable to you, am fine for you to have whatever opinion you 
like about it, do not need your approval before posting here, and am certain 
nothing I can say or do will change your mind on this anyway, it is 
pointless (for me) to continue this dialogue.

I am satisfied I have explained my position to the point where any 
reasonable person would understand it. Although I enjoy informed debate and 
don't even mind losing such debates occasionally, this one is going nowhere 
so it has to be terminated.

I expressed an opinion. That's what I always do when I post here. That's 
what I'm doing right now.

Believe whatever you want to about it.

Sorry, it's tea-time...game's over :-)

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 36)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-07T06:02:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd4m8j$daj$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net>`

```
In article <3llbdcF134ai5U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>> As shown by the definitions above, Mr Dashwood, you may have intended to
>> express an opinion... but it seems to have appeared in the form of a
…[7 more quoted lines elided]…
>change what I was doing.

Mr Dashwood, you appear to fall prey to your own logic.  According to you 
there is no 'what you were doing', or 'absolute fact of action'; there is 
only what people agree what you were doing.

You and I disagreed about this.  I offered definitions, logic and 
conclusions; despite repeated and polite requests you were unwilling or 
unable to do likewise.

Since there's disagreement and you do not believe there's 'absolute fact' 
to rely on... it seems that all there is left is definition, logic, 
conclusion and discussion.  For some reason you appear to think that 'I 
did not!' is a substitute for these.

>
>You can accept a dictionary definition that tells you what a fact is; I 
>can't.

The what is someone else to make of your use of the word, Mr Dashwood?  
How is anyone to do what is called 'communicating' without a common basis?

>
>You have deliberately excluded contexts that were very important to this 
>argument, and you refuse to accept that they were.

Mr Dashwood, if different use of definition are carried into the same 
context the result might be different; that is why I have tried so hard to 
clarify definitions first.  This seems to be anathema to you, for reasons 
I do not know... but I have found that careful attention to definition can 
remove many apparent disagreements.  Perhaps you enjoy the disagreements 
in some manner and wish to preserve them; I do not find disagreement based 
on definition to be anything of pleasure.

>
>Even above (in the area I snipped) you see the only context as being "the 
>English Language".  Check your dictionary for the meaning of 'context', and 
>consider how it affects meaning.

I should check my dictionary for a definition you suggest whilst you 
refuse repeated requests to do the same?  Mr Dashwood, that would appear 
to be expecting a behavior from another which one refuses, one'sself, to 
do.

[snip]

>You have played your broken record of "Is that absolute?" even after I have 
>genuinely explained why I do not believe in "absolute fact".

I have attempted to demonstrate, Mr Dashwood, that your beliefs lead to a 
contradiction; my apologies if I was unclear.

>You just keep 
>re-iterating your dictionary definitions to support your argument that my 
>expression of opinion was one of absolute fact. It wasn't.

You keep repeating this, Mr Dashwood, and I point out that you are asking 
me to accept this 'it was'nt'.  Consider:

A: (x)
B: According to definition that is (y).
A: No, it isn't.
B: Says who?
A: Says me.
B: Your word trumps that of a commonly-accepted source?
A: That's right.  I say so, there it is.

>As the originator 
>of it, I believe I am better placed to know what was intended than you are. 

That may well be, Mr Dashwood; Author's Intent is very important.  In this 
case Author's Intent appears to contradict definition; if that is the case 
an Author might wish to reconsider the words used or the method in which 
they were used since commonly-accepted definitions appear to show that an 
opposite interpretation is possible.

>It is just tiresome and silly. No progress is possible because you are not 
>listening to what I'm saying, and I won't accept your argument from 
>Authoriity.

I do not make an Argument from Authority, Mr Dashwood; I take definitions 
from there and I qualify following statements with 'in that'.  I am more 
than willing to countenance a counter but all you seem to have is 'As 
Author I intended...'

It is fine that you intend such, Mr Dashwood... but how is that made 
manifest in your statements?  Do you expect all readers to approach your 
works and universally substitute 'It is my opinion' or 'I believe' for 
your uses of 'It is'?

>We have fundamental differences of opinion about this that will 
>not be resolved by debate. So I say, with all goodwill and absence of 
…[5 more quoted lines elided]…
>pointless (for me) to continue this dialogue.

In the fashion you present it, Mr Dashwood, this may be the case.  I try 
to supply definitions, logic and conclusions... you counter with what 
appears to be Humpty-Dumptyistic 'it means what I want it to'.

>
>I am satisfied I have explained my position to the point where any 
>reasonable person would understand it. Although I enjoy informed debate and 
>don't even mind losing such debates occasionally, this one is going nowhere 
>so it has to be terminated.

I tried to direct it otherwise, Mr Dashwood... but my solo efforts can go 
only so far.

>
>I expressed an opinion. That's what I always do when I post here. That's 
>what I'm doing right now.

Is that a fact, now?

>
>Believe whatever you want to about it.
>
>Sorry, it's tea-time...game's over :-)

When you feel up to trying again, Mr Dashwood, perhaps your efforts may 
have a different outcome... but feel free to try again, by all means.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 36)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T08:11:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7snm$1dtg$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3llbdcF134ai5U1@individual.net...

> > As shown by the definitions above, Mr Dashwood, you may have intended to
> > express an opinion... but it seems to have appeared in the form of a
> > statement of absolute fact.
> >
> Only to you, Doc.

Absolutely, and incontrovertibly, wrong.

 > You can accept a dictionary definition that tells you what a fact is; I
> can't.

At least in the case of the Merriam-Webster offerings and the Oxford
University Press offerings (and specifically in contrast to the publications
and the activities of such organizations as, say, the Acad�mie Fran�aise),
English dictionaries tend to evolve as *reflections* of common usage, not as
a list of academic pronouncements as to how people ought to be referring to
things.   I have found that the Merriam-Webster offerings best reflect
common current American English; etymological matters are better covered by
the Oxford (greater or lesser) in my opinion.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 37)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T15:47:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F8LJe.39377$iG6.6353@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dd7snm$1dtg$1@si05.rsvl.unisys.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
…[26 more quoted lines elided]…
>    -Chuck Stevens
You have found that M-W best reflects common current American English...and 
by what means did you determine this?
By use of language with the people that you know (who I assume are educated 
middle america, and not for example, inner cities or the bowels of 
Mississippi).  It took me years to convince my wife that "chuddy" was 
chewing gum (she didn't believe me until she made a friend who lived less 
than 30 miles from where I grew up)....I never checked that was in the 
dictionary...I know people that I grew up with would know what "itchy chin" 
means...but I doubt anyone outside of that group would know...

We've also had a discussion with the use of "dialogue" as a verb.  I don't 
believe mw was the source, but rather the american heritage, but 
nonetheless, the argument there went that Coleridge and Shakespeare used the 
word as a verb and it's in the dictionary therefore it stands as acceptable 
and perfectly reasonable usage.  This despite the fact that it was majority 
considered "archaic".

I agree whole heartedly with your assertion that a dictionaries exist as a 
reflection of common usage..to assist with communication..if only people 
would use them as such.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 38)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T12:21:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8bd0$1mpp$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:F8LJe.39377$iG6.6353@tornado.tampabay.rr.com...

> You have found that M-W best reflects common current American
English...and
> by what means did you determine this?

I have compared various English dictionaries and have also done some
rudimentary research into the scholarship and research methodology that has
gone into those dictionaries (and families of dictionaries).   I believe
M-W's research is both more extensive and more careful than its competition
among those dictionaries that are specifically targeted to that purport to
reflect American English.  That has been confirmed by comparison of a number
of definitions, in particular between the M-W Third Unabridged and the
American Heritage and Random House erstwhile competitors.

A four-year degree in Linguistics, with several courses on the history of
English as well as on American Dialectology, also gave me some tools to form
such opinions.

> By use of language with the people that you know (who I assume are
educated
> middle america, and not for example, inner cities or the bowels of
> Mississippi).  It took me years to convince my wife that "chuddy" was
> chewing gum (she didn't believe me until she made a friend who lived less
> than 30 miles from where I grew up)....I never checked that was in the
> dictionary...I know people that I grew up with would know what "itchy
chin"
> means...but I doubt anyone outside of that group would know...

There are lots of dialect variations across the country, and there are lots
of dictionaries that reflect them.  Some regional dialect items do end up in
the "mainstream" dictionaries, but typically only when they are both used
and understood by a large and diverse subset of the population.    "Tonic"
as a noun, denoting a carbonated flavored beverage,  is in the Ninth
Collegiate -- because it's a well-known dialect feature -- but is also
described as "chiefly New England".

> We've also had a discussion with the use of "dialogue" as a verb.  I don't
> believe mw was the source, but rather the american heritage, but
> nonetheless, the argument there went that Coleridge and Shakespeare used
the
> word as a verb and it's in the dictionary therefore it stands as
acceptable
> and perfectly reasonable usage.  This despite the fact that it was
majority
> considered "archaic".

The M-W's I have handy at work don't mark the verb "dialogue" archaic.  What
"majority" considers it archaic?

And if it's the fact that it's fundamentally a "verbed noun", the practice
of verbing a noun has been a structural feature of English for a very long
time.   Some authorities on Proper English deem it anathema; others, who
seek to *describe* the language, recognize that it's part of the way the
language works -- just as "I ain't got no ..." is understandable in casual
speech as a *single* negative, and just as everybody understands that a
preposition is not an incomprehensible thing to end a sentence with.  Both
proscriptions have their origins at medieval English universities, where the
rules of *valid Latin* were presumed to apply to *proper English*.  My
recollection of high school Latin is that it's not quite so fluid in terms
of restructuring words in such ways as the hypothetical verbum => verbare
(or verbere, or verbire!).  I do recall that multiple negatives in Germanic
languages typicall serve to emphasize the negative sense of the utterance,
unlike Latin where, if they are allowed at all, logically reverse the sense.
Terminating propositions are structurally impossible in Latin but I'm
certain they represent an echo of the Germanic "separable-prefix"
compounding of verbs, which practice survives much more obviously in modern
German (as in a few more obvious in modern English -- "take the trash out"
vs. "take out the trash" vs. "out-take" vs. (courtesy of Babelfish -- 
idiomatic they may not be, but they illustrate the structure) "Nehmen Sie
den Abfall heraus" vs. "Ich erklaerte Ihnen, den Abfall herauszunehmen."

> I agree whole heartedly with your assertion that a dictionaries exist as a
> reflection of common usage..to assist with communication..if only people
> would use them as such.

Well, hmm.  My assertion is *not* a blanket assertion.  Some American
English dictionaries don't do as good a job of it, in my observation, as
others, and it is common in *some* languages (e.g. French) for dictionaries
to be *prescriptive* rather than *descriptive*.   My observations while
comparing the styles and approaches used in the development of dictionaries
in various language lead me to treat current Merriam-Webster's offerings,
starting with their Third Unabridged as a base, with more respect than those
from other publishers, from the standpoint that it was a better *reflection*
of common usage than most.  Such was also the opinion of my various English
Linguistics professors.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 39)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T19:52:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8d56$1u7$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com>`

```

On  8-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> And if it's the fact that it's fundamentally a "verbed noun", the practice
> of verbing a noun has been a structural feature of English for a very long
…[6 more quoted lines elided]…
> rules of *valid Latin* were presumed to apply to *proper English*.

I was aware of the Latin basis for the silly prohibition of ending sentences
with preposition.   You mentioned "both proscriptions" with "verbing a noun" and
with "double negatives".    I know some romance languages use double negatives.
 For my information, which of these are Latin impossibilities?


(As a programmer, I dislike double negatives as negative - but that doesn't mean
I have an objection to using them in Spanish).
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 40)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T13:10:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8e9c$1oho$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com> <dd8d56$1u7$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:dd8d56$1u7$1@peabody.colorado.edu...
>
> On  8-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> > And if it's the fact that it's fundamentally a "verbed noun", the
practice
> > of verbing a noun has been a structural feature of English for a very
long
> > time.   Some authorities on Proper English deem it anathema; others, who
> > seek to *describe* the language, recognize that it's part of the way the
> > language works -- just as "I ain't got no ..." is understandable in
casual
> > speech as a *single* negative, and just as everybody understands that a
> > preposition is not an incomprehensible thing to end a sentence with.
Both
> > proscriptions have their origins at medieval English universities, where
the
> > rules of *valid Latin* were presumed to apply to *proper English*.
>
> I was aware of the Latin basis for the silly prohibition of ending
sentences
> with preposition.   You mentioned "both proscriptions" with "verbing a
noun" and
> with "double negatives".    I know some romance languages use double
negatives.
>  For my information, which of these are Latin impossibilities?

Nouns follow prepositions in Latin, and Latin doesn't have separable
prefixes.  So far as I know, ending a sentence with a preposition is a
structural impossibility in Latin.

> (As a programmer, I dislike double negatives as negative - but that
doesn't mean
> I have an objection to using them in Spanish).

I'm not sure a native or near-native reader or speaker of Latin would
recognize a machine translation of something like "he ain't got no sense,
nohow" into that language (or for that matter, a number of other languages)
as having a *single* negative sense rather than *three* negative expressions
that have the cumulative result of negativity.   Dropping the "nohow" at the
end has no effect on the overall negativity of the utterance to the average
native-English hearer; the argument about such multiple negatives in "proper
English" is that it *does* affect the sense, and "propriety" would demand
the use of one, and only one, negative indicator in the utterance.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 39)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T19:59:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ROJe.85909$mC.10067@tornado.tampabay.rr.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dd8bd0$1mpp$1@si05.rsvl.unisys.com...
>
> "jce" <defaultuser@hotmail.com> wrote in message
…[21 more quoted lines elided]…
> such opinions.

You are indeed more qualified than I.

<snip good stuff>

The M-W's I have handy at work don't mark the verb "dialogue" archaic.  What
> "majority" considers it archaic?

I was referring to the American Heritage Usage Panel from which the original 
argument was drawn.
98% of the following http://www.bartleby.com/64/12.html
I assume it's the ones without the "*".

It's not relevant particularly, but as you asked the least I could do was 
show that I didn't just make it up.

<snip more good stuff>

>> I agree whole heartedly with your assertion that a dictionaries exist as 
>> a
…[17 more quoted lines elided]…
> Linguistics professors.

Correction understood and taken on board.

Interesting response - I've often wondered how and why someonen would choose 
dictionary (a) over dictionary (b).
I assumed (rather incorrectly for the more scholarly and literary amongst 
us) that the main reason would have been primarily size and then price.

Thanks.

JCE
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 40)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T13:28:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8faa$1p5l$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com> <1ROJe.85909$mC.10067@tornado.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:1ROJe.85909$mC.10067@tornado.tampabay.rr.com...

> Interesting response - I've often wondered how and why someonen would
choose
> dictionary (a) over dictionary (b).
> I assumed (rather incorrectly for the more scholarly and literary amongst
> us) that the main reason would have been primarily size and then price.

I have two book-form English dictionaries at home:  the M-W Third Unabridged
and the old two-volume Compact Oxford (the one that came with a magnifying
glass).   While I would have liked the twenty-volume version of the latter,
the price and the bookshelf space required for it were both beyond my
resources at the time.  I think the Compact Edition of that era actually
contained all the information in the "regular" first edition OED, with its
supplement, reproducing four of its pages on each page of onionskin paper.
I believe the *current* Compact Oxford is actually more competitive with a
M-W Collegiate.  In any case, I primarily use the (C)OED for etymological
questions, the answers to which don't go out of date.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 41)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T20:40:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8fvf$39s$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3lfvvnF12eps7U1@individual.net> <dcvkl2$g7o$1@panix5.panix.com> <3lilvhF131g2nU1@individual.net> <dd2hsn$3q6$1@panix5.panix.com> <3llbdcF134ai5U1@individual.net> <dd7snm$1dtg$1@si05.rsvl.unisys.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com> <1ROJe.85909$mC.10067@tornado.tampabay.rr.com> <dd8faa$1p5l$1@si05.rsvl.unisys.com>`

```

On  8-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> I have two book-form English dictionaries at home:  the M-W Third Unabridged
> and the old two-volume Compact Oxford (the one that came with a magnifying
> glass).   While I would have liked the twenty-volume version of the latter,
> the price and the bookshelf space required for it were both beyond my
> resources at the time.

I rarely use mine.   But I have other unabridged dictionaries that I can
actually read.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 42)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T18:28:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8mb4$ibo$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <1ROJe.85909$mC.10067@tornado.tampabay.rr.com> <dd8faa$1p5l$1@si05.rsvl.unisys.com> <dd8fvf$39s$1@peabody.colorado.edu>`

```
In article <dd8fvf$39s$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  8-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
…[8 more quoted lines elided]…
>actually read.

I keep my OED on a shelf near my computer at home... alone with Marshall's 
Interlinear Greek-English New Testament, the Soncino Press Pentateuch, the 
Novum Testamentum Graece (Oxford 1910, 1953 reprint), a Greek-English 
Lexicon (the little Liddle, not the Great Scott) and a copy of The Holy 
Scriptures According To The Masoretic Text... which shows more dust than 
the rest of them put together.  The web allows me ready access to m-w.com, 
the KJV (http://www.hti.umich.edu/k/kjv/), the Constitution of the United 
States of America and other texts, which, along with these, the differing 
interpretations of which make for so much discussion.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 40)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-08T18:16:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8lkd$b7r$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <F8LJe.39377$iG6.6353@tornado.tampabay.rr.com> <dd8bd0$1mpp$1@si05.rsvl.unisys.com> <1ROJe.85909$mC.10067@tornado.tampabay.rr.com>`

```
In article <1ROJe.85909$mC.10067@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:

[snip]

>Interesting response - I've often wondered how and why someonen would choose 
>dictionary (a) over dictionary (b).
>I assumed (rather incorrectly for the more scholarly and literary amongst 
>us) that the main reason would have been primarily size and then price.

I'm not sure about size... I believe Callimachus is often attributed as 
the source of 'mega biblion, mega kakon' (lit. 'big/great/large book, 
big/great/large bad/evil', sometimes rendered as 'A great book is a great 
evil').  I've found that the Oxford English Dictionary (OED) is the way to 
go for derivations and useage-cites (the American Heritage Dictionary 
(AHD) seems to crib etymologies from the OED) while http://www.m-w.com is 
readily available online... and www.dictionary.com uses a few sources that 
can provide cites of interest.

As for the proscriptive/descriptive debate... I try to avoid that.  That a 
conclusion is reached based on a definition found in a commonly-accepted 
source is, to me, a good foundation for definition... anyond can 'look it 
up in their Funk 'n Wagnalls'.  That words can be defined for particular 
discussions - 'in this case I am using 'history' not in the sense of 'a 
chronological record of significant events' but in the more radical sense 
of 'an inquiry' - is also, to me, a good foundation.

That a word is idiosyncratically defined - I recall a UseNet discussion I 
had, years ago, with a fellow who equated socialism with communism with 
altruism; I pointed out a few definitions and asked how he generated this 
equation... and his response was along the lines of 'it doesn't matter how 
they are defined, I know they're the same! - can make for some *very* 
weary interchanges.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T15:54:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqpca$nd1$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3laf38F11smc5U1@individual.net> <dcp7qp$sd2$1@panix5.panix.com> <3lbs0rF11m239U1@individual.net> <dcqhgt$1pp$1@panix5.panix.com> <3lc5fkF11uur6U1@individual.net>`

```

On  3-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

>  In
> my experience it has no associated implications of conveying contempt, yet
> two American based posters here say it has. I believe them (they are
> honourable men) but it doesn't gel with my experience or what I intended
> when I used the term.

This USAmerican has a similar experience as you have.   It may be that the
difference isn't geographical.   I also use "wrong" as a synonym for "mistaken"
most of the time.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2005-08-03T12:34:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqrnb$otj$1@panix5.panix.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <dcqhgt$1pp$1@panix5.panix.com> <3lc5fkF11uur6U1@individual.net> <dcqpca$nd1$1@peabody.colorado.edu>`

```
In article <dcqpca$nd1$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  3-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>most of the time.

You are using it, Mr Brazee, in a fashion which is defined in a 
commonly-accepted source:

http://m-w.com/cgi-bin/dictionary?book=Dictionary&va=wrong

3a: the state of being mistaken or incorrect

... so it appears there's nothing wrong there.

DD
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-03T14:22:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqk0a$kj1$1@peabody.colorado.edu>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <3laf38F11smc5U1@individual.net>`

```

On  2-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> While there is no denying that in base ten we
> all agree "five times five is twenty-five", this is simply an idea.

Speaking of number bases, I like "Christmas is Halloween"     Dec 25 = Oct 31
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-04T03:21:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lc5olF124h32U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <3laf38F11smc5U1@individual.net> <dcqk0a$kj1$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dcqk0a$kj1$1@peabody.colorado.edu...
>
>
…[7 more quoted lines elided]…
>
Man! That is SOOO cool! I have worked in octal on 6 bit  character machines 
and never come across that one before...
It's a shame we don't have a month "Hextember"...:-)

Pete.
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 13)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-03T09:26:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcqr82$2lqs$1@si05.rsvl.unisys.com>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu> <dco2qp$dgq$1@panix5.panix.com> <3laf38F11smc5U1@individual.net> <dcqk0a$kj1$1@peabody.colorado.edu>`

```
My favorite remains the answer "forty-two" to the question "what do you get
when you multiply six by nine?".   Forty-two is, of course, the correct
answer in an environment in which the presumed number base is thirteen.

    -Chuck Stevens


"Howard Brazee" <howard@brazee.net> wrote in message
news:dcqk0a$kj1$1@peabody.colorado.edu...
>
> On  2-Aug-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[4 more quoted lines elided]…
> Speaking of number bases, I like "Christmas is Halloween"     Dec 25 = Oct
31
```

###### ↳ ↳ ↳ Re: "Shared" procedure division code

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-08-03T11:39:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3laehbF11uts0U1@individual.net>`
- **References:** `<T9ADe.499087$3V6.422305@fe04.news.easynews.com> <3kp9r4Fvcc0pU2@individual.net> <dc8854$4gp$1@si05.rsvl.unisys.com> <3ks2bvF100lu4U1@individual.net> <dcbfk4$2gbb$1@si05.rsvl.unisys.com> <3kt6vbFvvrqoU1@individual.net> <dcdsbv$stj$1@si05.rsvl.unisys.com> <3l1g7qFvs80mU1@individual.net> <dcm6sh$2smh$1@si05.rsvl.unisys.com> <dco0l7$60r$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dco0l7$60r$1@peabody.colorado.edu...
>
>
…[18 more quoted lines elided]…
>
Thank you Howard. You expressed my thought better than I did.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
