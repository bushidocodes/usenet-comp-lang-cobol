[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hex Value Moves

_17 messages · 6 participants · 2007-05 → 2007-06_

---

### Hex Value Moves

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-31T13:55:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3mk4b$ms0$1@reader2.panix.com>`

```

All righty... it has been discussed here and I had a few moments to spare 
(and some client CPU cycles to burn) so I descended into... The Temple of 
Truth.  Given the code:

 IDENTIFICATION DIVISION.                           
 PROGRAM-ID.  SKEL1.                                
 ENVIRONMENT DIVISION.                              
 CONFIGURATION SECTION.                             
 SPECIAL-NAMES.                                     
       SYMBOLIC CHARACTERS                          
             SPECNAM-CH-E5 IS 230.                  
 DATA DIVISION.                                     
 WORKING-STORAGE SECTION.                           
 01  CH-E5-BIN        PIC S9(4) COMP  VALUE +229.   
 01  FILLER REDEFINES CH-E5-BIN.                    
     02  FILLER       PIC X.                        
     02  CH-E5        PIC X.                        
 01  CH-E5-IN-WS      PIC X VALUE X'E5'.            
 01  TESTCHAR01A      PIC X VALUE SPACES.           
*                                                   
 PROCEDURE DIVISION.                                
     DISPLAY '  BEGIN: '.                           
     DISPLAY ' '.                          
*                                          
     MOVE X'E5' TO TESTCHAR01A.            
     IF TESTCHAR01A = CH-E5-IN-WS AND      
        CH-E5-IN-WS = CH-E5       AND      
        CH-E5       = SPECNAM-CH-E5        
         DISPLAY '!! ALL EQUAL'            
     ELSE                                  
         DISPLAY '!! NOT EQUAL'.           
*                                          
     MOVE SPECNAM-CH-E5  TO TESTCHAR01A.   
     MOVE CH-E5          TO TESTCHAR01A.   
     MOVE CH-E5-IN-WS    TO TESTCHAR01A.   
     GOBACK.                               

... and the compiler of IBM Enterprise COBOL for z/OS  3.4.1 ... and a 
bunch of invocation parameters including, but not limited to, 
'SIZE(MAX),LIB,MAP,DYNAM,LIST,XREF,OPT,FLAG(I,I),NUMPROC(PFD),' (reasons 
for said options including, but not limited to, 'I had 'em hangin' 
around') ...

... then the SYSOUT of the job's run included:

  BEGIN:    
            
!! ALL EQUAL

Now comes the Deeper Stuff... and, in a nutshell, all MOVEs compiled into 
MVI statements...

... EXCEPT for the next-to-last, MOVE CH-E5 TO TESTCHAR01A; this resulted 
in (some editing in an attempt to improve legibility):

000030  MOVE 
  000342  D200 3010 3001  MVC 16(1,3),1(3)  TESTCHAR01A  CH-E5

According to the Data Division Map everything winds up as a DS 1C.  Since 
CH-E5 is subordinate to the group-level FILLER it has a displacement 
associated with it that the other WS fields do not, eg (some editing as 
above):

CH-E5 . . . . . . . . . . . . . . BLW=00000 001 0 000 001 DS 1C
CH-E5-IN-WS . . . . . . . . . . . BLW=00000 008           DS 1C

... and this may account for the difference.

Now... the question becomes, of course, 'does any of this make a 
difference?'... and the answer is a most definite 'probably not'.

What does the code do?  My guess, based on the NewLine and FormFeed 
instructions, is that based on an online transaction (it is CICS code) 
that something gets spooled to print.  

So... what's the volume of printed material?

That is unknown... but given the old standard (Murach, I think) that an 
MVC takes three times as long as an MVI then I'd conclude that the 
strictly scientific quantity of 'a whole bunch' of printing would have to 
be done using this program in order to justify the cost of recoding, 
testing and redeploying code that has been tooling along rather nicely for 
the past thirteen years or so.

My views are based on the code and my experience... and are, quite 
obviously, worth at least double what I have been asking folks to pay for 
them here.

DD
```

#### ↳ Re: Hex Value Moves

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-05-31T22:27:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DZH7i.194382$865.167087@fe05.news.easynews.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com>`

```
It would be (sort-of) interesting to see what changes in
  NUMPROC
    and
  TRUNC

do to the pseudo-assembler (if anything)
```

##### ↳ ↳ Re: Hex Value Moves

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-31T23:47:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3nmqg$ip7$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com>`

```
In article <DZH7i.194382$865.167087@fe05.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>It would be (sort-of) interesting to see what changes in
>  NUMPROC
…[3 more quoted lines elided]…
>do to the pseudo-assembler (if anything)

Hmmmm... I usually leave such things to folks better-versed in such 
matters than I am but I'm willing to try.  Can you provide a list of 
combinations of various NUMPROC and TRUNC possibilities you'd like to see 
fed in?

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-06-01T04:28:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ufN7i.196678$865.96862@fe05.news.easynews.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com>`

```
TRUNC(OPT),NUMPROC(NOPFD)

TRUNC(STD),NUMPROC(MIG)

and what you already did, should show if this make any difference.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-06-01T14:08:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3p28o$mfb$02$1@news.t-online.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com>`

```
Well, of course, everything is solved with
BINARY-CHAR UNSIGNED :-)
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 5)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-01T07:29:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UiU7i.7095$C96.6580@newssvr23.news.prodigy.net>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p28o$mfb$02$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message 
news:f3p28o$mfb$02$1@news.t-online.com...
> Well, of course, everything is solved with
> BINARY-CHAR UNSIGNED :-)

"Solved?"  There never was a 'problem' to 'solve' in the first place

A numeric literal is a numeric literal is a numeric literal regarless of the 
written form or radix thereof and there are rules applying to the use of 
numeric literals as the source operand in a MOVE statement. (As in "RTFM").

Whether or a not a specific make and model of a compiler accepts those 
numeric literals in decimal, hexadecimal, octal, binary or purple is 
compiler-dependent (Also as in "RTFM") .

No one dealt with the real 'problem' here: The USE of inline numeric 
literals rather than constants (if supported by compiler) or VALUE clauses 
in the DATA DIVISION is just begging for a maintenance nightmare.

MCM
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-01T13:06:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3p5kl$muj$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p28o$mfb$02$1@news.t-online.com> <UiU7i.7095$C96.6580@newssvr23.news.prodigy.net>`

```
In article <UiU7i.7095$C96.6580@newssvr23.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"Roger While" <simrw@sim-basis.de> wrote in message 
>news:f3p28o$mfb$02$1@news.t-online.com...
…[3 more quoted lines elided]…
>"Solved?"  There never was a 'problem' to 'solve' in the first place

[snip]

>No one dealt with the real 'problem' here: The USE of inline numeric 
>literals rather than constants (if supported by compiler) or VALUE clauses 
>in the DATA DIVISION is just begging for a maintenance nightmare.

Leaving aside the logic of 'There never was a 'problem'... the real 
'problem' here'... the way the program was written and used allowed for it 
to run untouched for almost a decade-and-a-half... and when it came time 
to change it I'd say that the skills required should be well within the 
set carried by a three-to-nine year programmer... well, closer to nine 
than to three, granted, but still within the 'journeyman' level.

Given that level of skill (and access to a standard development 
environment, without 'Please, DBA, compile my code?') then I would 
estimate resource use to be four hours of the programmer's time (excluding 
time to fill out paperwork to check out and check in the source, notify 
the testing team that the code is ready, etc.) and enough machine time to 
allow for a half-dozen compiles and tests.

As to whether or not a program has been written in a fashion which 
requires this kind of personnel/resource allocation for enhancement after 
thirteen years of acceptable performance is 'begging for a maintenance 
nightmare'... that conclusion will be left to the reader.  I, personally, 
would think it to be a rather... choosy beggar, but that, quite obviously, 
is a matter of opinion.

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-01T12:52:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3p4ps$biq$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com>`

```
In article <ufN7i.196678$865.96862@fe05.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>TRUNC(OPT),NUMPROC(NOPFD)
>
>TRUNC(STD),NUMPROC(MIG)
>
>and what you already did, should show if this make any difference.

Well, let's see... what I already did used NUMPROC(PFD) and TRUNC(STD); 
that resulted in everything being an MVI except for the subordinate item.

Using TRUNC(OPT),NUMPROC(NOPFD) gives the same result.

Using TRUNC(STD),NUMPROC(MIG) gives the same result.

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-06-01T16:37:03+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l68063lmfgt7612jq0pvfc9sg4ijbdv0gr@4ax.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p4ps$biq$1@reader2.panix.com>`

```
On Fri, 1 Jun 2007 12:52:12 +0000 (UTC) docdwarf@panix.com () wrote:

:>In article <ufN7i.196678$865.96862@fe05.news.easynews.com>,
:>William M. Klein <wmklein@nospam.netcom.com> wrote:
:>>TRUNC(OPT),NUMPROC(NOPFD)

:>>TRUNC(STD),NUMPROC(MIG)

:>>and what you already did, should show if this make any difference.

:>Well, let's see... what I already did used NUMPROC(PFD) and TRUNC(STD); 
:>that resulted in everything being an MVI except for the subordinate item.

:>Using TRUNC(OPT),NUMPROC(NOPFD) gives the same result.

:>Using TRUNC(STD),NUMPROC(MIG) gives the same result.

Of course.

I don't see any numeric non-literal operations.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-06-01T22:31:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K618i.65182$3h2.55933@fe08.news.easynews.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <DZH7i.194382$865.167087@fe05.news.easynews.com> <f3nmqg$ip7$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p4ps$biq$1@reader2.panix.com>`

```
Interesting (and a little surprising) to me - but that's why "try it and see" is 
always better than guessing.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-01T23:06:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3q8pp$5qc$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p4ps$biq$1@reader2.panix.com> <K618i.65182$3h2.55933@fe08.news.easynews.com>`

```
In article <K618i.65182$3h2.55933@fe08.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Interesting (and a little surprising) to me - but that's why "try it and
>see" is 
>always better than guessing.

I'd say that depends on who is generating the criteria for 'better', Mr 
Klein... why, just the other day I was talking with my technical lead 
about a situation; every other sentence he spoke began with 'It might be' 
or 'Maybe it's that' or 'They might have wanted'... and every time I 
encountered one my response was 'I don't know this but I can find out by 
(action)'.

He, it seems, would rather have positied possibilities while I wanted to 
actually *do* something to learn what would result... and maybe that's why 
he does what he does and I do what I do, who knows.

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-02T05:19:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180786744.190045.21040@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<f3q8pp$5qc$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <ufN7i.196678$865.96862@fe05.news.easynews.com> <f3p4ps$biq$1@reader2.panix.com> <K618i.65182$3h2.55933@fe08.news.easynews.com> <f3q8pp$5qc$1@reader2.panix.com>`

```
On 2 Jun, 00:06, docdw...@panix.com () wrote:
> In article <K618i.65182$3h2.55...@fe08.news.easynews.com>,
> William M. Klein <wmkl...@nospam.netcom.com> wrote:
…[16 more quoted lines elided]…
> DD

Or maybe he was fishing for information or hoping that someone else
(your good self perhaps?) would provide a definitive solution/
decision?

Even tech leads don't automatically know which solution is the best
and he may have just been feeling his way trying to determine what you
thought was the best solution.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-02T21:30:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3sni5$m2b$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <K618i.65182$3h2.55933@fe08.news.easynews.com> <f3q8pp$5qc$1@reader2.panix.com> <1180786744.190045.21040@o5g2000hsb.googlegroups.com>`

```
In article <1180786744.190045.21040@o5g2000hsb.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 2 Jun, 00:06, docdw...@panix.com () wrote:
>> In article <K618i.65182$3h2.55...@fe08.news.easynews.com>,
…[18 more quoted lines elided]…
>decision?

Not... really.  In this one, particular, unique, discrete and atomic 
circumstance I believe he was trying to employ a variation of the classic 
'I Will Do More Work Avoiding The Work Than Doing The Actual Work Would 
Require Me To Do'... even though *I* was the one who would be Doing All 
The Work.

Does it make sense?  Not to me... but I long ago observed that these 
human-being type people do not always behave in a manner which I would 
describe as 'rational'.

>
>Even tech leads don't automatically know which solution is the best
>and he may have just been feeling his way trying to determine what you
>thought was the best solution.

That has happened to me, at times... sometimes as part of a 'genuine team 
effort', when I will do my best to make sure that things go as easily for 
everyone as possible as long as tasks are distributed equitably, and 
sometimes as a kind of 'let's see if I can get you to do my job for me', 
at which times I will respond with crafty manuevers from the Martial Arts 
of the Mystic East... especially the motions described as 'Repulsing the 
Hideous Brain-Leech'.

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 9)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-02T15:15:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180822534.859314.44520@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<f3sni5$m2b$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <K618i.65182$3h2.55933@fe08.news.easynews.com> <f3q8pp$5qc$1@reader2.panix.com> <1180786744.190045.21040@o5g2000hsb.googlegroups.com> <f3sni5$m2b$1@reader2.panix.com>`

```
On 2 Jun, 22:30, docdw...@panix.com () wrote:
> In article <1180786744.190045.21...@o5g2000hsb.googlegroups.com>,
>
…[53 more quoted lines elided]…
> - Show quoted text -

I don't recall the 'Repulsing the Hideous Brain-Leech' being part of
either Sun Tzu's 'The Art of War' nor Miyamoto Musahis's 'The Five
Rings'.

Two typos corrected in one sentence. Well, 3 in 2 sentences now. Make
that four in three.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-03T01:58:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3t77e$i5q$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <1180786744.190045.21040@o5g2000hsb.googlegroups.com> <f3sni5$m2b$1@reader2.panix.com> <1180822534.859314.44520@g4g2000hsf.googlegroups.com>`

```
In article <1180822534.859314.44520@g4g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 2 Jun, 22:30, docdw...@panix.com () wrote:
>> In article <1180786744.190045.21...@o5g2000hsb.googlegroups.com>,

[snip]

>> >Even tech leads don't automatically know which solution is the best
>> >and he may have just been feeling his way trying to determine what you
…[12 more quoted lines elided]…
>Rings'.

At this point, old man, you might have trouble recalling which is the 
commode and which is the washing-machine.

DD
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-03T08:01:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180882887.316684.299770@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f3t77e$i5q$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <1180786744.190045.21040@o5g2000hsb.googlegroups.com> <f3sni5$m2b$1@reader2.panix.com> <1180822534.859314.44520@g4g2000hsf.googlegroups.com> <f3t77e$i5q$1@reader2.panix.com>`

```
On 3 Jun, 02:58, docdw...@panix.com () wrote:
> In article <1180822534.859314.44...@g4g2000hsf.googlegroups.com>,
>
…[25 more quoted lines elided]…
> DD

And I spotted the typo I left in place. That was Miyamoto Musashi that
was.

I find it amazing that the light always comes on automatically when I
enter the bathroom in an inebriated state.
```

###### ↳ ↳ ↳ Re: Hex Value Moves

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-03T21:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3vb70$3fp$1@reader2.panix.com>`
- **References:** `<f3mk4b$ms0$1@reader2.panix.com> <1180822534.859314.44520@g4g2000hsf.googlegroups.com> <f3t77e$i5q$1@reader2.panix.com> <1180882887.316684.299770@k79g2000hse.googlegroups.com>`

```
In article <1180882887.316684.299770@k79g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 3 Jun, 02:58, docdw...@panix.com () wrote:

[snip]

>> At this point, old man, you might have trouble recalling which is the
>> commode and which is the washing-machine.
…[5 more quoted lines elided]…
>enter the bathroom in an inebriated state.

Similar to the commode/washing-machine confusion... when the light comes 
on automatically it's less often the bathroom and more often the 
refrigerator.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
