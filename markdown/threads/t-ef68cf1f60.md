[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dinosaur Code!

_70 messages · 29 participants · 2000-02_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```

Some folks just talk about the Oldene Dayse, when (person) could do
(activity) such at ten people cannot do today... other folks work in
places where, as Faulkner said, the past is not only not-dead... it ain't
even laid down yet.

Behold some Production Code... this is something which runs Every Day:

--begin quoted code:

ID DIVISION.                                          
PROGRAM-ID. FRIIID27.                                 
REMARKS. CONVERTED 10-73 TO ANS COBOL BY R HOWELL.    
DATE-WRITTEN. SEPT. 1, 1971.                          
ENVIRONMENT DIVISION.                                 
CONFIGURATION SECTION.                                
SOURCE-COMPUTER. IBM-370.                             
OBJECT-COMPUTER. IBM-370.                             
INPUT-OUTPUT SECTION.                                 
FILE-CONTROL.                                         
    SELECT ID240I1 ASSIGN TO                          
    DA-2314-S-IN24 RESERVE NO ALTERNATE AREAS.        
    SELECT UNMATCH ASSIGN TO                          
    UT-2400-S-INMTCH RESERVE NO ALTERNATE AREAS.      
    SELECT ID270I2 ASSIGN TO                          
    DA-2314-S-OUT27 RESERVE NO ALTERNATE AREAS.       
    SELECT ID270I1 ASSIGN TO                          
    UT-2400-S-IN27 RESERVE NO ALTERNATE AREAS.        

--end quoted code

Just *sings*, don't it?... granted, in something like Ars Antiqua
chant-style, but it *sings*... differentiating between DA-2314 and
UT-2400!  RESERVE NO ALTERNATE AREAS!  Maybe if I look in the corner over
there I'll find a dusty ol' routine for Daddy Bones or Hank 'n Arch!

(note for young'uns - 'Daddy Bones' and 'Hank 'n Arch' were
stock-characters in Minstrel Shows, a form of entertainment in the Oldene
Dayse, when an actor could tread the boards wearing blackface such as
*ten* actors could not wear today)

DD
```

#### ↳ Re: Dinosaur Code!

- **From:** wramey@home.removethis.com (Wade Ramey)
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<wramey-1102001319160001@c380773-a.pinol1.sfba.home.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
docdwarf@clark.net () wrote:

> (note for young'uns - 'Daddy Bones' and 'Hank 'n Arch' were
> stock-characters in Minstrel Shows, a form of entertainment in the Oldene
> Dayse, when an actor could tread the boards wearing blackface such as
> *ten* actors could not wear today)

That clears it up.

Wade
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<4r3p4.4690$lK6.104460@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wramey-1102001319160001@c380773-a.pinol1.sfba.home.com>`

```
In article <wramey-1102001319160001@c380773-a.pinol1.sfba.home.com>,
Wade Ramey <wramey@home.removethis.com> wrote:
>In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
>docdwarf@clark.net () wrote:
…[6 more quoted lines elided]…
>That clears it up.

Better than, say, Accutane?

(there, you see?  I can make references to things known to them
young'uns!)

DD
```

#### ↳ Re: Dinosaur Code!

- **From:** "D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<8s0p4.233$j23.6181@news.uswest.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
<docdwarf@clark.net> wrote in message
news:2g_o4.4570$lK6.100048@iad-read.news.verio.net...
>
> Some folks just talk about the Oldene Dayse, when (person) could do
> (activity) such at ten people cannot do today... other folks work in
> places where, as Faulkner said, the past is not only not-dead... it ain't
> even laid down yet.

Very stunning example of fossilized remains, I dare say.  Twenty-six years
and counting since the last revision.


> Behold some Production Code... this is something which runs Every Day:
>
…[26 more quoted lines elided]…
> there I'll find a dusty ol' routine for Daddy Bones or Hank 'n Arch!

The mind boggles.  (Reserve no alternate comments)

Ciao,
```

#### ↳ Re: Dinosaur Code!

- **From:** bks@netcom.com (Bradley K. Sherman)
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<88248r$r1a$1@nntp3.atl.mindspring.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
 <docdwarf@clark.net> wrote:
>
>REMARKS. CONVERTED 10-73 TO ANS COBOL BY R HOWELL.    

But who was the original author?

    --bks
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Lt3p4.4693$lK6.103789@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <88248r$r1a$1@nntp3.atl.mindspring.net>`

```
In article <88248r$r1a$1@nntp3.atl.mindspring.net>,
Bradley K. Sherman <bks@netcom.com> wrote:
>In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
> <docdwarf@clark.net> wrote:
…[3 more quoted lines elided]…
>But who was the original author?

Perhaps his father, who then set sail one day, with four other passengers,
for a three-hour tour?

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** "D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Cyop4.1560$TK3.13131@news.uswest.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <88248r$r1a$1@nntp3.atl.mindspring.net> <Lt3p4.4693$lK6.103789@iad-read.news.verio.net>`

```

<docdwarf@clark.net> wrote in message
news:Lt3p4.4693$lK6.103789@iad-read.news.verio.net...
> In article <88248r$r1a$1@nntp3.atl.mindspring.net>,
> Bradley K. Sherman <bks@netcom.com> wrote:
…[8 more quoted lines elided]…
> for a three-hour tour?

That rang clear as a bell.

Incidentally, I think that I've heard of that Anastasio Shievenjinheimer
character.
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** alizard[spam]@ecis.com (A.Lizard)
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a4f63b.31276674@news.ecis.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <88248r$r1a$1@nntp3.atl.mindspring.net>`

```
On 11 Feb 2000 22:59:39 GMT, bks@netcom.com (Bradley K. Sherman)
wrote:

>In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
> <docdwarf@clark.net> wrote:
…[3 more quoted lines elided]…
>But who was the original author?

Somebody named Ada Lovelace, a girl geek back from those days of
olde. I think it was a port from something called an "Analytical
Engine" from one of the early high-tech firms that tanked shortly
after initial funding. 
A.Lizard

>    --bks
>

************************************************************************
"Here's the most exasperating part: Ninety-five percent of the Y2k hoax
hysteria is planted by people who stand to gain, head-lined by
propagation-hungry publishers, and purveyed as truth by perpetuators of
rumour." Dave Eastabrook
"Anybody who still believes in the media must have been in a coma for 
the past 30 years." - Robert Anton Wilson
Personal Web site http://www.ecis.com/~alizard
Y2Kinfo: http://www.ecis.com/~alizard/y2k.html
Littleton page:http://www.ecis.com/~alizard/littleto.html
backup address (if ALL else fails) alizard@[spam]onebox.com
PGP 6.5.1 key available by request,keyserver,or on my Web site
PGPfone v1.02 and v2.1 available for secure voice conferencing, get
your own (W9x,NT,Mac) at http://www.pgpi.org/products/nai/pgpfone/
************************************************************************
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** nan_forrant@bigfoot.com
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<88em5k$hh1$1@nnrp1.deja.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <88248r$r1a$1@nntp3.atl.mindspring.net>`

```
In article <88248r$r1a$1@nntp3.atl.mindspring.net>,
  bks@netcom.com (Bradley K. Sherman) wrote:
> In article <2g_o4.4570$lK6.100048@iad-read.news.verio.net>,
>  <docdwarf@clark.net> wrote:
…[7 more quoted lines elided]…
>

LOLLLLLLL I have seen "coverted notations(or even original Author names
such as Karl Marx or Fred Flintstone (this one was a little easier to
figure out the person still works here and his last name is FLINT haha)


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38ABA7F1.DE26553A@worldnet.att.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <88248r$r1a$1@nntp3.atl.mindspring.net> <88em5k$hh1$1@nnrp1.deja.com>`

```
nan_forrant@bigfoot.com wrote:
> 
> In article <88248r$r1a$1@nntp3.atl.mindspring.net>,
…[14 more quoted lines elided]…
> figure out the person still works here and his last name is FLINT haha)

We have programs in which the author is "Abe End.)

Bill L
```

#### ↳ Re: Dinosaur Code!

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<wO0p4.573$tT6.11143@news.swbell.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
Are you complaining about the code or bragging about the code?

Me, I would be bragging. Running everyday for twenty-seven years since
the last revision. How much better could it get?


<docdwarf@clark.net> wrote in message
news:2g_o4.4570$lK6.100048@iad-read.news.verio.net...
>
> Some folks just talk about the Oldene Dayse, when (person) could do
> (activity) such at ten people cannot do today... other folks work in
> places where, as Faulkner said, the past is not only not-dead... it
ain't
> even laid down yet.
>
> Behold some Production Code... this is something which runs Every
Day:
>
> --begin quoted code:
…[24 more quoted lines elided]…
> UT-2400!  RESERVE NO ALTERNATE AREAS!  Maybe if I look in the corner
over
> there I'll find a dusty ol' routine for Daddy Bones or Hank 'n Arch!
>
> (note for young'uns - 'Daddy Bones' and 'Hank 'n Arch' were
> stock-characters in Minstrel Shows, a form of entertainment in the
Oldene
> Dayse, when an actor could tread the boards wearing blackface such
as
> *ten* actors could not wear today)
>
> DD
>
>
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<882nt1$53c2$1@newssvr04-int.news.prodigy.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net>`

```

Jerry P <bismail@bisusa.com> wrote in message
news:wO0p4.573$tT6.11143@news.swbell.net...
> Are you complaining about the code or bragging about the code?
>
> Me, I would be bragging. Running everyday for twenty-seven years since
> the last revision. How much better could it get?

I agree with your assessment, Jerry.  I started programming in 1974.  In
1971, there were legitimate reasons for the RESERVE NO ALTERNATE AREAS
clause (indicating use only 1 I/O buffer for this file since the default was
2) due to disk space cost and sometimes shop restrictions of load module
size.  Back then, it was oftentimes necessary to use unblocked files for the
same reason instead of having the luxury of half-track blocked files whick
are common today.  I also think that the references to the 2314 disk device
and the 2400 tape device were required back then.  I'd hate to hazard a
guess as to the probability of programs written today still running in
production in the year 2029.  Think about it.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A51325.7B8C6DF4@worldnet.att.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net> <882nt1$53c2$1@newssvr04-int.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> Jerry P <bismail@bisusa.com> wrote in message
…[15 more quoted lines elided]…
> production in the year 2029.  Think about it.

Based on several factors, this was likely late Jurassic COBOL. Do you
have the radiocarbon tests back yet?

This was originally a DOS (that's dee oh ess, BTW) COBOL program,
probably D-COBOL, although I think the F-level compiler was available by
then. OS/360 always (IIRC, I didn't work with it until 1975) supported
device independence for sequential files, so OS COBOL programs did not
specify 2314 or 2401 and buffering was more complex than 1 or 2 I/O
buffers (can't tell you how long it's been since I wrote "I/O buffers").
OS systems typically had substantially more core (that's what it was
called), too. 

Bill Lynch
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38bba87c.6250049@news1.frb.gov>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net> <882nt1$53c2$1@newssvr04-int.news.prodigy.com>`

```
On Fri, 11 Feb 2000 22:34:12 -0600, Terry Heinze wrote:

>I agree with your assessment, Jerry.  I started programming in 1974.  In
>1971, there were legitimate reasons for the RESERVE NO ALTERNATE AREAS
>clause (indicating use only 1 I/O buffer for this file since the default was
>2) due to disk space cost and sometimes shop restrictions of load module
>size.  
[snip]

Another use I have seen for the RESERVE NO ALTERNATE AREAS clause was
with a card reader input file (not spooled).  If there was no
buffering, then a program could read a card, evaluate it, and decide
if it liked it.  If not, it could then pause and display a console
message asking someone to correct the card and then pass it back
through the card reader.  Obviously, the card reader was tied-up
during the process.

Such schemes would be big time wasters today, even if cards were still
the usual input medium.  In fact, they were generally not very
efficient in the "old days" either, but I have seen it done.  I guess
that some folks did not place much value on people's time or on
sharing resources/devices among users.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89i4i2$61fi$1@newssvr03-int.news.prodigy.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net> <882nt1$53c2$1@newssvr04-int.news.prodigy.com> <38bba87c.6250049@news1.frb.gov>`

```

WDS <WDS@WDS.WDS.5> wrote in message news:38bba87c.6250049@news1.frb.gov...
> Another use I have seen for the RESERVE NO ALTERNATE AREAS clause was
> with a card reader input file (not spooled).  If there was no
…[15 more quoted lines elided]…
> -------------------Decoy@Spammer.Trasher----------------

It's been a long time, but I believe in the 70s, RESERVE NO ALTERNATE AREAS
was required for print files.  It had something to do with the possible
overlapping of print lines as I recall.
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Ou3p4.4694$lK6.104488@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net>`

```
In article <wO0p4.573$tT6.11143@news.swbell.net>,
Jerry P <bismail@bisusa.com> wrote:
>Are you complaining about the code or bragging about the code?
>
>Me, I would be bragging. Running everyday for twenty-seven years since
>the last revision. How much better could it get?

Last *commented* revision... but it is neither bragging nor complaining,
merely marvelling.

DD
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<cn8eas8ud8hp1b4dms903eqmmn6301jtcc@4ax.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <wO0p4.573$tT6.11143@news.swbell.net>`

```
On Fri, 11 Feb 2000 17:20:10 -0600 "Jerry P" <bismail@bisusa.com> wrote:

:>Are you complaining about the code or bragging about the code?

:>Me, I would be bragging. Running everyday for twenty-seven years since
:>the last revision. How much better could it get?

Grasshopper,

Might you be making the critical mistake of assuming that the remarks have any
connection at all to the program?

   [ snipped ]
```

#### ↳ Re: Dinosaur Code!

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A50D8D.201A@NOSPAMguysoftware.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
> Behold some Production Code... this is something which runs Every Day:
…[7 more quoted lines elided]…
> there I'll find a dusty ol' routine for Daddy Bones or Hank 'n Arch!

Yeah, back then we ran a whole damn company (a major utility) on a Honeywell 200 with 
24K (that's 24,000 BYTES) of RAM (known as "core" then) with four tape drives, one 
reader-punch, one line printer, no disk, no console typewriter. (Had to "boot" it the 
hard way by keying in machine code with the buttons on the box).
I had a routine that printed 20 rows of * on the line printer to wake up the operator 
and lure him/her out of the little office to look at the message giving instructions for 
tape mounts or whatever.
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<psdp4.4836$a27.145266@news1.rdc1.mb.home.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com>`

```

"Ed Guy" <ed_guy@NOSPAMguysoftware.com> wrote in message >
> Yeah, back then we ran a whole damn company (a major utility) on a
Honeywell 200 with
> 24K (that's 24,000 BYTES) of RAM (known as "core" then) with four tape
drives, one
> reader-punch, one line printer, no disk, no console typewriter. (Had to
"boot" it the
> hard way by keying in machine code with the buttons on the box

Yea, fond memories.  COBOL-B ran in 8K, no PERFORM verb, only first 3
characters of datanames were significant.  That was when ALTER statement was
valuable.

Charlie Goodman
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<yEep4.4857$lK6.111572@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <psdp4.4836$a27.145266@news1.rdc1.mb.home.com>`

```
In article <psdp4.4836$a27.145266@news1.rdc1.mb.home.com>,
Charles Goodman <cgoodman@mbnet.mb.ca> wrote:
>
>"Ed Guy" <ed_guy@NOSPAMguysoftware.com> wrote in message >
…[7 more quoted lines elided]…
>valuable.

'Fond memories' of times when ALTER was 'valuable'?  As Aeschylus said,
'Great hardships make for later entertainments'.

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** "Bernard Nemeth" <bnemeth@shaw.wave.ca>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<xItp4.54825$up4.913456@news1.rdc1.ab.home.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <psdp4.4836$a27.145266@news1.rdc1.mb.home.com>`

```
I remember it well.  The Honeywell H200 came with 4K core memory in the low
end entry level model.  Anything beyond that was optional. The only software
that could run in the entry  configuration was the Easycoder-A assembler.
To create an executable program, you ran the source code card deck through
the card reader twice along with the assembler card deck, and if all went
well the card punch would spit out your self-booting executable program and
a listing would appear on the printer.  The basic peripherals were the card
reader,and punch, a line printer.  Seven tracks magnetic tapes appeared on
the higher end models.  Random access devices (drums and disks) evolved
later.

Software development packages those days were classed as A, B, D, F, or H
depending on whether the target machine was 4K, 8K, 16K, 24K or 32K.  Thus
the COBOL compiler for the 8K machines was labelled as COBOL-B.

Bernie Nemeth

"Charles Goodman" <cgoodman@mbnet.mb.ca> wrote in message
news:psdp4.4836$a27.145266@news1.rdc1.mb.home.com...
>
> "Ed Guy" <ed_guy@NOSPAMguysoftware.com> wrote in message >
…[9 more quoted lines elided]…
> characters of datanames were significant.  That was when ALTER statement
was
> valuable.
>
> Charlie Goodman
>
>
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000215002617.01108.00001016@ng-bk1.aol.com>`
- **References:** `<psdp4.4836$a27.145266@news1.rdc1.mb.home.com>`

```
> That was when ALTER statement was
>valuable.
>

Other than trying to sharpen your flint knife, what has ALTER ever been
"valuable " to do??  I ask because my first assignment was maintenance on a
hopsital claim program that contain no less than 15 ALTER...GO TO statements. 
I hated it then (spent three months rewriting the sucker, finally!!) and
despise it now.

"And if you try to tell that to the young people today, they don't believe
you!"
  Monty Python - Live at the Hollywood Bowl.


Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fWpq4.7003$a27.178606@news1.rdc1.mb.home.com>`
- **References:** `<psdp4.4836$a27.145266@news1.rdc1.mb.home.com> <20000215002617.01108.00001016@ng-bk1.aol.com>`

```
The object code for a GO TO is very small and very quick.  Remember the
PERFORM statement did not exist.  In place of a perform statement you would
ALTER a GO TO at the end of a bunch of code you wanted to 'perform'.  The
alternative was to set a flag and use an IF with GO TO at the end of the
'performed' code.  The comparison generated large code and was slow.
Remember 8K and 1 microsecond cycle time.  I can remember modifying code to
use ALTERs so that it would execute more quickly and fit into memory.

Charlie Goodman


"Steve Newton" <stevenln@aol.comnospam> wrote in message
news:20000215002617.01108.00001016@ng-bk1.aol.com...
> > That was when ALTER statement was
> >valuable.
…[3 more quoted lines elided]…
> "valuable " to do??
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kbDq4.7535$QK6.85960@news4.mia>`
- **References:** `<psdp4.4836$a27.145266@news1.rdc1.mb.home.com> <20000215002617.01108.00001016@ng-bk1.aol.com> <fWpq4.7003$a27.178606@news1.rdc1.mb.home.com>`

```
Charles Goodman wrote:
>Remember 8K and 1 microsecond cycle time.

Perhaps you mean 8k and 1 millisecond.  That's where I started.  But
the programs actually had to run in 4k.  We only had 8k because we
were a development center, and the compiler wouldn't run in 4k. :-)
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a6e8c0.364507854@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com>`

```
Hey Ed,

Ed Guy <ed_guy@NOSPAMguysoftware.com> wrote:

>Yeah, back then we ran a whole damn company (a major utility) on a Honeywell 200 with 
>24K (that's 24,000 BYTES) of RAM (known as "core" then) with four tape drives, one 
…[4 more quoted lines elided]…
>tape mounts or whatever.

You're the only other CDP I've seen around these parts.

-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A61E0B.559A@NOSPAMguysoftware.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com>`

```
Dean T. Miller wrote:
> 
> Hey Ed,
…[3 more quoted lines elided]…
> -- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)

Yeah, I guess it dates me.  I took it when the DPMA were still administering it.

Took it because like most of my generation there was no specific computer degree when I 
was a student.  To me it was an "electrical machine" so I took an EE degree.  My sister 
took a math degree and others took accounting degrees and we all ended up as computer 
professionals.  I wouldn't have bothered, but I took a job where the need arose to give 
expert testimony and I needed a specifically Data Processing designation.

I was surprised a few years ago when I was at an Institute of Internal Auditors course 
in San Francisco they still recognise it along with their  CIA designation (Certified 
Internal Auditor - a friend has a lot of fun with his business card saying Jerry M---, 
CIA) and the CISA (Certified Information Systems Auditor).
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** jbernier@microtec.net (Jacques Bernier)
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a60c70.40829285@news.microtec.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <38A61E0B.559A@NOSPAMguysoftware.com>`

```
Your message has been picked up by Echelon.

JB

On Sat, 12 Feb 2000 18:59:23 -0800, Ed Guy
<ed_guy@NOSPAMguysoftware.com> wrote:

snip

>CIA
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<BWyp4.5347$lK6.121298@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38a6e8c0.364507854@news1.newscene.com> <38A61E0B.559A@NOSPAMguysoftware.com> <38a60c70.40829285@news.microtec.net>`

```
In article <38a60c70.40829285@news.microtec.net>,
Jacques Bernier <jbernier@microtec.net> wrote:
>Your message has been picked up by Echelon.

... just like every one about the Culinary Institute of America?

DD

>On Sat, 12 Feb 2000 18:59:23 -0800, Ed Guy
><ed_guy@NOSPAMguysoftware.com> wrote:
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** "rdr" <not@thistime.com>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<9zIp4.71$5i7.18405@news.aloha.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38a6e8c0.364507854@news1.newscene.com> <38A61E0B.559A@NOSPAMguysoftware.com> <38a60c70.40829285@news.microtec.net> <BWyp4.5347$lK6.121298@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message ...
>In article <38a60c70.40829285@news.microtec.net>,
>Jacques Bernier <jbernier@microtec.net> wrote:
…[3 more quoted lines elided]…
>


Ahh.... memories of a childhood home, Frisbee golf on the banks of the
Hudson.

Love this thread. The H-200 reminds me of the tech changes in one of my
*careers*. Where I used to spend hours tweaking knobs (pots), now I
spend hours navigating menus. Endlessly pushing a few buttons.  I don't
know that anything is necessarily easier or faster, but there ceratanly
are lots more features. As I muse I wonder that anyone considering the
*benefits* of New Tech needs to keep in mind the learning curve involved
with keeping abreast.

\iii/
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<LrJp4.5558$lK6.128484@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38a60c70.40829285@news.microtec.net> <BWyp4.5347$lK6.121298@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net>`

```
In article <9zIp4.71$5i7.18405@news.aloha.net>, rdr <not@thistime.com> wrote:
>
>docdwarf@clark.net wrote in message ...
…[9 more quoted lines elided]…
>Hudson.

I learned about said Institute when I spent some time in an Academic Grove
a few miles north thereof; some have referred to it as My Old School.

>
>Love this thread. The H-200 reminds me of the tech changes in one of my
>*careers*. Where I used to spend hours tweaking knobs (pots), now I
>spend hours navigating menus.

Only times I ever needed to twist a pot was to get my voice into the
red... it seems like several lifetimes ago, aye.

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 8)_

- **From:** "rdr" <not@thistime.com>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<1h%p4.92$5i7.20818@news.aloha.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38a60c70.40829285@news.microtec.net> <BWyp4.5347$lK6.121298@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net> <LrJp4.5558$lK6.128484@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message ...
>In article <9zIp4.71$5i7.18405@news.aloha.net>, rdr <not@thistime.com>
wrote:
>>
>>docdwarf@clark.net wrote in message ...
>>>In article <38a60c70.40829285@news.microtec.net>,
>>>Jacques Bernier <jbernier@microtec.net> wrote:
>>>>Your message has been picked up by Echelon.


>>>... just like every one about the Culinary Institute of America?


>>Ahh.... memories of a childhood home, Frisbee golf on the banks of the
>>Hudson.

>I learned about said Institute when I spent some time in an Academic
Grove
>a few miles north thereof; some have referred to it as My Old School.

North? Funny, I always considered you more of a Vasser type ;)

>>Love this thread. The H-200 reminds me of the tech changes in one of
my
>>*careers*. Where I used to spend hours tweaking knobs (pots), now I
>>spend hours navigating menus.

>Only times I ever needed to twist a pot was to get my voice into the
>red...

Now why in the heck would you want to do that?

\iii/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"Common sense is not so common." -unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 9)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<6F1q4.5962$lK6.141105@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net> <LrJp4.5558$lK6.128484@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net>`

```
In article <1h%p4.92$5i7.20818@news.aloha.net>, rdr <not@thistime.com> wrote:
>
>docdwarf@clark.net wrote in message ...
…[18 more quoted lines elided]…
>North? Funny, I always considered you more of a Vasser type ;)

I've been considered many types, most of which I ain't... but the
school-errors keep happening over Andover Andover again.

>
>>>Love this thread. The H-200 reminds me of the tech changes in one of my
…[6 more quoted lines elided]…
>Now why in the heck would you want to do that?

Just on certain peaks... made sure I was pushing enough amplitude.

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 10)_

- **From:** "rdr" <not@thistime.com>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<0Z9q4.100$5i7.21783@news.aloha.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net> <LrJp4.5558$lK6.128484@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote
>rdr <not@thistime.com> wrote:
>>docdwarf@clark.net wrote in message ...
>>>rdr <not@thistime.com wrote:
>>>>docdwarf@clark.net wrote in message ...
>>>>>Jacques Bernier wrote:


>>>>>... just like every one about the Culinary Institute of America?


>>>>Ahh.... memories of a childhood home, Frisbee golf on the banks of
the
>>>>Hudson.

>>>I learned about said Institute when I spent some time in an Academic
Grove
>>>a few miles north thereof; some have referred to it as My Old School.

>>North? Funny, I always considered you more of a Vasser type ;)

>I've been considered many types, most of which I ain't... but the
>school-errors keep happening over Andover Andover again.

I can't quite put my finger on it. AU perhaps?

>>>>Love this thread. The H-200 reminds me of the tech changes in one of
my
>>>>*careers*. Where I used to spend hours tweaking knobs (pots), now I
>>>>spend hours navigating menus.

>>>Only times I ever needed to twist a pot was to get my voice into the
>>>red...

>>Now why in the heck would you want to do that?

>Just on certain peaks... made sure I was pushing enough amplitude.


A crooner from the olden dayse? Whodathunkit?

\iii/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"The secret of success is sincerity, once you can fake that you've got
it made." Jean Graudouix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 11)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Dlaq4.6088$lK6.144896@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net>`

```
In article <0Z9q4.100$5i7.21783@news.aloha.net>, rdr <not@thistime.com> wrote:
>
>docdwarf@clark.net wrote
…[21 more quoted lines elided]…
>I can't quite put my finger on it. AU perhaps?

No, no... American University's in Washington, DC.

>
>>>>>Love this thread. The H-200 reminds me of the tech changes in one of my
…[11 more quoted lines elided]…
>A crooner from the olden dayse? Whodathunkit?

Crooner?  Not I, jes' 'nother DJ... '... and now, the Magic Bowl Movement
from the Symphony in C-minus by George Amadeus Matesky.'

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 12)_

- **From:** NaKaula <hkaul@_lava.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<150220002219454998%hkaul@_lava.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net>`

```
In article <Dlaq4.6088$lK6.144896@iad-read.news.verio.net>,
<docdwarf@clark.net> wrote:

> In article <0Z9q4.100$5i7.21783@news.aloha.net>, rdr <not@thistime.com> wrote:
> >
…[42 more quoted lines elided]…
> from the Symphony in C-minus by George Amadeus Matesky.'

Unless one had to take an extended trip down the hall.  Then one aired
the Magic Bowel Movement Symphony... better known as a 'crapper'.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 12)_

- **From:** John Wiele <wiele@my-deja.com>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38AAD362.DD447A0A@my-deja.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
[snip irrelvevant, uninteresting stuff]
> Crooner?  Not I, jes' 'nother DJ... '... and now, the Magic Bowl Movement
> from the Symphony in C-minus by George Amadeus Matesky.'
> 

Presumably you refer to the inestimable Johann Amadeus Matetsky.  By the
most amazing coincidence I was just listening to the great Symphony in C
Minus yesterday when your post came across the wires.

				-JW
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 13)_

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38ada312.167697916@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net> <38AAD362.DD447A0A@my-deja.com>`

```
John Wiele <wiele@my-deja.com> wrote:

>docdwarf@clark.net wrote:
>> 
…[7 more quoted lines elided]…
>Minus yesterday when your post came across the wires.

That's Symphony in C--.

-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 14)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38AC03E7.BC5EC594@cusys.edu>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net> <38AAD362.DD447A0A@my-deja.com> <38ada312.167697916@news1.newscene.com>`

```
"Dean T. Miller" wrote:

> >Presumably you refer to the inestimable Johann Amadeus Matetsky.  By the
> >most amazing coincidence I was just listening to the great Symphony in C
> >Minus yesterday when your post came across the wires.
>
> That's Symphony in C--.

I get the major and minor keys mixed up.  Is C-- the same as D+ ?  Gotta find
out whether it passes or not.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 15)_

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38ac44fc.209148369@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net> <38AAD362.DD447A0A@my-deja.com> <38ada312.167697916@news1.newscene.com> <38AC03E7.BC5EC594@cusys.edu>`

```
Hi Howard,

Howard Brazee <howard.brazee@cusys.edu> wrote:

>"Dean T. Miller" wrote:
>
…[7 more quoted lines elided]…
>out whether it passes or not.

That was supposed to show up as "C- -", but doesn't show up right with
some proportional fonts.

-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 13)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38ABA846.E62ADD74@worldnet.att.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <1h%p4.92$5i7.20818@news.aloha.net> <6F1q4.5962$lK6.141105@iad-read.news.verio.net> <0Z9q4.100$5i7.21783@news.aloha.net> <Dlaq4.6088$lK6.144896@iad-read.news.verio.net> <38AAD362.DD447A0A@my-deja.com>`

```
John Wiele wrote:
> 
> docdwarf@clark.net wrote:
…[8 more quoted lines elided]…
> Minus yesterday when your post came across the wires.

Oh, yes, JAM, bombed in NYC, IIRC. Wasn't he a contemporary of PDQ Bach?

Bill L
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 8)_

- **From:** NaKaula <hkaul@_lava.net>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<140220002245091599%hkaul@_lava.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38a60c70.40829285@news.microtec.net> <BWyp4.5347$lK6.121298@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net> <LrJp4.5558$lK6.128484@iad-read.news.verio.net>`

```
In article <LrJp4.5558$lK6.128484@iad-read.news.verio.net>,
<docdwarf@clark.net> wrote:

> In article <9zIp4.71$5i7.18405@news.aloha.net>, rdr <not@thistime.com> wrote:
> >
…[21 more quoted lines elided]…
> red... it seems like several lifetimes ago, aye.

"into the red"... as in,

deja..... VU ?

(And technically, they were not 'pots'.  They were 'ladder
attenuators'.)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 9)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Rcaq4.6086$lK6.144891@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <9zIp4.71$5i7.18405@news.aloha.net> <LrJp4.5558$lK6.128484@iad-read.news.verio.net> <140220002245091599%hkaul@_lava.net>`

```
In article <140220002245091599%hkaul@_lava.net>,
NaKaula  <hkaul@_lava.net> wrote:
>In article <LrJp4.5558$lK6.128484@iad-read.news.verio.net>,
><docdwarf@clark.net> wrote:

[snippimente]

>> Only times I ever needed to twist a pot was to get my voice into the
>> red... it seems like several lifetimes ago, aye.
…[3 more quoted lines elided]…
>deja..... VU ?

Some folks relied on arranged introductions but I found those devices to
be the best way to...

... meet 'er.

>
>(And technically, they were not 'pots'.  They were 'ladder
>attenuators'.)

They was called what they was called... isn't, 'technically', a kangaroo
mouse neither?

DD
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** "Daniel P. B. Smith" <dpbsmith@bellatlantic.net>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<dpbsmith-E29D49.16115013022000@news5.bellatlantic.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com>`

```
In article <38a6e8c0.364507854@news1.newscene.com>, 
dtmiller@midiowa.net wrote:

> Hey Ed,
> 
…[17 more quoted lines elided]…
> -- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)

I have a CDP but I've stopped mentioning it since nobody (certainly no 
hiring managers) seem to have any idea what it is.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** david <dskirk@usa.net>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f9eascdqh0ebm17c5jbnp35jdf2uj9q2q@4ax.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net>`

```
 >.... <big snip>....
>> 
…[5 more quoted lines elided]…
>hiring managers) seem to have any idea what it is.

two thoughts:
1. i well remember the honeywell... and philco and GE and Univac and
Burroughs and RCA...   a golden era of computing when no one
considered it relevant that we use the same hardware instruction set
or the same operating software... was an exciting time... i began
programming in january, 1965, and the world is far different today...

2. on the CDP, it was a good idea in early 1970's, but lost favor as
companies began to drift from the mainframe. certification is still
important, but many are now looking to the client/server
certifications...  of course, the CDP indicated an awareness and skill
in busines priorities and processes; the client/server certification
is focused solely on knowledge of the technology. we have indeed lost
something in the process.  
david 


__________________________________________________
david                               dskirk@usa.net
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A72DD7.61426E58@worldnet.att.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <5f9eascdqh0ebm17c5jbnp35jdf2uj9q2q@4ax.com>`

```
david wrote:
> 
>  >.... <big snip>....
…[7 more quoted lines elided]…
> something in the process.

I got a CDP in 1969 (issued by the DMA) and absolutely no one ever asked
about it or cared a fig that I had one.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** MCH <milesh1@ix.netcom.com>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A72970.BB33986@ix.netcom.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net>`

```
> I have a CDP but I've stopped mentioning it since nobody (certainly no
> hiring managers) seem to have any idea what it is.
> 
> --
> Daniel P. B. Smith

Well, what is it?  "Certified Dilbert Programmer"?
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** walterm@rose.hp.com (Walter Murray)
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<88a0qj$p12$1@web1.cup.hp.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38A72970.BB33986@ix.netcom.com>`

```
MCH (milesh1@ix.netcom.com) wrote:
: > I have a CDP but I've stopped mentioning it since nobody (certainly no
: > hiring managers) seem to have any idea what it is.
: > 
: > Daniel P. B. Smith

: Well, what is it?  "Certified Dilbert Programmer"?

Here's my recollection of things.  It may not be completely correct,
but should be pretty close.

Back in the '60s and '70s there was talk of regulating computer
professionals.  It was being suggested in several state legislatures.
Pressure mounted in the wake of the realization that computers could
actually be used to embezzle.  Anybody remember the Equity Funding
scandal?

Several professional organizations, including the Data Processing
Management Assiciation (DPMA) and the Association for Computing
Machinery (ACM) realized it would be better if they took the
lead to develop credentials that would be recognized universally,
rather than have each state develop their own standards.

I think DPMA took the lead with the Registered Business Programmer
(RBP) examination.  Then a consortium of about seven organizations,
originally referred to as "the Foundation" developed the Certificate
in Data Processing (CDP), patterned after the CPA credential.  
Requirements to be awarded a CDP varied over the years, but
typically included several years of related college-level courses,
several years of experience in computing, passing an exam, being
of good moral character, subscribing to a code of ethics, etc.
The exam was a full-day affair in five sections.  (You got experience
for the programming section if you had already passed the RBP exam.)
It was not trivial.  Most people did not pass all five sections on
the first try.  Meeting all the requirements and passing the exam
gave you the right to use the initials CDP after your name.

Somewhere along the line the RBP program was replaced with the
Certified Computer Programmer (CCP) credential, which came in
three flavors:  business (COBOL), scientific (FORTRAN), and systems
(assembler).  

Eventually it was decided to create a new organization to promote
certification and to develop and administer new exams.  Thus was
born the Institute for Certification of Computer Professionals (ICCP).
They discontinued the Certified Computer Programmer credential and
recycled the abbreviation CCP to mean Certified Computer Professional,
which was the successor to the CDP.  The CCP program added  a
requirement for continuing education in order to retain the right
to use the credential.  However, holders of the CDP were grandfathered
in and could apply to receive a CCP.

Walter Murray, RBP, CCP, CDP
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A8E31B.AD4013CB@worldnet.att.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38A72970.BB33986@ix.netcom.com> <88a0qj$p12$1@web1.cup.hp.com>`

```
Walter Murray wrote:
> 
(snipped)
> 
> Back in the '60s and '70s there was talk of regulating computer
…[12 more quoted lines elided]…
> (RBP) examination.

Register Communists, not programmers!

Bill Lynch
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** "D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<NQgq4.116$yR5.3544@news.uswest.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38A72970.BB33986@ix.netcom.com> <88a0qj$p12$1@web1.cup.hp.com> <38A8E31B.AD4013CB@worldnet.att.net>`

```
"Bill Lynch" <wblynch@worldnet.att.net> wrote in message
news:38A8E31B.AD4013CB@worldnet.att.net...
> Walter Murray wrote:
> >
…[17 more quoted lines elided]…
> Register Communists, not programmers!

No, no, no ... you have it all wrong.  It's better known as another profit
center for the DPMA.  Good old Capitalism at its finest.

Ciao,
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a7803b.10743298@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net>`

```
Hi Dan,

"Daniel P. B. Smith" <dpbsmith@bellatlantic.net> wrote:

>I have a CDP but I've stopped mentioning it since nobody (certainly no 
>hiring managers) seem to have any idea what it is.

They had no idea in the 60's, either.  :)

I (and Kenniston Lord and others) attempted to start the "Society of
Certified Data Processors" around 1970.  It was patterned upon the CPA
association, but never got off the ground.  There was (and continues
to be) too much demand for computer people, so certification didn't
mean much (and doesn't seem to mean very much right now).

-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<iHWp4.2625$Ez.62409@news2.mia>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com>`

```
Dean T. Miller wrote:
>
>I (and Kenniston Lord and others) attempted to start the "Society of
…[3 more quoted lines elided]…
>mean much (and doesn't seem to mean very much right now).

It doesn't mean much because raw knowledge about facts, which is what
those kinds of tests are designed to rate, is only a very small part
of what makes for a good programmer.  Smarts, attitute and experience
are, in decreasing order, each far more important in most situations.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<37dq4.750$BS.8603@news.swbell.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia>`

```

Judson McClendon <judmc@bellsouth.net
>
> It doesn't mean much because raw knowledge about facts, which is
what
> those kinds of tests are designed to rate, is only a very small part
> of what makes for a good programmer. . . .

OTOH it means a great deal if you FAIL the test.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** "Daniel P. B. Smith" <dpbsmith@bellatlantic.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<dpbsmith-635E43.20451814022000@news5.bellatlantic.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia>`

```
In article <iHWp4.2625$Ez.62409@news2.mia>, "Judson McClendon" 
<judmc@bellsouth.net> wrote:

> Dean T. Miller wrote:
> >
…[9 more quoted lines elided]…
> are, in decreasing order, each far more important in most situations.

Uh, systems analysis is much more than "raw knowledge about facts."  And 
so is the Code of Ethics.
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<Kwfq4.4796$QK6.56356@news4.mia>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia> <dpbsmith-635E43.20451814022000@news5.bellatlantic.net>`

```
Daniel P. B. Smith wrote:
>Judson McClendon wrote:
>> Dean T. Miller wrote:
…[13 more quoted lines elided]…
>so is the Code of Ethics.

Daniel,

Are we having the same conversation? ;-)  Yes, I agree that "systems
analysis" is much more than "raw knowledge and facts."  However, the
discussion was about the value (or lack) of having a CDP certification,
and those were were issued based on tests.  Those kinds of tests try
to measure raw knowledge of facts, rather than ability, because direct
tests of ability (and grading of same) are far too difficult to arrange
in a completely objective way.  So my comments were about the tests and,
by implication, the actual certifications.  My comments had nothing
whatever to do with 'systems analysis' per se (or the Code of Ethics).
Your comments imply that either you completely missed my point, or I
have completely missed yours. :-)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a9ec3d.547076@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia>`

```
Hi Judson,

"Judson McClendon" <judmc@bellsouth.net> wrote:

>Dean T. Miller wrote:
>>
…[9 more quoted lines elided]…
>are, in decreasing order, each far more important in most situations.

I see you've never taken the CDP exams.  

Eight hours of tests, half of which covered management areas -- and to
be allowed to take the test, you had to have at least a BA/BS and 3
years of experience in the computer field (at least, those were the
requirements in 1964).  The technical part of the tests covered tab
machine analysis and operation (it was '64, after all), operations
research and other applied math, plus knowledge of computers
(primarily IBM), systems design methodology and programming languages
of the day.

My biggest joy in passing the exam was having the guy sitting next to
me fail it.  He was formerly my "boss" when I was in the army, a Ph.D.
in Physics and a GS something -- a real horn-hair.

-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A9869A.7346@NOSPAMguysoftware.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia> <38a9ec3d.547076@news1.newscene.com>`

```
Dean T. Miller wrote:
> 
> Hi Judson,
…[25 more quoted lines elided]…
> of the day.

And you might have added: no "syllabus" specified in advance.  They took the position 
that they could test on ANYTHING they considered relevant.  I passed the tests in 1972, 
which was the first year they included lots of questions on telephony and 
communications.  That year the failure rate was about 80%.  I was thankful for my EE 
degree!
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<lNfq4.4823$QK6.56775@news4.mia>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia> <38a9ec3d.547076@news1.newscene.com>`

```
Dean T. Miller wrote:
>Judson McClendon wrote:
>>Dean T. Miller wrote:
…[12 more quoted lines elided]…
>I see you've never taken the CDP exams.

No. :-)

>Eight hours of tests, half of which covered management areas -- and to
>be allowed to take the test, you had to have at least a BA/BS and 3
…[9 more quoted lines elided]…
>in Physics and a GS something -- a real horn-hair.

I fail to see your point.  To pass the test you answered questions,
isn't that true?  And to correctly answer the questions you had to
have specific knowledge, right?  So, the test measured knowledge.
I did not mean to imply that the tests were easy, or worthless, or
that they had no meaning.  What I was trying to say is that raw
knowledge simply does not equate with ability and/or performance.
There is come correlation, yes.  But every one of us has known people
who were very well educated, but could hardly tie their shoes in a
practical situation, or solve a real world problem.  The fact is,
there are factors far more important than raw knowledge.  An extremely
bright and talented person with incredible initiative, will, in the
long run, *always* trounce someone with less intelligence, initiative
and talent.  There are many other important attributes, such as the
willingness to suffer hardship to get the job done, tenacity, good
judgment (common sense), integrity, etc.  But those are much more
difficult to measure objectively than raw knowledge.  And as it turns
out, those bright, intelligent and motivated people will eventually
gain the knowledge, so testing knowledge does loosely correlate to
ability.  My point is that the correlation is much looser than might
be expected, because there are a lot of people out there who have
memorized a lot of facts, but who couldn't use one if it bit them in
the nose.  Perhaps your old Army boss was such a person? :-)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 8)_

- **From:** dtmiller@midiowa.net (Dean T. Miller)
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38a9d276.48758080@news1.newscene.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com> <dpbsmith-E29D49.16115013022000@news5.bellatlantic.net> <38a7803b.10743298@news1.newscene.com> <iHWp4.2625$Ez.62409@news2.mia> <38a9ec3d.547076@news1.newscene.com> <lNfq4.4823$QK6.56775@news4.mia>`

```
Hi Judson,

"Judson McClendon" <judmc@bellsouth.net> wrote:

>Dean T. Miller wrote:

>>I see you've never taken the CDP exams.
>
…[8 more quoted lines elided]…
>have specific knowledge, right?  So, the test measured knowledge.

The point of the above is that the knowledge measured was wide-ranging
enough to reject people who were active in the computer field but
didn't have adequate knowledge of the field.

By wide-ranging I mean the tests covered all areas of computer design,
operations and management.  The specific areas covered by the test
questions were a surprise to those being tested.  The only studying
possible was to study the entire field of computers (and tab
machines):  business, scientific and control.  

>I did not mean to imply that the tests were easy, or worthless, or
>that they had no meaning.  What I was trying to say is that raw
>knowledge simply does not equate with ability and/or performance.
>There is come correlation, yes.  

Well, the tests were timed (when I took them), so there is a type of
performance measurement.

But ... I agree that the tests weren't designed to measure conceptual
ability or the ability to come up with innovative solutions.

>But every one of us has known people
>who were very well educated, but could hardly tie their shoes in a
>practical situation, or solve a real world problem.  The fact is,
>there are factors far more important than raw knowledge.  

IMO, these tests were designed to reveal practical abilities, as
evidenced by my "boss's" rejection.  He had lots of theoretical
knowledge, but not much hands-on experience (How many punched cards
are in a stack 1" thick?).

>My point is that the correlation is much looser than might
>be expected, because there are a lot of people out there who have
>memorized a lot of facts, but who couldn't use one if it bit them in
>the nose.  Perhaps your old Army boss was such a person? :-)

Again, I agree.  


-- Dean -- from (almost) Duh Moines  (CDP, KB0ZDF)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<886tbi$3k9$1@nnrp1.deja.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A50D8D.201A@NOSPAMguysoftware.com> <38a6e8c0.364507854@news1.newscene.com>`

```
You can see a page for the H-200 at foodman123.com/history.htm
I used to dance on the console, too.

Tony Dilworth


In article <38a6e8c0.364507854@news1.newscene.com>,
  dtmiller@midiowa.net wrote:
> Hey Ed,
>
> Ed Guy <ed_guy@NOSPAMguysoftware.com> wrote:
>
> >Yeah, back then we ran a whole damn company (a major utility) on a
Honeywell 200 with
> >24K (that's 24,000 BYTES) of RAM (known as "core" then) with four
tape drives, one
> >reader-punch, one line printer, no disk, no console typewriter. (Had
to "boot" it the
> >hard way by keying in machine code with the buttons on the box).
> >I had a routine that printed 20 rows of * on the line printer to
wake up the operator
> >and lure him/her out of the little office to look at the message
giving instructions for
> >tape mounts or whatever.
>
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Dinosaur Code!

- **From:** Scott Peterson <scottp4.removethis@mindspring.com>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<nqs9asspfhi24trceje45312caj8ed51fm@4ax.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
docdwarf@clark.net () wrote:

>
>Some folks just talk about the Oldene Dayse, when (person) could do
…[33 more quoted lines elided]…
>

Pretty straight forward stuff for the really old DOS days. No device
indpendence with this stuff and all those wierd options in the select
and assign clauses worked.

I'd be much more interested in seeing what the procedure division code
looked like.  The last place I worked had some code like this that had
been converted from Honeywell to IBM in the early seventies  The
results were the most unreadable code I've ever seen. 


                         
                         		Scott Peterson


If someone with multiple personalities threatens 
to kill himself, is it considered a hostage situation?
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<uvJp4.5562$lK6.128192@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <nqs9asspfhi24trceje45312caj8ed51fm@4ax.com>`

```
In article <nqs9asspfhi24trceje45312caj8ed51fm@4ax.com>,
Scott Peterson  <scottp4.removethis@mindspring.com> wrote:

[snippage]

>I'd be much more interested in seeing what the procedure division code
>looked like.  The last place I worked had some code like this that had
>been converted from Honeywell to IBM in the early seventies  The
>results were the most unreadable code I've ever seen. 

Ow... I understand your desire, Mr Peterson, but I wonder how passing any
substantial chunk o' code to you might square with the usual
non-disclosure agreements; I trust you'll understand my reticence.

DD
```

#### ↳ Re: Dinosaur Code!

- **From:** Jeffry Kennedy <jakcert@attglobal.net>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38A7FF3E.F3E2AEE1@attglobal.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net>`

```
Awww doc you sure have a sweet way with code<G>  I think we have a couple of
2314 or 2311 spindles in the back room sitting next to the card reader punch
if you'd like to try them on for size.  Luckily we are fresh out of
"alternate areas'  ROFL.

PatH

docdwarf@clark.net wrote:

> Some folks just talk about the Oldene Dayse, when (person) could do
> (activity) such at ten people cannot do today... other folks work in
…[38 more quoted lines elided]…
> DD
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** docdwarf@clark.net ()
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7ATp4.5720$lK6.133190@iad-read.news.verio.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net>`

```
In article <38A7FF3E.F3E2AEE1@attglobal.net>,
Jeffry Kennedy  <jakcert@attglobal.net> wrote:
>Awww doc you sure have a sweet way with code<G>

Gosh, I bet you say that to *all* the coders... I'd blush, were I able to
remember how!

>I think we have a couple of
>2314 or 2311 spindles in the back room sitting next to the card reader punch
>if you'd like to try them on for size.  Luckily we are fresh out of
>"alternate areas'  ROFL.

Actually, the only reason I remember that bit of arcana is because an
instructor of mine got bored in class one day and said 'Now, you don't
have to remember this but...' and told a story about a problem solved by
using the RESERVE NO ALTERNATE AREAS option... it was one of the things
which pointed me towards consulting, actually.

DD
```

##### ↳ ↳ Re: Dinosaur Code!

- **From:** kiyoinc@ibm.XOUT.net (cory hamasaki)
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net>`

```
On Thu, 1 Jan 1970 00:59:59, Jeffry Kennedy <jakcert@attglobal.net> 
wrote:

> Awww doc you sure have a sweet way with code<G>  I think we have a couple of
> 2314 or 2311 spindles in the back room sitting next to the card reader punch
…[4 more quoted lines elided]…
> 

Serious?  Do you have a 3330-11 drive and control unit?  IBM, Memorex, 
CDC?   If so, drop me a line, a client was looking for one.

cory hamasaki

```

###### ↳ ↳ ↳ Re: Dinosaur Code!

- **From:** Jeffry Kennedy <jakcert@attglobal.net>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<38A951F8.D42F996F@attglobal.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost>`

```
sorry Cory no such luck.  I was trying to find those for you 2 years ago with no
success.  I miss spoke we don't have the spindles(ie drives) I think we just have
a few disk packs buried somewhere.  Maybe not even those any more.  But I did find
a 407 board back in the store room.  Unfurtunately I can't find the box of wires
for it  or the 407 for that mater<G>

PatH the curator

cory hamasaki wrote:

> On Thu, 1 Jan 1970 00:59:59, Jeffry Kennedy <jakcert@attglobal.net>
> wrote:
…[12 more quoted lines elided]…
> cory hamasaki
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 4)_

- **From:** kiyoinc@ibm.XOUT.net (cory hamasaki)
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<5CPnPdd87dY0-pn2-8d5eTCiIyEFI@localhost>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost> <38A951F8.D42F996F@attglobal.net>`

```
On Thu, 1 Jan 1970 00:59:59, Jeffry Kennedy <jakcert@attglobal.net> 
wrote:

>   I was trying to find those for you 2 years ago with no
> success.  I miss spoke we don't have the spindles(ie drives) I think we just have
…[3 more quoted lines elided]…
> 

No problem.   They haven't asked about it for a while.   I suspect that 
even if it's not a hot topic, they'd fund a data recovery but I don't 
have an open task order to do the recovery so, it's not my problem.

As for the 407, I saw a warehouse of EAM gear in 1995.   I went back in 
1997-8 and the guy had sent all the machines to the scrap metal dealer.

If you have a 2314, 2311, 3330 diskpack or what ever.  It might be fun
to keep one just to show people how big the old disks were.

cory hamasaki

```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 5)_

- **From:** Frank Ney <croaker@barkingmad.org>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<9a2jas0fa9usf6lmlipskpt6t5gshmap50@4ax.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost> <38A951F8.D42F996F@attglobal.net> <5CPnPdd87dY0-pn2-8d5eTCiIyEFI@localhost>`

```
On 15 Feb 2000 14:42:44 GMT, an orbiting mind control laser caused
kiyoinc@ibm.XOUT.net (cory hamasaki) to write:

>If you have a 2314, 2311, 3330 diskpack or what ever.  It might be fun
>to keep one just to show people how big the old disks were.

And if you get tired of keeping it around, you could always make a few
clocks...


Frank Ney  N4ZHG  WV/EMT-B  LPWV  NRA(L) ProvNRA GOA CCRKBA JPFO
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 6)_

- **From:** "D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<t5iq4.366$yR5.4568@news.uswest.net>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost> <38A951F8.D42F996F@attglobal.net> <5CPnPdd87dY0-pn2-8d5eTCiIyEFI@localhost> <9a2jas0fa9usf6lmlipskpt6t5gshmap50@4ax.com>`

```

"Frank Ney" <croaker@barkingmad.org> wrote in message
news:9a2jas0fa9usf6lmlipskpt6t5gshmap50@4ax.com...
> On 15 Feb 2000 14:42:44 GMT, an orbiting mind control laser caused
> kiyoinc@ibm.XOUT.net (cory hamasaki) to write:
…[5 more quoted lines elided]…
> clocks...

What about mobiles?

Speaking of clocks ... what's the going price for junk CDs these days?  I
have a few thousand that are rapidly depreciating into that class.  ;-)
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 7)_

- **From:** Frank Ney <croaker@barkingmad.org>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<83ujas8c87mflqpl8s3j50d68g7hc6m1i2@4ax.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost> <38A951F8.D42F996F@attglobal.net> <5CPnPdd87dY0-pn2-8d5eTCiIyEFI@localhost> <9a2jas0fa9usf6lmlipskpt6t5gshmap50@4ax.com> <t5iq4.366$yR5.4568@news.uswest.net>`

```
On Tue, 15 Feb 2000 13:45:04 -0600, an orbiting mind control laser caused
"D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
to write:

>
>"Frank Ney" <croaker@barkingmad.org> wrote in message
…[13 more quoted lines elided]…
>have a few thousand that are rapidly depreciating into that class.  ;-)

Making clocks out of AOL install CDs is kind of tacky...


Frank Ney  N4ZHG  WV/EMT-B  LPWV  NRA(L) ProvNRA GOA CCRKBA JPFO
```

###### ↳ ↳ ↳ Re: Dinosaur Code!

_(reply depth: 8)_

- **From:** alizard[spam]@ecis.com (A.Lizard)
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<38aadfb0.846539@news.ecis.com>`
- **References:** `<2g_o4.4570$lK6.100048@iad-read.news.verio.net> <38A7FF3E.F3E2AEE1@attglobal.net> <5CPnPdd87dY0-pn2-Rj356cdX6H4X@localhost> <38A951F8.D42F996F@attglobal.net> <5CPnPdd87dY0-pn2-8d5eTCiIyEFI@localhost> <9a2jas0fa9usf6lmlipskpt6t5gshmap50@4ax.com> <t5iq4.366$yR5.4568@news.uswest.net> <83ujas8c87mflqpl8s3j50d68g7hc6m1i2@4ax.com>`

```
On Wed, 16 Feb 2000 01:55:44 GMT, Frank Ney
<croaker@barkingmad.org> wrote:

>On Tue, 15 Feb 2000 13:45:04 -0600, an orbiting mind control laser caused
>"D. Scott Secor - Millennial Infarction Mitigator" <y2k@uswest.net.NO$PAM>
…[6 more quoted lines elided]…
>>> kiyoinc@ibm.XOUT.net (cory hamasaki) to write:
[snip]
>>have a few thousand that are rapidly depreciating into that class.  ;-)
>
>Making clocks out of AOL install CDs is kind of tacky...
>
Using them for the purpose AOL intends is considerably tackier.

A.Lizard

************************************************************************
"Here's the most exasperating part: Ninety-five percent of the Y2k hoax
hysteria is planted by people who stand to gain, head-lined by
propagation-hungry publishers, and purveyed as truth by perpetuators of
rumour." Dave Eastabrook
"Anybody who still believes in the media must have been in a coma for 
the past 30 years." - Robert Anton Wilson
Personal Web site http://www.ecis.com/~alizard
Y2Kinfo: http://www.ecis.com/~alizard/y2k.html
Littleton page:http://www.ecis.com/~alizard/littleto.html
backup address (if ALL else fails) alizard@[spam]onebox.com
PGP 6.5.1 key available by request,keyserver,or on my Web site
PGPfone v1.02 and v2.1 available for secure voice conferencing, get
your own (W9x,NT,Mac) at http://www.pgpi.org/products/nai/pgpfone/
************************************************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
