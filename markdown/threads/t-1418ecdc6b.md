[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Why read CLC?

_115 messages · 16 participants · 2008-06_

---

### Why read CLC?

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-04T06:59:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com>`

```
Yesterday I diagnosed a bug in our (rather large) legacy system. This
bug has been present for, oh, probably 10 years or more. How I was
able to do it is instructive.

The essence of the bug is that an "event writer" subprogram, invoked
by a batch transaction processor program, was generating "default
events" rather than "specific events" based upon transaction content.
That the "default event" is indeed a legitimate event (though
imprecise) is why this bug went so long undetected by the users.

I was focusing on this area due to renewed interest by the Users in
intepreting these events.

Diagnosis of this defect turned out to revolve around the behavior of
INITIALIZE. The original developer had written code to INITIALIZE at
the group level, then assign some specific values to some subordinate
and/or elementary items with specific MOVEs, before invoking the
subprogram with the group level as the parameter.

What was happening was that the subprogram was occasionally "side-
effecting" one of the subordinate level-10 items before returning to
the main program. Every subsequent invocation of the subprogram then
showed the default event generation.

The particular item that was "overwritten" was an "override value",
and the "override" effect was the "default event" generation, rather
than the specific table-lookup event generation.

Having read some of the INITIALIZE threads in CLC, and learning that
therein resided some important details regarding its behavior, I
consulted the IBM reference manual to refresh my memory that
INITIALIZE will not clear FILLERs. Yes, the Level-10 item had
subordinate elementary items that were cleared, but also a FILLER that
was not cleared.  Thus, once side-effected, this Level-10 item caused
override behavior, and default event generation,  to persist,
erroneously, for each subsequent transaction processed.

The fix was straightforward: do a MOVE of spaces into the Level-10
before each invocation of the subprogram (though I suppose I could
achieve the same effect by giving an elementary name to replace
FILLER.)

I understand maybe 50-60% of what is posted here. I'm simply not at
the same level of understanding or experience as some of you, or a lot
of you. But that is not at issue.  I don't need to be as "smart", or
"smarter" than all you CLC'ers. I "need" only to be a "little" smarter
than most of my co-workers, who don't read CLC. :-)

And that you help me to do.

I can't read everything here, but I try to read a lot. The value is
not restricted to learning from responses from my specific questions I
might post. The real value, I think, is what I pick up "along the
way", reading the other threads, even the ones with heated discussions
(maybe especially them.)

It's OK with me to not understand everything all at once, because each
time I understand a little more.

All of this is possibly, even probably, obvious to the more prominent
posters here. But it may not be to the lurkers, or the more timid,
among us.  There is a "social good" which arises out of the
motivations and intensity shown here, whatever their motivations.

I do not take that for granted. Neither should anyone else.

Ken
```

#### ↳ Re: Why read CLC?

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-04T14:39:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g269ei$ho7$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com>`

```
In article <1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:

[snip]

>The fix was straightforward: do a MOVE of spaces into the Level-10
>before each invocation of the subprogram (though I suppose I could
>achieve the same effect by giving an elementary name to replace
>FILLER.)

Rather than addressing individual fields - thereby ignoring what I see as 
the intention of an INITIALIZE - what I'll do is rename the offending 
FILLER to FILLER01 (or something similar) and add a comment... but that's 
just my style, said Casey.

DD
```

##### ↳ ↳ Re: Why read CLC?

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-04T07:59:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com>`

```
On Jun 4, 10:39 am, docdw...@panix.com () wrote:
> In article <1f980664-cc0e-4577-bd77-b0476d9a2...@56g2000hsm.googlegroups.com>,
>
…[14 more quoted lines elided]…
> DD

Hmmmmm... yes, that was my original inclination, too...

BUT - the FILLER, and its superordinate group level, is in a COPYLIB.
And if I change the COPYLIB, I'll have to migrate it (instead of the
caller program), and request recompiles of both the caller and the
called subprogram (just to be "safe").

So the migration complexity measure is -
1. 1st way (with a MOVE) - migrate main program, recompile main
program = complexity of 2 tasks.
vs.
2. 2nd way (relabel FILLER as FILLER-KLUGE) - migrate COPYLIB,
recompile main program, recompile subprogram = complexity of 3 tasks.

This difference is small, but nonzero, in a shop which migrates,
tests, and promotes source and executables cautiously.

Come to think of it, since I don't really care, this is the PERFECT
question to place before He-who-signs-my-timesheet, so that he may
exude management-control, and receive the euphoria which is its
consequence of that decision-making.

Such are the Zen-ways of Managing Your Manager. Or so I would like to
think.

But enough about me. What do YOU think of what _I_ think? :-)

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-04T10:09:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Qey1k.4074$co7.2035@nlpi066.nbdc.sbc.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com>`

```
<klshafer@att.net> wrote in message 
news:519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com...

>Come to think of it, since I don't really care, this is the PERFECT
>question to place before He-who-signs-my-timesheet, so that he may
>exude management-control, and receive the euphoria which is its
>consequence of that decision-making.

>..

>But enough about me. What do YOU think of what _I_ think? :-)

I think your decision to force the manager to earn his paycheck is a good 
one.

MCM
```

###### ↳ ↳ ↳ Re: Why read CLC?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-04T15:25:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Zty1k.386894$qg2.76630@fe08.news.easynews.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com>`

```
Depending on how this field is defined compared to other FILLER fields, you 
might be able to use COPY REPLACING to change the "FILLER" to 
"Used-to-be-Filler"  or some such name. e.g.

Copy WhatEver
   Replacing ==Filler  Pic X(10)== by
                   ==Used-to-be-Filler Pic X(10)==.

or if the only way to "identify" this filler is by the item before it, you can 
have things like:

Copy WhatEver
    Replacing ==05 Item-Before Pic X.
                         05  Filler==
            by    g ==05 Item-Before Pic X.
                          05 Used-to-be-Filler==.

On the other hand, sending  it "up the ladder" may be better anyway.

P.S.  Of course, IBM has accepted (but not implemented) a SHARE requirement to 
add support for the "new" '02 Standard INITIALIZE features which does have an 
option for initializing FILLER (NOT by default), but who  knows WHEN that will 
become available at this shop.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 4)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-04T11:53:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com>`

```
On Jun 4, 11:25 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Depending on how this field is defined compared to other FILLER fields, you
> might be able to use COPY REPLACING to change the "FILLER" to
…[4 more quoted lines elided]…
>                    ==Used-to-be-Filler Pic X(10)==.

Hmmmm.... let me see if I understand this approach. The "view" of the
COPYLIB to the invoking program is thus changed so that the INITIALIZE
will have the effect intended by the original developer, the defect is
therefore fixed, and yet, there is _no_ change to the view of the
COPYLIB seen by the subprogram, thus limiting the "scope of effect" of
this change, and consequently limiting the recompiles and retesting.

Nice. :-)

On the other hand (and doesn't there too often seem to the "the other
hand" :-) ), after having been exposed to maybe 10-20% of the 1.5
million of lines of code in the system, I have yet to encounter my
first "COPY... REPLACING" instance. I don't know if its use would
"violate defacto coding standards", I just don't know if they or the
"culture", are "ready for it."

Sidebar thread: This system will be replaced, but the effort to
replace it will probably be 7-10 years. The management structure is
being reorganized, and there may be a "window of opportunity" for New
Ideas and Practices, even if used only for "incremental enhancements
and routine maintenance".

What are your thoughts specifically, or your thoughts on where to
look, on assessing the "state" of the source code portfolio and the
system, with the objective of introducing some new "practices"?  Yes,
I know I could look at CMM, but I am really driving at "what
(relatively new) features of COBOL to use."

> P.S.  Of course, IBM has accepted (but not implemented) a SHARE requirement to
> add support for the "new" '02 Standard INITIALIZE features which does have an
> option for initializing FILLER (NOT by default), but who  knows WHEN that will
> become available at this shop.
>

Thanks... this is good to know. It also helps "soften the blow" to the
egos of any original developers, when explaining to Managers how this
defect has been present for years, but would not have been a defect at
all under an '02 Compiler (albeit, with non-default compile option.)

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-05T09:25:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com>`

```
klshafer@att.net wrote:
> On Jun 4, 11:25 am, "William M. Klein" <wmkl...@nospam.netcom.com>
> wrote:
…[22 more quoted lines elided]…
> "culture", are "ready for it."

My first attack would be to discover how many other places this copybook is 
used. If this is the only instance, change the copybook.

It may be this error you've found is pervasive throughout the system. It's 
worth checking.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 6)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-05T09:29:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com>`

```
On Jun 5, 10:25 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> My first attack would be to discover how many other places this copybook is
> used. If this is the only instance, change the copybook.
…[3 more quoted lines elided]…
>

OK, I just did that. The system got "lucky", so to speak, as described
below. :-)

Yes, there were a couple of other occurrences of main programs with
that COPYLIB.

However,

a. One main program included it, but never referenced it. The ol'
"don't know if I'm gonna need it, but I'll throw it in anyway", which
I consider generally to be bad style. But it's not "broken" in the
strict sense, so I'm sure the client would see nothing that needs
"fixing".

b. The second program, which not coincidentally is the outbound
interface corresponding to the inbound interface which is the offender
mentioned a couple of posts back, does include the COPYLIB, does
reference it, does the "inadequate" INITIALIZE, calls the subprogram
with the side effects, and yet... it shows the "correct" behavior,
recovering nicely from any occurrences of "default events."

Hmmmm... scratching my head... how can this one be working and the
other not? OH!  I see, it really already DOES an explicit MOVE into
the 4780-OVERRIDE-TITLE element. Ah! So in this program, it is already
explicitly initialized with a MOVE. That's why it works!

But wait a minute. It doesn't MOVE SPACES into it. It does a MOVE WRK-
OVERRIDE-TITLE, from Working Storage, into it. Lo and behold, WRK-
OVERRIDE-TITLE itself is NEVER INITIALIZED (nor is its superordinate
in the group), and is never MOVEd into, and it does not have a VALUE
clause!

Oh, well, a trace shows that indeed 4780-OVERRIDE-TITLE contains
SPACES upon entry to the subprogram, so all is well.

Forgive me, for I imagine others have asked this before, but what is
the compiler default for assigning values to PIC X fields if there is
no VALUE clause? I had always heard "don't count on anything, it will
be random memory values", but maybe compiler behavior has "saved the
day" on this second program.

Once again, because I would be unable to demonstrate "incorrect
behavior" of this second program, I probably wouldn't be able to "fix"
it, because "if it ain't broke...".

Nevertheless, from time to time I am amazed how some systems work in
spite of themselves...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-05T17:31:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g297u5$kjk$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>`

```
In article <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:

[snip]

>Oh, well, a trace shows that indeed 4780-OVERRIDE-TITLE contains
>SPACES upon entry to the subprogram, so all is well.
…[3 more quoted lines elided]…
>no VALUE clause?

I'd imagine that it depends on 'the compiler' and the options used for its 
invocation.

>I had always heard "don't count on anything, it will
>be random memory values", but maybe compiler behavior has "saved the
>day" on this second program.

I also was taught 'don't count on anything' but behavior seems to have 
changed from IKFCBL00 to IGYCRCTL.  For example... if I compile some 
source containing:

PROCEDURE DIVISION USING PARMS.        
MAINLINE.                              
    MOVE LK-PARMS  TO  WK-PARMS.       
    DIVIDE WK-MM BY WK-SS GIVING WK-HH.

... using IKFCBL00 (5740-CB1 RELEASE 2.4, IBM OS/VS COBOL JULY 1, 1982) 
(oh... and the time-date on the listing shows up as '13.09.46  DATE JUN  
5,1908') and the PMAP option the listing shows:

ENTRY      00040C                     START    EQU   *                  
           00040C  58 B0 C 0D0                 L     11,0D0(0,12)       
           000410  58 40 D 004                 L     4,004(0,13)        
           000414  58 40 4 018                 L     4,018(0,4)         
           000418  58 50 4 000                 L     5,000(0,4)         
           00041C  50 50 D 228                 ST    5,228(0,13)        
           000420  58 70 D 228                 L     7,228(0,13)        
MAINLINE                                                                
           000424                     PN=02    EQU   *                  
MOVE       000424  D2 09 6 018 7 002           MVC   018(10,6),002(7)   
DIVIDE     00042A  F2 71 D 208 6 020           PACK  208(8,13),020(2,6) 
           000430  F2 71 D 210 6 01D           PACK  210(8,13),01D(2,6) 
           000436  FD 31 D 214 D 20E           DP    214(4,13),20E(2,13)
           00043C  F8 71 D 210 D 214           ZAP   210(8,13),214(2,13)
           000442  F3 11 6 01A D 216           UNPK  01A(2,6),216(2,13) 
           000448  96 F0 6 01B                 OI    01B(6),X'F0'       

... while compiling the same code with IGYCRCTL (5655-G53 IBM Enterprise 
COBOL for z/OS 3.4.1) and the LIST option gives:

START    EQU   *              
         LR    3,15           
         LA    0,312(0,1)     
         CL    0,12(0,12)     
         BALR  15,0           
         BC    13,12(0,15)    
         L     15,768(0,12)   
         BALR  14,15          
         LR    1,15           
         ST    13,4(0,1)      
         ST    0,76(0,1)      
         MVC   0(4,1),88(3)   
         XC    132(4,1),132(1)
         ST    9,92(0,1)      
         LR    13,1           
         L     12,232(0,9)    

... and a whole bunch more stuff... and then 

*MAINLINE                                           
MOVE                                                
   5820 912C               L     2,300(0,9)         
   5830 9134               L     3,308(0,9)         
   D209 2018 3002          MVC   24(10,2),2(3)      
DIVIDE                                              
   F231 D100 201D          PACK  256(4,13),29(2,2)  
   F211 D108 2020          PACK  264(2,13),32(2,2)  
   FD31 D100 D108          DP    256(4,13),264(2,13)
   F311 201A D100          UNPK  26(2,2),256(2,13)  
   96F0 201B               OI    27(2),X'F0'        

... and it may be that in that 'whole bunch more stuff' are instructions 
to initialise various WORKING-STORAGE fields which were not coded with a 
VALUE.

Likewise, it may not be... or it may be that the next compiler upgrade 
will show different behavior.  An uninitialised value should not be 
trusted.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-05T12:36:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>`

```
On Thu, 5 Jun 2008 09:29:35 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:


>Forgive me, for I imagine others have asked this before, but what is
>the compiler default for assigning values to PIC X fields if there is
>no VALUE clause? I had always heard "don't count on anything, it will
>be random memory values", but maybe compiler behavior has "saved the
>day" on this second program.

Micro Focus initializes all working-storage to spaces. Old IBM compilers used to
initialize it to low-values, and had a compiler option WSCLAER that affected
initialization somehow. Someone discovered that INITIAL had a side-effect of initializing
everything without a VALUE to spaces on IBM.

In my opinion, VALUE is bad style because it implies that a procedure can be executed only
once. While that may be true when the program is written, if someone later changes the
flow to execute it multiple times, he's created a bug that's hard to find. One should get
in the habit of initializing structures at the beginning of a PROCEDURE, not at the
beginning of a program.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 8)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-05T12:24:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com>`

```
On Jun 5, 1:36 pm, Robert <n...@e.mail> wrote:
> One should get
> in the habit of initializing structures at the beginning of a PROCEDURE, not at the
> beginning of a program.

Yes, I consider this approach to be much more in the spirit of Yourdon
and Constantine's quest for "cohesion".

However, it has frequently been violated, as witnessed by the large
number of programs I have seen which have a 1000-INITIALIZE or a 1000-
HOUSEKEEPING paragraph, at or near the very beginning of 0000-MAIN,
wherein all the INITIALIZE, or 88-level SETs, or initial MOVEs are
done, regardless of how much later in the execution they are first
used.

Likewise, I see the approach you advocate as reducing unnecessary
"coupling". If the W-S data structure is initialized, before being
populated, in 2500-LOAD-SOME-REF-TBL, then it is no longer dependent
upon being initialized in 1000-HOUSEKEEPING.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-05T19:12:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com>`

```
On Thu, 5 Jun 2008 12:24:54 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jun 5, 1:36ï¿½pm, Robert <n...@e.mail> wrote:
>> One should get
…[11 more quoted lines elided]…
>used.

Yourdon and Constantine called that temporal cohesion, which is one of the BAD types. 

A procedure, like a story, should have a begining, middle and end. A missing beginning or
end usually means there is a structural error. 

>Likewise, I see the approach you advocate as reducing unnecessary
>"coupling". If the W-S data structure is initialized, before being
>populated, in 2500-LOAD-SOME-REF-TBL, then it is no longer dependent
>upon being initialized in 1000-HOUSEKEEPING.

We found a problem today that's been eluding reproducability for weeks. Our batch update
crashed in production. After it was restarted, it ran past that point without crashing. We
knew which transaction caused it to crash. The transaction ran fine by itself. 

It was crashing five layers deep in called programs, in a data layer written in C, with an
invalid pointer to a data buffer.  The conbination of conditions causing it to call that
data layer were unusual, occurring maybe a few times per month. 

The cause turned out to be a structure that was initialized once, when it was created, not
before each use. On the day of the crash, there were two transactions -- 10,000 and 40,000
-- hitting the bad code. The first one, 10,000, worked correctly because pointers in the
structure were null. The restart skipped 39,900 transactions, so the structure was virgin
on transaction 40,000. Apparently, in ten years of production, the program had never
encountered two such transactions in the same batch. Or maybe it wrote over an unrelated
chunk of memory without crashing. 

-----------------------------------------

Coupling that bugs me most are decisions passed through 'indicators' in memory or
databases. The program wants to say:

    if (condition1) or (condition2)
       action1
   end-if

Instead of saying it that way, it says:

    if (condition1)
       set indicator1 to true
   end-if

Somewhere far away it says:

    if (condition2)
       set indicator2 to true
   end-if

In another program, perhaps later in time, it says:

     if indicator1 or indicator2
       action1
    end-if

When trying to figure out why action1 was taken inappropriately, you have to search the
entire system for code that might have set the indicators incorrectly, then figure out
which of a dozen was the culpret. Of course, the person who wrote it knew right where to
look. 

The reasons bad programmers do it:
#7 Job security.
#6  Hey, it's a state machine.
#5  Avoid passing a new parameter to the function. 
#4  Save a few nanoseconds of cpu time.
#3  Avoid duplicating logic.
#2  It works. We have a deadline to meet.
and the number one reason is <drum roll>
#1 Fear of complexity. I never did understand and, or and not (but don't tell the boss).
      I believe in the KISS principle. 

Ironically, coupling doesn't reduce complexity, it adds complexity and unreliability.
Indicators should cause a red flag to go up.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 10)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-06T13:18:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com>`

```
On Jun 5, 8:12 pm, Robert <n...@e.mail> wrote:
> On Thu, 5 Jun 2008 12:24:54 -0700 (PDT), "klsha...@att.net" <klsha...@att.net> wrote:
> >On Jun 5, 1:36 pm, Robert <n...@e.mail> wrote:
…[29 more quoted lines elided]…
>
<snip>
> Indicators should cause a red flag to go up.

Now that you mention it, I see that it is no coincidence that I see a
_multitude_ of those types of indicators and their use throughout my
"offending" batch program.

Another tidbit I remember from Constantine: "indicators" are the type
of element that he would call "control coupling", because it passes
"control information" which explicitly affects how a downstream
procedure will process. So he called that "control coupling". "Control
coupling" is inherently more insidious than passing "pure data" types
of elements, which he called "data coupling".

Generally, you wish to eliminate control coupling, and minimize data
coupling. I believe I have heard this called elsewhere as "starving
the interface", if I understood it incorrectly.

It has proven a real challenge to understand a 13,000 LOC batch
program written in such a style. Lucky for me I have CLC to
help... :-)

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-07T00:24:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2ckg5$482$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com>`

```
In article <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 5, 8:12�pm, Robert <n...@e.mail> wrote:
>> On Thu, 5 Jun 2008 12:24:54 -0700 (PDT), "klsha...@att.net"
…[41 more quoted lines elided]…
>"offending" batch program.

Now that you're thinking of it... consider a classic batch program's flow, 
still in use in some benighted shops that keep functioning code running 
and don't rewrite without having to justify the budget.

It starts with Housekeeping... open the files, call the date routines, set 
up report headers based on dates and the PARMs passed/read... oh, and 
those report headers are, for a good chunk, VALUE clauses that don't 
change all that much, one decade to the next.  If something goes wrong the 
program ABENDs.

Next comes the Main Line... read a rec, check that the data are valid and 
if the data meet certain conditions, sometimes called the 'edit routines'.  
Flags should get set here and often do... except, of course, when things 
change after the program is old enough to vote and someone says 'there's 
no time/budget/personnel to handle the changes that way... all ya gotta do 
is check over *here* for this new stuff'.

For example... read a rec and check the region number, 000 - 099 = Eastern 
Region, 100 - 199 = Central Region, 200 - 299 = Mountain Region, 300 - 400 
= Western Region.  This works fine for a decade or so... until the 
divisions get divided into Northern and Southern sections (n00 - n49 and 
n50 - n99), each with different tax considerations... and then certain 
sections get divided into divisions, depending on volume... so there's an 
88 for EASTERN-NORTHERN-WEST but no need for a MOUNTAIN-SOUTHERN-EAST 88 
because there isn't enough business being done there.

It might be seen, then, that the program grows as the business grew, in a 
fashion more 'organic' than 'linear'; logic-trees in computer-science 
classes may have lots of straight lines and right angles while oak trees 
and baobabs often have fewer.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-07T18:14:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6aunafF384hkiU1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <g2ckg5$482$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g2ckg5$482$1@reader2.panix.com...
> In article 
> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com>,
…[75 more quoted lines elided]…
> and baobabs often have fewer.

A very nice analogy, Doc.

I don't see a popular movement to replace oaks with poplars any time 
soon...(the fact is that both have their place).

The idea of evolving systems has strong appeal for me and I am finding this 
approach very useful. In effect it is controlling the 'organic' evolution 
that decides the result.

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 13)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-07T14:30:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<upGdnSX9RLRSfNfVnZ2dnUVZ_hOdnZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <g2ckg5$482$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net>`

```
Pete Dashwood wrote:
>>
>> It might be seen, then, that the program grows as the business grew,
…[12 more quoted lines elided]…
>

Another law:

"A complex system that works is invariably found to have evolved from a 
simple system that works.'

Corollary:
"A complex system designed from scratch never works and cannot be patched up 
to make it work. You have to start over, beginning with a working simple 
system."
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 14)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:45:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8970af98-6560-4c78-8060-240eab5dc24c@m73g2000hsh.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <g2ckg5$482$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <upGdnSX9RLRSfNfVnZ2dnUVZ_hOdnZ2d@earthlink.com>`

```
On Jun 7, 3:30 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Pete Dashwood wrote:
>
…[24 more quoted lines elided]…
> - Show quoted text -

I believe it is Time Well Spent to design as well as you can, code as
well as you can, and test/debug as well as you can, those initial
basic building blocks of your system. That way, when you add do it,
you need only look in the incremental additions for the "newly"
discovered bugs.

Does that mean that I agree with you? :-)

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-08T12:34:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2gjl3$6n9$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <g2ckg5$482$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net>`

```
In article <6aunafF384hkiU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:g2ckg5$482$1@reader2.panix.com...

[snip]

>> It might be seen, then, that the program grows as the business grew, in a
>> fashion more 'organic' than 'linear'; logic-trees in computer-science
…[3 more quoted lines elided]…
>A very nice analogy, Doc.

Shucks, t'warn't nothin'.  It figures that something like that would take 
me decades to generate.

>
>I don't see a popular movement to replace oaks with poplars any time 
…[4 more quoted lines elided]…
>that decides the result.

Oh, a Darwinist, eh?  If you choose to extend the metaphor of 'organic 
change', Mr Dashwood, an amusing conclusion might be reached: evolution 
will be reactive, directed by environment, until a person actively invests 
time, effort and experimentation in 'selective breeding' to direct the 
form and function of the species... and even then that will not prevent 
situations changing in unforseen manners that the directed species cannot 
anticipate.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-09T00:51:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b22tnF35niqdU1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <g2ckg5$482$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:g2gjl3$6n9$1@reader2.panix.com...
> In article <6aunafF384hkiU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[32 more quoted lines elided]…
> anticipate.

True. That's why we have GE... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-08T12:55:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2gksl$3t9$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net>`

```
In article <6b22tnF35niqdU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:g2gjl3$6n9$1@reader2.panix.com...
>> In article <6aunafF384hkiU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>>The idea of evolving systems has strong appeal for me and I am finding 
>>>this
…[11 more quoted lines elided]…
>True. That's why we have GE... :-)

Everything is anticipated by General Electric?

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-08T11:38:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TUT2k.163$Jh7.149@newsfe21.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com>`

```
Since Yourdon & Constantine have been invoked in this discussion - I have a
question about a concept that turned up in their publications.  This was
"co-routines" - two or more definable routines (i.e., having a start and a
finish) that continuously swapped control between themselves to accomplish
some task or other.  I never understood the swapping mechanism (not
important, I suppose) and I never could imagine a task that would or could
be handled like that.  Anybody have any experience with these?

PL
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-09T11:31:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b38ehF38u69oU1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga>`

```


"tlmfru" <lacey@mts.net> wrote in message 
news:TUT2k.163$Jh7.149@newsfe21.lga...
> Since Yourdon & Constantine have been invoked in this discussion - I have 
> a
…[8 more quoted lines elided]…
>
The dispatcher routines within the SCOPE OS of the CDC Cyber series worked 
exactly like that.

The switching was accomplished, not by a semaphore or mailbox post as you 
might expect, but by a hardware "exchange jump" which caused a "context 
switch". (All registers saved and restored and a new task initiated.)

It was very effective.

You can (could?) use priveleged instructions on IBM mainframes to do 
something very similar doing a STM, then SVC to a new task and LM the new 
context.

It is pretty standard practice for multithreading environments where you 
want total control of the threading (not usually desirable but occasionally 
necessary). You can achieve it on a PC by raising your own interrupt, and 
both Java and C# (I'm sure there are others, too...) have methods available 
for listening, threading and control.

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-08T21:36:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga>`

```

"tlmfru" <lacey@mts.net> wrote in message 
news:TUT2k.163$Jh7.149@newsfe21.lga...
> Since Yourdon & Constantine have been invoked in this discussion - I have 
> a
…[9 more quoted lines elided]…
>

Donald Knuth's The ARt of Computer Programming Volume 1 discusses 
coroutines.  There is an elevator simulation and some other examples.  If 
you know IBM mainframe assembler language there are some examples of the 
coroutines from Knuth at: http://www.cbttape.org/cbtdowns.htm
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-08T21:43:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com...
>
> "tlmfru" <lacey@mts.net> wrote in message 
…[21 more quoted lines elided]…
>

Opps sorry, forgot to mention, see file number 590
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-08T21:35:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VE03k.228$QN1.89@newsfe15.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com>`

```
Will have a shufty at it.  I know BAL but don't have access to am IBM
system.

Thanks
Pl

Charles Hottel <chottel@earthlink.net> wrote in message
news:2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message
…[4 more quoted lines elided]…
> >> Since Yourdon & Constantine have been invoked in this discussion - I
have
> >> a
> >> question about a concept that turned up in their publications.  This
was
> >> "co-routines" - two or more definable routines (i.e., having a start
and
> >> a
> >> finish) that continuously swapped control between themselves to
…[11 more quoted lines elided]…
> > coroutines.  There is an elevator simulation and some other examples.
If
> > you know IBM mainframe assembler language there are some examples of the
> > coroutines from Knuth at: http://www.cbttape.org/cbtdowns.htm
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 20)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-09T22:00:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga>`

```
google for z390, it is free and lets you assemble and run  ibm assembler on 
a pc

"tlmfru" <lacey@mts.net> wrote in message 
news:VE03k.228$QN1.89@newsfe15.lga...
> Will have a shufty at it.  I know BAL but don't have access to am IBM
> system.
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 21)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-09T22:44:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com>`

```
There are several ways to implement coroutines in IBM mainframe assembler, 
depending on the brach instructions used.

If you have two coroutinescalled IN and OUT you can do the following using 
two registers:

    "IN" ------BALR R7,R8 -----> "OUT"
    "IN" <-----BALR R8,R7 -------"OUT"

Or you can use  the following using a single register:

    "IN" <----BAL  R7,0(R7) -----> "OUT"

Or here is another way using a single register:

    "IN" <------BALR R7,R7 ------> "OUT"

IIRC the elevator simulation uses a more general "Call Table" approach.

If you download the zip file you will also need Xmit Manager to view the 
files on a PC.  Here is the overview documentation from the $$ASMDOC file:


*-------------------------------------------------------------------

--* * ASM00003 KNUTH COROUTINE

* *-------------------------------------------------------------------

--*

17 JUL 1980 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 191-194

COROUTINE EXAMPLE


TRANSLATE ONE CODE INTO ANOTHER. INPUT CODE TO BE TRANSLATED IS A

SEQUENCE OF ALPHAMERIC CHARACTERS TERMINATED BY A PERIOD, E.G.,


A2B5E3426FG0ZYW3210PQ89R.


BLANK COLUMNS ARE TO BE IGNORED. FROM LEFT TO RIGHT, IF THE NEXT

CHARACTER IS A DIGIT, SAY N, IT INDICATES (N+1) REPETITIONS OF THE

FOLLOWING CHARACTER, WHETHER THE FOLLOWING DIGIT IS A DIGIT OR NOT

. A NONDIGIT SIMPLY DENOTES ITSELF.


OUTPUT CONSISTS OF THE SEQUENCE INDICATED AND SEPARATED INTO GROUP

S OF THREE CHARACTERS:


ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.


TWO COROUTINES AND A SUBROUTINE. SUBROUTINE 'NEXTCHAR' FINDS THE

NONBLANK CHARACTER. COROUTINE 'IN' FINDS THE CHARACTERS OF THE

INOUT CODE WITH THE PROPER REPLICATION. COROUTINE 'OUT' PUT THE CO

DE INTO THREE-DIGIT GROUPS.


*-------------------------------------------------------------------

--* * ASM00004 KNUTH COROUTINE USING BALR R7,R8

* *-------------------------------------------------------------------

--*

17 JUL 1980 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 191-194

COROUTINE EXAMPLE


TRANSLATE ONE CODE INTO ANOTHER. INPUT CODE TO BE TRANSLATED IS A

SEQUENCE OF ALPHAMERIC CHARACTERS TERMINATED BY A PERIOD, E.G.,


A2B5E3426FG0ZYW3210PQ89R.


BLANK COLUMNS ARE TO BE IGNORED. FROM LEFT TO RIGHT, IF THE NEXT

CHARACTER IS A DIGIT, SAY N, IT INDICATES (N+1) REPETITIONS OF THE

FOLLOWING CHARACTER, WHETHER THE FOLLOWING DIGIT IS A DIGIT OR NOT

. A NONDIGIT SIMPLY DENOTES ITSELF.


OUTPUT CONSISTS OF THE SEQUENCE INDICATED AND SEPARATED INTO GROUP

S OF THREE CHARACTERS:


ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.


TWO COROUTINES AND A SUBROUTINE. SUBROUTINE 'NEXTCHAR' FINDS THE

NONBLANK CHARACTER. COROUTINE 'IN' FINDS THE CHARACTERS OF THE

INOUT CODE WITH THE PROPER REPLICATION. COROUTINE 'OUT' PUT THE CO

DE INTO THREE-DIGIT GROUPS.


'IN' ------BALR R7,R8 -----> 'OUT'

'IN' <-----BALR R8,R7 ------ 'OUT'


*-------------------------------------------------------------------

--* * ASM00005 KNUTH COROUTINE USING BAL R7,0(R7)

* *-------------------------------------------------------------------

--*

17 JUL 1980 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 191-194

COROUTINE EXAMPLE


TRANSLATE ONE CODE INTO ANOTHER. INPUT CODE TO BE TRANSLATED IS A

SEQUENCE OF ALPHAMERIC CHARACTERS TERMINATED BY A PERIOD, E.G.,


A2B5E3426FG0ZYW3210PQ89R.


BLANK COLUMNS ARE TO BE IGNORED. FROM LEFT TO RIGHT, IF THE NEXT

CHARACTER IS A DIGIT, SAY N, IT INDICATES (N+1) REPETITIONS OF THE

FOLLOWING CHARACTER, WHETHER THE FOLLOWING DIGIT IS A DIGIT OR NOT

. A NONDIGIT SIMPLY DENOTES ITSELF.


OUTPUT CONSISTS OF THE SEQUENCE INDICATED AND SEPARATED INTO GROUP

S OF THREE CHARACTERS:


ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.


TWO COROUTINES AND A SUBROUTINE. SUBROUTINE 'NEXTCHAR' FINDS THE

NONBLANK CHARACTER. COROUTINE 'IN' FINDS THE CHARACTERS OF THE

INOUT CODE WITH THE PROPER REPLICATION. COROUTINE 'OUT' PUT THE CO

DE INTO THREE-DIGIT GROUPS.


'IN' <---BAL R7,0(R7)---> 'OUT'


*-------------------------------------------------------------------

--* * ASM00006 KNUTH COROUTINE USING BALR R7,R7

* *-------------------------------------------------------------------

--*

17 JUL 1980 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 191-194

COROUTINE EXAMPLE


TRANSLATE ONE CODE INTO ANOTHER. INPUT CODE TO BE TRANSLATED IS A

SEQUENCE OF ALPHAMERIC CHARACTERS TERMINATED BY A PERIOD, E.G.,


A2B5E3426FG0ZYW3210PQ89R.


BLANK COLUMNS ARE TO BE IGNORED. FROM LEFT TO RIGHT, IF THE NEXT

CHARACTER IS A DIGIT, SAY N, IT INDICATES (N+1) REPETITIONS OF THE

FOLLOWING CHARACTER, WHETHER THE FOLLOWING DIGIT IS A DIGIT OR NOT

. A NONDIGIT SIMPLY DENOTES ITSELF.


OUTPUT CONSISTS OF THE SEQUENCE INDICATED AND SEPARATED INTO GROUP

S OF THREE CHARACTERS:


ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.


TWO COROUTINES AND A SUBROUTINE. SUBROUTINE 'NEXTCHAR' FINDS THE

NONBLANK CHARACTER. COROUTINE 'IN' FINDS THE CHARACTERS OF THE

INOUT CODE WITH THE PROPER REPLICATION. COROUTINE 'OUT' PUT THE CO

DE INTO THREE-DIGIT GROUPS.


'IN' <---BALR R7,R7---> 'OUT'


*-------------------------------------------------------------------

--* * ASM00007 KNUTH ELEVATOR SIMULATION

* *-------------------------------------------------------------------

--*

18 MAY 1981 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 279-293

ELEVATOR SIMULATION


*-------------------------------------------------------------------

--* * ASM00008 KNUTH ELEVATOR SIMULATION 2.2.5 EXERCISE 5

* *-------------------------------------------------------------------

--*

18 MAY 1981 - CHARLES HOTTEL

KNUTH, FUNDAMENTAL ALGORITHMS, 2ND EDITION, PP 279-293

ELEVATOR SIMULATION


SECTION 2.2.5 EXERCISE 5: MAN NUMBER 10, IN=2, OUT=4











"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com...
> google for z390, it is free and lets you assemble and run  ibm assembler 
> on a pc
…[50 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 22)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:33:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com> <mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com>`

```
On Jun 9, 10:44 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> There are several ways to implement coroutines in IBM mainframe assembler,
> depending on the brach instructions used.
>

[stuff from Don Knuth, classical algorithmist, snipped]

Thanks, Charles.

I caught just a whiff of the Wikipedia entry on co-routines and did
some Googling... I think that what are popularly known as "pipes" in
the Unix world may be implemented as co-routines. You know, when the
output of "grep" is fed into the stream editor "sed".

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 23)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-10T18:34:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q7WdnbvLW_j3nNLVnZ2dnUVZ_tLinZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com> <mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com> <49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com...
On Jun 9, 10:44 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> There are several ways to implement coroutines in IBM mainframe assembler,
> depending on the brach instructions used.
>

[stuff from Don Knuth, classical algorithmist, snipped]

Thanks, Charles.

I caught just a whiff of the Wikipedia entry on co-routines and did
some Googling... I think that what are popularly known as "pipes" in
the Unix world may be implemented as co-routines. You know, when the
output of "grep" is fed into the stream editor "sed".

Ken

[Charlie]

Coroutines call each other, usually using a mechanism that allows them to do 
so from whatever point they desire.

Pipes are not coroutines.  They are communicating processes, producers and 
consumers if you like, usually communicating via a queue.  The processes in 
pipes do not call each other.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 24)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-11T07:05:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com> <mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com> <49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com> <q7WdnbvLW_j3nNLVnZ2dnUVZ_tLinZ2d@earthlink.com>`

```
On Jun 10, 6:34 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> <klsha...@att.net> wrote in message
>
…[24 more quoted lines elided]…
> pipes do not call each other.

Hi, Charlie,

This is why I thought pipes might be an application of coroutines...
Wikipedia says: "Coroutines are well-suited for implementing more
familiar program components such as cooperative tasks, iterators,
infinite lists and pipes."

I do not know what "pipes" the Wikipedia author might have been
thinking of. The "pipes" that I am most familiar with are those from
the Unix world.

But that should not obscure the greater purpose here - we were trying
to find application examples of co-routines for Mr. PL. So a more
direct line of inquiry might be useful... what applications were well
suited for the examples posted by you/Knuth?

Yes, my vague recollection from computer science thirty years ago was
that they could be used for cooperative processes to overcome
different physical record units between two different devices. But I
have forgotten the details long ago.

Do you know of other applications?

Thanks a lot,
Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 25)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-11T19:49:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com> <mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com> <49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com> <q7WdnbvLW_j3nNLVnZ2dnUVZ_tLinZ2d@earthlink.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com...
On Jun 10, 6:34 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> <klsha...@att.net> wrote in message
>
…[26 more quoted lines elided]…
> pipes do not call each other.

Hi, Charlie,

This is why I thought pipes might be an application of coroutines...
Wikipedia says: "Coroutines are well-suited for implementing more
familiar program components such as cooperative tasks, iterators,
infinite lists and pipes."

I do not know what "pipes" the Wikipedia author might have been
thinking of. The "pipes" that I am most familiar with are those from
the Unix world.

But that should not obscure the greater purpose here - we were trying
to find application examples of co-routines for Mr. PL. So a more
direct line of inquiry might be useful... what applications were well
suited for the examples posted by you/Knuth?

Yes, my vague recollection from computer science thirty years ago was
that they could be used for cooperative processes to overcome
different physical record units between two different devices. But I
have forgotten the details long ago.

Do you know of other applications?

Thanks a lot,
Ken

[Charlie]

You could think of a program that does I/O and the routine(s) that do the 
actual I/O as coroutines.

In the elevator simulation the elevators and the passengers(actually I think 
a list of passengers) are implemented via coroutines.  Each time the 
elevator returns control to the passenger, the passenger coroutine resumes 
from wherever it was when it gave up control to the elevator, and vice versa 
for when the passenger gives up control to the elevator.  The elevator can 
call the passenger from many different places, wherever and whenever it 
desires,  so there are not single entry and exit points in these routines.

In both of these examples the routines are thought of as being somewhat 
equal, i.e. one is not subordinate to the other..

No doubt you could implement 'pipes' via coroutines, but when I hear 'pipes' 
I think of Unix pipes and I think they use a queue with some kind of monitor 
to synchronize access to the queue.  MS DOS emulated this by using a 
temporary intermmediate file, but that implementation did not give the 
overlap in processing that Unix pipes give.

In an operating system that implements cooperative multiprocessing you could 
view the cooperating processes as coroutines.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 26)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-12T15:37:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <w4OdnUs30PyKFNHVnZ2dnUVZ_tHinZ2d@earthlink.com> <2rudnVqdmKQ5F9HVnZ2dnUVZ_hadnZ2d@earthlink.com> <VE03k.228$QN1.89@newsfe15.lga> <EtGdnd-JTbG6fdDVnZ2dnUVZ_oDinZ2d@earthlink.com> <mP6dncIRA7Qcd9DVnZ2dnUVZ_hOdnZ2d@earthlink.com> <49f4adbc-183a-4024-b178-10420b64d05e@l42g2000hsc.googlegroups.com> <q7WdnbvLW_j3nNLVnZ2dnUVZ_tLinZ2d@earthlink.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com>`

```
On Jun 11, 7:49 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> <klsha...@att.net> wrote in message
>
…[28 more quoted lines elided]…
> view the cooperating processes as coroutines.

Yes, thanks, Charles. This helps refresh my memory, and squares up
with I am able to remember.

Kinda interesting how passengers entering and exiting the elevator in
the simulation amounts to the same problem...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 27)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-13T01:04:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2sh2i$d7o$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com>`

```
In article <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 11, 7:49�pm, "Charles Hottel" <chot...@earthlink.net> wrote:
>> <klsha...@att.net> wrote in message
…[6 more quoted lines elided]…
>> [Charlie]

[snip]

>> In the elevator simulation the elevators and the passengers(actually I think
>> a list of passengers) are implemented via coroutines.  Each time the
…[7 more quoted lines elided]…
>> equal, i.e. one is not subordinate to the other..

[snip]

>Yes, thanks, Charles. This helps refresh my memory, and squares up
>with I am able to remember.
>
>Kinda interesting how passengers entering and exiting the elevator in
>the simulation amounts to the same problem...

Ow... elevator-controlling routines were written by folks with a closer 
understanding of the machine than I have but there's something I see as 
being incorrect about the evaluations given above.

The elevator does not 'call' anyone; unless it has a default setting (no 
input for (time) and it automatically initiates the sequence to move to 
(floor)) then all motion is in response to a passenger's (or potential 
passenger's) request.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 28)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-13T08:49:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com>`

```
On Jun 12, 9:04 pm, docdw...@panix.com () wrote:
> In article <57aeac6f-5d14-46bd-8558-b3204c382...@c58g2000hsc.googlegroups.com>,
> Ow... elevator-controlling routines were written by folks with a closer
…[8 more quoted lines elided]…
> DD

I have had to think about it for a while. Here is what I have come up
with.

One thing I am pretty certain about, the elevator has a "capacity",
and that is what is serving as the "circular queue" into which
passengers are added (produced into) and then deleted (consumed.) A
tiny difference here: in some the Input/Output utility apps I think
the circular queue is usually (always) FIFO. In the elevator case, it
would not be FIFO, hence not really a queue at all, but rather a
buffer, or a "pool."

I think maybe the elevator _can_ make a call. We kind have to think
about those pushbuttons... the ones in the elevator, but also the ones
on the floors. When all the passengers have been delivered, and there
are no more buttons lit within the elevator, it makes a "call" to the
floors - Produce me a passenger!  If no buttons are pushed, it enters
an idle state, until some floor button is pushed. Then it moves to
that floor. This produces a passenger. So the elevator is "consuming"
the passengers by delivering them, and asking the floors to "produce"
them. From the floors point of view, it is calling the elevator to
consume them.

The elevator can "call" the floors to produce another passenger after
every time it delivers one to a floor and opens the door. If one of
the floor buttons pushed is in between current-floor and next-floor-
pressed in the elevator, then he can pick up that passenger "along the
way."

By the way, elevator simulation, I think, is the classical application
used to illustrate "state-transitions." I remember seeing it. Can't
remember where though. Might have been in Yourdon/Constantine. Might
have been in something by the other real-time structured design
people; either Ward/Mellor or Hatley/Pirbhai. I'm sure Google can find
them.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-13T23:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2v1de$bb0$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com>`

```
In article <72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 12, 9:04�pm, docdw...@panix.com () wrote:
>> In article
…[15 more quoted lines elided]…
>passengers are added (produced into) and then deleted (consumed.)

Bingo... let's stop right here and examine the phenomenon.  I would say 
all an elevator recognises are requests to stop at a certain floor; 
whether those requests are internal or external is irrelevant.  All that 
matters is that a request to stop at (floor) is made and whether the 
elevator can stop, safely, before reaching the floor for which the request 
was made.

In other words... given the same direction and distance from (floor) it 
makes no difference whether a request-to-stop was made by a passenger on 
(floor) *or* by a passenger already in the elevator who pushes a button 
for that floor (intentionally or accidentally).  In the latter 
circumstance (called by the professionals 'OWB' or 'Oops, Wrong Button' 
scenario) nothing is being introduced other than a request to stop.

[snip]

>I think maybe the elevator _can_ make a call. We kind have to think
>about those pushbuttons... the ones in the elevator, but also the ones
>on the floors. When all the passengers have been delivered, and there
>are no more buttons lit within the elevator, it makes a "call" to the
>floors - Produce me a passenger!

Ummmmm... that, I would say, is streching it a weeeeeee bit; to call a 
check for input a demand that input be produced seems analagous to calling 
'listening for the telephone to ring' 'demanding the telephone produce a 
ring'.

>If no buttons are pushed, it enters
>an idle state, until some floor button is pushed. Then it moves to
>that floor. This produces a passenger.

I disagree.  Remember the childhood game of 'ring and run'?  Assume that 
someone pushes a floor-button and then is called away before the elevator 
arrives; the elevator responds to the input but no further input is 
received.  The doors then close and the elevator resumes its previous 
direction of travel if another input is recognised (or another button is 
pushed to issue a summons in that same direction), reverses direction if 
there is no input in the original direction and there is an input in the 
opposite direction... or then 'times out' and goes to the default floor.

>So the elevator is "consuming"
>the passengers by delivering them, and asking the floors to "produce"
>them. From the floors point of view, it is calling the elevator to
>consume them.

An interesting assumption... what might be the floor's 'point of view' for 
the OWB scenario?

('oh look... here's something unexpected!')

>
>The elevator can "call" the floors to produce another passenger after
>every time it delivers one to a floor and opens the door.

Again, only in the same manner as one 'calls' the telephone to see if it 
is ringing.  Consider the following conversation:

A: 'Well, one might say that the merchang pays me for my money with a 
canteloupe.'

B: 'Were one to say that it would be meaningless.'

A: 'For what reason is it meaningless?'

B: 'For the reason that the meaning of words are in their use (per 
Wittgenstein) and the use of the word 'paying' in the context of a 
transaction such as you describe is to indicate the party tendering cash, 
not the party rendering goods.'

[snip]

>By the way, elevator simulation, I think, is the classical application
>used to illustrate "state-transitions." I remember seeing it. Can't
…[3 more quoted lines elided]…
>them.

I remember it as something used to test folks working towards a Bachelor's 
in Computer Science... and my smiling at thinking about how it had been 
applied, before computers existed, with great clacking relays and 
elevator-cars moving at 1,000 f/s (304.8 m/s).

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 30)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-14T10:45:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2fc1d67-22e4-4b12-b8c9-42ae3bb31402@z72g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com> <g2v1de$bb0$1@reader2.panix.com>`

```
On Jun 13, 7:55 pm, docdw...@panix.com () wrote:
> In article <72c58973-9e29-423e-8a09-fc84c9e32...@z66g2000hsc.googlegroups.com>,
>
…[7 more quoted lines elided]…
> was made.

The distinction between the external requests (buttons on the floors)
and internal requests (buttons in the elevator) matters. A floor
button pushed means that a passenger (usually) is about to enter the
elevator. An elevator button pushed means that a passenger is about to
exit. The elevator has a fixed capacity. Probably the simulation is to
determine, given a certain quasi-random distribution of floor button
pushes, and also internal button pushes, how often does the elevator
have to refuse the entry of another passenger. They have to decline
entry, and push the button again. For another elevator, or the same
elevator later.

>
> In other words... given the same direction and distance from (floor) it
…[4 more quoted lines elided]…
> scenario) nothing is being introduced other than a request to stop.

Yes, to be a good simulation, you would probably need some salting in
of OWB's, so that not every internal button pushed results in a
passenger exit (passenger consumed.) On the other hand, sometimes
multiple passengers will exit on the same floor, from the same
internal button pushed. I suppose they would have to build that in to.

>
> [snip]
…[10 more quoted lines elided]…
> ring'.

Yes, I know, it is perhaps counter-intuitive. But calling upon the
floors to "produce" a passenger, is not quite like "produce on
demand." It is simply "produce, and I'll wait until you do." I think
in implementations, the producer, if unable to produce, would simply
return to the consumer, with nothing added to the queue. The consumer,
then seeing that nothing has been produced, and having already
consumed everyone in the elevator, then once again calls the
producer.

In real-time systems, the "calls" can be dispensed with altogether.
You don't really need them. What you need are these things -
a. shared memory (that is the circular queue, or if not FIFO, the
"pool")
b. a "semaphore" to control access to the queue, to avoid "race
conditons". In some hardware I think that is called "lock and
test" (or was it test and lock?). Anyway, the instruction to test-and-
request-lock has to be a single instruction

This way, the two co-routines, which are now not quite co-routines,
are actually independently executing "peer" programs. One produces
into the queue; the other consumes from the queue. If the producer
sees the queue is full, he has nothing to do, so he sleeps. Same thing
for the consumer.

>
> >If no buttons are pushed, it enters
…[10 more quoted lines elided]…
> opposite direction... or then 'times out' and goes to the default floor.

Well, yes, not every button push will produce a passenger. Have to
build that into the simulation. But without the floor button push, the
elevator would not go that floor (after exiting all passengers),
unless that is the default floor. so the floor button push is
necessary to the produce action to occur.

>
> >So the elevator is "consuming"
…[6 more quoted lines elided]…
>

Yes, I *think* that the floor is the "producer".

On the other hand, it does seem that passengers "produce themselves",
by entering, and then "consume themselves", by exiting. So maybe I
don't have it _all_ down just yet.


> ('oh look... here's something unexpected!')
>
…[7 more quoted lines elided]…
>

Well, yes, that is it, peculiar it might be. Elsewhere I have seen it
termed a 'yield', rather than a 'call'. The observer yields to the
phone, sleeping until it rings. (That is what self-confident suitors
(or dould that be suitees?) do... _sleeping_, instead of "waiting by
the phone" for Romeo to call. :-) )


> A: 'Well, one might say that the merchang pays me for my money with a
> canteloupe.'
…[22 more quoted lines elided]…
> elevator-cars moving at 1,000 f/s (304.8 m/s).

What we also learned in CompSci Systems Analysis class was the
solution to the elevator problem of "What if the passenger has to wait
too long and gets irritated?"

I'm not joking - the solution our instructor told us was - ta-da! -
mount a couple of mirros so they can busy themselves by combing their
hair and straightening their ties.

I am unsure which real-time model that solution follows: Ward/Mellor,
Hatley/Pirbhai. Answer left to the student as an exercise.

Anyway, maybe all of this "makes it better." If it doesn't, then who
do YOU think the producers and consumers are?

I could be wrong, ya know. Sort of along the lines of "Yeah, I thought
I made a mistake once, but I was wrong."

And if so, I can always apply the Politician's Ploy, "Listen to what
I  _meant_, not what I _said_!"

Best wishes,
Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-15T12:26:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g331pg$c20$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com> <g2v1de$bb0$1@reader2.panix.com> <b2fc1d67-22e4-4b12-b8c9-42ae3bb31402@z72g2000hsb.googlegroups.com>`

```
In article <b2fc1d67-22e4-4b12-b8c9-42ae3bb31402@z72g2000hsb.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 13, 7:55�pm, docdw...@panix.com () wrote:
>> In article
…[14 more quoted lines elided]…
>elevator.

Leaving aside the status of 'usually' in any series of binary 
instructions... a floor button pushed seems nothing more than a request of 
'based on your direction/speed stop here'.

>An elevator button pushed means that a passenger is about to
>exit.

As above... an elevator button pushed seems, likewise, 'based on your 
direction/speed stop here'.  Differentiating between the two equal 
requests would seem to require something else.

>The elevator has a fixed capacity. Probably the simulation is to
>determine, given a certain quasi-random distribution of floor button
…[3 more quoted lines elided]…
>elevator later.

Ignoring the 'ahhhhh, but the boxer is left-handed' advent of Yet Another 
Variable... this seems easily disposed of.  Given that it is rather 
unlikely that an elevator in motion will suddenly show a load-weight 
increase outside of the one manifested by acceleration the condition of 
overload could be dealt with by mechanical means.

(every (n) fractions-of-a-second a stopped car compares its load to 
the maximum permitted under conditions of (current-load plus 
acceleration-increase); if greater then the general program is overriden 
and the car Does Not Move (and, of course, displays a Helpful Error 
Message) until it is safe to continue)

>
>>
…[11 more quoted lines elided]…
>internal button pushed. I suppose they would have to build that in to.

I disagree, as stated above.  Capacity is a different circuit, entire, 
based on the calculation of what will be pressing on the floor of the car 
at maximum speed.  Weight-changes outside of this occur only at a stop.

>
>>
…[13 more quoted lines elided]…
>Yes, I know, it is perhaps counter-intuitive.

Not 'counter-intuitive'; as demonstrated below it is a new use of words, a 
use in a way not encompassed by previous uses.

>But calling upon the
>floors to "produce" a passenger, is not quite like "produce on
>demand."
>It is simply "produce, and I'll wait until you do." 

See above - 'Produce me a passenger!' is your own phrasing, Mr Shafer, and 
in common English use indicates an Imperative mood.  The Imperative, by 
definition (http://dictionary.reference.com/browse/imperative), is the 
mood 'used in commands, requests, etc.'  

[snip]

>In real-time systems, the "calls" can be dispensed with altogether.

As noted earlier... this is a bit closer to the machine than my 
experience.  My approach, obviously, is more along the lines of 'do not 
burn up resources until the Enter key is pressed'... and the magic of how 
the pseudoconversation is resumed is left to those whose interpersonal 
skills are - believe it or not! - even worse than mine, the Systems folks.

[snip]

>> >If no buttons are pushed, it enters
>> >an idle state, until some floor button is pushed. Then it moves to
…[11 more quoted lines elided]…
>Well, yes, not every button push will produce a passenger.

Every request, internal or external, will (given associated conditions of 
direction and speed) produce a stop.  If the inputs are identical 
('request to stop at (floor)') and the results are identical ('direction 
and speed allow for stopping at (floor) so sequence-for-stopping 
initiated') then 'elegance' - or simple laziness - seems to indicate they 
be handled identically.

>Have to
>build that into the simulation. But without the floor button push, the
>elevator would not go that floor (after exiting all passengers),
>unless that is the default floor. so the floor button push is
>necessary to the produce action to occur.

If an elevator will not go to a floor unless a button on that floor is 
pushed, Mr Shafer, then there cannot be an OWB scenario... or *any* 
infulence on stopping by the passengers already inside.

[snip]

>> Again, only in the same manner as one 'calls' the telephone to see if it
>> is ringing.  Consider the following conversation:
>>
>
>Well, yes, that is it, peculiar it might be.

Not 'peculiar', Mr Shafer... in the sense that 'it isn't spoken of in that 
manner' then, per Wittgenstein, it is meaningless.  An attempt to redefine 
phenomena is, at base, an attempt to define phenomena; if definitions are 
not agreed-upon in advance a bit of confusion might result.

[snip]

>> I remember it as something used to test folks working towards a Bachelor's
>> in Computer Science... and my smiling at thinking about how it had been
…[9 more quoted lines elided]…
>hair and straightening their ties.

So far, Mr Shafer, we've been dealing with elevator-cars, floors, speeds 
and directions, requests for stops and the like.  What need is there to 
introduce actual human beings into that situation?  After all, when it 
comes to computer systems those human-type people just make things so... 
messy.

(again, per Wittgenstein, on the results of logic: 'The bridge must not 
fall down.')

>
>I am unsure which real-time model that solution follows: Ward/Mellor,
…[3 more quoted lines elided]…
>do YOU think the producers and consumers are?

As mentioned a long ways back, Mr Shafer, I do not think of producers and 
consumers in this scenario, I think of stop-requests and the ability to 
satisfy same (direction/speed).  The only thing produced is an alternation 
between rest and motion, the only thing consumed is energy.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 29)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-14T15:29:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f-dneSWAIpzhsnVnZ2dnUVZ_vzinZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:72c58973-9e29-423e-8a09-fc84c9e3231e@z66g2000hsc.googlegroups.com...
On Jun 12, 9:04 pm, docdw...@panix.com () wrote:
> In article 
> <57aeac6f-5d14-46bd-8558-b3204c382...@c58g2000hsc.googlegroups.com>,
…[9 more quoted lines elided]…
> DD

I have had to think about it for a while. Here is what I have come up
with.

One thing I am pretty certain about, the elevator has a "capacity",
and that is what is serving as the "circular queue" into which
passengers are added (produced into) and then deleted (consumed.) A
tiny difference here: in some the Input/Output utility apps I think
the circular queue is usually (always) FIFO. In the elevator case, it
would not be FIFO, hence not really a queue at all, but rather a
buffer, or a "pool."

I think maybe the elevator _can_ make a call. We kind have to think
about those pushbuttons... the ones in the elevator, but also the ones
on the floors. When all the passengers have been delivered, and there
are no more buttons lit within the elevator, it makes a "call" to the
floors - Produce me a passenger!  If no buttons are pushed, it enters
an idle state, until some floor button is pushed. Then it moves to
that floor. This produces a passenger. So the elevator is "consuming"
the passengers by delivering them, and asking the floors to "produce"
them. From the floors point of view, it is calling the elevator to
consume them.

The elevator can "call" the floors to produce another passenger after
every time it delivers one to a floor and opens the door. If one of
the floor buttons pushed is in between current-floor and next-floor-
pressed in the elevator, then he can pick up that passenger "along the
way."

By the way, elevator simulation, I think, is the classical application
used to illustrate "state-transitions." I remember seeing it. Can't
remember where though. Might have been in Yourdon/Constantine. Might
have been in something by the other real-time structured design
people; either Ward/Mellor or Hatley/Pirbhai. I'm sure Google can find
them.

Ken

[Charlie]

See my earlier response to DocDwarf.

Step E4 of the elevator (let people in, out):

If anyone in the ELEVATOR list has OUT = FLOOR, send the man of this type 
who has most recently entered immediately to step M6 (Get Out) of his 
program, wait 25 units, the repeat step E4.  If no such men exist, but 
QUEUE[FLOOR] is not empty, send the front man of that queue immediatelt to 
step M5 (Get In) instead of M4. in his program, wait 25 units, and repeat 
step E4......
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 28)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-06-14T15:22:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:g2sh2i$d7o$1@reader2.panix.com...
> In article 
> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com>,
…[47 more quoted lines elided]…
>

Sorry for the slow response.  I had a procedure in the hospital and they 
kept me there and extra day.

The program simulates the elevator at tha Mathematics building at CalTech. 
Here is a brief overview.

Coroutine M (Men):

M1. Enter, prepare for successor
M2. Signal and wait (for the elevator)
M3. Enter queue
M4. Give up
M5. Get In
M6. Get Out

Couroutine E(Elevator)

E1. Wait for call
E2. Change of state?
E3. Open door
E4. Let people out, in
E5. Close door
E6. Prepare to move
E7. Go up a floor
E8. Go down a floor
E9. Set inaction indicator

Subroutine D (Decision):

D1. Decision necessary?
D2. Should door open?
D3. Any calls?
D4. Set State
D5. Elevator dormant?

For more details see The Art of Computer Programming, Volume 1, second 
edition pp 279 -293.

At the time I was first exposed to this book as a reading assignment in 
college I only knew a very little PDP-8 assembly language. This book really 
opened up my eyes to the world of computer science and how much more there 
was to it than I had ever thought. I remember studying this elevator 
simulation and thinking it was so very complicated that I could never 
understand it.  When I returned to it much later with experience in COBOL 
and IBM mainframe assembler and was actually able to implement it I remember 
experiencing a great feeling of progress and accomplishment.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-15T12:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3329u$f90$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com>`

```
In article <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>
><docdwarf@panix.com> wrote in message news:g2sh2i$d7o$1@reader2.panix.com...

[snip]

>> The elevator does not 'call' anyone; unless it has a default setting (no
>> input for (time) and it automatically initiates the sequence to move to
…[4 more quoted lines elided]…
>kept me there and extra day.

Best wishes for a speedy, complete and convenient convalescence, Mr 
Hottel.

>
>The program simulates the elevator at tha Mathematics building at CalTech. 
…[29 more quoted lines elided]…
>D5. Elevator dormant?

Hmmmmm... I notice that M2 and E1 can be either internal (person in car) 
or external (from floor); M4 seems valid only for those on the floor.

[snip]

>I remember studying this elevator 
>simulation and thinking it was so very complicated that I could never 
>understand it.  When I returned to it much later with experience in COBOL 
>and IBM mainframe assembler and was actually able to implement it I remember 
>experiencing a great feeling of progress and accomplishment.

I will confess - as might be readily apparent to any reader - that I've 
never formally studied this problem and all my comments, evaluations and 
suggestions are extemporaneous.

As such they should be considered to be of appropriate value.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 30)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-16T07:19:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fed03729-0b33-4e15-aeee-1403ee71baca@t54g2000hsg.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <g3329u$f90$1@reader2.panix.com>`

```
On Jun 15, 8:35 am, docdw...@panix.com () wrote:
> In article <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7in...@earthlink.com>,
>
…[5 more quoted lines elided]…
>

And Value is what they do have, Mr. DocDwarf, for in Some Ways (but
probably not all) I may be coming over to your way of thinking...

After a couple of long drives over the weekend, and the commensurate
Quality Time With Self, and temporarily disabling the FM radio, this
came to mind...

Yes, from the elevator point of view, what is important are the button-
pushes. The elevator will request that they be produced, and then will
consume them, and when consumed, will de-illuminate them. (Perhaps you
can help me with a verb better than de-illuminate.)

But it takes people to push the buttons, Mr. Dashwood, and Mr. Charles
put forth so succinctly in his CoRoutine Men above.

The model below will presuppose that we cannot have those button-
pushes without Men, but because I am taking a slightly different
approach, let us call them Passengers, for their destiny is to ride
the elevator.

So what we start with is a coroutine Produce_Passenger, which will
create out of thin error a Passenger to enter our Building, Elevator
Rides, Inc., in downtown Manhattan, and said passenger will be created
with some characteristics important to our modeling, such as his
proclivity to hit the wrong button, how easily he tires, how curious
he might be regarding going from floor to floor, and we also assign
some "state" variables to him so that we might track his location (on
which floor, or in transit in the elevator), and a little bit of his
history (time entered building, number floor visited, etc. etc,
whatever is needed to make our modeling "realistic").

After creation, said Passenger enters the building, and
Produce_Passenger calls coroutine Consume_Passenger, whose purpose is
to consume said passenger by tiring him out with button-pushes and
elevator rides, until such time as he returns to Floor 1, exits the
building, crosses against a red light, is struck by a New York City
taxicab, and is killed. (The end.)  From time to time
Consume_Passenger will also call Produce_Passenger, so that there will
be another Passenger to consume, but we will (arbitrarily) set a
restriction of 1000 passengers in our building (due to hardware
constraints), and should the rate of consumption at some times be less
than the rate of production, Produce_Passenger may Return having
created no Passengers at all. This is OK.

So Produce_Passenger adds to the (non-FIFO) passenger queue, and
Consume_Passenger deletes from the (non-FIFO) passenger queue, but OH!
there is more going on, for we have not yet discussed the Elevator.

Part of what Consume_Passenger does is take our Passenger
characteristics and "model" the proclivity of the Passenger to push
buttons to ride the elevator, and it will have him do so, so that he
may take a ride. In doing this Consume_Passenger will see to it that
the passenger pushes a button, and thus Produce_Button_Push, which
then enters the Button_Push (non-FIFO) queue. From time to time, then
Consume_Passenger will also call upon Elevator, which in fact we could
call Consume_Button_Push, for indeed, Mr. DocDward, that is all the
elevator does, or can do, as you have gently pointed out to me - all
he can do is respond the button-push, de-illuminating the light
indicator when he attains the floor of the internal button pressed, or
responds the request button outside the elevator floor.
So the Consume_Passenger coroutine could maybe be called more aptly
Consume_Passenger_by_Producing_Button-Pushes, for it does both.

Here is a summary then...
Produce_Passenger adds to the Passenger Queue
Consume_Passenger_by_Producing_Button-Pushes deletes from the
Passenger Queue, but adds to the Button-Push queue.
Consume_Button_Push deletes from the Button-Push queue.

Now something very Beautiful and very Eerie is going on here, for...

if we choose aliases such "Life" for Produce_Passenger, and "Death"
for Consume_Passenger", and "The Ride" for Consume_Button_Push, what
we have is this...

Life thinks he is the Master over Death and TheRide.
Death thinks he is the Master over Life and TheRide,
but,
TheRide also thinks he is Master over Life and Death.

So the moral of this simulation program, is, -
"Be conscious of what you do on the Elevator because, in some views,
it is more important than Life and Death itself."

Or, if slightly different interpretation,
"Be nice to the folks on your way up, because you may see them again
on your way down."

. . .

Next Sunday at the Church of the Evangelizing Elevator -

Guest Lay Pastor Mr. Dashwood will deliver a sermon on "Repent Now!
for CoBOL is going to Hell in a Handbasket!"

Mr. DocDwarf will be Acolyte, because he is so good at providing
Light.

Mr. Charles Hottel will be Lector, and he will read to us from the
Book of Knuth, so that we might learn something useful.

Mr. HeyBub will be Sargent-at-Arms so that Security may be provided.

Music by The Ramones Gospel Choir Ensemble, directed by Tommy Ramone
(and not Phil Spector.)

And as for me? OH! I will be an Usher, so that I may greet you at the
door, For you are blessings to me all, and also, hee hee hee, be
responsible for passing the Offertory Plate. :-)

Your buddy,
Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-16T16:19:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g363qv$cc5$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <g3329u$f90$1@reader2.panix.com> <fed03729-0b33-4e15-aeee-1403ee71baca@t54g2000hsg.googlegroups.com>`

```
In article <fed03729-0b33-4e15-aeee-1403ee71baca@t54g2000hsg.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 15, 8:35�am, docdw...@panix.com () wrote:
>> In article <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7in...@earthlink.com>,
…[9 more quoted lines elided]…
>probably not all) I may be coming over to your way of thinking...

''You agree with me?  One of us must be wrong!', he cried, Wildely.'

[snip]

>Yes, from the elevator point of view, what is important are the button-
>pushes. The elevator will request that they be produced, and then will
>consume them, and when consumed, will de-illuminate them. (Perhaps you
>can help me with a verb better than de-illuminate.)

Extinguish... but I'd still question the use of 'request that they be 
produced' instead of 'check if there are any' or a simpler 'determine 
existence'.

>But it takes people to push the buttons, Mr. Dashwood, and Mr. Charles
>put forth so succinctly in his CoRoutine Men above.

I disagree.  It makes no difference to the elevator whether a finger, an 
errant broom-handle or an intoxicated (and very heavy) insect caused the 
input; all the elevator sees is 'stop requested'.

In support of this assertion I offer the fact of heat-sensitive elevator 
buttons, ones which saw a kind of faddish acceptance in the US until 
someone realised such devices could cause an elevator to stop at a floor 
on which a fire had started.

>The model below will presuppose that we cannot have those button-
>pushes without Men, but because I am taking a slightly different
>approach, let us call them Passengers, for their destiny is to ride
>the elevator.

This might, better than anything else, demonstrate the value of such a 
Deterministic assumption.

>
>So what we start with is a coroutine Produce_Passenger, which will
…[8 more quoted lines elided]…
>whatever is needed to make our modeling "realistic").

Occam's/Ockham's Razor might be used to pare this down a bit.  'Entities 
must not be multiplied beyond necessity'; unless one is running a Very 
Secure Institution it appears not to matter when someone came in, how long 
they spent where, summer- or winter-weight suits... to a moving elevator 
the necessary entities are direction, speed and request to stop at a 
floor.

[snip]

>So Produce_Passenger adds to the (non-FIFO) passenger queue, and
>Consume_Passenger deletes from the (non-FIFO) passenger queue, but OH!
…[7 more quoted lines elided]…
>then enters the Button_Push (non-FIFO) queue.

Trim, trim and trim yet again.  A request to stop at a floor will not 
always produce a passenger (the OFN, or 'Oops, Forgot Notepad' scenario, 
which causes an elevator to stop at a floor where no passenger enters... 
or maybe it was a poltergeist)...

... and a stop at a floor will not always produce a request to move to 
another floor, as in the case of someone getting the elevator and seeing 
that someone else there has already pressed (floor).

All the elevator sees is 'request to stop'.

[snip]

>Here is a summary then...
>Produce_Passenger adds to the Passenger Queue
>Consume_Passenger_by_Producing_Button-Pushes deletes from the
>Passenger Queue, but adds to the Button-Push queue.
>Consume_Button_Push deletes from the Button-Push queue.

There's still more to trim.  Perhaps it is better to fall back from Occam 
to Aristotle and consider a single-elevator system.  An elevator may, at 
any given moment, have one of three conditions:

1) Stopped and without direction ('dormant').
2) Stopped and with direction (floor-stop).
3) Moving and with direction (what it says).

For 1)... a request to stop at a floor generates a 'go there now', whether 
that request comes from a button on that floor being pressed or the button 
inside the elevator corresponding to that floor is pressed.

For 2)... a request to stop at a floor generates 'am I going that way?'.  
If the elevator is going that way then it stops at that floor.

For 3)... a request to stop at a floor generates 'am I able to stop there 
according to (rules)?'  If it can, it does.

Notice that 3) is the only condition which requires a complex 
evaluation... and if 3) results in a stop then the logic for 2) seems 
sequentially appropriate.

>
>Now something very Beautiful and very Eerie is going on here, for...
…[12 more quoted lines elided]…
>it is more important than Life and Death itself."

Perhaps I am immoral, then, as I see it only as 'While I am moving or at 
rest, let me consider my inertia and the requests which exist for me, that 
I might satisfy them according to the Way which seems best.'

[snip]

>Mr. DocDwarf will be Acolyte, because he is so good at providing
>Light.

I aspire to be an Alcol... but I have reached only Alcol-lite.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-17T19:15:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bp6klF3cp6r7U1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <g3329u$f90$1@reader2.panix.com> <fed03729-0b33-4e15-aeee-1403ee71baca@t54g2000hsg.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:fed03729-0b33-4e15-aeee-1403ee71baca@t54g2000hsg.googlegroups.com...
On Jun 15, 8:35 am, docdw...@panix.com () wrote:
<snip>
. . .

Next Sunday at the Church of the Evangelizing Elevator -

Guest Lay Pastor Mr. Dashwood will deliver a sermon on "Repent Now!
for CoBOL is going to Hell in a Handbasket!"

[Pete]

Sorry, I can't make it. I have an Ascension service at the Church of  Top 
Down Design.

Besides, I was excommunicated from the Church of the Evangelizing Elvator... 
Heresy...something about Dwarves not being able to reach the buttons...

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 29)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-16T10:31:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <800dbb70-a54f-40d6-b747-7af41f6f1cee@t54g2000hsg.googlegroups.com> <W66dnYI8678M-c3VnZ2dnUVZ_gWdnZ2d@earthlink.com> <57aeac6f-5d14-46bd-8558-b3204c382af2@c58g2000hsc.googlegroups.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com>`

```
On Jun 14, 3:22 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> Sorry for the slow response.  I had a procedure in the hospital and they
> kept me there and extra day.

That you would help us so soon in understanding this speaks volumes of
you, Mr. Charles.

>
> The program simulates the elevator at tha Mathematics building at CalTech.
…[32 more quoted lines elided]…
> edition pp 279 -293.

That would be the _Fundamental Algorithms_ volume? Mr. Knuth is one
smart feller. As a grad student in Computer Science, I was assigned
and completed some of his 5, 10, 15, and maybe 20 or 25 point
"problems." We were all mortified at the 30 or 35 point problems.
There were always rumours that his 50 point problems were sometimes
"problems that had not yet been solved."

>
> At the time I was first exposed to this book as a reading assignment in
…[6 more quoted lines elided]…
> experiencing a great feeling of progress and accomplishment.

Very well, then Mr. Charles, I shall take your advice, and if upon
reading more of the contributions of Knuth and DocDwarf on Elevator
Simulations I still do not have full and complete understanding, then
I will "sleep on it" (maybe for quite a while) and do COBOL (maybe for
quite a while), and just trust that in due time, "it" will come to me.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-16T18:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g36a0g$hpu$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com>`

```
In article <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:

[snip]

>Very well, then Mr. Charles, I shall take your advice, and if upon
>reading more of the contributions of Knuth and DocDwarf on Elevator
>Simulations I still do not have full and complete understanding, then
>I will "sleep on it" (maybe for quite a while) and do COBOL (maybe for
>quite a while), and just trust that in due time, "it" will come to me.

Mr Shafer, with all respect due you and your opinions: it is my belief 
that I am unworthy of this association.  A period/full stop should have 
been placed after the name of Knuth.

(Yes, I know that structure was a bit tortured but to say 'Y is unworthy 
of being mentioned in the same sentence as X' mentions them in the same 
sentence.)

(at times I respond to 'May I ask you a question?' with 'You already have.  
Would you care to ask another?')

DD
```

###### ↳ ↳ ↳ Co-routines (was: Why read CLC?)

_(reply depth: 31)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-16T13:52:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mDy5k.629$oY2.589@newsfe21.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com>`

```
A most interesting discussion!

My understanding of "co-routines" is, as I mentioned at first, that there
exist two routines which proceed from start to finish (although one must
start first, of course), swapping control back and forth along the way, to
accomplish something or other; implying that each is aware of and relies on
the other: thus the "co-" in the name.  Now it may be I misunderstand the
concept, or it may be a lack of imagination on my part, but none of the
examples and discussions seem to me to demonstrate either a "true"
co-routine or a task that can best be accomplished by a co-routine.

Including this discussion, the Wiki articles, and whatever else I've read,
the examples given all seem to be some task that proceeds from start to
finish and only then hands off to some other routine.  Examples such as Unix
pipes are a little ambiguous; I always thought that pipes were such that the
output of one program would be directed to another as input, but only at
completion of the first program.  If instead control swaps after the
creation of an output record, it is definitely more co-routine-ish but
neither program needs to be aware of the other's existence: after all, it's
a matter of replacing the first program's "output device" with a program.
If I understand it correctly both the first and second programs perform an
i/o: program 1 writes a record (using standard system calls, I would think)
and the second reads a record which in this case comes from the first.
Whichever way the pipes work, neither program co-operates with each other in
the co-routine sense as I understand it.

System I/O routines were mentioned as possible candidates: the same
objection applies, I think, in that the routine that handles the hardware
level and the application routine that waits for the record to be read or
written do not co-operate: each assumes the existence of the other but need
know nothing about it (apart from the format of the system calls) or even if
it exists.

If a co-routine is in fact some piece of code that runs from entrance to
release of control and then waits for something to happen to regain control,
then any I/O-dependent program is a co-routine.  Any event-oriented (GUI)
program hands off control to the screen handler; the screen handler
classifies anything that happens and passes control to a calling program.
But again, neither the calling program or the screen handler needs to know
anything about the other.

The discussions I've read clearly indicate that the question is a fuzzy one
at best.  Definitions vary and candidates are suggested but I have yet to
see a definitive aha! at which point everyone agrees and goes to have a
beer.

It's significant, I think, that Constantine and Yourdon and Knuth et al saw
it necessary to indicate the existence of the co-routine as distinct from
the interrupt-driven, I/O release, etc., type programming already well
understood by that time; although it would seem that they failed to make it
clear what they meant.  Or, perhaps, they wanted to introduce a concept that
they could eat out on!  (Unworthy of me, I know, but Yourdon at least had a
very smug writing style).

And leaving aside the existence or not of co-routines, not one example makes
an unassailable case.  I know the elveator simulation is only an example for
discussion but for sure if I were writing it I wouldn't write it that way.
Any process that can create four or five different inputs would do for the
"persons" and the "floors": a random-number generator, wind-speed readings
taken every second at thirty different locations - even an A/R transaction
file would probably do!

Nonetheless, I have enjoyed reading all the comments and arguments.
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 32)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-16T12:44:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68770628-82df-405e-a567-75755c82d2c0@m45g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga>`

```
On Jun 16, 2:52 pm, "tlmfru" <la...@mts.net> wrote:
> A most interesting discussion!

> <summary deleted>

Well put, Mr. PL, though the only nit that I might pick with you is...

> ... I have yet to
> see a definitive aha! at which point everyone agrees and goes to have a
> beer.
>

Mr. PL, we reached _that_ aha! any number of times in this thread,
sort of along the lines of "Everyone needs to believe in Something. I
believe I'll have another beer!" :-)

Yours,
Ken
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 32)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-16T19:12:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y_CdnS_BNZ3GbsvVnZ2dnUVZ_uOdnZ2d@posted.mid-floridainternet>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga>`

```

"tlmfru" <lacey@mts.net> wrote in message
news:mDy5k.629$oY2.589@newsfe21.lga...
> A most interesting discussion!
>
…[3 more quoted lines elided]…
> accomplish something or other; implying that each is aware of and relies
on
> the other: thus the "co-" in the name.  Now it may be I misunderstand the
> concept, or it may be a lack of imagination on my part, but none of the
> examples and discussions seem to me to demonstrate either a "true"
> co-routine or a task that can best be accomplished by a co-routine.

"It is rather difficult to find short, simple examples of
coroutines which illustrate the importance of the idea;
the most useful coroutine applications are generally quite
lengthy." -- Donald E. Knuth, "The Art of Computer
Programming," Volume 1, Fundamental Algorithms,
Second Edition, 1973, page 191.

> Including this discussion, the Wiki articles, and whatever else I've read,
> the examples given all seem to be some task that proceeds from start to
> finish and only then hands off to some other routine.  Examples such as
Unix
> pipes are a little ambiguous; I always thought that pipes were such that
the
> output of one program would be directed to another as input, but only at
> completion of the first program.  If instead control swaps after the
> creation of an output record, it is definitely more co-routine-ish but
> neither program needs to be aware of the other's existence: after all,
it's
> a matter of replacing the first program's "output device" with a program.
> If I understand it correctly both the first and second programs perform an
> i/o: program 1 writes a record (using standard system calls, I would
think)
> and the second reads a record which in this case comes from the first.
> Whichever way the pipes work, neither program co-operates with each other
in
> the co-routine sense as I understand it.

It isn't in the application programs; it is in the implementation
of the "pipe". One routine captures 'stdout', the other supplants
'stdin', and these routines work together.

< http://www.csci.csusb.edu/dick/monograph/01_2.html >
-----
Co-Routines

If there is a tool that transforms a batch version into a real
time version then a batch version is a worthwhile prototype.
It is easy to speed up simple batch systems directly when
you use co-routines as in Conway's 1963 "Separable
Diagram Compiler" or the COBOL SORT verb. Knuth
traces co-routines back to 1958 [Knuth69]. Knuth, Floyd,
Dahl, and others have shown that co-routines can give
simpler solutions than subroutines [Knuth69] [Dahletal72]
[FloydinACM86] [ NON-SEQUENTIAL in subjects ]
They were mentioned in the original work on SD
[StevensMyersetal74] and Structured Programming
[Dahletal72] but then vanished from sight. Perhaps because
co-routines come in pairs and so it is not easy to use
them with hierarchical code.
-----
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 33)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-17T08:25:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5086dad-6643-43c8-ab93-cef1697705e1@d77g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <y_CdnS_BNZ3GbsvVnZ2dnUVZ_uOdnZ2d@posted.mid-floridainternet>`

```
On Jun 16, 7:12 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> "tlmfru" <la...@mts.net> wrote in message
>
…[10 more quoted lines elided]…
> Second Edition, 1973, page 191.

> <stuff deleted>

> It isn't in the application programs; it is in the implementation
> of the "pipe". One routine captures 'stdout', the other supplants
…[21 more quoted lines elided]…
>

Very helpful additions to the discussion and our understanding. Thank
you very much.

Interesting comment about the mention of co-routines in SD. Tickled my
memory just a bit, enough to point out, along with our observations on
the work of Constantine, that Wayne Stevens, and also Glen Myers, were
contributors to Structured Design.

See, for example,
http://www.reengineer.org/stevens/ .

and the 2007 recipient of the Stevens Award, Nicholas Zvegintzov -
http://reengineer.org/stevens/index2007.html ,
which also has a list of all previous Stevens Award recipients.

Ken
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 34)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-17T13:26:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsWdnZWXKsRUbsrVnZ2dnUVZ_obinZ2d@posted.mid-floridainternet>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <y_CdnS_BNZ3GbsvVnZ2dnUVZ_uOdnZ2d@posted.mid-floridainternet> <a5086dad-6643-43c8-ab93-cef1697705e1@d77g2000hsb.googlegroups.com>`

```

<klshafer@att.net> wrote in message
news:a5086dad-6643-43c8-ab93-cef1697705e1@d77g2000hsb.googlegroups.com...
>On Jun 16, 7:12 pm, "Rick Smith" <ricksm...@mfi.net> wrote:

[snip]

>> <http://www.csci.csusb.edu/dick/monograph/01_2.html>
>> -----
>> Co-Routines
>>
[snip]
>> They were mentioned in the original work on SD
>> [StevensMyersetal74] and Structured Programming
…[3 more quoted lines elided]…
>> ------

[snip]

>Interesting comment about the mention of co-routines in SD.

Perhaps more curious than interesting!

I retrieved a PDF copy of "Structured Design" at
< http://www.research.ibm.com/journal/sj/132/ibmsj1302C.pdf >,
searched it, and found no reference to "co-routine" or
"coroutine".
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 35)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-17T18:19:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g38v86$94i$1@reader2.panix.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <y_CdnS_BNZ3GbsvVnZ2dnUVZ_uOdnZ2d@posted.mid-floridainternet> <a5086dad-6643-43c8-ab93-cef1697705e1@d77g2000hsb.googlegroups.com> <gsWdnZWXKsRUbsrVnZ2dnUVZ_obinZ2d@posted.mid-floridainternet>`

```
In article <gsWdnZWXKsRUbsrVnZ2dnUVZ_obinZ2d@posted.mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><klshafer@att.net> wrote in message
…[5 more quoted lines elided]…
>>> <http://www.csci.csusb.edu/dick/monograph/01_2.html>

[snip]

>>Interesting comment about the mention of co-routines in SD.
>
>Perhaps more curious than interesting!

From http://dictionary.reference.com/browse/curious :

--begin quoted text:

3. arousing or exciting speculation, interest, or attention through being 
inexplicable or highly unusual; odd; strange:

--end quoted text

From http://dictionary.reference.com/browse/interesting :

--begin quoted text:

1. engaging or exciting and holding the attention or curiosity:

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Co-routines (was: Why read CLC?)

_(reply depth: 33)_

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2008-06-18T11:16:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73e4bc1a-a3ad-4162-892c-ebfff3111cc7@p25g2000hsf.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <y_CdnS_BNZ3GbsvVnZ2dnUVZ_uOdnZ2d@posted.mid-floridainternet>`

```
On Jun 16, 6:12 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> "tlmfru" <la...@mts.net> wrote in message
>
…[19 more quoted lines elided]…
> Second Edition, 1973, page 191.


In Cobol, sort input and output procedures are actually coroutines to
the sort.  Obviously this implements the typical producer/consumer
type of coroutine, and the coroutine switch happens at the release or
return.
```

###### ↳ ↳ ↳ Re: Co-routines

_(reply depth: 32)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-06-17T20:36:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3ascv02ir0@news2.newsguy.com>`
- **In-Reply-To:** `<mDy5k.629$oY2.589@newsfe21.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga>`

```
tlmfru wrote:
> Examples such as Unix
> pipes are a little ambiguous; I always thought that pipes were such that the
> output of one program would be directed to another as input, but only at
> completion of the first program.  If instead control swaps after the
> creation of an output record, it is definitely more co-routine-ish

It's neither, actually.

In a simple pipeline (there are other uses of pipes, but we'll ignore 
them for simplicity) like:

	ls | sort

what happens is something like this:

1. The shell creates a pipe, which has an "in" end and and "out" end. 
(Simple pipes in Unix are unidirectional.)

2. The shell creates a child process. The child process sets its 
output to the "in" end of the pipe, and executes "ls".

3. The shell creates another child process. The child process sets its 
input to the "out" end of the pipe, and executes "sort".

Note that the ordering of steps 2 and 3 is unimportant. Also, it's not 
guaranteed that one will finish before the other begins, because once 
the child process is created, the shell process continues.

When a child process is created, it's put on the run queue, and it 
will get a timeslice when it gets to the front of the queue.

If the "sort" process tries to read from the pipe before there's any 
data in it, it'll block. That is, it will go from the runnable state 
to the I/O-wait state. So it doesn't matter if sort gets going before 
ls does.

4. The "ls" process will start generating output (eventually). Its 
output is the pipe, which is just a buffer in the kernel. As ls writes 
output, the buffer starts to fill.

5. The kernel sees there's data in the pipe, so sort will no longer be 
blocked. So it switches it from I/O-wait to runnable and puts it on 
the run queue.

6. At this point a number of things can happen, in any order:
    6a. sort gets a timeslice and reads some data out of the pipe. 
Note that sort *has* to buffer all of its data (the record that will 
be first in the sorted output might arrive last in the input), so sort 
just reads and buffers.
    6b. ls fills up the pipe buffer (because sort hasn't gotten a 
timeslice yet, or because ls is faster, or whatever). ls tries to 
write more data and is blocked. It goes into I/O-wait.
    6c. sort drains the pipe buffer. It tries to read more and goes 
into I/O-wait.
    6d. ls and sort happen to stride just right, neither filling nor 
exhausting the pipe buffer as they run in their timeslices. They 
alternate running as they come up in the run queue.
    6e. This is a multiprocessor system, and ls and sort actually run 
simultaneously.

These things repeat as long as ls is running.

7. ls reaches the end of its output. It exits, closing its end of the 
pipe. Note that if the total output of ls is smaller than the pipe 
buffer (typically 4KB), this can happen before the sort process ever 
reads anything.

8. sort drains the last of the input from the pipe. It tries to read 
again, and gets an EOF indication, because the "in" end of the pipe 
has been closed.

9. sort does its thing, writes its output, and exits.

So both scenarios (one process runs to completion before the other 
does anything significant, or the two alternate) can appear, as can 
various others where the two processes stumble over each other and the 
pipe buffer, and go in and out of runnable state.

There's also the case where the process that's reading the pipe closes 
its end prematurely. (This happens frequently - eg you pipe the output 
of a program into "more", then quit more before the end of the 
output.) In that case, the writing process will receive SIGPIPE when 
it next tries to write to the pipe.

 > but
> neither program needs to be aware of the other's existence: after all, it's
> a matter of replacing the first program's "output device" with a program.

With a pipe, actually - the programs don't communicate directly (as 
they would with eg shared memory). But your general point is correct, 
and I wouldn't call programs communicating by IPC a good example of 
coroutines.
```

###### ↳ ↳ ↳ Re: Co-routines

_(reply depth: 33)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-18T07:54:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<304fc11a-3d21-47a2-823d-e84522e41ceb@m45g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <g3ascv02ir0@news2.newsguy.com>`

```
On Jun 17, 3:36 pm, Michael Wojcik <mwoj...@newsguy.com> wrote:

<< very good description of unix pipes snipped >>

> With a pipe, actually - the programs don't communicate directly (as
> they would with eg shared memory). But your general point is correct,
> and I wouldn't call programs communicating by IPC a good example of
> coroutines.
>

With a little help from Google, namely

http://homes.ieu.edu.tr/~bhnich/CS305/Ch13.ppt#5http://homes.ieu.edu.tr/~bhnich/CS305/Ch13.ppt#5,

which says, in part,
"Coroutines have a single thread of control"

and
http://www.cs.cornell.edu/Courses/cs414/2005sp/lectures/11-syncproblems.ppt#2

which sets forth, in part, an example of solving the producer-consumer
problem with shared memory and semaphores (and also talks about unix
pipes);

and
http://groups.google.com/group/comp.os.research/browse_thread/thread/91873810cda3f535/e1d600f748fabb97?lnk=st&q=#e1d600f748fabb97

which says,
"Systems which are non-pre-emptive and may only ever have a single
active flow of control (regardless of the number of processors
available) are referred to as coroutine systems.  Coroutine
programming requires quite a different approach from threads-based
programming, as many of the synchronisation and resource-sharing
problems which occur in threaded environments need never trouble the
coroutines programmer."

So, Michael, let me see if my understanding is correct, in your
view...

Producer/Consumer problems may be solved with either IPC/
multithreading or coroutines.

Coroutines are single-threaded solutions to the producer/consumer
problem, relying on a CALL/RETURN within a single executable which
provides the synchronization.

IPC producer/consumer tasks are threads-based and do not make "calls"
- they must have additional synchronization and resource-sharing
primitives to accomplish the same (such as shared memory and
semaphores, or perhaps message passing).

So (probably) all (most?) of coroutines have a producer/consumer
aspect to them, but not all producer/consumer problems are solved by
coroutines. Some are solved by IPC.

Is this right?

What would we call the IPC producer/consumer tasks if not
"coroutines"? Would we call them "cooperative processes"?

Ken
```

###### ↳ ↳ ↳ Re: Co-routines

_(reply depth: 34)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-06-20T09:32:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3fvkh02q8m@news2.newsguy.com>`
- **In-Reply-To:** `<304fc11a-3d21-47a2-823d-e84522e41ceb@m45g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <g3ascv02ir0@news2.newsguy.com> <304fc11a-3d21-47a2-823d-e84522e41ceb@m45g2000hsb.googlegroups.com>`

```
klshafer@att.net wrote:
> http://groups.google.com/group/comp.os.research/browse_thread/thread/91873810cda3f535/e1d600f748fabb97?lnk=st&q=#e1d600f748fabb97
> 
…[7 more quoted lines elided]…
> coroutines programmer."

I'd just add here that you have to be careful with these definitions. 
They're not standardized, and practitioners don't always agree on them 
(which is probably not surprising).

So, for example, there are a number of non-preemptive threading 
implementations that are still referred to as "threaded environments" 
by their developers, even though they'd be "coroutine systems" under 
the definition above.

> So, Michael, let me see if my understanding is correct, in your
> view...
> 
> Producer/Consumer problems may be solved with either IPC/
> multithreading or coroutines.

I'd generalize that a bit.

You can have only one active flow of control, or you can have 
multiple. You can have multiple flows of control with shared resources 
(threads with preemptive multitasking, or multiple processes using 
shared memory) or with separated resources (multiple processes with 
some other form of IPC that's serialized by the OS).

There are ways to implement Producer/Consumer architectures in any of 
those environments.

Coroutines use a single active flow of control. Another P/C option for 
a single active flow of control is to run the producer to completion 
first, buffering all of its output, and then to run the consumer; 
that's actually quite common in batch processing, even on PCs. 
(Toolchains for building software often work that way, for example.) 
That's also how pipes worked in MS-DOS - something like "dir | find" 
would write the output from the "dir" command to a temporary file, 
then run the "find" command against the contents of that file, then 
delete the file.

> Coroutines are single-threaded solutions to the producer/consumer
> problem, relying on a CALL/RETURN within a single executable which
> provides the synchronization.

That's one possibility. Various environments provide various options. 
In most assembly environments, for example, you can use non-local 
branches to implement coroutines: the program just jumps back and 
forth between unrelated sections of code. In CICS, you have XCTL 
(transfer control). Scheme has continuations, which let you package up 
the current processing state in order to resume it later.

You can also implement logical coroutines within a single function (or 
"procedure", or "program", depending on the terminology you prefer) 
with a state machine. Typically that's a loop around an alternation 
statement (in COBOL, a PERFORM UNTIL around an EVALUATE). The machine 
has states for "coroutine 1" and for "coroutine 2".

> IPC producer/consumer tasks are threads-based and do not make "calls"
> - they must have additional synchronization and resource-sharing
> primitives to accomplish the same (such as shared memory and
> semaphores, or perhaps message passing).

They don't have to be based on threads necessarily. They could be two 
separate processes, for example.

> So (probably) all (most?) of coroutines have a producer/consumer
> aspect to them, but not all producer/consumer problems are solved by
> coroutines. Some are solved by IPC.
> 
> Is this right?

There might be appropriate applications for coroutines that aren't 
really producer/consumer, but none come to mind at the moment.

> What would we call the IPC producer/consumer tasks if not
> "coroutines"? Would we call them "cooperative processes"?

I don't think there's any commonly-used term to cover all the 
non-coroutine P/C designs. Most people just say "threads" or 
"processes" as appropriate.
```

###### ↳ ↳ ↳ Re: Co-routines

_(reply depth: 35)_

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2008-06-20T14:52:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12be7525-e3fa-46c9-a3c7-9bbd74f3508f@z66g2000hsc.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <g2sh2i$d7o$1@reader2.panix.com> <2qGdnaJHmOjIh8nVnZ2dnUVZ_h7inZ2d@earthlink.com> <ae4e5b4e-88a9-4d1c-948e-70e5a0644d5a@d45g2000hsc.googlegroups.com> <g36a0g$hpu$1@reader2.panix.com> <mDy5k.629$oY2.589@newsfe21.lga> <g3ascv02ir0@news2.newsguy.com> <304fc11a-3d21-47a2-823d-e84522e41ceb@m45g2000hsb.googlegroups.com> <g3fvkh02q8m@news2.newsguy.com>`

```
On Jun 20, 3:32 am, Michael Wojcik <mwoj...@newsguy.com> wrote:
> I'd just add here that you have to be careful with these definitions.
> They're not standardized, and practitioners don't always agree on them
…[5 more quoted lines elided]…
> the definition above.


It is, of course, trivial to build a non-preemptive threading package
on top of coroutines (in short, every thread is a coroutine to the
dispatcher).  It's also trivial to emulate coroutines on top of
threads by giving each coroutine a semaphore, and moving a single
“run” signal around from semaphore to semaphore at the coroutine
switches.  Under the hood that doesn't look much like traditional
coroutines, but the end result is just the same.

I'd say the critical issue distinguishing a non-preemptive thread from
a coroutine is that in the later case the control flow switches
directly to the other coroutine, whereas with threads, you don't know
which thread is going to be dispatched after you release control
(assuming more than one is runnable, and you don't have detailed
knowledge of the dispatcher's processes).


> There might be appropriate applications for coroutines that aren't
> really producer/consumer, but none come to mind at the moment.


Coroutines are often used to implement state machines, although
arguably that more thread-like.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T08:16:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga>`

```
On Jun 8, 12:38 pm, "tlmfru" <la...@mts.net> wrote:
> Since Yourdon & Constantine have been invoked in this discussion - I have a
> question about a concept that turned up in their publications.  This was
…[6 more quoted lines elided]…
> PL

Hi, tlmfru/PL,

Posted directly under you, but with recognition of what Mr. Pete D.
and Mr. Charles H. have already said... here is what I remember about
co-routines...

Probably have their origin in the FORTRAN world, though as Pete points
out can be hosted in other languages. Since FORTRAN has
"subroutines" (and not "subprograms", or "procedures", or whatever",
that is probably why they are called co-ROUTINES.

Pete, do you know if much of SCOPE was written in FORTRAN? I had
always heard that much (even most) of KRONOS was written in FORTRAN
(that is where I cut my computer teeth.)

Anyway, to the structure of them - this is what I remember from
Computer Science about 30-35 years ago... memory is hazy, other
contributors welcome to correct me if I don't have exactly right.

Co-Routines are "peer" routines that exist in a sort of Master-Slave
relationship, with each one thinking it is the master and the other
the slave.

Classic Example: The Producer / Consumer problem. One routine is
responsible for "producing" something (like a "record"), and the other
is responsible for "consuming" it.

Sequence goes something like this... both of them are subroutines in
the FORTRAN sense, but in their interaction, they are co-routines...
Names are limited to seven characters or less :-).
    Subroutine prodrec (record)
C comment - produces a record, then consumes it
    <do some stuff to build a record>
    Call consrec (record)
999 return
    end

    Subroutine consrec (record)
C comment - consumes a record, then asks for another
    <do some stuff to dispose of record>
    Call prodrec (record)
999 return
    end

Notice that the return statements are never executed, unless we allow
for an "exceptional event" and a conditional RETURN, or the evil GOTO
999.

As far usefulness, I think I was told something about Input-Output
transformers and the like, where one routine reads from a slow-device,
like a card-reader, and the other routine writes to a fast-device,
like a disk or drum, and so the co-routines serve a "buffering" role.
I remember being told that "buffering" helps conpensate differences in
device speed, and "blocking" helps compensate for storage efficiency
(back when the inter-record gap on a mag tape took up a significant
stretch of the tape.)

Maybe in some OS's they could be made separately schedule-able tasks
that could be given different priorities, thus helping with load
balancing within the OS. That is speculation on my part.

I can't recall if I had occasion to use co-routines. I don't think so.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T10:14:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<03ee5e39-07b8-4688-a1a6-fe89c641d4d2@d77g2000hsb.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com>`

```
On Jun 9, 11:16 am, "klsha...@att.net" <klsha...@att.net> wrote:
> Sequence goes something like this... both of them are subroutines in
> the FORTRAN sense, but in their interaction, they are co-routines...
…[17 more quoted lines elided]…
> 999.

Hmmmm... upon re-reading this, I don't think I got it "just right." In
the above, wouldn't the "return addresses" be stacked, and because the
stack was never "popped", eventually this would cause a run-time
error?

There must have been a way to do the RETURNs, and still let each of
the other subroutines invoke the other as if it were a slave. I have a
vague recollection that it involved the use of a "switch" variable,
which had the effect of determining the "entry point" within each
routine. Ya'll are welcome to refresh my memory, if deemed worthwhile.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-09T12:49:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t1e3k.5101$yi.5014@newsfe13.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com> <03ee5e39-07b8-4688-a1a6-fe89c641d4d2@d77g2000hsb.googlegroups.com>`

```

<klshafer@att.net> wrote in message
news:03ee5e39-07b8-4688-a1a6-fe89c641d4d2@d77g2000hsb.googlegroups.com...
On Jun 9, 11:16 am, "klsha...@att.net" <klsha...@att.net> wrote:
> Sequence goes something like this... both of them are subroutines in
> the FORTRAN sense, but in their interaction, they are co-routines...
…[17 more quoted lines elided]…
> 999.

Hmmmm... upon re-reading this, I don't think I got it "just right." In
the above, wouldn't the "return addresses" be stacked, and because the
stack was never "popped", eventually this would cause a run-time
error?


PL> There is another way to handle "return addresses" which doesn't use this
new-fangled "stack" concept (<g>); that is, the first thing the routine does
upon entry is to save the return address (typically contained in a register)
at some "save-retrun-address"  location which it controls.  When ready to
return, this "save-return-address" is retrieved and the routine transfers to
that location.

Thus there never would be an overflow since only one memory location is used
per routine.  And, obviously, if the rule is strictly followed that each
save location belongs to one routine and is never used for or by anything
else, "nothing can go wrong".  Works very well.  Has done for decades.

I think I first heard about stacks round about the time of DEC: the PDP line
in particular.

PL
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-10T12:59:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b61voF3b9ap7U1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com> <03ee5e39-07b8-4688-a1a6-fe89c641d4d2@d77g2000hsb.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:03ee5e39-07b8-4688-a1a6-fe89c641d4d2@d77g2000hsb.googlegroups.com...
On Jun 9, 11:16 am, "klsha...@att.net" <klsha...@att.net> wrote:
> Sequence goes something like this... both of them are subroutines in
> the FORTRAN sense, but in their interaction, they are co-routines...
…[17 more quoted lines elided]…
> 999.

Hmmmm... upon re-reading this, I don't think I got it "just right." In
the above, wouldn't the "return addresses" be stacked, and because the
stack was never "popped", eventually this would cause a run-time
error?

There must have been a way to do the RETURNs, and still let each of
the other subroutines invoke the other as if it were a slave. I have a
vague recollection that it involved the use of a "switch" variable,
which had the effect of determining the "entry point" within each
routine. Ya'll are welcome to refresh my memory, if deemed worthwhile.

[Pete]

You may be getting confused with "serial reusability" which used an 
indicator value to select an entry point. This was a "poor man's 
re-entrancy" which could be used in COBOL environments, even though COBOL 
did not support true re-entrancy.(To do so would require saving and 
restoring registers, and the instruction counter...) IMS DC in the IBM 
mainframe environment used this for resuming conversations with 3270 screens 
in conversational mode. It was very efficient and a good solution, but fell 
into disfavour because it required a GO TO... DEPENDING ON ... :-) (and the 
TP software moved on as well...)

I have seen the same approached used on other platforms, where multiple 
threads can use the same piece of code, within a clearly defined set of 
boundaries. Once a thread gets the code, it executes it up to the boundary 
(always just preceding a referenceable label), dequeues, then re-enters when 
it is re-activated and carries on from the label until the next boundary... 
hence, "serial reusability". These are not co-routines.

(If the code was TRULY re-entrant and reusable, it would be interruptible at 
ANY point, and could resume from the immediately following instruction, 
wthout needing an "entry point" or label at that place in the code.   This 
is pretty much the "exchange jump" mechanism I described earlier for the 
Cyber.)

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-09T12:42:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mXd3k.5100$yi.353@newsfe13.lga>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com>`

```

<klshafer@att.net> wrote in message
news:d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com...
On Jun 8, 12:38 pm, "tlmfru" <la...@mts.net> wrote:
>> Since Yourdon & Constantine have been invoked in this discussion - I have
a
>> question about a concept that turned up in their publications. This was
>> "co-routines" - two or more definable routines (i.e., having a start and
a
>> finish) that continuously swapped control between themselves to
accomplish
>> some task or other. I never understood the swapping mechanism (not
>> important, I suppose) and I never could imagine a task that would or
could
>> be handled like that. Anybody have any experience with these?
>>
>> PL

>Anyway, to the structure of them - this is what I remember from
>Computer Science about 30-35 years ago... memory is hazy, other
…[4 more quoted lines elided]…
>the slave.

>Classic Example: The Producer / Consumer problem. One routine is
>responsible for "producing" something (like a "record"), and the other
>is responsible for "consuming" it.

>Sequence goes something like this... both of them are subroutines in
>the FORTRAN sense, but in their interaction, they are co-routines...
…[6 more quoted lines elided]…
>    end

>    Subroutine consrec (record)
>C comment - consumes a record, then asks for another
…[3 more quoted lines elided]…
>    end

My memory is also less than perfect, but this doesn't conform to what I do
remember.  There was a diagram that showed control going from top to bottom
in each of the co-routines, BUT jumping from one to the other any number of
times along the way.  Your example shows each routine essentially going from
start to finish before jumping to the other.

>As far usefulness, I think I was told something about Input-Output
>transformers and the like, where one routine reads from a slow-device,
…[5 more quoted lines elided]…
>stretch of the tape.)

Hmm.  As I recall this was allwed for by hardware interrupts: I/O operated
to/from a particular memory area called a buffer; after each transfer
(signalled by a particular flag which was set) there was an interrupt which
the I/O routine had to service; for input functions it moved the contents of
the buffer to the memory space of the program that wanted it; for output, it
made sure that the operation had completed successfully and prepared for the
next output operation.  It's a lot more complicated than that: there were
multiplexor channels for slow devices, which could run several transfers
simultaneously (not actually, of course, but it looked like it), and
selector channels for high-speed devices - one transfer at a time.  To
control all that there were byte-transfer interrupts, mostly at the hardware
level.  Blocking did indeed improve utilization of the medium, and speeded
the programs up.

Anyway, I can't recall that >>routines<< compensated for I/O speeds: each
I/O handler operated independently of all others and only got fancy if it
had to handle multiple devices of the same type (tape or disc drives,
fr'instance).

Interesting thoughts, though.

PL/The Legendary Man from Un.  (Un is not Wigan.  You have to be English to
understand).
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T11:00:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<785f1184-1e74-42ce-a8fd-12a7331ea1db@34g2000hsf.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com> <mXd3k.5100$yi.353@newsfe13.lga>`

```
On Jun 9, 1:42 pm, "tlmfru" <la...@mts.net> wrote:
> <klsha...@att.net> wrote in message
>
…[8 more quoted lines elided]…
> start to finish before jumping to the other.

Yes, some of the fog accumulated from years past has begun to lift. I
do now seem to remember the flow as "jumping from one to the other any
number of times along the way." The example that I gave was incorrect.
No matter. It was sufficient to jar your memory so that you could
offer a more correct one...


> Hmm.  As I recall this was allwed for by hardware interrupts: I/O operated
> to/from a particular memory area called a buffer; after each transfer
…[18 more quoted lines elided]…
>

Made more complicated by the fact that the CDC architecture used
Peripheral Processor Units (PPUs) to handle the IO. We were told they
were the real Masters of the system. The CPU was actually a slave. It
did nothing until PPU permitted it to do so, somehow.

...

So maybe we never did answer the question - what was the _use_ of
these co-routines?


> PL/The Legendary Man from Un.  (Un is not Wigan.  You have to be English to
> understand).- Hide quoted text -

PL-eased to meet ya ...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-10T12:42:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b60uqF3a1qt9U1@mid.individual.net>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:d2639c03-667e-409a-85ba-314941e45856@x41g2000hsb.googlegroups.com...
On Jun 8, 12:38 pm, "tlmfru" <la...@mts.net> wrote:
> Since Yourdon & Constantine have been invoked in this discussion - I have 
> a
…[7 more quoted lines elided]…
> PL

Hi, tlmfru/PL,

Posted directly under you, but with recognition of what Mr. Pete D.
and Mr. Charles H. have already said... here is what I remember about
co-routines...

Probably have their origin in the FORTRAN world, though as Pete points
out can be hosted in other languages. Since FORTRAN has
"subroutines" (and not "subprograms", or "procedures", or whatever",
that is probably why they are called co-ROUTINES.

Pete, do you know if much of SCOPE was written in FORTRAN? I had
always heard that much (even most) of KRONOS was written in FORTRAN
(that is where I cut my computer teeth.)

[Pete]

I believe SCOPE was written in COMPASS, the Cyber Assembler. But I can't be 
sure. It doesn't surprise me to hear that KRONOS was written in FORTRAN. 
FORTRAN was much beloved by CDCers... :-)

In the early 1970s the Professional Services division of CDC were trying to 
establish a COBOL "presence" within the Australian subsidiary. I was 
involved in that and my Boss was very successful in getting it set up. After 
it took off, I was seconded to the new NZ subsidiary as a pre-sales analyst 
and support consultant. I remember those times with fondness. The guy I was 
supporting was one of the best computer salesmen I have ever encountered and 
he taught me much. He pulled off some amazing marketing coups... (NZ TAB 
(national online betting system), replacement of IBM 3330s with plug 
compatible CDC equivalents at a prestige IBM site, and setting up the first 
public bureau satellite link between Australia and NZ. All very interesting 
and educational for me... :-))

There were still a limited number of Business oriented analysts within the 
company and demand for their services was increasing, so I was constantly 
being forced to pack a bag and be somewhere at the drop of a hat. (Mainly 
USA or Oz...) It played Hell with my relationship at the time and in the end 
I had to choose, so I quit the company (reluctantly...).

<snipped a very good explanation of co-routines>

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-09T23:23:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IaadncBFmOUAbtDVnZ2dnUVZ_hudnZ2d@posted.mid-floridainternet>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga>`

```

"tlmfru" <lacey@mts.net> wrote in message
news:TUT2k.163$Jh7.149@newsfe21.lga...
> Since Yourdon & Constantine have been invoked in this discussion - I have
a
> question about a concept that turned up in their publications.  This was
> "co-routines" - two or more definable routines (i.e., having a start and a
…[3 more quoted lines elided]…
> be handled like that.  Anybody have any experience with these?

I did a bit of searching and found one site that mentioned
the COBOL SORT statement as a use of coroutines.
Once the sort is initiated, the input and output procedures,
in turn, swap control with the sort routine.

I think another case would be Report Writer with its
INITIATE and TERMINATE statements to establish
and end the Report Writer routine and the GENERATE
statement to relinquish control to Report Writer.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-06-10T09:10:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2l9d1$k7i$1@nntp.fujitsu-siemens.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga>`

```
"tlmfru" <lacey@mts.net> schrieb im Newsbeitrag 
news:TUT2k.163$Jh7.149@newsfe21.lga...
> Since Yourdon & Constantine have been invoked in this discussion - I have 
> a
…[6 more quoted lines elided]…
>
No own experience, but many many years ago there was a then popular book by 
Michael Jackson 'Structured COBOL programming' (hope I remember the title 
correctly): He proposed that the program structure should reflect the 
structure of input and output data; he analyzed various cases, where this 
was not possible or such an attempt resulted in 'bad' programs: one of the 
diagnosed reasons was 'incompatibility' of input and output data, a 
situation he called *structure clash*. He proposed soulutions independent of 
the concrete problem (similar to 'patterns' in OO, 'discovered' many years 
later!). One of the universal solutions used coroutines - without 
appropriate COBOL language constructs, his examples did simulate the 
coroutines using a main- and a sub-program with a state variable and many go 
to statements.

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:42:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9dd742d-1346-4d39-9c9b-74924565e631@t54g2000hsg.googlegroups.com>`
- **References:** `<g269ei$ho7$1@reader2.panix.com> <6aunafF384hkiU1@mid.individual.net> <g2gjl3$6n9$1@reader2.panix.com> <6b22tnF35niqdU1@mid.individual.net> <g2gksl$3t9$1@reader2.panix.com> <TUT2k.163$Jh7.149@newsfe21.lga> <g2l9d1$k7i$1@nntp.fujitsu-siemens.com>`

```
On Jun 10, 3:10 am, "Karl Kiesel" <Karl.Kie...@fujitsu-siemens.com>
wrote:
> No own experience, but many many years ago there was a then popular book by
> Michael Jackson 'Structured COBOL programming' (hope I remember the title
…[9 more quoted lines elided]…
> to statements.

Yes, I think I read some of Michael Jackson's work (the computer guy,
not the dancer/entertainer :-) ), but that was quite a while ago. And
yes, I remember his notion of "structure clash."

Some of this is beginning to fit together better in my mind now. I
think an example of "structure" clash was in doing a device-to-device
copy, as in copying disk binary file to 80-column card, or vice versa
(once upon a time, such things were necessary, were they not?) We had
a data clash, because the record lengths did not match up (disk sector
vs. 80-columns). I have a vague recollection of my computer science
instructor telling me that co-routines were a way of compensating for
differences in "physical record units" between two devices.

That this might be remarked upon by Constantine, would be, I think, in
his discussion of "transform centered design", and his "afferent" and
"efferent" modules. (One was output only, the other input only, don't
recall which was which and don't have my copy handy).

Recalling what the data flow diagrams looked like in "transform
centered design", they do remind me of the Unix "piping".

Ken

>
> Karl Kiesel
> Fujitsu Siemens Computers, München
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-06T19:31:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com>`
- **References:** `<Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com>`

```
On Fri, 6 Jun 2008 13:18:48 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jun 5, 8:12ï¿½pm, Robert <n...@e.mail> wrote:
>> On Thu, 5 Jun 2008 12:24:54 -0700 (PDT), "klsha...@att.net" <klsha...@att.net> wrote:
…[36 more quoted lines elided]…
>"offending" batch program.

How do bad programmers achieve such concord? Is there a book: Crap Code in 24 Hours? They
act like there's an unwritten 'standard' and are offended by programmers who don't know or
follow it. 

It's funny to get two of them in a room and ask about something borderline.
"What about 88s? Are they ok to use or not?" Then watch them argue, each confident that
his opinion is Universal Truth carved in stone.  

>Another tidbit I remember from Constantine: "indicators" are the type
>of element that he would call "control coupling", because it passes
…[3 more quoted lines elided]…
>of elements, which he called "data coupling".

I didn't get the idea from Constantine, but am pleased to see confirmation. Control
coupling is exactly the right term.

>Generally, you wish to eliminate control coupling, and minimize data
>coupling. I believe I have heard this called elsewhere as "starving
>the interface", if I understood it incorrectly.

Starving the interface is a bad idea. Rather than passing four data structures, they'll
copy the data of interest into a single structure. In the worst case, they'll pass it with
EXTERNAL rather than as a parameter (says he, sticking his finger in his throat and
gagging). 

>It has proven a real challenge to understand a 13,000 LOC batch
>program written in such a style.

That's nothing. Serious bad programmers round the size to hundreds of thousands of lines. 

I worked at a place where I got to rewrite 1,000+ bad programs. The AVERAGE ratio between
after and before was 50%. Half the bad code was superfluous. Even I was surprised. I would
have guessed 20%. Average execution speed increased 30%. Bottom line, total IT expense was
reduced $6M per year. 

It's much easier today. You can achieve that kind of efficiency by simply replacing the
mainframe with a Unix box. Bad guys will say it ain't so, but they know it is.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-07T18:09:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6aun0nF39kcpkU1@mid.individual.net>`
- **References:** `<Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com...
> On Fri, 6 Jun 2008 13:18:48 -0700 (PDT), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[46 more quoted lines elided]…
> How do bad programmers achieve such concord?

"good" and "bad" are moral terms that have nothing to do with programming, 
however, it is pedantic to insist on this and, as I fully understand what 
you mean, I won't...:-)

Certainly some code is perceived to be "better" than other code, but what 
does that statement really mean? The criteria by which code is "judged" are 
usually subjective, and you will often find that the person reviewing it has 
different criteria from the person who wrote it. All of us are affected by 
our education and experience in computer programming, but that education and 
experience is NOT the same for all. Neither are the local parameters at the 
time the code was written.

Is someone a "bad" programmer because they don't understand the formal 
definition of coupling (control or otherwise), but they saw indicators used 
in some code they had to mantain and thought it was a useful way to 
"remember" conditions without needing to retest data buffers for the 
duration of the thread? If the program works fine, how can it be "bad"? Some 
people would argue that a semaphore driven process can be generalized much 
more easily than one that isn't. Are they wrong? (Although you admitted that 
you have a problem with Boolean operations, Robert, some of us don't, and 
are quite happy to use complex sets of ones and zeros to drive a process... 
Certainly, I don't do this as a matter of course, but I have done so where 
the occasion warranted it (process control in an oil refinery))

Different criteria.

There is a certain smugness in deciding that the way in which you do 
something is the ONLY way.

It never ceases to amaze me how passionate some programmers become about 
details of coding style.

It's only computer code, not life and death.

For me now, past arguments about the merits or demerits of certain COBOL 
constructs can be seen in perspective, and I realize how futile they were.

All contractors, instead of denigrating their colleagues as "bad" 
programmers, should give thanks to the gods f Mammon that there is such an 
opportunity to fix stuff...:-)


>Is there a book: Crap Code in 24 Hours?

There doesn't need to be. Less than optimum practice gets perpetuated 
through restrictive shop standards that cater for the lowest common 
denominator of skill. Having no clear statement in the sandards as to what 
the coding priorities are, simply leads people to assume subjective ones. 
(On the several occasions when I have been required to formulate site 
standards in my life, I have always started with a list of what the 
priorities are that code should achieve. (Unsurprisingly, the fact that it 
must work correctly, is always number 1.... :-)))


>They
> act like there's an unwritten 'standard' and are offended by programmers 
…[7 more quoted lines elided]…
> his opinion is Universal Truth carved in stone.

To me the important thing here is the attitude they exhibit, rather than 
what they are actually arguing about.

>
>>Another tidbit I remember from Constantine: "indicators" are the type
…[12 more quoted lines elided]…
>>the interface", if I understood it incorrectly.

I betcha Constantine never worked on the shop floor in a large commercial 
COBOL shop. :-)

While I have no issue with his statements (and at least he had the grace to 
explain why he believed they were important), I wouldn't get unwrapped about 
code not adhering to it either. We don't live in a perfect world and people 
do the best they can under pressure.

>
> Starving the interface is a bad idea. Rather than passing four data 
> structures, they'll
> copy the data of interest into a single structure.

I do that all the time and have never suffered from doing so.  I have a 
single interface block. It contains "to" and "from" areas and is always 
passed by reference.  I don't like interfaces anyway and would mch rather 
see properties being used for data, but sometimes it makes sense. Why do you 
believe it is better to pass four parameters than one?


>In the worst case, they'll pass it with
> EXTERNAL rather than as a parameter (says he, sticking his finger in his 
…[4 more quoted lines elided]…
>>program written in such a style.

OR... it has been an interesting and useful interaction with the real world 
and a sample of things to come. There is a satisfaction in applying skill to 
make things better... think about it.

>
> That's nothing. Serious bad programmers round the size to hundreds of 
> thousands of lines.
>

Size, per se, is not necessarily "bad". (Certainly, a very large program has 
more propensity for being "sub-optimum" ...) A large, integrated, monolithic 
batch program, for example, can be much more efficient than a number of 
dynamically loaded modules. (However, it will suffer in other areas... 
multithreading, maintenance, etc. The point is that there are few blacks and 
whites if a program achieves the desired results. Insisting on blacks and 
whites and deciding that anything which isn't is "bad", says more about the 
perspective of the commentator than it does about any intrinsic value of the 
program code.

(If, indeed, program code can actually have an intrinsic value...if seven 
programmers all arrive at a correct solution to the same problem, using 
seven different programs, how is one of them any more intrinsically valuable 
than the other six? It isn't. Any such (unnecessary) judgement is simply 
subjective).

> I worked at a place where I got to rewrite 1,000+ bad programs.

Really? I would've written a program to either do or help me do that. Life's 
too short... :-)


> The AVERAGE ratio between
> after and before was 50%. Half the bad code was superfluous. Even I was 
…[3 more quoted lines elided]…
> reduced $6M per year.

And what percentage of that 6M saving did your grateful employer pass on to 
you? (rhetorical...)

I saved a company $200,000 with an idea and a program I wrote back in 1967. 
My Boss said the CEO had authorised for me to receive a $5 raise. I told 
them to shove it, quit, and went off and got my very first contract in NZ. 
:-)

>
> It's much easier today. You can achieve that kind of efficiency by simply 
> replacing the
> mainframe with a Unix box. Bad guys will say it ain't so, but they know it 
> is.

Guess I must be a Bad Guy then. I believe "crap code" is not endemic to any 
particular platform. (I'm not saying it is platform independent, but that's 
a whimsical idea :-))

BOTTOM LINE: "crap code " is a fact of life, but usually it is subjective 
judgement that makes it so (obviously, the person who wrote it didn't think 
it was crap code...). What is much more important than crap code is how you 
react to crap code. Slagging off colleagues you never even met, persuading 
everyone how incredibly right you always are, and what a hero you must be 
for handling this steaming pile and whipping it into fertilizer, may do 
wonders for your ego and self-image, it might even help you to feel much 
superior to the people who perpetrated the code, but at the end of the day, 
the code gets fixed and someone, somewhere, produces more of it. Not from 
malevolence or the desire to see you rant, but through lack of knowing any 
better, or simply subjectively disagreeing with your assessment, which never 
was Holy Writ. Programming is arguable and depends on subjective criteria. 
Deal with it; that's what they pay you for.

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 13)_

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2008-06-07T11:52:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5aec9453-7c5c-4b88-a9a4-3931b9ca4b82@d1g2000hsg.googlegroups.com>`
- **References:** `<Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net>`

```
On 7 Jun, 07:09, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[237 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I agree. I would add that it is possible to program both well or badly
in a variety of styles, languages and platforms.

Robert
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-07T21:11:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net>`

```
On Sat, 7 Jun 2008 18:09:25 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>Certainly some code is perceived to be "better" than other code, but what 
>does that statement really mean? The criteria by which code is "judged" are 
>usually subjective, and you will often find that the person reviewing it has 
>different criteria from the person who wrote it. 

We judge some countries, cities, cooking, beverages and automobiles better than others.
Our ranking has nothing to do with morality, it is about quality. 

>All of us are affected by 
>our education and experience in computer programming, but that education and 
>experience is NOT the same for all. Neither are the local parameters at the 
>time the code was written.

The best code I've seen was written by a high school student; the worst was written by a
man with a PhD in computer science and 30 years of experience. 

>Is someone a "bad" programmer because they don't understand the formal 
>definition of coupling (control or otherwise), but they saw indicators used 
>in some code they had to mantain and thought it was a useful way to 
>"remember" conditions without needing to retest data buffers for the 
>duration of the thread? If the program works fine, how can it be "bad"?

If an automobile transports you from A to B, how can it be bad? Ask anyone who bought a
Yugo or a 1960s era British car. 

>There is a certain smugness in deciding that the way in which you do 
>something is the ONLY way.

You have it backwards. Good programmers do not insist their way is the only way, BAD
programmers are the ones who do that. They call it Shop Standards. The standards are
sometimes written, but often are not. Programmers are expected to 'just know' what they
say. 

Who wants shop standards? Bad programmers. They are lying when they say management wants
them. Who enforces shop standards? The same bad programmers, with religious zeal and
certainty. 

>It never ceases to amaze me how passionate some programmers become about 
>details of coding style.
>
>It's only computer code, not life and death.

For bad programmers, it's the fear of being caught in a lie. They fear being found out and
demoted to a menial job.

>>Is there a book: Crap Code in 24 Hours?
>
…[7 more quoted lines elided]…
>must work correctly, is always number 1.... :-)))

My number 1 is "Design top-down, program bottom-up. Learn to tell the difference."
When people try to do everything in one mode exclusively, the result is junk. For
programmers, the danger is trying to design bottom-up. Most visionaries try to do
everything top-down, and to trivialize programming. 

>>They
>> act like there's an unwritten 'standard' and are offended by programmers 
…[10 more quoted lines elided]…
>what they are actually arguing about.

It's the attitude of religious believers who think they have Truth on their side and are
terrified of being wrong. I don't find it interesting, I find it ignoble. It's an
evolutionary trait that got mankind through a million years of uncertainty.

>>>Another tidbit I remember from Constantine: "indicators" are the type
>>>of element that he would call "control coupling", because it passes
…[14 more quoted lines elided]…
>COBOL shop. :-)

# Professor, Department of Mathematics & Engineering, University of Madeira, Funchal,
Portugal [2006 --]
# Director, Laboratory for Usage-Centered Software Engineering, University of Madeira,
Funchal, Portugal [2006 --]
# Chief Scientist, Principal Consultant, Constantine & Lockwood, Ltd. [1993 --]
# Professor of Information Technology, University of Technology Sydney, Australia. [1994 -
2003]
# Independent Consultant. [1987 - 1993]
# Clinical Supervisor, Adolescent and Family Intervention, LUK, Inc., Fitchburg, Mass.
[1984 - 1986]
# Assistant Professor of Human Development and Family Studies (adjunct), University of
Connecticut. [1983 - 1987]
# Assistant Clinical Professor of Psychiatry, Tufts University, School of Medicine. [1973
- 1980].
# Director of Research, Concord (Massachusetts) Family Service Society. [1973]
# Faculty member, I.B.M. Systems Research Institute. [1968 - 1972]
# President, Information & Systems Institute, Inc. [1966 - 1968]
# Post-graduate program instructor, Wharton School of Business, University of
Pennsylvania. [1967]
# Staff Consultant, Programmer/Analyst, C E I R, Inc. [1963 - 1966]

"Many other methodologies have been developed since, and almost all have been strongly
influenced by Structured Design, right up to the latest Unified Process and Unified
Modelling Language for Object Oriented and Aspect Oriented Software Engineering. Indeed,
so pervasive has been Structured Design's influence that the most recent methodologies -
the so-called Agile software development Methodologies - and Kent Beck's "Extreme
Programming" in particular, define themselves primarily by the ways in which their
approaches *differ* from Structured Design - as in the Agile Manifesto, or even in the
choice of the name "Extreme Programming"."

http://en.wikipedia.org/wiki/Larry_Constantine


>While I have no issue with his statements (and at least he had the grace to 
>explain why he believed they were important), I wouldn't get unwrapped about 
>code not adhering to it either. We don't live in a perfect world and people 
>do the best they can under pressure.

Pressure is a common excuse for bad programming. 'We don't have time to do it right. Just
get it done as quickly as possible. We'll pretty it up later.' Of course, later never
comes. The idea that good programming is a luxury is belied by the fact that it is 50% the
size of bad programming. Also, it is more likely to work the first time. 

>> Starving the interface is a bad idea. Rather than passing four data 
>> structures, they'll
…[4 more quoted lines elided]…
>passed by reference. 

I did exactly the same for years.

> I don't like interfaces anyway and would mch rather 
>see properties being used for data, but sometimes it makes sense. Why do you 
>believe it is better to pass four parameters than one?

It reduces the number of copybooks from 5 to 4 and it eliminates MOVE statements. 

Generally, I see MOVE statements as non-productive, unless they actually do something like
editing a number. They are bureaucratic overhead. It is better to use primary sources
where they sit in memory. Called programs do not mischeviously screw around with other
fields in the structure. You're paranoic if you think so.

>> I worked at a place where I got to rewrite 1,000+ bad programs.
>
>Really? I would've written a program to either do or help me do that. Life's 
>too short... :-)

I wrote a Cobol Beautifier. But I've never seen a way to mechanically beautify ugly logic.
That computer science hasn't even come close proves that programming talent is still
needed, despite claims to the contrary.

>> The AVERAGE ratio between
>> after and before was 50%. Half the bad code was superfluous. Even I was 
…[6 more quoted lines elided]…
>you? (rhetorical...)

$100K in seed money to start my own company, and managing spun off businesses for four
years. 

>> It's much easier today. You can achieve that kind of efficiency by simply 
>> replacing the
…[5 more quoted lines elided]…
>a whimsical idea :-))

Crap code is endemic to mainframes, because the inmates are still running the asylum. When
the code is moved to Unix, bad guys hold on only half the time. In the other half, they
are replaced by programmers from other cultures, who are not expert in Cobol but recognize
bad logic, because it's the same in any language. 

>BOTTOM LINE: "crap code " is a fact of life, but usually it is subjective 
>judgement that makes it so (obviously, the person who wrote it didn't think 
…[10 more quoted lines elided]…
>Deal with it; that's what they pay you for.

Typically, I fix crap code for six months, then they keep me around another six months
because they hope to learn better programming. 

Your emotional investment here, in defense of bad programming, is telling.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-08T12:44:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2gk80$bt3$1@reader2.panix.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com>`

```
In article <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 7 Jun 2008 18:09:25 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz>
…[9 more quoted lines elided]…
>Our ranking has nothing to do with morality, it is about quality. 

I barely know what *I* do, Mr Wagner, let alone anyone else... but I 
rarely judge something to be 'better than something else'; my experiences 
tell me that one thing would be 'better FOR (PURPOSE) (emphasis intended) 
than something else'.

To say 'a baking potato is better than a cooking apple' might make for 
some moderately... interesting pie.

[snip]

>The best code I've seen was written by a high school student; the worst
>was written by a
>man with a PhD in computer science and 30 years of experience. 

If someone else has different experience - the best code they've seen 
written was by the PhD and the worst by the teenager - then is that person 
wrong, incorrect, inexperienced, possessing different criteria for 
'best'... or Some of the Above?

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 15)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-08T11:56:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W7qdnasOrMu-ktHVnZ2dnUVZ_uudnZ2d@earthlink.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <g2gk80$bt3$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
>
> To say 'a baking potato is better than a cooking apple' might make for
> some moderately... interesting pie.
>

But baking (either) then eating is significantly different from eating then 
baking.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-09T00:56:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2hv48$cc7$1@reader2.panix.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <g2gk80$bt3$1@reader2.panix.com> <W7qdnasOrMu-ktHVnZ2dnUVZ_uudnZ2d@earthlink.com>`

```
In article <W7qdnasOrMu-ktHVnZ2dnUVZ_uudnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>
…[5 more quoted lines elided]…
>baking. 

A change in sequence might have discernable effects in a variety of 
situations... in some languages, however, order word important less much 
is.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-09T00:48:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b22osF39l4mnU1@mid.individual.net>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com...
> On Sat, 7 Jun 2008 18:09:25 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[11 more quoted lines elided]…
> Our ranking has nothing to do with morality, it is about quality.

As perceived by each of us, subjectively.

>
>>All of us are affected by
…[9 more quoted lines elided]…
>

In whose opinion, Robert? Yours,  right? It is a subjective judgement.

>>Is someone a "bad" programmer because they don't understand the formal
>>definition of coupling (control or otherwise), but they saw indicators 
…[7 more quoted lines elided]…
> Yugo or a 1960s era British car.

If your personal criteria for a car has "Get me where I'm going..." at the 
top, you would be well satisifed with any of these. Millions of people voted 
with their chequebooks and bought them. The fact that you or I may not have, 
does not make those people wrong. It is a subjective judgement.

>
>>There is a certain smugness in deciding that the way in which you do
>>something is the ONLY way.
>
> You have it backwards.

I don't think so...:-)

>Good programmers do not insist their way is the only way, BAD
> programmers are the ones who do that. They call it Shop Standards. The 
…[9 more quoted lines elided]…
> certainty.

Sometimes. Certainly not always.
>
>>It never ceases to amaze me how passionate some programmers become about
…[6 more quoted lines elided]…
> demoted to a menial job.

Funny, most of the programmers I have encountered (self included) have 
always been interested in finding alternative, possibly "better" ways of 
doing things . I don't know anyone who was afraid of being caught out in a 
lie. This sounds like rhetoric rather than fact, to me.
>
>>>Is there a book: Crap Code in 24 Hours?
…[11 more quoted lines elided]…
> difference."

So if a program didn't work correctly you would still value it, as long as 
it was designed top-down and built bottom up? I respect your right to 
believe that. It is subjective judgement. Other mileages may vary... :-)

> When people try to do everything in one mode exclusively, the result is 
> junk. For
…[20 more quoted lines elided]…
> terrified of being wrong. I don't find it interesting, I find it ignoble.

I think attitude is important. It is important when you work on your own and 
it is important when you work with a team.


> It's an
> evolutionary trait that got mankind through a million years of 
> uncertainty.
>

Some of us have grown out of it :-)

>>>>Another tidbit I remember from Constantine: "indicators" are the type
>>>>of element that he would call "control coupling", because it passes
…[45 more quoted lines elided]…
>

Thanks. That was pretty much what I expected. It doesn't make his input any 
less valuable, but it does help to explain why he may not be aware of the 
pressures that people have to operate under in the real world.



> "Many other methodologies have been developed since, and almost all have 
> been strongly
…[15 more quoted lines elided]…
>

A blatant troll which I shall ignore...:-)

>
>>While I have no issue with his statements (and at least he had the grace 
…[13 more quoted lines elided]…
> size of bad programming. Also, it is more likely to work the first time.

I am not advocating good, or  excusing bad, programming. I'm simply saying 
that programming gets done. During that process people learn stuff and the 
next time they do something they try to apply what they learned the last 
time they did it.

The whole issue is not as important as we sometimes think. If programs work 
correctly, it really doesn't matter whether the code is "good" or "bad", 
although most of us strive to make it as good as we can. Self appointed 
pundits making judgements about something that is purely subjective anyway, 
may not actually make the situation any better. Moaning and sniping at "bad" 
code also achieves very little.

This discussion reminds me a lot of the advent of virtual storage. Passions 
ran high about the "Art" of computer programming, which hinged on the 
unteachable principle of optimizing programs in time and space, when both 
these commodities were at a premium. Esoteric techniques were developed to 
save a few bytes in memory, or make loops execute faster, overlap IO, cut 
through convoluted logic with propositional calculus and Boolean 
simplifications, all exciting stuff that made practitioners "artists".

Then virtual storage arrived and suddenly one of the basic constraints was 
removed. Take all the space you want... we have heaps... Initially, it was 
pretty easy to make it look stupid by causing it to thrash itself to death, 
but as OSes and hardware got smarter, so did the paging system.

Eventually we came to accept that batch processes running in virtual memory 
didn't require any special techniques to write and those of us who derived 
satisfaction from squeezing hardware moved into online and multithreaded 
systems, where there was still some need for our skills.

That was decades ago. Today it is pretty much irrelevant. Certainly, if you 
DELIBERATELY write "bad" code you can slow things down considerably, but I 
don't think anyone does that. Optimizing compilers ensure that object code 
at least has a fighting chance of performing well (always provided it is 
logically correct, of course...)

The current discussion about "good" and "bad" programming is just as 
irrelevant. It is an echo from the days when COBOL was the only game in town 
and amending lines of code was the only way to fix computer systems. It 
wasn't enough to simply "write" code, it had to be maintained as well. Those 
days are largely gone, and even on sites where COBOL is still in use, the 
constraints of time and space have been eradicated, by hardware with 
performance that would have been unimaginable back in the COBOL heyday, and 
virtual storage that offers an address space in the ball park of the 
distance to the planet Neptune in miles. So what exactly is this "good" as 
opposed to "bad" code and why would it matter, as long as the program 
obtains the desired result?

I believe it doesn't. I further believe that arguments of this nature are 
simply about ego, and occasionally about hankerings for "glory days"... If 
someone writes EVALUATE instead of a series of IFs (or vice versa), if 
someone uses the odd GO TO, or even the odd ALTER, you won't hear me 
grizzling. If I have to maintain a program where the code isn't "pure" 
according to the tenets of computer science, sorry, I don't care. Bring it 
on. It's what I do. I'm a programmer. Done it all my life.



>
>>> Starving the interface is a bad idea. Rather than passing four data
…[15 more quoted lines elided]…
> statements.

As I generally don't use COPY BOOKS (I see no point in propagating source 
code when I can write a component to encapsulate it and use an object 
instance of that... An exception might be where a number of components use a 
common service through an interface, but then I tend to make the "interface" 
a property (or properties)  of the service... (the clients would get and set 
properties rather than include an interface definition in themselves...)), 
I'm not impressed by this argument.  VERY RARELY I MAY use a COPY Book. If I 
did, I don't see how the number of them "is reduced from 5 to 4" in your 
example. I use 1, not  4 or 5.

Eliminates MOVE statements? How? There is one move to the interface and 
another when it is returned. How is that MORE than would otherwise be the 
case?
>
> Generally, I see MOVE statements as non-productive, unless they actually 
…[3 more quoted lines elided]…
> where they sit in memory.

I don't entirely disagree, but I don't see it as Holy Writ, either.

>Called programs do not mischeviously screw around with other
> fields in the structure. You're paranoic if you think so.

I don't have, and have not had for a several decades now, problems with 
Linkage. None of my code, calling or called, "screws around" with fields it 
isn't supposed to. I think I see what you're getting at, but I always make 
sure the interface is designed so that whatever uses it, will use ALL of it, 
and it is usually encapsulated in the server anyway.

As posted here recently, I am currently working on an interface, some parts 
of which are quite complex and not yet complete. When I am satisfied with 
the structure, I'll then decide whether it will be embedded in the server or 
not. The COBOL clients are being manipulated by C# code, which can insert 
whatever I want into them, so whether I use an INVOKE ...USING... or a 
series of SETs followed by a simple INVOKE, there will be no COPY book 
required.


>
>>> I worked at a place where I got to rewrite 1,000+ bad programs.
…[6 more quoted lines elided]…
> beautify ugly logic.

While I accept what you say, (YOU haven't seen it) I can assure you that 
there are such tools and some of them are VERY effective. We had some posts 
here a long time ago (Apr, 2001) where there were some samples of really 
ugly "logic" which I simplified manually using Boolean simplifications, just 
to demonstrate the technique. I asked if anyone knew of any software 
available which could do this (I was seriously considering writing some :-)) 
when I received the following response:

<quoted from CLC Apr 15, 2001>

If multiple copies of this "cloned" code (or variants) exist across
multiple files, than you indeed have a serious problem keeping
them up to date.

A tool that can find these copies and factor them out into single
abstractions (e.g., a copybook) can be seen at
http://www.semdesigns.com/Products/Clone/index.html


Another poster suggested that carrying out symbolic simplification
of the ugly IF statements would at least help readability.
The DMS engine underneath the Clone remover can actually
do such symbolic simplification.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-08T19:54:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com>`
- **References:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net>`

```
On Mon, 9 Jun 2008 00:48:26 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert" <no@e.mail> wrote in message 
>news:c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com...
>> On Sat, 7 Jun 2008 18:09:25 +1200, "Pete Dashwood" 

>>>All of us are affected by
>>>our education and experience in computer programming, but that education 
…[10 more quoted lines elided]…
>In whose opinion, Robert? Yours,  right? It is a subjective judgement.

It was an opinion shared by 20 programmers who were familiar with their work.

>>>>They
>>>> act like there's an unwritten 'standard' and are offended by programmers
…[17 more quoted lines elided]…
>it is important when you work with a team.

That's the most subjective judgement of all, and the opinion of one manager.

>The current discussion about "good" and "bad" programming is just as 
>irrelevant. It is an echo from the days when COBOL was the only game in town 
…[16 more quoted lines elided]…
>on. It's what I do. I'm a programmer. Done it all my life.

Good programming reduced the total IT expenses of one company by 88%. It was a supermarket
chain with 200 stores, 15K employees, annual sales $1.6 B. Published norms for the
supermarket industry said its IT expenses should have been 0.5% of sales = $8 M, which
implies 50 programmers. Other supermarket chains of comparable size did indeed spend that
much. We spent $1 M on six programmers and an IBM 4361 running VSE, supporting 100
terminals. We didn't just maintain, we developed significant new systems, including four
brands of POS, a voice/DTMF controlled order entry system, a truck maintenance system and
all new financials. 

If we had not rewritten the bad programs, we would have needed 50 programmers, like the
competition. That went on for six years. After I left, they increased the staff to 50 and
the computer to one ten times as big, running MVS. IT expenses went from $1 M to $8 M. 

>>>> Starving the interface is a bad idea. Rather than passing four data
>>>> structures, they'll
…[28 more quoted lines elided]…
>case?

The data is coming from or going to larger structures, typically database rows or file
records. Most people use copybooks for such things. If you simply pass those structures,
you don't have to copy fields to and from an interface structure. 

If the called program is a data layer doing IO, you must pass it whole records.

>> Generally, I see MOVE statements as non-productive, unless they actually 
>> do something like
…[4 more quoted lines elided]…
>I don't entirely disagree, but I don't see it as Holy Writ, either.

It's not high on my list, just a passing idea.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-09T14:05:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b3henF394dciU1@mid.individual.net>`
- **References:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com...
> On Mon, 9 Jun 2008 00:48:26 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[49 more quoted lines elided]…
> manager.

Sentences that start with "I" are usually of a subjective nature. I make no 
apology for this, neither have I implied anywhere that a subjective 
judgement is "bad", merely that it is ... subjective. The statement above is 
not a judgement (in the sense of judging others) it is merely an expressed 
opinion, and yes, it is most certainly subjective.

>
>>The current discussion about "good" and "bad" programming is just as
…[36 more quoted lines elided]…
> all new financials.

So the systems you developed were not poorly written in the first place and 
therefore have no place in this discussion... :-)
>
> If we had not rewritten the bad programs, we would have needed 50 
> programmers, like the
> competition.

If you pleeze, yer 'onner, that is speculative and hypothetical. It cannot 
be established whether that statement is true or not.



>That went on for six years. After I left, they increased the staff to 50 
>and
> the computer to one ten times as big, running MVS.

Ah, that would be the loonies running the asylum again... :-)

Well, we can conclude you were worth 44 ordinary programmers...
I'm amazed they let you go.


IT expenses went from $1 M to $8 M.
>
What about profits...?


>>>>> Starving the interface is a bad idea. Rather than passing four data
>>>>> structures, they'll
…[38 more quoted lines elided]…
> you don't have to copy fields to and from an interface structure.

OK, I get what you're saying now. Thanks.

(This does not imply agreement, only understanding... :-))
>
> If the called program is a data layer doing IO, you must pass it whole 
…[12 more quoted lines elided]…
>

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-09T12:27:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14oq4418eo6sio50es9mbe9nbgok768vee@4ax.com>`
- **References:** `<i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com> <6b3henF394dciU1@mid.individual.net>`

```
On Mon, 9 Jun 2008 14:05:12 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert" <no@e.mail> wrote in message 
>news:27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com...
>> On Mon, 9 Jun 2008 00:48:26 +1200, "Pete Dashwood" 
>> <dashwood@removethis.enternet.co.nz>
>> wrote:

>> Good programming reduced the total IT expenses of one company by 88%. It 
>> was a supermarket
…[15 more quoted lines elided]…
>therefore have no place in this discussion... :-)

The most important systems in a supermarket company control the warehouse -- pick tickets
(shipments), purchasing and inventory. Those programs, which comprised at least half the
total code, were already written. They were mission critical. If they failed, the company
would be non-functional within days. 

>> If we had not rewritten the bad programs, we would have needed 50 
>> programmers, like the
…[3 more quoted lines elided]…
>be established whether that statement is true or not.

1. Similar companies had 50 programmers.
2. That company's IT expanded to 50 programmers. 

That's the best possible evidence. If you don't believe it, you're being irrational.

>>That went on for six years. After I left, they increased the staff to 50 
>>and
>> the computer to one ten times as big, running MVS.
>
>Ah, that would be the loonies running the asylum again... :-)

IBM's Account Management was running the asylum. 

>Well, we can conclude you were worth 44 ordinary programmers...
>I'm amazed they let you go.

The correct conclusion is 6 programmers with well written Cobol are equivalent to 50
programmers with 'industry standard' mediocre Cobol. 

Pass it on to your company CEO.

>IT expenses went from $1 M to $8 M.
>>
>What about profits...?

Net profit went down by $7 M. The difference went straight to the bottom line.

The company was losing money the whole time. My Store Inventory system enabled management
to conceal losses for five years. Is that a selling point?
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-09T07:20:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RJmdnZ2uePm5vdDVnZ2dnUVZ_gCdnZ2d@earthlink.com>`
- **References:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com>`

```
Robert wrote:
>
> Good programming reduced the total IT expenses of one company by 88%.
…[14 more quoted lines elided]…
>

More System Laws:

1. The System itself tends to expand at 5-6% per year.

2. Systems attract systems people. For every system, there is a type of 
person adapted to thrive on it or in it.

3. Systems develop goals of their own the instant they come into being. 
Intrasystem goals come first.

4. Efficient systems are dangerous to themselves and to others.

5. The system can temporarily be controlled, but will eventually win.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:54:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4461c09a-81b4-4458-b095-1a113aabc4f7@j22g2000hsf.googlegroups.com>`
- **References:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com> <RJmdnZ2uePm5vdDVnZ2dnUVZ_gCdnZ2d@earthlink.com>`

```
On Jun 9, 8:20 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> More System Laws:
>
> 1. The System itself tends to expand at 5-6% per year.
Yes, along as it is Alive, it is Growing.

>
> 2. Systems attract systems people. For every system, there is a type of
> person adapted to thrive on it or in it.

The Puzzle presents itself to the world. The appropriate PuzzleSolvers
are then attracted to it. It is rather like sockets, and plugs, is it
not? But which is male and which is female? :-)

>
> 3. Systems develop goals of their own the instant they come into being.
> Intrasystem goals come first.

I think this can lead to various, differing, manifestations of
"success" on software projects. "Success" is in the context of "goals
of their own."

>
> 4. Efficient systems are dangerous to themselves and to others.

Dangerous to themselves, because efficent systems create powerful
enemies?

>
> 5. The system can temporarily be controlled, but will eventually win.- Hide quoted text -

Yes, but it feels so goooooooddddd to turn oneself over to Something
That is Bigger.

...

Mr. Heybub,

If I may, please, do your co-workers tell you that you are fun to work
with?

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-11T10:25:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9tidnSy6G-bSc9LVnZ2dnUVZ_jOdnZ2d@earthlink.com>`
- **References:** `<afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <27ko445ah8c4taaksfh5nj7p4u3tq5s056@4ax.com> <RJmdnZ2uePm5vdDVnZ2dnUVZ_gCdnZ2d@earthlink.com> <4461c09a-81b4-4458-b095-1a113aabc4f7@j22g2000hsf.googlegroups.com>`

```
klshafer@att.net wrote:
>
> ...
…[5 more quoted lines elided]…
>

Visit us on the tx.guns newsgroups. We have a lot of fun exploring the human 
condition.

Recent subjects:
"Don't stress the crabs"
"Lucky he wasn't thrown to the floor"
"Lure this, creep!"
"Claw hammer used on man's head"
"Burglar mistakes dog for one that gives a shit"
"Saving the odd sausage"
"Man arrested while stalking asparagus"

--- for example

ROMANTIC PROPOSAL
How precious.

"[MADISON, Wisc] After kicking in the woman's bedroom door, [a naked]
Behrend jumped on the woman's bed, gave her a big hug, and said, 'I want to
have sex with you, and I love you, and I want to marry you,' according to
the criminal complaint filed Wednesday."

He was finally overcome by sheer weight of officers, but:

"Previous to that, he had sexually assaulted one of the women officers by
grabbing her breasts, the complaint says, and through most of the struggle
he was making lewd and suggestive comments to various officers."

Police think mushrooms and alcohol may have been involved. Or lust.

or

SHERMAN TANK FOUND IN HOLE

"An American tank that formed part of the 1944 D-Day invasion force was
discovered buried under a street in northern France."

Entire French village surrenders.

With pic
http://www.telegraph.co.uk/news/worldnews/europe/france/2075833/World-War-II-US-D-Day-invasion-tank-unearthed-in-France.html

or

THIS IS YOUR BRAIN ON DRUGS

1. Boise, Idaho cops become suspicious upon seeing an SUV driving backwards
at speed.

2. When cops try to investigate, driver bails, runs to apartment building.

3. Cops follow, woman says "in there," cops find hole in ceiling and
crashing noises. Suspect is ripping through walls!

4. Cops call for backup, evacuate building.

5. More cops arrive and search resumes.

6. Suspect has, by this time, tunneled into basement.

7. K-9 points to pile of wood. Cops say "Come out, come out, wherever you
are! We have a dog!"

8. Suspect says "Yeah, and I've got a gun!"

9. Cops remove wood and find suspect attempting to solder without proper
ventilation.

10. Cops shoot suspect.

11. Dog gets bacon treat. All ends well.

http://www.idahostatesman.com/102/story/402397.htm

-----------
Anyway, I think you get the idea. See you soon.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 15)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T09:41:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net>`

```
My comments interspersed among Robert's and Pete's. At the
(acceptable) risk of being branded a Robert-ista :-) ...

On Jun 8, 8:48 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[5 more quoted lines elided]…
>

Robert:
> > My number 1 is "Design top-down, program bottom-up. Learn to tell the
> > difference."
…[5 more quoted lines elided]…
>

Yes, Structured Design is a version of top-down, with some heuristics
(coupling and cohesion) thrown in to help you evaluate the "goodness"
of the design. In my (subjective?) opinion, this measure of goodness
is not _subjective_; it is objective and real.


Pete:
> >>I betcha Constantine never worked on the shop floor in a large commercial
> >>COBOL shop. :-)
>

Robert:
> > # Professor, Department of Mathematics & Engineering, University of
> > Madeira, Funchal,
…[50 more quoted lines elided]…
> A blatant troll which I shall ignore...:-)

I did not view it as a troll. I presume some are verifiable facts. The
other, the "opinion" that much of Agile/XP draws upon earlier works of
Constantine squares with my own experience of interacting with the
Agile/XP folks, and looking at their Bibliographies of their own
books, which I see crediting Constantine.

This also helps to explain the importance of "refactoring" to XP.
Constantine, if he was not the first to use the term "factor" as in
"factor out the common code into a separate module", at least was very
important in popularizing the idea.

Though I may differ with the Agile/XP folks regarding their near-
absolutist position of "the design is in the code", I recognize that
in their emphasis on "refactoring" they are underscoring the
importance of "design" as they see it and the striving the improve it
incrementally.


Pete:
> The whole issue is not as important as we sometimes think. If programs work
> correctly, it really doesn't matter whether the code is "good" or "bad",
…[3 more quoted lines elided]…
> code also achieves very little.

Programs can "work" (sort of) correctly, and still be very difficult
to understand and to modify. In this sense, it does matter whether the
code is "good" or "bad". But rather than use those terms, with their
implied value judgments, should we not instead use the heuristics
themselves, such as "this program shows good cohesion", and this
program has "excessive coupling"?

I know that I felt (subjectively?) that I achieved a first-order
improvement in my code readability (by me, let alone others) and
reliability when I was persuaded (by others, by recognized authorities
with _some_ credentials) to use the "structured programming"
techniques, and then I achieved another second-order improvement when
I was persuaded again (by Constantine, et al.) to use the "structured
design" techniques.

I did not cultivate these concepts as the my own self-appointed pundit
creations; I recognized them from someone smarter than me, and then
internalized them best I knew how.

It has helped me throughout to hold close a "realist" point of view, a
point of view that I know I have mentioned elsewhere, but maybe not on
CLC (sorry, I can't remember). But it goes along these lines: For
every (God-given) problem, there is one best (God-given) design and
one best (God-given) implementation of it (program.) So I am not
really "creating" a design, or "creating" a program - I am merely
"discovering" it. Being fallible, and with limited "awareness", as all
humans are, I will fall short. That is why _no_ perfect programs are
written.

But in aspiring to do this, to uncover this Truth in Reality, we do
better than if we do not aspire at all. And since it is not My
Creation, it is easy to let go of my shortsighted efforts when a
better way becomes apparent.

For the Philosopher-Kings among us, this way of looking at things has
something to do with Number Theory, and the argument between abstract
mathematicians as to whether "numbers" are creations/inventions of
man, with no objective reality outside of man's mind, or are they
creations of God, with an objective reality independent of Man. I
believe the former were/are called "conceptualists", and the latter
called "realists."

All this has something do with an earlier (historical) discussion
regarding "does the color red exist", apart from the fact that "this
car is red", "this rose is red", "his face is red :-) ".

I welcome followups to enlighten me, but we are close to being OT, and
maybe crossed that line some time ago...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-09T17:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2joih$ft5$1@reader2.panix.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com>`

```
In article <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:

[snip]

>But it goes along these lines: For
>every (God-given) problem, there is one best (God-given) design and
…[4 more quoted lines elided]…
>written.

This might explain why, decades on back, folks used to say that 60/70/80% 
(or suchlike) of a given DP/IS/MIS/IT budget had to be dedicated to 
maintenance/ehnahcement... it's because there's one best program for every 
situation and it never gets written.

(if code is forever written anew, of course, then no money needs to be 
allocated to maintenance/enhancement; even Doing The Same Thing Over 
becomes development)

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T11:07:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393028db-e2f9-455c-89d6-0b6653a93d40@34g2000hsh.googlegroups.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <g2joih$ft5$1@reader2.panix.com>`

```
> This might explain why, decades on back, folks used to say that 60/70/80%
> (or suchlike) of a given DP/IS/MIS/IT budget had to be dedicated to
> maintenance/ehnahcement... it's because there's one best program for every
> situation and it never gets written.

Au contraire, my dear Doc, it gets written - it just takes an Eternity
of time. :-) One just has to take a very, very, loooooonnnngggg term
view of things...

In the meantime, it makes for an acceptably good living for you and
me, as you very well know...

>
> (if code is forever written anew, of course, then no money needs to be
…[3 more quoted lines elided]…
> DD

I have heard this described cynically in the Java/C#/O-O world as
development/maintenance being "write once, then write once again" :-),
with apologies to Mr. Pete, who I would think would beg to differ...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-09T18:27:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2jslm$spc$1@reader2.panix.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <g2joih$ft5$1@reader2.panix.com> <393028db-e2f9-455c-89d6-0b6653a93d40@34g2000hsh.googlegroups.com>`

```
In article <393028db-e2f9-455c-89d6-0b6653a93d40@34g2000hsh.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>> This might explain why, decades on back, folks used to say that 60/70/80%
>> (or suchlike) of a given DP/IS/MIS/IT budget had to be dedicated to
…[4 more quoted lines elided]…
>of time. :-)

As opposed to... an Eternity of space?  Some far proximity?

[snip]

>In the meantime, it makes for an acceptably good living for you and
>me, as you very well know...

I've said that it beats working on the loading-dock, aye.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-11T01:25:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b7dmpF38rb61U1@mid.individual.net>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <g2joih$ft5$1@reader2.panix.com> <393028db-e2f9-455c-89d6-0b6653a93d40@34g2000hsh.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:393028db-e2f9-455c-89d6-0b6653a93d40@34g2000hsh.googlegroups.com...
>> This might explain why, decades on back, folks used to say that 60/70/80%
>> (or suchlike) of a given DP/IS/MIS/IT budget had to be dedicated to
…[20 more quoted lines elided]…
> with apologies to Mr. Pete, who I would think would beg to differ...

No apology required. I've heard that too... :-)

For myself, yes, I would offer a different experience. I seldom need to 
rewrite. One of the secrets of success is "granularity". If components are 
small, the chances of having to rewrite are dimininshed, and even if you do 
have to, it is trivial. As component size (and consequent complexity) 
increases, so do the chances of the component not doing exactly what you 
want and needing to be extended, have certain methods overridden, or be 
rewritten.

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-06-09T13:05:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xge3k.5949$QI2.3890@newsfe23.lga>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com>`

```

<klshafer@att.net> wrote in message
news:491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com...
>Pete:
> The whole issue is not as important as we sometimes think. If programs
work
> correctly, it really doesn't matter whether the code is "good" or "bad",
> although most of us strive to make it as good as we can. Self appointed
> pundits making judgements about something that is purely subjective
anyway,
> may not actually make the situation any better. Moaning and sniping at
"bad"
> code also achieves very little.

>Ken:
Programs can "work" (sort of) correctly, and still be very difficult
to understand and to modify. In this sense, it does matter whether the
code is "good" or "bad". But rather than use those terms, with their
implied value judgments, should we not instead use the heuristics
themselves, such as "this program shows good cohesion", and this
program has "excessive coupling"?

PL:
Older members in the group will remember the halcyon days of long ago when
anyone could pick up a manual, read it once, and call themselves a
programmer; or, worse, read a few articles in "Datamation" and call
themselves a consultant.  Curiously, in my experience a lot of these people
were in the furniture business!  Anyway.  One such person wrote a program (a
trial balance, I think) which I had to try and fix after it had been some
months in operation.

This program would have been BAD by any possible definition.  There was no
logical flow: there were GOTO's to distant bits of code in the middle of
some other routine; data-names were two or three characters; obviously it
had been written on pieces of coding forms that were then taped together!
But that could have been borne; the real problem was that the READ's were
scattered all over the place, and there were dozens of them.  Whenever a
record had been written (anywhere in the program) there was a read
immediately following: the sequential file reads had each their own AT END
routine, no two quite the same; randon reads to the ISAM files (also
anywhere in the program ) were coded >READ filename INVALID KEY DISPLAY
"invalid key".<  I was the third and most experienced person to be asked to
look at the program (as the author had gone back to furniture).  I simply
could not figure it out: the one and only program that evr defeated me.  I
gave up and reverse-engineered the thing. It worked OK until the system was
replaced.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-10T00:08:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqrr44pdac9sulbrp4bosqncd91o7e5b8k@4ax.com>`
- **References:** `<f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <Xge3k.5949$QI2.3890@newsfe23.lga>`

```
On Mon, 9 Jun 2008 13:05:33 -0500, "tlmfru" <lacey@mts.net> wrote:


>Older members in the group will remember the halcyon days of long ago when
>anyone could pick up a manual, read it once, and call themselves a
>programmer; or, worse, read a few articles in "Datamation" and call
>themselves a consultant.  

To get a consultant job today, you must correctly answer six screening questions:

1.  Name the four Cobol divisions. 
     (We're talking Cobol 85. Don't get fancy with the 02 standard.)
2. What's the difference between an index and a subscript?
3. How many bytes does this take: comp-3 pic s9(5)?
4. What two verbs are used with SORT?
5. What is an 88?
6. What's the difference between SEARCH and SEARCH ALL.

Difficult, huh?

Here is my suggested screening test.

1.  ZERO can be used in an IF statement two ways. One is a figurative constant, for 
     example IF foo = ZERO. What is the other?

2.  How would you copy foo1 tofoo2  trimming leading spaces, if any, with a single
statement.  Both are PIC x(30).

3. What's the difference between WORKING-STORAGE and LOCAL-STORAGE?

4. What does GLOBAL do?

5. 88 foo VALUES 2 4 6. 
    SET foo TO TRUE. 
    What value does it set, or do you get a compilation error?

6. Where or why would you use this:
    01  ()-record.

7. 01 foo PIC ---,--9.99 VALUE ZERO. 
    DISPLAY foo.
    What is displayed?

8. The word VARYING can be used four ways. Name three.

9. What does NEXT SENTENCE do?

10  01  foo PIC 9 VALUE 4.
      EVALUATE foo
          WHEN 2 OR 4
              DISPLAY 'found'
          WHEN OTHER
              DISPLAY 'not found ' foo
      END-EVALUATE
      What is displayed, or do you get a compilation error?
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-06-10T06:53:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Txp3k.65240$SV4.50536@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<eqrr44pdac9sulbrp4bosqncd91o7e5b8k@4ax.com>`
- **References:** `<f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <Xge3k.5949$QI2.3890@newsfe23.lga> <eqrr44pdac9sulbrp4bosqncd91o7e5b8k@4ax.com>`

```
Robert wrote:
> (snip) 
> 
> 6. Where or why would you use this:
>     01  ()-record.

I've never seen this before, what does it do?

Is this specific to a particular vendor's compiler?  I would be very 
surprised if this is standard COBOL.  Of course, I have been surprised 
before.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-10T09:14:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QBr3k.978385$us.385683@fe04.news.easynews.com>`
- **References:** `<f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <Xge3k.5949$QI2.3890@newsfe23.lga> <eqrr44pdac9sulbrp4bosqncd91o7e5b8k@4ax.com> <Txp3k.65240$SV4.50536@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold,
  If it were coded:

    01  (pref)-record.
        or

    01  :pref:-record.

would you be able to guess the answer to

    "Where or why would you use this:"

All of them can be used in the same way.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 20)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-06-11T06:51:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_BK3k.36004$102.5130@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<QBr3k.978385$us.385683@fe04.news.easynews.com>`
- **References:** `<f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <Xge3k.5949$QI2.3890@newsfe23.lga> <eqrr44pdac9sulbrp4bosqncd91o7e5b8k@4ax.com> <Txp3k.65240$SV4.50536@bgtnsc04-news.ops.worldnet.att.net> <QBr3k.978385$us.385683@fe04.news.easynews.com>`

```
William M. Klein wrote:
> Arnold,
>   If it were coded:
…[11 more quoted lines elided]…
> 

Bill,

Thanks for the explanation!  We actually use this, but only the 
":pref:" format.

With kindest regards,
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-11T01:19:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b7datF3be0odU1@mid.individual.net>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com...
My comments interspersed among Robert's and Pete's. At the
(acceptable) risk of being branded a Robert-ista :-) ...

On Jun 8, 8:48 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[5 more quoted lines elided]…
>

Robert:
> > My number 1 is "Design top-down, program bottom-up. Learn to tell the
> > difference."
…[5 more quoted lines elided]…
>

Yes, Structured Design is a version of top-down, with some heuristics
(coupling and cohesion) thrown in to help you evaluate the "goodness"
of the design. In my (subjective?) opinion, this measure of goodness
is not _subjective_; it is objective and real.

[Pete]

For that to be true it would need to be inarguable and universally agreed. 
It isn't. It is real to you (and to many people) but it is still subjective. 
No matter how strongly you may agree with it, it is still a matter of 
opinion and opposing arguments can be presented. Structured is not the ONLY 
way to write computer programs. It is not even the only "good" way. As soon 
as we start that argument we are into the realm of subjectivity and opinion.

But this discussion is not about the goodness or badness of structured 
programming or any other particular technique. It is about "good" 
programming and "bad" programming. My point was that it is not as relevant 
in today's world as it was in yesterday's, for the reasons I described. You 
can have all the academic arguments in the world for as long as you want to, 
but if program code does what it is supposed to then HOW it does it is 
becoming less and less relevant.

Pete:
> >>I betcha Constantine never worked on the shop floor in a large 
> >>commercial
> >>COBOL shop. :-)
>

Robert:
> > # Professor, Department of Mathematics & Engineering, University of
> > Madeira, Funchal,
…[55 more quoted lines elided]…
> A blatant troll which I shall ignore...:-)

I did not view it as a troll.

[Pete]

Given my stated preference for Agile development (which I have no intention 
of arguing here) it was a pretty blatant attempt on Robert's part to get me 
to respond...:-) It failed.

[/Pete]


 I presume some are verifiable facts. The
other, the "opinion" that much of Agile/XP draws upon earlier works of
Constantine squares with my own experience of interacting with the
Agile/XP folks, and looking at their Bibliographies of their own
books, which I see crediting Constantine.

This also helps to explain the importance of "refactoring" to XP.
Constantine, if he was not the first to use the term "factor" as in
"factor out the common code into a separate module", at least was very
important in popularizing the idea.

Though I may differ with the Agile/XP folks regarding their near-
absolutist position of "the design is in the code", I recognize that
in their emphasis on "refactoring" they are underscoring the
importance of "design" as they see it and the striving the improve it
incrementally.

[Pete]

The emphasis is in the "incrementally" far more than in the refactoring. You 
are taking too academic a view of this. That's why I won't be arguing it 
here. When you have actually built systems using a truly Agile process, I'll 
be more amenable to discussion. :-)


Pete:
> The whole issue is not as important as we sometimes think. If programs 
> work
…[6 more quoted lines elided]…
> code also achieves very little.

Programs can "work" (sort of) correctly, and still be very difficult
to understand and to modify.

[Pete]

And that is fine. AS LONG AS YOU NEVER NEED TO MODIFY THEM. It is only this 
misguided emphasis on ease of maintenance that renders coding style 
important. It is a legacy from the days when COBOL source code was King.

Source code ISN'T King any more, outside in the real world. Objects and 
Object code have staged a coup and the old Royal House has been toppled. We 
use encapsulated components and objects that DON'T need maintenance, any 
more than a Lego block needs to be re-designed. If it doesn't fit, replace 
it. If it isn't exactly what you want, replace it. We do exactly the same 
with electronic components. A circuit board fails, throw it away and plug a 
new one in. Whether it was TTL or second or third generation integration, or 
LSI, or VLSI, is completely irrelevant as long as the interface is 
compatible, the voltage levels are OK and the inputs and outputs are specced 
and achieved by the board.

If a software component does what it is specced to do, NO-ONE cares about 
techniques used in coding it, because no-one is going to change it. You 
might as well be concerned with the language it is written in. (You're not, 
because it is irrelevant as long as it does what it is supposed to do.)

The whole argument about "good" and "bad" code is simply an echo of the 
past. These days tools generate code. No-one is particularly worried about 
what particular coding techniques they use.

Your arguments are relevant to COBOL because (hundreds of...) thousands of 
lines of code need to be maintained (unless you use OO COBOL, and nobody 
does...). In the other 98% of computer programming that is going on in the 
world, coding style is almost irrelevant. There are useful practices that 
programmers observe as a matter of course, but they aren't Holy Writ. 
(Professional programmers still write "good" code because it is pride and 
force of habit, and it does no harm... :-)) We all want to be proud of what 
we do. It becomes counter-productive when you start criticising what someone 
else did, because it violates your personal subjective view of what is 
"good" or "bad"...

Have your own opinions, apply them in your code. Reserve judgement on 
others.

[/Pete]

 In this sense, it does matter whether the
code is "good" or "bad".

[Pete]

Why? If no-one is going to change it and it does what it's supposed to, why 
should I care? (I actually don't... and I'm kind of trying to persuade you 
not to either :-))

[/Pete]


But rather than use those terms, with their
implied value judgments, should we not instead use the heuristics
themselves, such as "this program shows good cohesion", and this
program has "excessive coupling"?

[Pete]

Sure if you want to... but the same arguments made above still apply.

[/Pete]

I know that I felt (subjectively?) that I achieved a first-order
improvement in my code readability (by me, let alone others) and
reliability when I was persuaded (by others, by recognized authorities
with _some_ credentials) to use the "structured programming"
techniques, and then I achieved another second-order improvement when
I was persuaded again (by Constantine, et al.) to use the "structured
design" techniques.

I did not cultivate these concepts as the my own self-appointed pundit
creations; I recognized them from someone smarter than me, and then
internalized them best I knew how.

[Pete]

So you arrived at your current conviction by persuasion and study. Your 
opinion was shaped by your experience and education, just like all of us. 
Nothing wrong in that, but recognize that it is subjective opinion and don't 
worry too much of you fail to Evangelize it. It isn't religion, it is 
computer programming. (and it's relevance in the world at large is 
diminishing...)

[/Pete]

It has helped me throughout to hold close a "realist" point of view, a
point of view that I know I have mentioned elsewhere, but maybe not on
CLC (sorry, I can't remember). But it goes along these lines: For
every (God-given) problem, there is one best (God-given) design and
one best (God-given) implementation of it (program.)

[Pete]

As an Atheist I don't believe problems come from God and I don't believe 
their solutions are God given either. I can accept that there are many ways 
to skin a cat and the relative "goodness" or "badness" of any given way 
depends on the priorities, experience, and perceptions of the person doing 
the skinning. Cat flaying, like computer programming, is different things to 
different people.

[/Pete]

So I am not
really "creating" a design, or "creating" a program - I am merely
"discovering" it. Being fallible, and with limited "awareness", as all
humans are, I will fall short. That is why _no_ perfect programs are
written.

[Pete]

Oh sure... let's give up now and let God do the programming... :-)

[/Pete]

But in aspiring to do this, to uncover this Truth in Reality, we do
better than if we do not aspire at all. And since it is not My
Creation, it is easy to let go of my shortsighted efforts when a
better way becomes apparent.

[Pete]

Well said.

[/Pete]

For the Philosopher-Kings among us, this way of looking at things has
something to do with Number Theory, and the argument between abstract
mathematicians as to whether "numbers" are creations/inventions of
man, with no objective reality outside of man's mind, or are they
creations of God, with an objective reality independent of Man. I
believe the former were/are called "conceptualists", and the latter
called "realists."

[Pete]

Or are they something other than either of the above?

Why limit it to blacks and whites? As a conceptualist I can conceive of a 
reality outside of the Mind of Man...

[/Pete]

All this has something do with an earlier (historical) discussion
regarding "does the color red exist", apart from the fact that "this
car is red", "this rose is red", "his face is red :-) ".

I welcome followups to enlighten me, but we are close to being OT, and
maybe crossed that line some time ago...

[Pete]

An interesting post, Ken. I understand why you feel the way you do and I 
don't think you're "wrong". I do think that applying a subjective standard 
to people other than oneself may not be fruitful, even if that subjective 
standard works very well for the subject :-)...

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:23:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4eb41888-d37a-4058-9463-5904ff8e6da7@d45g2000hsc.googlegroups.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net>`

```
On Jun 10, 9:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
> news:491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com...
> My comments interspersed among Robert's and Pete's. At the
> (acceptable) risk of being branded a Robert-ista :-) ...

> [Ken]
>
…[14 more quoted lines elided]…
> as we start that argument we are into the realm of subjectivity and opinion.

[/Pete]

Hmmmmmm... then please allow me to re-phrase this way:
That structured programming, cohesion, and minimal coupling constitute
desirable program characteristics, and that those characteristrics are
real and objective, is a subjective _belief_ that I have. And I am
searching for others who believe that way. Because that Way is _my_
Path. If I understand you correctly, you are not on that Path, the
Path which is my Path. More at the end of this post.

[Pete]
>
> But this discussion is not about the goodness or badness of structured
…[5 more quoted lines elided]…
> becoming less and less relevant.

[/Pete]


I had not thought myself an "academic." On the other hand, one of my
shop's Business Analysts has taken to calling me "Professor". He, like
you, knows I teach Algebra one night a week. :-) Yes, I have a couple
of degrees on my resume. My career engagements (about thirty or thirty-
five in all), have been pretty evenly divided between government and
corporate. There was one engagement for a state college where I
installed a repeatable test generator. My partner did the English
portion; I did the Math portion. :-)

[Pete]
>
> > A blatant troll which I shall ignore...:-)
[/Pete]

[Ken]
>
> I did not view it as a troll.
[/Ken]

>
> [Pete]
…[6 more quoted lines elided]…
>

Hmmmm... after reading your last statement, and re-reading Robert's
post on Constantine, I still cannot see it as a troll. But how am I to
know what is in Robert's heart?

So I shall just ask him, and hear what he has to say, if he deems it
worthy of a reply:

Robert, were your comments on Constantine a troll?


[Ken]
> This also helps to explain the importance of "refactoring" to XP.
> Constantine, if he was not the first to use the term "factor" as in
…[7 more quoted lines elided]…
> incrementally.
[/Ken]

>
> [Pete]
…[4 more quoted lines elided]…
> be more amenable to discussion. :-)
[/Pete]

I will risk a tad bit more dialogue, anyway. The early systems I
developed, albeit fairly small, were done as Team of One. Many of us
old-timers remember the drill. Some conversations with the client,
list the requirements (sort of), design, code, test and debug,
install, train, and document to the extent the client asked for. Was
this Agile-like?  Maybe it was only "Pre-Agile". Is it enough to give
me "license" to so engage you herein?

Ahhhh, I'm feeling "lucky", so what the heck...

Here is what someone more knowledgable than I on Agile has to say. On
the other hand, I have heard rumors that this certain Jason Gorham is
now "post-Agile", rather than "Agile." (Sidebar: "post-Agile" is a
term largely credited to Jon Kohl, a very nice young man who I have
met and who I like a lot. He can be found at
http://www.kohl.ca/blog/ )

Jason Gorham, http://parlezuml.com/blog/?sectionid=10

<begin Jason Gorham post>

__Quality Trends Can Reveal Inadequate Refactoring Effort__

A less pithy, and arguably far more constructive, answer to the
question "are we doing enough refactoring?" can be find by examining
how the quality of our code changes over time.

Take package-level coupling and cohesion, for example. if we want to
objectively gauge if we're doing enough to keep packages cohesive and
loosely coupled enough for our requirements, we can monitor those
aspects of quality as the project progresses and identify where the
trend might be headed.

<some stuff deleted>

Anyway, however often you choose to measure code quality, over time
you will doubtless notice a trend towards lowre quality as the code
grows and evolves. That's just natural code ageing, and it happens to
even the best development teams.

But better teams' code tends to age slower, because they put more
effort into keeping it "young" as they go.

If the trend tells you that inter-package coupling is probably going
to be too high by your release date, then you should consider putting
more effort into optimising that aspect of quality. Likewise for
package cohesion, or any other aspect of code quality you deem
important enough to monitor.

<stuff deleted>

I think you might be surprised at just how quickly code can age, and
just ___how much refactoring effort___ (emphasis added by KLS) is
really required to keep your code in good enough shape.

<end Jason Gorham post>

<<stuff deleted>>

[Ken]
>
> But rather than use those terms ("good" and "bad"), with their
> implied value judgments, should we not instead use the heuristics
> themselves, such as "this program shows good cohesion", and this
> program has "excessive coupling"?
[/Ken]

>
> [Pete]
…[3 more quoted lines elided]…
> [/Pete]

Well, yes, the same points still apply, but with the lowered decibel
level, maybe they are not even seen as "arguments"... rather, simply,
"differences."

<stuff deleted>

[Ken]
> I was persuaded again (by Constantine, et al.) to use the "structured
> design" techniques.
> I did not cultivate these concepts as the my own self-appointed pundit
> creations; I recognized them from someone smarter than me, and then
> internalized them best I knew how.
[/Ken]

>
> [Pete]
…[8 more quoted lines elided]…
> [/Pete]

Did it sound like Evangelizing? I thought it not - I did not ask you
for money, did I? :-) I thought that was one of the requirements to be
an Evangelist... Please see conclusion below...

>
<<stuff deleted>>

> An interesting post, Ken. I understand why you feel the way you do and I
> don't think you're "wrong". I do think that applying a subjective standard
> to people other than oneself may not be fruitful, even if that subjective
> standard works very well for the subject :-)...

Conclusion:
I am happy you found it interesting. But still I am unsure that you
"understand why [I] feel the way [I] do." So I will make a little more
effort...

Each of us is on Earth to work on a puzzle. Each one of us has a
different puzzle, though many puzzles overlap. None of us sees the Big
Puzzle, for that is only within the Realm of the Master Puzzlemaker.

Part of working on the puzzle involves finding people whose puzzles
overlap your puzzle, and who can help you work on it. But even those
whose puzzles do not overlap can help you, because by acknowledging
that you do not share their puzzle, you are farther along at finding
the people who do share your puzzle.

If I understand you, Mr. Pete, your puzzle involves something along
the lines of replacing procedural source with replaceable,
componentized, objects. (My words only, please feel free to tell me in
your own words what your "puzzle" is.)

My puzzle involves something along the line of "invariance" - what
aspects of "procedural source" will survive, and needs to be
maintained, in a way that we best can do. Finding people who see the
same "objective reality" of coupling and cohesion is part of that.

From my view, that is what is going on. That is all that is going on.
It is also, hmmmm, enough..., even _plenty_ enough.

Thank you for the time you have spent with me, and on my behalf ...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-10T20:37:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4q7u44l0fsp7l15hpv1tmljvqc8009nip2@4ax.com>`
- **References:** `<h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net> <4eb41888-d37a-4058-9463-5904ff8e6da7@d45g2000hsc.googlegroups.com>`

```
On Tue, 10 Jun 2008 10:23:50 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jun 10, 9:19ï¿½am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
>> <klsha...@att.net> wrote in message

>
>[Pete]
…[26 more quoted lines elided]…
>Robert, were your comments on Constantine a troll?

I saw it as blatant self-promotion, written by Constantine. 

A troll posts inflamatory remarks intended to provoke an angry response. I was trying to
provoke a reasoned response, not an angry one. Building a bridge (or not) between 70s
software architecture, championed by you,  and Agile, advocated by Pete, seemed
appropriate to the discussion.

In my opinion, both Structured and Agile are somewhat flawed models for three reasons:

1. Lack of substantiation. We are asked to take the author's word for everything.
2. Influenced by computer capability/limitations.
3, Tied to style/fashion of one generation.

My favorite author on programming in the abstract is Steve McConnell in Code Complete. He
substantiates claims with evidence and provides many citations. He sees programming as a
craft rather than a work product. In other words, his audience is programmers rather than
managers. He's not selling faster and cheaper, he is promoting quality. He is agnostic as
to language and linguistic model -- object oriented versus verb oriented. His theme is
that the biggest obstacle is the programmer's psychology and untrained thinking, not
external forces such as users and managers.  His approach is timeless and self-sufficient.
It will never go out of date because human nature doesn't change.

http://www.practicalpc.co.uk/reviews/books/codecomplete2.htm
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-11T18:47:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b9anvF3b8oc4U1@mid.individual.net>`
- **References:** `<h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net> <4eb41888-d37a-4058-9463-5904ff8e6da7@d45g2000hsc.googlegroups.com> <4q7u44l0fsp7l15hpv1tmljvqc8009nip2@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:4q7u44l0fsp7l15hpv1tmljvqc8009nip2@4ax.com...
> On Tue, 10 Jun 2008 10:23:50 -0700 (PDT), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[71 more quoted lines elided]…
> http://www.practicalpc.co.uk/reviews/books/codecomplete2.htm

Robert, this is a simply excellent response and I withdraw my accusation 
(which was made light-heartedly anyway... :-))

Good job. (I'm so impressed that I'll check out more on McConnell as soon as 
I have some time.)

Thanks.

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-11T13:48:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b8p7pF3ah3rhU1@mid.individual.net>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net> <4eb41888-d37a-4058-9463-5904ff8e6da7@d45g2000hsc.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:4eb41888-d37a-4058-9463-5904ff8e6da7@d45g2000hsc.googlegroups.com...
On Jun 10, 9:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
> news:491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com...
> My comments interspersed among Robert's and Pete's. At the
> (acceptable) risk of being branded a Robert-ista :-) ...

> [Ken]
>
…[18 more quoted lines elided]…
> opinion.

[/Pete]

Hmmmmmm... then please allow me to re-phrase this way:
That structured programming, cohesion, and minimal coupling constitute
desirable program characteristics, and that those characteristrics are
real and objective, is a subjective _belief_ that I have. And I am
searching for others who believe that way. Because that Way is _my_
Path. If I understand you correctly, you are not on that Path, the
Path which is my Path. More at the end of this post.
[Pete]

I walk many paths... Some are easier than others. Any path that takes me 
where I want to go is worth the walk.  Your path is fine, but it is not the 
"only way" for me. (It may well be for you...)


[Pete]
>
> But this discussion is not about the goodness or badness of structured
…[7 more quoted lines elided]…
> becoming less and less relevant.

[/Pete]


I had not thought myself an "academic." On the other hand, one of my
shop's Business Analysts has taken to calling me "Professor". He, like
you, knows I teach Algebra one night a week. :-) Yes, I have a couple
of degrees on my resume. My career engagements (about thirty or thirty-
five in all), have been pretty evenly divided between government and
corporate. There was one engagement for a state college where I
installed a repeatable test generator. My partner did the English
portion; I did the Math portion. :-)

[Pete]
>
> > A blatant troll which I shall ignore...:-)
[/Pete]

[Ken]
>
> I did not view it as a troll.
[/Ken]

>
> [Pete]
…[8 more quoted lines elided]…
>

Hmmmm... after reading your last statement, and re-reading Robert's
post on Constantine, I still cannot see it as a troll. But how am I to
know what is in Robert's heart?

So I shall just ask him, and hear what he has to say, if he deems it
worthy of a reply:

Robert, were your comments on Constantine a troll?


[Ken]
> This also helps to explain the importance of "refactoring" to XP.
> Constantine, if he was not the first to use the term "factor" as in
…[7 more quoted lines elided]…
> incrementally.
[/Ken]

>
> [Pete]
…[6 more quoted lines elided]…
> be more amenable to discussion. :-)
[/Pete]

I will risk a tad bit more dialogue, anyway. The early systems I
developed, albeit fairly small, were done as Team of One. Many of us
old-timers remember the drill. Some conversations with the client,
list the requirements (sort of), design, code, test and debug,
install, train, and document to the extent the client asked for. Was
this Agile-like?  Maybe it was only "Pre-Agile". Is it enough to give
me "license" to so engage you herein?

Ahhhh, I'm feeling "lucky", so what the heck...

Here is what someone more knowledgable than I on Agile has to say. On
the other hand, I have heard rumors that this certain Jason Gorham is
now "post-Agile", rather than "Agile." (Sidebar: "post-Agile" is a
term largely credited to Jon Kohl, a very nice young man who I have
met and who I like a lot. He can be found at
http://www.kohl.ca/blog/ )

Jason Gorham, http://parlezuml.com/blog/?sectionid=10

<begin Jason Gorham post>

__Quality Trends Can Reveal Inadequate Refactoring Effort__

A less pithy, and arguably far more constructive, answer to the
question "are we doing enough refactoring?" can be find by examining
how the quality of our code changes over time.

Take package-level coupling and cohesion, for example. if we want to
objectively gauge if we're doing enough to keep packages cohesive and
loosely coupled enough for our requirements, we can monitor those
aspects of quality as the project progresses and identify where the
trend might be headed.

<some stuff deleted>

Anyway, however often you choose to measure code quality, over time
you will doubtless notice a trend towards lowre quality as the code
grows and evolves. That's just natural code ageing, and it happens to
even the best development teams.

But better teams' code tends to age slower, because they put more
effort into keeping it "young" as they go.

If the trend tells you that inter-package coupling is probably going
to be too high by your release date, then you should consider putting
more effort into optimising that aspect of quality. Likewise for
package cohesion, or any other aspect of code quality you deem
important enough to monitor.

<stuff deleted>

I think you might be surprised at just how quickly code can age, and
just ___how much refactoring effort___ (emphasis added by KLS) is
really required to keep your code in good enough shape.

<end Jason Gorham post>

<<stuff deleted>>

[Ken]
>
> But rather than use those terms ("good" and "bad"), with their
> implied value judgments, should we not instead use the heuristics
> themselves, such as "this program shows good cohesion", and this
> program has "excessive coupling"?
[/Ken]

>
> [Pete]
…[3 more quoted lines elided]…
> [/Pete]

Well, yes, the same points still apply, but with the lowered decibel
level, maybe they are not even seen as "arguments"... rather, simply,
"differences."

<stuff deleted>

[Ken]
> I was persuaded again (by Constantine, et al.) to use the "structured
> design" techniques.
> I did not cultivate these concepts as the my own self-appointed pundit
> creations; I recognized them from someone smarter than me, and then
> internalized them best I knew how.
[/Ken]

>
> [Pete]
…[9 more quoted lines elided]…
> [/Pete]

Did it sound like Evangelizing? I thought it not - I did not ask you
for money, did I? :-) I thought that was one of the requirements to be
an Evangelist... Please see conclusion below...

>
<<stuff deleted>>

> An interesting post, Ken. I understand why you feel the way you do and I
> don't think you're "wrong". I do think that applying a subjective standard
> to people other than oneself may not be fruitful, even if that subjective
> standard works very well for the subject :-)...

Conclusion:
I am happy you found it interesting. But still I am unsure that you
"understand why [I] feel the way [I] do." So I will make a little more
effort...

Each of us is on Earth to work on a puzzle. Each one of us has a
different puzzle, though many puzzles overlap. None of us sees the Big
Puzzle, for that is only within the Realm of the Master Puzzlemaker.

Part of working on the puzzle involves finding people whose puzzles
overlap your puzzle, and who can help you work on it. But even those
whose puzzles do not overlap can help you, because by acknowledging
that you do not share their puzzle, you are farther along at finding
the people who do share your puzzle.

If I understand you, Mr. Pete, your puzzle involves something along
the lines of replacing procedural source with replaceable,
componentized, objects. (My words only, please feel free to tell me in
your own words what your "puzzle" is.)

My puzzle involves something along the line of "invariance" - what
aspects of "procedural source" will survive, and needs to be
maintained, in a way that we best can do. Finding people who see the
same "objective reality" of coupling and cohesion is part of that.

From my view, that is what is going on. That is all that is going on.
It is also, hmmmm, enough..., even _plenty_ enough.

Thank you for the time you have spent with me, and on my behalf ...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 17)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-10T10:28:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b3dbddb-3198-42e2-b312-734b2d081b4b@k13g2000hse.googlegroups.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net>`

```
I think my original Reply timed out... having saved the following in
Notepad ahead of time, I am re-posting... I apologize if there is any
duplication.... Ken


On Jun 10, 9:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
> news:491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com...
> My comments interspersed among Robert's and Pete's. At the
> (acceptable) risk of being branded a Robert-ista :-) ...

> [Ken]
>
…[14 more quoted lines elided]…
> as we start that argument we are into the realm of subjectivity and opinion.

[/Pete]

Hmmmmmm... then please allow me to re-phrase this way:
That structured programming, cohesion, and minimal coupling constitute
desirable program characteristics, and that those characteristrics are
real and objective, is a subjective _belief_ that I have. And I am
searching for others who believe that way. Because that Way is _my_
Path. If I understand you correctly, you are not on that Path, the
Path which is my Path. More at the end of this post.

[Pete]
>
> But this discussion is not about the goodness or badness of structured
…[5 more quoted lines elided]…
> becoming less and less relevant.

[/Pete]


I had not thought myself an "academic." On the other hand, one of my
shop's Business Analysts has taken to calling me "Professor". He, like
you, knows I teach Algebra one night a week. :-) Yes, I have a couple
of degrees on my resume. My career engagements (about thirty or thirty-
five in all), have been pretty evenly divided between government and
corporate. There was one engagement for a state college where I
installed a repeatable test generator. My partner did the English
portion; I did the Math portion. :-)

[Pete]
>
> > A blatant troll which I shall ignore...:-)
[/Pete]

[Ken]
>
> I did not view it as a troll.
[/Ken]

>
> [Pete]
…[6 more quoted lines elided]…
>

Hmmmm... after reading your last statement, and re-reading Robert's
post on Constantine, I still cannot see it as a troll. But how am I to
know what is in Robert's heart?

So I shall just ask him, and hear what he has to say, if he deems it
worthy of a reply:

Robert, were your comments on Constantine a troll?


[Ken]
> This also helps to explain the importance of "refactoring" to XP.
> Constantine, if he was not the first to use the term "factor" as in
…[7 more quoted lines elided]…
> incrementally.
[/Ken]

>
> [Pete]
…[4 more quoted lines elided]…
> be more amenable to discussion. :-)
[/Pete]

I will risk a tad bit more dialogue, anyway. The early systems I
developed, albeit fairly small, were done as Team of One. Many of us
old-timers remember the drill. Some conversations with the client,
list the requirements (sort of), design, code, test and debug,
install, train, and document to the extent the client asked for. Was
this Agile-like?  Maybe it was only "Pre-Agile". Is it enough to give
me "license" to so engage you herein?

Ahhhh, I'm feeling "lucky", so what the heck...

Here is what someone more knowledgable than I on Agile has to say. On
the other hand, I have heard rumors that this certain Jason Gorham is
now "post-Agile", rather than "Agile." (Sidebar: "post-Agile" is a
term largely credited to Jon Kohl, a very nice young man who I have
met and who I like a lot. He can be found at
http://www.kohl.ca/blog/ )

Jason Gorham, http://parlezuml.com/blog/?sectionid=10

<begin Jason Gorham post>

__Quality Trends Can Reveal Inadequate Refactoring Effort__

A less pithy, and arguably far more constructive, answer to the
question "are we doing enough refactoring?" can be find by examining
how the quality of our code changes over time.

Take package-level coupling and cohesion, for example. if we want to
objectively gauge if we're doing enough to keep packages cohesive and
loosely coupled enough for our requirements, we can monitor those
aspects of quality as the project progresses and identify where the
trend might be headed.

<some stuff deleted>

Anyway, however often you choose to measure code quality, over time
you will doubtless notice a trend towards lowre quality as the code
grows and evolves. That's just natural code ageing, and it happens to
even the best development teams.

But better teams' code tends to age slower, because they put more
effort into keeping it "young" as they go.

If the trend tells you that inter-package coupling is probably going
to be too high by your release date, then you should consider putting
more effort into optimising that aspect of quality. Likewise for
package cohesion, or any other aspect of code quality you deem
important enough to monitor.

<stuff deleted>

I think you might be surprised at just how quickly code can age, and
just ___how much refactoring effort___ (emphasis added by KLS) is
really required to keep your code in good enough shape.

<end Jason Gorham post>

<<stuff deleted>>

[Ken]
>
> But rather than use those terms ("good" and "bad"), with their
> implied value judgments, should we not instead use the heuristics
> themselves, such as "this program shows good cohesion", and this
> program has "excessive coupling"?
[/Ken]

>
> [Pete]
…[3 more quoted lines elided]…
> [/Pete]

Well, yes, the same points still apply, but with the lowered decibel
level, maybe they are not even seen as "arguments"... rather, simply,
"differences."

<stuff deleted>

[Ken]
> I was persuaded again (by Constantine, et al.) to use the "structured
> design" techniques.
> I did not cultivate these concepts as the my own self-appointed pundit
> creations; I recognized them from someone smarter than me, and then
> internalized them best I knew how.
[/Ken]

>
> [Pete]
…[8 more quoted lines elided]…
> [/Pete]

Did it sound like Evangelizing? I thought it not - I did not ask you
for money, did I? :-) I thought that was one of the requirements to be
an Evangelist... Please see conclusion below...

>
<<stuff deleted>>

> An interesting post, Ken. I understand why you feel the way you do and I
> don't think you're "wrong". I do think that applying a subjective standard
> to people other than oneself may not be fruitful, even if that subjective
> standard works very well for the subject :-)...

Conclusion:
I am happy you found it interesting. But still I am unsure that you
"understand why [I] feel the way [I] do." So I will make a little more
effort...

Each of us is on Earth to work on a puzzle. Each one of us has a
different puzzle, though many puzzles overlap. None of us sees the Big
Puzzle, for that is only within the Realm of the Master Puzzlemaker.

Part of working on the puzzle involves finding people whose puzzles
overlap your puzzle, and who can help you work on it. But even those
whose puzzles do not overlap can help you, because by acknowledging
that you do not share their puzzle, you are farther along at finding
the people who do share your puzzle.

If I understand you, Mr. Pete, your puzzle involves something along
the lines of replacing procedural source with replaceable,
componentized, objects. (My words only, please feel free to tell me in
your own words what your "puzzle" is.)

My puzzle involves something along the line of "invariance" - what
aspects of "procedural source" will survive, and needs to be
maintained, in a way that we best can do. Finding people who see the
same "objective reality" of coupling and cohesion is part of that.

From my view, that is what is going on. That is all that is going on.
It is also, hmmmm, enough..., even _plenty_ enough.

Thank you for the time you have spent with me, and on my behalf ...

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-06-11T18:41:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b9adkF3ameasU1@mid.individual.net>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <6b22osF39l4mnU1@mid.individual.net> <491a042e-f2b3-45af-ae38-dc7a162a7917@i76g2000hsf.googlegroups.com> <6b7datF3be0odU1@mid.individual.net> <7b3dbddb-3198-42e2-b312-734b2d081b4b@k13g2000hse.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:7b3dbddb-3198-42e2-b312-734b2d081b4b@k13g2000hse.googlegroups.com...
>I think my original Reply timed out... having saved the following in
> Notepad ahead of time, I am re-posting... I apologize if there is any
…[60 more quoted lines elided]…
> I had not thought myself an "academic."

The word "academic" has more meanings than "pertaining to Acadaemia"...


>On the other hand, one of my
> shop's Business Analysts has taken to calling me "Professor". He, like
…[70 more quoted lines elided]…
>

No. Conversations with the client, while valuable, do not in and of 
themselves make a development Agile. I'm making no further comment on this. 
Anyone who wants to know what is and isn't Agile, should read their web site 
and engage in their forums.

> Ahhhh, I'm feeling "lucky", so what the heck...
>
…[112 more quoted lines elided]…
>

I disagree, but I do so gently... :-)

> Part of working on the puzzle involves finding people whose puzzles
> overlap your puzzle, and who can help you work on it. But even those
…[7 more quoted lines elided]…
> your own words what your "puzzle" is.)

I don't see computer programming as a puzzle at all. My "puzzle" as you put 
it is much bigger than that :-)

>
> My puzzle involves something along the line of "invariance" - what
…[7 more quoted lines elided]…
> Thank you for the time you have spent with me, and on my behalf ...

Your courtesy is creditable and your gentleness is very welcome in CLC. Five 
to ten years ago I would have been happy to debate this with you. Not now. I 
simply have neither time nor inclination for debates where no minds are 
likely to be changed:-). There is nothing wrong with the principles you have 
espoused and you have misunderstood if you think I am opposed. I can 
summarize my position with two statements:

1. There are many "right" ways to program computers. It depends on 
subjective judgements and priorities. Even within the same paradigm, what is 
"good" and what is "bad" is very often a matter of opinion and priorities.

2. The whole subject of computer programming is of dimininshing relevance in 
today's world. This is because hardware performance is ever increasing, code 
is being generated automatically, the action of "computer programming" is 
becoming higher level and more visual , thereby requiring less technical 
skill (the visual IDE can "steer" the programmer), and code is inevitably 
reused rather than being written from scratch.

I would add a final rider that, in my opinion, criticising code produced by 
other people (especially when they are not present) is neither professional, 
mature, nor helpful. This would only be acceptable in a code review session 
or workshop where the purpose was to improve the general standard of code 
(by mutual agreement).

During my working career I have been exposed to code (in a number of 
languages) that made me swear, sometimes even get angry. But you grow... :-) 
These days I see it as something broken that needs fixing. A challenge to my 
skill, and a chance to get some job satisfaction by solving it.:-)

I have noticed that the job of programming has become significantly easier 
in the last few years. This is due to far better support of the process by 
both software and hardware, and also by using different development 
techniques. It is only a matter of time before "programming" (in the sense 
of cobbling lines of source code together)  is rendered moot...

Pete.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 14)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-09T10:02:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa766236-61c4-4c90-8b03-6fd1849b8288@59g2000hsb.googlegroups.com>`
- **References:** `<eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com>`

```
On Jun 7, 10:11 pm, Robert <n...@e.mail> wrote:
> >> Starving the interface is a bad idea. Rather than passing four data
> >> structures, they'll
…[7 more quoted lines elided]…
>

I'm unsure that I understand you. Nevertheless, here is my opinion, in
the context of my understanding of coupling and cohesion...

Generally, the fewer parameters passed to a subprogram/subroutine, the
better. A large number of parameters passed, either to or from, is a
"clue" that the invoked module may be performing more than one
"function" (somewhat vague, I grant you), and thus is not as
"cohesive" as it should be. (Because functional cohesion is the
highest level of cohesion. Said for the benefit of others, because I
know you already know this :-).)

Passing more "parameters", or "fields" to an invoked module, than it
really needs, may tempt the coder to "use" those fields in the invoked
module, thus weakening it cohesion. That is why, in the absence of
other all-other-considerations, it is better to pass four parameters
than five.

And "packaging" the four parameters into one customized (for purpose
of invocation) structure so that only _one_ parameter is passed is a
"sleight of hand" which though it may "conform to shop standards, in
perverted form", does not reduce the coupling in fact.

There are tradeoffs to be made here. We all make compromises. If a
record-level structure has the three or four things that the invoked
module needs, yeah, go ahead and pass it in its entirety. But Mr.
Klein has given us the syntax to "mask out" the things we don't need
in the linkage section COPYLIB, so that the invoked module isn't
tempted to "do mischief" beyond its "authority" of designed scope.

Not that I would advocate doing that in COBOL. I've never seen it done
that way. But I have seen it, and did it myself, in passing labeled
COMMON in FORTRAN. If there were large areas of the COMMON area not to
be used by the subroutine, we masked them out such as IARRAY(100),
IDUMMY1(367), ICMD(10), IDUMMY2(28), IRETURN.

The invoked module was thus "permitted" to use IARRAY and ICMD and to
return result in IRETURN. Areas masked in IDUMMY1 and IDUMMY2 were not
needed, and because they were masked, the coder of the subordinate
module was not ever tempted to use them.

Thus was the interface "starved", and "cohesion" protected (best as
could be).

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-09T20:34:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62gr44dbsntvq2pe14cod8jopb7ikt2q14@4ax.com>`
- **References:** `<i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com> <f34e52e6-845f-4aa1-b23d-ce31f9102f4b@y38g2000hsy.googlegroups.com> <h1sg449kgpj00nma7hqv6rtk5cg86urr8u@4ax.com> <030f28cb-22dc-4fdc-95bc-b27d26c58b87@25g2000hsx.googlegroups.com> <06hj44p207vmj5c91cj74j7r1sps1l0q4v@4ax.com> <6aun0nF39kcpkU1@mid.individual.net> <c95m44ddugnkmvqgdrjni21an1f967qmp9@4ax.com> <aa766236-61c4-4c90-8b03-6fd1849b8288@59g2000hsb.googlegroups.com>`

```
On Mon, 9 Jun 2008 10:02:35 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jun 7, 10:11ï¿½pm, Robert <n...@e.mail> wrote:
>> >> Starving the interface is a bad idea. Rather than passing four data
…[30 more quoted lines elided]…
>perverted form", does not reduce the coupling in fact.

You just stated what I meant. Copying four variables to a fifth structure doesn't simplify
anything, it adds four unnecessary MOVE statements. 

Plus, it obscures the fact that the called program is referencing four structures. 

>There are tradeoffs to be made here. We all make compromises. If a
>record-level structure has the three or four things that the invoked
…[3 more quoted lines elided]…
>tempted to "do mischief" beyond its "authority" of designed scope.

The blocking structure redefining the original structure is little different from a
customi interface block.  PIC X redefining non-string types is error-prone. 
You might make an error in addition. Someone might add a field in the middle. 
The size of a tiny binary might change from one to two bytes. 

If you fear your own programs doing mischief, you should be in security rather than
development. 

>Not that I would advocate doing that in COBOL. I've never seen it done
>that way. But I have seen it, and did it myself, in passing labeled
…[7 more quoted lines elided]…
>module was not ever tempted to use them.

Tempted? If a future change adds another parameter, you need only change the called
program. That's simpler than changing three lines in a blocking structure, or adding a
variable to a custom structure and a MOVE. Then forgetting to change another caller, and
getting garbage in the new field. 

>Thus was the interface "starved", and "cohesion" protected (best as
>could be).

If you want to starve the interface, passing four variables individually takes less code
than four MOVEs.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 8)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-06-06T09:05:18+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2anjd$mjd$1@nntp.fujitsu-siemens.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com>`

```

"Robert" <no@e.mail> schrieb im Newsbeitrag 
news:i18g44l3vi50ou89394o14okkfkjjv0kaa@4ax.com...
> On Thu, 5 Jun 2008 09:29:35 -0700 (PDT), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[8 more quoted lines elided]…
> beginning of a program.

Considering the extension to the INITIALIZE statement in COBOL STD2002, 
VALUES might not be such a bad idea - at least if the same initial values 
are needed by several procedures: INITIALIZE...TO VALUE will restore these 
values without requiring the user to provide these values explicitly.

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-05T20:20:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yUX1k.84719$RG7.83614@fe09.news.easynews.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com...
On Jun 5, 10:25 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
><snip>
Forgive me, for I imagine others have asked this before, but what is
the compiler default for assigning values to PIC X fields if there is
no VALUE clause? I had always heard "don't count on anything, it will
be random memory values", but maybe compiler behavior has "saved the
day" on this second program.

The answers from a Standards point-of-view is that results are unpredictable.

If, as I think you indicated, you are using a "current" IBM z/OS COBOL compiler, 
(probably Enterprise COBOL), then results are unpredictable (and they really CAN 
vary).  However, this also dpends on the STORAGE LE run-time option.  If, as 
many shops do, your shop specifies (or this application specifies STORAGE=("00", 
....) then this means that Working-Storage items that aren't redefined and dont' 
have a value clause) will be initialized to low-values (i.e. X"00").  Other 
values (including X"40" or EBCDICspaces) are also possible.

Whatever the application is getting today, IBM does NOT guarantee that it will 
in the future - unless the LE STORAGE option is specified.

FYI, if applications have started using the "newere" LOCAL-STORAGE SECTION (as 
well as Working-Storage) then another LE run-time options tells what to do with 
those items if no VALUEclause is specified.  This becomes much more expensive 
(for performance) for Local-Storage, but it is considered "good programming" to 
always take of data item initialization explicity within your program IF you 
rely on what the data item has.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-05T19:26:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br0h44hadh1lbgmjktk9h0fo54g96hua7g@4ax.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <yUX1k.84719$RG7.83614@fe09.news.easynews.com>`

```
On Thu, 05 Jun 2008 20:20:47 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>
><klshafer@att.net> wrote in message 
…[17 more quoted lines elided]…
>values (including X"40" or EBCDICspaces) are also possible.

I like the idea of initializing it to something distinctive, such as "?". Then you can
readily see it was never initialized in printouts, files and memory dumps. And no one will
be temped to rely on it.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-06T09:37:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <Zty1k.386894$qg2.76630@fe08.news.easynews.com> <dbced165-43a7-4657-8cd0-ac7e5a5f8b64@59g2000hsb.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com>`

```
klshafer@att.net wrote:
>
> Nevertheless, from time to time I am amazed how some systems work in
> spite of themselves...
>

Dirty little secret: They don't work.

Funtional Indeterminacy Theorem (FIT)

"In complex systems, malfunction and even total non-function may not be 
detectable for long periods, if ever. Such systems may, however, persist 
indefinitely or even expand.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-06T14:58:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2bjba$ob6$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>`

```
In article <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>klshafer@att.net wrote:
>>
…[4 more quoted lines elided]…
>Dirty little secret: They don't work.

Hmmmm... seems like a lot of people are keeping quiet when they don't get 
paid because the payroll system I'm working on 'don't work'.

>
>Funtional Indeterminacy Theorem (FIT)
…[3 more quoted lines elided]…
>indefinitely or even expand. 

Human beings are, quite often, born with vermiform appendices.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 9)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-06-07T07:36:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pUq2k.25111$102.13477@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<g2bjba$ob6$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com> <g2bjba$ob6$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[18 more quoted lines elided]…
> 

It appears that the vermiform appendix might have some useful function 
after all, as part of the human immune system:

http://en.wikipedia.org/wiki/Vermiform_appendix
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-08T12:49:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2gkhh$mhu$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com> <g2bjba$ob6$1@reader2.panix.com> <pUq2k.25111$102.13477@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <pUq2k.25111$102.13477@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>docdwarf@panix.com wrote:
>> In article <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>,
…[21 more quoted lines elided]…
>http://en.wikipedia.org/wiki/Vermiform_appendix

It seems that it is still being researched, Mr Trembley... and if things 
get demonstrated with a sufficient amount of Scientific Certainty then the 
entry of http://en.wikipedia.org/wiki/Vestigial_structure#Humans might 
need to be changed.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 9)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-06-07T14:35:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<voKdnTjd0oF2f9fVnZ2dnUVZ_q3inZ2d@earthlink.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com> <g2bjba$ob6$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[9 more quoted lines elided]…
> get paid because the payroll system I'm working on 'don't work'.

You just haven't hit all the bugs yet. A company I used to work for did 
payroll for some clients. The program, which had worked flawlessly for many 
a year, had an internal limit as to how much it could deduct for SSI. Sure 
enough, the limit was hit, but nobody noticed until the W2s were printed.

Then they noticed.

'Til this day there is a debate as to whether it was a "flailing" or a 
"flogging."

If I were you, I'd leave while everything seems to be working swell. Or hide 
the whips.
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 10)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-07T14:46:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SAB2k.178$cW3.7@nlpi064.nbdc.sbc.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <eeadneNEXvHPatrVnZ2dnUVZ_gqdnZ2d@earthlink.com> <afec2bd6-5a37-4af3-b6d4-9450211f1893@i76g2000hsf.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com> <g2bjba$ob6$1@reader2.panix.com> <voKdnTjd0oF2f9fVnZ2dnUVZ_q3inZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:voKdnTjd0oF2f9fVnZ2dnUVZ_q3inZ2d@earthlink.com...
> docdwarf@panix.com wrote:
> You just haven't hit all the bugs yet. A company I used to work for did 
…[5 more quoted lines elided]…
> Then they noticed.

Reminds me of a similar story from my time with Systems Design Inc. 
(1983-88)

No, our payroll software did not exceed any dollar limits (everything was 
PICTURE S9(9)V9(2)), but we did have one  client complain about his payroll 
check printing routine. It truncated the "Federal Withholding Tax" to 
9(5).99... the size of the column on the client-provided form.

Strangely enough, absolutely *none* of my programmers felt any sympathy.. 
after all, the truncated field was "Federal Witholding *this pay period*" 
(At this time, $35,000 or $40,000 per YEAR was pretty good GROSS pay for a 
programmer).

MCM
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-08T12:54:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2gkph$4ti$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com> <g2bjba$ob6$1@reader2.panix.com> <voKdnTjd0oF2f9fVnZ2dnUVZ_q3inZ2d@earthlink.com>`

```
In article <voKdnTjd0oF2f9fVnZ2dnUVZ_q3inZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <m6ednQ18vOUU1tTVnZ2dnUVZ_j6dnZ2d@earthlink.com>,
…[12 more quoted lines elided]…
>You just haven't hit all the bugs yet.

That a system has undiscovered bugs - as, I have been taught, all systems 
do - then those don't seem to be making the system 'not work'.

>A company I used to work for did 
>payroll for some clients. The program, which had worked flawlessly for many 
>a year, had an internal limit as to how much it could deduct for SSI. Sure 
>enough, the limit was hit, but nobody noticed until the W2s were printed.

Times changed and the system didn't change... until it had to.  To limit 
storage to (size) requires constant monitoring so that storage can be 
changed to (larger size) before a user is adversely effected.

>
>Then they noticed.
…[5 more quoted lines elided]…
>the whips.

I am me and my experience tells me that it doesn't matter when I leave... 
anything that goes wrong gets blamed on the Previous One Out the Door.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-04T15:47:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g26df3$979$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com>`

```
In article <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 4, 10:39�am, docdw...@panix.com () wrote:
>> In article <1f980664-cc0e-4577-bd77-b0476d9a2...@56g2000hsm.googlegroups.com>,
…[20 more quoted lines elided]…
>called subprogram (just to be "safe").

How curious... it is Shop Standard, then, to recompile all programs 
containing a copybook that gets changed?

>
>So the migration complexity measure is -
…[4 more quoted lines elided]…
>recompile main program, recompile subprogram = complexity of 3 tasks.

Ahhhhh... so they leave it to the programmer to determine what needs 
recompilation due to a change!  They deserve what they get.

>This difference is small, but nonzero, in a shop which migrates,
>tests, and promotes source and executables cautiously.

If caution is being exercised - as opposed to 'make folks do more work 
with a lack of certainty about thoroughness' - then the decision would not 
rest with one who is knee-deep in code.  A change would be made, whether 
to a program, copybook, screen or subroutine, and Production 
Implementation Control Committee, at its semi-weekly meeting, would 
determine what needs to be modified in order to accomodate the change.

(this prevents a programmer's changing, say, a LINKAGE copybook and then 
forgetting/not being aware that Very Important Programs need to reflect 
such)

>
>Come to think of it, since I don't really care, this is the PERFECT
>question to place before He-who-signs-my-timesheet, so that he may
>exude management-control, and receive the euphoria which is its
>consequence of that decision-making.

Beware of what you ask for, Mr Shafer, lest you receive it.  I have known 
Managers (in shops where there is no documentation outside of 
text-searching libraries (SUPERC) or text-searching Librarian libraries 
(ESCLIBR)) to ask for lists of all programs which reference (fieldname)... 
no, not *all* programs, that's too many, just programs in the Payroll 
system... no, still too many, just in the Accounts Receivable subsystem... 
no, too many... just in the Accounts Receivable subsystem that have been 
compiled in the past three years... what's the matter, why does it take 
These Consultants so long to answer a simple question?

>
>Such are the Zen-ways of Managing Your Manager. Or so I would like to
>think.

It might be best to adopt a tactic from the Noble Bar and try to make sure 
never to ask a Timesheet Signer any question that you do not already know 
how it will be answered.

>
>But enough about me. What do YOU think of what _I_ think? :-)

I can barely think about what you communicate, let alone what you think.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 4)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-04T10:16:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <g26df3$979$1@reader2.panix.com>`

```
On Jun 4, 11:47 am, docdw...@panix.com () wrote:
> In article <519cc534-2596-4766-a9c3-333fb73c2...@j22g2000hsf.googlegroups.com>,
>
…[12 more quoted lines elided]…
>

Well, in a word, "no".  It also not a Shop Standard, where I work, to
re-test all main programs when a called subprogram is changed (or at
least to do a cursory impact assessment.)

Probably, in the thinking of where I am, those would be
characteristics of "advanced shops" :-).

Lacking that maturity, other Teams have experienced much wailing and
gnashing of teeth upon the occurrence of "things-that-used-to-work-
don't-work-anymore", and the subsequent production-itis interruptus.

I will be gentle. To "acclimate" them to the benefits of these
practices, I will introduce them in situations "where it doesn't
really matter." They do not yet have the powers of discrimination to
determine when to and when not to, anyway. Such powers of
discrimination are beyond "advanced shops", and reside only in "very
advanced shops". :-)

>
> Ahhhhh... so they leave it to the programmer to determine what needs
> recompilation due to a change!  They deserve what they get.

Well, they deserve to be, uh, _helped_. As do I. As do you, or so I
choose to believe.

> (this prevents a programmer's changing, say, a LINKAGE copybook and then
> forgetting/not being aware that Very Important Programs need to reflect
> such)
>

Yes, indeed, that is where it is. In the LINKAGE section.

>

> Beware of what you ask for, Mr Shafer, lest you receive it.  I have known
> Managers (in shops where there is no documentation outside of
…[7 more quoted lines elided]…
>

Ahhh, yes, Master DocDwarf, it is part of the Journeyman's Master Plan
to introduce them to "Ways of grep, awk, and sed", and to let go of
SUPERC. It is a Plan which probably should be thought of as a One Year
Plan, no - a Three Year Plan, no - a Five Year Plan. Well, a Plan of
Indeterminate Length, but no matter, as long as we go in That
Direction.

> >Such are the Zen-ways of Managing Your Manager. Or so I would like to
> >think.
…[4 more quoted lines elided]…
>

Hmmmm... I first heard this mantra (in its most generic form) from
Bruce Williams, the Talk Show Host. Something along the lines of,
"Never ask an important question for which you don't already know the
answer."

>
>
…[3 more quoted lines elided]…
>

I am flattered, O Wise One, I say, blushing. I too aspire to a Special
Transcendence whereby I may work and communicate and yet never have to
think at all. Sort of like Wally in Dilbert. It may take many
lifetimes to achieve it.

Thanks,
Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-04T17:48:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g26khb$6gm$1@reader2.panix.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <g26df3$979$1@reader2.panix.com> <cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com>`

```
In article <cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jun 4, 11:47�am, docdw...@panix.com () wrote:
>> In article
…[17 more quoted lines elided]…
>Well, in a word, "no".

Such a compact word... there's scarcely enough space in it to include the 
variations between the alternatives!

>It also not a Shop Standard, where I work, to
>re-test all main programs when a called subprogram is changed (or at
…[3 more quoted lines elided]…
>characteristics of "advanced shops" :-).

One person's 'advancement' may be another's 'unnecessary complexity', 
one's sees 'simplicity', another's 'primitive unsophistication'.

There are times when a 'this won't have an affect' are right... and times 
when it causes a Corner Office Idiot to call everyone who is capable of 
actually fixing the problem into the Corner Office to explain to said 
Idiot - a proudly Non-Technical Person - just what went wrong, how they 
are going to fix it and why it will never, ever happen again.

[snip]

>I will be gentle. To "acclimate" them to the benefits of these
>practices, I will introduce them in situations "where it doesn't
>really matter."

It is not easy to know which situations will come back to bite if one has 
no scars... and having scars is no guarantee that one will be able to 
avoid future bites.  What is Life without a bit of Uncertainty?

[snip]

>>
>> Ahhhhh... so they leave it to the programmer to determine what needs
…[3 more quoted lines elided]…
>choose to believe.

It is one thing to help, it is another thing to stem a rot which 
originates from the head.  'This axe needs fixing... replace the haft, 
replace the blade and it will be fine.'

>> (this prevents a programmer's changing, say, a LINKAGE copybook and then
>> forgetting/not being aware that Very Important Programs need to reflect
>> such)
>
>Yes, indeed, that is where it is. In the LINKAGE section.

It was a lucky guess, that is all.

>> Beware of what you ask for, Mr Shafer, lest you receive it. �I have known
>> Managers (in shops where there is no documentation outside of
>> text-searching libraries (SUPERC) or text-searching Librarian libraries
>> (ESCLIBR)) to ask for lists...

[snip... and pardon me for interrupting myself]
>
>Ahhh, yes, Master DocDwarf, it is part of the Journeyman's Master Plan
>to introduce them to "Ways of grep, awk, and sed", and to let go of
>SUPERC.

No 'Master' I, jes' ol' Doc... and what is less important is the tool 
used, what is more important is the reason and end.  If the reason and end 
are 'a systemwide data dictionary, relating fields and copybooks to the 
programs which use them, programs to the systems that use them and systems 
to the departments that use them' then it might be a Good Idea to evaluate 
other tools.

(the inevitable objection of 'But those cost *money*!' should be met with 
'so do man-hours spent, XIO spun and CPU burned using inappropriate tools 
to manage the system')

>It is a Plan which probably should be thought of as a One Year
>Plan, no - a Three Year Plan, no - a Five Year Plan. Well, a Plan of
>Indeterminate Length, but no matter, as long as we go in That
>Direction.

Very good... it is not the destination, it is the journey... except when 
one is going to the bank to deposit one's paycheck/que; this may be why 
Direct Deposit could lead to keeping the electricity paid-for and yet fall 
short of being Enlightening.

[snip]

>> >But enough about me. What do YOU think of what _I_ think? :-)
>>
…[5 more quoted lines elided]…
>lifetimes to achieve it.

I'm a Wise Guy?  Hey, Porcupine, pick two!  All I aspired to above was a 
variant of Wittgenstein's 'I cannot know what you mean, only what you 
say'... but if you find a compliment there then please, think nothing of 
it.

DD
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 5)_

- **From:** Robin Lee <robinlee@news.com>
- **Date:** 2008-06-08T16:06:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Taqdnes6BfBuptHVnZ2dnUVZ_qjinZ2d@giganews.com>`
- **In-Reply-To:** `<cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <g26df3$979$1@reader2.panix.com> <cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com>`

```
Um, I can only say that this is probably the most interesting thread I've seen 
anywhere in many years. The conditions and situations in this scenario are oh so 
familiar, yet described with refreshingly brilliant humor.

It would be interesting to see just where this "7-10 year" system migration is in, 
oh, say 12 years.


klshafer@att.net wrote:
> > 
> Thanks,
> Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 6)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-06-13T14:00:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<075178f1-fa69-4b94-ac73-0b7981ee6aec@m44g2000hsc.googlegroups.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <g26df3$979$1@reader2.panix.com> <cc543230-a71a-408a-b270-ef90f4a631b6@d45g2000hsc.googlegroups.com> <Taqdnes6BfBuptHVnZ2dnUVZ_qjinZ2d@giganews.com>`

```
On Jun 8, 4:06 pm, Robin Lee <robin...@news.com> wrote:
> Um, I can only say that this is probably the most interesting thread I've seen
> anywhere in many years. The conditions and situations in this scenario are oh so
…[4 more quoted lines elided]…
>

Thanks for noticing, Mr. Robin Lee... and though the future is
difficult to divine, and it is uncertain where this 7-10 year effort
will be "in, oh, say 12 years", we have the following "anecdote" to
help guide us...

Recently our project hired a subject matter expert (SME) to help us;
in fact, we hired him away from a _similar_ effort being undertaken by
a similar sized organization, in the same "application" domain, about
800-1000 miles away, which is attempting a "similar" replacement.
Replacing COBOL with Java, or so it is rumored.

He brought us this News Update: after _one year_ of effort toward said
"replacement", their ... best ... estimate ... of ... how... far ...
behind ... schedule ... they ... are ... is... (are you ready for
this?) - is _one year_.

Students are invited to draw their own conclusions. Quiz at 11:30pm,
after Weather and Sports.

Ken
```

###### ↳ ↳ ↳ Re: Why read CLC?

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-08T20:29:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<al0p441fh8an4b9db7h1iefiklk0av5i3d@4ax.com>`
- **References:** `<1f980664-cc0e-4577-bd77-b0476d9a2b83@56g2000hsm.googlegroups.com> <g269ei$ho7$1@reader2.panix.com> <519cc534-2596-4766-a9c3-333fb73c2167@j22g2000hsf.googlegroups.com> <g26df3$979$1@reader2.panix.com>`

```
On Wed, 4 Jun 2008 15:47:48 +0000 (UTC), docdwarf@panix.com () wrote:

>If caution is being exercised - as opposed to 'make folks do more work 
>with a lack of certainty about thoroughness' - then the decision would not 
…[7 more quoted lines elided]…
>such)

In all Unix and many Windows environments, the build would be controlled by a 'make file'
that knew about dependencies. Every program using the changed copybook would be compiled
automatically. 

There is something wrong with a methodology that deliberately puts components out of sync.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
