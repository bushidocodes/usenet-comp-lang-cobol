[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu cobol debugging

_53 messages · 11 participants · 2008-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu cobol debugging

- **From:** "Steve Rainbird" <steve.nospam.rainbird@mssint.nospam.com>
- **Date:** 2008-10-15T17:13:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lmj5cFd4rklU1@mid.individual.net>`

```
Is there a way of tracing a Fujitsu Cobol program.

In Microfocus I can do SET TRACE and the READY TRACE and it will tell me 
what paragraphs are being executed.

Is there a similar function in Fujitsu Cobol.

TIA
```

#### ↳ Re: Fujitsu cobol debugging

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-15T13:41:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvdcf494kv3nnoq23a73s663t5aegvna66@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net>`

```
On Wed, 15 Oct 2008 17:13:30 +0100, "Steve Rainbird"
<steve.nospam.rainbird@mssint.nospam.com> wrote:

>Is there a way of tracing a Fujitsu Cobol program.
>
…[3 more quoted lines elided]…
>Is there a similar function in Fujitsu Cobol.

Use compiler option TRACE or -Dr [maxlines]  Default is a few hundred lines.
Trace output will go to (program).trc. You can change it with an environment variable.
Fujitsu does not use READY TRACE.
```

#### ↳ Re: Fujitsu cobol debugging

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-16T10:12:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ln4m5Fd51euU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net>`

```


"Steve Rainbird" <steve.nospam.rainbird@mssint.nospam.com> wrote in message 
news:6lmj5cFd4rklU1@mid.individual.net...
> Is there a way of tracing a Fujitsu Cobol program.
>
…[8 more quoted lines elided]…
> Steve

Why don't you add it to a project and build for debug?

Then you can step through it, watch variables, set breakpoints and animate 
it just like MF, if you want to.

TRACE is SO 1960s mainframe...:-)

Pete.
```

##### ↳ ↳ Re: Fujitsu cobol debugging

- **From:** "Steve Rainbird" <steve.nospam.rainbird@mssint.nospam.com>
- **Date:** 2008-10-15T23:19:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ln8jpFd3c90U1@mid.individual.net>`
- **In-Reply-To:** `<6ln4m5Fd51euU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <6ln4m5Fd51euU1@mid.individual.net>`

```


"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6ln4m5Fd51euU1@mid.individual.net...
>
>
…[24 more quoted lines elided]…
>

True, but mainly because I am telnet'ing into the server and compiling and 
running from the command line, but also because I guess I am a 1960's 
programmer (well 1970's really).
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-17T00:48:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6loo0rFdhaqtU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <6ln4m5Fd51euU1@mid.individual.net> <6ln8jpFd3c90U1@mid.individual.net>`

```


"Steve Rainbird" <steve.nospam.rainbird@mssint.nospam.com> wrote in message 
news:6ln8jpFd3c90U1@mid.individual.net...
>
>
…[32 more quoted lines elided]…
> programmer (well 1970's really).

I'm a 1960's programmer... but you grow...:-) I like to think I learned 
SOMETHING in 43 years...

This is really horrific at so many levels that I can't imagine anyone 
requiring productive work to be developed this way. Having open Telnet ports 
for development is insane (there are so many better ways this COULD be 
done... even FTP and batch compilation with scripting would be more secure 
than what you describe... and more transparent.). Compiling from a command 
line is primitive but reasonable, on a local machine... apart from that, 
there are all the tools that simply aren't available because of the 
constrained environment.

Although the Fujitsu IDE is not in the same league as Visual Studio or 
Eclipse, it is light years ahead of what you are doing... Building stuff as 
projects keeps everything tidy, gives you access to proper debugging, allows 
you to create .EXEs, .DLLs,  or COM servers, allows use of MAKE 
(automatically) and other utilities, not to mention: Object Browsing, easy 
linking to APIs (including Windows), Web Development  (CGI and ISAPI), and 
Source program control, all at your fingertips. Some of these things you CAN 
set up through the command line, but it is MUCH easier to do it in the IDE.

Certainly, I use remote compilation for generated COBOL programs,  but it is 
all fully automated by scripting and there are no open Telnet ports 
involved. The scripts compile, link, and generate the COBOL85.CBR and 
ODBC.info files (if required), along with a MAKE file and .CBI file for each 
program. Compilation and error lists are returned to a specified directory 
on the local machine, along with the executables.  Compilation is usually 
batches of programs and, because they have been generated, they don't 
require debugging. My Toolset offers local or remote compilation. I use 
remote because I only have COBOL on one machine, and that is not my primary 
development machine.

I would not consider doing development in either the environment just 
described, or the one you described above.

Like the Little Gingerbread Man, I have nothing more to say...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-10-16T20:56:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9TJk.304$ys6.266@newsfe02.iad>`
- **In-Reply-To:** `<6ln8jpFd3c90U1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <6ln4m5Fd51euU1@mid.individual.net> <6ln8jpFd3c90U1@mid.individual.net>`

```
Steve Rainbird wrote:
> 
> 
…[36 more quoted lines elided]…
> 
I perused this thread noting you had been an M/F user, but then ignored 
it because of the word 'TRACE'

Steve,

I perused this thread noting you had been an M/F user switching to F/J 
(probably price ? ), but then ignored it when I saw you use the word 
'TRACE' - 'Oh mainframe stuff, forget it", I said to myself - because I 
have never programmed for a mainframe.

I was outside having a contemplative cigarette on a now dark but 
pleasant evening; I could sit out there without a coat, although I'm 
wearing a sweater. Then a bell rang about the TRACE module in M/F - and 
I'm using Net Express which I assume you were ? I looked at it when I 
first got into N/E but it just didn't do a thing for me; it was 
primarily process flow as far as I can recall. I suspect M/F added Trace 
as a feature to accommodate mainframe dinosaurs like you. That's not an 
insult - I'm 77.

First off I endorse all that Pete writes in this thread and his separate 
"Debugging in General", reference animating. I can understand, that 
based on a programming style which may still be similar to what you 
wrote in the 70's, TRACE may seem the ideal.

However a quote from Richard very recently, paraphrased, "A paragraph 
should only cover one topic/idea". I'll take that even further - A 
paragraph should not be a small essay - if it follows Richard's rule it 
should be able to fit in less than a page, half a page preferably.

To have a PERFORM paragraph

	 	READ-INVENTORY-MAKE-DECISIONS-THEN-WRITE-RECORD

is a recipe for disaster when you are trying to debug regardless of 
tool. As you have been at the game since the 70s, hopefully you are 
coding above as :-

	perform READ-INVENTORY
	perform MAKE-DECISIONS
	perform WRITE-RECORD

As they are distinct topics/paragraphs they are accessible from 
different areas in the program; not always a safe thing to do, but 
hopefully you get the point I'm making. Another better technique, for 
perform READ-INVENTORY have a CALL to a sub-program that handles the 
Inventory File and all file accesses, keeping the sub-program active by 
calling entry point Sections and Exiting the Section; only close 
sub-file and CANCEL sub-program when finished. With some testing, your 
sub-program can be made bullet-proof, rather like invoking proven 
methods in OO. (Apologies if I'm trying to teach my grandmother how to 
suck eggs).

Animators are much more proficient than Tracing. By testing you can get 
a feel for where the error finally occurs and as Pete pointed out, put a 
STOP in the animator on a line and let the program zip through until it 
hits the STOP flag. Having confirmed where it is finally wrong you can 
now set other STOP points further back in the source that you suspect 
led to the error. Yes, you can work forwards with the Animator guessing 
where the error might have started, but depending upon the complexity of 
the code - backtracking on a known error is probably easier.

Jimmy

Pet's tag line :

"I used to write COBOL...now I can do anything."

Perhaps mine should be :

"I used to write COBOL...now I don't."
```

#### ↳ Re: Fujitsu cobol debugging

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-15T16:50:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net>`

```
On Wed, 15 Oct 2008 17:13:30 +0100, "Steve Rainbird"
<steve.nospam.rainbird@mssint.nospam.com> wrote:

>Is there a way of tracing a Fujitsu Cobol program.
>
>In Microfocus I can do SET TRACE and the READY TRACE and it will tell me 
>what paragraphs are being executed.

I worked at three former mainframe shops that wanted trace, but didn't know it was
available on MF. Tens of thousands of paragraphs read:

4790-CALCULATE-SECRET-OVERCHARGE.
    IF  WS-DEBUG-ON
          DISPLAY '4790-CALCULATE-SECRET-OVERCHARGE'
    END-IF.
   ....

Why not use debug lines with D in card column 7? Because they can't recompile on the
production machine. Because they can't change source code to add WITH DEBUGGING MODE, all
source changes must be approved by a committee. Because they cannot recompile at all; only
the Build Team can.
```

##### ↳ ↳ Re: Fujitsu cobol debugging

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-16T01:25:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gd6560$e2n$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>`

```
In article <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>,
Robert  <no@e.mail> wrote:
>On Wed, 15 Oct 2008 17:13:30 +0100, "Steve Rainbird"
><steve.nospam.rainbird@mssint.nospam.com> wrote:
…[14 more quoted lines elided]…
>   ....

END-IF?  One o' them newfangled COBOL '85 constructs, I guess... durned 
kids, can't leave COBOL the way Rear Admiral Hopper intended, gotta go 
makin' it all like Modula-2 'r somethin'.

>
>Why not use debug lines with D in card column 7? Because they can't
>recompile on the
>production machine.

That, actually, is a practise I agree with... such things have covered my 
gluteals.

'Remember that day you left early because you had the flu and were puking 
into the wastebasket so much the Health Department threatened to close us 
down?  Well, the Corner-Office Idiot didn't care that you hadn't signed 
off the code to Test, he wanted it NOW so he had Ops get past the RACF on 
your PDS and move it into Prod... and man, you are in trouble, it was 
throwing all kinds of weird DISPLAYs!'

'Of course it was, I had debugging code in it... any fool who demands that 
source containing debugging lines gets put into Prod gets just what he 
deserves.'

>Because they can't change source code to add WITH
>DEBUGGING MODE, all
>source changes must be approved by a committee.

That I've never seen... 'We want you to change the code but don't change 
it; write your changes in a separate file and the committee will look at 
them.  If they're approved you can implement THOSE CHANGES ONLY... so make 
sure you cover all possibilities the very first time through.'

Somehow I think this mechanism would see - or 'not see', most likely - 
many work-arounds.

>Because they cannot
>recompile at all; only
>the Build Team can.

Pfawgh... a classic 'don't tell *me* I can't do that', a bit of sniffing 
through the JES log will reveal where the compiler lives and then building 
one's own jobstream is a textbook matter.

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-15T22:59:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com>`

```
On Thu, 16 Oct 2008 01:25:20 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>,
>Robert  <no@e.mail> wrote:
…[20 more quoted lines elided]…
>makin' it all like Modula-2 'r somethin'.

Yeahbut, notice the period after it. They made us use END-IF but didn't say anything about
periods. We outsmarted them.

>>Why not use debug lines with D in card column 7? Because they can't
>>recompile on the
…[14 more quoted lines elided]…
>deserves.'

Since there's no compiler in prod, there's no source code in prod either. Executables are
what gets moved to prod, by promoting them within change control. 

>>Because they can't change source code to add WITH
>>DEBUGGING MODE, all
…[5 more quoted lines elided]…
>sure you cover all possibilities the very first time through.'

It's called peer review. It's done using a file compare program, not hilighters on
greenbar like in the Good Old Days. 

I once corrected spelling errors in old comments, was told to revert them. Out of scope.

>Somehow I think this mechanism would see - or 'not see', most likely - 
>many work-arounds.

Process serves one purpose: identify the guilty when things go wrong. If nothing ever went
wrong, they wouldn't need a process. In the case of source code changes, the change
management software knows by who and when each change was made. 

>>Because they cannot
>>recompile at all; only
…[4 more quoted lines elided]…
>one's own jobstream is a textbook matter.

They can compile for Test, by running a makefile given to them. They can't see what
happens during a Production build. For one thing, they don't have permission to read the
Build Team's compiler option file. For another, they don't know the names of prod library
directories, which are not necessarily the same as Test.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-16T12:16:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gd7bbc$bpf$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com>`

```
In article <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 16 Oct 2008 01:25:20 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[26 more quoted lines elided]…
>periods. We outsmarted them.

Those terrible periods/full stops... how *did* anyone get code to work 
in the decades which preceded the 'one per paragraph' Law of Style being 
passed?

As for 'we outsmarted them'... there is no 'we', there is no 'them', there 
is only Getting The Job Done.

>
>>>Why not use debug lines with D in card column 7? Because they can't
…[4 more quoted lines elided]…
>>gluteals.

[snip]

>>'Of course it was, I had debugging code in it... any fool who demands that 
>>source containing debugging lines gets put into Prod gets just what he 
…[4 more quoted lines elided]…
>what gets moved to prod, by promoting them within change control. 

I am not sure how you are using 'in prod' when it comes to source code; 
are you saying that there is no library in which can be found the set of 
statements which were compiled into the current Prod executable?  If so 
then 'change control' is a contradiction in terms.

>
>>>Because they can't change source code to add WITH
…[8 more quoted lines elided]…
>It's called peer review.

This is a different use of the term than the one I was taught.  As I 
recall the way things were done... a user requests a 
modification/enhancement, the request - sometimes refined by a business 
analyst, sometimes not - gets passed on to a programmer, the programmer 
'assumes the position' (feet up on the desk, cuppa mud in one hand, 
smokin'-butt in the other, staring at the acoustic tiles to map out memory 
locations), the Muse descends, the keyboard clatters and code gets 
written.

This code, after satisfying the programmer's testing, is passed on to the 
Test Group where a bunch of folks try - and usually succeed - in breaking 
it; the errors/shortcomings/shoulda-beens are noted and passed back to the 
programmer.  The programmer then 'assumes the position'... et and cetera, 
until the Test Group says 'All right, it does what they meant, not what 
they said'.

*Then* the programmer's 'peers' - in the sense of other programmers, 
usually, as not all of anything turn out to be equal - gather and go over 
the changes, or 'review' the code.

>It's done using a file compare program, not
>hilighters on
>greenbar like in the Good Old Days. 

You had hilighters?  We were lucky to get the pencil-stubs left over from 
the accountants.

>
>I once corrected spelling errors in old comments, was told to revert
>them. Out of scope.

A fellow I know once told me a woman said he was the best lover she had 
ever had; I did not respond with Aristotle's view on what doth not or doth 
a summer make.

>
>>Somehow I think this mechanism would see - or 'not see', most likely - 
>>many work-arounds.
>
>Process serves one purpose: identify the guilty when things go wrong.

Hammers serve one purpose: drive screws when you don't have a screwdriver.

>If
>nothing ever went
>wrong, they wouldn't need a process.

If there were no hypothetical situations this statement would not exist.

>In the case of source code changes,
>the change
>management software knows by who and when each change was made. 

... and the user who requested the change... and the reason that the user 
requested the change... and the source of the reason (company policy, new 
law, change in business practices) for the user's requesting the change...

... if it is done in a moderately complete manner, that is.  The effect on 
a system of a marketer's request for a change to an accounting formula 
might be... amusing, to say the least.

'The columns were all crowded... some figures had four numbers after the 
decimal point, others only two and '00'... so I just told them to 
calculate things to two decimal places to make everything even, what's so 
wrong about that?'

>
>>>Because they cannot
…[7 more quoted lines elided]…
>They can compile for Test, by running a makefile given to them.

The programmers need to have things *given* to them?  Why, there were 
times when disk-space was so expensive we had to code a COBUCLG stream 
from the JOB-card up because we couldn't save anything and they'd thrown 
out the paper-tape drives... ain't there nobody around who can run a 
decompile and read BAL any more?

>They
>can't see what
…[4 more quoted lines elided]…
>directories, which are not necessarily the same as Test. 

A shop where they hire coders who can't hack root, don't know how to 
shoulder-surf and can't figure out how to bribe/blackmail someone in 
Ops... deserves what it gets, I guess.

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 5)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-10-16T13:27:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lotpoFd8o53U2@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com>`

```
In article <gd7bbc$bpf$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com>,
> Robert  <no@e.mail> wrote:

>>happens during a Production build. For one thing, they don't have
>>permission to read the
…[6 more quoted lines elided]…
> Ops... deserves what it gets, I guess.

They are all written on the last page of the boss's desk calendar.  Or at
least that was where I used to find them back in my Univac-1100 COBOL days.
:-)

bill
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:05:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tfief4tbfjjdkh7gc9e90eo4lalr80ih6o@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com>`

```
On Thu, 16 Oct 2008 12:16:44 +0000 (UTC), docdwarf@panix.com () wrote:

>A fellow I know once told me a woman said he was the best lover she had 
>ever had; I did not respond with Aristotle's view on what doth not or doth 
>a summer make.

My wife told me I was a model lover.   Then I looked up "model", and
discovered it was used to describe a cheap plastic imitation of the
real thing.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-17T10:22:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
>
> Hammers serve one purpose: drive screws when you don't have a
> screwdriver.
>

Oh bother. Back when I got started we used a fern.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-17T15:34:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdab9r$3il$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com> <S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com>`

```
In article <S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>
…[4 more quoted lines elided]…
>Oh bother. Back when I got started we used a fern. 

A fern?  Dot's vot de ladies use vhen de vetter gets hot... dey waves in 
frondt of de face a fern, no?

(no wonder dialect humor died)

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-18T10:09:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lsd91Fe14heU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com> <S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com...
> docdwarf@panix.com wrote:
>>
…[5 more quoted lines elided]…
>
OK, can you "translate" this please?

For me, a fern is primitive plant which happens to be the symbol of our 
nation. (The All Blacks, our national Rugby team, wear black jerseys with a 
silver fern on them. (Actually, the fern on the jersey is white, but the 
species it represents is called a "silver fern". It is native to New 
Zealand.))

I know a joke explained is a joke ruined, but I'd really like to understand 
this...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-20T09:59:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZP-dnQ3dSbF6AWHVnZ2dnUVZ_oninZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com> <S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com> <6lsd91Fe14heU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com...
…[18 more quoted lines elided]…
>

"A fern is any one of a group of about 20,000 species of plants classified 
in the phylum or division Pteridophyta..."

Some are better at turning screws. It's a mark of a professional to pick the 
right fern.

It's kinda like picking people. As the former governor (with emphasis on 
'former') of Arizona once said: "Sometimes a Black man is the best man for 
the cotton-pickin' job!"
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-21T10:19:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6m4autFf1d3iU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gd7bbc$bpf$1@reader1.panix.com> <S9idnbiw6s9bMGXVnZ2dnUVZ_sWdnZ2d@earthlink.com> <6lsd91Fe14heU1@mid.individual.net> <ZP-dnQ3dSbF6AWHVnZ2dnUVZ_oninZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:ZP-dnQ3dSbF6AWHVnZ2dnUVZ_oninZ2d@earthlink.com...
> Pete Dashwood wrote:
>> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
…[26 more quoted lines elided]…
>

Ah, I was slow. Thanks.

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:03:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com>`

```
On Wed, 15 Oct 2008 22:59:13 -0500, Robert <no@e.mail> wrote:

>I once corrected spelling errors in old comments, was told to revert them. Out of scope.

Me too.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-17T11:13:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lpsk1Fdeu7eU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com...
> On Wed, 15 Oct 2008 22:59:13 -0500, Robert <no@e.mail> wrote:
>
…[10 more quoted lines elided]…
> - James Madison

I am just staggered by this. The fact that both you and Robert have both 
experienced it shows there are sites (hopefully only in North America; I 
have never encountered such nonsense in Europe or Australasia)  where 
process is more important than common sense.

This reminds me of ISO 9000 or BS 5750  which were/are systems of procedure 
to ensure Quality Control.  Procedures were devised with forms for each 
process which required ticks in boxes and signatures. (In fact, the IT part 
of this was called "TickIt"...) Of course situations arise where the process 
simply can't complete - a key signatory is ill or on holiday or 
unobtainable, or a situation arises that was never foreseen at the time the 
procedure was formulated, so everything grinds to a halt.

The way that sensible companies got round this was to write an emergency 
override process into all key procedures, which allowed the procedure to be 
bypassed with full documentation as to why and how this was necessary. 
Common sense.

What bothers me about people reverting spelling corrections as "out of 
scope" is the "mind set" of such a person. It is a robotic compliance with 
process and procedure, without the exercise of intelligence or common sense. 
Action overriding thought.

I guess that explains a lot about the kind of problems encountered on such 
sites. And the unhappiness of the people who work there.

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-10-17T12:49:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lrfunFdnvmqU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net>`

```
In article <6lpsk1Fdeu7eU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> 
> 
…[19 more quoted lines elided]…
> process is more important than common sense.

I am in the US and I have never encountered this.

> 
> This reminds me of ISO 9000 or BS 5750  which were/are systems of procedure 
> to ensure Quality Control.  

ISO 9000.  Ah yes.  it's all about process, not quality.  Unless it has
been re-written the requirement of ISO 9000 is that the process can be
repeated over and over in exactly the same manner with exactly the same
result.  In other words, if you make bolts and the threads run in the
wrong direction all ISO 9000 requires is that they all come out the same
way.  There is no requirement that the product actually work or even be
of good quality, just consistent.  :-)  How's that for common sense.

bill
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-18T10:41:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lsf55Fdmti0U1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <6lrfunFdnvmqU1@mid.individual.net>`

```


"Bill Gunshannon" <billg999@cs.uofs.edu> wrote in message 
news:6lrfunFdnvmqU1@mid.individual.net...
> In article <6lpsk1Fdeu7eU1@mid.individual.net>,
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
…[24 more quoted lines elided]…
> I am in the US and I have never encountered this.

Pleased to hear it, Bill.

Have you worked on a good number of sites?

>
>>
…[11 more quoted lines elided]…
>

Yes, it amused me at the time. :-)

However, outrageous amounts of money were to be made by being a TickIT 
auditor, as companies scrambled to get accredited, so I did the course and 
jumped on the bandwagon. (Never envy someone who makes more than you do... 
do what he's doing...) The cost of the course was repaid many times over in 
the year or so I did this, but it was deathly boring work and definitely not 
for me.

Pete
```

###### ↳ ↳ ↳ Correcting comments during mainteance (was: Fujitsu cobol debugging

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-10-18T05:55:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TSeKk.56752$jm2.33688@fe08.news.easynews.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <6lrfunFdnvmqU1@mid.individual.net> <6lsf55Fdmti0U1@mid.individual.net>`

```
<previous post snipped>
Concerning "allowing" changes to comments (e.g. correcting spelling) when doing 
maintenance.

It is my experience, that in "large IBM mainframe shops"  it is OFTEN (or at 
least used to be frequently) required that EVERY change in source code when 
doing maintenance needed to be "documented" via the shops "change management" 
procedures.  As an employee (and later when working with user groups), I *never* 
heard of an employee not being allowed to correct internal comments - if they 
included something like "additional editorial corrections to internal 
documentation" when doing their "turn-over" procedures.

HOWEVER, I can imagine (even if I never saw it myself) that the rules for 
"contractors" or "consultants" might have been slightly different.  Not only 
would then need to be able to "explain" every change to source code that they 
did, but they might also be required to "relate it" to something in the original 
contract/specifications.  Again, I never saw this, but can imagine it happening.

I would be interested if any employee (rather than contractor/consultant) in the 
US or anywhere else was told NOT to correct comments while doing maintenance.
```

###### ↳ ↳ ↳ Re: Correcting comments during mainteance (was: Fujitsu cobol debugging

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-18T21:57:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ltmo4Fe4u1eU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <6lrfunFdnvmqU1@mid.individual.net> <6lsf55Fdmti0U1@mid.individual.net> <TSeKk.56752$jm2.33688@fe08.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:TSeKk.56752$jm2.33688@fe08.news.easynews.com...
> <previous post snipped>
> Concerning "allowing" changes to comments (e.g. correcting spelling) when 
…[16 more quoted lines elided]…
> imagine it happening.

I can imagine it happening, but wouldn't want to work in a place where it 
did.

Given that there is a peer review process in place, why would you be 
concerned about monitoring changes to code? If it doesn't work you can roll 
it back; if there is actually malicious intent (and this is every bit as 
likely from a permanent employee as it is from a contractor... maybe even 
more so) peer review should pick it up.

I have worked on sites where the Programme office required all changes to be 
documented, according to the change control procedures implemented in the 
company. It never applied to program code (at the detail level... a document 
would be raised describing the change and where it was applied, the reason 
for it, and who applied it) and certainly not to comments.

Shops that differentiate between contractors and permies are generally not 
good places to work for contractors or permies. Having second class citizens 
in any shop is bad for morale and counter productive.

Making someone explain why they corrected grammar or spelling in the 
comments in what purports to be a "self-documenting" language is just 
stupid. The comments were changed in keeping with the spirit of the 
language. End of Story.

>
> I would be interested if any employee (rather than contractor/consultant) 
> in the US or anywhere else was told NOT to correct comments while doing 
> maintenance.
>

That's NOT the same thing at all. The question is whether they were told to 
revert changes  to comments, having applied them.

I would hope there are no instances.

Pete.
```

###### ↳ ↳ ↳ Re: Correcting comments during mainteance

_(reply depth: 10)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-10-19T07:05:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<__AKk.79616$Mh5.2131@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<6ltmo4Fe4u1eU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <6lrfunFdnvmqU1@mid.individual.net> <6lsf55Fdmti0U1@mid.individual.net> <TSeKk.56752$jm2.33688@fe08.news.easynews.com> <6ltmo4Fe4u1eU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
> news:TSeKk.56752$jm2.33688@fe08.news.easynews.com...
…[12 more quoted lines elided]…
> Pete.

I've only worked in one place for the last 22 years, but I have never 
heard of this practice.  I certainly wouldn't ask any programmer to 
revert changes to comments.  In my own work I have corrected previous 
programmer's comments for spelling, grammar, and content errors.  During 
code walkthroughs we often ask for enhancements or corrections to 
program comments when we think it would improve the product.

As far as I can tell, we treat the work the same way whether the 
programmer is an employee or contractor.  I've worked with several 
contract programmers that I would have liked to see stay on as permanent 
employees, and sometimes their fresh perspective teaches us new 
techniques.
```

###### ↳ ↳ ↳ Re: Correcting comments during mainteance

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-20T03:25:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6m0u9tFehqonU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <6lrfunFdnvmqU1@mid.individual.net> <6lsf55Fdmti0U1@mid.individual.net> <TSeKk.56752$jm2.33688@fe08.news.easynews.com> <6ltmo4Fe4u1eU1@mid.individual.net> <__AKk.79616$Mh5.2131@bgtnsc04-news.ops.worldnet.att.net>`

```


"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:__AKk.79616$Mh5.2131@bgtnsc04-news.ops.worldnet.att.net...
> Pete Dashwood wrote:
>> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
…[16 more quoted lines elided]…
> heard of this practice.

Good :-)


>  I certainly wouldn't ask any programmer to revert changes to comments.

I can't see any sensible manager doing this. That was my point. The worrying 
thing here is the mind set that would make someone WANT to revert 
comments...or think it was so important not to violate process or procedure.

> In my own work I have corrected previous programmer's comments for 
> spelling, grammar, and content errors.  During code walkthroughs we often 
> ask for enhancements or corrections to program comments when we think it 
> would improve the product.

Absolutely. I have rewritten comments in countless programs. (And never been 
told to change them back again..) But I have only done a small amount of 
work on one site in the USA, and it was in the USA that the practise was 
reported. Over the years I have probably worked on at least 50 sites (all 
outside the USA) and I have never seen this.

>
> As far as I can tell, we treat the work the same way whether the 
> programmer is an employee or contractor.

Sounds like a good shop. My experience has been that these are the most 
pleasant places to work. Not just because they treat employees the same and 
focus on the work, but because it is indicative of a right attitude... The 
"mind set" I mentioned earlier.


> I've worked with several contract programmers that I would have liked to 
> see stay on as permanent employees, and sometimes their fresh perspective 
> teaches us new techniques.

It's really nice to hear you say that, Arnold. So often the attitude to 
contractors is a negative one. I've never stopped learning throughout my 
career and sometimes this is a two-way street. Personally, I don't presume 
to teach people (although there have been some occasions where part of my 
job was to train people) but I'm very happy to walk through an approach and 
explain why I chose it, or discuss coding techniques at low level. I've 
certainly never hesitated to help and support colleagues if I could, and 
have been glad of their support on various occasions.

I believe work should be a place we enjoy going to. We certainly spend 
enough of our lives there. The corporate culture and the attitude of 
managers and staff have a big bearing on this.

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-17T13:24:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gda3m0$s2o$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net>`

```
In article <6lpsk1Fdeu7eU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[7 more quoted lines elided]…
>> Me too.

[snip... is there any kind of purpose served in quoting a .sig except when 
responding to it?]

>I am just staggered by this. The fact that both you and Robert have both 
>experienced it shows there are sites (hopefully only in North America; I 
>have never encountered such nonsense in Europe or Australasia)  where 
>process is more important than common sense.

'The two most common elements in the Universe are hydrogen and stupidity', 
or so Harlan Ellison put it... for the record I've been changing comments, 
adding comments, deleting dead code (*** FOR BIGSHOT'S STATISTICAL RUN 29 
OCT 87') and received nothing but hearty thanks for doing such.

One of the reasons for the UseNet is to benefit from the words and 
experiences of others; if I wanted only agreement I would speak with my 
mirror... well... actually, I wouldn't, I avoid them... the psychopath who 
lives in them frightens me.

('Real Programmers comb their hair only when they have... and they don't 
use mirrors, they use the reflection from the CRT.')

[snip]

>What bothers me about people reverting spelling corrections as "out of 
>scope" is the "mind set" of such a person. It is a robotic compliance with 
>process and procedure, without the exercise of intelligence or common sense. 

An organisation attracts and rewards behaviors which it believes to be 
valuable; looking for a buffalo in a bunny-hutch (or a rabbit in a herd of 
bison) might yield scant results.

>Action overriding thought.
>
>I guess that explains a lot about the kind of problems encountered on such 
>sites. And the unhappiness of the people who work there.

I'm not sure about that 'happiness' part, Mr Dashwood... some folks seem 
to be quite satisfied doing the same thing, day in and day out, and get 
upset when things change.  Others, of course, thrive on change and 
challenge.  Let's see... ahhhhh, in 
<http://groups.google.com/group/comp.lang.cobol/msg/f07cd644102d8254?dmode=source> 
I quoted 
<http://groups.google.com/group/comp.lang.cobol/msg/12e0303b6b75284f?dmode=source>

--begin quoted text:

A buddy o' mine used to be Materials/Inventory Manager for a jewelery 
manufacturer... he could never understand folks who considered inertia to 
be valuable, in and of it'sself.  After a meeting where things got a 
bit... heated a VP took him aside and asked, seriously, what the problem 
was... after all, in his (the VP's) department they'd been doing things 
exactly the same way for the past twenty years.

'Where's your passion for work?', asked my buddy, 'Where do you strive to 
do something more, where to you work to make things better?'

'You don't understand', said the VP, 'we've been doing the exact same 
thing for the past twenty years.'

The VP could not understand why anyone would not see this as a Very Good 
Thing.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-18T10:34:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lseo0Fe253dU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <gda3m0$s2o$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:gda3m0$s2o$1@reader1.panix.com...
> In article <6lpsk1Fdeu7eU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[31 more quoted lines elided]…
> use mirrors, they use the reflection from the CRT.')

Real programmers don't have hair... they tore it out years ago. :-)

>
> [snip]
…[8 more quoted lines elided]…
> bison) might yield scant results.

I'm not sure you can blame the organisation for stupidity which is endemic 
to the IT department, although I would agree that Corporate "culture" often 
has a bearing on the shaping of such policies.

>
>>Action overriding thought.
…[6 more quoted lines elided]…
> upset when things change.

Yes, you're right. I tend to discount such people from my considerations. I 
guess I subconsciously shun the existence of them, not wanting to believe 
they exist. (It is bad enough when they are encountered in reality, and 
especially when they hold positions of Authority...)

Of course, people have a right to feel however they feel about change, but 
slavish devotion to process and procedure is something else again. It might 
work in the Russian Army, but it isn't even a good thing for the military. I 
remember a large part of my military training was designed to foster the 
building of initiative in bad situations. The idea was that the Warsaw Pact 
had us (NZ was a contributor to NATO) heavily outgunned and outnumbered, but 
the weakness was that their guys were trained to follow orders without 
thought or question. Once their Officers were dead, they were pretty much 
useless. We, on the other hand were capable of thinking for ourselves and 
assessing situations. (The assessment would probably be to depart the scene 
as quickly as possible...:-) but at least we didn't need to be ordered to 
retreat...)

With 40 years of hindsight, I can see certain flaws in this idea, (there is 
no real evidence that Russian soldiers are any more mindless than anyone 
else, for a start...), but at the time it seemed quite reasonable (like so 
many military ideas do). At least we did get to do interesting exercises 
which did test and strengthen our ability to cope, rather than just marching 
up and down all day.




> Others, of course, thrive on change and
> challenge.  Let's see... ahhhhh, in
…[15 more quoted lines elided]…
>

That's it in a nutshell; the desire for things to be better. The pursuit of 
this goal (and the conflict it inevitably causes) is a major factor in both 
personal and professional growth. When you stop wanting this, you might as 
well stay home in bed.

> 'You don't understand', said the VP, 'we've been doing the exact same
> thing for the past twenty years.'
>
> The VP could not understand why anyone would not see this as a Very Good
> Thing.

Yes, I have encountered such people. I like to pretend they don't exist... 
It makes me feel better... :-)

I'm not sure that the connection between slavish devotion to procedure and 
resistance to change is established, but I do catch your drift.

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-18T01:22:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdbdog$5n0$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <6lpsk1Fdeu7eU1@mid.individual.net> <gda3m0$s2o$1@reader1.panix.com> <6lseo0Fe253dU1@mid.individual.net>`

```
In article <6lseo0Fe253dU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:gda3m0$s2o$1@reader1.panix.com...
>> In article <6lpsk1Fdeu7eU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>> One of the reasons for the UseNet is to benefit from the words and
>> experiences of others; if I wanted only agreement I would speak with my
…[6 more quoted lines elided]…
>Real programmers don't have hair... they tore it out years ago. :-)

Real Programmers don't get ulcers... they give them. (pax General David 
Sarnoff)

>
>>
…[13 more quoted lines elided]…
>has a bearing on the shaping of such policies.

Corporate Culture can be though of as a cancer, perhaps... some are 
localised, some metastsized/systemic.

[snip]

>> I'm not sure about that 'happiness' part, Mr Dashwood... some folks seem
>> to be quite satisfied doing the same thing, day in and day out, and get
>> upset when things change.
>
>Yes, you're right.

Hmmmmm... someone out there should mark a calendar.

>I tend to discount such people from my considerations.

Mr Dashwood, have a care about that... there is only one of you so there's 
more of them than there is of you... and by the rules of Democracy that 
makes *them* 'right'.

>I 
>guess I subconsciously shun the existence of them, not wanting to believe 
>they exist. (It is bad enough when they are encountered in reality, and 
>especially when they hold positions of Authority...)

They are Out There, Mr Dashwood, as we both know... just as there are 
people Out There who seem to understand only physical violence.  One tries 
to live one's life so as to minimise chances for contact with such folks 
but the best laid plans and all that... sometimes you run across one.  In 
such a running-across - whether it is with a person who wants to do Always 
The Same or a person who seems to understand only physical violence - it 
might be of benefit to have already learned how to... communicate with 
them.

>
>Of course, people have a right to feel however they feel about change, but 
>slavish devotion to process and procedure is something else again.

A slavish devotion to New-ness for the Sake of New-ness is yet another 
thing; perhaps it is a Good Idea to slavish devote one'sself to avoid any 
sort of slavish devotion.

[snip]

>With 40 years of hindsight, I can see certain flaws in this idea, (there is 
>no real evidence that Russian soldiers are any more mindless than anyone 
…[3 more quoted lines elided]…
>up and down all day.

What one has to teach a twenty-year-old so that such a youth will, on 
command, run into live machinegun fire might not be the same thing one 
should use to teach a sixty-year-old to do the same thing... if one could, 
at all.  Wasted on the young, aye.

>> Others, of course, thrive on change and
>> challenge.  Let's see... ahhhhh, in
…[22 more quoted lines elided]…
>well stay home in bed.

It would be nice to have a roof over one's head while one did so, Mr 
Dashwood... and maybe a bit of beef, a blot of mustard, a bit of cheese or 
a fragment of underdone potato, as well.  Fortunate, indeed, are those who 
enjoy what earns them their living; the differentiation between Work and 
Play begins to disintergrate.

>
>> 'You don't understand', said the VP, 'we've been doing the exact same
…[6 more quoted lines elided]…
>It makes me feel better... :-)

I'd like to pretend I'm the King of England... but being the King of 
England already there's not much to the game.  As noted above, pretend or 
not, they are Out There and you may have to deal with them.

>
>I'm not sure that the connection between slavish devotion to procedure and 
>resistance to change is established, but I do catch your drift.

Procedure = that which is already being done.

Change = doing that which is not already being done.

'I love change... as long as I don't have to do anything differently.'

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-17T10:40:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <gd6560$e2n$1@reader1.panix.com> <5fcdf45h0i39lncs671m1opu5ck1l5dqpu@4ax.com> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net>`

```
Pete Dashwood wrote:
>> --
>> "In no part of the constitution is more wisdom to be found,
…[3 more quoted lines elided]…
>> - James Madison

Madison was wrong. Article II give the president the unrestricted right to 
wage whatever war he wants against whomever he wants. The Congress only 
"declares" war; it is the president who "wages" war.


>
> I am just staggered by this. The fact that both you and Robert have
…[15 more quoted lines elided]…
> this was necessary. Common sense.

Sometimes common sense prevails. After 9/11, meetings were held by all the 
stakeholders in the air transport industry (regulators like the FAA, 
airlines, passenger advocates, law enforcement, etc.) with a view toward 
developing a set of standard responses should a similar event occur in the 
future.

After months of negotiations and meetings a decision was finally agreed to 
by all.

Do nothing.

Should something like that happen again, let the people involved with the 
situation make ad hoc decisions. Immediately. On the spot. Here's an actual 
example of a decision made on 9-11:

FAA Assistant Director: "How many flights aloft over CONUS (continental 
United States), real-world?
Worker: "About forty-eight hundred."
FAA guy: "Okay. This shit stops right now. I want ATC-Zero (all planes 
grounded) nationwide, and I want it now."

No one asked it he had the authority to order such a drastic action (he 
didn't). No one asked how we could divert several hundred incoming 
international flights to Canada or Hawaii. The workers just got busy doing 
their best.

>
> What bothers me about people reverting spelling corrections as "out of
…[6 more quoted lines elided]…
>

It's a guy thing.

Men are genetically programmed to be process oriented. Organizations that 
are predominately male have uniforms, funny hats (Shriners), a 
chain-of-command, regalia, ceremony, status, etc. The "process" is more 
important than the results. Witness memos announcing a pre-planning meeting 
for the re-organization seminar (sometimes there's a pre-pre-planning 
meeting).

In my view, the whole problem in the Middle East is that the "Peace Process" 
is an end in itself. The "middle east problem" could probably be rectified 
in one afternoon by a bunch of women getting together over coffee (after 
complaining about their husbands).
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-17T16:13:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdadk2$7vv$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com>`

```
In article <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Pete Dashwood wrote:
>>> --
…[6 more quoted lines elided]…
>Madison was wrong.

Yeah, what did Madison know... after all, he represented Virginia at the 
Continental Congress, was a figure of note at the Constitutional 
Convention, helped frame the Bill of Rights and was elected President.

>Article II give the president the unrestricted right to 
>wage whatever war he wants against whomever he wants. The Congress only 
>"declares" war; it is the president who "wages" war.

A declaration (http://www.merriam-webster.com/dictionary/declare , 1) 
makes known formally, officially or explicitly; it answers the question of 
'is there a war?'.  While the President may engage in or carry out 
(http://www.merriam-webster.com/dictionary/wage[2] , 1) the war one might 
have difficulty carrying out or engaging in an activity which does not 
exist... and, Constitutionally speaking, the existence of war depends on 
Congressional declaration.

At least... that's the way the Constitution and the English language have 
been used for a few centuries; perhaps I wasn't on the mailing-list to be 
notified of the change.

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 8)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-20T10:05:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[29 more quoted lines elided]…
>

I'm sure the people in Iraq, Afghanistan, Serbia, Albania, Sudan, Haiti, 
Somalia, and Bosnia, who all experienced Bill Clinton's "war" activities, 
would disagree. I suppose the more pedantic phraseology would be "engaged in 
activities which, if declared, would be considered "war."
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-20T10:30:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bcpf4t647ape7c2sg8t51vl7rki1qjq5a@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <gdief49m3ct2umelsjme6l88f26e9hjp52@4ax.com> <6lpsk1Fdeu7eU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com>`

```
On Mon, 20 Oct 2008 10:05:33 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>> At least... that's the way the Constitution and the English language
>> have been used for a few centuries; perhaps I wasn't on the
…[6 more quoted lines elided]…
>activities which, if declared, would be considered "war." 

Sure.   When the powerful do not wish to have their power limited by
the Constitution, they are facile in redefining what it says.
Sometimes they get away with it.   Pedantic phraseology allowed these
presidents to wage "police actions", without amending the Constitution
to allow them to declare these to be wars.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-20T16:37:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdic45$922$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com>`

```
In article <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com>,
…[34 more quoted lines elided]…
>would disagree.

I barely know what *I* agree with, let alone anyone else... when folks 
from Iraq, Afghanistan, Serbia, etc. begin posting their disagreements 
I'll have something to discuss with them.

>I suppose the more pedantic phraseology would be "engaged in 
>activities which, if declared, would be considered "war." 

I suppose that the Constitution, clearly and unambiguously, states in 
Section I, Article 8, that:

--begin quotes text:

The Congress shall have power... To declare war, grant letters of marque 
and reprisal, and make rules concerning captures on land and water;

--end quoted text

The Constitution, as noted in Article VI, states:

--begin quoted text

This Constitution, and the laws of the United States which shall be made 
in pursuance thereof; and all treaties made, or which shall be made, under 
the authority of the United States, shall be the supreme law of the land;

--end quoted text

... and as such is Law.  Law requires careful reading, re-reading, 
consideration, discussion, re-discussion and re-evaluation; if doing such 
requires that one be 'a formalist or precisionist in teaching' 
( http://www.merriam-webster.com/dictionary/pedant ) then being a pedant 
might seem to be appropriate.

(note - while the President has (Art.II, Sec 2) 'power, by and with the 
advice and consent of the Senate, to make treaties' a treaty is, by 
definition (http://www.merriam-webster.com/dictionary/treaty) 'a contract 
in writing between two or more political authorities (as states or 
sovereigns) formally signed by representatives duly authorized and usually 
ratified by the lawmaking authority of the state' it would be interesting 
to see who served as 'political authority' besides the United States.  A 
treaty with only one signatory seems to be as much of a treaty as a sale 
with only one party is a sale... it takes at least two to treatise.)

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 10)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-20T14:31:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
>>>
>>>> Article II give the president the unrestricted right to
…[66 more quoted lines elided]…
>

You skipped the germane part of Article II Section 2: "The president shall 
be the Commander of Chief of the Army and Navy of the United States, and of 
the Militia of the several States, when called into the actual Service of 
the United States..."

To translate this into common-speak, the president can order the armies to 
march to and fro and kill anybody they meet. This power is absolute and 
cannot be gainsaid by the Congress or the courts.

But, one can't call it a "war" unless the Congress has so blessed the 
action.

As one opinion by a court of appeals held: "... if the president's actions 
do not agree with the will of the citizenry, they are at liberty to replace 
him at the next election."
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-20T14:50:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>`

```
On Mon, 20 Oct 2008 14:31:41 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>To translate this into common-speak, the president can order the armies to 
>march to and fro and kill anybody they meet. This power is absolute and 
…[3 more quoted lines elided]…
>action.

Do you believe that was the intention of the founders such as Madison?
```

###### ↳ ↳ ↳ OT - Constituion and Was (waws: Fujitsu cobol debugging

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-10-20T23:23:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ip8Lk.103083$sg2.31404@fe09.news.easynews.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com>`

```
As far as "intent" goes.  As I recall, the writers of the constitution weren't 
"planning" on there being a standing army.  Therefore, it is hard for me to 
"guess" that they were expecting the president to be able to do much with the 
non-existing group of soldiers - when the congress had NOT made a formal 
declaration of war.
```

###### ↳ ↳ ↳ Re: OT - Constituion and Was (waws: Fujitsu cobol debugging

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-10-20T17:28:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fu8Lk.34198$SH5.32689@newsfe08.iad>`
- **In-Reply-To:** `<Ip8Lk.103083$sg2.31404@fe09.news.easynews.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com> <Ip8Lk.103083$sg2.31404@fe09.news.easynews.com>`

```
William M. Klein wrote:
> As far as "intent" goes.  As I recall, the writers of the constitution weren't 
> "planning" on there being a standing army.  Therefore, it is hard for me to 
…[3 more quoted lines elided]…
> 
Wouldn't normally bother with this stuff, but as it was one from you......

Bit like J4/PL22.4 - go to great lengths to revamp Collection concepts, 
subsequently put out the TR  - AND didn't initially ask if anybody would 
actually use their version of collections :-)

Jimmy
```

###### ↳ ↳ ↳ Re: OT - Constituion and Was (waws: Fujitsu cobol debugging

_(reply depth: 13)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2008-10-21T02:50:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<prbLk.3889$x%.1357@nlpi070.nbdc.sbc.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com> <Ip8Lk.103083$sg2.31404@fe09.news.easynews.com>`

```
In article <Ip8Lk.103083$sg2.31404@fe09.news.easynews.com>, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
>As far as "intent" goes.  As I recall, the writers of the constitution weren't 
>"planning" on there being a standing army.  

That position is pretty hard to justify, considering that the Constitution 
explicitly grants Congress the power to fund and maintain an army and a navy, 
and explicitly designates the President as Commander-in-Chief thereof. Hard to 
imagine that the framers didn't expect the Congress and the President to 
exercise those powers...
```

###### ↳ ↳ ↳ Re: OT - Constituion and Was (waws: Fujitsu cobol debugging

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-10-21T05:53:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u7eLk.108592$ZW7.96979@fe10.news.easynews.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com> <Ip8Lk.103083$sg2.31404@fe09.news.easynews.com> <prbLk.3889$x%.1357@nlpi070.nbdc.sbc.com>`

```
Hard to deal with exact intent, but, for example, from:
   http://etext.virginia.edu/jefferson/quotations/jeff1480.htm

"I do not like [in the new Federal Constitution] the omission of a Bill of 
Rights providing clearly and without the aid of sophisms for... protection 
against standing armies." --Thomas Jefferson to James Madison, 1787. ME 6:387

among other quotes.
```

###### ↳ ↳ ↳ Re: OT - Constituion and Was (waws: Fujitsu cobol debugging

_(reply depth: 14)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-21T14:14:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<io2dnVzNw_6Zt2PVnZ2dnUVZ_qDinZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com> <Ip8Lk.103083$sg2.31404@fe09.news.easynews.com> <prbLk.3889$x%.1357@nlpi070.nbdc.sbc.com>`

```
Doug Miller wrote:
>
> That position is pretty hard to justify, considering that the
…[7 more quoted lines elided]…
> exercise those powers...

Yes. It is often said that Congress, by controlling the purse-strings, can 
act as a brake on the President. Yet...

When Teddy Roosevelt proposed sending the US Navy on an around-the-world 
tour to demonstrate the power of the United States, Congress balked at 
appropriating the money.

Roosevelt said: "I have enough money to send them HALF WAY around the world. 
Let's see if Congress can find the money to get them back!"
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 12)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-21T14:11:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cd-dncQPwb3KtGPVnZ2dnUVZ_szinZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <H9CdnV426atyLGXVnZ2dnUVZ_rbinZ2d@earthlink.com> <gdadk2$7vv$1@reader1.panix.com> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <hnrpf4htlnbspudn639jo79tqn6vtq4st0@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 20 Oct 2008 14:31:41 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[8 more quoted lines elided]…
> Do you believe that was the intention of the founders such as Madison?

Certainly. The notion is scattered throughout the Federalist Papers, some 
even written by Madison.

And, it makes sense. You can't have a war run by committee. Even the Roman 
Senate knew that.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-21T01:15:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdjafn$9i7$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>`

```
In article <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>>>
>>>>> Article II give the president the unrestricted right to
>>>>> wage whatever war he wants against whomever he wants. The Congress
>>>>> only "declares" war; it is the president who "wages" war.

[snip]

>You skipped the germane part of Article II Section 2: "The president shall 
>be the Commander of Chief of the Army and Navy of the United States, and of 
…[8 more quoted lines elided]…
>action.

That the President is Commander in Chief was never questioned... what this 
status can be interpreted as, howerver, in the absence of a Declaration of 
War (solely the province of Congress, as per Article I), is another 
matter, entire.

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 12)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-21T14:15:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1eCdnQFhl6XAt2PVnZ2dnUVZ_hSdnZ2d@earthlink.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <3_KdnTP4QJWjA2HVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdic45$922$1@reader1.panix.com> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdjafn$9i7$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[25 more quoted lines elided]…
>

Maybe so. But it's never been a problem. The president marches his armies to 
and fro at will. Congress never has stopped him - and probably never will 
try.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-22T02:02:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdm1jr$jjh$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com> <gdjafn$9i7$1@reader1.panix.com> <1eCdnQFhl6XAt2PVnZ2dnUVZ_hSdnZ2d@earthlink.com>`

```
In article <1eCdnQFhl6XAt2PVnZ2dnUVZ_hSdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <J4CdneY4Qt4AQWHVnZ2dnUVZ_g2dnZ2d@earthlink.com>,
…[28 more quoted lines elided]…
>Maybe so.

No 'maybe' about it, according to the black-letter law.  Congress declares 
war, the President wages it.

>But it's never been a problem.

That you are aware of.  In the annals of politics there have been quite a 
few 'Well, all right... I won't (x) if you'll (y)'.

DD
```

##### ↳ ↳ Re: Fujitsu cobol debugging

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:00:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kshef417opmge4bt1mup347rdkoblq5la0@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>`

```
On Wed, 15 Oct 2008 16:50:56 -0500, Robert <no@e.mail> wrote:

>I worked at three former mainframe shops that wanted trace, but didn't know it was
>available on MF. Tens of thousands of paragraphs read:
…[4 more quoted lines elided]…
>    END-IF.

Alternatively, we have old code with exit paragraphs converted to:

 SOURCE-COMPUTER.                               
**            IBM-390 WITH DEBUGGING MODE.     
               IBM-390.                          
     ...

 1234-MY-PARAGRAPH.
D      MOVE '1234-MY-PARAGRAPH    TO PARAGRAPH-NAME.
       ...

 1234-END-OF-PARAGRAPH.
       CONTINUE.
D     DISPLAY PARAGRAPH-NAME.

This way we can have the displays ready with quickly with a compile
change.

I dislike EXIT paragraphs, but most of our programmers use the
programming styles that I started off with in the 1960s, even though
they started off later.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:15:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41jef49mgd0hpchhnifdihnrr6nqdfu543@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <kshef417opmge4bt1mup347rdkoblq5la0@4ax.com>`

```
On Thu, 16 Oct 2008 08:00:06 -0600, Howard Brazee <howard@brazee.net>
wrote:

>MOVE '1234-MY-PARAGRAPH    TO PARAGRAPH-NAME.

An advantage to this, is that populating PARAGRAPH-NAME can be done
within a called paragraph and checked later.
```

###### ↳ ↳ ↳ Debugging in general WAS: Re: Fujitsu cobol debugging

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-17T12:14:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lq06nFdmh7dU1@mid.individual.net>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <kshef417opmge4bt1mup347rdkoblq5la0@4ax.com> <41jef49mgd0hpchhnifdihnrr6nqdfu543@4ax.com>`

```

```

##### ↳ ↳ Re: Fujitsu cobol debugging

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:02:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com>`

```
On Wed, 15 Oct 2008 16:50:56 -0500, Robert <no@e.mail> wrote:

>Why not use debug lines with D in card column 7? Because they can't recompile on the
>production machine. Because they can't change source code to add WITH DEBUGGING MODE, all
>source changes must be approved by a committee. Because they cannot recompile at all; only
>the Build Team can.

But they can compile with READY TRACE on the production machine?
Debugging commands are for debugging, not production.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-16T14:11:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gd7i32$eah$1@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com>`

```
In article <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 15 Oct 2008 16:50:56 -0500, Robert <no@e.mail> wrote:

[snip]

>But they can compile with READY TRACE on the production machine?

It might be a good idea to check the compiler manual first. For example:

From 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/8.1.9?SHELF=&DT=20020920180651&CASE=&FS=TRUE>

--begin quoted text:

The READY or RESET TRACE statement can appear only in the Procedure 
Division, but has no effect on your program. 

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T08:40:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hdkef49uk902si7ej67lfaubel5rjlkdis@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com> <gd7i32$eah$1@reader1.panix.com>`

```
On Thu, 16 Oct 2008 14:11:46 +0000 (UTC), docdwarf@panix.com () wrote:

>>But they can compile with READY TRACE on the production machine?
>
…[8 more quoted lines elided]…
>Division, but has no effect on your program. 

I misunderstood - I thought that it was Fujitsu that had READY TRACE,
and we were telling how we got around not having it anymore on CoBOL
compilers for Z-OS.     I was sorrier to see EXHIBIT NAMED CHANGED go
away than READY TRACE though.
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-16T15:02:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gd7l2o$lag$2@reader1.panix.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com> <gd7i32$eah$1@reader1.panix.com> <hdkef49uk902si7ej67lfaubel5rjlkdis@4ax.com>`

```
In article <hdkef49uk902si7ej67lfaubel5rjlkdis@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 16 Oct 2008 14:11:46 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[14 more quoted lines elided]…
>compilers for Z-OS.

You think that's a good'un?  I was talking about constructing COBUCLG jobs 
and Mr Wagner was saying something about makefiles... there is largeness, 
it contains multitudes!

DD
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-16T10:21:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dqmef4pgcjnb6000uue46tsl2jvgcl8iup@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com>`

```
On Thu, 16 Oct 2008 08:02:36 -0600, Howard Brazee <howard@brazee.net> wrote:

>On Wed, 15 Oct 2008 16:50:56 -0500, Robert <no@e.mail> wrote:
>
…[6 more quoted lines elided]…
>Debugging commands are for debugging, not production.

They turn on debug externally, with an environment variable. If using TRACE, they could
say:

IF  WS-DEBUG-ON
    READY TRACE
END-IF
```

###### ↳ ↳ ↳ Re: Fujitsu cobol debugging

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-16T09:51:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jloef4l7d3jffiffh3v97m8ggb0qpkt7mm@4ax.com>`
- **References:** `<6lmj5cFd4rklU1@mid.individual.net> <uoocf4p95n7mg26498etdmnj6or5foupdc@4ax.com> <l9ief4lcc7iaptrocp4ev45rk4iepf6480@4ax.com> <dqmef4pgcjnb6000uue46tsl2jvgcl8iup@4ax.com>`

```
On Thu, 16 Oct 2008 10:21:32 -0500, Robert <no@e.mail> wrote:

>They turn on debug externally, with an environment variable. If using TRACE, they could
>say:
…[3 more quoted lines elided]…
>END-IF


Ahh, then they can also use it for other debugging techniques.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
