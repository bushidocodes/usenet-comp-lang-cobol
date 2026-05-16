[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXIT SECTION/PARAGRAPH

_51 messages · 10 participants · 2007-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### EXIT SECTION/PARAGRAPH

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-07T16:31:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbrnco$hhi$03$1@news.t-online.com>`

```
Does the per subject terminate current execution
of this module (possibly the runtime executable)
when
a) No section is there , (with EXIT PARAGRAPH)
b) SECTION is there but no paragraph.

Roger
```

#### ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-07T12:59:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13e312ci1s7ur41@corp.supernews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:fbrnco$hhi$03$1@news.t-online.com...
> Does the per subject terminate current execution
> of this module (possibly the runtime executable)
> when
> a) No section is there , (with EXIT PARAGRAPH)
> b) SECTION is there but no paragraph.

EXIT SECTION without a section is a syntax error,
as required by 2002, EXIT statement SR(11).

EXIT PARAGRAPH in an unnamed paragraph
transfers control to the end of the paragraph, as
required by 2002, EXIT statement GR(11).

Note that, if declaratives are used and there is only
one section for the body of the procedure division,
EXIT SECTION will transfer control to the end of
that section as required by 2002, EXIT statement
GR(12). This will, in effect, transfer control to the
explicit GOBACK statement that occurs at the end
of the source element, as described in 2002, 14.5.3,
last paragraph.
```

##### ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-07T13:30:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13e32rs3666u84a@corp.supernews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:13e312ci1s7ur41@corp.supernews.com...
[snip]
> This will, in effect, transfer control to the
> explicit GOBACK statement [...]

I should have written "... implicit GOBACK satement ...".
```

##### ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-07T22:45:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com>`

```
On Fri, 7 Sep 2007 12:59:30 -0400, "Rick Smith" <ricksmith@mfi.net> wrote:

>Note that, if declaratives are used and there is only
>one section for the body of the procedure division,
…[5 more quoted lines elided]…
>last paragraph.

Old School Cobol programmers have an almost genetic belief that the last line of a program
must be its exit. I've seen this structure thousands of times:

procedure division.
main-line.        *> non-functional paragraph name
    perform beginning-of-program
    perform middle-of-program
    perform end-of-program.
....
end-of-program.
    goback.        
*  --- last line in source code ---

Why don't they say GO TO end-of-program, or just say goback in main-line?

Why don't they understand that temporal cohesion is a poor way to structure a program?
Cohesion is supposed to be functional.

Now that goback at the end is in the Standard, their instictive belief has been
vindicated. They'll cite it as proof they were Right all along.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-08T07:10:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HVrEi.133327$VU2.71937@fe02.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com>`

```
Interesting.  I have NEVER seen that structure.  I almost always see either a 
"perform 999-End-Of-Program" -  that never comes back - but includes closes and 
GOBACK, etc.
Or I see the GOBACK at the end of the mainline.

FYI,
   You might want to look at the section "5.1.1.8 Implicit EXIT PROGRAM" in the 
COBOL Migration Guide at:
    http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg32/5.1.1.8

The "user expecting an ABEND if you "fall off" the end of the source code" is 
the problem that I have heard of with OLD IBM mainframe code.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T06:17:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com>`

```
On Sat, 08 Sep 2007 07:10:31 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Interesting.  I have NEVER seen that structure.  I almost always see either a 
>"perform 999-End-Of-Program" -  that never comes back - but includes closes and 
>GOBACK, etc.

Same as my example. I omitted closes to illustrate the point.

>Or I see the GOBACK at the end of the mainline.

That's where it belongs. Entry was at main-line, so exit should be at the same level.

The fundamental problem is PERFORM, a degraded form of CALL. If paragraphs had been
CALLed, they would have received as much respect as programs. Moreover, we could have
passed parameters to them. Instead of being forced to write:

move x to foo-input
perform foo
move foo-output to y

We should have written

call foo using x, y

>FYI,
>   You might want to look at the section "5.1.1.8 Implicit EXIT PROGRAM" in the 
…[4 more quoted lines elided]…
>the problem that I have heard of with OLD IBM mainframe code.

In the days of GO TO spaghetti, there was a real danger of going into free fall. To guard
against that, large programs had safety nets -- paragraphs that would abend because they
should never have been fallen into.  

foo-exit.
    exit.

foo-exit-safety-net.
    display 'Control fell out of foo '
    call 'abend'.

Why did we ever have GO TO? It derived from assembly language. Hardware engineers had an
unseen role in the design of Cobol. It took more than a decade to figure out that GO TO
was a bad idea. Thirty years later, we still don't undrstand why the more subtle PERFORM,
derived from Basic GOSUB, is a bad idea. It's a bad idea for the same reason slavery was
bad: we don't need second class entities. The system works better when all logic entities
have the same structure and standing.


>-- 
>Bill Klein
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-09T01:57:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kfo1qF3fohvU1@mid.individual.net>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com...
> On Sat, 08 Sep 2007 07:10:31 GMT, "William M. Klein" 
> <wmklein@nospam.netcom.com> wrote:
…[62 more quoted lines elided]…
> have the same structure and standing.

That's an interesting opinion and very well stated.

I thought about it and I can't agree. :-)

I  don't see PERFORM as a second class citizen at all, and have been very 
glad to use it in COBOL programs over decades.

I can't see...
                CALL foo
                           USING parm1 parm2 parm3
                                     ON EXCEPTION
                                             CALL something-else
                 VARYING parm1
                       FROM  1
                            BY   1
                       UNTIL   parm1 > 1000
                                 AFTER  parm2
                                 FROM  1
                                       BY  1
                                  UNTIL  parm2 > 1000
                                               AFTER  parm3
                                               FROM  1
                                                      BY 1
                                                UNTIL  parm3 > 1000
                   END-CALL

 ...as having quite the same elegance.

I believe there is a place for calling something external, and there is a 
place for using something internal and the two are of equal Class and 
standing.

Of course, people who are persuaded by your argument are not REQUIRED to use 
PERFORM.

(COBOL is very democratic that way... :-))

Pete.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T12:00:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <5kfo1qF3fohvU1@mid.individual.net>`

```
On Sun, 9 Sep 2007 01:57:11 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[98 more quoted lines elided]…
>standing.

There is a place for loop control and there is a place for call. Assigning both roles to
the verb PERFORM is equivocal. 

Loop control should enclose the code being looped. It doesn't belong on the invoking call.
Someone reading the paragraph has no clue it's inside a loop.

    set address of foo-variable-1 to address of parm1
    set address of foo-variable-2 to address of parm2
    set address of foo-variable-3 to address of parm3
    perfxorm foo

foo. 
    PERFORM VARYING foo-variable-1 FROM 1 BY 1 UNTIL foo-variable-1 > 1000
         .... 
    END-PERFORM.

>Of course, people who are persuaded by your argument are not REQUIRED to use 
>PERFORM.
>
>(COBOL is very democratic that way... :-))

CALL 'foo' USING parm1 parm2 parm3

ENTRY 'foo' USING foo-variable-1 foo-variable-2 foo-variable-3
    PERFORM VARYING foo-variable-1 FROM 1 BY 1 UNTIL foo-variable-1 > 1000
         .... 
    END-PERFORM
    GOBACK.    

Don't like either? Write foo as a called program.

Whatever you do, do *not* use EXTERNAL or GLOBAL.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-09T12:32:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kgt8cF3ie8vU1@mid.individual.net>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <5kfo1qF3fohvU1@mid.individual.net> <64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com...
> On Sun, 9 Sep 2007 01:57:11 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[144 more quoted lines elided]…
>

The above demonstrates the flexibility of COBOL :-)

> Whatever you do, do *not* use EXTERNAL or GLOBAL.
>

There are occasions when it makes a lot of sense to use EXTERNAL and GLOBAL. 
Nested progams are a case in point.

Furthermore Fujitsu PowerCOBOL (a very useful quick build GUI with all event 
processing written in COBOL) REQUIRES the use of EXTERNAL GLOBAL for data to 
be shared across forms.

Be careful with sweeping statements based on opinion, even when it is 
informed opinion, Robert :-)

Pete.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-09T16:11:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189379509.966237.315940@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <5kfo1qF3fohvU1@mid.individual.net> <64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com>`

```
On Sep 9, 5:00 am, Robert <n...@e.mail> wrote:

> Whatever you do, do *not* use EXTERNAL or GLOBAL.

You seem unaware of how the object model is implemented in Cobol.
Perhaps you are stuck in an obsolete pre-OO mindset.

OO Cobol is an expansion of the nested program model. The class is a
separate module with object data being 'GLOBAL' to the methods that
are 'sub-programs' within the module.

Claiming that GLOBAL should not be used is contrary to the ability to
create an 'object' with 'methods' using the nested program structure
available for a couple of decades.

But then you have never let facts get in the way of your opinionated
rants.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T00:31:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iek9e3t4a4fa3nb0t418v688j0hqv3a0ig@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <5kfo1qF3fohvU1@mid.individual.net> <64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com> <1189379509.966237.315940@y42g2000hsy.googlegroups.com>`

```
On Sun, 09 Sep 2007 16:11:49 -0700, Richard <riplin@Azonic.co.nz> wrote:

>On Sep 9, 5:00 am, Robert <n...@e.mail> wrote:
>
…[11 more quoted lines elided]…
>available for a couple of decades.

That's what the object-storage section is for. It is global to either class or instance
methods without using the word GLOBAL.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-09T23:27:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189405678.357264.310110@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<iek9e3t4a4fa3nb0t418v688j0hqv3a0ig@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <5kfo1qF3fohvU1@mid.individual.net> <64j5e35naar2qs3kqhirlih79e3l1vm2eg@4ax.com> <1189379509.966237.315940@y42g2000hsy.googlegroups.com> <iek9e3t4a4fa3nb0t418v688j0hqv3a0ig@4ax.com>`

```
On Sep 10, 5:31 pm, Robert <n...@e.mail> wrote:
> On Sun, 09 Sep 2007 16:11:49 -0700, Richard <rip...@Azonic.co.nz> wrote:
> >On Sep 9, 5:00 am, Robert <n...@e.mail> wrote:
…[15 more quoted lines elided]…
> methods without using the word GLOBAL.

So ? Using ANSI'85 nested programs over the last 20 years to emulate
OO just means that one has to use GLOBAL for object data rather than
have it implicit with the much later actual OO.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-08T13:57:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbu9p4$nm2$1@reader1.panix.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>`

```
In article <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>The fundamental problem is PERFORM, a degraded form of CALL.

Mr Wagner, it might well be argued that 'PERFORM' is no more 'a degraded 
form of CALL' in the same wise that 'any way to transfer control from the 
currently executing statement' is 'a degraded form of (branch 
instruction)'.

Such arguments may, perhaps, be able to give their originators and/or 
participants a 'such a clever lad I am!' feeling... but be of limited 
application once the client starts paying for time.  Philosophising, for 
some, is an enjoyable thing but, as Wittgenstein said, 'The bridge must 
not fall down'... this has been pointed out in response to your postings 
previously.

>If
>paragraphs had been
>CALLed, they would have received as much respect as programs.

If my Sainted Paternal Grandmother - may she sleep with the angels! - had 
wheels then she'd have been a trolley-car.

She didn't.

DD
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T12:28:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <fbu9p4$nm2$1@reader1.panix.com>`

```
On Sat, 8 Sep 2007 13:57:56 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>,
>Robert  <no@e.mail> wrote:
…[12 more quoted lines elided]…
>application once the client starts paying for time.

The client pays oarsmen to row the boat until higher paid shipbuilders finish its
replacement built with J2EE and Beans.

> Philosophising, for 
>some, is an enjoyable thing but, as Wittgenstein said, 'The bridge must 
>not fall down'...

ï¿½The limits of my language mean the limits of my world.ï¿½

ï¿½If people did not sometimes do silly things, nothing intelligent would ever get done.ï¿½
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-08T21:48:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbv5bj$l5m$1@reader1.panix.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <fbu9p4$nm2$1@reader1.panix.com> <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com>`

```
In article <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 8 Sep 2007 13:57:56 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[18 more quoted lines elided]…
>replacement built with J2EE and Beans.

The client does with its money as it sees fit, Mr Wagner; as long as what 
is requested of me fits into the rate and is neither illegal nor a 
sufficient affront to my professional standards I put in my eight and try 
to come in just slightly under time, under budget and over spec.

>
>> Philosophising, for 
…[3 more quoted lines elided]…
>The limits of my language mean the limits of my world.

This above all, to thine own cells be true. - Gregor Mendel, maybe.

>If people did not sometimes do silly things, nothing intelligent would
>ever get done.

Those who cite the fine line between genius and madness frequently fall 
closer to the latter than the former. - Anonymous

DD
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-09T12:51:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kgudbF3jtu0U1@mid.individual.net>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <fbu9p4$nm2$1@reader1.panix.com> <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com> <fbv5bj$l5m$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fbv5bj$l5m$1@reader1.panix.com...
> In article <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com>,
> Robert  <no@e.mail> wrote:
…[41 more quoted lines elided]…
>
That Algernon Nonymous...pretty safe for him to snipe at people. Sometimes 
he is right on target, though.

I smiled at this last because it caused an image to come to my mind which I 
haven't seen in, oh, fifty years... :-)

A group of schoolboys are being introduced to "Bookkeeping" which they would 
not normally be doing, but their usual teacher is sick. The Bookkeeping 
teacher is a very dour, humourless Scottish gentleman who has a reputation 
for beating boys painfully and unmercifully, and is therefore not to be 
confronted or trifled with.

The teacher, in an attempt to explain double entry bookkeeping, had related 
how, in ancient times people carved one side of a stick to represent money 
coming in and the other side to represent value going out. When the stick 
was symettrical the account had a zero balance.

A grubby 12 year old urchin put his hand up.

"Sir, why didn't they just put stones in a bag to represent money coming in 
and take them out to represent payments? Then, when the bag was empty the 
account would be cleared, and they wouldn't have to lug sticks around with 
them." (The boy had obviously not considered the inconvenience of lugging 
bags of stones around with them...)

There was a silence. The steel blue Scottish eyes bored into the boy...

"Dashwood, there is a fine line between genius and idiocy. You are on that 
line..."

I never asked any more questions in Bookkeeping and our normal teacher 
returned soon after so we didn't have to do it any more and could get back 
to more important things like Science and Literature... :-)

Pete.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T21:01:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k5k6e3l3eeu3olemculjklao692o2hq6rq@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com> <fbu9p4$nm2$1@reader1.panix.com> <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com> <fbv5bj$l5m$1@reader1.panix.com>`

```
On Sat, 8 Sep 2007 21:48:35 +0000 (UTC), docdwarf@panix.com () wrote:


>>The client pays oarsmen to row the boat until higher paid shipbuilders
>>finish its
…[5 more quoted lines elided]…
>to come in just slightly under time, under budget and over spec.

As the boat sinks, I picture you dutifully staying on board playing "PERFORM 9999-EOJ
THRU 9999-EX." I picture a bumper sticker "I'll give up my THRU when they pry my cold
fingers from the keyboard."
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T02:05:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbvkdb$g6q$1@reader1.panix.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <38m5e31437e4ns5h772h3t0lvsqhg2pvkt@4ax.com> <fbv5bj$l5m$1@reader1.panix.com> <k5k6e3l3eeu3olemculjklao692o2hq6rq@4ax.com>`

```
In article <k5k6e3l3eeu3olemculjklao692o2hq6rq@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 8 Sep 2007 21:48:35 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[14 more quoted lines elided]…
>fingers from the keyboard."

That you can picture it, Mr Wagner, gives it no force of existence outside 
of what you can picture; I am nowhere near believing 'it happened 
yesterday, therefore it must happen tomorrow'.

There just might, possibly, be things in Heaven and upon Earth not dreamt 
of in your philosophies.

DD
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-08T16:09:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189292947.713033.16820@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <HVrEi.133327$VU2.71937@fe02.news.easynews.com> <m9s4e31kd9spf9011fb891re7ktpsdt81g@4ax.com>`

```
On Sep 8, 11:17 pm, Robert <n...@e.mail> wrote:

> The fundamental problem is PERFORM, a degraded form of CALL. If paragraphs had been
> CALLed, they would have received as much respect as programs. Moreover, we could have
…[4 more quoted lines elided]…
> move foo-output to y

You are not "forced to write" that at all.

> We should have written
>
> call foo using x, y

And how will a 'paragraph' receive these parameters ? Oh, wait, that
looks just like a nested program now.

> In the days of GO TO spaghetti, there was a real danger of going into free fall. To guard

Only when written by incompetent programmers^H^H^H^H^H^H^Hcoders.

> against that, large programs had safety nets -- paragraphs that would abend because they
> should never have been fallen into.
…[6 more quoted lines elided]…
>     call 'abend'.

> Why did we ever have GO TO? It derived from assembly language. Hardware engineers had an
> unseen role in the design of Cobol. It took more than a decade to figure out that GO TO
> was a bad idea.

GO TO was how programmers designed and implemented programs in the
1950s.

> Thirty years later, we still don't undrstand why the more subtle PERFORM,
> derived from Basic GOSUB, is a bad idea.

COBOL predated BASIC by many years, it doesn't have anything "derived
from Basic".

> It's a bad idea for the same reason slavery was
> bad: we don't need second class entities. The system works better when all logic entities
> have the same structure and standing.

Please give an example of any programming language where "all logic
entities have the same structure and standing". For example where a
class has the same "structure and standing" as a statement.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-08T11:52:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbu2ef$m51$1@reader1.panix.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com>`

```
In article <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 7 Sep 2007 12:59:30 -0400, "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[23 more quoted lines elided]…
>Why don't they say GO TO end-of-program, or just say goback in main-line?

I barely know why *I* say things, Mr Wagner, let alone anyone else... but 
many's the time I've been on a site where the standard was:

PROCEDURE DIVISION.

PERFORM 0000-HOUSKEEPING THRU 0000-EX.
PERFORM 3000-MAIN-LINE   THRU 3000-EX.
PERFORM 9999-EOJ         THRU 9999-EX.
GOBACK.

3000-MAIN-LINE. <== note 'out-of-sequence' numbering.  The reason given 
for this is that Housekeeping is done once and should be 'out of the way' 
(farther down in the source), EOJ is at the end and, likewise, farther 
down... and most problems occur in the mainline, so keep that more 
convenient than the other paragraphs.

>
>Why don't they understand that temporal cohesion is a poor way to
>structure a program?

The way that a program's skeleton was put together, decades on back, just 
might possibly not reflect the current programmers' understandings.

>Cohesion is supposed to be functional.

Mr Wagner, this is not a world where, in my experience, 'supposed to be' 
is actualised often enough that the lack of this occurring is worthy of 
much note... perhaps our experiences are different.

>
>Now that goback at the end is in the Standard, their instictive belief has been
>vindicated. They'll cite it as proof they were Right all along.

As long as the checks clear the bank, Mr Wagner, a Real Programmer might 
not see much more in 'what they cite' than noise.

DD
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T12:44:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com>`

```
On Sat, 8 Sep 2007 11:52:47 +0000 (UTC), docdwarf@panix.com () wrote:


>As long as the checks clear the bank, Mr Wagner, a Real Programmer might 
>not see much more in 'what they cite' than noise.

Checks that no longer clear the bank:

Westinghouse, Enron, AT&T, Gulf Oil, Texaco, Best, Builders Square, Marshall Field's,
Montgomery Ward, FW Woolworth, Zayre, Houston Natural Gas, Sylvania, Lionel, Doubleday,
Winchester, Pullman, Braniff, TWA, Chase Manhattan Bank, Arthur Anderson, EF Hutton, Paine
Webber, American Motors, McDonnell  Douglas, Grumman, Banquet Foods, United Fruit, Amdahl,
Control Data, DEC, Netscape, Prime, Tandem, Compaq, Hayes, Burroughs, Commodore,
AgfaPhoto, IG Farben, Golden Nugget, MGM Grand, Caesars.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-08T18:05:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rvBEi.347002$sR4.53071@fe08.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com>`

```
And which of those companies stopped "clearing their checks" because of the 
placement of GOBACK (or Stop Run) in their COBOL programs????  <G>
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-08T12:41:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B5mdnWhzcsG9cH_bnZ2dnUVZ_jadnZ2d@comcast.com>`
- **In-Reply-To:** `<rvBEi.347002$sR4.53071@fe08.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com> <rvBEi.347002$sR4.53071@fe08.news.easynews.com>`

```
William M. Klein wrote:
> And which of those companies stopped "clearing their checks" because of the 
> placement of GOBACK (or Stop Run) in their COBOL programs????  <G>

Heh....

000-PRINT-CHECKS.
     PERFORM PRINT-ROBERTS-CHECK.
     PERFORM PRINT-PETES-CHECK.
     PERFORM PRINT-DANIELS-CHECK.
     STOP RUN.
     PERFORM PRINT-BILLS-CHECK.

Don't ya hate it when that happens?  ;)
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-09T12:55:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kgul4F3irkgU1@mid.individual.net>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com> <rvBEi.347002$sR4.53071@fe08.news.easynews.com> <B5mdnWhzcsG9cH_bnZ2dnUVZ_jadnZ2d@comcast.com>`

```


"LX-i" <lxi0007@netscape.net> wrote in message 
news:B5mdnWhzcsG9cH_bnZ2dnUVZ_jadnZ2d@comcast.com...
> William M. Klein wrote:
>> And which of those companies stopped "clearing their checks" because of 
…[12 more quoted lines elided]…
>
Lol!

(Thanks for paying me... ;-))

Pete.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 8)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-08T22:37:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qbmdnUCL09545X7bnZ2dnUVZ_tvinZ2d@comcast.com>`
- **In-Reply-To:** `<5kgul4F3irkgU1@mid.individual.net>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com> <rvBEi.347002$sR4.53071@fe08.news.easynews.com> <B5mdnWhzcsG9cH_bnZ2dnUVZ_jadnZ2d@comcast.com> <5kgul4F3irkgU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:B5mdnWhzcsG9cH_bnZ2dnUVZ_jadnZ2d@comcast.com...
…[16 more quoted lines elided]…
> (Thanks for paying me... ;-))

Well, you're check's been printed, but the STOP RUN came in there before 
PERFORM MAIL-THE-CHECKS.  Sorry...  :(

;)
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T19:58:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bf6e3d8m51riv28dg0rdt4ieo5coceslo@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com> <rvBEi.347002$sR4.53071@fe08.news.easynews.com>`

```
On Sat, 08 Sep 2007 18:05:12 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>And which of those companies stopped "clearing their checks" because of the 
>placement of GOBACK (or Stop Run) in their COBOL programs????  <G>

Tech companies with the highest job growth:

Omnivision (camera chips)
Perficient (consulting)
AMD 
Apple
Google
Genentech
Network Appliance
Cognizant (consulting)
Nvida
iMergent (exploitation jobs)
Akami (internet content delivery)
Cybersource (electronic payment processing)
Netflix
Priceline

None of them has an opening for a Cobol programmer.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-08T21:50:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbv5f6$dfj$1@reader1.panix.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com> <fbu2ef$m51$1@reader1.panix.com> <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com>`

```
In article <1in5e35i7lvu73ocsbaqasvp00skl6quun@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 8 Sep 2007 11:52:47 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[15 more quoted lines elided]…
>AgfaPhoto, IG Farben, Golden Nugget, MGM Grand, Caesars.

Companies come and companies go, Mr Wagner... and the checks issued by my 
current client still clear the bank.

DD
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-10T11:12:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1luae31t3jin0nsh96h4urii0qpm955uv5@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <gq54e3tujvakviekt9uklks3hv2vlracur@4ax.com>`

```
On Fri, 07 Sep 2007 22:45:59 -0500, Robert <no@e.mail> wrote:

>Old School Cobol programmers have an almost genetic belief that the last line of a program
>must be its exit. I've seen this structure thousands of times:
…[11 more quoted lines elided]…
>Why don't they say GO TO end-of-program, or just say goback in main-line?

Hmmm, I usually have a 
    perform beginning-of-program
    perform middle-of-program
    perform end-of-program.
    goback.

The end-of-program paragraphs does the closes, database finishes, and
display of counts and such.   Housekeeping.

I like to see the goback in the main computer.   I can see right at
the start that there is no drop through to the main body of code.
```

##### ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T12:04:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com>`

```
On Fri, 7 Sep 2007 12:59:30 -0400, "Rick Smith" <ricksmith@mfi.net> wrote:

>
>"Roger While" <simrw@sim-basis.de> wrote in message
…[12 more quoted lines elided]…
>required by 2002, EXIT statement GR(11).

Micro Focus gives a fatal error:

       procedure division.
           if 1 = 2
               exit paragraph
           end-if 
           goback


     3         exit paragraph
* 161-S**********************
**
**    Can only be used within a Paragraph
cob: error(s) in compilationl
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-10T14:22:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eb33f2np62be7@corp.supernews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com>`

```

"Robert" <no@e.mail> wrote in message
news:96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com...
> On Fri, 7 Sep 2007 12:59:30 -0400, "Rick Smith" <ricksmith@mfi.net> wrote:
[snip]
> >EXIT PARAGRAPH in an unnamed paragraph
> >transfers control to the end of the paragraph, as
…[15 more quoted lines elided]…
> cob: error(s) in compilationl

Does Micro Focus claim the compiler conforms to the
COBOL 2002 standard?

Or, are you assuming that EXIT PARAGRAPH as an
extension to the COBOL 1985 standard has the same
behavior as the COBOL 2002 standard?

Incidently, the relation "1 = 2" is a syntax error in both
the current and previous standards. At least one of the
items must be a variable! [This was discussed a year or
so ago, in conjunction with PERFORM UNTIL 1 = 0.]
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-10T21:15:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc455b$4vp$01$1@news.t-online.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com> <13eb33f2np62be7@corp.supernews.com>`

```
While there is a standard for EXIT PARAGRAPTH,
the standard for EXIT SECTION seems to be lacking.
(Or at least not defined)
a)
No SECTION
No PARAGRAPTH

b)
SECTION
No PARAGRAPTH

c)
PARAGRAPH
No Section

d) No SECTION/PARAGRAPH

Hmm, I know what MF does and of course OC :(current) -)

Roger
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-10T21:35:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc469n$sng$02$1@news.t-online.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com> <13eb33f2np62be7@corp.supernews.com> <fc455b$4vp$01$1@news.t-online.com>`

```
I suppose the question is why is
a SECTION other than a PARAGRAPH here?

(Or not when not definied)

Roger

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:fc455b$4vp$01$1@news.t-online.com...
> While there is a standard for EXIT PARAGRAPTH,
> the standard for EXIT SECTION seems to be lacking.
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-10T22:14:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ebumngtegam3d@corp.supernews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com> <13eb33f2np62be7@corp.supernews.com> <fc455b$4vp$01$1@news.t-online.com> <fc469n$sng$02$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:fc469n$sng$02$1@news.t-online.com...
> I suppose the question is why is
> a SECTION other than a PARAGRAPH here?
…[24 more quoted lines elided]…
> > Hmm, I know what MF does and of course OC :(current) -)

I am not entirely certain what your question is; but
maybe the following programs will help, at least, to
refine the question. Each of these produces the same
results.
-----
       program-id. exit-1.
      * paragraphs only
       data division.
       linkage section.
       1 cmd-code pic x.
       procedure division.
           if cmd-code not = "A"
               exit paragraph
           end-if
           display "cmd-code = A"
           goback.
       1.  if cmd-code not = "B"
               exit paragraph
           end-if
           display "cmd-code = B"
           goback.
       2.  display "unrecognized cmd-code"
           goback.
-----
       program-id. exit-2.
      * sections only
       data division.
       linkage section.
       1 cmd-code pic x.
       procedure division.
       0 section.
           if cmd-code not = "A"
               exit paragraph
           end-if
           display "cmd-code = A"
           goback.
       1 section.
           if cmd-code not = "B"
               exit paragraph
           end-if
           display "cmd-code = B"
           goback.
       2 section.
           display "unrecognized cmd-code"
           goback.
-----
       program-id. exit-3.
      * sections with paragraphs
       data division.
       linkage section.
       1 cmd-code pic x.
       procedure division.
       0 section.
       begin.
           if cmd-code not = "A"
               exit paragraph
           end-if
           display "cmd-code = A"
           goback.
       1 section.
       begin.
           if cmd-code not = "B"
               exit paragraph
           end-if
           display "cmd-code = B"
           goback.
       2 section.
       begin.
           display "unrecognized cmd-code"
           goback.
-----
Each of these was run with Micro Focus COBOL 3.2.24
and I believe are standard conforming programs under 2002.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T21:10:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZoiFi.363641$sR4.181094@fe08.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com> <13eb33f2np62be7@corp.supernews.com>`

```
Interesting ...
   I just checked the MF 5.0 LRM and they mark EXIT FUNCTION/METHOD with an 
ISO2002 bubble (and an MF bubble)

But they only mark EXIT PARAGRAPH/SECTION/CYCLE with MF bubbles.

This means that OFFICIALLY, they only claim it as an extension - not as a part 
of their PARTIAL implementation of the '02 Standard.

My guess (only a guess) is that this is a DOX error and that they really do 
conform (and think they conform) to the '02 Standard for this feature.

Although they do NOT claim full conformance to the entire '02 Standard, their 
LRM does mark those individual features that they claim are implemented in 
accordance to that Standard (that were not in the '85 Standard).  See their 
explanation of the ISO2002 bubble in the NOTATION section.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-10T21:32:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ebs8mof83nl03@corp.supernews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <13e312ci1s7ur41@corp.supernews.com> <96uae3106tktv1aclfgel7fsg6j7lm0nsq@4ax.com> <13eb33f2np62be7@corp.supernews.com> <ZoiFi.363641$sR4.181094@fe08.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:ZoiFi.363641$sR4.181094@fe08.news.easynews.com...
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:13eb33f2np62be7@corp.supernews.com...
…[3 more quoted lines elided]…
> >> On Fri, 7 Sep 2007 12:59:30 -0400, "Rick Smith" <ricksmith@mfi.net>
wrote:
> > [snip]
> >> >EXIT PARAGRAPH in an unnamed paragraph
…[19 more quoted lines elided]…
> > COBOL 2002 standard?
[snip]
> Interesting ...
>    I just checked the MF 5.0 LRM and they mark EXIT FUNCTION/METHOD with
an
> ISO2002 bubble (and an MF bubble)
>
> But they only mark EXIT PARAGRAPH/SECTION/CYCLE with MF bubbles.
>
> This means that OFFICIALLY, they only claim it as an extension - not as a
part
> of their PARTIAL implementation of the '02 Standard.
>
> My guess (only a guess) is that this is a DOX error and that they really
do
> conform (and think they conform) to the '02 Standard for this feature.

Documentation error or not, there is no syntax rule in
2002 regarding EXIT PARAGRAPH; thus a syntax
error would seem to be non-conforming with respect
to the standard. One unanswered question is: What
does the Micro Focus LRM for 5.0 have as syntax
rules for EXIT PARAGRAPH?

If there are syntax rules for EXIT PARAGRAPH,
then Micro Focus has elected, apparently, to not
conform with the standard for that item. If there is no
syntax rule and a syntax error is given, then it would
seem the LRM does not agree with the compiler.

The following program, using Micro Focus COBOL
3.2.24 (Jun 1994), does not produce a syntax error
and runs as I expect it should, given the rules in 2002
as I understand them.
-----
       program-id. exitpara.
       data division.
       working-storage section.
       1 const-1 pic 9 value 1.
       procedure division.
           if const-1 = 1
               exit paragraph
           end-if
           goback.
-----
```

#### ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-07T22:13:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com>`

```
On Fri, 7 Sep 2007 16:31:51 +0200, "Roger While" <simrw@sim-basis.de> wrote:

>Does the per subject terminate current execution
>of this module (possibly the runtime executable)
>when
>a) No section is there , (with EXIT PARAGRAPH)
>b) SECTION is there but no paragraph.

EXIT PERFORM from code that's not under a paragraph header will give a compiler error like
"must appear within a paragraph".

EXIT SECTION from code that's not under a section header will give a compiler error like
"must appear within a section".

If they pass those tests, they go to the end of the paragraph or section, same as if your
code fell to the end. If that means falling off the end of the procedure division, most
compilers generate a GOBACK there, some throw an exception.
```

##### ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-08T16:18:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189293494.659714.317920@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com>`

```
On Sep 8, 3:13 pm, Robert <n...@e.mail> wrote:
> On Fri, 7 Sep 2007 16:31:51 +0200, "Roger While" <si...@sim-basis.de> wrote:
> >Does the per subject terminate current execution
…[5 more quoted lines elided]…
> EXIT PERFORM from code that's not under a paragraph header will give a compiler error like

You obviously meant EXIT PARAGRAPH.

> "must appear within a paragraph".

No. Wrong. There is no code in a Cobol program that is not in a
'paragraph', It may be an implicit unnamed paragraph if the programmer
hasn't written a header.

> EXIT SECTION from code that's not under a section header will give a compiler error like
> "must appear within a section".
…[3 more quoted lines elided]…
> compilers generate a GOBACK there, some throw an exception.

Which ones "throw an exception" ?
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T21:22:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com>`

```
On Sat, 08 Sep 2007 16:18:14 -0700, Richard <riplin@Azonic.co.nz> wrote:

>On Sep 8, 3:13 pm, Robert <n...@e.mail> wrote:
>> On Fri, 7 Sep 2007 16:31:51 +0200, "Roger While" <si...@sim-basis.de> wrote:
…[11 more quoted lines elided]…
>hasn't written a header.

That's what I thought, until I tried it with Micro Focus Server Express 2.2.

>> EXIT SECTION from code that's not under a section header will give a compiler error like
>> "must appear within a section".
…[5 more quoted lines elided]…
>Which ones "throw an exception" ?

Bill says old mainframe compilers, which sounds right to me.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-09T15:27:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189376823.322007.290810@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com>`

```

On Sep 9, 2:22 pm, Robert <n...@e.mail> wrote:
> On Sat, 08 Sep 2007 16:18:14 -0700, Richard <rip...@Azonic.co.nz> wrote:

> >> EXIT PARAGRAPH from code that's not under a paragraph header will give a compiler error like
> >> "must appear within a paragraph".
…[5 more quoted lines elided]…
> That's what I thought, until I tried it with Micro Focus Server Express 2.2.

MF Cobol doesn't give an error because "it's not in a paragraph", if
it does give an error it is for some other reason.

> >> EXIT SECTION from code that's not under a section header will give a compiler error like
> >> "must appear within a section".
…[7 more quoted lines elided]…
> Bill says old mainframe compilers, which sounds right to me.

The standard for Cobol requires that 'falling off the end of the code'
is equivalent to a STOP RUN (or EXIT PROGRAM) and always has done.
Whether Bill actually said that is unsupported hearsay.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T05:55:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z_4Fi.358615$sR4.91761@fe08.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com>`

```
Richard,
   True today - not always true.

See SUBSTANTIVE CHANGE 21 on page XVII-61 of the '85 Standard which starts with,

"EXIT PROGRAM statement (1 IPC). When there is no next executable statement in a 
called program, an implicit EXIT PROGRAM statement is executed."

P.S.  This is why the IBM mainframe compilers have different behavior for their 
'74 vs '85 compiler setting (CMPR2 - causes an ABEND while '85 acts as if EXIT 
PROGRAM were coded).  I did provide the reference in an earlier note and can 
provide it again - if anyone wants it.

P.P.S.  I don't know if Micro Focus emulates this with their OSVS or VSC2(2) 
compiler settings, but it wouldn't surprise me if they did.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-10T00:28:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189409300.085925.239340@r34g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<Z_4Fi.358615$sR4.91761@fe08.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <Z_4Fi.358615$sR4.91761@fe08.news.easynews.com>`

```
On Sep 10, 5:55 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Richard,
>    True today - not always true.
…[8 more quoted lines elided]…
> PROGRAM were coded).

With '74 (and earlier) does 'falling off the end' of an UNcalled
program cause a STOP RUN or an ABEND ?
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T14:07:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nccFi.122047$1J4.66000@fe06.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <Z_4Fi.358615$sR4.91761@fe08.news.easynews.com> <1189409300.085925.239340@r34g2000hsd.googlegroups.com>`

```
It is my MEMORY (without checking it) that even the '85 and '02 Standards do NOT 
define what is "required" to happen when you "fall off the end" of source code 
in the "main" (not called/activated) program.

From looking at:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3MG32/5.1.1.8.3

I think (but haven't tested it) that results are STILL (post-85-standard) 
undefined when there is no STOP RUN (or GOBACK) at the end of source code in the 
main program.  I have NOT checked this in the '85 or '02 Standards, so I could 
be mistaken on this.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-10T10:24:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46E51B6B.6F0F.0085.0@efirstbank.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <Z_4Fi.358615$sR4.91761@fe08.news.easynews.com> <1189409300.085925.239340@r34g2000hsd.googlegroups.com> <nccFi.122047$1J4.66000@fe06.news.easynews.com>`

```
>>> On 9/10/2007 at 8:07 AM, in message
<nccFi.122047$1J4.66000@fe06.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
>"Richard" <riplin@Azonic.co.nz> wrote in message 
>news:1189409300.085925.239340@r34g2000hsd.googlegroups.com...
…[4 more quoted lines elided]…
> It is my MEMORY (without checking it) that even the '85 and '02 Standards

> do NOT 
> define what is "required" to happen when you "fall off the end" of 
…[8 more quoted lines elided]…
> I think (but haven't tested it) that results are STILL (post-85-standard)

> undefined when there is no STOP RUN (or GOBACK) at the end of source 
> code in the 
> main program.  I have NOT checked this in the '85 or '02 Standards, so I 
> could 
> be mistaken on this.

I just happen to still have access to IBM DOS/VS COBOL REL 3.1, which is a
"pre-85 standard" compiler.  I just compiled the following program:

 IDENTIFICATION DIVISION.
 PROGRAM-ID. STOPIT.     
 ENVIRONMENT DIVISION.   
 DATA DIVISION.          
                         
 PROCEDURE DIVISION.     
     DISPLAY 'ONE'.      
                         
 TWO.                    
     DISPLAY 'TWO'.      

It actually issued the following warning:
00010  ILA5029I-W     STOP RUN GENERATED AFTER LAST STATEMENT.

Seems to me it would have been better served to generate a GOBACK instead of
a STOP RUN, though...

Dunno how versions prior to 3.1 function with regard to this.

Frank
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T20:54:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aiFi.398988$rk4.12098@fe09.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <Z_4Fi.358615$sR4.91761@fe08.news.easynews.com> <1189409300.085925.239340@r34g2000hsd.googlegroups.com> <nccFi.122047$1J4.66000@fe06.news.easynews.com> <46E51B6B.6F0F.0085.0@efirstbank.com>`

```
Thanks Franc,
  Now that you mention it, I remember seeing messages like that in CICS programs 
that used EXEC CICS RETURN and didn't have any GOBACK (or STOP RUN).  (Which was 
always scary - as you weren't supposed to use STOP RUN under CICS)
```

###### ↳ ↳ ↳ No paragraphs in "standard" COBOL (was: EXIT SECTION/PARAGRAPH

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T06:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P35Fi.118345$1J4.83829@fe06.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com>`

```
If a compiler claims to conform to the '02 Standard (at least for this) - or has 
such an extension, a "conforming" compiler need not have all procedure division 
code within NAMED paragraphs.

See substantive change 90 on page 828 of the '02 Standard.  It states,

"90) Paragraph-name. A paragraph-name is not required at the beginning of the 
procedure division or a section."

I believe (but won't swear to it), that MF has had this as an extension for many 
releases.

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1189376823.322007.290810@50g2000hsm.googlegroups.com...
>
> On Sep 9, 2:22 pm, Robert <n...@e.mail> wrote:
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: No paragraphs in "standard" COBOL (was: EXIT SECTION/PARAGRAPH

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-10T00:23:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189409036.404027.305410@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<P35Fi.118345$1J4.83829@fe06.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <P35Fi.118345$1J4.83829@fe06.news.easynews.com>`

```
On Sep 10, 6:00 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> If a compiler claims to conform to the '02 Standard (at least for this) - or has
> such an extension, a "conforming" compiler need not have all procedure division
…[8 more quoted lines elided]…
> releases.

EXIT PARAGRAPH is an extension prior to '02.
```

###### ↳ ↳ ↳ Re: No paragraphs in "standard" COBOL (was: EXIT SECTION/PARAGRAPH

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T14:11:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<egcFi.122071$1J4.96566@fe06.news.easynews.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com> <1189376823.322007.290810@50g2000hsm.googlegroups.com> <P35Fi.118345$1J4.83829@fe06.news.easynews.com> <1189409036.404027.305410@y42g2000hsy.googlegroups.com>`

```
Sorry that I wasn't clear.  I am POSITIVE that MF introduced EXIT PARAGRAPH as 
an extension before the '02 Standard was passed.  What I am not as positive of, 
is that I *think* that MF had n extension allowing for procedure division code 
to exist before/without a paragraph (or section) header.

My note was replying to the thread comments,

>> >No. Wrong. There is no code in a Cobol program that is not in a
>> >'paragraph', It may be an implicit unnamed paragraph if the programmer
>> >hasn't written a header.
>>
>> That's what I thought, until I tried it with Micro Focus Server Express 2.2.
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-10T19:33:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc3v5r$nne$01$1@news.t-online.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <1189293494.659714.317920@g4g2000hsf.googlegroups.com> <tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com>`

```
Ia a section implied ?

Roger

"Robert" <no@e.mail> schrieb im Newsbeitrag 
news:tvl6e394ebogoq92r630h15e11fs8ltlb2@4ax.com...
> On Sat, 08 Sep 2007 16:18:14 -0700, Richard <riplin@Azonic.co.nz> wrote:
>
…[32 more quoted lines elided]…
> Bill says old mainframe compilers, which sounds right to me.
```

##### ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-10T11:19:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33vae358s4n9oihtbc01s24hvnp8d7jg63@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com>`

```
On Fri, 07 Sep 2007 22:13:34 -0500, Robert <no@e.mail> wrote:

>EXIT PERFORM from code that's not under a paragraph header will give a compiler error like
>"must appear within a paragraph".

I'm curious.   My compiler gives warning if we have sections without
paragraphs.   I haven't worked at a place where that was a style that
was used.    

Does anybody know why that would be a style of coding these days?
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-10T14:57:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46E55B57.6F0F.0085.0@efirstbank.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <33vae358s4n9oihtbc01s24hvnp8d7jg63@4ax.com>`

```
>>> On 9/10/2007 at 11:19 AM, in message
<33vae358s4n9oihtbc01s24hvnp8d7jg63@4ax.com>, Howard
Brazee<howard@brazee.net> wrote:
> On Fri, 07 Sep 2007 22:13:34 -0500, Robert <no@e.mail> wrote:
> 
…[8 more quoted lines elided]…
> Does anybody know why that would be a style of coding these days?

Do you mean something like this?

 PROCEDURE DIVISION.
 STARTUP SECTION.
     PERFORM HOUSEKEEPING
     PERFORM MAINLINE
     PERFORM CLEANUP
     GOBACK.

 HOUSEKEEPING SECTION.
     OPEN INPUT FILE1
     OPEN OUTPUT FILE2
     .

 MAINLINE SECTION.
     PERFORM FIRST
     PERFORM SECOND
     PERFORM THIRD
     .

 FIRST SECTION.
*    stuff here
     .

 SECOND SECTION.
*    stuff here
     .
 THIRD SECTION.
*    stuff here
     .

 HOUSEKEEPING SECTION.
     CLOSE FILE1
           FILE2
     .

For better of for worse, we have code like this.  Generally I'd say there is
an additional "EXIT" paragraph at the end of each section, though often if
someone ads a section later and there's no "GO TO ...EXIT..." it's often
omitted (intentionally or otherwise!).

There is no shop standard that requires this style of coding, nor is there
one restricting it.

It definitely does not cause the compiler to issue any warnings.

Once again, speaking for myself, I would not use SECTIONs if it were not for
the fact that my compiler does not support EXIT PARAGRAPH.  But because it
does not I have quite a few, mostly older, programs that are coded this
way.

Frank
```

###### ↳ ↳ ↳ Re: EXIT SECTION/PARAGRAPH

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-11T11:41:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pnkde3148acb74fnp1h5bgci7fsirbi4fu@4ax.com>`
- **References:** `<fbrnco$hhi$03$1@news.t-online.com> <me44e3dls6go3dhcgh105kje5l2ql1ajbd@4ax.com> <33vae358s4n9oihtbc01s24hvnp8d7jg63@4ax.com> <46E55B57.6F0F.0085.0@efirstbank.com>`

```
On Mon, 10 Sep 2007 14:57:27 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>Once again, speaking for myself, I would not use SECTIONs if it were not for
>the fact that my compiler does not support EXIT PARAGRAPH.  But because it
>does not I have quite a few, mostly older, programs that are coded this

So there's a compiler that supports EXIT SECTION but not EXIT
PARAGRAPH?

(I understand the GO TO EXIT bit, even if I don't program that way).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
