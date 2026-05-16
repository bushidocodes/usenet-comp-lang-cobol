[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# grep'ing CoBOL source

_17 messages · 8 participants · 2010-08 → 2010-09_

---

### grep'ing CoBOL source

- **From:** Ken <klshafer@att.net>
- **Date:** 2010-08-12T18:13:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>`

```
Gentle CLC'ers,

I got a couple of puzzles to work on, one technical and the other one
business/career like, and I'm pretty sure at least Richard will sign
on to the technical and everybody can chime in on the career/tactical
one.

Goes like this...

My shop (about 20-25 developers, and another 20-25 business analysts,
testers, managers, etc.) bought a CoBOL Analyzer tool several months
ago and is trying to make it work, evaluate its effectiveness, decide
on whether to sign on for upgrades and maintenance, etc. etc. I'm not
sure, but I think they paid somewhere in the 5-figure range for it.
Sorry, no product names will be given to protect both the guilty, and
the innocent (that's ME :-).

Anyway, I kinda wanted to test it out myself, but I never got an
install, The Fates decided that others would be the Chosen, so I just
let it go...

They tried it out on the biggest single program in our system, one
I've made a lot of requested changes to, about 15K LOC (without the
DB2 DCLGEN and COPY expansions), and I confessed I chuckled a bit when
it blew up because nested PERFORMs it was stacking to prepare a HIPO
chart to wrap around the building walls blew a gasket. Yes, yes, I was
gratified to feel that even at my tender gray-haired age, the PERFORM
push-down stack in my brain during my visual code analysis apparently
exceeds that of a 5-figure tool.

No matter.  It piqued my interest when I got assigned my next task,
the "sticky field" task.
The Manager asked of Me: Ken, Suppress the current online system's
behavior of clearing the case-number field when navigating online
between subsystems. The User wants the value _retained_. It's too much
trouble to re-enter. It's already retained within subsystems, but is
lost when moving from subsystem to subsystem (subsystem == 1st level
submenu item from the top level main menu.)

The Maintenance Guru immediately turned me on to a quick fix in screen
MAINMENU that cleared the field in the COMMAREA (MOVE SPACES TO...)
before invoking SUBMENU with another transaction. OH! Easy enough.
"All ya' gotta do is disable that one line", the Business Analyst
chortled :-).

Maintenance Guru says, "Not so fast... Submenu 10 doesn't seem to work
with that change alone. Ken,  you better check out why not..."

Yes, sir, Guru, and I found that SUBMENU also had a MOVE SPACES TO
<sticky-field> statement as well. I heard a little voice say, "All ya'
gotta do is disable that line and the first line too." :-)

Hmmmm.... could _other_ "clearing statements" be lurking elsewhere, in
other screens, ready to trip me up??

So I took up The Quest...

Went home, went on my computer where I had installed MKS Toolkit (Unix
like utilities for WinDoze/DOS), for which I have multiple paid-for
versions/licenses, and copied the .exe's onto a CD-ROM. Probably all I
need is grep (global regular expression print), sed (stream editor),
sh (shell), and echo (display).

Went to work the next day, and loaded the CD into the READ-only CD-ROM
drive (No writes to external media permitted!!) drive of my work
machine, went into Accessories, and opened up a DOS command-line box.
Then executed a tiny autoexec.bat file on my CDE to set four or five
environment variables that were needed (including PATH). They would
apply only to the life of the DOS box, then die.

Then I downloaded via terminal emulator FTP about 5000 COPYLIBs and
2000 program sources from the mainframe DVLP partitioned data set
(PDS) onto my C: drive. No security violation, nothing squawked. Gee,
I must be authorized to do this... :-).

At this point, caution got the best of me, and I went to the System
Admin...

Me: "Hey, Scott - ya' know how we often download a program or two from
the mainframe so we can cut and paste snippets into MS-Word with
highlighted text and the like to conduct code reviews of our changes?"

Scott: "Yeah."

Me: "Well, any prohibition against using wildcarding to download the
whole shebang?"

Scott: "If you're not taking it out of the building, No."

Me: "And Scott, as Admin, you're the only one with authority to
install software on the PC's, right?"

Scott: "Yep, only a guy with Admin privileges can do that, and that's
me. You're not Admin. You don't even have the capability to do it."

Me: "That's reassuring <smile>. So if I execute .exe's off a CD-ROM in
a DOS box, that's not an Install, right? I'm not writing any
executables to the C: drive, and I'm not changing the Registry."

Scott: "That's not an Install. You're OK."

I smiled. :-).

Went back to my machine, and breathlessly entered...

sh <enter>

and promptly saw the friendly $ shell prompt.

I changed working directories to position me over the 5000 COPYLIBs
that contain procedure division code for the screens...

Executed some grep one-liners until I put the debugged results into a
shell script (used temp files rather than piping to help debug
intermediate results.)

echo "grep'ing TO XFER-BLK-BOX-ACCOUNT..."
grep "TO.*XFER-BLK-BOX-ACCOUNT" *.CPY >tmpb1.txt
echo "grep'ing TO XFER-BLK-BOX-ACCT-NUM..."
grep "TO.*XFER-BLK-BOX-ACCT-NUM" *.CPY >tmpb2.txt
cat tmpb1.txt tmpb2.txt >blkboxto.txt
echo "blkboxto.txt contains all TO BLK-BOX-ACCOUNT and TO-BLK-BOX-ACCT-
NUM stmnts"
sed -n /ZERO/p <blkboxto.txt >blkboxzerosto.txt
echo "blkboxzerosto.txt contains all ZEROS/ZEROES TO BLK-BOX-ACCT-NUM
stmnts..."
sed -n /SPACES/p <blkboxto.txt >blkboxspacesto.txt
echo "blkboxspacesto.txt contains all SPACES TO BLK-BOX-ACCOUNT
stmnts..."
sed -E /\(ZERO\)/d <blkboxto.txt | sed -E /\(SPACES\)/d
>bklboxotherto.txt
echo "blkboxotherto.txt contains all <<other-than-spaces-or-zeros>> TO
stmnts..."
echo "Done!"

It executed and scanned the 5000 COPYLIBs in less than two
minutes :-).

Result: I had files of occurrences of three kinds of statements -
o One file of about 5 or 6 MOVE SPACES TO <sticky-field>  (including
MAINMENU)
o One file of about 8 or 10 MOVE ZEROES TO <sticky-field-redefined-as-
PIC9's>
o One file of about 40 or 50 MOVE <other-data-element> to <sticky-
field>

Gleefully entered the conference room with Maintenance Guru, Team
Lead, Business Analyst, and Functional Analyst..

"Yeah, all we gotta do is disable the clearing statement in the main
menu...
 - and in this Option 10 submenu...
 - and in these other two or three submenus...
 - and check out these other 8 or 10 screens farther down the
subsystem screen navigation path to see if its safe to disable there
too, and then test the screen navigation paths around all of these
we've changed.

The Maintenance Guru grinned, the Team Lead looked a little quizzical,
and the analysts looked a little mystified that something so simple
could require modifying more than a couple of screens, but they were
otherwise agreeable.

But I was not finished...

"OH! And one more thing, just to make sure... I know you want the
value _retained_, but when there is a screen whose intent is to
_change_ the  value, then _that_ new value becomes the sticky value,
and it's OK the original one is lost, right? Here's a list of about 50
screens out of the 600 or so that do that. I think I got them all, but
I might have missed a couple."

Everybody agreed that indeed this was what was wanted, so we adjourned
amicably.

Afterward, Team Lead took me aside to ask, "Ken, why did you present
that list of screens where the case-number is reset to nonzero?"

Me: "Oh, just so that there were plenty of examples for the Analysts
to know what I was talking about."

He must have been wondering why two or three examples were not enough
for me, and not knowing how I did it, he must have imagined me single-
stepping ISPF 3.14 through 5000 COPYLIBs representing 600 screens,
searching for MOVE TO sticky-field statements. I laughed to
myself. :-)

If you're still with me, here's the two questions...

1. Technical. OK, I left some stuff out above. I also grep'd for
INITIALIZE <sticky-field>, but that didn't turn up anything. The
tougher situation is when <sticky-field> appears on a source line by
itself, or with a comma, or a period, or the like, and the CoBOL MOVE
statement wraps around multiple source lines. grep and sed work on one
line at a time. I'm pretty sure that I could have programmed something
in the awk utility to cover line wraparound, but didn't want to take
the time.

Instead I grep'd for this to identify the "standalone" lines...

grep -E "^...... *,? *XFER-BLK-BOX-ACCOUNT *[,.]* *[0-9]*$" *.CPY
>xferd07alone.txt
(The beginning and end of this regular expression string is to account
for line numbers at the beginning and end of the record.)

There weren't too many of those, 20 or 30, so I just went into the
COPYLIB source for each of them to see how they were used. Here I did
severalt that were being INITIALIZEd by an INITIALIZE verb a few
source lines above, and I found a couple where sticky-field was one of
several destinations for MOVE SPACES. I added these to my lists.

So, question - will the grep above catch 99% of the "isolated" data-
element lines? OK, I guess it wouldn't catch the following line
123456                              , XFER-BLK-BOX-ACCOUNT
END-IF      12345678
but usually if we have something like...
IF something-or-other
       MOVE SPACES TO element-1,
                                      element-2,
                                      element-3,
                                      element-4
END-IF
... we have the END-IF on a line by itself, right? And not on the same
line as element-4? OK, you know I'm not talking what is syntactically
correct, but rather what is the preponderance of coding style across
the industry.

Anyway, I'm just looking for a "succint" regular expression to grep
and find nearly all occurrences of a data-element appearing on a line
by itself. Regular Expression syntax is still a bit of a challenge for
me, and I usually approach it by starting with the most loosely
defined one that matches too much stuff and then I add more and more
to the expression to zero in on the "hits" that I am really looking
for.

2. Career/Political Question -
- What do I do now? I mentioned this tool capability to one low-level
manager, and he was kinda interested, but he is not yet following up
with me... hmmm.... might be conflicting with a more expensive tool
that doesn't do as much, but just as easily Top Manager maybe wants to
kill that one, so maybe it's OK, maybe not. Can't get a good read.
- Uhhhhh --- OK, I've got multiple licenses, so _probably_ I've got
that angle covered as far as I'm not using unlicensed software, but
maybe there's some fine print somewhere that says I can _Install_ it
on a machine, but I can't make "copies" of it onto a CD... :-) --- but
I'm not gonna share it willy-nilly across the floor, I'm not into
that, so probably I'm low-profile enough to be Ok...I'm either going
to be the only user, or the shop will have to pony up for full install
licenses (they would want that for the support, anyway.)
- Cost is only about $500 a seat - do I promote this capability and
request 5-6 copies for the managers and a few key techs like me? Or do
I "fly below the radar" best I can, quietly execute this tool myself
and myself only, be the "best" maintenance grunt :-) onsite as far as
finding system impact of cross-referenced changes like this, and
feather my own job-security nest that way?
- OK, OK, I could ask He Who Signs My Timesheet, but his fortunes may
be tied to Expensive-Tool (there are clues that this is at least
somewhat true), and do I really need his permission to do what I'm
doing? From what I can tell I haven't violated any policy (haven't
taken company work product offsite, haven't installed unauthorized
software), all I've done amounts to bringing in a Cross pen to write
with instead of a Bic pen? (A bit of an overstatement, but you get the
point.)
- Or do I call an end to what has been an interesting experiment, and
go back to using ISPF 3.14 over and over again, for after all, I am
paid by the hour, and the Customer has been satisfied so far...

Your humbl' CLC occasional contributor,

Ken
```

#### ↳ Re: grep'ing CoBOL source

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-13T13:08:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i43g4g$ger$1@reader1.panix.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>`

```
In article <098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>,
Ken  <klshafer@att.net> wrote:
>Gentle CLC'ers,

Oh... ruling me out from the start, eh?

[snip]

>My shop (about 20-25 developers, and another 20-25 business analysts,
>testers, managers, etc.) bought a CoBOL Analyzer tool several months
>ago and is trying to make it work, evaluate its effectiveness, decide
>on whether to sign on for upgrades and maintenance, etc. etc. I'm not
>sure, but I think they paid somewhere in the 5-figure range for it.

Ahhhh, the old 'buy it first and let someone else see if it works' 
routine, that way the person authorising the purchase can always said 
'Well sure *I* bought it but (name of subordinate) couldn't make it work 
so It Isn't My Fault.'

(never mind that the purchase can be written off/depreciated as can any 
other business expense... something Cost Money so fingers must be pointed)

[snip]

>"All ya' gotta do is disable that one line", the Business Analyst
>chortled :-).
>
>Maintenance Guru says, "Not so fast... Submenu 10 doesn't seem to work
>with that change alone. Ken,  you better check out why not..."

This Guru fellow seems *very* secure in his position; responding to an 
'All ya gotta do' in that way seems to indicate such.

>
>Yes, sir, Guru, and I found that SUBMENU also had a MOVE SPACES TO
…[4 more quoted lines elided]…
>other screens, ready to trip me up??

At this point one turns it into a Matter of Simple Mathematics... haw haw 
haw!  'Gosh, Mr Corner-Office Idiot, I have a numeric sequence that begins 
with zero, one and two; all I gotta do is find out whether it continues in 
unitary digit incrementals (following the sequence of intergers) or does 
it shift into an exponential series (computers do stuff like that, 
y'know... they go from 2 to 4 to 8 to 16 to 32 really easily and you never 
know when you're going to encouter *that*)... '

(and at this point eyes should begin to glaze and you Move In For The 
Kill, the prize of the hunt, in this instance, being enough time to do 
what's needed without stinkwads stopping your cubicle every 37.5 minutes 
saying 'So how far have you gotten on this?', and you should muster 
enthusiasm and glee for the next)

'... but since we all know that Things Are Different Here maybe it's 
something *really* fascinating, like a Fibonacci sequence of 
0,1,1,2,3,5,8,13,21... oh, *you* know the rest... and they're found all 
over the place, like the distribution of seeds in a sunflower spiral, the 
shell of the nautilus (the cephalopod, not the submarine in the Jules 
Verne story... or that exercise-device they used to advertise on 
television... I wonder whatever happened to those) and the surface-cells 
in pine cones... just fascinating, the 'Golden Ratio', or 'Phi'. of 
1:1.618 just kind of falls right out of it...'

... and at this point everyone in the room should be willing to cut you a 
five-week task order just to get you out so they can get back to talking 
about golf or sports scores.

>
>So I took up The Quest...

[snip]

>Gleefully entered the conference room with Maintenance Guru, Team
>Lead, Business Analyst, and Functional Analyst..
…[25 more quoted lines elided]…
>amicably.

Another classic... 'we always want it done (this way) except when we 
don't'.

>
>Afterward, Team Lead took me aside to ask, "Ken, why did you present
…[3 more quoted lines elided]…
>to know what I was talking about."

I would say this was a missed chance to Establish Precedence.  Not that I 
am an example of anything special... but when I am asked 'Why did you do 
this?' and the immediate response is not 'Because (person of sufficient 
authority) told/asked me to' I reply 'I thought it was a Good Idea at the 
time; it allowed for...' and in this case the follow-through is 'the 
Analysts to have plenty of examples'.

In other cases it may be something like 'I thought it was a Good Idea at 
the time; it demonstrated the pervalence of the situation so that time 
could be saved avoiding other facile (fancy-talk for 'all ya gotta do') 
attempts at resolution' or 'I thought it was a Good Idea at the time; it 
showed the possible cost-reductions would be balanced against the 
maintenance and testing costs'...

... but the point is *not* to give an actual reason, the point is to get 
'I thought it was a Good Idea at the time' to be an acceptable response 
from you.

[snip]

>1. Technical. OK, I left some stuff out above. I also grep'd for
>INITIALIZE <sticky-field>, but that didn't turn up anything. The
>tougher situation is when <sticky-field> appears on a source line by
>itself, or with a comma, or a period, or the like, and the CoBOL MOVE
>statement wraps around multiple source lines.

I was wondering when this might appear.  Since I'm unfamiliar with the 
'all ya gotta do' to make grep and sed and such work I would have used 
something like:

//SEARCH  EXEC PGM=ISRSUPC,      
//            PARM=(SRCHCMP,     
//            'ANYC')            
//NEWDD  DD DSN=YOUR.PDS.NAME,
//          DISP=SHR             
//OUTDD  DD SYSOUT=*             
//SYSIN  DD *                    
SRCHFOR  ' STICKY-FIELD'                 
CMPCOLM 12:72
/*

This will process all the members of a PDS (and search only between 
columns 12 and 72, saving Valuable CPU Time).  Note the space after the 
first ' in the SRCHFOR card; this is used to eliminate hits on 
WS-STICKY-FIELD or TEST-STICKY-FIELD.  (if such hits are wanted then 
remove the space and snug the ' up to the S)

[snip]

>2. Career/Political Question -

I'm really no good at all at addressing such matters; I manipulated my 
brag-sheet to show two years' worth of experience as an employee and have 
been 'topped out' as a consultant/contractor/hired gun ever since.

DD
```

##### ↳ ↳ OT: Dealing with the COI

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-08-17T04:56:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eefc9ae1-cb34-4eb4-8d94-9451a1428861@i31g2000yqm.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <i43g4g$ger$1@reader1.panix.com>`

```
On Aug 13, 2:08 pm, docdw...@panix.com () wrote:
>
> I would say this was a missed chance to Establish Precedence.  Not that I
…[4 more quoted lines elided]…
> Analysts to have plenty of examples'.

As most COIs are blessed with aftersight, 'I thought it was a good
idea....' can be met by 'With your experience you should have realised
that it was a bad idea....'.

Perhaps a wiser option would be 'Bearing in mind the problems
with....the best option is to go with....'. You will still be wrong
but at least you have explained why your option is best up front and
got a tacit sign-in from all present.
```

###### ↳ ↳ ↳ Re: OT: Dealing with the COI

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-17T12:08:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4du3d$2v0$1@reader1.panix.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <i43g4g$ger$1@reader1.panix.com> <eefc9ae1-cb34-4eb4-8d94-9451a1428861@i31g2000yqm.googlegroups.com>`

```
In article <eefc9ae1-cb34-4eb4-8d94-9451a1428861@i31g2000yqm.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Aug 13, 2:08?pm, docdw...@panix.com () wrote:
>>
…[9 more quoted lines elided]…
>that it was a bad idea....'.

My reply to that is usually 'If the results were known in advance then 
another path would have been taken; had either of us the ability to 
predict the future that well we might be making our livings off 
stockmarket-earnings.'

(Having it thusly demonstrated that I am working with a second-guessing 
micro-manager I polish up my bragsheet and look for another contract.)

>
>Perhaps a wiser option would be 'Bearing in mind the problems
>with....the best option is to go with....'. You will still be wrong
>but at least you have explained why your option is best up front and
>got a tacit sign-in from all present.

Note, Mr Maclean, that your wiser option is cited as present tense and 
mine is past.  There might be a difference in approach given the location 
in space-time that one finds one'sself in regarding the event in question.

DD
```

#### ↳ Re: grep'ing CoBOL source

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-08-13T17:14:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c65614d$0$286$14726298@news.sunsite.dk>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>`

```
Ken wrote:

<<snip technical details>> 

> Executed some grep one-liners until I put the debugged results into a
> shell script (used temp files rather than piping to help debug
…[48 more quoted lines elided]…
> the industry.

That would be a difficult answer to your question. But I might try. You
can concatenate a lot of lines with sed (before your grep), where the
last line of a serie should have a single dot for termination of a
COBOL statement. In the grep statement each line terminator like <LF>
will be changed to a space when not preceded by a dot.

In that way grepping on source and destination fields will be more
simple with a regular expression.

BTW, since some recent sed versions the --in-place option can be used to
avoid temporary files.

> 2. Career/Political Question -
> - What do I do now? I mentioned this tool capability to one low-level
…[7 more quoted lines elided]…
> on a machine, but I can't make "copies" of it onto a CD... :-)

I don't have read the license of your software as we don't have
MS-Windows software on our networks, but both grep and sed are
available in multiple Free Software servions, as in you have the right
to study, modify and redistribute it like you want.

But to give rest to others problems, you might select an older box,
install a Linux distribution, a BSD version or even an OpenSolaris
version on it and run FTP, grep and sed without retributions.

Good luck with your 5 figure savings. :-)
```

#### ↳ Re: grep'ing CoBOL source

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2010-08-13T10:39:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odqdnc2xyeCK-vjRnZ2dnUVZ_gSdnZ2d@giganews.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>`

```
"Ken" <klshafer@att.net> wrote in message 
news:098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com...
>
> My shop (about 20-25 developers, and another 20-25 business analysts,
…[14 more quoted lines elided]…
> sed -n /ZERO/p <blkboxto.txt >blkboxzerosto.txt

[finding essentially MOVE ZERO/SPACE to XFER-BLK-... targets]

>It executed and scanned the 5000 COPYLIBs in less than two
>minutes :-).

Yes, grep was invented so people could fish around in big piles of code
quickly.    And that's really useful, as Ken has shown.

The good news is that grep is pretty fast.   The not so good
news is that is only pretty fast; he had to run it bunch of times.
Note he was piping the results to temp files to record what he did,
so he could decide if the answer was good.   He didn't say it,
but presumably he had to go open the files that appeared interesting
to verify his hits.

There are alternatives to grep which are faster and more convenient.

They are called "source code search engines".
OpenGrok (hub.opensolaris.org/bin/view/Project+opengrok)
is one of them (opensource).  It indexes and will thus search for 
identifiers very quickly;
it does this by knowing enough about the various langauges you
might work with to pick out identifiers.  It also
searches for abitrary strings with regexes at grep-like speeds,
and will show you lists of hits and offer to show you the code
directly.

Another is our Source Code Search Engine (commercial)
(www.semanticdesigns.com/Products/SearchEngine)
The SCSE knows the lexical structure (language tokens:
keywords, identifiers, numbers, comments, strings, whitespace)
of a variety of languages [e.g., Java, C#, C++, ) but
especially including COBOL
(and specifically AS400 and IBM Enterprise COBOL).
SCSE indexes *everything*, so it has lightning fast searches
for identifiers and combinations of tokens for complex queries.

Ken's search could have been written to the SCSE as:

    'MOVE'  ('ZERO'|'SPACES') 'TO' I=XFER-BLK-BOX-ACC*

(In fact for this query you don't really  need the 'MOVE' keyword).
You don't need to say anything about the whitespace, because
SCSE knows that whitespace isn't interesting (by definition,
in *any* language, for each langauge's defintiion of whitespace).
You don't need to worry about line breaks or formatting, because
they are whitespace, too.    Response times are seconds
across millions of lines of code, thousands of files.

Instead of temp files, he would have seen a GUI list of individual
lines across *all* files containing his hits; a single click from there
would pull up the the source file with the hit highlighted.

Such tools really are convenient ways to get "good information,
really fast".   I think the other tool Ken mentioned is one that
brings up "great information (maybe), much more slowly".

-- IDB
```

#### ↳ Re: grep'ing CoBOL source

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-08-16T12:51:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com>`

```
On Aug 12, 9:13 pm, Ken <klsha...@att.net> wrote:

> So, question - will the grep above catch 99% of the "isolated" data-
> element lines? OK, I guess it wouldn't catch the following line
…[24 more quoted lines elided]…
> read more »

something like:

grep -E "\bXFER-BLK-BOX-ACCOUNT\b" file ...
```

##### ↳ ↳ Re: grep'ing CoBOL source

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-17T23:15:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cv9ahFa0uU1@mid.individual.net>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com>`

```
Derek Schrock wrote:
> On Aug 12, 9:13 pm, Ken <klsha...@att.net> wrote:
>
…[30 more quoted lines elided]…
> grep -E "\bXFER-BLK-BOX-ACCOUNT\b" file ...

Unfortunately, that won't catch the case where it is followed by a full stop 
or comma...

I'm not familiar with Grep, but I do have a nodding acquaintance with 
regular expressions. (At least, in a MS .Net environment...)

An expression can be told to look across multiple lines... ?m:
it can be told to ignore whitespace... ?x:
and it can be told to ignore match case... ?i:

So, a MATCH expression :   ?m:?x:?i:XFER-BLK-BOX-ACCOUNT

Applied to the following code snippet:

move spaces to
               XFER-BLK-BOX-ACCOUNT,
               dname-1,
               dname2
more code...
move something to XFER-BLK-BOX-ACCOUNT

...will match both instances of XFER-BLK-BOX-ACCOUNT. But it doesn't take 
into account the context; match is purely on target string.

if you want to find instances of space, spaces, zero, zeroes or zeros being 
moved to the target, the corresponding expression would be:

?m:?x:?i:(space|zero).*(\r\n|.*).*XFER-BLK-BOX-ACCOUNT

This will match on the first instance in the above, and both instances in:

move spaces to
               XFER-BLK-BOX-ACCOUNT,
               dname-1,
               dname2
more code...
move zeroes to XFER-BLK-BOX-ACCOUNT

BUT, it won't match the first instance in:

move spaces to
               dname,
               XFER-BLK-BOX-ACCOUNT,
               dname-1,
               dname2
more code...
move zeroes to XFER-BLK-BOX-ACCOUNT

To enhance it so it will find the target in a string of datanames,  where 
the target isn't necessarily the first one, retaining the context (Move 
spaces/zeros etc), and across multiple lines,  you would need:

?m:?x:?i:(?:space|zero.*\w*.*\r\n)*.*(XFER-BLK-BOX-ACCOUNT)

This finds both instances of the above and it doesn't matter where the 
target is in a list of datanames.However, it doesn't match references to the 
target that do NOT involve spaces or zeros.

I use an Australian tool called Rad Software Regular Expression designer 
downloadable for free from http://www.radsoftware.com.au/regexdesigner/ to 
test and play with Regexes.

Pete.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

- **From:** Ken <klshafer@att.net>
- **Date:** 2010-08-18T11:51:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8338991-24d1-44f8-a606-ce0e75f71fa4@5g2000yqz.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net>`

```
On Aug 17, 7:15 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> An expression can be told to look across multiple lines... ?m:
> it can be told to ignore whitespace... ?x:
> and it can be told to ignore match case... ?i:

I don't think these ?x:, ?i:, ?m: are available to me... maybe they're
dotNet regexe's from what I read of the weblink you provided, but they
may not be POSIX? (I think MKS Toolkit is limited to POSIX
implementation, at least the early v5.2 version that I have. Could be
reason to upgrade to version 8 or 9 of MKS.)

>
> ?m:?x:?i:(space|zero).*(\r\n|.*).*XFER-BLK-BOX-ACCOUNT

But ahhhhh!! Even though \r (carriage return) and \n (new line) are
not mentioned in the MKS regexp manual page, they ARE mentioned as "C
escapes" in the awk page! So I can experiment with them. One
implementation question though probably comes to the forefront. For
MKS within WinDoze/DOS, does \n match LF (linefeed) or does it match
CR-LF? I really had not thought of using the "c escapes" in the
regular expression. I do remember using \t (tab) in some awk programs
I wrote some years back. If my foggy memory serves me correctly, some
Unix and lookalike utilities use tab as the default field separator on
output, and I usually mapped it over to something non-white-space like
":".

>
> ?m:?x:?i:(?:space|zero.*\w*.*\r\n)*.*(XFER-BLK-BOX-ACCOUNT)
>

Sadly, I don't think \w is available to me either...

Ken
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-19T11:37:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d395lF8nhU1@mid.individual.net>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <b8338991-24d1-44f8-a606-ce0e75f71fa4@5g2000yqz.googlegroups.com>`

```
Ken wrote:
> On Aug 17, 7:15 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> reason to upgrade to version 8 or 9 of MKS.)

Like I said, I'm only familiiar with the MS environment. I don't know what 
is available in your environment; Regexes vary across platforms, although 
the "core" syntax seems to remain consistent. I did test the constructs I 
posted, using the tool I linked to.

I was kind of hoping you might just try the expressions and tell us if they 
worked or not... :-)
>
>>
…[7 more quoted lines elided]…
> CR-LF?

What's MKS?

In Windows \n matches LF (I think...) that's why I used \r\n

Regular expressions were never part of MS DOS.


> I really had not thought of using the "c escapes" in the
> regular expression.

Sometimes, the best approach is the empirical one. Trial and error. The 
problem is that manual writers sometimes assume certain things and sometimes 
they forget certain things. Unless the people who wrote the software 
actually write the manual (and very often they don't), the manual is really 
a guide to how the software is supposed to work. (It's a bit like the pirate 
code in 'Pirates of the Caribbean"... :-))


> I do remember using \t (tab) in some awk programs
> I wrote some years back. If my foggy memory serves me correctly, some
…[8 more quoted lines elided]…
> Sadly, I don't think \w is available to me either...

It is very useful. So is ?x:

Pete.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-08-19T05:10:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2bb21d76-2d19-4a12-9e49-a74036ccd909@x21g2000yqa.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <b8338991-24d1-44f8-a606-ce0e75f71fa4@5g2000yqz.googlegroups.com>`

```
On Aug 18, 7:51 pm, Ken <klsha...@att.net> wrote:
> On Aug 17, 7:15 am, "Pete Dashwood"
>
…[22 more quoted lines elided]…
> I wrote some years back.

According to my Unix book (O'Reilly) AWK, NAWK and GAWK use \n to be
newline and \r to be carriage return. The implication being that
newline is not an implicit carriage return.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-19T13:31:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ce1r66tgrvvqok238fokouh79u6cf8it8d@4ax.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <b8338991-24d1-44f8-a606-ce0e75f71fa4@5g2000yqz.googlegroups.com> <2bb21d76-2d19-4a12-9e49-a74036ccd909@x21g2000yqa.googlegroups.com>`

```
On Thu, 19 Aug 2010 05:10:47 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>According to my Unix book (O'Reilly) AWK, NAWK and GAWK use \n to be
>newline and \r to be carriage return. The implication being that
>newline is not an implicit carriage return.

If you write an editor to be used on a Mac, it needs to be able to
handle classic Mac & Unix endings and probably Windows as well.

DOS (and Windows)... uses a carriage return and line-feed character
pair (= 2 bytes with hexadecimal value 0D and 0A).
UNIX ... uses just the line-feed character (= 1 byte with hexadecimal
value 0A).
MAC (Apple) ... uses just the carriage return character (= 1 byte with
hexadecimal value 0D).

But no need to handle EBCDIC conventions.

The most problem makes the MAC line ending type when combined with DOS
line endings and the file contains now CR+CR+LF. How should an
application read that now? As 2 blank MAC lines and 1 blank UNIX line
(= 3 blank lines), as 1 blank MAC line and 1 blank DOS line (= 2 blank
lines) or as mistake in line endings and therefore display the first
CR as character and interpret the remaining CR+LF pair as DOS line
ending.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-09-01T06:20:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net>`

```
On Aug 17, 7:15 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Derek Schrock wrote:
> > On Aug 12, 9:13 pm, Ken <klsha...@att.net> wrote:
…[97 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."


So the idea here is to find all instances of "string" plus the
context?

If so you could use grep's -n (assuming you have that option).  This
will print the line number along with the matched line.  Using this
information you could write a complementary awk program to pull the
context.

For instance:
[dereks@ircbsd ~]$ grep -n FILE foo.*
foo.c:19:    FILE* f = fopen( filename, "rb" );
...

We know that foo.c has reference to "FILE" on line 19.
With the awk script you would store old lines before and after line
19.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 4)_

- **From:** Ken <klshafer@att.net>
- **Date:** 2010-09-01T08:49:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a61d4cc-55e9-437d-8926-6f385b8e7d0e@y11g2000yqm.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com>`

```
On Sep 1, 9:20 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
> So the idea here is to find all instances of "string" plus the
…[16 more quoted lines elided]…
> - Show quoted text -

I've thought along similar lines. The CoBOL program already has line
numbers, so don't need the -n. It's been a few years since I wrote
some awk, so I'll have to refresh my memory a bit. But the strategy
should be fairly simple. For my purposes, the "context" need only be
the preceding five lines or so. (Also keep in mind that I need this
"context" _only_ for those lines that contain the target data-element
on a line all by itself, without a preceding "TO" on that same line,
because I can grep those lines already and have all the info I need.)

So use an array of size 5 say, and accumulate the "context" as I scan
the file, keeping only the five most recent line. Then look for the
regexp that matches an "isolated data-element" and print out the
preceding five lines and the current line.

As I said, my awk is rusty, but it would go something like this...

BEGIN {
       context[1]=""
       context[2]=""
       context[3]=""
       context[4]=""
       context[5]=""
      }
/^...... *,? *XFER-BLK-BOX-ACCOUNT *,? */ {print
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print context[1]
            print context[2]
            print context[3]
            print context[4]
            print context[5]
            print $0
           }
/./        {context[1]=context[2]
            context[2]=context[3]
            context[3]=context[4]
            context[4]=context[5]
            context[5]=$0
           }
END   {
       print "Done!"
      }

... which produces the result -

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
002200
00220003
002300 A-100-CLEAR-XFER-
FIELDS.                                         00230000
002400     MOVE SPACES TO XFER-GENERIC-SEGMENT-
KEYS,                    00240000
002500                    XFER-AFDC-ACCT-
ID,                            00250000
002600                    XFER-AFDC-
CASE,                               00260003
002700                    XFER-BLK-BOX-
ACCOUNT                          00270005
Done!

And I can immediately see, that yes, this is an occurrence where XFER-
BLK-BOX-ACCOUNT is a destination for a MOVE.

This brings me full circle to the original question, which is - is the
regexp /^...... *,? *XFER-BLK-BOX-ACCOUNT *,? */ for "XFER-BLK-BOX-
ACCOUNT alone on a line" optimally correct?

Ken
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 5)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-09-02T06:38:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<09fa73c7-aa30-47e6-b7ba-bb2b4accd8ef@v41g2000yqv.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com> <8a61d4cc-55e9-437d-8926-6f385b8e7d0e@y11g2000yqm.googlegroups.com>`

```
On Sep 1, 11:49 am, Ken <klsha...@att.net> wrote:
> On Sep 1, 9:20 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[89 more quoted lines elided]…
> Ken

The awk looks fine but the /./ isn't really needed:

awk '
{  #This action set will run on everyline
  #do something
}'

is the same as

awk '
/./ { #If the line has anything on it, every line has a '\n'
  #do something
}'

half dozen, six in the other...

I would have used grep's -n line number, awk's NF, and a larger buffer
once you found a match and read the buffer backwards until you match a
verb (MOVE, etc....).


As far as the regex goes it may match lines that you're not expecting:

/^...... *,? *XFER-BLK-BOX-ACCOUNT *,? */

Match conditions:
"^......" Line begins with any thing for the first six characters
#cobol lin num
" *" followed by any number of spaces
",?" followed by an optional comma
" *" followed by any number of spaces
"XFER-BLK-BOX-ACCOUNT" followed by the string "XFER-BLK-BOX-ACCOUNT"
" *" followed by any number of spaces
",?" followed by an optional comma
" *" followed by any number of spaces  #Here lies the issue


So the following lines for example:

123456          , XFER-BLK-BOX-ACCOUNT ,
....
164325         XFER-BLK-BOX-ACCOUNT
.....
654321         ,XFER-BLK-BOX-ACCOUNT  MORETEXTAFTER  #We don't want to
match this right?

If so the regex would change to require a read to the end of line:

/^...... *,? *XFER-BLK-BOX-ACCOUNT *,? *$/

Adding the '$' forces the read to the end of line changing the last
condition from the above list:

" *$" followed by any number of spaces to the end of line.  #Added for
"alone on a line"

There could be additional optimizations to the regex but I if it works
it works.
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 6)_

- **From:** Ken <klshafer@att.net>
- **Date:** 2010-09-02T09:01:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11cf1607-ee2e-4fd0-9b75-deca07dc5389@x25g2000yqj.googlegroups.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com> <8a61d4cc-55e9-437d-8926-6f385b8e7d0e@y11g2000yqm.googlegroups.com> <09fa73c7-aa30-47e6-b7ba-bb2b4accd8ef@v41g2000yqv.googlegroups.com>`

```
On Sep 2, 9:38 am, Derek Schrock <derekschr...@gmail.com> wrote:
> On Sep 1, 11:49 am, Ken <klsha...@att.net> wrote:
>
>
> The awk looks fine but the /./ isn't really needed:

Yeah, I figured that out later :-) - an example of something I knew
once, but had since forgot (my last awk programming was about 10 years
ago. I'm picking it up again...  hmmmmm.... later reading of the awk
man page shows me that "you do not need to declare awk variables and
you do not need to initialize them. The value of an unitialized
variable is the empty string..." - so I guess the BEGIN assignments
are also unneeded.
>
/>
> I would have used grep's -n line number, awk's NF, and a larger buffer
> once you found a match and read the buffer backwards until you match a
> verb (MOVE, etc....).

That's a good idea. What we're really doing then is scanning backwards
until we hit the beginning of the CoBOL "statement" (the verb),
instead of just an arbitrary number of lines.

>
> As far as the regex goes it may match lines that you're not expecting:
>
> /^...... *,? *XFER-BLK-BOX-ACCOUNT *,? */

Very true, in fact I tweaked the awk below to delete some of those
undesired lines...

>
> Match conditions:
> "^......" Line begins with any thing for the first six characters

It's usually a 6-digit line number, but sometimes it is spaces. I
guess I could use the [ 0-9] syntax. But again, I was kinda lazy. dot
(.) worked just fine :-).

> #cobol lin num
> " *" followed by any number of spaces
…[24 more quoted lines elided]…
> "alone on a line"

Yes, you are touching on some stuff I encountered. In fact, in another
iteration I had experimented with -
"^...... *,? *XFER-BLK-BOX-ACCOUNT *[,.]* *[0-9]*$"

(where I had the trailing [0-9] because there are also line numbers in
73-80)

However, in considering...
> 654321         ,XFER-BLK-BOX-ACCOUNT  MORETEXTAFTER  #We don't want to
> match this right?
I did want to show up the following:
123456           ,XFER-BLK-BOX-ACCOUNT, SOME-OTHR-DATA-ELT,
12345678

so that's why I backed off from trying to match all the way to the end-
of-line $.

>
> There could be additional optimizations to the regex but I if it works
> it works.-

That's what I really, really like about grep and awk. Can tinker to my
heart's delight with nearly instantaneous feedback and fine-tune to
focus in on what I am looking for.

My latest versions - wrap in a tiny shell script, and do some glob'ing
on *.cpy...

context.ksh:
echo "Running awk to scan for isolated XFER-BLK-BOX-ACCOUNT, -ACCT-NUM
lines..."
awk -f context.awk *.cpy >context.txt
echo "context.txt contains the isolated lines in context."
echo "Done!"

Then modify the awk script to delete the unnecessary BEGIN section,
look for both XFER-BLK-BOX-ACCOUNT and redefined alias XFER-BLK-BOX-
ACCT-NUM, and print out the file name that contains the hit (now
necessary because we are glob'ing). Add a couple tweaks to suppress
false hits like PIC lines in Working-Storage and <, >, + comparisons,
so the following works pretty well:

context.awk:
/^...... *,? *XFER-BLK-BOX-ACCOUNT *,? */ {
            hits = match($0,/ PIC /) + match($0,/[<>=]/)
            if (hits == 0) {
                print
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                print FILENAME, ":", context[1]
                print FILENAME, ":", context[2]
                print FILENAME, ":", context[3]
                print FILENAME, ":", context[4]
                print FILENAME, ":", context[5]
                print FILENAME, ":", $0
                }
           }
/^...... *,? *XFER-BLK-BOX-ACCT-NUM *,? */ {
            hits = match($0,/ PIC /) + match($0,/[<>=]/)
            if (hits == 0) {
                print
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                print FILENAME, ":", context[1]
                print FILENAME, ":", context[2]
                print FILENAME, ":", context[3]
                print FILENAME, ":", context[4]
                print FILENAME, ":", context[5]
                print FILENAME, ":", $0
                }
           }
           {context[1]=context[2]
            context[2]=context[3]
            context[3]=context[4]
            context[4]=context[5]
            context[5]=$0
           }

Thanks for you feedback.

Ken
```

###### ↳ ↳ ↳ Re: grep'ing CoBOL source

_(reply depth: 4)_

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2010-09-02T17:33:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N7OdneEHU52nux3RnZ2dnUVZ_tadnZ2d@giganews.com>`
- **References:** `<098a698a-a3da-4e55-b6b5-12a58ee646f9@d8g2000yqf.googlegroups.com> <f676deda-3d7e-4157-95ca-d74902256a2c@5g2000yqz.googlegroups.com> <8cv9ahFa0uU1@mid.individual.net> <0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com>`

```

"Derek Schrock" <derekschrock@gmail.com> wrote in message 
news:0848dc74-354f-431c-b4c6-f0b97daf8e07@d8g2000yqf.googlegroups.com...
On Aug 17, 7:15 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Derek Schrock wrote:
> > On Aug 12, 9:13 pm, Ken <klsha...@att.net> wrote:
…[13 more quoted lines elided]…
> >> same line as element-4? OK, you know I'm not talking what is
...

>So the idea here is to find all instances of "string" plus the
>context?

>If so you could use grep's -n (assuming you have that option).  This
>will print the line number along with the matched line.  Using this
>information you could write a complementary awk program to pull the
>context.

The SD Source Code Search engine will let you code various searches
in terms of (COBOL) langauge elements rather than characters.

Specifically for the issue
discussed here, you can tell it to capture K lines of context;
the search log file will then contain the the actual hits and K lines
before and after the hit.   No messing with awk needed.
www.semanticdesigns.com/Products/SearchEngine


-- IDB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
