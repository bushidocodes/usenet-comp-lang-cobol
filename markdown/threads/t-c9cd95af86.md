[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call a .BAT file?

_33 messages · 8 participants · 2009-03_

---

### Call a .BAT file?

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-03-11T23:00:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net>`

```
I want to have my program execute a .BAT file, then continue to process. 
Call and cancel doesn't work.  I'm using an old version of MicroFocus COBOL. 
Is there a method to accomplish this?  TIA, Paul
```

#### ↳ Re: Call a .BAT file?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-13T01:37:44+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71se0pFmonffU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net>`

```
Paul H wrote:
> I want to have my program execute a .BAT file, then continue to
> process. Call and cancel doesn't work.  I'm using an old version of
> MicroFocus COBOL. Is there a method to accomplish this?  TIA, Paul

You can get your COBOL program to execute ANY executable (including a .BAT 
file) by using the Windows Shell API. It is exactly the same as running a 
DOS command.

You need the ShellExecute  or WinExec commands of the Windows API. If you 
are running an old (16 bit) compiler it is in a .dll called "shell.dll", if 
you are running something better than windows 95 it is in a .dll called 
"shell32.dll"

Here's a link to sample code:

http://supportline.microfocus.com/examplesandutilities/nesamp.asp#Win32API

If you substitute your .Bat filename into the WinExec sample, where it says 
"Notepad.exe"  you should be OK.

WinExec is fine to kick off something simple, but you should really use the 
ShellExecuteEX if you are going to handle documents.

Check out both these samples for future reference.

(BTW, .bat files are really obsolete and best avoided. These days it is .wsh 
(Windows Script Hosting), which has much richer functionality,  is closer to 
the system, and much more stable. You can do much more than was ever 
possible with .bat files. Depending on what you want your batch file to do, 
you should consider writing it in WSH or VBScript. (You can also use 
JavaScript or C# if you want to get really sexy :-))

HTH,

Pete
```

##### ↳ ↳ Re: Call a .BAT file?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-12T08:36:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:71se0pFmonffU1@mid.individual.net...
> (BTW, .bat files are really obsolete and best avoided. These days it is 
> .wsh (Windows Script Hosting), which has much richer functionality...

I have too often seen *.bat or *.cmd files shelled to do things like copy a 
file or start another executable, best guess is because it's 'easier' to 
shell out than to use the instrinc functions provided in the language.

Copy =   OPEN INPUT, OPEN OUTPUT, READ, WRITE, CLOSE , CLOSE   (that's 
really tough, huh?)

Start program=   operating system dependent, but CALL, DOS_EXEC and 
CreateProcess come to mind.

I really have a low tolerance for people who use *.bat or *.cmd or even WSH 
to do things which can be done in the current language just because it's 
easier.

There is no elevator to success; there are only stairs.

MCM
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T13:47:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb3pr$dsj$2@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>`

```
In article <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:

[snip]

>I really have a low tolerance for people who use *.bat or *.cmd or even WSH 
>to do things which can be done in the current language just because it's 
>easier.

Is your tolerance higher for those who re-invent wheels?

>
>There is no elevator to success; there are only stairs.

Compare and contrast this with '... and then the Muse descended on me and 
all of a sudden it became clear'.

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-12T08:59:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <gpb3pr$dsj$2@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:gpb3pr$dsj$2@reader1.panix.com...
> In article <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[8 more quoted lines elided]…
> Is your tolerance higher for those who re-invent wheels?

Well, yes.

I spend most of my "newsgroup time" in a BASIC-language group (I haven't 
written a line of COBOL since 2001), and many of the programmers there are 
new and inexperienced.. not to mention young and immature.

If that particular programmer has not yet written his own "file copy"  or 
"launch another program"  routine  which he can re-use in future 
applications, I think it's time he or she DID re-invent that wheel, rather 
than write and call/invoke/shell a batch or command file.

Unless I infer too much, most of the COBOL programmers who frequent this 
group have been around for a while.. we HAVE already invented our wheels and 
CAN and DO re-use them.

MCM
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T14:09:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb52t$dsj$5@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <gpb3pr$dsj$2@reader1.panix.com> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com>`

```
In article <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:gpb3pr$dsj$2@reader1.panix.com...
>> In article <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>,
…[11 more quoted lines elided]…
>Well, yes.

A honest answer, then.

[snip]

>Unless I infer too much, most of the COBOL programmers who frequent this 
>group have been around for a while.. we HAVE already invented our wheels and 
>CAN and DO re-use them.

I cannot speak for others, of course... but one of the first things I was 
taught when learning COBOL was 'When something is wanted, look around for 
something else similar, copy it and do global-replaces.'

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-12T09:45:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <gpb3pr$dsj$2@reader1.panix.com> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:gpb52t$dsj$5@reader1.panix.com...
> In article <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[7 more quoted lines elided]…
> something else similar, copy it and do global-replaces.'


I guess I was "lucky" enough no one ever told me that... and the few times I 
tried that on my own, the "something similar" was invariably "buggy"  so I 
had to rewrite it anyway. (yes, it *WAS* re-useable happily ever after, 
thank you).

Besides, what do the 'newbies' learn from "search and replace?"

Answer: they learn how to search and replace.  We'd all have much better 
software if we forced the new people to actually THINK when they do a job.

MCM
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T15:20:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb980$hal$1@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com>`

```
In article <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:gpb52t$dsj$5@reader1.panix.com...
>> In article <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com>,
…[13 more quoted lines elided]…
>thank you).

So... you got three learning experiences for the price of one, how to 
search for what you want, to test what you found for bugs and then to 
write something new using the knowledge you had gained from the previous 
exercise.

('Whoops, better not do that... last time it went into a loop and Ops 
called me nasty names!')

>
>Besides, what do the 'newbies' learn from "search and replace?"

The skills of research and the discipline to evaluate what they have 
found.  I think it was Einstein who said 'Why should I remember how many 
feet are in a mile when I know where to look it up?'... argumentum ad 
vericundiam, I know, but ol' Albert ain't a half-bad example to follow, 
for some things.

>
>Answer: they learn how to search and replace.

If that is all they learn then the sooner they become Managers the 
better... and leave the programming to the programmers.

>We'd all have much better 
>software if we forced the new people to actually THINK when they do a job.

Some folks manage to see farther because they can stand on the shoulders 
of giants... others suffer from acrophobia.

I don't know why but I am reminded of a story I heard in a radio interview 
with Les Paul, may he sleep with the angels.  He said that he grew up 
surrounded by music; his mother had a radio, a grammaphone, a player piano 
and various other devices.

When he was about... five years old he said he noticed something.  The 
player piano had something in it that went around and around; if he put 
his hand on the wheel the music would slow down but it would 'sound mostly 
the same' (a five-year-old's way of saying 'maintained constant pitch').  
The grammaphone had something that went around and around and made music, 
too - Genuine Titanium Needles, Never Need Replacing! - but when he put 
his hand on the roundy-going thing the music would slow down... and sound 
*different* (a five-year-old's way of saying 'showed a decrease in 
pitch').

So... here you have two things that make music, both have 
roundie-go-rounds... but it you put your hand on one *this* happens and 
you put your hand on the other *this* AND *that* happens.

Some five-year-olds would be satisfied with being able to change the 
phenomenon, some might think it worthy of a 'golly, that's keen!'... Les 
Paul said he sat and looked and thought and thought... and all he could 
come up with was 'WHY?'

What he did after that, of course, was change the way music was made and 
heard... but he started with the works of others.  Similarly, with the 
writing of code: first you learn to define your programming problem, then 
you learn how to research how others have approached that programming 
problem, then you learn to adapt their solutions to your particular 
variant of that programming problem...

... *then* you start writing code... and if you're lucky you get to look 
back on routines you wrote a few decades back and say 'Who wrote this 
junk?'

DD
```

###### ↳ ↳ ↳ IT Training - was Re: Call a .BAT file?

_(reply depth: 8)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-12T11:24:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dHaul.22432$eT1.20608@newsfe20.iad>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <gpb980$hal$1@reader1.panix.com>`

```
I think this is worth another thread to find out whether Doc's experience is
the norm these days.

I say "these days" because, having been around a long time, I can state with
confidence that I/T training consisted of learning the elements of a
language, solving a few homework problems and maybe programming a lab
problem (which to my vexation proved that my hand calculations were
incorrect), and then being thrown out into the world.  Learning on the job
followed - and lucky the person who didn't make ghastly, expensive mistakes
which were only tolerated because employers didn't have much choice then.
After a while it became obvious that one must PLAN a program instead of
battering out code and beating it into shape by testing.  Only after
considerable further time did one's ego become secure enough to realize that
other programmers had good, useable ideas.  And only some time after that
did one get into the habit of actively looking for code to use.  (I alway
tried to get my staff to document their one-off "mickey mouse" programs in
the confidence that they'd be useful again).

Doc's program as laid out makes perfect sense - although language elements
would have to come into it fairly early - but I am skeptical that it is done
that way, even thse days.

Any comments?

PL


<docdwarf@panix.com> wrote in message news:gpb980$hal$1@reader1.panix.com...
> In article <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com>,
> What he did after that, of course, was change the way music was made and
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IT Training - was Re: Call a .BAT file?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T18:35:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpbkli$g35$2@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <gpb980$hal$1@reader1.panix.com> <dHaul.22432$eT1.20608@newsfe20.iad>`

```
In article <dHaul.22432$eT1.20608@newsfe20.iad>, tlmfru <lacey@mts.net> wrote:
>I think this is worth another thread to find out whether Doc's experience is
>the norm these days.

No need to do that, Mr Lacy... it's been remarked by many that there's 
little about me - experience included - that has been called 'the norm'.

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file? - Einstein extract

_(reply depth: 8)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-12T11:26:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WJaul.22434$eT1.4938@newsfe20.iad>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <gpb980$hal$1@reader1.panix.com>`

```

----- Original Message -----
From: <docdwarf@panix.com>
> The skills of research and the discipline to evaluate what they have
> found.  I think it was Einstein who said 'Why should I remember how many
…[3 more quoted lines elided]…
>

I forget the exact details, but there is also the story of Albert and the
paperclip.  I don't know if this is apocryphal.

He and a colleague were working on something and needed to keep some papers
together.  They couldn't find a paperclip so Einstein started twisting some
miscellaneous bit of wire into the approximate shape required.  His
colleague by that time had actually found the clips - so Einstein grabbed
one and started twisting it into the appropriate shape!  He later admitted
that once he got well into doing something it was hard for him to stop and
regroup.

A lot of the maxims about Einstein seem to me to be based on infrequent,
momentary aberrations of the sort we all commit.from time to time.
Interesting, though.

PL
```

###### ↳ ↳ ↳ Re: Call a .BAT file? - Einstein extract

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-12T11:52:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rriir4ppsbriggffkn7r3g4h9cc89pesgs@4ax.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <gpb980$hal$1@reader1.panix.com> <WJaul.22434$eT1.4938@newsfe20.iad>`

```
On Thu, 12 Mar 2009 11:26:56 -0600, "tlmfru" <lacey@mts.net> wrote:

>He and a colleague were working on something and needed to keep some papers
>together.  They couldn't find a paperclip so Einstein started twisting some
…[4 more quoted lines elided]…
>regroup.

I guess I've seen that - and probably done that.

I also like the story in _Zen and the Art of Motorcycle Maintenance_
where the author cut up a can to make a shim for a handlebar of a BMW.
The owner appeared to very much prefer to buy a German made shim that
would work no better than have a piece of a can in his machine.
```

###### ↳ ↳ ↳ Re: Call a .BAT file? - Einstein extract

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-13T13:18:18+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tn2bFn43nfU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <gpb980$hal$1@reader1.panix.com> <WJaul.22434$eT1.4938@newsfe20.iad>`

```
tlmfru wrote:
> ----- Original Message -----
> From: <docdwarf@panix.com>
…[20 more quoted lines elided]…
> to time. Interesting, though.

Thanks Peter, your post gives me hope... :-)

I had reason to believe the seal on my refrigerator might be faulty. I 
checked it out and it looked to be fine, but I still had this gnawing doubt.

How could I make sure it was a tight seal?

Then I had this brilliant idea...

If I put the room in total darkness, closed the fridge, and could still see 
chinks of light, then the seal must be compromised....

It took me a full five seconds to realise the flaw in this logic... :-)

Fortunately, it turns out the seal was perfect and I had nothing to worry 
about (at least, as far as the refrigerator is concerned; the state of my 
mental capacity could be an entirely different source of worry...:-))

Knowing that Albert Einstein was subject to similar aberrations is very 
reassuring... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-12T11:48:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dliir497741913q1gvhf352ifalnokclql@4ax.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <gpb3pr$dsj$2@reader1.panix.com> <cz8ul.22088$Ws1.19846@nlpi064.nbdc.sbc.com> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com>`

```
On Thu, 12 Mar 2009 09:45:15 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>Besides, what do the 'newbies' learn from "search and replace?"
>
>Answer: they learn how to search and replace.  We'd all have much better 
>software if we forced the new people to actually THINK when they do a job.

And they also learn to analyze, research, & test.    Since coding is
the smallest & easiest part of programming, I don't find this to be a
poor strategy.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T18:44:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpbl5m$g35$3@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <gpb52t$dsj$5@reader1.panix.com> <ae9ul.1880$im1.646@nlpi061.nbdc.sbc.com> <dliir497741913q1gvhf352ifalnokclql@4ax.com>`

```
In article <dliir497741913q1gvhf352ifalnokclql@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 12 Mar 2009 09:45:15 -0500, "Michael Mattias"
><mmattias@talsystems.com> wrote:
…[8 more quoted lines elided]…
>poor strategy.

From 
<http://groups.google.com/group/comp.software.year-2000/msg/1bb65f9ecc90567c?dmode=source>

--begin quoted text:

First you are learnen to scharfen der knife, *den* you are learnen to 
cutten der vood.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-12T11:46:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uhiir4h3ea0hiclr8k4v4de2imfo5umlsh@4ax.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>`

```
On Thu, 12 Mar 2009 08:36:03 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>I really have a low tolerance for people who use *.bat or *.cmd or even WSH 
>to do things which can be done in the current language just because it's 
>easier.

There are advantages in calling external working programs, whether
they are .bat, *.cmd or SQL.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-13T13:06:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tmc0Fn6i3nU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com>`

```
Michael Mattias wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:71se0pFmonffU1@mid.individual.net...
…[16 more quoted lines elided]…
> because it's easier.

I take your point.

I was faced with exactly this recently in a C# program. It would have been 
very easy to "Shell out" and run Xcopy to copy a number of files from a 
remote directory to a local one. Instead I used the intrinsic functionality 
of .NET's "File" class and was able to check for existence as well as a few 
other thngs before doing the actual transfer.

I do use WSH where it makes sense, but I would rather not, and if the 
language can accommodate what I'm trying to do then I would always go that 
route in preference.
>
> There is no elevator to success; there are only stairs.

Er...sometimes there's an escalator... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-13T07:35:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:71tmc0Fn6i3nU1@mid.individual.net...
> Michael Mattias wrote:
>> There is no elevator to success; there are only stairs.
>
> Er...sometimes there's an escalator... :-)

From Kiwi to paradigm American youth.... always looking for the easy way?


MCM
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-13T13:03:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpdlj1$g36$3@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>`

```
In article <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
>news:71tmc0Fn6i3nU1@mid.individual.net...
…[5 more quoted lines elided]…
>From Kiwi to paradigm American youth.... always looking for the easy way?

As the Italians used to say, 'Warum einfach machen wann Mann kann 
kompliziert?'

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-14T11:56:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7206l1FmsavuU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com> <gpdlj1$g36$3@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[11 more quoted lines elided]…
> kompliziert?'

[for the benefit of non-German speakers: "Why make things simple, when you 
can complicate them."]

I get irritated when I hear someone (usually a Manager) using the acroynm 
"KISS" (Keep It Simple, Stupid) to rally the troops.

I was in a meeting once where someone trotted out this old chestnut and I 
said: "Yes, we need a solution that you can understand." he never realized I 
was using "you" to mean him, and the irony was lost, but it made me feel 
better anyway... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-03-13T18:05:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0cb4a5d6-68a1-4234-bd1f-3207ba6f0934@e36g2000prg.googlegroups.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com> <gpdlj1$g36$3@reader1.panix.com> <7206l1FmsavuU1@mid.individual.net>`

```
On Mar 14, 11:56 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <GJsul.22159$Ws1.5...@nlpi064.nbdc.sbc.com>,
…[23 more quoted lines elided]…
> better anyway... :-)

Why be difficult to deal with when, with just a little more effort,
one can be completely impossible.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-14T08:25:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpfpmc$cba$1@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com> <gpdlj1$g36$3@reader1.panix.com> <7206l1FmsavuU1@mid.individual.net>`

```
In article <7206l1FmsavuU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>,
…[15 more quoted lines elided]…
>can complicate them."]

According to http://babelfish.altavista.com - which,in my 
browser,redirects to http://babelfish.yahoo.com, how things change, my 
word, indeed - it gets rendered as 'Why simply make when man can 
complicate?'... but Mr Dashwood;s translation should suffice.

>
>I get irritated when I hear someone (usually a Manager) using the acroynm 
>"KISS" (Keep It Simple, Stupid) to rally the troops.

It has been long, long time since someone has tried to pull that one on 
me.  My response used to be 'It isn't really that difficult, let me show 
you what it is *really* doing...' and then compile with a LIST option and 
say 'Now here,s what's *really* going on...' ... and wait until the eyes 
glazed over and then I'd never be bothered by that person again.

Nowadays I don't get much of it, though... and when I do I remind my 
client that making something simple is very, *very* hard work and you do 
realise that asking for more of my work means means signing more of my 
timesheets, right?

I know I am a consultant/contractor/hired gun and no matter how good my 
work is the moment I leave anything that goes wrong will be blamed on 
me... it is De Rererum Natura in this (and many other) crafts, it's always 
the fault of the guy who just left.  I work very, very hard, though... 
including comments like *** KIDS, DON'T TRY THIS AT HOME *** and *** 
WARNING: TWO-YEAR PROGRAMMER CODE STOP HERE, CONTINUE WITH CAUTION *** so 
that I hope to have, some day, a corner-office idiot look at my work and 
say 'But... but it is so *simple*, why did we pay him so much money to 
write such simple stuff?'... and not realise that the difficulty came from 
making the stuff simple, to eliminate reference modifications from 
copymembers that weren't designed to do what they wanted and submit them 
along for the Prod move, to break down a ADD that went on for pages into 
four COMPUTES (that still go on for pages... but the chunks got 
smaller)... little things.

Meanwhile, in the latest newse... we've gotten a new Corner Office Idiot, 
our... where's my octal hand?... sixth in two years... but he seems to 
like me and has extended my contract, originally a 'nine months at the 
most' job begun in November, 2003, for another four months.

(I actually dodged an offer of a full-time position rather well, even by 
my own standards... the COI made one, I burbled some 'How very kind of 
you, let me muse over this' noises'... waited a bit... and then, like all 
the other Corner Office Idiots, she was gone.  When my Tech Lead mentioned 
it, long after the position had expired, I smiled and said 'Come now, Mr 
Jones... Ms Smith did not offer me a full-time job, considering what we 
both know about me we know that she offered me an insult.  Wasn't I 
polite?'

He laughed, ruefully, and said 'Yeah... but if that's all she had to 
offer...'... and I responded with 'If that's what she has to offer then 
this is what she gets in return; it is good that I am calm and do not take 
umbrage at such insults, eh?'

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 8)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-03-14T16:46:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ojQul.21840$yr3.1440@nlpi068.nbdc.sbc.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com> <gpdlj1$g36$3@reader1.panix.com> <7206l1FmsavuU1@mid.individual.net> <gpfpmc$cba$1@reader1.panix.com>`

```
In article <gpfpmc$cba$1@reader1.panix.com>, docdwarf@panix.com () wrote:
>In article <7206l1FmsavuU1@mid.individual.net>,
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

>>>
>>> As the Italians used to say, 'Warum einfach machen wann Mann kann
>>> kompliziert?'

Should be "komplizieren"; "kompliziert" means "complicated".

Should also be "mann", not "Mann". In lower-case, it's a pronoun meaning "one, 
someone, anyone, generic 'you', etc.". In upper-case, it's a noun meaning 
"man, mankind".

The word order is wrong, too: should be "... wann mann komplizieren kann."

"Einfach" can be translated as either "simple" or "simply"; inserting "etwas" 
("something") after "Warum" removes the ambiguity of meaning.

>>
>>[for the benefit of non-German speakers: "Why make things simple, when you 
…[5 more quoted lines elided]…
>complicate?'... but Mr Dashwood;s translation should suffice.

The babelfish translation is a fairly accurate translation of what you 
[incorrectly] *wrote*; Mr. Dashwood's translation accurately captures what I 
believe you *meant*.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-16T16:03:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gplt7r$ejb$1@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <7206l1FmsavuU1@mid.individual.net> <gpfpmc$cba$1@reader1.panix.com> <ojQul.21840$yr3.1440@nlpi068.nbdc.sbc.com>`

```
In article <ojQul.21840$yr3.1440@nlpi068.nbdc.sbc.com>,
Doug Miller <spambait@milmac.com> wrote:
>In article <gpfpmc$cba$1@reader1.panix.com>, docdwarf@panix.com () wrote:
>>In article <7206l1FmsavuU1@mid.individual.net>,
…[6 more quoted lines elided]…
>Should be "komplizieren"; "kompliziert" means "complicated".

I'm not sure... I'm not Italian.

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-14T11:44:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7205tqFmocbmU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com>`

```
Michael Mattias wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:71tmc0Fn6i3nU1@mid.individual.net...
…[8 more quoted lines elided]…
> MCM

Yes, I think so.

I have a theory that all intelligent people are lazy. (It doesn't mean that 
all lazy people are intelligent :-))

If being smart doesn't help us find easier, better, more effiecient, ways to 
do things, then there's not much point in being smart.

The Victorian work ethic embodied in the "stairs to success" is a noble one 
and will work whether you are smart or not, but it is the nature of smart 
people to look for an "easier" way.

6 years ago, here in this very forum, Judson and I were debating the merits 
of  "good" and "bad" code. There were some very long posts and I offer the 
following extract from one of them...:

<anecdote on the side - skip this if you are of a serious disposition and
are only interested in the debate...>


Many years ago, before my body was wrecked by a dissolute, self indulgent
lifestyle, I used to climb mountains.


(Hanging on to a rock face by your fingernails is excellent practice for
handling IT deadlines, but I didn't know that at the time <G>)


Anyway, the guy who was my climbing teacher was one of the wild breed of
Kiwis who live ONLY for mountains. He belonged to the same club as Edmund
Hillary and was of similar disposition.


On one occasion we were working our way up a ridge on Taranaki (Mt. Egmont,
8260 feet...believe me I have counted every one of them several
times...<G>), when we came to a sheer outcrop of rock called "Humphrey's
Castle".  Noticing there was a well worn path around this obstacle, and not
being entirely stupid, I started to walk around it. Bob, my teacher, pulled
me up and said: "Whered'ja think yer goin'?". I replied that there was an
established path around it and it made sense to take the low risk approach.
He looked at me with piercing blue eyes that showed just the faintest hint
of scorn, and said: "Peter, let's pretend this is the ONLY way..."  To my
surprise we scaled it, and I was rewarded with a smile from Bob for my
efforts, and a sandwich on the top of it. The view was worth the climb, and
the lesson has never been forgotten over the ensuing years.


To this day, whenever I hear the phrase: "the only way..." I think about a
summer afternoon sitting on Humphries Castle gazing down a sheer rock face
several thousand feet into green valleys below, and realise that "the only
way" is NOT the only way; it is the only way we can think of at the moment,
and sometimes, the hard way is the most rewarding.


</anecdote on the side - skip this if you are of a serious disposition and
are only interested in the debate...>

As you can see, I am not averse to doing things that are hard, but (and I 
find this increasingly as I get older) I will ALWAYS look for an easier way.

I don't think there's anything wrong with this and I'm quite sure we 
wouldn't have most of the labour saving devices we take for granted every 
day, if there weren't other people out there who feel the same.

Pete.
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-16T09:43:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mssr45o1gf17et4mp4aga2isa5aboiish@4ax.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <ld8ul.22086$Ws1.16486@nlpi064.nbdc.sbc.com> <71tmc0Fn6i3nU1@mid.individual.net> <GJsul.22159$Ws1.5311@nlpi064.nbdc.sbc.com> <7205tqFmocbmU1@mid.individual.net>`

```
On Sat, 14 Mar 2009 11:44:10 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I have a theory that all intelligent people are lazy. (It doesn't mean that 
>all lazy people are intelligent :-))
>
>If being smart doesn't help us find easier, better, more effiecient, ways to 
>do things, then there's not much point in being smart.

I don't see a correlation between intelligence and laziness myself.
But intelligent people can use their laziness more effectively (By
inventing ways to make less work in the future).

That said - two types of laziness are the person who leaves his dishes
out so that he doesn't have to do them yet, and the person who washes
the dishes now so that he doesn't have a big stack to do later.
```

##### ↳ ↳ Re: Call a .BAT file?

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-03-12T09:01:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49b915b6$0$5453$bbae4d71@news.suddenlink.net>`
- **In-Reply-To:** `<71se0pFmonffU1@mid.individual.net>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net>`

```
Thanks Pete.  I am using scripts in the .BAT file to initiate an FTP.  My 
Cobol program 1st modifies the .BAT file to put yesterday's date into the 
name of the file to be retrieved, then FTP's it, then processes the file for 
it's intended business purpose.  Since the .BAT file works, "if it ain't 
broke, don't fix it".  Thanks again, Paul


"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:71se0pFmonffU1@mid.individual.net...
Paul H wrote:
> I want to have my program execute a .BAT file, then continue to
> process. Call and cancel doesn't work.  I'm using an old version of
> MicroFocus COBOL. Is there a method to accomplish this?  TIA, Paul

You can get your COBOL program to execute ANY executable (including a .BAT
file) by using the Windows Shell API. It is exactly the same as running a
DOS command.

You need the ShellExecute  or WinExec commands of the Windows API. If you
are running an old (16 bit) compiler it is in a .dll called "shell.dll", if
you are running something better than windows 95 it is in a .dll called
"shell32.dll"

Here's a link to sample code:

http://supportline.microfocus.com/examplesandutilities/nesamp.asp#Win32API

If you substitute your .Bat filename into the WinExec sample, where it says
"Notepad.exe"  you should be OK.

WinExec is fine to kick off something simple, but you should really use the
ShellExecuteEX if you are going to handle documents.

Check out both these samples for future reference.

(BTW, .bat files are really obsolete and best avoided. These days it is .wsh
(Windows Script Hosting), which has much richer functionality,  is closer to
the system, and much more stable. You can do much more than was ever
possible with .bat files. Depending on what you want your batch file to do,
you should consider writing it in WSH or VBScript. (You can also use
JavaScript or C# if you want to get really sexy :-))

HTH,

Pete
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T14:16:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb5g7$dsj$6@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <49b915b6$0$5453$bbae4d71@news.suddenlink.net>`

```
In article <49b915b6$0$5453$bbae4d71@news.suddenlink.net>,
Paul H <NoSpamphobergNoSpam@att.net> wrote:

[snip]

>Since the .BAT file works, "if it ain't 
>broke, don't fix it".

No, no... first, start with a square... then carefully align your chisel 
and remove each of the corners, making it an octagon... then do it again, 
making a hexadecagon... and then again, and again, and again, and again, 
using something similar to the polygon approximation method of determining 
pi (hey, it worked for Archimedes, didn't it?)... and, well, you'll never 
really *get* a circle but you'll get something awfully close and it'll be 
All Your Own Invention and that's what's most important, right?

And then, when you're done, dusty and proud... tell this to your Manager 
as part of your status-report, s/he'll be *so* proud that you used up all 
that time and resources instead of putting to work that which was already 
there and running like a watch... oh, and I'm the King of England, too.  
God Save the Me!

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 4)_

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-03-12T09:56:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49b922b4$0$5493$bbae4d71@news.suddenlink.net>`
- **In-Reply-To:** `<gpb5g7$dsj$6@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <71se0pFmonffU1@mid.individual.net> <49b915b6$0$5453$bbae4d71@news.suddenlink.net> <gpb5g7$dsj$6@reader1.panix.com>`

```

Hi Doc.  Do you mean that I shouldn't set aside all my other assignments to 
bring every aspect of this issue up to the latest state of the art 
methodology, even if it may only be used for another few months?  Aww 
shucks!  And I've only been programming in various languages (10 or 15) for 
a few years (since 1963) so I really want to keep current on EVERYTHING! 
I'm doing Cobol because I have a contracting job for a company that can't 
hardly find anyone who understands their systems.  Thanks, Paul

<docdwarf@panix.com> wrote in message news:gpb5g7$dsj$6@reader1.panix.com...
In article <49b915b6$0$5453$bbae4d71@news.suddenlink.net>,
Paul H <NoSpamphobergNoSpam@att.net> wrote:

[snip]

>Since the .BAT file works, "if it ain't
>broke, don't fix it".

No, no... first, start with a square... then carefully align your chisel
and remove each of the corners, making it an octagon... then do it again,
making a hexadecagon... and then again, and again, and again, and again,
using something similar to the polygon approximation method of determining
pi (hey, it worked for Archimedes, didn't it?)... and, well, you'll never
really *get* a circle but you'll get something awfully close and it'll be
All Your Own Invention and that's what's most important, right?

And then, when you're done, dusty and proud... tell this to your Manager
as part of your status-report, s/he'll be *so* proud that you used up all
that time and resources instead of putting to work that which was already
there and running like a watch... oh, and I'm the King of England, too.
God Save the Me!

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T15:27:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb9kp$hal$2@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <49b915b6$0$5453$bbae4d71@news.suddenlink.net> <gpb5g7$dsj$6@reader1.panix.com> <49b922b4$0$5493$bbae4d71@news.suddenlink.net>`

```
In article <49b922b4$0$5493$bbae4d71@news.suddenlink.net>,
Paul H <NoSpamphobergNoSpam@att.net> wrote:
>
>Hi Doc.  Do you mean that I shouldn't set aside all my other assignments to 
>bring every aspect of this issue up to the latest state of the art 
>methodology, even if it may only be used for another few months?

As Wittgenstein taught, 'meaning is the result of interpretation'... and 
there might be more than one way to interpret what I wrote.

>Aww 
>shucks!  And I've only been programming in various languages (10 or 15) for 
>a few years (since 1963) so I really want to keep current on EVERYTHING! 

Best to take it easy, then... I've noticed a trend towards replacing good, 
solid vacuum-tubes ('valves' in Britspeak) with thingummies based on the 
work of William Shockley (and others), I think they're called 
'transistors'.

>I'm doing Cobol because I have a contracting job for a company that can't 
>hardly find anyone who understands their systems.

I've noticed that companies who say 'we can't find hardly nobody who can 
(x)' are usually saying 'we can't find hardly nobody who can (x) FOR THE 
PRICE WE WANT TO PAY'; my advice is 'double the rate you're offering and 
see what kind of responses you get.'

>Thanks, Paul

You're quite welcome... and it was worth at least *double* what I charged 
you for it!

DD
```

###### ↳ ↳ ↳ Re: Call a .BAT file?

_(reply depth: 6)_

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-03-12T11:37:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49b93a35$0$5497$bbae4d71@news.suddenlink.net>`
- **In-Reply-To:** `<gpb9kp$hal$2@reader1.panix.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <49b915b6$0$5453$bbae4d71@news.suddenlink.net> <gpb5g7$dsj$6@reader1.panix.com> <49b922b4$0$5493$bbae4d71@news.suddenlink.net> <gpb9kp$hal$2@reader1.panix.com>`

```
I know what you mean.  When I went to DeVry in about 1960, they trained us a 
little in analog computer technology (using 400 volt DC and tubes, as I 
remember, with circuits that measured voltages to determine results of 
division, etc. to a somewhat accurate answer - sort of like an electronic 
slide rule).  They said there were digital computers but they would never go 
anywhere.  We also fooled around a little with transistors, but mostly built 
full-wave ??? vacuum tube power supplies.  And, I'm probably getting about 
what I'm worth for the Cobol work - but I can do it at home, so my commute 
is walking upstairs in my 'jammies...  Keeps the semi-retired 
getting-feeble-minded folks like me busy.

<docdwarf@panix.com> wrote in message news:gpb9kp$hal$2@reader1.panix.com...
In article <49b922b4$0$5493$bbae4d71@news.suddenlink.net>,
Paul H <NoSpamphobergNoSpam@att.net> wrote:
>
>Hi Doc.  Do you mean that I shouldn't set aside all my other assignments to
>bring every aspect of this issue up to the latest state of the art
>methodology, even if it may only be used for another few months?

As Wittgenstein taught, 'meaning is the result of interpretation'... and
there might be more than one way to interpret what I wrote.

>Aww
>shucks!  And I've only been programming in various languages (10 or 15) for
>a few years (since 1963) so I really want to keep current on EVERYTHING!

Best to take it easy, then... I've noticed a trend towards replacing good,
solid vacuum-tubes ('valves' in Britspeak) with thingummies based on the
work of William Shockley (and others), I think they're called
'transistors'.

>I'm doing Cobol because I have a contracting job for a company that can't
>hardly find anyone who understands their systems.

I've noticed that companies who say 'we can't find hardly nobody who can
(x)' are usually saying 'we can't find hardly nobody who can (x) FOR THE
PRICE WE WANT TO PAY'; my advice is 'double the rate you're offering and
see what kind of responses you get.'

>Thanks, Paul

You're quite welcome... and it was worth at least *double* what I charged
you for it!

DD
```

#### ↳ Re: Call a .BAT file?

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-03-12T10:50:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d12cc229-ee24-49ba-a5f9-5cc2198887f8@v13g2000pro.googlegroups.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net>`

```
On Mar 12, 5:00 pm, "Paul H" <NoSpamphobergNoS...@att.net> wrote:
> I want to have my program execute a .BAT file, then continue to process.
> Call and cancel doesn't work.  I'm using an old version of MicroFocus COBOL.
> Is there a method to accomplish this?  TIA, Paul

CALL "SYSTEM" USING command-string

The command string should be null terminated.
```

##### ↳ ↳ Re: Call a .BAT file?

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-03-12T20:53:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49b9bc9f$0$5475$bbae4d71@news.suddenlink.net>`
- **In-Reply-To:** `<d12cc229-ee24-49ba-a5f9-5cc2198887f8@v13g2000pro.googlegroups.com>`
- **References:** `<49b888db$0$5478$bbae4d71@news.suddenlink.net> <d12cc229-ee24-49ba-a5f9-5cc2198887f8@v13g2000pro.googlegroups.com>`

```

That worked!  That was entirely too easy.  I can't thank you enuf!

<riplin@Azonic.co.nz> wrote in message 
news:d12cc229-ee24-49ba-a5f9-5cc2198887f8@v13g2000pro.googlegroups.com...
On Mar 12, 5:00 pm, "Paul H" <NoSpamphobergNoS...@att.net> wrote:
> I want to have my program execute a .BAT file, then continue to process.
> Call and cancel doesn't work. I'm using an old version of MicroFocus 
> COBOL.
> Is there a method to accomplish this? TIA, Paul

CALL "SYSTEM" USING command-string

The command string should be null terminated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
