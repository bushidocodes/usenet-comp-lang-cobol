[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL batch compiles

_43 messages · 6 participants · 2010-07 → 2010-08_

---

### PowerCOBOL batch compiles

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-31T01:17:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bg1mjF2teU1@mid.individual.net>`

```
I have a client who has a fairly major application written as a series of 
PowerCOBOL projects.

Building this for new releases is a maor undertaking and each project has to 
be activated  (compiled and built) by hand.

I have a solution but, before implementing it, I would like to be sure I'm 
not re-inventing the wheel.

Does anyone have any thoughts or existing approaches to this problem?

I'll state my solution if  there are no better ideas. If you have a solution 
and would be prepared to sell it to us, please let me know by private mail, 
giving a brief overview and some sample screen shots.

Basically, the solution should be able to:

1. Permit selection of any number of PowerCOBOL projects.
2. Batch build and compile the specified projects in 1 above and provide 
compiler listings and diagnostics for each compilation, along with object 
modules (.DLL or .EXE) as specified for each project.
3. Compiles must be able to run locally or remotely on a "COBOL server" with 
source, objects and listings, all delivered back to specified directories.

My solution will do this, but if you have anything close that does some or 
all of it, please talk to me :-)

Pete.
```

#### ↳ Re: PowerCOBOL batch compiles

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-07-30T14:04:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H-idnbDWyZ3Tv87RnZ2dnUVZ_jCdnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I have a client who has a fairly major application written as a
> series of PowerCOBOL projects.
…[23 more quoted lines elided]…
> some or all of it, please talk to me :-)

Yeah, we do/did that.

COMPILE.BAT

@ECHO OFF
IF %1X == RELEASEX GOTO USAGEOK
IF %1X == DEBUGX GOTO USAGEOK
ECHO .
ECHO Usage is COMPILE RELEASE or COMPILE DEBUG
GOTO QUIT

:USAGEOK
ECHO BEGIN > RESULT.TXT
ECHO List of attempted compilations %DATE%  %1 > COMPLIST.TXT
ECHO List of compiles > COMPLIST.TXT
FOR %%A IN (BIS*.PPJ) do call :compile2 %%A %1
FOR %%A IN (*.BLG) DO TYPE %%A >> RESULT.TXT
FOR %%A IN (*.BLG) DO DEL %%A
GOTO QUIT

:COMPILE2
@ECHO OFF
REM PC User's Guide Chap 6, p 253
ECHO %1
echo %1 >> COMPLIST.TXT
ECHO Compile %1
echo === BEGIN %1  >> RESULT.TXT


POWERCOB /REBUILD /%2 %1
REM POWERCOB /REBUILD /RELEASE %1


IF ERRORLEVEL 1 GOTO FAIL
GOTO OK

:FAIL
ECHO . >> RESULT.TXT
ECHO !!!  E R R O R  I N   %1    !!! >> RESULT.TXT
ECHO . >> RESULT.TXT
GOTO :EOF

:OK
TYPE *.BLG >> RESULT.TXT
DEL *.BLG /Q
echo === END %1 >> result.txt
ECHO =============================== >> RESULT.TXT
ECHO =============================== >> RESULT.TXT
ECHO . >> RESULT.TXT
ECHO . >> RESULT.TXT
GOTO :EOF

:QUIT

-------
```

##### ↳ ↳ Re: PowerCOBOL batch compiles

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-31T13:08:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhbclFjjoU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <H-idnbDWyZ3Tv87RnZ2dnUVZ_jCdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> I have a client who has a fairly major application written as a
…[79 more quoted lines elided]…
> -------

Jerry,

thanks very much for posting this. It is food for thought and I'll consider 
it in more detail. Obviously, I'd like something better than a DOS batch 
file but the principles are interesting and I never denigrate anything that 
works. I think I can produce something more or less equivalent in WSH and 
then integrate that with a .NET front end or the existing Toolset tabbed 
interface.

(Just looking through it was a trip down memory lane :-) "The ghost of Xmas 
past"...)

Thanks for the response.

Pete.
```

#### ↳ Re: PowerCOBOL batch compiles

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-30T12:05:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<424622f2-c857-49be-b8cc-d5b5c214d76b@v6g2000prd.googlegroups.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net>`

```
On Jul 31, 1:17 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I have a client who has a fairly major application written as a series of
> PowerCOBOL projects.
…[23 more quoted lines elided]…
> all of it, please talk to me :-)

I don't have a Windows Fujitsu COBOL available currently so I can't
test for your environment, but project uses make to do the compiles.
When 'build' is selected it writes a makefile and starts make.

It is only necessary to capture these makefiles and tailor them to
suit your needs and have a batch file kick off the ones that you need.
```

##### ↳ ↳ Re: PowerCOBOL batch compiles

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-31T12:50:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhaa9FehkU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <424622f2-c857-49be-b8cc-d5b5c214d76b@v6g2000prd.googlegroups.com>`

```
Richard wrote:
> On Jul 31, 1:17 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[35 more quoted lines elided]…
> suit your needs and have a batch file kick off the ones that you need.

Yes, that is how our existing batch compiles work. MAKE is already 
integrated into our solution for batch compiling NETCobol. PowerCOBOL is a 
little more difficult, not so much from the actual mechanics of compilation, 
but for integrating this with the existing Toolset.

There is also a complication with compiling for COM. The process needs to 
override the compiler assigned GUID  and assign its own, so we can reference 
it later. However, the Toolset already does that for NETCobol COM components 
and it is just a different template for PowerCOBOL so I am confident we can 
do it.

Thanks for the post, Richard.

Pete.
```

#### ↳ OOPS! PowerCOBOL batch compiles

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-07-30T14:10:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I have a client who has a fairly major application written as a
> series of PowerCOBOL projects.
…[25 more quoted lines elided]…
> Pete.

I skipped over the part where you were willing to PAY for a solution!

Oh well, maybe our efforts can contribute to the overall knowledge base of 
the group. I just want to make this a better world.

In that regard, I just started a new police story book. In the first five 
pages, I've added the following to my language style:

* Giving us the stink eye.
* Flashlight therapy
* They gonna be drawin' you in chalk on the sidewalk
* 'Roided up primate
* Hold a grudge longer than my ex-wife
* The medicine man's gonna be waving chicken claws over your ashes
* You're circling the drain

By the time I finish the book, I'll be erudite for sure.
```

##### ↳ ↳ Re: OOPS! PowerCOBOL batch compiles

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-31T13:02:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhb0sFhuaU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> I have a client who has a fairly major application written as a
…[27 more quoted lines elided]…
> I skipped over the part where you were willing to PAY for a solution!

Well, I already have a solution; I would pay for anything that helps me 
implement it quicker or contributes towards it.

Jerry, I absolutely promise you if we use any part of what you posted and 
make profit from it, you will be contacted and I'll work out something with 
you, just as I would for anyone else.

I don't expect people to make money for me, I don't steal ideas, and I am 
more than happy to share the results of joint effort.

Just being able to discuss options is actually helpful, but that is no more 
than I would do for others... :-)

>
> Oh well, maybe our efforts can contribute to the overall knowledge
> base of the group. I just want to make this a better world.

Speaking for myself, I can say your posts here over years have already done 
that... :-)
>
> In that regard, I just started a new police story book. In the first
…[9 more quoted lines elided]…
>

One of the things I loved about my stay in Texas was the very colourful 
figures of speech. It seems the criminals are not excluded from this :-)

(I especially loved number 4... but all of them made me smile.)


> By the time I finish the book, I'll be erudite for sure.

I can see that police work in Texas (and probaly anywhere, for that 
matter...) is definitely educational...

Pete.
```

###### ↳ ↳ ↳ Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-31T13:36:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhd06Fr0qU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> Pete Dashwood wrote:
…[65 more quoted lines elided]…
> (I especially loved number 4... but all of them made me smile.)

Sorry, that should have been number 5. It is Saturday morning here, I got to 
bed at 3:30 after a thoroughly enjoyable Friday night (It was National 
Poetry Day here and I was involved in some celebrations that involved me 
playing music and reciting, egged on by an increasingly drunken bunch of 
Friday Niters who were also doing their party pieces. It was a public 
function with, free admission (food and booze you paid for) in the heart of 
our city so you can imagine that we got a good cross section of poetry and 
general entertainment. (I was quite amazed by the talent there is in this 
town. Some of these people should definitely be performing for a living.) 
One Australian, who had already had a few too many, got up and recited the 
entire saga of "The Man from Snowy River" (by Banjo Patterson, if you want 
to look it up; a stirring piece of poetry), without a single hiccup or 
error, did it passionately in a totally appropriate Australian accent, to 
tumultuous applause. Another guy, who looked like he might have been 
homeless, recited W.B. Yeats' "The Song of Wandering Aengus" (It's the one 
which ends with "the silver apples of the moon, the golden apples of the 
sun" - Ray Bradbury wrote a short story named from it) and again, it was 
flawless. You could've heard a pin drop until he finished and then there was 
huge applause. We had various musicians doing stuff and it was a throughly 
enjoyable evening. However, the result for me is that my focus this morning 
is not what it should be and I mis-counted the rows above... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-07-30T22:22:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Sorry, that should have been number 5. It is Saturday morning here, I
…[21 more quoted lines elided]…
> not what it should be and I mis-counted the rows above... :-)

National Poetry Day? Heh!

We just had a kerfuffle here. An arch-conservative, Glenn Beck, wrote a new 
fiction book, "The Overton Window." Here's a youtube trailer for the book:

http://www.youtube.com/watch?v=wBoeHgy7svg

Further, the poem also appears on the book jacket. Here it is:

-----

As it will be in the future, it was at the birth of Man
There are only four things certain since Social Progress began.
That the Dog returns to his Vomit and the Sow returns to her Mire,
And the burnt Fool's bandaged finger goes wabbling back to the Fire;

And that after this is accomplished, and the brave new world begins
When all men are paid for existing and no man must pay for his sins,
As surely as Water will wet us, as surely as Fire will burn,
The Gods of the Copybook Headings with terror and slaughter return!

-----

Well, when the political liberals saw this, they went nuts. Waving this tome 
aloft, they cried that Beck was insane, that whoever could concoct such as 
this was obviously diseased. The author should be burnt at the stake and the 
ashes scattered (take no chances). I'm serious the "progressives" nearly 
itched to death!

The poem, "The Gods of the Copybook Headings," was written by Rudyard 
Kipling in 1919.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-01T01:00:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bil48FgrnU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[46 more quoted lines elided]…
>

As Kipling is one of my favourites I am familiar with the poem. Those are 
the last two verses. It is worth reading the whole thing:

http://wolfpangloss.wordpress.com/2007/10/24/kipling-the-gods-of-the-copybook-headings/


> Well, when the political liberals saw this, they went nuts. Waving
> this tome aloft, they cried that Beck was insane, that whoever could
…[5 more quoted lines elided]…
> Kipling in 1919.

After his only (and much loved) son had been tragically killed pointlessly 
in the First World War. (BBC made an excellent documentary about the 
circumstances leading to, and culminating in, the lad's demise.

I viewed the video link but it is just a dramatic presentation of the last 
two verses of Kipling's poem.

It didn't give much insight into what exactly the "Overton Window" is about.

I then found this:
http://www.youtube.com/watch?v=26fdAIVzZYo&feature=related

It is interesting, but for an entire society to get excited about what is 
simply a negotiation stratagem and recognised by anyone who has studied 
conflict resolution and negotiation as the "Salami" ploy, is a bit 
disappointing.

Obviously, this book is simply becoming a focal point for people whose 
political views are already polarised.

The dangerous thing about that is that while the extremists on both side are 
creating fire and smoke, it tends to overwhelm the people in the centre 
which is where sanity normally resides...

I look forward to the movie... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-01T10:40:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net>`

```
Pete Dashwood wrote:


> It is interesting, but for an entire society to get excited about
> what is simply a negotiation stratagem and recognised by anyone who
…[9 more quoted lines elided]…
>

The "entire society" didn't get polarized over a negotiation strategy - no 
one had even READ the book.

The left got exercised over the POEM! Some of their commentators latched on 
to it (the poem) as evidence of a warped mind so compromised by disease or 
defect as to prove that all the thoughts emanating from its author were 
alien to life itself, if not the stability of the solar system.

The negotiation strategy is simply the engine that drives the story - heck, 
I once read a thriller where the engine was the thought process of the lead 
detective who was killed on page two! Every fiction work (except those by 
James Fennimore Cooper) has to have a thread that ties the various bits 
together. No, the excitement was not over the story or the thread; it was 
over the poem.

A few years ago, there was damn near a race riot in D.C. when one (white) 
city councilman accused another (black) of being niggardly.

Just this past week, a congress-critter suggested that the Federal 
Communications Commission yank the license of the Fox Network. The FCC 
doesn't license networks, only broadcast stations. We had one Congressman 
who, when questioning the Chairman of the Joint Chiefs of Staff earilier 
this year over the proposed relocation of 5,000 Marines, their families, and 
equipment to Guam, inquired as to whether the increased weight might cause 
the island to tip over and sink.

'Tis a pity that those in power are dumber than a crate of anvils.

But it is what it is. That's why we need experts (i.e., "special interests") 
to advise them.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-02T12:23:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bmhg2F4b6U1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>
…[15 more quoted lines elided]…
> - no one had even READ the book.

I have a feeling that is going to change... :-)

Whatever else is happening this is a very good example of viral book 
marketing.
>
> The left got exercised over the POEM! Some of their commentators
…[3 more quoted lines elided]…
> stability of the solar system.

Well, Kipling upset a lot of people (including Queen Victoria) during his 
lifetime and, as a result was never made Poet Laureate (which many people 
thought he should have been). He wrote a poem about British soldiers being 
killed for sixpence a day and the Queen was not amused. The last verse, 
although a statement of what was happening in his time, is a chilling 
premonition of what is happening currently.

http://www.daypoems.net/poems/1799.html

One of the criteria for assessing poetry is the reaction it evokes. It is no 
surprise to me that a Kipling poem is still "working" almost 100 years after 
it was written.

It is a bit ironic that the Left are offended, though. Kipling was 
politically Left of centre all his life and horrified by the class system 
and the entrenched tyranny of the Right wing upper classes. However, he 
believed in duty, decency, and honour, and these things are often associated 
with the establishment and the Right. (My personal opinion is that he may 
have re-evaluated some of the established forms of this after his son was 
killed, but I may be doing him a disservice. Certainly he knew the risks and 
was proud that his son went to serve.)

>
> The negotiation strategy is simply the engine that drives the story -
…[3 more quoted lines elided]…
> ties the various bits together.

Yes, most of us struggled with "The Last of the Mohicans"... :-)


> No, the excitement was not over the
> story or the thread; it was over the poem.

I don't think that is a bad thing. It depends... If the people got incensed 
because they had taken two verses of the poem out of context and didn't 
really understand what it was saying, then that is something else, but 
agitation caused by poetry is generally a "Good Thing".

>
> A few years ago, there was damn near a race riot in D.C. when one
> (white) city councilman accused another (black) of being niggardly.

Yes, I read about that at the time. In a way it is amusing, but in another 
way it is frightening...

>
> Just this past week, a congress-critter suggested that the Federal
…[6 more quoted lines elided]…
> sink.

Without seeing the context, it is hard to comment. He may have intended it 
as a figure of speech. Could ANYONE really believe that? I don't think so.
>
> 'Tis a pity that those in power are dumber than a crate of anvils.

In a Democracy, we seldom get the politicians we want; we invariably get the 
politicians we deserve.
>
> But it is what it is. That's why we need experts (i.e., "special
> interests") to advise them.

Hmmm... that's OK as long as the process is open and the people are 
answerable for the advice they give.

Pete.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-02T14:36:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <8bmhg2F4b6U1@mid.individual.net>`

```
On Mon, 2 Aug 2010 12:23:28 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>In a Democracy, we seldom get the politicians we want; we invariably get the 
>politicians we deserve.

I disagree - depending on how you are defining "we".   Or are you
saying that trying very hard but failing to get the politician we want
means we deserved what we got because of our failure?   And our
children deserved it as well because of our failure?

When we get the politicians we want, we deserve what we get.   
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-03T23:12:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bqbttF78lU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 2 Aug 2010 12:23:28 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[3 more quoted lines elided]…
>> get the politicians we deserve.

I first made this observation 40 years ago after being bitterly disappointed 
that the people I supported did not win the election. In the ensuing years I 
have become older and wiser and reflected on it.

If we have implemented a system which gives us a voice, but have grown too 
lazy and apathetic to get more than a 40% turnout to the polls on election 
day (in Australia, it is illegal not to vote, although you can legally spoil 
your paper; in NZ voting is optional), then we do indeed deserve the idiots 
that get into power.

If the population has become so inured to bad results ("Don't vote; the 
Government will get in...") that people have become politically apathetic or 
apolitical, then we do indeed deserve the idiots that get to into power.

If the system has become so badly broken that "public service" is all about 
getting your snout in the trough,  then we do indeed deserve the idiots that 
get to into power.


>
> I disagree - depending on how you are defining "we".   Or are you
…[4 more quoted lines elided]…
> When we get the politicians we want, we deserve what we get.

Whether they are the ones we want or the ones we don't want, in a democratic 
society, we deserve what we get.

I stand by my statement.

Pete.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-03T08:55:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abg56tn6ksjtucrsb8d9kc63fl348udm1@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <8bqbttF78lU1@mid.individual.net>`

```
On Tue, 3 Aug 2010 23:12:59 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>If we have implemented a system which gives us a voice, but have grown too 
>lazy and apathetic to get more than a 40% turnout to the polls on election 
>day (in Australia, it is illegal not to vote, although you can legally spoil 
>your paper; in NZ voting is optional), then we do indeed deserve the idiots 
>that get into power.

I thought they just got taxed for not voting, thanks for the
clarification.     The question is - does mandated voting result in
better results?

And the other question is who is "we", that deserve the idiots? Those
who voted for the idiots?   Those who campaigned tireless and voted
for the idiots' opponents - but failed?
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 9)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-03T14:50:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 2 Aug 2010 12:23:28 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> When we get the politicians we want, we deserve what we get.

Lawrence J. Peter (discoverer of the "Peter Principle") once said: "I have 
been studying governments, man and boy, for over forty years. I have yet to 
discover whether we are being led by well-meaning fools or by really bright 
people who are just putting us on."

My rendition: "In a suitably advanced society, it is impossible to tell 
whether a government action is motivated by malice or incompetence."
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-03T13:53:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drsg56t14bj5hu69tmga5o9ohr0ma4rle9@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <CNidnQrtOpZYvs7RnZ2dnUVZ_qydnZ2d@earthlink.com> <8bhb0sFhuaU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com>`

```
On Tue, 3 Aug 2010 14:50:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>Lawrence J. Peter (discoverer of the "Peter Principle") once said: "I have 
>been studying governments, man and boy, for over forty years. I have yet to 
>discover whether we are being led by well-meaning fools or by really bright 
>people who are just putting us on."

I suspect many of our leaders in government and elsewhere are
somewhere in between.

>My rendition: "In a suitably advanced society, it is impossible to tell 
>whether a government action is motivated by malice or incompetence." 

Trolls are another example of people who play roles until that role is
them.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-04T13:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i3bq4u$9ao$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <drsg56t14bj5hu69tmga5o9ohr0ma4rle9@4ax.com>`

```
In article <drsg56t14bj5hu69tmga5o9ohr0ma4rle9@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>Trolls are another example of people who play roles until that role is
>them.

From http://www.gutenberg.org/files/4363/4363.txt :

--begin quoted text:

146. He who fights with monsters should be careful lest he thereby become 
a monster. And if thou gaze long into an abyss, the abyss will also gaze 
into thee.

(Nietzsche, 'Beyond Good and Evil', tr. Helen Zimmern)

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-04T09:44:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ok2j565hsefue3q5pi65hnd3ofgo16j96v@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <drsg56t14bj5hu69tmga5o9ohr0ma4rle9@4ax.com> <i3bq4u$9ao$2@reader1.panix.com>`

```
On Wed, 4 Aug 2010 13:32:14 +0000 (UTC), docdwarf@panix.com () wrote:

>--begin quoted text:
>
…[8 more quoted lines elided]…
>DD

Very good.    Of course I'm* not subject to that, I'm careful.
*  For a very large value of "I".
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-04T13:26:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i3bpq2$9ao$1@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com>`

```
In article <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Howard Brazee wrote:

[snip]

>> When we get the politicians we want, we deserve what we get.
>
…[6 more quoted lines elided]…
>whether a government action is motivated by malice or incompetence." 

I was taught 'never attribute to malice that which can be explained by 
incompetence'; a cursory bit of research reveals:

From http://en.wikiquote.org/wiki/Robert_J._Hanlon :

--begin quoted text

In The Sorrows of Young Werther (ed. note: 1774) Goethe declared: 
"Misunderstandings and neglect occasion more mischief in the world than 
even malice and wickedness. At all events, the two latter are of less 
frequent occurrence."

In his story Logic of Empire (1941) Heinlein declares: "You have 
attributed conditions to villainy that simply result from stupidity". He 
calls this the "devil theory" of sociology. 

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-04T09:52:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com>`

```
On Wed, 4 Aug 2010 13:26:26 +0000 (UTC), docdwarf@panix.com () wrote:

>I was taught 'never attribute to malice that which can be explained by 
>incompetence';

Me too.   I'm a big believer in incompetence, and I believe that most
all villains think they're the good guys, or at least they are right
to respond to their injustices.    Someone can, say decide to start an
unwinnable war to protect us - if it doesn't protect us and also costs
us dearly, then it is incompetence to blame.

Trouble is, the victims aren't any better off being destroyed by
incompetence.   

Our society has a value where we don't punish people as much who
either didn't mean to do their crime or who commit their crime in a
state of high passion.    That doesn't protect the rest of us though.
Consider, who is the bigger danger to you - the guy who committed a
crime in road rage, or the guy who killed his spouse for the insurance
money?
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 12)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-04T11:32:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<peGdnafDeLOoC8TRnZ2dnUVZ_uednZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 4 Aug 2010 13:26:26 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[8 more quoted lines elided]…
>

If you're talking about the "War on Terror," the actual goal (and one which 
a politican cannot say) is "We are not in this war to win it because it is 
unwinnable. Our goal is not to lose."
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-04T10:46:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<la6j56h33hg1en9lkk77h99lobrptamra1@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <peGdnafDeLOoC8TRnZ2dnUVZ_uednZ2d@earthlink.com>`

```
On Wed, 4 Aug 2010 11:32:44 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>If you're talking about the "War on Terror," the actual goal (and one which 
>a politican cannot say) is "We are not in this war to win it because it is 
>unwinnable. Our goal is not to lose." 

It appears that the #1 war priority of all presidents since WWII is
"We won't lose this war on *my* watch".
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-04T17:30:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i3c82p$3o$1@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com>`

```
In article <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 4 Aug 2010 13:26:26 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>to respond to their injustices.

I recall it being pointed out by Socrates that all people do what they do 
with the belief that they are doing something good, at least for 
themselves.

[snip]

>Our society has a value where we don't punish people as much who
>either didn't mean to do their crime or who commit their crime in a
…[3 more quoted lines elided]…
>money?

It seems to be a matter of degree, almost an accepting of 
that-which-is-human; folks are not expected to be in control of themselves 
at all times, 'anyone can just snap', but not anyone is expected to be 
able to place the horror of murder in a context where they conclude that 
planning, forethought and timing are to be dedicated to it.

Our society seems to place great weight on intention, the 'mens rea' 
lawyers talk about, and the greatest opprobrium being reserved for those 
who premeditatively take another's life after 'lying in wait'.

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 12)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-04T21:21:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com>`

```
Howard Brazee wrote:
>
> Our society has a value where we don't punish people as much who
…[4 more quoted lines elided]…
> money?

There are three, and only three, acceptable reasons for punishment.
* To rehabilitate the offender,
* To protect society from further depredations by the accused, and
* To serve as a deterrent to other similarily inclined.

Just punishment SHOULD be different for the heat-of-passion killer and the 
assassin.

If you ever pass a prison where some of the inmates are outside the walls - 
cutting the grass and so on - be aware that they are almost always 
murderers!

Someone who kills in a fit of passion, who commits a crime of opportunity, 
is almost always a rule-follower. "Hey squint, check out a broom, sweep the 
sidewalks, and be back at 4:30" when addressed to a rode-rage murderer will 
be met by "Yes, boss."

On the other hand, the armed robber, the burglar, doesn't follow the rules. 
He started his escapade with the intent to be a criminal.

He won't be back at 4:30.
```

###### ↳ ↳ ↳ OT: crime and punishment WAS: Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-06T00:51:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bvqf8FuuiU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Howard Brazee wrote:
>>
…[5 more quoted lines elided]…
>> insurance money?

I have some strong views on punishment. I don't think it serves any real 
purpose, but for the sake of this argument, let's look at HeyBub's three 
conditions...

>
> There are three, and only three, acceptable reasons for punishment.

My position is that punishment is barbaric and pointless as a concept. BUT, 
I have to admit there are crimes (and specific criminals) for which 
rehabilition would seem to be impossible. (persistent re-offenders, certain 
classes of crime which show the perpetrator has no place in a civilized 
society, etc.). In these cases I would advocate death in as humane a manner 
as possible (little needle in the back of the hand, probably), or banishment 
(although finding places where you could banish such people to is 
increasingly difficult and there is no sound reason why the rest of society 
should support them in banishment or pay fees to a host country, any more 
than it should support them for long term imprisonment, so death is probably 
the cleanest, simplest, and certainly the cheapest solution overall. It also 
cleans up the gene pool... (Just as well I don't rule the world... :-))

Having stated my position, I'll now look at the three reasons in terms of 
it...


> * To rehabilitate the offender,

I am strongly in favour of rehabilitation. Any of us can slip up 
occasionally and need some correction. However, "rehabilitation" to me does 
not mean "conditioned response" (cf. "A Clockwork Orange") or obedience out 
of fear. It means the person concerned has genuinely realized that the 
behaviours they exhibited can't work in a society and they no longer have 
the need or desire to re-offend. In other words, a change of attitude 
towards a more positive contribution to society. I don't believe this 
transformation is achieved by punishment, so punishment is pointless as a 
means to rehabilitation.There has to be a change of mind, not just of 
behaviour. You can certainly coerce someone into changing their behaviour, 
but until they change their mind you haven't rehabilitated them.

> * To protect society from further depredations by the accused,

Locking them up achieves that. But I don't see locking them up as a 
punishment. It is just a necessary consequence of their actions until we are 
sure they can be trusted back in society. If we were going to punish them by 
imprisonment (and I am NOT advocating this) we'd go back to the days of 
dank, dark, deep, dungeons, with inmates chained and flogged regularly and 
fed bread and water. Instead we provide air-conditioned cells, a balanced 
diet, regular exercise, access to learning and colour TV (which shows it 
isn't punishment, just confinement.)


> and
> * To serve as a deterrent to other similarily inclined.

Unfortunately, to people who are that way inclined, the threat of punishment 
is no deterrent at all. They don't believe they will get caught so there is 
no fear of punishment. In the days when we hanged people for burglary and 
robbery, houses still got turned over and people still got robbed.

What is needed is to encourage the attitude that burglary and robbery create 
misery in society and are undesirable for that reason. (it may be you, your 
family or loved ones who are the next victims, so why inflict it on others?)

A change of mind. Impossible? Maybe.

But we have changed people's minds about drinking and driving and it was 
done by intensive TV campaign and not by punishment. (There are still some 
idiots who do this of course, but here in NZ statistics for this have not 
been increasing, despite an increasing number of road users. It is too soon 
to know if there is an actual decline or not. The good result is largely due 
to an intensive campaign to raise awareness of the terrible costs this has 
for society as a whole, by the use of dramatic (and clever) advertising.)

I believe that punishment stems from the desire for revenge, and that desire 
is far more destructive to the person nurturing it than it is to the target 
of it.

The result of "An eye for an eye and a tooth for a tooth" is a blind, 
toothless world.

I have had occasions in my life when I wanted revenge. (Not any more...). I 
felt much better when I was able to let it go and the funny thing was that 
the the people who I wanted it on got their come-uppance anyway.  You can't 
go through life ripping people off and behaving like a scumbag, and hope to 
get away with it indefinitely. Sooner or later the Universe steps in and 
restores a balance... In the East this process is called Karma, but whatever 
you call it you can see it in operation if you wait long enough.

I realise that many people will strongly disagree with what I've written 
here; nevertheless, it is what I believe so, as always, "I call 'em like I 
see 'em... " :-)

>
> Just punishment SHOULD be different for the heat-of-passion killer
> and the assassin.

Only if you believe there is a place for punishment at all. I don't, so I 
don't see any punishment as "just".


>
> If you ever pass a prison where some of the inmates are outside the
…[11 more quoted lines elided]…
> He won't be back at 4:30.

Very interesting and I'm sure you're right. I think it is an important 
distinction, but, as Howard says, who is the greater threat to us?

In both cases I'd like to see rehabilitation but it is certainly more 
difficult with some than with others.

I'd also like to see more positive ways for people to pay off their debt to 
society (community service, involvement in assistance programs etc.) so that 
rather than society exacting revenge, there can be much more positive 
results. The victims should also be a part of the rehabilitation process and 
recompense (not just financial) for victims should be inherent in it.

During the last few hundred years the criminal justice system has made major 
advances, but there are still criminals and much remains to be done.

How we deal with crime reflects on all of us and it isn't just the criminals 
who need to examine their attitude. Society as a whole has to get over the 
need for punishment and revenge; it changes nothing.

Pete.
```

###### ↳ ↳ ↳ Re: crime and punishment

_(reply depth: 14)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-05T08:53:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZrKdndeH2en_X8fRnZ2dnUVZ_r-dnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com> <8bvqf8FuuiU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> During the last few hundred years the criminal justice system has
…[6 more quoted lines elided]…
> Pete.

You make some good points. I would point out, however, that "retribution" is 
not an approved reason for punishment.

You're also correct that all punishment methodologies do not drive crime to 
zero. The question is, however, what would the crime rate be if there were 
no consequence for the perp? Or what would the crime rate be if the 
penalties were changed?

Societies have been tinkering with crime and it's aftermath since Cain 
killed Abel, mostly from the victim's perspective.

Just yesterday, a convicted federal judge petitioned the court for a 
reduction in his prison sentence because he was subjected to unspeakable 
horrors while confined to the Grey Bar Hotel (one of these psychologically 
debilitating episodes was having to listen to the screams of fellow inmates 
who were being raped).
```

###### ↳ ↳ ↳ Re: crime and punishment

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-06T14:20:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c19r8FjpvU1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com> <8bvqf8FuuiU1@mid.individual.net> <ZrKdndeH2en_X8fRnZ2dnUVZ_r-dnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[24 more quoted lines elided]…
> the screams of fellow inmates who were being raped).

As noted earlier, we, as a society are responsible for the state of the 
prisons we run. If criminal acts are flagrantly committed in prisons, if 
warders and guards are corrupt and turn a blind eye, then that has to be 
addressed and we need mechanisms in place to address it.

It is ridiculous to expect to rehabilitate people if they are placed in an 
institution that is less than exemplary. If prisons are allowed to 
disintegrate into lawless hell-holes, there will be no progress.

You don't want to hear how I would solve this...:-)

I'd simply close down the worst of these institutions and execute the 
inmates AND the guards and management who allowed it to become so bad. (This 
would save law-abiding taxpayers a fortune...) The inmates, because they 
were anti-social in the first place and preferred to remain so instead of 
trying to get better, the guards and warders because they derelicted their 
duty to provide an environment where people CAN get better, and failed to 
set an example of righteous behaviour that could inspire others to do what's 
right instead of what's easy.

Make it a policy that both staff and inmates are responsible for the state 
of a prison. And if the result is an unacceptable state, terminate the lot 
of them. :-)

(I realise this would probably result in not many people volunteering for 
the Prison Service... :-) Might need to have a process whereby staff could 
protest the policies being implemented or dissociate themselves on record 
from certain practices which were not helping the goal of providing a 
working crime-free environment where rehabilitation can occur. If there were 
more whstle blowers it might be possible to arrest the decline before the 
drastic actions I outlined were necessary. As long as warders and staff buy 
into the idea that crime is OK there will never be progress in dealing with 
crime. As long as guards turn a blind eye to illegal activity in jails there 
will never be progress in dealing with crime.

Complement this with an affirmative program for prisons. Points for the 
least number of riots and assaults, the least number of repeat offenders, 
validation for prisoners achieving education, inter-prison sport programs, 
and so on. Make prisons work to change minds. Reward positive behaviour by 
prisoners with days off their sentence, positive behaviour by guards and 
wardens  (above and beyond what is expected) with paid holiday days. Run 
role playing and dramatization groups where lessons can be learned about 
behaviour, and other options explored rather than negative outcomes, without 
preaching a religious message. )

Hey, maybe it wouldn't be so bad if I ruled the world, after all... :-)

Pete.
```

###### ↳ ↳ ↳ Re: crime and punishment

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-06T14:45:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c1babFqi2U1@mid.individual.net>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com> <8bvqf8FuuiU1@mid.individual.net> <ZrKdndeH2en_X8fRnZ2dnUVZ_r-dnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[11 more quoted lines elided]…
>

Whether it is "officially" or not, it certainly is in the minds of many 
people.


> You're also correct that all punishment methodologies do not drive
> crime to zero. The question is, however, what would the crime rate be
> if there were no consequence for the perp? Or what would the crime
> rate be if the penalties were changed?

It depends on the "penalties". I'm not suggesting there should be no 
consequences for crime. Far from it. I'm suggesting that the consequences 
should not involve pointless punishment. Instead, the consequences should be 
time consuming, require effort on the part of the perpetrator, but that 
effort should be worthwhile for all concerned. In effect, they work off 
their debt through positive action that helps the victims of their crime 
come to terms with it (at least as far as is possible; some victims will 
never recover from what was done to them) and helps them grow as people. The 
final result is of value to the reformed criminal and to society as a whole. 
There has still been damage done, but everything that could be done to 
repair it has been and there will not be a recurrence. It is the best we can 
hope for and I don't see punishment as being part of it.

>
> Societies have been tinkering with crime and it's aftermath since Cain
> killed Abel, mostly from the victim's perspective.

I think it's time we took a broader view. It should encompass the criminal, 
the victim, the correctional facilities, and society as a whole.In 
isolation, none of these can help lower the crime rate. Together, they 
possibly can. It isn't just about lowering the crime rate either. It is also 
about repairing as far as possible the damage already done.


>
> Just yesterday, a convicted federal judge petitioned the court for a
…[3 more quoted lines elided]…
> the screams of fellow inmates who were being raped).

I've covered this in a separate (less serious) post...

Pete.
```

###### ↳ ↳ ↳ Re: crime and punishment

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-06T12:10:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i3gu3g$nc4$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bvqf8FuuiU1@mid.individual.net> <ZrKdndeH2en_X8fRnZ2dnUVZ_r-dnZ2d@earthlink.com> <8c1babFqi2U1@mid.individual.net>`

```
In article <8c1babFqi2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>HeyBub wrote:

[snip]

>> Just yesterday, a convicted federal judge petitioned the court for a
>> reduction in his prison sentence because he was subjected to
…[4 more quoted lines elided]…
>I've covered this in a separate (less serious) post...

Hmmmm... in a previous posting a 'Member of Congress advocating' turned 
into a 'Professor of Law inquiring' after a request for a cite.

Leaving aside that prisoners are well-known for petioning for a variety of 
things one might wonder what this 'convicted federal jude' and 'prison 
rape' might turn into upon research.  There's little to be seen at 
<http://www.google.com/search?hl=en&tbo=p&rlz=1T4GGLL_en&tbs=nws%3A1&q=federal+judge+convicted+reduction+rape&aq=f&aqi=&aql=&oq=&gs_rfai=> 
but that might indicate only that it didn't make 'the news'.

So, once again... is anyone able to provide a citation which documents the 
assertion that 'a convicted federal judge petitioned for a reduction of 
sentence because he heard another inmate scream while being raped'?

(it would be in poor taste to ask 'if so, can anyone ascertain if the 
rapists were inmates or Law Enforcement Officers?')

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-05T13:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i3ed98$nvh$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com>`

```
In article <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Howard Brazee wrote:
>>
…[7 more quoted lines elided]…
>There are three, and only three, acceptable reasons for punishment.

'There are more things in heaven and earth, Horatio, than are dreamt of in 
your philosophy.'

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-05T08:52:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtjl56tqgir3kl08otc05gj0337faolf0h@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bmhg2F4b6U1@mid.individual.net> <dtae565kffn0pr7d574qpk5ka9f2stla98@4ax.com> <k9SdnZcV-MeW7sXRnZ2dnUVZ_tSdnZ2d@earthlink.com> <i3bpq2$9ao$1@reader1.panix.com> <co2j56li2cg3926dqgkvufentp5k0rtu5b@4ax.com> <dvydnbFpu-rbvcfRnZ2dnUVZ_jKdnZ2d@earthlink.com>`

```
On Wed, 4 Aug 2010 21:21:49 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>There are three, and only three, acceptable reasons for punishment.
>* To rehabilitate the offender,
…[4 more quoted lines elided]…
>assassin.

I suppose it depends on which of the above reasons dominate.    To
protect society, it makes sense to look at the criminal who is most
likely to repeat his crime.    I contend that would be the
heat-of-passion killer.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T12:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i36coi$6rm$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>`

```
In article <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]

>Just this past week, a congress-critter suggested that the Federal 
>Communications Commission yank the license of the Fox Network.

Cite, please?

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 8)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-02T07:42:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DYWdnX56qp7_IMvRnZ2dnUVZ_s-dnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <i36coi$6rm$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[7 more quoted lines elided]…
>

My bad. It wasn't a Congress-critter; it was Jonathan Zasloff, law professor 
at UCLA, on the notorious "JournoList"

"I hate to open this can of worms," he wrote, "but is there any reason why 
the FCC couldn't simply pull [Fox's'] broadcasting permit once it expires?"
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T12:58:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i36fdh$kr1$1@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com> <i36coi$6rm$2@reader1.panix.com> <DYWdnX56qp7_IMvRnZ2dnUVZ_s-dnZ2d@earthlink.com>`

```
In article <DYWdnX56qp7_IMvRnZ2dnUVZ_s-dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <euednZKJBpriCMjRnZ2dnUVZ_g-dnZ2d@earthlink.com>,
…[14 more quoted lines elided]…
>the FCC couldn't simply pull [Fox's'] broadcasting permit once it expires?" 

Curious how a 'congress-critter suggested' turns, when the facts are 
examined, into a law professor inquiring 'is there any reason'.

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T12:11:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i36ckt$6rm$1@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net>`

```
In article <8bil48FgrnU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>HeyBub wrote:

[snip]

>> Well, when the political liberals saw this, they went nuts. Waving
>> this tome aloft, they cried that Beck was insane, that whoever could
>> concoct such as this was obviously diseased. The author should be
>> burnt at the stake and the ashes scattered (take no chances). I'm
>> serious the "progressives" nearly itched to death!

[snip]

>It is interesting, but for an entire society to get excited about what is 
>simply a negotiation stratagem and recognised by anyone who has studied 
>conflict resolution and negotiation as the "Salami" ploy, is a bit 
>disappointing.

Speaking only from my small bit of This Side of the Pond, Mr Dashwood, I 
can confess to utter unawareness that such a book was published and saw no 
evidence that anyone of any study beyond grade-school evidence ought but 
sadness and boredom.

(note to those from other lands - whenever an American (or someone who 
purports to think like one )makes a statement about an entire group, such 
as 'all the political liberals' (or feels the need to qualify a labelling 
of a group with quotation marks, such as "prograssives" (" original)) it 
is, in my experience, less an attempt at description than it is an attempt 
at propagandising.)

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-02T07:53:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8bil48FgrnU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[28 more quoted lines elided]…
>

Your experience is sadly flawed.

When a smattering of the members of [group] assert something and no other 
member of [group] objects, one can fairly assume the assertion is 
universally accepted by all members of [group].

This concept is called "assent by silence" [qui tacet consentire videtur].

I put "progressives" (sorry about offending your sensitive nature with the 
typographical error) in scare quotes to signify the word does not represent 
its conventional meaning, but is rather an attempt by members of the liberal 
persuasion to rehabilitate their image.
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T13:03:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i36fnm$kr1$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com> <J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com>`

```
In article <J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:

[snip]

>> (note to those from other lands - whenever an American (or someone who
>> purports to think like one )makes a statement about an entire group,
…[12 more quoted lines elided]…
>This concept is called "assent by silence" [qui tacet consentire videtur].

My experience seems less flawed than that concept.

(when anyone (a member of the group 'homo sapiens') does not object to 
something another member of that group asserts 'one can fairly assume that 
the assertion is universally accepted by all members'... no need to reply, 
I guess)

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 8)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-08-02T13:28:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b10e56tmad3ibt4d6588av6udb8n97720b@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com> <J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com>`

```
On Mon, 2 Aug 2010 07:53:03 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>docdwarf@panix.com wrote:
>> In article <8bil48FgrnU1@mid.individual.net>,
…[38 more quoted lines elided]…
>

No it is not.  It is called apathy.


>I put "progressives" (sorry about offending your sensitive nature with the 
>typographical error) in scare quotes to signify the word does not represent 
>its conventional meaning, but is rather an attempt by members of the liberal 
>persuasion to rehabilitate their image. 
>

Regards,
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T23:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i37j11$jv8$1@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com> <J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com> <b10e56tmad3ibt4d6588av6udb8n97720b@4ax.com>`

```
In article <b10e56tmad3ibt4d6588av6udb8n97720b@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
>On Mon, 2 Aug 2010 07:53:03 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
>wrote:

[snip]

>>This concept is called "assent by silence" [qui tacet consentire videtur].
>>
>
>No it is not.  It is called apathy.

Hey, nobody has any feelings about apathy!

(An. Gr. 'pathos', a feeling, a-, without)

DD
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 9)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-02T20:53:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZNKdnbhq0pA868rRnZ2dnUVZ_vidnZ2d@earthlink.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com> <J4Gdnb87DvIiIsvRnZ2dnUVZ_rGdnZ2d@earthlink.com> <b10e56tmad3ibt4d6588av6udb8n97720b@4ax.com>`

```
SkippyPB wrote:
>>
>> When a smattering of the members of [group] assert something and no
…[8 more quoted lines elided]…
>

+1
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-02T14:41:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n2be569f45bagvvn4di28cth64udrqoi0q@4ax.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bhd06Fr0qU1@mid.individual.net> <pcudnZbmNsl9C87RnZ2dnUVZ_oqdnZ2d@earthlink.com> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com>`

```
On Mon, 2 Aug 2010 12:11:10 +0000 (UTC), docdwarf@panix.com () wrote:

>(note to those from other lands - whenever an American (or someone who 
>purports to think like one )makes a statement about an entire group, such 
…[3 more quoted lines elided]…
>at propagandising.)

Labels disguise truth and facts.    Some labels are "magic" and are
used without any real logic - for instance the same policy pushed by
Republicans when pushed by Democrats is "Socialism".

(When I compare what Obama is doing and what Reagan did and proposed,
it is not at all obvious to me that Reagan was more conservative).
```

###### ↳ ↳ ↳ Re: Oops! correction WAS: Re: OOPS! PowerCOBOL batch compiles

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-02T23:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i37j8h$jv8$2@reader1.panix.com>`
- **References:** `<8bg1mjF2teU1@mid.individual.net> <8bil48FgrnU1@mid.individual.net> <i36ckt$6rm$1@reader1.panix.com> <n2be569f45bagvvn4di28cth64udrqoi0q@4ax.com>`

```
In article <n2be569f45bagvvn4di28cth64udrqoi0q@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 2 Aug 2010 12:11:10 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>Labels disguise truth and facts.

Labels (say, for the amount of heat necessary to raise the temperature of 
1cc of pure water at sea level one degree Centigrade) allow for 
measurement and reproducible phenomena, as well.

>Some labels are "magic" and are
>used without any real logic - for instance the same policy pushed by
>Republicans when pushed by Democrats is "Socialism".

This might be a cause for some folks' asking into definitions and 
demonstrated chains of reasoning... funny how that works, eh?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
