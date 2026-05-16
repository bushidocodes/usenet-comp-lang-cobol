[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Modernization of COBOL Applications

_42 messages · 16 participants · 2005-09_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Modernization of COBOL Applications

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-14T06:51:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>`

```

I've been thinking about the modernization of COBOL applications running on 
a mainframe environment so I decided to work on a rambling set of questions.

Seems to me that there is growing move to "enable" mainframe functions with 
the littlest effort possible.  I've seen the obvious solutions that are move 
the application to a Unix flavor...or port some portion to .NET framework, 
however, I was thinking more of the case where the existing function is 
appropriate and what was needed was an extension out into the new world.   I 
am looking at the old application branching out as well as how new 
requirements can be solutioned in an existing environment using new 
tooling/design patterns.

For the existing case. If you can imagine - we have a module that updates a 
customer from some green screen.  I would want to enable the update function 
as a callable service.  All authorization and authentication issues aside - 
the desire would be to have a module that can be called by "either" the CICS 
transaction or via, say, a SOAP service request.

I don't see immediately how the architecture of a typical COBOL application 
would manage to accomplish this easily.  For existing function, it seems 
that there is a multi phase approach that is required - the extraction of 
business rules that define the operation (what is needed to update a 
customer), the extraction of the logic rules (who and how is this allowed) 
and the creation of the presentation of the rules. Finally, there is the 
communication of the request to the actual transaction.  For the new 
functions, it would be a much easier as it would be a case of just designing 
the modules with those business rules truly externalized in the first place.

Would it seem more appropriate that the a new calling module be "non CICS" 
and call the CICS module...and leaving the CICS green screen transactions as 
just with the function externalized...or does it make more sense to 
completely decouple the CICS from the act of updating the customer account? 
Can CICS call a non CICS program now that I think about it..? *It's been a 
while ;-) *

In my mind, it makes more sense to remove the CICS subsystem from the 
equation - but then I'm left with what is the best option to implement the 
transaction based activities...should I have a daemon running unders USS on 
z/OS or some other method of application triggering....?  CICS has been 
updated recently to be pretty flexible in terms of some web enablement but I 
just don't like the idea of it.  Is that *dumb* of me?

Should I look at migrating or using a z/Linux LPAR as the front door?  Seems 
to bring into play a lot of uneccessary networking - I don't believe that 
there is a communication channel supported...

I'm also looking at the same ideas for non CICS based items that are today 
Batch based but have some scope for function use.  The same question exists 
here...is there a standard transaction processor to use ?

Anyone have any good resources? Anything on creating mainframe web services 
framework - which, whilst not exactly what I'm looking at, would give me 
some good pointers.  Is there a decent example of how to setup portals for 
new functions...so for example, creating a portal so that an operations team 
could look at the current system status, or help desk look at customer 
configurations..etc..or setting up LDAP for authorizations, or UDDI 
registry,  etc etc?

To reiterate - I am not looking to move to Unix/Windows flavor platform 
(except if it can be resident on a mainframe).  If you believe the 
Windows/Unix is the only "real" method to do this type of work..I'd be 
interested to know why?

I think ultimately, I'd be really interested in something that was like the 
http://www.droplets.com/ which seems to be a pretty neat deployment method 
for mainframe activity :-)

My final question - if I may be so bold - is that reading online I see a lot 
of the function that is being enabled is simple presentation layer type 
items (so registering for a plane seat on the web versus on a green screen) 
or access to people's tax records.....does anyone know of a real example of 
a mainframe application being enabled to provide some function that could 
not be implemented using some Host-On-Demand, Java 3270 emulator ?  In other 
words, any true b2b type activity ?

This last question I didn't actually do any research yet, so I will probably 
go find some of those white paper customer success stories...so unless it is 
off the top of your head don't worry too much :-)

I will read this again tomorrow to see if it still makes sense...and make 
updates if necessary....

MANY thanks in advance...

JCE
```

#### ↳ Re: Modernization of COBOL Applications

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-14T14:14:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg9b7i$e0l$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>`

```
In article <sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:

[snip]

>For the existing case. If you can imagine - we have a module that updates a 
>customer from some green screen.  I would want to enable the update function 
>as a callable service.  All authorization and authentication issues aside - 
>the desire would be to have a module that can be called by "either" the CICS 
>transaction or via, say, a SOAP service request.

Where do the customer data 'live' (mainframe/elsewhere) and in what format 
(flat file/VSAM/database)?

>
>I don't see immediately how the architecture of a typical COBOL application 
…[4 more quoted lines elided]…
>and the creation of the presentation of the rules.

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

DD
```

##### ↳ ↳ Re: Modernization of COBOL Applications

- **From:** Jeff Lanam <jeff-dot-lanam@hp-dot-com-not.net>
- **Date:** 2005-09-14T17:09:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com>`

```
On Wed, 14 Sep 2005 14:14:10 +0000 (UTC), docdwarf@panix.com () wrote:

>
>
>(addendum to note to newbies - if you need to then ask a Local Geezer 
>'What is 'greenbar'?')
>


Big paper windows.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-14T17:50:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg9ntc$4q4$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com>`

```
In article <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com>,
Jeff Lanam  <jeff-dot-lanam@hp-dot-com-not.net> wrote:
>On Wed, 14 Sep 2005 14:14:10 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>Big paper windows.

Or maybe a drinking-establishment specialising in concoctions containing 
chartreuse.

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-09-19T20:53:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9c36a$432f6b7e$45491c57$18163@KNOLOGY.NET>`
- **In-Reply-To:** `<dg9ntc$4q4$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com> <dg9ntc$4q4$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com>,
> Jeff Lanam  <jeff-dot-lanam@hp-dot-com-not.net> wrote:
…[14 more quoted lines elided]…
> chartreuse.

So, basically any bar on St. Patty's Day, right?
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-20T09:12:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgojqo$kdd$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com> <dg9ntc$4q4$1@reader1.panix.com> <9c36a$432f6b7e$45491c57$18163@KNOLOGY.NET>`

```
In article <9c36a$432f6b7e$45491c57$18163@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <4jkgi19m5eqpsa2b1plqtmth0ctrlro9m2@4ax.com>,
…[12 more quoted lines elided]…
>So, basically any bar on St. Patty's Day, right?

Perhaps things have changed since I ceased frequenting such 
establishments... but what the advertisers used to call 'The Day For the 
Wearin' o' the Green' was not, as I recall it, one for sales of 
http://www.chartreuse.fr/pa_green&yellow_uk.htm.

DD
```

##### ↳ ↳ Re: Modernization of COBOL Applications

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-15T03:17:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3os7emF78ubjU1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dg9b7i$e0l$1@reader1.panix.com...
> In article <sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[83 more quoted lines elided]…
>

I 'm really sorry you did. That was brilliant! Some time ago I worked for a 
major insurer where we encountered this kind of nonsense frequently. I used 
to refer to these cases as the 'one legged black lesbian dwarves' (I was 
young and irreverent; nowadays I would drop the 'black'... It is really OK 
to insult disabled, gay, and especially, dwarves, in one sentence, but 
coloured people have definitely had enough...I'm not one to put the boot in 
when people are down... )  This is one of the best examples I have ever seen 
of the kind of exceptions that test program development. Managers want 
simple rules; the real world has the above.

Well done, Doc!

> (note to newbies - it might be helpful to keep situations like this in
> mind the next time you ask 'why would *anyone* code an IF statement that
> goes on for four-and-a-half pages of greenbar?')
>

No. It might be useful to keep in mind the basic tenets of Boolean 
simplification and reduce it to a few lines of greenbar... Or think about 
alternatives like EVALUATE...

> (addendum to note to newbies - if you need to then ask a Local Geezer
> 'What is 'greenbar'?')

Outside the US it is sometimes referred to as 'lineflo'.

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-15T11:49:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgbn4t$guv$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <3os7emF78ubjU1@individual.net>`

```
In article <3os7emF78ubjU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:dg9b7i$e0l$1@reader1.panix.com...

[snip]

>> ... et and cetera.  I think I'll stop now.
>>
>
>I 'm really sorry you did. That was brilliant!

Pfoo... you'se jes' easily impressed.

>Some time ago I worked for a 
>major insurer where we encountered this kind of nonsense frequently.

'Nonsense'?  That might be applied to 'true arcana', such as certain areas 
of accounting designed for Special Interests (I recall, vaguely, certain 
oil-revenue procedures that were valid only in the states of Oklahoma, 
Arkansas and Texas (named OAT for that reason) but I chose those examples 
because they'd make sense to Just About Anyone who has submitted an 
insurance-claim.

>I used 
>to refer to these cases as the 'one legged black lesbian dwarves' (I was 
…[3 more quoted lines elided]…
>when people are down... )

Not even in your own mouth?  (Sorry... cheap shot but I couldn't resist.)

>This is one of the best examples I have ever seen 
>of the kind of exceptions that test program development. Managers want 
>simple rules; the real world has the above.

Linking to the Management thread?  I'd say 'No... Managers (and users) do 
not want simple rules, they want complex rules implemented exactly as they 
intended no matter how simplistically they were stated.  (see 'DWIM 
command (absence thereof)')

>
>Well done, Doc!

See above about 'easily impressed'... but thanks, anyhow.

>
>> (note to newbies - it might be helpful to keep situations like this in
…[6 more quoted lines elided]…
>alternatives like EVALUATE...

Eh?  The code to deal with this was written, tested and has been running 
since the shop upgraded to a System/370; it Ain't Broke... and besides, 
whose budget is going to be used for it?  (back to Management)

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-17T05:08:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p0cgsF7rmd4U1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <3os7emF78ubjU1@individual.net> <dgbn4t$guv$1@reader1.panix.com>`

```
 

<docdwarf@panix.com> wrote in message news:dgbn4t$guv$1@reader1.panix.com...
> In article <3os7emF78ubjU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[22 more quoted lines elided]…
>
I was using 'nonsense' in the non-literal sense (which is often employed in 
the U.K.) to represent anything that is a tiresome exception to some 
established rule. I agree that your examples are literally far from 
nonsensical.

You really are too literal, Doc... :-)

>>I used
>>to refer to these cases as the 'one legged black lesbian dwarves' (I was
…[7 more quoted lines elided]…
>
I would expect nothing less than a low blow from a dwarf...

>>This is one of the best examples I have ever seen
>>of the kind of exceptions that test program development. Managers want
…[5 more quoted lines elided]…
> command (absence thereof)')

Then we have to disagree. My experience is that most people prefer 
non-complexity and that is what often leads to oversimplification and 
consequent failure in systems...

As for DWIM... I remember reading an internal tehnical paper many years ago 
(around 30, actually) when I was working for CDC, which claimed that the 
company's tech researchers had succeeded in fabricating memory from tachyon 
particles. (Tachyons, for those without an affinity for Physical Science, 
are rmarkable because they actually move backwards in time; popping into 
existence when they are extremely old, gradually getting younger and 
younger, until finally popping out again...) The tachyon memory, it was 
claimed, would revolutionise the computer industry, because it meant that a 
computer so equipped would know the answer  to your question before you had 
asked it...
>
>>
…[16 more quoted lines elided]…
> whose budget is going to be used for it?  (back to Management)

The same budget that has someone permanently on call because it keeps 
failing in the said 'IF'... In the long run, surgery is cheaper than many 
packets of band aids...

And besides, there is much more job satisfaction in reducing four pages to 
15 lines or so, so people will find the time, whether it is budgeted or not. 
(It's the sort of thing I would have once taken home at the weekend to amuse 
myself with instead of the Sunday crossword. In fact, I seem to remember 
some years ago Eileen (Yukon Mama) posting such an example and I did 
simplify it instead of doing a cryptic crossword...

http://groups.google.co.nz/group/comp.lang.cobol/browse_frm/thread/451c55148d10483e/ebf2cc8f052c4ed3?tvc=1&q=group:comp.lang.cobol+author:YukonMama&hl=en#ebf2cc8f052c4ed3

Check entry 21 from 'anonymous' in the thread.

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-09-16T12:45:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126899943.812325.14520@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3p0cgsF7rmd4U1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <3os7emF78ubjU1@individual.net> <dgbn4t$guv$1@reader1.panix.com> <3p0cgsF7rmd4U1@individual.net>`

```

Pete Dashwood wrote:
I'm not one to put the boot
> >>in
> >>when people are down... )
…[4 more quoted lines elided]…
> 
That one was beneath you, Peter.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-17T11:46:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dggvmk$l6r$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dgbn4t$guv$1@reader1.panix.com> <3p0cgsF7rmd4U1@individual.net> <1126899943.812325.14520@g49g2000cwa.googlegroups.com>`

```
In article <1126899943.812325.14520@g49g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>
>Pete Dashwood wrote:
…[8 more quoted lines elided]…
>That one was beneath you, Peter.

Still... no need to get short with him over it.

(come to think of it... hard to get short with him *under* it, as well)

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** James Johnson <saildot.maryland@verizon.net>
- **Date:** 2005-09-17T01:16:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<garmi1tmj78apruv7aurgbrg0r2htiepm7@4ax.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <3os7emF78ubjU1@individual.net> <dgbn4t$guv$1@reader1.panix.com> <3p0cgsF7rmd4U1@individual.net>`

```
On Sat, 17 Sep 2005 05:08:34 +1200, "Pete Dashwood" <dashwood@enternet.co.nz>
wrote:

> 
>
…[91 more quoted lines elided]…
>
When I was a beginning programmer I was working on such a problem and came up
with a solution to fix the problem and incidentally reduce those 4 pages  to 1/4
of a page of code.  In the tech review meeting my work leader tore my head off
about my solution and directed me to just "bandaid" it.   Embarrassed and hurt I
later found that she had been  the original coder of that 4 page IF statement.  

Man is not a rational animal.  We just pretend to be sometimes.

JJ

>And besides, there is much more job satisfaction in reducing four pages to 
>15 lines or so, so people will find the time, whether it is budgeted or not. 
…[11 more quoted lines elided]…
>

James Johnson
remove the "dot" from after sail in email address to reply
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-17T11:45:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dggvla$q6a$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <3os7emF78ubjU1@individual.net> <dgbn4t$guv$1@reader1.panix.com> <3p0cgsF7rmd4U1@individual.net>`

```
In article <3p0cgsF7rmd4U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
> 
>
…[29 more quoted lines elided]…
>nonsensical.

... and in the case of insurance they were the established rules, as well.

>
>You really are too literal, Doc... :-)

I am not bigrammatic!  Oh... not 'two literals', sorry.

[snip]

>>>This is one of the best examples I have ever seen
>>>of the kind of exceptions that test program development. Managers want
…[9 more quoted lines elided]…
>consequent failure in systems...

It is a wonderful world which has such varied experiences in it, aye.

>
>As for DWIM... I remember reading an internal tehnical paper many years ago 
…[8 more quoted lines elided]…
>asked it...

This seems to be a variant of Asimov's 'thiotimoline', a compound so 
soluble that it dissolves in water before the water is added.

[snip]

>>>> (note to newbies - it might be helpful to keep situations like this in
>>>> mind the next time you ask 'why would *anyone* code an IF statement that
…[13 more quoted lines elided]…
>packets of band aids...

I have never, Mr Dashwood, heard of a system so well-written that the 
on-call positions were disbanded; management seems to have learned that 
there's *always* something to go wrong, someplace, and if someone else 
isn't on call then the manager gets called.

>
>And besides, there is much more job satisfaction in reducing four pages to 
>15 lines or so, so people will find the time, whether it is budgeted or not. 

Of course this is so... and I am the King of England, you may call me Your 
Majesty.  With all due respect, Mr Dashwood, if your assertion were true 
then there would be no more four-and-a-half page IFs left over from the 
System/370 coversion... and a few are still out there, I believe.

>(It's the sort of thing I would have once taken home at the weekend to amuse 
>myself with instead of the Sunday crossword. In fact, I seem to remember 
>some years ago Eileen (Yukon Mama) posting such an example and I did 
>simplify it instead of doing a cryptic crossword...

Using yourself as a comparative, Mr Dashwood?  That way can lead to 
disappointment.

DD
```

##### ↳ ↳ Re: Modernization of COBOL Applications

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-09-17T10:37:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7Nednex7Qcm5trHeRVn-2w@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:

> In article <sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[80 more quoted lines elided]…
> ... et and cetera.  I think I'll stop now.
Let me throw in a few unpopular ideas.
1. The Murach/Noll combine in one of their books ( I forget which)
recommended against CICS decades ago. Among other things it isn't COBOL,
and it is slow to code. So the first few things to consider are separating
the user interface part of the app from the logic part and then working
toward a different user interface as a callable function. There are several
imperfect possibilities, such as html, Tcl/Tk and the somewhat dubious
screen section in (more or less) standard COBOL. But the interface should
be portable. 

2. The EVALUATE verb is only slightly less obnoxious than its immediate
parent, the extraordinarily convoluted nested IF. I use neither. For one
thing both violate the COBOL principles that any action is terminated by a
period, and any action takes one or at most two lines of code. The simple
"test this field for a value and then proceed accordingly" situation is
best solved by a string of equally simple if statements. Since the field
can only hold one value at a time there is no need for complicated and
buggy ELSE IF nesting. And the professor types would have you indenting the
code clear off the page, all in the name of readability. Nonsense.

Now what about the dwarf minority lesbian or her cousin the red-haired
left-handed Eskimo shortstop? Well there are two approaches I might favor.
The first might be called the flowchart approach. You test for a condition
and then perform a lower level module that tests for another condition etc. 
But I prefer the Decision Logic Table approach for this kind of complexity.
First you build the DLT, then you boil it down to its most economic size,
and then you implement each rule with a complex IF such as 
IF A AND B AND C AND NOT D PERFORM X-SEQUENCE. This involves liberal use of
condition names and switches of course. But all the logic fits on one or
two lines. And the logic behind the logic is analyzed and tested beforehand
during the DLT analysis. This is not the swiftest way home, but it is clear
and understandable even six months after you wrote it. And you can show the
DLT to the consumer and ask the the Peggy Lee torch song question: "is that
all there is?"  Chances are excellent that there are at least three other
special situations that said consumer forgot to mention. 

Many decades ago, before Murach, before even Dykstra, the Navy Programming
Languages Division came up with a Decision Logic Table Translator, written
in COBOL of course, which would take a DLT embedded as comment statements
in a source program and translate it to executable code. There were tons of
GO TOs generated. I still have the code somewhere.

Those who have never heard of a DLT are banished to the minor league. Those
who never heard of the Navy Programming Languages Division are remanded to
Java-Script or Visual Basic or whatever.  

Enough, I have to clean up the puppy pen and do some real work on the
computer. Sometimes it is difficult to distinguish between the two tasks. 
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-17T15:39:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dghdal$l7e$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com>`

```
In article <7Nednex7Qcm5trHeRVn-2w@adelphia.com>,
John Culleton  <john@wexfordpress.com> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Now... the question of 'the extraction of business rules' and 'the
>> extraction of logic rules' is where it gets sticky.  Take the example of
…[24 more quoted lines elided]…
>> ... et and cetera.  I think I'll stop now.

[snip]

>First you build the DLT, then you boil it down to its most economic size,
>and then you implement each rule with a complex IF such as 
>IF A AND B AND C AND NOT D PERFORM X-SEQUENCE. This involves liberal use of
>condition names and switches of course. But all the logic fits on one or
>two lines.

Hmmmm... so the abovementioned situation might boil down to 'one or two 
lines' like...

IF UTERINE-INFECTION-CLAIM AND POLICY-RIDER-EXISTS AND (POLICYHOLDER = 
FEMALE OR PERSON-COVERED = FEMALE) AND (HYSTERECTOMY-NOT-PERFORMED OR 
HYSTERECTOMY-DATE < UTERINE-INFECTION-TREATMENT-DATE) AND 
(UTERINE-INFECTION-TREATMENT-DATE < POLICY-RIDER-EFFECTIVE-DATE)...

If I am correct then a difficulty might be found in directing the flow of 
processing for 'sub-conditions', something you'd want to do if the first 
two are true and the third false, the first three true and the fourth 
false, etc... or am I missing something?

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-09-17T13:59:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sidnZ0ir9EJx7HeRVn-jw@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <dghdal$l7e$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:

> In article <7Nednex7Qcm5trHeRVn-2w@adelphia.com>,
> John Culleton  <john@wexfordpress.com> wrote:
…[54 more quoted lines elided]…
> DD
Grr. Now I have to do some work, which I hate. I much prefer to BS my way
through life. I will put together the DLT as a graphic (it is impossible to
line up columns in an email) and post it somewhere. 

As for subconditions, the action of a rule in a DLT can be to process
another DLT.  But that gets us back into flowchart logic. The science of
DLT is explained in books. The art consists of knowing how complex a DLT do
you allow before breaking it off and creating another.  
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-09-17T14:37:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com>`

```
John Culleton wrote:

> docdwarf@panix.com wrote:
> 
…[65 more quoted lines elided]…
> do you allow before breaking it off and creating another.

My solution posted here:

http://wexfordpress.com/tex/dlt.pdf

Criticisms/corrections accepted with my usual grumpiness.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-17T22:04:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgi3u8$8mg$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>`

```
In article <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>,
John Culleton  <john@wexfordpress.com> wrote:

[snip]

>My solution posted here:
>
>http://wexfordpress.com/tex/dlt.pdf

Looks like my guess was close... but as my first programming instructor 
used to say, 'Examples in books are not always compiled.'

PERFORM PAY CLAIM?

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 7)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-09-17T18:59:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XaudnZ3o9cJkPbHeRVn-pA@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:

> In article <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>,
> John Culleton  <john@wexfordpress.com> wrote:
…[12 more quoted lines elided]…
> DD
(grump)
So you never forgot a hyphen?
(end grump)
Anyhow did you like/dislike the ultimate result (with error corrected)?
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-18T01:01:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b03Xe.85845$AI1.61342@fe02.news.easynews.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com>`

```
Personally, I'll take a COBOL EVALUATE statement  (or nested EVALUATEs if 
needed) every time - when trying to implement a complex decision table. 
However, I do accept this as a "style" issue and probably based on what COBOL 
syntax (and semantics) one is already (most) familiar with.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-18T17:44:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p4f0lF8ll8hU1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com>`

```
Sorry, John, I didn't like it because of the duplication of code...

IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE >RIDER-DATE AND 
HYSTERECTOMY AND HYS-DATE > INFECTION-DATE
PERFORM PAY CLAIM
ELSE
IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE AND 
NO-HYSTERECTOMY
PERFORM PAY CLAIM
ELSE
PERFORM DENY-CLAIM.

Applying Boolean simplification, becomes...

IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE
    IF (NOT HYSTERECTOMY OR HYS-DATE > INFECTION-DATE)
         PERFORM PAY-CLAIM
    ELSE
         PERFORM DENY-CLAIM
    END-IF
END-IF

I agree with Bill, it comes down to style.

Pete.

"John Culleton" <john@wexfordpress.com> wrote in message 
news:XaudnZ3o9cJkPbHeRVn-pA@adelphia.com...
> docdwarf@panix.com wrote:
>
…[19 more quoted lines elided]…
> -- 
No, it doesn't get my vote. I believe the less code there is the less chance 
for error there is, and it is easier to read and absorb small constructs 
rather than long ones. Besides, knowing I did something twice when there was 
really no need to, just makes me wake up sweating... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 9)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-09-18T09:39:20+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q2qi15mlfghnafvhinqp2fl4i4rt5ghb1@4ax.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net>`

```
On Sun, 18 Sep 2005 17:44:39 +1200 "Pete Dashwood" <dashwood@enternet.co.nz>
wrote:

:>Sorry, John, I didn't like it because of the duplication of code...

:>IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE >RIDER-DATE AND 
:>HYSTERECTOMY AND HYS-DATE > INFECTION-DATE
:>PERFORM PAY CLAIM
:>ELSE
:>IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE AND 
:>NO-HYSTERECTOMY
:>PERFORM PAY CLAIM
:>ELSE
:>PERFORM DENY-CLAIM.

:>Applying Boolean simplification, becomes...

:>IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE
:>    IF (NOT HYSTERECTOMY OR HYS-DATE > INFECTION-DATE)
:>         PERFORM PAY-CLAIM
:>    ELSE
:>         PERFORM DENY-CLAIM
:>    END-IF
:>END-IF

Not identical.

What if CLAIMANT-FEMALE is false?

Be careful when "simplifying" logic.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-18T23:50:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p52jpF8lvukU1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net> <8q2qi15mlfghnafvhinqp2fl4i4rt5ghb1@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message 
news:8q2qi15mlfghnafvhinqp2fl4i4rt5ghb1@4ax.com...
> On Sun, 18 Sep 2005 17:44:39 +1200 "Pete Dashwood" 
> <dashwood@enternet.co.nz>
…[26 more quoted lines elided]…
> What if CLAIMANT-FEMALE is false?

The claim will not be paid.  However, I didn't specifically deny it because 
of a mistake I made when hurriedly 'translating' into symbolic notation...
>
> Be careful when "simplifying" logic.

Sound advice. I usually am, but slipped up on this occasion. Thanks for 
spotting it.

I hasten to add that in a 'real' environent it would have failed the testing 
and I would then have fixed it... (well, that's my story and I'm sticking to 
it... :-))

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 9)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-09-18T07:04:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<3p4f0lF8ll8hU1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net>`

```


Pete Dashwood wrote:
 > (snip)
> Sorry, John, I didn't like it because of the duplication of code...
…[23 more quoted lines elided]…
> Pete.

Err...Shouldn't that be more like this:

PROCESS-UTERINE-INFECTION.

IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE
     IF NOT HYSTERECTOMY
     OR HYS-DATE > INFECTION-DATE
          PERFORM PAY-CLAIM
     ELSE
         PERFORM DENY-CLAIM
     END-IF
ELSE
     PERFORM DENY-CLAIM      <== the missing path...
END-IF

Splitting up the OR is my stylistic preference (not a quibble with 
your excellent simplification), but it seems to me that if this logic 
is to be restricted to processing a claim for uterine infection then 
an ELSE path was omitted.

Of course, I could be wrong about that.

On the other hand, I thought Richard's EVALUATE statement was fairly 
easy to understand.  Perhaps if there were a Decision Table translator 
for COBOL it would generate COBOL code that looked like that.  At 
least I hope so.

I have to admit I am very weak on Decision Tables.  I don't remember 
them being covered at all where I learned programming.  It seems to me 
that the descriptions of LEX and YACC that I have read sound like a 
form of decision table processing generated from some rule 
specifications.

As a side note, I heard an anecdote about a very large mainframe 
financial application written in COBOL with an extremely complex 
decision table.  The decision table was so large that the developers 
built a MicroFocus COBOL program to pre-process the decision table 
rules and generate an optimized COBOL decision table as a code 
fragment, which was then copied into the mainframe COBOL programs.  It 
drove the project manager crazy when he found out his mainframe 
programs were partially written by PC programs.

With kindest regards,
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-19T00:11:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p53scF8jeogU1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net> <tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net...
>
>
…[42 more quoted lines elided]…
>
Yes.

(Hangs head, shuffles feet, mumbles apology... and refers back to Benyamin's 
spotting of the same error...)

> Splitting up the OR is my stylistic preference (not a quibble with your 
> excellent simplification), but it seems to me that if this logic is to be 
> restricted to processing a claim for uterine infection then an ELSE path 
> was omitted.
>
Yes, I agree. I would also normally put the OR on a second line. On this 
occasion I was cutting and pasting John's code.

> Of course, I could be wrong about that.
>
No, you and Benyamin both spotted it correctly. I checked the symbolic 
translation I did and found it immediately... I did do it quickly, but it's 
no excuse... guess I'm getting old... :-)

I would actually go further if I was serious about this.... The real code I 
would use would be something like...
01  CLAIM-FLAG PIC X VALUE SPACE.
      88  PAYING-CLAIM      VALUE '1'.
      88  DENYING-CLAIM   VALUE ZERO.
...
PROCESS-UTERINE-INFECTION-CLAIM.
      SET DENY-CLAIM TO TRUE
      IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE
           IF (NOT HYSTERECTOMY)
                         OR
                (HYS-DATE > INFECTION-DATE)
                       SET PAY-CLAIM TO TRUE
           END-IF
      END-IF
(Any other processing that might be common between the Paying and Denying 
process, or any other processing connected with this type of claim that 
might be added later, and could override whether it is paid or 
denied...)...then...
     IF PAYING-CLAIM
          PERFORM PAY-CLAIM
     ELSE
          PERFORM DENY-CLAIM
     END-IF

> On the other hand, I thought Richard's EVALUATE statement was fairly easy 
> to understand.

Yes, I liked that too.

> Perhaps if there were a Decision Table translator for COBOL it would 
> generate COBOL code that looked like that.  At least I hope so.
…[14 more quoted lines elided]…
>
"The best tools for the job..."

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-19T00:20:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p54c9F8oov9U1@individual.net>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net> <tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net> <3p53scF8jeogU1@individual.net>`

```
Ouch! Please replace the code I posted as follows:

I would actually go further if I was serious about this.... The real code I
would use would be something like...
01  CLAIM-FLAG PIC X VALUE SPACE.
      88  PAYING-CLAIM      VALUE '1'.
      88  DENYING-CLAIM   VALUE ZERO.
...
PROCESS-UTERINE-INFECTION-CLAIM.
      SET DENYING-CLAIM TO TRUE
      IF CLAIMANT-FEMALE AND POLICY-RIDER AND INFECTION-DATE > RIDER-DATE
           IF (NOT HYSTERECTOMY)
                         OR
                (HYS-DATE > INFECTION-DATE)
                       SET PAYING-CLAIM TO TRUE
           END-IF
      END-IF
(Any other processing that might be common between the Paying and Denying
process, or any other processing connected with this type of claim that
might be added later, and could override whether it is paid or
denied...)...then...
     IF PAYING-CLAIM
          PERFORM PAY-CLAIM
     ELSE
          PERFORM DENY-CLAIM
     END-IF

(sigh...)

Pete.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 10)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-20T20:55:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jH_Xe.180229$wr.13468@clgrps12>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com> <3p4f0lF8ll8hU1@individual.net> <tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net>`

```
"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:tk8Xe.267908$5N3.245937@bgtnsc05-news.ops.worldnet.att.net...
> As a side note, I heard an anecdote about a very large mainframe financial 
> application written in COBOL with an extremely complex decision table. 
…[5 more quoted lines elided]…
> programs.


    And yet the manager was not upset when he found out that his programmers 
were only describing the algorithms to perform in some high level language, 
while all the "real" work of transforming this into code you could actually 
run was being done by the compiler?

    Had I discovered this thread earlier, I was actually going to suggest, 
as an alternate solution, to write a tool (perhaps a plugin to an IDE) that 
would let you draw state diagrams 
(http://en.wikipedia.org/wiki/State_diagram), and which would automatically 
generate the COBOL code for you. These state diagrams would then BE the 
source code (for that particular module of the application anyway), and 
COBOL would be a lower level representation to it, just as machine code is a 
lower level representation of COBOL code.

    Writing programs which write programs which write programs which write 
programs (and so on ad nauseum) is actually considered typical in the shop 
I'm working at. You have to force yourself to *FORGET* the big picture, and 
only concentrate on the task at hand, less you start suffering from vertigo.

    - Oliver
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-18T12:09:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgjleb$osm$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <dgi3u8$8mg$1@reader1.panix.com> <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com>`

```
In article <XaudnZ3o9cJkPbHeRVn-pA@adelphia.com>,
John Culleton  <john@wexfordpress.com> wrote:
>docdwarf@panix.com wrote:
>
…[17 more quoted lines elided]…
>(end grump)

Compilers... the close-to-original spell-checkers.

>Anyhow did you like/dislike the ultimate result (with error corrected)?

It seems to have produced results close to my guess, Mr Culleton... but 
I've not seen the tool applied to a project of any scope so more than that 
I cannot say.  One swallow, summer making, that sor of thing.

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-17T22:06:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127019992.133792.264170@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com>`

```
> http://wexfordpress.com/tex/dlt.pdf

This can be mechanistically converted to an EVALUATE:

<code>

       IDENTIFICATION DIVISION.
       PROGRAM-ID.     dt.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  Claimant-Sex                PIC X.
           88  Claimant-Female         VALUE "F".
       01  Policy-Status               PIC X.
           88  Policy-Rider            VALUE "Y".
       01  Womb-Status                 PIC X.
           88  Hysterectomy            VALUE "Y".
       01  Hys-Date                    PIC 9(8).
       01  Inf-Date                    PIC 9(8).
       01  Rider-Date                  PIC 9(8).

       PROCEDURE DIVISION.
       DTTest.

           EVALUATE Claimant-Female
               ALSO Policy-Rider
               ALSO Inf-Date > Rider-Date
               ALSO Hysterectomy
               ALSO Hys-Date > Inf-Date

           WHEN     TRUE
               ALSO TRUE
               ALSO TRUE
               ALSO TRUE
               ALSO TRUE

                   PERFORM Pay-Claim

           WHEN     TRUE
               ALSO TRUE
               ALSO TRUE
               ALSO FALSE
               ALSO ANY

                   PERFORM Pay-Claim

           WHEN OTHER

                   PERFORM Deny-Claim

           END-EVALUATE

           STOP RUN.

       Pay-Claim.
                   
       Deny-Claim.

       END PROGRAM dt.
</code>
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 7)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-09-18T09:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QtednVtpZ4JB8bDeRVn-tQ@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com> <mL-dnSc-y4sR_rHeRVn-vA@adelphia.com> <1127019992.133792.264170@g49g2000cwa.googlegroups.com>`

```
Richard wrote:

>> http://wexfordpress.com/tex/dlt.pdf
> 
…[58 more quoted lines elided]…
> </code>

De gustibus non est disputandum or something like that. (My Latin is a bit
weak. 

The tradeoff taken in my solution is to get the logic right with the fewest
chances of errors. It is not unusual to have half a dozen or more rules in
a DLT. If you just go down each "rule" mechanically and code a huge IF
statement for each the logic will be correct. True the code will not be as
compact or as elegant as a more complex solution with ORs etc. But accuracy
is the key, and for the complex choice--complex action  situation (the
example given is still pretty simple) the DLT gives the best chance of a
correct result first time. Note that my first DLT had an error and someone
else's code had an error. But I was able to spot and correct my error at
the DLT stage.

And my solution is also efficient in programmer time. I coded the first big
IF, then duplicated it using my editor, and deleted the unneeded code. 

YMMV of course. 

For a good book on DLT I recommend _Decision Tables in Software Engineering_
by Richard Hurley, ISBN 0-442-23599-2. Available used and new on Amazon.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-17T21:51:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgi34h$3kh$1@reader1.panix.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <dghdal$l7e$1@reader1.panix.com> <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com>`

```
In article <7sidnZ0ir9EJx7HeRVn-jw@adelphia.com>,
John Culleton  <john@wexfordpress.com> wrote:
>docdwarf@panix.com wrote:
>
>> In article <7Nednex7Qcm5trHeRVn-2w@adelphia.com>,
>> John Culleton  <john@wexfordpress.com> wrote:

[snip]

>>>First you build the DLT, then you boil it down to its most economic size,
>>>and then you implement each rule with a complex IF such as
…[18 more quoted lines elided]…
>through life.

Oh, I *cannot resist...

... looking to move up to Management, eh?

>I will put together the DLT as a graphic (it is impossible to
>line up columns in an email) and post it somewhere. 

That would be of interest, I'd say... and those 'all ya gotta do is' 
solutions have a tendency, in my experience, to require others to do More 
Work.

>
>As for subconditions, the action of a rule in a DLT can be to process
>another DLT.  But that gets us back into flowchart logic.

Funny how those Hoary Ancient Practises keep rearing their ugly heads, 
aye.

>The science of
>DLT is explained in books. The art consists of knowing how complex a DLT do
>you allow before breaking it off and creating another.  

If my clients wanted artists they'd hire (insert name of 
painter/sculptor/worker in other medium here).  They want code so they 
call for (echo chamber on) CAAAPPPPPTTTAAAIIIIINNNNNNN... COBOL... OBOl... 
OBol... Obol.

DD
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-17T12:18:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126984717.455391.125640@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<7Nednex7Qcm5trHeRVn-2w@adelphia.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com>`

```

John Culleton wrote:
> But I prefer the Decision Logic Table approach for this kind of complexity.
> First you build the DLT, then you boil it down to its most economic size,
> and then you implement each rule with a complex IF ...

There were several decision table preprocessors available many years
ago, I still have a couple of books on the subject. They were a good
method of implementing a design by taking specs that were created as
decision tables and simply dropping these into the source code and
letting the preprocessor tell you what was wrong.

The EVALUATE was designed to emulate and replace decision tables but
got it 'sideways'. Also a proper preprocessor would evaluate all the
conditions specified and tell you what combinations were not included.

I don't know of any DT preprocessors that are available today.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-09-17T17:29:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ip2rlklul679b@corp.supernews.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1126984717.455391.125640@f14g2000cwb.googlegroups.com...
[snip]
> I don't know of any DT preprocessors that are available today.

Then let me inform you that though the full product may
not be available today; "A free preview release of
LogicGem 3.0 is available for download. Please note
that the preview will expire on October 1, 2005. "
< http://www.catalyst.com/products/logicgem/ >

"LogicGem is a Decision Table or Logic Table processor.
You populate a table with a set of conditions and
corresponding actions that can apply to those conditions
and LogicGem will complete the table for you by finding
any missing rules and automatically removing all of the
redundant rules. It is the only method whereby you are
assured of mathematical perfection for your logic. Once
the logic has been perfected, LogicGem will then translate
the completed table into source code for the language of
your choice, including English for documentation purposes."

However, "language of choice" does not include COBOL.
From < http://www.catalyst.com/products/logicgem/release.html >,
"Computer languages supported are BASIC, C, C++,
Fortran, FoxPro, Java, Pascal, PowerBuilder, SAS,
Visual Basic, Visual Basic.NET, Visual C#.NET, and
XBase.

I reviewed LogicGem 2.0 (a DOS product) about ten years
ago; but never used that product.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-23T02:02:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127466168.315083.151580@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1126984717.455391.125640@f14g2000cwb.googlegroups.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com>`

```
> I don't know of any DT preprocessors that are available today.

Here's one that I prepared earlier today:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.     dtprocess.
      * Copyright Azonic Associates 2005
      * 23 September 2005
      * released under the Gnu Public License (GPL)
      * this code may be used and modified as long
      * as this copyright notice is included.
      *
      * The source program being processed may contain a number
      * of decision tables. Each table must be laid out as:
      *
      * *>header         rulehead
      *    copy line
      * *>conditions     rules
      * *>section separator
      * *>actions        actionqualifiers
      * *>terminator line
      *
      * Each line between the header and the terminator inclusive,
      * except the copy line, must have an '*' in column 7
      * and a '>' or space in column 8.
      *
      * Header:
      *
      *    The Header starts a Decision Table and, starting with
      *    the asterisk in column 7 is:
      *
      *        *>DECISION-TABLE name            1 2 ... E
      *
      *    The name is documentary only and must start in column
      *    24 and not contain any spaces.
      *
      *    The remainder of the line will contain the rule numbers
      *    which are one or two digits except the last which is
      *    the 'else' rule and must be numbered as E.
      *
      *    There must be at least one space between each rule
      *    number.
      *
      * copy line:
      *
      *    The copy line specifies the output file for the decision
      *    table code. It must not be a comment line as it will be
      *    used to read the source file into the program:
      *
      *    Temporary rule: the name must not contain a '.'.
      *
      *        COPY "dtsourcecob".
      *
      * Condition Lines:
      *
      *    Must have '*' in col 7 a condition starting in col 9.
      *    In the column under the rule number in the header the
      *    condition value should be set to 'Y', 'N' or '-' where:
      *
      *         Y   indicates the condition is to be true
      *         N   indicates the condition is not to be true
      *         -   indicates the condition is not tested
      *
      * Separator line
      *
      *    Must have '*' in col 7 and at least 6 hyphens starting
      *    in column 9:
      *
      *    *>-----------------------------
      *
      * Action Lines:
      *
      *    Must have '*' in col 7 an imperitive statement starting
      *    in col 9.
      *    In the column under the rule number in the header the
      *    action value should be set to '*', or space where:
      *
      *         *   indicates the action is to be performed
      *       space indicates the action is not to be performed
      *
      * Terminator line
      *
      *    Must have '*' in col 7 and 'END-TABLE' starting
      *    in column 9, the name is optional:
      *
      *       *>END-TABLE name
      *
      * Limits:
      *
      *    Rules:      50
      *    Conditions: 50
      *    Actions:    50
      *
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           ARGUMENT-NUMBER   IS Argument-Number
           ARGUMENT-VALUE    IS Argument-Value
           .
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           SELECT Source-File
               ASSIGN Source-Name
               ORGANIZATION LINE SEQUENTIAL
               FILE STATUS File-Status.

           SELECT Copy-File
               ASSIGN Copy-Name
               ORGANIZATION LINE SEQUENTIAL
               FILE STATUS File-Status.

       DATA DIVISION.
       FILE SECTION.
       FD  Source-File.
       01  Source-Line.
           03  Source-No               PIC X(6).
           03  Source-Flag             PIC X.
           03  Source-Body             PIC X(249).

       FD  Copy-File.
       01  Copy-Line                   PIC X(256).

       WORKING-STORAGE SECTION.
       01  File-Status.
           03  FS-1                    PIC X.
           03  FS-2                    PIC X.

       01  Source-Name                 PIC X(80).
       01  Copy-Name                   PIC X(80).

       01  In-Decision                 PIC X.
       01  In-Name                     PIC X.
       01  In-Rule                     PIC X.
       01  In-Conditions               PIC X.
       01  In-Actions                  PIC X.
       01  Action-OK                   PIC X.
       01  C                           PIC X.

       01  I                           PIC S9(4).
       01  OI                          PIC S9(4).

       01  Work-Text                   PIC X(80).
       01  Work-Col                    PIC 999.
       01  Text-Len                    PIC 999.

       01  Header-Hold                 PIC X(256).

       01  DT-Data.
           03  DT-Name                 PIC X(32).
           03  DT-CLimit               PIC 9(4).
           03  DT-CIndex               PIC 9(4).
           03  DT-RLimit               PIC 9(4).
           03  DT-RIndex               PIC 9(4).
           03  DT-SLimit               PIC 9(4).
           03  DT-SIndex               PIC 9(4).

           03  DT-Columns              OCCURS 50.
            05 DT-Rule                 PIC XX.
            05 DT-Column               PIC 999.

           03  DT-Conditions           OCCURS 50.
            05 DT-Condition            PIC X(80).
            05 DT-Rules                OCCURS 50.
               07  DT-Rule-Entry       PIC XX.

           03  DT-Sources              OCCURS 50.
            05 DT-Source               PIC X(80).
            05 DT-Actions              OCCURS 50.
               07  DT-Action-Entry     PIC XX.


       PROCEDURE DIVISION.
       Decision-Table.

           MOVE SPACES          TO Source-Name
           DISPLAY 1          UPON Argument-Number
           ACCEPT Source-Name FROM Argument-Value
               ON EXCEPTION
                   CONTINUE
           END-ACCEPT
           IF ( Source-Name = SPACES )
               DISPLAY "ERROR: No filename specified."
               PERFORM Program-Usage
           ELSE
               OPEN INPUT Source-File
               IF ( FS-1 NOT = "0" )
                   DISPLAY "ERROR: File not found " Source-Name
                   PERFORM Program-Usage
               ELSE
                   PERFORM Process-Source
                   CLOSE Source-File
               END-IF
           END-IF

           STOP RUN
           .
       Program-Usage.
           DISPLAY "dtprocess Decision Table preprocessor"
           DISPLAY "Usage:"
           DISPLAY "       dtprocess sourcefilename"
           DISPLAY " "
           DISPLAY "Copyright Azonic Associates 2005"
           .

       Process-Source.

           MOVE SPACES         TO Source-Line
                                  In-Decision

           PERFORM
               UNTIL Source-Line = HIGH-VALUES

               READ Source-File
                   AT END
                       MOVE HIGH-VALUES TO Source-Line
                   NOT AT END
                   IF ( Source-Body = SPACES )
                       CONTINUE
                   ELSE
                   IF ( In-Decision = "Y" )
                       PERFORM Process-Decision
                   ELSE
                   IF ( Source-Flag = "*" )
                       PERFORM Process-Comment
                   END-IF
                   END-IF
                   END-IF
               END-READ
           END-PERFORM
           .

       Process-Comment.

           IF ( Source-Body(2:14) = "DECISION-TABLE" )
               MOVE Source-Line    TO Header-Hold
               MOVE "Y"            TO In-Decision
               PERFORM Initialise-DT-Data
               PERFORM Process-Decision-Header
               DISPLAY "Processing table " DT-Name
               MOVE "Y"            TO In-Conditions
               MOVE SPACE          TO In-Actions
           END-IF
           .

       Initialise-DT-Data.

           MOVE SPACES     TO DT-Data
           MOVE ZERO       TO DT-CIndex
                              DT-CLimit
                              DT-RIndex
                              DT-RLimit
                              DT-SIndex
                              DT-SLimit
           .

       Process-Decision-Header.

           MOVE ZERO           TO Text-Len
           MOVE 17             TO I
           MOVE ZERO           TO OI
           MOVE "Y"            TO In-Name
           PERFORM
               UNTIL I > 249

               MOVE Source-Body(I:1) TO C
               IF ( C = SPACE )
                   IF ( In-Name = "Y" )
                       MOVE Work-Text TO DT-Name
                       MOVE SPACE    TO In-Name
                       MOVE SPACE    TO Work-Text
                       MOVE ZERO     TO OI
                   ELSE
                   IF ( In-Rule = "Y" )
                       ADD 1         TO DT-RLimit
                       MOVE Work-Text TO DT-Rule(DT-RLimit)
                       MOVE Work-Col TO DT-Column(DT-RLimit)
                       MOVE SPACE    TO In-Rule
                       MOVE SPACE    TO Work-Text
                       MOVE ZERO     TO OI
                   END-IF
                   END-IF
               ELSE
               IF ( In-Name = "Y"
                 OR In-Rule = "Y"
                  )
                   ADD 1             TO OI
                   MOVE C            TO Work-Text(OI:1)
               ELSE
                   MOVE "Y"          TO In-Rule
                   MOVE I            TO Work-Col
                   ADD 1             TO OI
                   MOVE C            TO Work-Text(OI:1)
                   IF ( Text-Len = ZERO )
                       SUBTRACT 2 FROM I GIVING Text-Len
                   END-IF
               END-IF
               END-IF
               ADD 1                 TO I
           END-PERFORM
           .

       Process-Decision.

           IF ( Source-Body(2:9) = "END-TABLE" )
               PERFORM Write-Source-Copy
               PERFORM Create-Table-Source
               MOVE SPACE          TO In-Decision
               MOVE SPACE          TO In-Conditions
               MOVE SPACE          TO In-Actions
           ELSE
           IF ( Source-Body(2:6) = "------" )
               PERFORM Write-Source-Copy
               MOVE SPACE          TO In-Conditions
               MOVE "Y"            TO In-Actions
           ELSE
           IF ( Source-Flag NOT = "*" )

               MOVE ZERO           TO I
               INSPECT Source-Body
                   TALLYING I FOR LEADING SPACES
               ADD 6               TO I
               MOVE ZERO           TO OI
               MOVE SPACES         TO Copy-Name
               PERFORM
                   UNTIL I > 80

                   MOVE Source-Body(I:1) TO C
                   IF NOT ( C = SPACE OR QUOTE OR "." )
                       ADD 1       TO OI
                       MOVE C      TO Copy-Name(OI:1)
                   END-IF
                   ADD 1           TO I
               END-PERFORM
               PERFORM Create-Table-Start

           ELSE
           IF ( In-Conditions = "Y" )
               PERFORM Write-Source-Copy
               ADD 1               TO DT-CLimit
               MOVE Source-Body(2:Text-Len) TO DT-Condition(DT-CLimit)
               PERFORM
                   VARYING DT-RIndex FROM 1 BY 1
                     UNTIL DT-RIndex > DT-RLimit

                   MOVE DT-Column(DT-RIndex) TO I
                   MOVE Source-Body(I:2)
                               TO DT-Rule-Entry(DT-CLimit DT-RIndex)
               END-PERFORM
           ELSE
           IF ( In-Actions = "Y" )
               PERFORM Write-Source-Copy
               ADD 1               TO DT-SLimit
               MOVE Source-Body(2:Text-Len) TO DT-Source(DT-SLimit)
               PERFORM
                   VARYING DT-RIndex FROM 1 BY 1
                     UNTIL DT-RIndex > DT-RLimit

                   MOVE DT-Column(DT-RIndex) TO I
                   MOVE Source-Body(I:2)
                               TO DT-Action-Entry(DT-SLimit DT-RIndex)
               END-PERFORM

           END-IF
           END-IF
           END-IF
           END-IF
           END-IF
           .

       Create-Table-Start.

           DISPLAY "Writing File: " Copy-Name
           OPEN OUTPUT Copy-File

           MOVE SPACES             TO Copy-Line
           MOVE "*"                TO Copy-Line(7:1)
           MOVE "File-Name:"       TO Copy-Line(12:)
           MOVE Copy-Name          TO Copy-Line(30:)
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           MOVE "*"                TO Copy-Line(7:1)
           MOVE "Decision Table:"  TO Copy-Line(12:)
           MOVE DT-Name            TO Copy-Line(30:)
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           MOVE "*"                TO Copy-Line(7:1)
           MOVE "Generated by:"    TO Copy-Line(12:)
           MOVE "dtprocess"        TO Copy-Line(30:)
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           WRITE Copy-Line

           MOVE Header-Hold        TO Copy-Line
           WRITE Copy-Line
           .

       Write-Source-Copy.

           MOVE Source-Line        TO Copy-Line
           WRITE Copy-Line
           .

       Create-Table-Source.

           MOVE SPACES             TO Copy-Line
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           MOVE "EVALUATE"         TO Copy-Line(12:)
           PERFORM
               VARYING DT-CIndex FROM 1 BY 1
                 UNTIL DT-CIndex > DT-CLimit

               MOVE DT-Condition(DT-CIndex) TO Work-Text
               DISPLAY Work-Text(1:32)

               MOVE DT-Condition(DT-CIndex) TO Copy-Line(21:)
               WRITE Copy-Line
               MOVE "    ALSO"         TO Copy-Line(12:)
           END-PERFORM

           PERFORM
               VARYING DT-RIndex FROM 1 BY 1
                 UNTIL DT-RIndex > DT-RLimit

               MOVE SPACES             TO Copy-Line
               MOVE "*"                TO Copy-Line(7:1)
               MOVE "rule"             TO Copy-Line(12:)
               MOVE DT-Rule(DT-RIndex) TO Copy-Line(17:)
               WRITE Copy-Line

               MOVE SPACES             TO Copy-Line
               MOVE "WHEN"             TO Copy-Line(12:)

               IF ( DT-Rule(DT-Rindex) = "E" )
                   MOVE "OTHER"        TO Copy-Line(21:)
                   WRITE Copy-Line
               ELSE
                   PERFORM
                       VARYING DT-CIndex FROM 1 BY 1
                         UNTIL DT-CIndex > DT-CLimit

                       IF ( DT-Rule-Entry(DT-CIndex DT-RIndex)
                               = "Y" OR " Y" OR "y" OR " y" )
                           MOVE "TRUE"     TO Copy-Line(21:)
                       ELSE
                       IF ( DT-Rule-Entry(DT-CIndex DT-RIndex)
                               = "N" OR " N" OR "n" OR " n" )
                           MOVE "FALSE"    TO Copy-Line(21:)
                       ELSE
                           MOVE "ANY"      TO Copy-Line(21:)
                       END-IF
                       END-IF
                       WRITE Copy-Line
                       MOVE "    ALSO"     TO Copy-Line(12:)
                   END-PERFORM
               END-IF

               MOVE SPACES                 TO Copy-Line
               MOVE SPACE                  TO Action-OK
               PERFORM
                   VARYING DT-SIndex FROM 1 BY 1
                     UNTIL DT-SIndex > DT-SLimit

                   IF ( DT-Action-Entry(DT-SIndex DT-RIndex)
                            = "*" OR " *" )
                       MOVE DT-Source(DT-SIndex) TO Copy-Line(20:)
                       WRITE Copy-Line
                       MOVE "Y"            TO Action-OK
                   END-IF
               END-PERFORM
               IF ( Action-OK NOT = "Y" )
                   MOVE "CONTINUE"     TO Copy-Line(20:)
                   WRITE Copy-Line
               END-IF
           END-PERFORM

           MOVE SPACES             TO Copy-Line
           MOVE "END-EVALUATE"     TO Copy-Line(12:)
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           MOVE "."                TO Copy-Line(12:)
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           WRITE Copy-Line

           MOVE SPACES             TO Copy-Line
           MOVE "*"                TO Copy-Line(7:1)
           MOVE "End of File:"     TO Copy-Line(12:)
           MOVE Copy-Name          TO Copy-Line(30:)
           WRITE Copy-Line

           CLOSE Copy-File
           .

       END PROGRAM dtprocess.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-23T12:17:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127503035.875866.107300@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1127466168.315083.151580@z14g2000cwz.googlegroups.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com> <1127466168.315083.151580@z14g2000cwz.googlegroups.com>`

```
> dtprocess

What the program does not do, and would be very useful if it did, is
analyse the rules. It should check for duplicates, for masked out
unreachable rules, and preferably ensure completeness with every
possible combination given in a rule (ie with the else rule redundant).

Ideas on how that might be done would be useful. 2 ** 50 is a big
number.

The program could also check for duplicate adjacent action blocks and
merge them. Another enhancement would be to cater for the action flags
specifying the order. Instead of simple '*' indicating an action to be
done the column could be given as numbers that will be used to sort the
actions for this rule.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 6)_

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2005-09-24T16:40:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dh4gvj01vn0@enews4.newsguy.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com> <1127466168.315083.151580@z14g2000cwz.googlegroups.com> <1127503035.875866.107300@o13g2000cwo.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:1127503035.875866.107300@o13g2000cwo.googlegroups.com...
> > dtprocess
>
…[5 more quoted lines elided]…
> number.

One can often write a straightforward code generator to generating
working code from correct input for a specification language
with the simplicity of a finite statemachine.

It gets a lot harder if the tool has to diagnose syntax and as many semantic
errors as possible, if the input language is sophisticated (imagine
what happens if you allow decision tables inside decision tables
as a an example) or the result must be reasonably optimized.

In this case, one needs a compiler-like infrastructure,
to ensure strong parsing (thus good syntax error checking),
strong semantic analysis, and optimization technology
like compilers have.  COBOL isn't particularly suited
for this.

The DMS Software Reengineering Toolkit is.
See http://www.semanticdesigns.com/Products/DMS/DMSToolkit.html

The way we would solve this problem is to define a decision
table language (we have a nested finite-state automata
language which is a superset), and define analysis
and "source-to-source" transformation rules that map
the input language to the output language.  These
 rules essentially are "algebra for programs", and
say essenttialy "if you see this code fragment
(in some langauge), it is the same as that code fragment
in (the same or another) langauge".  In this
case the languages would be DecisionTables
and COBOL respectively.
You can see what transformation rules look like at
www.semdesigns.com/Products/DMS/ProgramTransformation.html.

With such machinery, checking for duplicates can be
reliably accomplished; a BIG engine for finding
duplicate code is discussed at our web site under the
name "clone detection", but it contains exactly the
duplicate checking logic needed for this task.
In effect, it compares compiler-like data structures
representing the code fragments to see if they
are identical or similar (e.g., it doesn't compare
text strings).

Completeness checking (I assume you mean by this
that every input combination is covered) can
be handled by forming a boolen algebra expression
for each table row, and taking the disjunction of
all table rows as a symbolic booelan formula.
If that disjunctive formulat can be simplified to
"true" by applying boolean logic rules, then
all input cases are covered; if not, the complement
of the simplifed formula is a case not handled.
Such logic rules can be code directly as
transformations, and we do this pretty often with
DMS because lots of people want to work with and simplify
boolean formulas.

You'd probably also want to check for subsumption:
does one condition imply another?  If so, there are
circumstances when both trigger, and the actions
might be inconsistent.  If the actions aren't inconsistent,
then the subsumed one is redundant.

> The program could also check for duplicate adjacent action blocks and
> merge them.

That's clone detection again.

> Another enhancement would be to cater for the action flags
> specifying the order. Instead of simple '*' indicating an action to be
> done the column could be given as numbers that will be used to sort the
> actions for this rule.

When you add ordering to the rules, the checking
gets more complex.  Just means you need the supporting
machinery even more :-}

I'm not suggesting everybody run out and buy DMS;
just letting people know that there are sophisticated
engines to enable custom, high-quality code generation
with good checking capabilities.
If your organization does a lot of this kind of thing,
well, DMS might be worth considering.

If your present table generator works, that should
be OK for the moment.

It might amuse folks to know that DMS contains a
number of little languages of its own (syntax, transformation
rules, ...) which are generators, and that we use DMS to generate
and enhance itself,  and that it is about a 5 million line
system at this point.  DMS wouldn't be possible without
itself :-}
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-24T15:27:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127600852.567111.18560@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<dh4gvj01vn0@enews4.newsguy.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com> <1127466168.315083.151580@z14g2000cwz.googlegroups.com> <1127503035.875866.107300@o13g2000cwo.googlegroups.com> <dh4gvj01vn0@enews4.newsguy.com>`

```
> (imagine what happens if you allow decision tables inside
> decision tables as a an example)

That is unlikely as it is only necessary to PERFORM another.

> When you add ordering to the rules,

The rules are not to be reordered, evaluation must be done in the order
presented. The ordering was potentially of the actions:

   *> PERFORM Allow-Entry            1  2
   *> PERFORM Require-Payment   2  1

> With such machinery, checking for duplicates can be
> reliably accomplished;

The problem is identifying that these are the same:

    *> condition 1        Y Y
    *> condition 2        -  Y
    *> condition 3        N -

The number of possible combinations is 2 ** no-of-conditions. Each rule
will cover 2 ** number-of '-'.

One simple way to test for masking and completeness is to set up a
table of flags of size 2**conditions. Each rule would then calculate
the postions in the table that caters for and would check and set the
flags.  This may be OK for numbers up to 20 or 25, which may be a
realistic limit in any case.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-23T02:06:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127466367.732262.237420@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1126984717.455391.125640@f14g2000cwb.googlegroups.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com> <1126984717.455391.125640@f14g2000cwb.googlegroups.com>`

```
> I don't know of any DT preprocessors that are available today.

Test program for dtprocess:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.     dttest.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  Example-Sex                 PIC X.
           88  Example-Male            VALUE "M".
           88  Example-Female          VALUE "F".
           88  Example-Unsexed         VALUE x"00" THRU "E"
                                               "G" THRU "L"
                                               "N" THRU x"FF".
       01  Example-Age                 PIC 999.
       01  Example-Funds               PIC S9(8)V99.

       PROCEDURE DIVISION.
       Decision-Test.

           DISPLAY "Female 15 0.00"
           MOVE "F"        TO Example-Sex
           MOVE 15         TO Example-Age
           MOVE ZERO       TO Example-Funds
           PERFORM Example-DT

           DISPLAY "Female 17 0.00"
           MOVE "F"        TO Example-Sex
           MOVE 17         TO Example-Age
           MOVE ZERO       TO Example-Funds
           PERFORM Example-DT

           DISPLAY "Male 19 0.00"
           MOVE "M"        TO Example-Sex
           MOVE 19         TO Example-Age
           MOVE ZERO       TO Example-Funds
           PERFORM Example-DT

           DISPLAY "Male 19 150.00"
           MOVE "M"        TO Example-Sex
           MOVE 19         TO Example-Age
           MOVE 150.00     TO Example-Funds
           PERFORM Example-DT

           DISPLAY "Male 22 0.00"
           MOVE "M"        TO Example-Sex
           MOVE 22         TO Example-Age
           MOVE ZERO       TO Example-Funds
           PERFORM Example-DT

           STOP RUN
           .

       Example-DT.
      *>DECISION-TABLE Test-of-DTProcess 1 2 3 4 E
           COPY "dttest1cob".
      *> Example-Female                  Y N N N -
      *> Example-Age > 21                - N Y Y -
      *> Example-Age > 18                - Y - - -
      *> Example-Age > 16                Y - - - -
      *> Example-Funds > 100.00          - Y Y - -
      *>--------------------------------------------
      *> PERFORM Refuse-Entry                    *
      *> PERFORM Allow-Entry             * * * *
      *> PERFORM Ask-Identity              * *
      *> PERFORM Require-Payment           * *
      *>END-TABLE Test-of-DTProcess

       Refuse-Entry.
           DISPLAY "refused"
           .
       Allow-Entry.
           DISPLAY "allowed"
           .
       Ask-Identity.
           DISPLAY "identity required"
           .
       Require-Payment.
           DISPLAY "payment required"
           .

       Second-DT.
      *>DECISION-TABLE Second-Test       1 2 3 4 E
           COPY "dttest2cob".
      *> Example-Female                  Y Y N N -
      *> Example-Funds > 100.00          Y N Y N -
      *>--------------------------------------------
      *> PERFORM Refuse-Entry                  *
      *> PERFORM Allow-Entry             * * *
      *>END-TABLE Second-Test
       END PROGRAM dttest.
```

###### ↳ ↳ ↳ Re: Modernization of COBOL Applications

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-09-20T08:57:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-CAFC26.08574220092005@ispnews.usenetserver.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com> <dg9b7i$e0l$1@reader1.panix.com> <7Nednex7Qcm5trHeRVn-2w@adelphia.com>`

```
In article <7Nednex7Qcm5trHeRVn-2w@adelphia.com>,
 John Culleton <john@wexfordpress.com> wrote:

> Let me throw in a few unpopular ideas.
> 1. The Murach/Noll combine in one of their books ( I forget which)
…[6 more quoted lines elided]…
> be portable. 

I'm not conversant with that text, but any opinion of CICS based on 
decades old issues is going to miss many great features introduced in 
the past two decades.  IBM has introduced numerous features in the last 
two decades that make CICS a great platform for supporting any 
application.

I'm not sure what 'it isn't COBOL' means -- CICS has fully supported 
Cobol for a very long time.  It certainly can be Cobol.  Especially if 
one has no attached terminal to muck things up, it can be pure Cobol.


> 2. The EVALUATE verb is only slightly less obnoxious than its immediate
> parent, the extraordinarily convoluted nested IF. I use neither. For one
…[6 more quoted lines elided]…
> code clear off the page, all in the name of readability. Nonsense.

There is a Cobol principle that requires all actions be terminated by a 
period?  Isn't that what explicit scope terminators were supposed to fix 
when they were introduced several decades ago.

And those professor types that would have you 'indent the code clear off 
the page' have a sound scientific basis for doing so.  Studies have 
shown very clearly that indentation to match logic improves reader 
comprehension.

The optimum was 2 to 4 bytes indentation, with 6 to 8 offering no 
benefit.  The 'block' style offering a negative effect on comprehension.  
Some will try and claim that it is "what you are used to", but it isn't.  
It is just a function of the human brain and visual recognition tend to 
work.

In a slightly related note:
There is a cute email chain letter circulating that claims to be from 
the Yale Psychology Department -- it has no vowels and some other 
letters have been removed from the interior of the words, yet it is 
surprisingly readable.  If I can find it I'll post it.  It gives some 
interesting insight into how the mind 'reads'.
```

#### ↳ Re: Modernization of COBOL Applications

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-14T20:03:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jm%Ve.10669$vo5.6756@fe01.news.easynews.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>`

```
I have ZERO "real-world" experience doing this, but I do follow a number of 
vendors who provide solutions/products targeted at this.  A couple things you 
might want to look at (even if it is just for ideas) are:

WebSphere Developer for zSeries at:
 http://www-306.ibm.com/software/awdtools/devzseries/

   or

Micro Focus Express Enterprise Edition "Component Generator", see:
  http://supportline.microfocus.com//documentation/books/mx30/mx30indx.htm

and look for the "Component Generator" documentation.
```

#### ↳ Re: Modernization of COBOL Applications

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-09-14T22:33:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-727F24.22334014092005@ispnews.usenetserver.com>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>`

```
In article <sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>,
 "jce" <defaultuser@hotmail.com> wrote:

> I've been thinking about the modernization of COBOL applications running on 
> a mainframe environment so I decided to work on a rambling set of questions.
…[8 more quoted lines elided]…
> tooling/design patterns.

I think the easiest way to accomplish this is to expose your current 
functions as web services.

Is this a 3270 green screen only?  Or can clients access the app via 
tcp/ip, appc, mqseries, etc? 

There are products that will do transparent conversion of green screens 
into web services.  GT-Software comes to mind.  So does something called 
"ScreenSurfer", but I can't remember who makes that.


> For the existing case. If you can imagine - we have a module that updates a 
> customer from some green screen.  I would want to enable the update function 
> as a callable service.  All authorization and authentication issues aside - 
> the desire would be to have a module that can be called by "either" the CICS 
> transaction or via, say, a SOAP service request.

If your apps are set up with business modules that can be invoked to 
perform their function without the screens.  IBM has a SOAP for CICS 
example out there.  I haven't used it and can't speak about it.


> Would it seem more appropriate that the a new calling module be "non CICS" 
> and call the CICS module...and leaving the CICS green screen transactions as 
…[3 more quoted lines elided]…
> while ;-) *

CICS is going to help you load-balance, scale and ease your networking 
code.  And you can call non-CICS programs all you want -- it is actually 
quite a bit faster than a LINK or XCTL.

Why would you want to rewrite all of that...


> I think ultimately, I'd be really interested in something that was like the 
> http://www.droplets.com/ which seems to be a pretty neat deployment method 
> for mainframe activity :-)

Interesting...
```

#### ↳ Re: Modernization of COBOL Applications

- **From:** "Larry Kahm" <lkahm@nospam_heliotropicsystems.com>
- **Date:** 2005-09-16T16:53:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QLCWe.21$iv5.0@trndny03>`
- **References:** `<sLPVe.68865$p_1.47526@tornado.tampabay.rr.com>`

```
Interesting discourse you've got started here.

While having breakfast this morning, I read about a product called 
BluePhoenix (www.bphx.com).  Not only does it work with COBOL, but it works 
several other "legacy" languages and processes as well.

Should an application live on the mainframe, or should it be distributed? 
Hmmm.  I'd rather see it on a z/OS platform - even if the box is partitioned 
out to Linux.  I have witnessed too many server farms grow as an 
applications group's reach has exceed it's grasp [ Oh yes, of >course< we 
need a new stand-alone QA environment - and the 16 boxes to support it.... ]

Larry Kahm
Heliotropic Systems, Inc.

"jce" <defaultuser@hotmail.com> wrote in message 
news:sLPVe.68865$p_1.47526@tornado.tampabay.rr.com...
>
> I've been thinking about the modernization of COBOL applications running 
…[90 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
