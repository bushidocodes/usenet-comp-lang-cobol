[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# newbie question on cobol syntax

_297 messages · 17 participants · 2007-04 → 2007-05_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### newbie question on cobol syntax

- **From:** Mayer <mayer.goldberg@gmail.com>
- **Date:** 2007-04-22T13:02:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
Hello:

I noticed two styles of cobol syntax:

main.
    display "hello"
    display "goodbye"
    stop run
    .

vs.

main.
    display "hello".
    display "goodbye".
    stop run.

Some books use the first, others the second. I have no idea what's the
difference between them, but I note the following:

- MF Cobol/DOS allows both

- RM Cobol/DOS allows only the second, i.e., requires a period at the
end of each statement.

Can someone please explain to me the function of the period in cobol,
what is the basis for the difference in syntax, and what is
recommended.

Thanks,

Mayer
```

#### ↳ Re: newbie question on cobol syntax

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-22T21:48:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0gl7k$p4d$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
In article <1177272149.938765.13260@o5g2000hsb.googlegroups.com>,
Mayer  <mayer.goldberg@gmail.com> wrote:
>Hello:

[snip]

>Can someone please explain to me the function of the period in cobol,
>what is the basis for the difference in syntax, and what is
>recommended.

To work backwards... what is recommended is starting with the style of 
code on your job-site (or learning what your instructor instructs you to 
do), there is no 'the basis' but, quite possibly, a few different bases 
and the function of the period is what, for the most part, what The Manual 
says it to be.

(Even the term used to define this particular bit of punctuation varies 
from one group to the next; some adherents to a primitive language which 
serves as a basis for a bit of what Americans speak will insist on using 
two words ('full stop') to describe it, rather than the one ('period') 
which can be found in citations as early as the seventeenth century... 
their reasons for doing this are still unknown but they are, at times, 
*most* insistent.)

DD
```

##### ↳ ↳ Re: newbie question on cobol syntax

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-22T23:44:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JrSWh.116487$aG1.66743@pd7urf3no>`
- **In-Reply-To:** `<f0gl7k$p4d$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0gl7k$p4d$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <1177272149.938765.13260@o5g2000hsb.googlegroups.com>,
> Mayer  <mayer.goldberg@gmail.com> wrote:
…[27 more quoted lines elided]…
> 
Very insistent, us folks from the 'Mother country'. Not sure of origins, 
but in days of telegrams :-

'WILL BE LEAVING BY FLIGHT AC 124. STOP. PLANE ARRIVES CALGARY 13.05 
LOCAL TIME. STOP'.

Same sort of thing using teleprinters in military to send signals :-

'FROM C-IN-C MEAF TO AOC-IN-C IRAQ. STOP. FOR UK EYES ONLY. STOP. YOUR 
A12345 12 SEPTEMBER 1954. STOP. GOD HELP US WHEN THE YANKS TAKE OVER. STOP.'

For your edification, something else which amuses North Americans, "If 
you like I'll knock you up". NOT to be translated as, "If you like I'll 
leave a bun in your oven".

Saw the latter's origins on TV. Back in yon days of the Industrial 
Revolution and the 'dark Satanic Mills', when the poor sods, 
disenfranchised from their farms worked in the grimy mills starting work 
  at 05:00 or 06:00 so the mill owner could save on lighting. It takes 
me all my effort to be awake by 08:00, so they had a similar problem 
with their times too.

For about a penny per week/month each household would pay somebody to 
knock them up. This man went down the rows of dingy terraced houses with 
a long stick and tapped(knocked) at the window immediately above the 
front door.

Another interesting one from TV. Do you know the origins of 'freelance' ?

BTW - Afterthought. You refer to hiring agencies as those 'pimps' Don't 
disagree with your conclusion/description. However, if a pimp is trying 
to gain you useful paid employment does that make you an whore (or in 
line with Imus an 'ho') ?

Jimmy
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-23T09:30:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0huc7$a4g$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0gl7k$p4d$1@reader2.panix.com> <JrSWh.116487$aG1.66743@pd7urf3no>`

```
In article <JrSWh.116487$aG1.66743@pd7urf3no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:
>docdwarf@panix.com wrote:
>> In article <1177272149.938765.13260@o5g2000hsb.googlegroups.com>,
…[8 more quoted lines elided]…
>>>recommended.

[snip]

>> (Even the term used to define this particular bit of punctuation varies 
>> from one group to the next; some adherents to a primitive language which 
…[6 more quoted lines elided]…
>Very insistent, us folks from the 'Mother country'.

Yes, quite insistent... and the reasons, as noted above, are still 
unknown.  Time passes, terminologies change - not much talk of women 
having 'the vapors', is there? - and yet this particular bit still rolls 
on.

>Not sure of origins, 
>but in days of telegrams :-
>
>'WILL BE LEAVING BY FLIGHT AC 124. STOP. PLANE ARRIVES CALGARY 13.05 
>LOCAL TIME. STOP'.

See above and the OED, Mr Gavan... the use Americans make is first cited 
in 1609, not too many telegrams back then.

(note to Mr Goldberg - this was pointed out to this newsgroup a half-dozen 
years ago, see 
<http://groups.google.com/group/comp.lang.cobol/msg/f5a18356c2cad15b?dmode=source>

>
>Same sort of thing using teleprinters in military to send signals :-
>
>'FROM C-IN-C MEAF TO AOC-IN-C IRAQ. STOP. FOR UK EYES ONLY. STOP. YOUR 
>A12345 12 SEPTEMBER 1954. STOP. GOD HELP US WHEN THE YANKS TAKE OVER. STOP.'

See above, Mr Gavan... teleprinters postdate telegrams (shouldn't that be 
'telegrammes'?) and both postdate Davies' used in the early seventeenth 
century by a goodly time.

[snip]

>Another interesting one from TV. Do you know the origins of 'freelance' ?

Off the top of my head I'd say it might be related to samurai traditions.

>
>BTW - Afterthought. You refer to hiring agencies as those 'pimps' Don't 
>disagree with your conclusion/description. However, if a pimp is trying 
>to gain you useful paid employment does that make you an whore (or in 
>line with Imus an 'ho') ?

No more than one is trying to change one's hat-size by visiting a 
'headshrinker' or expecting an amputation from one's annual visit to the 
'sawbones', Mr Gavan.

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-23T08:07:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177340839.047930.275980@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<f0huc7$a4g$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0gl7k$p4d$1@reader2.panix.com> <JrSWh.116487$aG1.66743@pd7urf3no> <f0huc7$a4g$1@reader2.panix.com>`

```
On 23 Apr, 10:30, docdw...@panix.com () wrote:
> In article <JrSWh.116487$aG1.66743@pd7urf3no>,
> James J. Gavan <jgavandeletet...@shaw.ca> wrote:
…[4 more quoted lines elided]…
>

I'll be brief as I'm suffering another migraine. From Wikipedia:

"A freelancer or freelance worker is a person who pursues a profession
without a long-term commitment to any one employer. The term was first
coined by Sir Walter Scott (1771-1832) in his well-known historical
romance Ivanhoe to describe a "medieval mercenary warrior." "

also:

"However, many Asian countries appear to follow Hormung by holding low
regard for freelancers, often associating the practice with personal
failure (an inability to find work with a major employer) and even
criminality (see: Ninja)."
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-23T15:23:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0ij22$h4l$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <JrSWh.116487$aG1.66743@pd7urf3no> <f0huc7$a4g$1@reader2.panix.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com>`

```
In article <1177340839.047930.275980@o5g2000hsb.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 23 Apr, 10:30, docdw...@panix.com () wrote:
>> In article <JrSWh.116487$aG1.66743@pd7urf3no>,
…[10 more quoted lines elided]…
>without a long-term commitment to any one employer.

Compare and contrast with the 'masterless samurai', or ronin... and please 
pardon my obscurity.

L Silberstein, A'83
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-23T10:27:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177349271.353717.85480@d57g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<f0ij22$h4l$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <JrSWh.116487$aG1.66743@pd7urf3no> <f0huc7$a4g$1@reader2.panix.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com> <f0ij22$h4l$1@reader2.panix.com>`

```
On 23 Apr, 16:23, docdw...@panix.com () wrote:
> In article <1177340839.047930.275...@o5g2000hsb.googlegroups.com>,
>
…[17 more quoted lines elided]…
> L Silberstein, A'83

Pardon - no. So obscure that I gave up before getting hit by another
migraine. However, I didi find this little gem on Amazon:

'83,000 Square Miles, Kansas Day Trips: No Lines No Waiting' by Steve
Harper.

And all for less than US$8. Apologies to those who live/work in Kansas.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-24T01:04:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QIcXh.121335$6m4.48978@pd7urf1no>`
- **In-Reply-To:** `<1177340839.047930.275980@o5g2000hsb.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0gl7k$p4d$1@reader2.panix.com> <JrSWh.116487$aG1.66743@pd7urf3no> <f0huc7$a4g$1@reader2.panix.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com>`

```
Alistair wrote:
> On 23 Apr, 10:30, docdw...@panix.com () wrote:
> 
…[10 more quoted lines elided]…
> I'll be brief as I'm suffering another migraine. From Wikipedia:

The idea was to get the dwarf to do his own homework.
> 
> "A freelancer or freelance worker is a person who pursues a profession
…[10 more quoted lines elided]…
> 
Interesting about Sir Walter, and the reference to Ivanhoe, (Robin Hood, 
King Richard and his nasty brother John), seems to put it in the right 
period, late 1100s and early 1200s.

But not quite what I saw as an explanation on TV. Can't recall the 
programme name, but English and the regular commentator had a somewhat 
cockney accent. The series covered battles but primarily the techniques 
of weaponry. (Not to be confused with that excellent series 'Battle' or 
'Battlefield' - Sir Peter Snow (????), former ITV anchor and his son. 
Using computer graphics for terrain layouts, they concentrated on the 
game plan for specific battles).

Briefly it appears it dates approximately to late 1100s to say 1400s, 
though we know jousting continued on through the early Tudors. 'In days 
of old when young men were bold' those with the money had ambitions to 
become knights, and suited up, jousted with LANCES for a fair maiden's 
hand. A fairly expensive 'sport' to enter, and as an extension they 
would serve monarchs to gain the honour of glory, such as the Crusades.

I can't recall exactly but he specifically mentioned German lancers. 
Like everything else there is always the factor of supply and demand, so 
sometimes they were needed and other times there weren't opportunities 
to demonstrate their skills. These FREE LANCERS offered their military 
know-how to the first comer who was prepared to pay them. As the 
Wikipedia entry says, they were the first 'mercenaries'.

Above is not contradicting the Wikipedia, but does seem to spell it out 
more clearly.

Hope your migraine goes real quick. I'm one of the fortunate ones; I 
have never had a single headache in my life.

Jimmy
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-24T11:01:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177437689.189719.73750@o40g2000prh.googlegroups.com>`
- **In-Reply-To:** `<QIcXh.121335$6m4.48978@pd7urf1no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0gl7k$p4d$1@reader2.panix.com> <JrSWh.116487$aG1.66743@pd7urf3no> <f0huc7$a4g$1@reader2.panix.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com> <QIcXh.121335$6m4.48978@pd7urf1no>`

```
On 24 Apr, 02:04, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Alistair wrote:
> > On 23 Apr, 10:30, docdw...@panix.com () wrote:
…[10 more quoted lines elided]…
> The idea was to get the dwarf to do his own homework.


:-(    sorry. I should have read between the lines (but people keep
telling me off for that).



>
>
…[6 more quoted lines elided]…
> game plan for specific battles).

I recall a small military bloke (Richard ?) giving lectures on major
battles (Agincourt, Waterloo, Trafalgar - all the ones that the French
prefer to forget) and some poor ones done by Peter Snow (you can catch
them on UK TV History on satellite) and his son. I thought PSnow's
were cheap tricks to catch the attention of casual browsers.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-24T18:08:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0lh3e$rop$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com> <QIcXh.121335$6m4.48978@pd7urf1no> <1177437689.189719.73750@o40g2000prh.googlegroups.com>`

```
In article <1177437689.189719.73750@o40g2000prh.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 24 Apr, 02:04, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
>> Alistair wrote:
…[14 more quoted lines elided]…
>telling me off for that).

Eh?  Now I'm confused.  A freelancer is one whose services are not bound 
to a lord, a ronin is a samurai is one whose services are not bound a 
lord... this was the relation I saw when I made my comment and in case I 
haven't already then permit me to offer my apologies for my obscurity but 
I'm uncertain what homework was seen as necessary.

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-26T08:35:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177601738.038399.20870@b40g2000prd.googlegroups.com>`
- **In-Reply-To:** `<f0lh3e$rop$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1177340839.047930.275980@o5g2000hsb.googlegroups.com> <QIcXh.121335$6m4.48978@pd7urf1no> <1177437689.189719.73750@o40g2000prh.googlegroups.com> <f0lh3e$rop$1@reader2.panix.com>`

```
On 24 Apr, 19:08, docdw...@panix.com () wrote:
> In article <1177437689.189719.73...@o40g2000prh.googlegroups.com>,
>
…[31 more quoted lines elided]…
> - Show quoted text -

Now I understand the reference to Samurai (or Ronin). Now explain the
L Silberstein reference please as trawling through Alta Vista gave me
another headache and nothing useful withing the first 30 references.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-26T16:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0qijg$e1r$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1177437689.189719.73750@o40g2000prh.googlegroups.com> <f0lh3e$rop$1@reader2.panix.com> <1177601738.038399.20870@b40g2000prd.googlegroups.com>`

```
In article <1177601738.038399.20870@b40g2000prd.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 24 Apr, 19:08, docdw...@panix.com () wrote:
>> Eh?  Now I'm confused.  A freelancer is one whose services are not bound
…[11 more quoted lines elided]…
>another headache and nothing useful withing the first 30 references.

Gah... it's what happens when you let someone else use your account 'just 
for a moment, to check email' and they leave behind references to 
something you'd been discussing about relativity by email.

DD
```

#### ↳ Re: newbie question on cobol syntax

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-22T22:24:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qgRWh.115821$6m4.100182@pd7urf1no>`
- **In-Reply-To:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
Mayer wrote:
> Hello:
> 
…[30 more quoted lines elided]…
> 
Well first off - if you can, avoid using both compilers - you will get
yourself in one hell of a mess :-)

Are you sure about RM/COBOL being adamant about periods/full-stops, or
is it perhaps what you interpreted ? The following extract from a very
old RM compiler, Version 2 and no longer supported :-

--------------------------------------------------------------------------

        B040-ENTER-ID.

             ACCEPT WS-SCREEN-PROGRAM, POSITION 40, LINE 15,
             PROMPT "-", ECHO, CONVERT, REVERSE, NO BEEP
             ACCEPT WS-SCREEN-PAGE, POSITION 43, LINE 15,
             PROMPT "-", ECHO, CONVERT, REVERSE, NO BEEP

             IF  WS-SCREEN-PROGRAM = ZEROES
                 MOVE "Are you sure - Program Zero ? y/n"
                 TO WS-INSTRUCTION-TEXT
                 MOVE SPACES TO WS-INSTRUCTION-EXIT
                 PERFORM Z040-INSTRUCTION-LINE
                 PERFORM Z025-ANSWER

                 IF      WS-ANSWER = "N"
                         GO TO B040-ENTER-ID.

             IF  WS-SCREEN-PAGE = ZEROES
                 MOVE "Screen ID can't be zeroes"
                 TO WS-ERROR-MESSAGE-TEXT
                 PERFORM Z050-ERROR-MESSAGE
                 GO TO B040-ENTER-ID.

             IF          WS-SELECTION NOT = 2
                         MOVE ZEROES TO WS-LINE-ID

             ELSE        PERFORM  B050-LINE-ID.

        B050-LINE-ID.

             ACCEPT      WS-LINE-ID, POSITION 45, LINE 15,
                         PROMPT "-", ECHO, CONVERT, REVERSE, NO BEEP

                 IF      WS-LINE-ID = ZEROES
                         MOVE "Line ID can't be zeroes"
                         TO WS-ERROR-MESSAGE-TEXT
                         PERFORM Z050-ERROR-MESSAGE
                         GO TO B050-LINE-ID.

        C010-RECORD.

             IF          WS-SELECTION = 1
                         MOVE 3 TO WS-NUMBER-OF-QUESTION
                         PERFORM C020-DISPLAY-SCREEN
                         PERFORM C030-READ-RECORD

             ELSE        MOVE 4 TO WS-NUMBER-OF-QUESTION
                         PERFORM D020-DISPLAY-SCREEN
                         PERFORM C030-READ-RECORD.

             IF  WS-RECORD-EXISTS = "Y"

                 IF      WS-SELECTION = 1
                         PERFORM C040-DISPLAY-VALUES

                 ELSE    PERFORM D040-DISPLAY-VALUES.

             IF  WS-RECORD-EXISTS = "N"
                         MOVE
                         "No record - do you want to input ? y/n"
                         TO WS-INSTRUCTION-TEXT
                         MOVE SPACES TO WS-INSTRUCTION-EXIT
                         PERFORM Z040-INSTRUCTION-LINE
                         PERFORM Z025-ANSWER

                    IF   WS-ANSWER = "Y"
                         PERFORM C060-ENTER-NEW-DATA

                    ELSE GO TO C010-EXIT.

                 PERFORM C070-LINE-NUMBER THROUGH C070-EXIT.

000000 C010-EXIT.
                 EXIT.
---------------------------------------------------------------------------------------

If you look at the above code your compiler should certainly hiccup if
you leave out the very last period/full-stop before the next paragraph
name. If you have perform PARAGRAPH-NAME-A and the para-name isn't
preceded by a period, you should get an error like "Invalid Paragraph Name".

I tried searching the latest version of Net Express for "period", "full
stop" - no luck. Familiarize yourself with END SCOPE Terminators - which
weren't around when I wrote the above code.

In written English we finalize our thoughts by putting a period at the
end of a sentence. We group a series of like sentences into a paragraph
and terminate that with a CR/LF(Carriage-Return, Line Feed), have a
blank line and start a new paragraph on the next line.

Translate that to COBOL - using Scope Terminators, mainly you only need
a period preceding the next 'heading' Section, Paragraph-Name etc.

Let's take the very last sequence above and show how it could be edited
to operate with scope terminators "-

             IF (#1) WS-RECORD-EXISTS = "N"
                         MOVE
                         "No record - do you want to input ? y/n"
                         TO WS-INSTRUCTION-TEXT
                         MOVE SPACES TO WS-INSTRUCTION-EXIT
                         PERFORM Z040-INSTRUCTION-LINE
                         PERFORM Z025-ANSWER

                    IF (#2)  WS-ANSWER = "Y"
                         PERFORM C060-ENTER-NEW-DATA

                    ELSE (#2) GO TO C010-EXIT
---->		 don't need the period here replaced by following end-if

---->		   END-IF (#2)

---->      END-IF (#1)

                 PERFORM C070-LINE-NUMBER THROUGH C070-EXIT.

---->       If I didn't have the line 'PERFORM C070-LINE...." nor the
two lines for C010-EXIT, then a period would be required after the final
'END-IF', denoting the end of the current paragraph.


000000 C010-EXIT.
                 EXIT.

Note the two 'IF' s are paired off with an END-IF and we don't need any
intervening periods. (Scope Terminators are the equivalent of something
being finished with a period).

Not a very expansive explanation but if you are saying that RM/COBOL is
rejecting the following, then it might be useful to post the full source
that you are getting errors for, plus the error messasges in the 
following :-

> main.
>     display "hello"
>     display "goodbye"
>     stop run
>     .

Just a thought, it's so long ago. Doesn't 'old' RM require something like :-

MAIN-SECTION.
FIRST-PARAGRAPH.		?????????

display "hello"
display "goodbye"
stop run
.

And 'Yes' you DEFINITELY need that period after STOP RUN :-)

Jimmy
```

##### ↳ ↳ Re: newbie question on cobol syntax

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-22T23:00:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JORWh.115853$6m4.94294@pd7urf1no>`
- **In-Reply-To:** `<qgRWh.115821$6m4.100182@pd7urf1no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <qgRWh.115821$6m4.100182@pd7urf1no>`

```
James J. Gavan wrote:
> Mayer wrote:
> <snip>

> Not a very expansive explanation but if you are saying that RM/COBOL is
> rejecting the following, then it might be useful to post the full source
…[20 more quoted lines elided]…
> 
Mayer,

Pretty dumb of me - I should have checked the beginning of the program I 
extracted from :-

-----------------------------------------------------------------------
000340     COPY    "\USR\CS\TEXT2\CSWSCOMM.CBL".

000670 PROCEDURE DIVISION
000680
000340     COPY    "\USR\CS\TEXT2\CSERROR.CBL".
000710
000720 A010-MAIN-LINE SECTION.
000730 A010-BEGIN.
000740
                 IF      WS-LABEL-CHECK NOT = "QQ"
                         STOP RUN

                 ELSE    MOVE WS-PROGRAM-TITLE TO WS-SCREEN-TITLE
                         PERFORM X010-OPEN-FILES.

        A010-NEXT.
----------------------------------------------------------------------

I think your problem with RM/COBOL will be resolved if you have :-

PROCEDURE DIVISION.
A010-MAIN-LINE SECTION.
A010-BEGIN (or MAIN-PARAGRAPH if you like).

Micro Focus compilers allow you to take 'shortcuts'.

Jimmy
```

#### ↳ Re: newbie question on cobol syntax

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-22T23:52:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KySWh.3317$ff2.277@fe08.news.easynews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
I am surprised by your statement that RM had a problem with the first example - 
but it may depend upon the context of the entire COBOL program. (What message 
does it give you?)

As far as the Procedure Division goes (different rules for other divisions). 
There are requirements that:

 A) every procedure-name (header) - paragraph or section name MUST be terminated 
by a period (full-stop).

 B) There must be a period (full-stop) at the end of each set of procedure 
division statements that constitute a procedure, i.e. each paragraph or section 
(terminated by another paragraph or section name - or by the end of source 
code - or End Program header).

 There is a SEMANTIC difference for periods.  They end SENTENCES.  This is where 
a NEXT SENTENCE phrase (or statement - if your compiler has such a statement as 
an extension - as Micro Focus does) will "go to".  For example.

  If Field-1 = A
      Next Sentence
 Else
     Display  "Here"
     .
    Display "There"
    .

Gets very different results from

  If Field-1 = A
      Next Sentence
 Else
     Display  "Here"
    Display "There"
      .

As far as WHERE you place the period (same line or next) this should make no 
difference. HOWEVER, your compiler may follow rules about A-margin/B-Margin (and 
columns 1-6).   So you need to understand these (if your compiler cares).

P.S.  And YES  a "Continue" is a very different thing than a "Next Sentence" - 
if your compiler allows them both to be used in the same place.
```

##### ↳ ↳ Re: newbie question on cobol syntax

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-23T08:50:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com>`

```
On Sun, 22 Apr 2007 23:52:11 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

> There is a SEMANTIC difference for periods.  They end SENTENCES.  This is where 
>a NEXT SENTENCE phrase (or statement - if your compiler has such a statement as 
…[17 more quoted lines elided]…
>      .

Some compilers will allow

If Field-1 = A
     Next Sentence
Else
     Display "Here"
End-IF

Display "There".

In which case "Next Sentence" still goes to the next sentence.    I
see no advantage in ever using NEXT SENTENCE now that CONTINUE is
available.

Some pre-compilers create implicit IF statements without creating
END-IF statements.   In these special cases, a style of including
full-stop periods can be beneficial.     But in other cases, the
Righteous arguments for one style over another are more of a religious
nature.

And it is easy to see what Righteous people inflict on the world.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-23T15:30:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0ijf7$9ig$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com>`

```
In article <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>I see no advantage in ever using NEXT SENTENCE now that CONTINUE is
>available.

I'm not sure how you intend 'using' to be interpreted here, Mr Brazee... 
but I've run across a bit of the 'installed base' that requires NEXT 
SENTENCE to be compiled and executed in the same manner as it was when the 
code was first written in FCOBOL.

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-23T15:38:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <f0ijf7$9ig$1@reader2.panix.com>`

```
Actually,
   If you have code that compiled with "FCOBOL" - or even with OS/VS COBOL and 
you NOW are using the newer (IBM) compilers, then changing every NEXT SENTENCE 
to CONTINUE should never change the logic flow.

The only time that there is a "difference in logic flow" is when you MIX old 
COBOL (with NEXT SENTENCE) *with* scope terminators (END-IF or whatever). 
Therefore, if you are worried about "base of code" BUT are using newer compiler, 
then feel "safe" in changing NEXT SENTENCE to CONTINUE.

Of course as "your - not my - sainted mother" is reported to have said <G> such 
changes are rarely requested by those who sign your paychecks.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-23T09:52:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oblp23l3pfiv81qcgfbkcero4l47jqr0p5@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <f0ijf7$9ig$1@reader2.panix.com> <Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>`

```
On Mon, 23 Apr 2007 15:38:17 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>The only time that there is a "difference in logic flow" is when you MIX old 
>COBOL (with NEXT SENTENCE) *with* scope terminators (END-IF or whatever). 
>Therefore, if you are worried about "base of code" BUT are using newer compiler, 
>then feel "safe" in changing NEXT SENTENCE to CONTINUE.

Since my compiler allows such mixing - a bit of thinking is necessary
before such conversion.

Another place where CONTINUE is useful is replacing the exit command.
This facilitates the "D" in column 6 for debugging:

 2000-READ-EXIT.
      EXIT.

vs.
  2000-READ-EXIT.
D      DISPLAY "reached end of read paragraph".
        CONTINUE.


My new code doesn't contain exit paragraphs, but when I maintain, I
try not to rewrite.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-23T16:55:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0iode$6sc$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <f0ijf7$9ig$1@reader2.panix.com> <Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>`

```
In article <Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Actually,
>   If you have code that compiled with "FCOBOL" - or even with OS/VS COBOL and 
…[4 more quoted lines elided]…
>COBOL (with NEXT SENTENCE) *with* scope terminators (END-IF or whatever). 

Bingo, Mr Klein... code that has been around that long has, in my 
experience, been through a few hands of vary levels of capability; styles 
are mixed and stability, at times, a wee bit... precarious.

>Therefore, if you are worried about "base of code" BUT are using newer
>compiler, 
>then feel "safe" in changing NEXT SENTENCE to CONTINUE.

I've felt safe about things which the Testing Crew grew a bit... upset 
about.  Increasing the number of code changes, or so I have seen, 
increases the size of the Test Plan and the amount of time folks spend 
dealing with it.

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-24T00:20:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93cXh.120694$6m4.113430@pd7urf1no>`
- **In-Reply-To:** `<Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <f0ijf7$9ig$1@reader2.panix.com> <Ip4Xh.81928$OL2.22938@fe04.news.easynews.com>`

```
William M. Klein wrote:
> Actually,
>    If you have code that compiled with "FCOBOL" - or even with OS/VS COBOL and 
…[10 more quoted lines elided]…
> 
Seeing as you brought up his 'sainted mother', note how we are moving 
further back through his family tree, the latest being, I think,  "My 
sainted Maternal Grandfather, may he sleep with the angels, ........".

Given a choice, I would have thought that his Maternal Grandfather would 
have preferred to sleep with his Maternal Grandmother rather than the 
angels. However, if Heaven is all it is cracked up to be, his Maternal 
Grandfather might possibly like a shot at sleeping with his Paternal 
Grandmother, and then he would be laying back in the puff-ball clouds 
with a smile on his lips, like the cat that got the cream..

Jimmy
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-24T00:47:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0jk2p$mnd$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <f0ijf7$9ig$1@reader2.panix.com> <Ip4Xh.81928$OL2.22938@fe04.news.easynews.com> <93cXh.120694$6m4.113430@pd7urf1no>`

```
In article <93cXh.120694$6m4.113430@pd7urf1no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:

[snip]

>Seeing as you brought up his 'sainted mother', note how we are moving 
>further back through his family tree, the latest being, I think,  "My 
>sainted Maternal Grandfather, may he sleep with the angels, ........".

Wonderful thing, this WorldWide Web... according to 
<http://groups.google.com/group/comp.lang.cobol/msg/7608963489ff17d9?dmode=source 
I last mentioned my Sainted Paternal Grandfather on 15 Apr 2007 and my 
Sainted Maternal Grandfather... never.

(this might have something to do with the fact that my parents neglected 
even to conceive of conceiving me until a decade-and-some-good-change had 
passed since his shuffling off this mortal coil... my Sainted Maternal 
Grandfather - may he sleep with the angels! - as a result of at least 
these circumstances, if not others, and I had fewer chances for first-hand 
experience of each other)

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-23T15:34:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cm4Xh.9184$9i2.4154@fe06.news.easynews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com...
> On Sun, 22 Apr 2007 23:52:11 GMT, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
<snip>

> Some compilers will allow
>
…[11 more quoted lines elided]…
>

Howard,
  I know that you know this, but just in case some "newbie" (see subject line 
doesn't) this is the reason that understanding Next Sentence vs Continue is 
importaat (if your compiler supports this extension).

 If Field-1 = A
     Next Sentence
 Else
     Display "Here"
 End-IF
 Display "There"
   .
 Display "Some Place Else
    .
 Display "Still another logic branch
   .

yields different results from

      If Field-1 = A
          Next Sentence
      Else
          Display "Here"
      End-IF
       Display "There"
  *  no period
     Display "Some Place Else
    .
     Display "Still another logic branch
       .

And neither of the above is the same as

      If Field-1 = A
          Continue
      Else
          Display "Here"
      End-IF
      Display "There"
          .
     Display "Some Place Else
    .
     Display "Still another logic branch
       .

* * * * *

As most people (but not all) agre, "mixing" next sentence with scope delimiters 
is NOT a good thing to do.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-23T09:58:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com>`

```
On Mon, 23 Apr 2007 15:34:58 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>As most people (but not all) agre, "mixing" next sentence with scope delimiters 
>is NOT a good thing to do.

I've heard of, but haven't come across code that used "next sentence"
to work as "exit paragraph".

paragraph-a.
    if my-account = "zzzz" 
         next sentence
    end-if
    perform a
    perform b
    perform c
	.
paragraph-b.

I don't care for this myself.   CoBOL should be clear and should avoid
"tricks" wherever possible.


Eschew obfuscation.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-04-23T12:23:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177356217.808102.76680@d57g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com>`

```
On Apr 24, 3:58 am, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 23 Apr 2007 15:34:58 GMT, "William M. Klein"
>
…[18 more quoted lines elided]…
> "tricks" wherever possible.

It does. That is, the Cobol standard does avoid such tricks and
specifies that the above does not comply. It is only some vendors that
allow such tricks.

Actually another 'trick' with MF is to put an OLDNEXTSENTENCE
directive in the site defaults then the above 'trick' fails to work
causing much confusion and hilarity.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-23T20:20:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com>`
- **In-Reply-To:** `<1177356217.808102.76680@d57g2000hsg.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com>`

```
Richard wrote:
> On Apr 24, 3:58 am, Howard Brazee <how...@brazee.net> wrote:
>> I've heard of, but haven't come across code that used "next sentence"
…[17 more quoted lines elided]…
> allow such tricks.

I was thinking that it was forbidden per the standard.  I guess I 
haven't been out of the scene for that long...  :)
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-24T03:12:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PAeXh.75234$mJ2.62275@fe10.news.easynews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com>`

```
The Standard doesn't allow a NEXT SENTENCE with an END-IF (at the same level, so 
this is "non-Standard".  However, a number of vendors allow this (as a 
documented extension).
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-24T08:45:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com>`

```
On Mon, 23 Apr 2007 20:20:50 -0600, LX-i <lxi0007@netscape.net> wrote:

>> It does. That is, the Cobol standard does avoid such tricks and
>> specifies that the above does not comply. It is only some vendors that
…[3 more quoted lines elided]…
>haven't been out of the scene for that long...  :)

Which is why in my first message of the thread mentioning this
possibility, I said:

>Some compilers will allow
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 8)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-24T19:08:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com>`
- **In-Reply-To:** `<1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 23 Apr 2007 20:20:50 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[9 more quoted lines elided]…
>> Some compilers will allow

I remember - but I also remember thinking, then, that telling a newbie 
about a dangerous feature allowed by some compilers, might not have been 
the best direction to take the conversation.  (Kind of like telling 
someone to overrun their table index if they needed more memory - sure, 
it'll work, but it's not the right way to do it.)

But, it wasn't my conversation, so I stayed out...  :)  Today, I was 
coding away at my new Java job, and found myself creating a setter method...

public void setDescription(final String psDescription) {
     move psDescription to msDescription
}

I got to the "c" in "msDescription" and realized what I was doing!  Oops...
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-25T16:45:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5984nrF2jrmikU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com...
> Howard Brazee wrote:
>> On Mon, 23 Apr 2007 20:20:50 -0600, LX-i <lxi0007@netscape.net> wrote:
…[28 more quoted lines elided]…
>

Wait 'til you start writing (in COBOL...)

wsvalue = ws-number.ToString();     :-)

It took me about two weeks of intensive coding in C# before I stopped making 
the kind of error you describe...

These days it doesn't happen... :-)


Pete.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-25T19:41:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com>`
- **In-Reply-To:** `<5984nrF2jrmikU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com...
…[18 more quoted lines elided]…
> the kind of error you describe...

So far, it hadn't happened.  Of course, I'm just starting to get into 
the meat of it.  Between Java and C#, though, I'd have to say I prefer 
C#'s syntax, especially when it comes to properties.

Our system uses Apache, Struts, and Velocity, along with Java and 
Oracle.  I like the way it's laid out, but there are a lot of different 
pieces in different places.  I'm beginning to understand MVC, but it 
seems that C# is a little more straightforward in that as well.

> These days it doesn't happen... :-)

So there's hope for me yet - cool!  (Of course, this will probably be my 
last "hands in the code" assignment, especially if I make E-7.  That'll 
put me into management at that point.)
```

###### ↳ ↳ ↳ OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 11)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-26T22:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Js9Yh.131155$DE1.38614@pd7urf2no>`
- **In-Reply-To:** `<xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com>`

```
LX-i wrote:
<snip>

> 
> So there's hope for me yet - cool!  (Of course, this will probably be my 
> last "hands in the code" assignment, especially if I make E-7.  That'll 
> put me into management at that point.)
> 

Daniel,

What the hell is an E-7 ? OK, so I used Google to find out.

Never ever did get a handle on British Army officer ranks. Actually
never dealt with them and didn't want to :-)

For comparison of British Services, you might want to look at following,
plus the second shows RAF rank insignia, (presumably current ?).

http://www.bomber-command.info/rafranks.htm
http://www.raf.mod.uk/structure/ranks.cfm

Reasonably easy to figure out RAF and RN officer ranks because they are
a series of thick and thin stripes at the cuff, for dress uniform and
worn as shoulder loops when in RAF/RN battle-dress. I had always assumed
that an RAF group captain was the equivalent of an Army brigadier, which
I think you folks call a Brigadier General. While not an 'air officer' a
group captain is the first rank where they wear 'scrambled egg' on the
peak of their cap.

If you look at the list of RAF non-comm ranks it's been updated since I
left (1961). As you will note the chevrons, are v-shaped pointing
downwards. I trained as an Administrative Apprentice between Feb '49 -
Sep 50 in S. Wales. (We had three 'trades', secretarial,
equipment/supplies (everything from logistical control of toilet rolls
to aircraft engines) ands accounting (I'm fairly certain the latter was
nothing but Payroll - for sure they never produced a P & L statement :-)
). My training included shorthand, (Pitman's) and typing. A short period
before we passed out the Air Ministry introduced a new series of ranks
both for ground and non-comm aircrew - technicians. This sort of
paralleled the chevrons but were inverted.

The reasoning behind the new ranks - pure speculation - if you followed
the traditional rank route you would make it in progressive steps from
AC1(Aicraftsman 1st Class), through corporal and sergeant before the age
of 30, provided you did a reasonable job and kept your nose clean. It
stagnated a little after that, usually you didn't make flight sergeant
(three chevrons and a crown) until you were knocking 40. It's so long
ago that I can't remember specifics but I think you could take 
technician  examinations and if you passed you got the next technician 
rank. This allowed a minority and 'brighter' people to bypass the 
time-served approach.

I 'passed out' from training with speeds of 60 wpm for typing and 120
wpm for shorthand and on the basis of that I automatically got the rank
Junior Technician come 1951/01/01. Because of the shorthand/typing my
first posting was AMU(IG) - they do LOVE their sets of initials in the
military don't they ? Nobody could translate AMU(IG) for me but I was
given a rail and Underground voucher to get to Air Ministry Unit, West
Drayton, Middlesex, (fairly close to Heathrow). Having dragged my crap
through the camp to the orderly room they gave me another Underground
voucher to get to IG Richmond, (in Surrey, and Richmond Hill overlooks
the Thames; a magnificent view in September). Still no clue what the
'IG' is. 'Can you tell me how to get to the RAF in Richmond ?", I ask a
paper-seller. "Sorry mate, there's no RAF 'ere. The nearest is
Chessington", which I knew had a zoo. Fortunately a young WRAF comes on
the scene, works where I want to go and gives me directions. You've been
there done that, ask somebody for directions in a strange place and
you've lost it when they've directed you to the first left turn. Sod it
! I elicit the help of a taxi driver and after about fifteen minutes we
eventually are parked outside No. 136 Richmond Hill. No signs, no RAF
or Union Jacks flying and nothing in the grimy looking front window to
indicate either.

Anyhow I had arrived. Two private houses leased, for the Inspector 
General of the RAF, an Air Chief Marshal, final posting before he 
retires. So as secretary to the ACM I take his letters down in 
shorthand, which he gently dictates 'cos I'm a kid. Having typed and 
corrected the first letter a dozen times, they get themselves in a real 
secretary a 35-40 year old WRAF sergeant :-). Not quite the end of my 
secretarial career, I did shorthand/type stuff for his wing commanders 
and for about eight months was secretary for an Air Commodore at HQMEAF 
in Egypt, SESO (Senior Equipment Staff Officer).

Above of course, allows me to wax nostalgic. But back to the technician
ranks - you'll see from the current rank insignia that they use a
four-bladed propeller. Well during my time is was just moving the
chevrons around from South-pointing to North-pointing. Whether they had
back during my time, or currently, examinations for promotion I just
don't know. But how do you achieve your E-ratings in the USAF, time 
served or some form of examination ?

I had a little smile about you being in 'management'. Related to a
commercial setup is that like saying your are a Chief Programmer
controlling a team or perhaps a Programming project leader ? The 'smile'
is it would never have happened in the RAF in my time or even after I
left. As part of the English caste system you would have needed to be an
'officer and gentleman' to have the necessary intelligence.

Case in point. Around '69-'70, Ivor my DPM, (did his National Service,
conscription, in the RAF leaving with the exalted rank of LAC (Leading
Aircraftsman), subsequently traveled and became a computer operator at
a GE site in California), and yours truly, (leaving with the rank of
sergeant), did a liaison visit to a military site at Blandford Forum,
Dorset(shire) - forgotten name, but let's call it Joint Military
Computer Education Centre.

Don't know what rank the CO was but the place was primarily run by two
RAF flight lieutenants in the Education Branch. Candidates from all
three services were there for periods of training, (might have been 6
months or logically longer - just don't remember). But a prerequisite
was that they should all be officers and gentlemen. (From memory I would
say up to squadron leader/major rank). The two flight 'lewies' could
sense that Ivor and I had military backgrounds but were too polite  to
ask to satisfy their curiosity. We really smirked to ourselves when we
reached their computer room. The Operations Manager was a hairy-arsed
flight sergeant and his minions were aicraftsmen and corporals. OK for
the serfs to mind the shop, but design - good gracious me, that requires
superior qualities.

Nearly forgot - those apprentices who trained in accounting. Well much 
of that work being Payroll is now done by those computer thingies. As 
part of cost-cutting the MofD in UK has amalgamated departments and 
possibly originally had three computerized payrolls for army navy/RM and 
air force. But to upgrade, makes sense - one payroll for the lot. After 
all, other than their uniforms change colour, it's the same thing - right ?

For the switchover, take the smallest of the three first, the RAF. Small 
piece in Weekly 'Express' - a right cock-up ! People not receiving 
allowances when they should and others receiving allowances when they 
shouldn't. Permutations on the previous plus late cheques arriving in 
bank accounts. Nothing been written since, but one can hazard a guess at 
people spinning off into space. No it wasn't programmed by the 
'militaire' but done by an outside contractor called EDS. Oops ! EDS 
used to be on the J4 COBOL Committee until about a year or so back.


Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 12)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-26T20:39:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com>`
- **In-Reply-To:** `<Js9Yh.131155$DE1.38614@pd7urf2no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no>`

```
James J. Gavan wrote:
> LX-i wrote:
> <snip>
…[9 more quoted lines elided]…
> What the hell is an E-7 ? OK, so I used Google to find out.

All US Military services use the same pay grades - E-1 through E-9 for 
enlisted, O-1 through O-10 for officers.  The different services have 
different names for these ranks - in the Air Force, E-7 is Master 
Sergeant (MSgt), the beginning of the Senior NCO tier.  On occasion, 
you'll find a MSgt still laying code, but more often, they're NCOIC's or 
superintendents.

> Never ever did get a handle on British Army officer ranks. Actually
> never dealt with them and didn't want to :-)

The US Navy is weird all the way around.  Their ranks for E-4 through 
E-6 are related to their jobs, so you've got two letters and 3-2-1 as 
you rise in your job.  And, while the Army and Marines are close in 
enlisted ranks, the Navy is the only service that uses different officer 
rank names than the other three.

> For comparison of British Services, you might want to look at following,
> plus the second shows RAF rank insignia, (presumably current ?).
…[6 more quoted lines elided]…
> worn as shoulder loops when in RAF/RN battle-dress.

I find those confusing as all-get-out.  :)  I guess it's what you're 
used to...

> If you look at the list of RAF non-comm ranks it's been updated since I
> left (1961). As you will note the chevrons, are v-shaped pointing
> downwards.

I noticed that - there are even chevrons with a separate insignia above 
it.  Interesting.  In my last job, we did some work with the Royal 
Netherlands Air Force; their was different still.

> The reasoning behind the new ranks - pure speculation - if you followed
> the traditional rank route you would make it in progressive steps from
…[7 more quoted lines elided]…
> time-served approach.

[snip]

> But how do you achieve your E-ratings in the USAF, time 
> served or some form of examination ?

We have what's called the Weighted Airman Promotion System.  You get 
points for how long you've been in the USAF, how long you've been in 
your current rank, decorations, and past performance appraisals (which 
are weighted chronologically from your latest one back).  That's your 
starting point.  Then, there are two tests, 100 questions (points) each; 
one covers general military information, and the other covers your 
specific job.

Once everyone has tested, they calculate the scores, line 'em up in 
descending order, decide how many stripes to give, and draw the line at 
that point in the list.  What this means is that every year, the "cutoff 
score" can be different.  And, since you get points every year, those 
who don't test well still have an opportunity.  The average Time in 
Service (TIS) for TSgt (E-6) is 14 years - I put it on in just under 9. 
  :)  Average TIS for MSgt is 16.1 years - supposedly, TSgt is the 
toughest rank to make.  Those who are encouraging me are saying that 
there's a good chance I could make it first shot, though I'm trying not 
to get my hopes up.  I missed TSgt the first time, but was just sure I 
had made it - it was a *big* letdown.

> I had a little smile about you being in 'management'. Related to a
> commercial setup is that like saying your are a Chief Programmer
> controlling a team or perhaps a Programming project leader ?

It depends.  In my last organization, there was a role in our process of 
"Software Project Manager."  They were the person who manages the 
development team, and balances the customer's needs against the 
abilities of the team.  (i.e. "No, we can't rewrite the whole system by 
next Tuesday!"  ;>  )  For large projects, these were usually 
high-ranking civilians (GS-11 to GS-13, O-4 (Major) to O-5 (Lieutenant 
Colonel) officer equivalent), but for smaller ones, you could have an 
enlisted guy doing it.  (The SPM on one project was an E-5! (Staff 
Sergeant - the first NCO rank))  My new organization uses Agile 
development, so they have the roles defined there (Product Owner, 
ScrumMaster, etc.).  I'm the only military person in my shop, and I 
report directly to a GS-14.

The other thing Senior NCO programmers do is the job of superintendent. 
  This is where your main job is the "military" aspect of the job rather 
than software engineering and development.  You're in charge of making 
sure that all the military below you are up to date on appraisals; you 
brief them on policy on a recurring basis; you put out fires as they 
arise; you assign people to taskings as you receive them.  Of course, 
along with that is supporting all organizational events (going-aways, 
promotions, calls, etc.) and usually directly supervising the NCOICs 
(Non-Commissioned Office in Charge - usually one per office) under you.

> The 'smile'
> is it would never have happened in the RAF in my time or even after I
> left. As part of the English caste system you would have needed to be an
> 'officer and gentleman' to have the necessary intelligence.

A lot of this used to be done by officers - in fact, at my last job, I 
was working on some old code that had a "1LT" as the author (O-2). 
Officers never write code anymore.  :)  The NCO corps has been given 
more and more responsibility.  We now have three levels of Professional 
Military Education (one between E-4 and E-5, one between E-6 and E-7, 
and one between E-7/8 and E-8/9 - that last one used to be 8-9, but 
they're pushing to move it to the 7-8 transition), each of which is 
focused on increased leadership and management skills.

There is a new policy that just went into effect that states that your 
appraisal (EPR - Enlisted Performance Report) cannot get "senior rater" 
indorsement if you do not have you Community College of the Air Force 
(CCAF) associate's degree.  On the EPR, your supervisor signs it, and 
then the "additional rater" (usually your supervisor's supervisor) signs 
(indorses) it.  One you get to E-7, this person is likely to be a 
"senior rater" (I'm sure of the exact rank where that title begins). 
Anyway, if the senior rater doesn't sign it, it basically kills your 
chances of selection for E-8 and E-9, which use an evaluation board in 
addition to the WAPS testing described above.

About that CCAF - in the Air Force, all basic and technical training is 
assigned college credit.  Add 20 hours of "general education" on top of 
it, and you've got it.

> The Operations Manager was a hairy-arsed
> flight sergeant and his minions were aicraftsmen and corporals. OK for
> the serfs to mind the shop, but design - good gracious me, that requires
> superior qualities.

Heh - that sounds about rights.  When I went to 7-level school (see 
below for an explanation of that), that's when they taught us design, as 
well as configuration management and limited project management.

7-level?  Our job codes are 5 characters - mine is 3C0X2.  The "X" is 
replaced with the level (an odd number), depending on how much I've 
learned.  My current job code is 3C072.  You don't get "9" until E-9 
(CMSgt).

> For the switchover, take the smallest of the three first, the RAF. Small 
> piece in Weekly 'Express' - a right cock-up ! People not receiving 
…[5 more quoted lines elided]…
> used to be on the J4 COBOL Committee until about a year or so back.

Not related to software screw-ups, but check out my latest blog entry. 
Basically, the Army is having to borrow from the Air Force and Navy's 
money (payroll included) because Congress hasn't passed the emergency 
appropriations bill.  There's a link at the top of the post to the 
original article, if you just want to read the facts instead of my 
right-wing ranting about it.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-27T06:08:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CrgYh.132963$DE1.61323@pd7urf2no>`
- **In-Reply-To:** `<FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com>`

```
LX-i wrote:
> James J. Gavan wrote:
> 
…[13 more quoted lines elided]…
>
<snip> -

Daniel,

Thanks for the very detailed explanation. I wont claim I memorized it, 
but get the gist.

> Not related to software screw-ups, but check out my latest blog entry. 
> Basically, the Army is having to borrow from the Air Force and Navy's 
…[4 more quoted lines elided]…
> 

You being right-wing - I never would have guessed :-) Remember 'US 
Presidents and Foreign Policy'. Don't have to wait until 2008 - same 
answer as the American public is giving in polls.

Jimmy
You being right-wing - I never would have guessed.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 14)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-27T19:08:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com>`
- **In-Reply-To:** `<CrgYh.132963$DE1.61323@pd7urf2no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no>`

```
James J. Gavan wrote:
> LX-i wrote:
>> Not related to software screw-ups, but check out my latest blog entry. 
…[7 more quoted lines elided]…
> You being right-wing - I never would have guessed :-)

heh - I know, I hide it so well... :)

> Remember 'US 
> Presidents and Foreign Policy'. Don't have to wait until 2008 - same 
> answer as the American public is giving in polls.

You got me there...  What is that a reference to?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 15)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-29T03:41:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0uUYh.143628$aG1.81147@pd7urf3no>`
- **In-Reply-To:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com>`

```
LX-i wrote:
> James J. Gavan wrote:
> 
…[20 more quoted lines elided]…
> 

Come on, come on, don't play 'Mr. Innocent' :-). Am I dreaming what I'm
reading in Canadian papers. Polls in the States put Dubya's popularity
rating down to 30% last time I looked. Not sure which old 'Eastern'
bloc country, but Dubya can take heart that the other guy's popularity
rating was down to 5% !

BBC World News did a week of 10 minute items on the Iraq story, 
sub-topics. I had to write to an MD in Sri Lanka to check when his 
sister, our friend, would by flying back to Calgary. As he was a 
physician I wrote him the following :-

------------------------------------------------------------------------------
Do you ever watch BBC World News ? As a doctor you might have a mild 
interest in the following. This past week they have been doing ten 
minute pieces about Iraq. Last night "Iraq War - to date 3,000 
fatalities and over 50,000 wounded". Interesting though, the ratio 
casualties to dead, Vietnam 3:1 whereas Iraq 16:1 - due to the fact 
front line medical aid is more sophisticated, they are able to get more 
alive back to the States.

Mind you looking at the tragic young men going through therapy, 
exercising with stumps for legs, or no limbs at all - not sure it's a 
situation I would want to be in. However, there is a military hospital 
in California that specializes in the brain damaged. One young sergeant 
who was interviewed was incredibly articulate and positive. He had one 
ear blown off and brain damage which left his mind absolutely blank 
about childhood memories. Part of therapy was getting him onto a 
bicycle. Then he suggested, and the military supported him 
enthusiastically, that he should get into motorized mountain bike 
riding. The got him the bike. As he said, entering competitions, and 
having to keep a mental log of venues, dates, times, competitors etc., 
has helped his retentive abilities.
---------------------------------------------------------------------------------

So as tragic as the Iraq War might be there are small dramatic positives 
when you look at the wounded to dead ratio.

PS: I quote BBC above - 50,000 wounded; I think I subsequently picked up 
from a US network that the figure is 30,000.

PPS: For Alistair. Yes I could probably get more UK stuff if I want to 
shell out additional monthly charges for more TV level options. Of what 
I currently have at least 80% is crap/dumbed down catering to the morons 
who like American/Canadian/UK-Idol and the 'Reality' shows. My latest 
setup gives me a minimum of four channels that show movies - so I can be 
a bit selective in choosing.

Different from UK where you have an upfront fee/licence. Canada and I 
believe the States is probably a parallel situation. You may/may not pay 
for a cable initial installation fee. Then they put packages together, 
giving you different options and you pay according to the Level. I think 
it's a similar operation with the satellite dishes.

Tor TV we have Basic plus Level 1 - Currently about $34 per month 
(including 6% GST) and $45 per month for direct cable for Internet. 
Conveniently Shaw provides both my TV and Web access. (For comparison 
Canadian dollar is currently 'almost' equal to US dollar - so take it as 
two dollars to a pound sterling).

Fortunately because of a channel number re-shuffle to accommodate 
HDV/HTV (?) I can now receive for free, BBC World 24/7 - so if I miss 
the main news which I used to get pre-recorded from PBS Spokane 
(SPO-CAN) in Washington State, at 18:00 MT, I can pick it up directly 
from BBC on the hour, GMT of course.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 16)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-29T08:23:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177860215.349763.291600@y80g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<0uUYh.143628$aG1.81147@pd7urf3no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no>`

```
On 29 Apr, 04:41, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> ---------------------------------------------------------------------------­---
> Do you ever watch BBC World News ? As a doctor you might have a mild
…[6 more quoted lines elided]…
>
Scientific American has an mp3 podcast for April 18, 2007 which covers
the improvements made in emergency care provided to soldiers by the US
military. Go to (sorry, I know some people don't like Go Tos!)
www.sciam.com/podcast/index.cfm?e_type=W for a free download.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 16)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-29T18:53:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **In-Reply-To:** `<0uUYh.143628$aG1.81147@pd7urf3no>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no>`

```
James J. Gavan wrote:
> LX-i wrote:
>> James J. Gavan wrote:
…[10 more quoted lines elided]…
> rating was down to 5% !

Right - but you said we didn't have to wait until 2008.  According to 
our Constitution, you're right - for new foreign policy (well, from new 
folks anyway) we have to wait until 2009.  Diplomacy is the domain of 
the executive branch, not the legislative branch.

And, I find it really strange that Pelosi and company didn't have time 
for the President of this country (who offered to meet with them to 
discuss foreign policy), and the didn't have time to meet with General 
Petraeus, the new US commander in Iraq.  However, she *did* have time to 
go meet with Bahar Assad, the president of Syria (a state sponsor of 
terrorism) and deliver a message from the US and Israel that neither 
country had authorized her to deliver.

Elections have consequences, true - but a party control change in the 
legislative branch doesn't change foreign policy.

And, regarding approval numbers - W's numbers are abysmal - the reason 
for that is that on the Democrat side, he could cure cancer and they'd 
still hate him for "stealing" the 2000 election.  However, that hasn't 
kept him from trying to play the middle a lot, to try to appease them. 
That leads to high dissatisfaction among Republicans.  Combine both 
those, and you get what you get.

Those number are interesting, but you can't really make any inferences 
from them.  Just because someone says they disapprove of the President 
(and that's a black and white question - no room for gray) doesn't mean 
that they wish they had voted for the opposition party.  As many things 
as I feel he's rolled over on (Social Security reform, illegal 
immigration reform, etc.), I *still* think we're better off than we 
would have been under a President Kerry.

> Mind you looking at the tragic young men going through therapy, 
> exercising with stumps for legs, or no limbs at all - not sure it's a 
…[14 more quoted lines elided]…
> when you look at the wounded to dead ratio.

That depends on how you look at it.  I'd much rather come home from war 
and spend time with my family for the rest of my life, even if I were in 
a wheelchair.  Sure, I wouldn't *choose* to spend the rest of my life in 
a wheelchair.  But, I *chose* to join the military; and, if in the 
course of defending the nation, I had a "near-fatal" injury, I'd be very 
grateful for the "near" part.  :)

> Different from UK where you have an upfront fee/licence. Canada and I 
> believe the States is probably a parallel situation. You may/may not pay 
> for a cable initial installation fee. Then they put packages together, 
> giving you different options and you pay according to the Level. I think 
> it's a similar operation with the satellite dishes.

Yep - we paid $30 for an install fee, then get $30 off for 6 months (I 
think - my wife does most of that stuff).
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-30T02:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f13k12$33u$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
In article <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>And, I find it really strange that Pelosi and company didn't have time 
>for the President of this country (who offered to meet with them to 
…[4 more quoted lines elided]…
>country had authorized her to deliver.

I find it a bit... humorous that her visit was trumpeted well in advance, 
cleared through all appropriate diplomatic channels, argued pro-and-con 
nigh unto the death by pundits, analysts, critics and supporters...

... and some people are still innocent enough to believe that something 
actually *happened* then that was not planned by and agreed to in advance 
by all parties involved.  Everyone in on the deal was under so much 
scrutiny that she couldn't even bring a cake in the shape of a key!

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-30T08:46:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<570c339vv5shli961bilduq9ea80lcvcm3@4ax.com>`
- **References:** `<I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
On Sun, 29 Apr 2007 18:53:36 -0600, LX-i <lxi0007@netscape.net> wrote:

>Right - but you said we didn't have to wait until 2008.  According to 
>our Constitution, you're right - for new foreign policy (well, from new 
>folks anyway) we have to wait until 2009.  Diplomacy is the domain of 
>the executive branch, not the legislative branch.

Not entirely.   Which causes some consternation when executives sign
treaties which don't get ratified.

Often diplomacy works similar to the president's veto power over the
legislature - only in reverse.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-30T08:51:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com>`
- **References:** `<I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
On Sun, 29 Apr 2007 18:53:36 -0600, LX-i <lxi0007@netscape.net> wrote:

>And, regarding approval numbers - W's numbers are abysmal - the reason 
>for that is that on the Democrat side, he could cure cancer and they'd 
…[3 more quoted lines elided]…
>those, and you get what you get.

Those who thought he stole the election thought so when his numbers
were at their highest.   Dissatisfied Republicans still like him
compared to the Democrats.    His numbers fell when those in the
middle became dissatisfied.

But the leading Democratic candidates are both Senators.    The last
Senator to win was Kennedy, and he needed Johnson as a running mate
(and Richard Daly), to defeat Nixon who made a bad mistake in having
Henry Cabot Lodge as his running mate.

Maybe the new money will make a difference - it certainly appears that
all of the candidates for both parties are willing to be bought. But
traditionally, we prefer an executive over a law maker (law makers
have to compromise a lot).
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-30T19:59:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com>`
- **In-Reply-To:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com>`
- **References:** `<I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com>`

```
Howard Brazee wrote:
> But the leading Democratic candidates are both Senators.    The last
> Senator to win was Kennedy, and he needed Johnson as a running mate
> (and Richard Daly), to defeat Nixon who made a bad mistake in having
> Henry Cabot Lodge as his running mate.

.snicker.  love the "Daly" reference.  Which party is it again, the one 
that doesn't want to combat voter fraud?  W probably would have won the 
popular vote in 2000 too if you didn't count all the dead people...

> Maybe the new money will make a difference - it certainly appears that
> all of the candidates for both parties are willing to be bought. But
> traditionally, we prefer an executive over a law maker (law makers
> have to compromise a lot).

This is true.  Giuliani is the only major player with executive 
experience on the Republican side, and they don't really *have* a 
front-runner on the Democrat side (though Bill Richardson, the NM 
governor who's running, might be one of the few Democrats I'd consider 
voting for).

But hey - Fred Thompson's been a DA!  ;)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-01T09:24:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com>`

```
On Mon, 30 Apr 2007 19:59:32 -0600, LX-i <lxi0007@netscape.net> wrote:

>This is true.  Giuliani is the only major player with executive 
>experience on the Republican side, and they don't really *have* a 
>front-runner on the Democrat side (though Bill Richardson, the NM 
>governor who's running, might be one of the few Democrats I'd consider 
>voting for).

It is interesting that Guiliani's political strength is that he
survived 9/11.    Richardson's strength is that two administrations
previous to his got New Mexico into a fiscal crisis, so the previous
administration had to do some belt tightening to fix its economy - and
his administration had the revenue from this fix.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-01T22:16:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **In-Reply-To:** `<i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 30 Apr 2007 19:59:32 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[7 more quoted lines elided]…
> survived 9/11.

Maybe for the general populace, but Republicans knew about him even 
before 9/11.  His biggest accomplishment pre-9/11 was bringing the crime 
rate way, way down.

> Richardson's strength is that two administrations
> previous to his got New Mexico into a fiscal crisis, so the previous
> administration had to do some belt tightening to fix its economy - and
> his administration had the revenue from this fix.

I hadn't read up much on local NM politics since I got here.  He seemed 
to be one of the more reasonable people on Clinton's cabinet (I know - 
not much competition there), and he seems to already have a lot of 
international clout due to his dealings with energy.  I did meet one of 
his former security guards, and asked him if there were any scandals 
waiting to break.  He said no, but that Richardson was a typical 
politician in the traditional sense.

I said "might...consider" voting for - I still think that, right now, 
the weakest Republican candidate is immensely preferable to the 
strongest Democrat candidate.  Figuring out exactly who they are is an 
exercise left to the reader.  ;)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-05-10T17:40:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net>`
- **In-Reply-To:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
LX-i wrote:
>>
>> It is interesting that Guiliani's political strength is that he
…[5 more quoted lines elided]…
> 
Now that's an interesting statement.

Perhaps it's more accurate to say 'he was (fortunate to be) in 
office when the crime rate fell.'

Here's how I've heard it:
It was the result of contraception & abortion.

vide:
The Reluctant Economist
Perspectives on Economics, Economic History, and Demography
Richard A. Easterlin, University of Southern California

Here's a link to a 'dialog' on the topic:

http://www.slate.com/id/33569/entry/33571/

Happy reading.

Michael
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-10T10:54:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdj6435vof4d1jgnrbklbjvs9491op2oco@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net>`

```
On Thu, 10 May 2007 17:40:03 +0100, Michael Russell
<Michael.Russell@msn.com> wrote:

>Now that's an interesting statement.
>
…[13 more quoted lines elided]…
>http://www.slate.com/id/33569/entry/33571/

Or buy _Freakonomics: A Rogue Economist Explores the Hidden Side of
Everything_  (2005) by Steven Levitt and Stephen J. Dubner.

Fun reading.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-10T21:53:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **In-Reply-To:** `<xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net>`

```
Michael Russell wrote:
> LX-i wrote:
>>>
…[13 more quoted lines elided]…
> It was the result of contraception & abortion.

Ah - the Roe effect.  :)  I don't think it would account for a 50%+ drop 
in crime in 8 years...

(I read the article - I just disagree with it as a cause for the 
reduction.  It read more like a defense of abortion.)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-05-11T10:14:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Kmdnb6si7pnrtnbRVnyiwA@pipex.net>`
- **In-Reply-To:** `<Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
LX-i wrote:
> Michael Russell wrote:
>> LX-i wrote:
…[21 more quoted lines elided]…
> 
Oh. OK. Whatever.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-11T08:58:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On Thu, 10 May 2007 21:53:56 -0600, LX-i <lxi0007@netscape.net> wrote:

>
>Ah - the Roe effect.  :)  I don't think it would account for a 50%+ drop 
>in crime in 8 years...

Why not?   Do you think the mayor's policy would account for such a
drop?

>(I read the article - I just disagree with it as a cause for the 
>reduction.  It read more like a defense of abortion.)

Ahh, that's why not.    Such an accounting has side effects that you
don't care for.

But if you care about both issues (crime & abortion), it would be
worth analyzing to see if the root cause shown here (fewer hopeless
poor people), can be created by other means.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-11T16:41:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>`
- **In-Reply-To:** `<3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 10 May 2007 21:53:56 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[4 more quoted lines elided]…
> drop?

Yes - increased enforcement makes more people obey the law; not because 
they think it's a good law, but because they want to avoid the penalties 
for breaking it.

>> (I read the article - I just disagree with it as a cause for the 
>> reduction.  It read more like a defense of abortion.)
…[6 more quoted lines elided]…
> poor people), can be created by other means.

I do care about both issues.  But, even if it were true, and 100% of the 
crime reduction in our nation were due to abortion, I'd still be against 
it - just as I'd be against capital punishment for petty larceny.  (I 
can see it now - outlaw abortion except for emergencies, health of the 
mother, or if either parent has a previous conviction.  How cynical 
would that law be?!?)

Besides, if we start trying to pre-judge people, we're in very dangerous 
territory.  The entire concept of "innocent until proven guilty" would 
go out the window.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-12T08:15:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f23t3c$lsi$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>`

```
In article <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Howard Brazee wrote:
>> On Thu, 10 May 2007 21:53:56 -0600, LX-i <lxi0007@netscape.net> wrote:
…[9 more quoted lines elided]…
>for breaking it.

Oh... is *that* why the USA has such a high percentage of the population 
incarcerated?

(I believe it was Gladstone who said 'Liberalism is trust of the people, 
tempered by prudence; Conservatism is distrust of the people, tempered by 
fear.')

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-12T08:22:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`
- **In-Reply-To:** `<f23t3c$lsi$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[12 more quoted lines elided]…
> incarcerated?

Could be - what I find hard to believe is the mantra of "If the crime 
rate is down, why are so many people locked up?"  It's kind of like 
asking, "If I'm sweating so much, why am I so hot?"

> (I believe it was Gladstone who said 'Liberalism is trust of the people, 
> tempered by prudence; Conservatism is distrust of the people, tempered by 
> fear.')

I hope Gladstone said some other things too, because he or she is way 
off on that one.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-12T11:06:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lslb431dmr0a7ejbn8j8anjk40pqsa5dj8@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`

```
On Sat, 12 May 2007 08:22:18 -0600, LX-i <lxi0007@netscape.net> wrote:

>docdwarf@panix.com wrote:
>> In article <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>,
…[24 more quoted lines elided]…
>off on that one.  :)

He knew of what he spoke.  He is still regarded as one of the greatest
British prime ministers, with Winston Churchill and others citing
Gladstone as their inspiration.  His full name, William Ewart
Gladstone was a British Liberal Party statesman and Prime Minister
(1868ï¿½1874, 1880ï¿½1885, 1886 and 1892ï¿½1894). He was a notable political
reformer, known for his populist speeches, and was for many years the
main political rival of Benjamin Disraeli.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I'd give my right arm to be ambidextrous!"
-- Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-12T23:24:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f25ib8$2ag$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`

```
In article <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>,
…[17 more quoted lines elided]…
>asking, "If I'm sweating so much, why am I so hot?"

Eh?  Sweating is a neutral response; it can be a sign of either health or 
sickness.  It is not readily apparent what you are attempting to 
communicate here; you might be saying that the percentage of a country's 
population which has been imprisoned is a sign of that country's health... 
whether ill or good health is unsure.

>
>> (I believe it was Gladstone who said 'Liberalism is trust of the people, 
…[4 more quoted lines elided]…
>off on that one.  :)

A bit of research into Gladstone might be in order, then... remember, some 
say that Away Back When the principles which are now called Republican 
were adhered to by what was then called the Democratic party and 
vice-versa.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-12T20:49:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com>`
- **In-Reply-To:** `<f25ib8$2ag$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[23 more quoted lines elided]…
> whether ill or good health is unsure.

OK - bad example.  I see the high prison population as one of the causes 
of the low crime rate.  So, the original statement becomes "If 
[symptom], then why [cause]?"

>>> (I believe it was Gladstone who said 'Liberalism is trust of the people, 
>>> tempered by prudence; Conservatism is distrust of the people, tempered by 
…[7 more quoted lines elided]…
> vice-versa.

True, and I'll look into it.  But I can't imagine the antics of the 
current Democrat party being considered conservative *ever*.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-13T12:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f26uk5$h1d$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com>`

```
In article <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>,
…[3 more quoted lines elided]…
>>>> LX-i  <lxi0007@netscape.net> wrote:

[snip]

>>>>> Yes - increased enforcement makes more people obey the law; not because 
>>>>> they think it's a good law, but because they want to avoid the penalties 
…[15 more quoted lines elided]…
>[symptom], then why [cause]?"

I see... so you see that Americans, per capita, commit more crimes than do 
almost any other nationality on the planet and, as such, deserve to have 
and benefit from having a larger percentage of their fellow-citizens 
living behind bars and kept there by armed guards as a result.

Gladstone: '... Conservatism is distrust of the people, tempered by 
fear'... now might you see why this came to mind?

>
>>>> (I believe it was Gladstone who said 'Liberalism is trust of the people, 
…[11 more quoted lines elided]…
>current Democrat party being considered conservative *ever*.  :)

Members of the current Democratic Party are just that, Mr Summers... they 
are members of the current Democratic party, no more, no less.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-13T15:39:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com>`
- **In-Reply-To:** `<f26uk5$h1d$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> I see... so you see that Americans, per capita, commit more crimes than do 
> almost any other nationality on the planet and, as such, deserve to have 
> and benefit from having a larger percentage of their fellow-citizens 
> living behind bars and kept there by armed guards as a result.

Not everyone can handle freedom.  With increased freedom comes increased 
incentive to break the law - the whole "give an inch, take a mile" 
thing.  Also, capital punishment is used a lot less in this country than 
in non-free countries.  You don't have full jails if you execute 
criminals instead of incarcerate them.  :)

> Gladstone: '... Conservatism is distrust of the people, tempered by 
> fear'... now might you see why this came to mind?

I'd see why it came to mind - but I think that it oversimplifies the 
situation to the point where it trends toward inaccuracy.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-14T09:24:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f299t4$1ea$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com>`

```
In article <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> I see... so you see that Americans, per capita, commit more crimes than do 
…[4 more quoted lines elided]…
>Not everyone can handle freedom.

Quite right... increased freedom means fewer legal constraints, it only 
makes sense that decreasing legal constraints will result in... more 
activities which exceed legal constraints; the logical conclusion, then, 
is that the most free society is the one with the most crime.

> With increased freedom comes increased 
>incentive to break the law - the whole "give an inch, take a mile" 
>thing.

'More freedom makes for a greater incentive to commit crimes'... so a 
society of slaves, which has less freedom, should have less crime... but 
one of the few countries with a higher per-capita imprisonment rate than 
the United States is the former Soviet Union... so it can be concluded 
that there was just too much freedom there.

>Also, capital punishment is used a lot less in this country than 
>in non-free countries.  You don't have full jails if you execute 
>criminals instead of incarcerate them.  :)

So... less freedom and more capital punishment makes for a smaller 
per-capita prison population; no wonder someone noticed that 'the only 
place to find maximimum security is in jail'.

>
>> Gladstone: '... Conservatism is distrust of the people, tempered by 
…[3 more quoted lines elided]…
>situation to the point where it trends toward inaccuracy.

That's right... accuracy comes in saying 'the fewer legal constraints 
people have the more likely they are to commit crimes... except, of 
course, for the former Soviet Union because they were Just Plain Bad.'

... and I, of course, am the King of England.  God Save the Me!

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-14T06:57:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>`
- **In-Reply-To:** `<f299t4$1ea$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[10 more quoted lines elided]…
> is that the most free society is the one with the most crime.

Sounds like anarchy to me...  :)

However, issues dealing with people can seldom be broken down to "if (x) 
then not (y)".  The fact that a larger percentage than most of the 
population is jailed, by itself, cannot be used to make concrete 
statements on the freedom of a society.  As you pointed out, the USSR 
had a high prison population as well, even higher than ours.

Governments aren't like computer programs or mathematical problems, 
because they have an extra unknown variable - humans.  Communism was 
great - on paper.  But it failed to recognize the innate needs of 
humans, and as such, had to be enforced with a heavy hand and eventually 
collapsed.  (It's on its way out - even in China.)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-14T13:19:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f29nks$ksv$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>`

```
In article <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com>,
…[13 more quoted lines elided]…
>Sounds like anarchy to me...  :)

What something 'sounds like', Mr Summers, could have more to do with the 
ear perceiving it than anything else.

>
>However, issues dealing with people can seldom be broken down to "if (x) 
>then not (y)".

Hmmmmm... 'if healthy then not sick'... 'if having longevity then not 
dying young'... 'if free market then not many legal restraints on 
trade'... 'if believing in deities then not atheistic'.

>The fact that a larger percentage than most of the 
>population is jailed, by itself, cannot be used to make concrete 
>statements on the freedom of a society.

The fact that a society chooses to hold a larger percentage than most 
behind concrete cannot be used to make statements on the freedom of a 
society... all right, I'll bite: what, Mr Summers, in your opinion, *can* 
be used to make such statements?

>As you pointed out, the USSR 
>had a high prison population as well, even higher than ours.

Quite right, Mr Summers... but nothing of interest can be concluded from 
that, I'm sure.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-14T18:35:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>`
- **In-Reply-To:** `<f29nks$ksv$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[5 more quoted lines elided]…
> trade'... 'if believing in deities then not atheistic'.

OK - substitute "groups of people" for people above.

>> The fact that a larger percentage than most of the 
>> population is jailed, by itself, cannot be used to make concrete 
…[5 more quoted lines elided]…
> be used to make such statements?

You're not paying attention.  See the "by itself" up there?  It can be 
used as *part* of an analysis, but one cannot make concrete statements 
regarding the freedom of a society *solely* on its prison population ratio.

I was really hoping we could have a good discussion.  However, you are 
once again refusing to debate substance, and are content to pick apart 
style.  Whether you realize you're doing it or not, I simply don't have 
the time to go back and forth for 10 clarifications on the things I say, 
when it seems that you intentionally misinterpret them in the only way I 
happen to leave open for misinterpretation.

It's not that I don't have the inclination - I'd love to get to a point 
where you tell me my actual point is bull, and not some misstatement or 
misinterpretation of what I said.  But, it's a free country, and a free 
Internet - you have the right to discuss things in whatever manner you 
feel is appropriate.

With a 2-year-old, a kid in T-ball, a kid in baseball, the older two in 
Cub Scouts, college courses, and spending time with my wife - I simply 
don't have the time.  My entire entry into this discussion was to let 
Mr. Dashwood know that some of the spin that he was hearing about the 
way things are going in this country was not necessarily how everyone 
else saw it.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-15T00:50:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2b04m$749$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>`

```
In article <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>,
…[8 more quoted lines elided]…
>OK - substitute "groups of people" for people above.

I did... the result is:

'However, issues dealing with groups of people can seldom be broken doen 
to 'if (x) the not (y)'

'Hmmmmm... 'if healthy then not sick'... 'if having longevity then not 
dying young'... 'if free market then not many legal restraints on 
trade'... 'if believing in deities then not atheistic'.'

Doesn't seem to be much of a difference.

>
>>> The fact that a larger percentage than most of the 
…[8 more quoted lines elided]…
>You're not paying attention.

Quite the contrary, Mr Summers; some might say that I am paying more 
attention than your words, corrections and re-corrections deserve.

>See the "by itself" up there?  It can be 
>used as *part* of an analysis, but one cannot make concrete statements 
>regarding the freedom of a society *solely* on its prison population ratio.

That I saw such a thing, Mr Summers, might have been indicated by my 
request for your opinion.

>
>I was really hoping we could have a good discussion.  However, you are 
…[4 more quoted lines elided]…
>happen to leave open for misinterpretation.

Is that how you see this, Mr Summers?  How very interesting... my view of 
the interaction is entirely different; since you don't have the time 
further discussion I'll leave you to things you see as being of greater 
merit.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-15T21:33:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N-6dnU9tB-o45tfbnZ2dnUVZ_r_inZ2d@comcast.com>`
- **In-Reply-To:** `<f2b04m$749$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <f2b04m$749$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[17 more quoted lines elided]…
> trade'... 'if believing in deities then not atheistic'.'

"If not black then white"  "If not Catholic then Protestant"  "If not 
European then Asian"

> Doesn't seem to be much of a difference.

Guess it depends on your perspective.

>>>> The fact that a larger percentage than most of the 
>>>> population is jailed, by itself, cannot be used to make concrete 
…[8 more quoted lines elided]…
> attention than your words, corrections and re-corrections deserve.

Than they deserve?  What makes my words more or less deserving than 
anyone else's?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-16T09:35:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2ej9d$3cm$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <f2b04m$749$1@reader2.panix.com> <N-6dnU9tB-o45tfbnZ2dnUVZ_r_inZ2d@comcast.com>`

```
In article <N-6dnU9tB-o45tfbnZ2dnUVZ_r_inZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>,
…[25 more quoted lines elided]…
>Guess it depends on your perspective.

*Now* you begin to get it... good!  So... if not imprisoned then... what?

>>>>> The fact that a larger percentage than most of the 
>>>>> population is jailed, by itself, cannot be used to make concrete 
…[11 more quoted lines elided]…
>anyone else's?

(quotes below supplied on offline request)

You'd have to ask the ones who might deem them such, Mr Summers... at any 
rate, since you now have the time to continue the conversation it might be 
nice to return to the point you didn't address.  You say you 'find it hard 
to believe the mantra find hard to believe is the mantra of "If the crime 
rate is down, why are so many people locked up?"' and asking such is kind 
of like asking, "If I'm sweating so much, why am I so hot?"...

... and when it is pointed out that fever is a neutral response, generated 
by both healthy and unhealthy causes, so that having so many people locked 
up might be a sign of health or disease, you assert that 'not everyone can 
handle freedom'.  When it is pointed out that a logical conclusion of this 
is 'most free society is the one with the most crime', putting the former 
Soviet Union in a rather... curious light you then state that 'issues 
dealing with people can seldom be broken down to "if (x)
then not (y)"'...

... and that the a large percentage of a society's population denied of 
freedom cannot be used to make concrete statements of the freedom of the 
society.  That, apparently, is absurd - 'it is a very free society for 
some people, not others' - but I tried to engage you further by asking 
'what, Mr Summers, in your opinion, *can* be used to make such 
statements?'.

At that point you suddenly became Too Busy to Answer.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 38)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-18T08:11:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hLGdnY-0vpG9KdDbnZ2dnUVZ_rHinZ2d@comcast.com>`
- **In-Reply-To:** `<f2ej9d$3cm$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <f2b04m$749$1@reader2.panix.com> <N-6dnU9tB-o45tfbnZ2dnUVZ_r_inZ2d@comcast.com> <f2ej9d$3cm$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> At that point you suddenly became Too Busy to Answer.

I found out I have 8 weeks more than I though I had on my college 
classes...  :)  But, a thoughtful response takes time, which I won't 
have until I return.  It's on its way...
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-15T01:14:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DP72i.185503$aG1.61145@pd7urf3no>`
- **In-Reply-To:** `<kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>`

```
LX-i wrote:
> docdwarf@panix.com wrote:
> 
…[13 more quoted lines elided]…
>

Daniel, ( or Mr. Summers as he keeps calling you). Shouldn't that be 
Sgt. Summers :-)

Not quite clear - is the above head count three potential Republicans or 
five ? :-). Even 3 would be 3 too many !

As to bull I was somewhat surprised by a couple of assertions you made 
in other messages (1) Global warming was bull and (2) You know better 
sources than CNN or BBC for news. Care to elaborate on the latter ?
(You can ignore CNN - other than watching for day-by-day coverage on the 
early part of Gulf War II, I don't watch).

However let's roll global warming and news sources together :--

http://news.bbc.co.uk/2/hi/americas/6648265.stm

Above was a news item I watched on PBS this evening and checked the web 
site for backup. I think we can safely assume that Evangelical 
colleges/universities are not hotbeds for growing Democrats. So now give 
your 'spin' on what the article covers - and which radio/TV-broadcaster, 
in your view, would give better(or unbiased) coverage than BBC.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-15T20:33:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aaadneS9mb8c8NfbnZ2dnUVZ_g-dnZ2d@comcast.com>`
- **In-Reply-To:** `<DP72i.185503$aG1.61145@pd7urf3no>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <DP72i.185503$aG1.61145@pd7urf3no>`

```
James J. Gavan wrote:
> LX-i wrote:
>>
…[9 more quoted lines elided]…
> Sgt. Summers :-)

Technically (no pun intended) it's TSgt Summers.  But, I'm easy - call 
me whatever you want, just don't call me late for dinner!

> Not quite clear - is the above head count three potential Republicans or 
> five ? :-). Even 3 would be 3 too many !

Just 3 - 3 very active boys...

> As to bull I was somewhat surprised by a couple of assertions you made 
> in other messages (1) Global warming was bull and (2) You know better 
…[6 more quoted lines elided]…
> http://news.bbc.co.uk/2/hi/americas/6648265.stm

Wow - they even updated it to include the fact that Dr. Falwell passed 
away today.  Impressive...

> Above was a news item I watched on PBS this evening and checked the web 
> site for backup. I think we can safely assume that Evangelical 
> colleges/universities are not hotbeds for growing Democrats. So now give 
> your 'spin' on what the article covers - and which radio/TV-broadcaster, 
> in your view, would give better(or unbiased) coverage than BBC.

The article above is quite well-balanced.  It doesn't try to make 
statements, it simply presents the two sides.  I'm impressed.  If that's 
the normal way everyday news is presented by the BBC, I'd change my tune.

As to the media in this country, there is one example that I think is 
pretty illustrative.  Rush Limbaugh has a three-hour-a-day, 
five-day-a-week radio talk show.  As he does his show, he has an 
Internet video stream running (called the "Dittocam").  In the run-up to 
the 2006 elections, Michael J. Fox did an ad for a couple of candidates 
supporting embryonic stem cell research.  Rush commented that it looked, 
for lack of a better term, faked.  He moved his arms the way Michael J. 
Fox did in the ad, for a couple of seconds.  This video surfaced on a 
couple of networks, MSNBC included.  Rush saw that, and realized that 
they had completely taken that part out of context, sped it up, and 
looped it to make it look a *whole* lot worse than it was.  He called 
them on it on his radio show, and Joe Scarborough admitted that they 
had, in fact, manipulated the video to make it run longer*.
* http://newsbusters.org/node/9027

Another example came in the run-up to the 2004 elections.  A "breaking 
story" was presented on 60 Minutes by then regular CBS Evening News 
anchor Dan Rather, showing memos from Lt. George Bush's Texas Air 
National Guard days.  These proved that he was given special treatment 
to avoid combat, a claim made by the Kerry campaign.  There was just one 
*big* problem - the memos were fakes**.  In under 24 hours, a blogger 
reproduced one of the memos exactly - using 12-point Times New Roman 
font on Microsoft Word.  These documents were supposed to be from 1972. 
  Proportional fonts and computer-generated superscripts were not part 
of the TXANG's computer technology in 1972 - in fact, such a memo would 
have likely been typed on a regular impact typewriter.
** http://en.wikipedia.org/wiki/Rathergate

Yet another comes from polls.  Polls are used for a multitude of things, 
but many times, the polls themselves are the news.  (BTW - did you know 
that our Congress' approval rating is now lower than President Bush's?) 
  This was also evident around the 2004 election - nearly all the exit 
polls showed Kerry running away with the election***.  However, Bush 
easily won.  Later speculations included the Kerry camp leaking the 
polls.  However it came down, the polls were reported, and the polls 
were wrong.
*** 
http://en.wikipedia.org/wiki/2004_U.S._presidential_election_controversy,_exit_polls

Another way polls can give misleading results are in the questions. 
"Which plan for Social Security reform do you prefer - the increased 
contributions of the Democrats, or the gutting of the system by 
Republicans?"  Who wouldn't prefer "contributions" over "gutting"?

These three are some of the more egregious examples in recent memory. 
In the first, they knowingly manipulated the facts.  In the latter two, 
they failed to vet sources and resources, and used flawed techniques. 
(The linked article describes a group from the University of Utah, whose 
exit poll was very, very close to accurate.)

Walter Cronkite, an CBS anchorman for many, many years, used to end his 
newscasts by saying "And that's the way it is."  These days, we have 
access to the information to prove that it is, in fact, *not* the way it 
is.  But, when the majority of Americans still form their opinions about 
world events from these sources, it's frustrating to those of us who 
have seen a better way.  The current administration does not attempt to 
educate the public (another of my big gripes with them).  Why are tax 
cuts good?  Why is "gutting" Social Security actually the most caring 
thing to do?  Without them presenting their side, it's left to the 
alternative media and concerned individuals to do their best to get the 
word out.

It's good to see a balanced report like the one linked above - if you 
had never heard of global warming before, you would know both sides to 
the argument.  Throw in some science, showing alternate reasons for 
planetary temperature fluctuations (such as the earth's rotation, 
sunspot activity, and normal up-and-down cycles), and the majority will 
form the correct opinion - it is malarkey.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-16T09:10:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sm7m43pgvuas1sodn18auug9eakrfd1pnm@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <DP72i.185503$aG1.61145@pd7urf3no> <aaadneS9mb8c8NfbnZ2dnUVZ_g-dnZ2d@comcast.com>`

```
On Tue, 15 May 2007 20:33:35 -0600, LX-i <lxi0007@netscape.net> wrote:

>Rush saw that, and realized that 
>they had completely taken that part out of context, sped it up, and 
…[3 more quoted lines elided]…
>* http://newsbusters.org/node/9027

How does speeding it up make it last longer?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 38)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-16T19:53:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KO6dnd9XI9cnKNbbnZ2dnUVZ_i2dnZ2d@comcast.com>`
- **In-Reply-To:** `<sm7m43pgvuas1sodn18auug9eakrfd1pnm@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <DP72i.185503$aG1.61145@pd7urf3no> <aaadneS9mb8c8NfbnZ2dnUVZ_g-dnZ2d@comcast.com> <sm7m43pgvuas1sodn18auug9eakrfd1pnm@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 15 May 2007 20:33:35 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[7 more quoted lines elided]…
> How does speeding it up make it last longer?

The looping does that - the speeding up makes the gestures look more 
boisterous than they were.  One thing I left out of that was that later, 
Michael J. Fox said in an interview that he had taken too much of his 
medicine before shooting those spots, to make his symptoms more 
pronounced.  (I guess Parkinson's medicine is not one of those "if a 
little is good, more must be more good" things...)

But the clarifications aren't what makes the news - it's the original, 
sensational, emotional (and often fabricated) event.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-15T21:35:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5atd7iF2q51ueU1@mid.individual.net>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com...
> docdwarf@panix.com wrote:
>> In article <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com>,
>> LX-i  <lxi0007@netscape.net> wrote:
>snip

> With a 2-year-old, a kid in T-ball, a kid in baseball, the older two in 
> Cub Scouts, college courses, and spending time with my wife - I simply 
…[4 more quoted lines elided]…
>

Don't waste time here on my account, Daniel :-)

(Not that I don't appreciate your posts...)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-15T08:07:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ecWdneMNgqUgI9TbnZ2dnUVZ_gydnZ2d@comcast.com>`
- **In-Reply-To:** `<5atd7iF2q51ueU1@mid.individual.net>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <3-mdnWFhmK9fwdXbnZ2dnUVZ_rylnZ2d@comcast.com> <f29nks$ksv$1@reader2.panix.com> <kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com> <5atd7iF2q51ueU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:kKqdnXF_cObUndTbnZ2dnUVZ_rqhnZ2d@comcast.com...
…[13 more quoted lines elided]…
> Don't waste time here on my account, Daniel :-)

Heh - I'm not.  That was the original post, though, that took it from a 
military discussion to the more philosophical one that it has become.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** JB <hongedo@videotron.ca>
- **Date:** 2007-05-16T22:38:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<op.tsf9l9j8pvlc0o@lemou>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com>`

```
On Mon, 14 May 2007 05:24:52 -0400, <docdwarf@panix.com> wrote:
>
> ... and I, of course, am the King of England.  God Save the Me!

But of course, Yer Grandee!

I just found this particular bit o' history:

http://www.mises.org/misesreview_detail.asp?control=122&sortorder=issue

How tellin' nay?

Doris Skie
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-17T12:47:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179431251.889440.324250@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<op.tsf9l9j8pvlc0o@lemou>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou>`

```
On 17 May, 03:38, JB <hong...@videotron.ca> wrote:
> On Mon, 14 May 2007 05:24:52 -0400, <docdw...@panix.com> wrote:
>
…[11 more quoted lines elided]…
>

Yep, us Brits do spying, on the cheap, so much better than the Cousins
with all their technology. And, to ensure that your ally doesn't
renege on the deal you have to spy on him.

Did you know that American friendly fire incidents pre-date the Iraq
wars? I met an elderly director of the charity that I volunteer for
last night and he remembers, in WW2, when the USAF bombed Brighton. It
brought to mind the Milo Minderbender from Catch 22.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-18T12:01:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com>`

```
On 17 May 2007 12:47:31 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 17 May, 03:38, JB <hong...@videotron.ca> wrote:
>> On Mon, 14 May 2007 05:24:52 -0400, <docdw...@panix.com> wrote:
…[21 more quoted lines elided]…
>brought to mind the Milo Minderbender from Catch 22.

American friendly fire incidents occurred with some regularity during
the Vietnam War.  Not so much bombings but artillery fire.  I was
involved (the recipient as it were) of just such an incident.
Fortunately, no one was killed but our position was severally damaged.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-18T10:30:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4lr439ts3mfh1o2pf57rs4lmtgn96tqcu@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com>`

```
On Fri, 18 May 2007 12:01:28 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>American friendly fire incidents occurred with some regularity during
>the Vietnam War.  Not so much bombings but artillery fire.  I was
>involved (the recipient as it were) of just such an incident.
>Fortunately, no one was killed but our position was severally damaged.

Before friendly fire accidents were friendly sword swinging accidents.
The Fog of War has always existed.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-18T09:52:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179507143.231293.55110@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com>`

```
On 18 May, 17:01, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
> On 17 May 2007 12:47:31 -0700, Alistair
>
…[47 more quoted lines elided]…
> - Show quoted text -

I know blue-on-blue incidents are a regular feature of warfare but
surely the Vietnam war versions were mostly US on US and not US on
Allies? Vietnam is one of my occasional areas of interest and I have
certainly come across documentation of US on US friendly fire before.
I used to think that the film Platoon was a load of hog-wash until I
re-read a platoon leader's diary (Tim O'Brien: If I die in a combat
zone").
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-18T18:04:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XUl3i.192774$DE1.107081@pd7urf2no>`
- **In-Reply-To:** `<1179507143.231293.55110@h2g2000hsg.googlegroups.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com>`

```
Alistair wrote:
> On 18 May, 17:01, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
> 
…[61 more quoted lines elided]…
> 
I was aware of blue-on-blue but I saw a fairly recent reference in the 
Express where UK is now using the American 'friendly fire'.

Canada had its first blue-on-blue from USAF in Afghanistan some years 
back - the first troops we had lost since the Korean War.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-18T12:19:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tgrr43dukshp3ir4jqg4e4uq34ni26c8cd@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com> <XUl3i.192774$DE1.107081@pd7urf2no>`

```
On Fri, 18 May 2007 18:04:39 GMT, "James J. Gavan"
<jgavandeletethis@shaw.ca> wrote:

>I was aware of blue-on-blue but I saw a fairly recent reference in the 
>Express where UK is now using the American 'friendly fire'.

It's a bad idea to kill NFL stars with friendly fire.   So lie about
it.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-19T12:20:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4p8u43diacv24lpb9338531vlrgam4g52i@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com>`

```
On 18 May 2007 09:52:23 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 18 May, 17:01, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
>> On 17 May 2007 12:47:31 -0700, Alistair
…[56 more quoted lines elided]…
>zone").

Our main "allies" in Vietnam besides the South Vietnamese were the
South Koreans and the Australians.  They pretty much worked different
areas than the Americans and were independant.  My outfit did a brief
operation with the Koreans but all they ever did was camp with us and
then go off and do their thing in the morning.  So the majority of
friendly fire incidents were US on US.

Platoon is the only Vietnam war movie I've ever seen that gives an
honest depection of what it was really like.  Full Metal Jacket came
close but had too much fantasy in it to be as accurate.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-20T09:09:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179677387.454411.206360@w5g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<4p8u43diacv24lpb9338531vlrgam4g52i@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com> <4p8u43diacv24lpb9338531vlrgam4g52i@4ax.com>`

```
On 19 May, 17:20, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
> On 18 May 2007 09:52:23 -0700, Alistair
>
…[70 more quoted lines elided]…
> close but had too much fantasy in it to be as accurate.

Some of the Full Metal Jacket film was shot about 2 miles from where I
live.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 38)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2007-05-21T11:53:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o1g35313ofd4autb7os9ruj3dif2uhoenj@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com> <4p8u43diacv24lpb9338531vlrgam4g52i@4ax.com> <1179677387.454411.206360@w5g2000hsg.googlegroups.com>`

```
On 20 May 2007 09:09:47 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 19 May, 17:20, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
>> On 18 May 2007 09:52:23 -0700, Alistair
…[74 more quoted lines elided]…
>live.

Did you have to duck the shrapnel?  :)

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"My grandmother is over eighty and still doesn't need glasses. 
Drinks right out of the bottle." 
-- Henny Youngman 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 39)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-21T13:12:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179778358.333780.206810@y18g2000prd.googlegroups.com>`
- **In-Reply-To:** `<o1g35313ofd4autb7os9ruj3dif2uhoenj@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <f26uk5$h1d$1@reader2.panix.com> <j8qdnUrM29UTGNrbnZ2dnUVZ_iydnZ2d@comcast.com> <f299t4$1ea$1@reader2.panix.com> <op.tsf9l9j8pvlc0o@lemou> <1179431251.889440.324250@k79g2000hse.googlegroups.com> <i7jr4352t55h2kum16m07p16f7enm5b70o@4ax.com> <1179507143.231293.55110@h2g2000hsg.googlegroups.com> <4p8u43diacv24lpb9338531vlrgam4g52i@4ax.com> <1179677387.454411.206360@w5g2000hsg.googlegroups.com> <o1g35313ofd4autb7os9ruj3dif2uhoenj@4ax.com>`

```
On 21 May, 16:53, SkippyPB <swieg...@nospam.neo.rr.com> wrote:
> On 20 May 2007 09:09:47 -0700, Alistair
>
…[95 more quoted lines elided]…
> - Show quoted text -

I don't recall whether I was living here at the time that the film was
shot (no pun intended) but it was done on an army training base. The
scenes with what look like modern rubble strewn aircraft hangers came
from here. Palm trees in skips.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T08:56:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com>`

```
On Sat, 12 May 2007 20:49:56 -0600, LX-i <lxi0007@netscape.net> wrote:

>OK - bad example.  I see the high prison population as one of the causes 
>of the low crime rate.  So, the original statement becomes "If 
>[symptom], then why [cause]?"

Can you cite figures that support what you see?   It seems so
counter-intuitive that there would be more prisoners when there are
fewer criminals.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-14T15:52:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2a0k2$b1q$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>`

```
In article <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Sat, 12 May 2007 20:49:56 -0600, LX-i <lxi0007@netscape.net> wrote:
>
…[4 more quoted lines elided]…
>Can you cite figures that support what you see?

Oh, that doesn't matter anyways, Mr Brazee... later in the thread Mr 
Summers states that this sort of cause-and-effect reasoning doesn't work 
with those human-being-type people, anyhow... or something like that.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T12:51:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com>`

```
On Mon, 14 May 2007 15:52:34 +0000 (UTC), docdwarf@panix.com () wrote:

>>Can you cite figures that support what you see?
>
>Oh, that doesn't matter anyways, Mr Brazee... later in the thread Mr 
>Summers states that this sort of cause-and-effect reasoning doesn't work 
>with those human-being-type people, anyhow... or something like that.

It can be tough for any of us when someone brings up observations that
are counter to expectations we believe strongly in.

There are various options available.   The most common by far is to
deny the observations.    But there are others that take more work and
flexibility.

If empirical evidence doesn't show that my solution works, maybe it
isn't my basic assumptions that are wrong, it might just be the
implementation.   Some analysis and testing might come up with a
better solution that doesn't require too large of a change in my
beliefs.

Or if empirical evidence is supporting a solution that is unacceptable
to me, some analysis and testing may come up with an alternative
solution that works.

There are many ways of achieving a goal.    But we need to define the
goal properly (we want holes, not bits).    In this case, the goal is
neither punishment nor abortion - the goal is crime reduction.   If it
happens that the "wrong" process is working better, figure out why -
and then find a third path that works better than either.    (We don't
need to emulate Mussolini to make the trains run on time)

We're CoBOL programmers and our working environment is moving away
from our skills.    But our jobs aren't to write CoBOL, our jobs are
to process the data that enables our customers to do their jobs
better.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-15T10:34:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5as6fsF2pa737U1@mid.individual.net>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com...
> On Mon, 14 May 2007 15:52:34 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[33 more quoted lines elided]…
> better.

Another excellent statement , Howard. I agree wholeheartedly.

"Any fool can find fault; it takes a wise man to find fault wisely."

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-15T11:10:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com>`

```
On Mon, 14 May 2007 12:51:13 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Mon, 14 May 2007 15:52:34 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[33 more quoted lines elided]…
>better.   

Regarding the crime reduction...this started during the Clinton
administration when they (his administration dnd the Congress) put
more money into the states hands to train more police and put their
butts on the street.  Technology advances in CSI were also made
because of the additional funds being allocated.  With more police
with better tools on the streets, more arrests and convictions were
being made.  The federal and state legislatures followed this up with
new, longer sentencing guidlines which meant longer prison terms.  

Once Bush got in office, the monies for the extra police and tools was
cut off (had to pay for those tax cuts).  After 9/11 new rules and
procedures were developed by the feds, but little or no money was
given to the cities that needed it to meet these rules. Thus they had
to layoff cops.  Meanwhile all those longer prison sentences were
still being metted out albiet to fewer people but the effect was the
same.  Now, every nearly every prison in the US is over crowded.  In
many places, like Florida e.g., they've had to relase non-violent
offenders just to make room.

Some stats to point this out:  In 1999, the last year of the Clinton
administration, according to the FBI there were 14,355,600 arrests in
the US for crimes ranging from murder to vagrancy.  Drug abuse
violations accounted for 1,557,100 arrests (slightly more than the
arrests for DUI at 1,549,500) but property crime arrests (burglary,
larceny-theft, motor vehicle theft, and arson) accounted for the most
at 1,676,100.  In 1999, there was a 5 percent decrease in the number
of arrests nationwide.

In 2005, the last year for which statistics have been calculated,
there were 14,094,186 arrests occurred nationwide for all offenses
(except traffic violations), of which 603,503 were for violent crimes,
and 1,609,327 for property crimes. The number of arrests for drug
abuse violations in 2005 (an estimated 1.8 million arrests, or 13.1
percent of the total) was more than for any other offense.
Nationwide, the 2005 rate of arrests was estimated at 4,761.6 arrests
per 100,000 inhabitants; for violent crime, the estimate was 204.8 per
100,000; and for property crime, the estimate was 549.1 per 100,000.
Although the number of arrests in 2005 increased only a slight 0.2
percent from the 2004 figure, arrests for murder rose 7.3 percent.

Basically, the number of arrests (overall) has gone down because there
are less police on the streets.  Is there less crime being committed
as well?  With the large gap between the poor and the rich and even
the poor and the middle class in this country, I doubt it.  Poor
economics with few job joices for the disadvantaged and uneducated
generally props up the crime rate.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-15T16:52:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SI-dnWisOIZRpNfbnZ2dnUVZ_i2dnZ2d@comcast.com>`
- **In-Reply-To:** `<pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com> <pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com>`

```
SkippyPB wrote:
> Once Bush got in office, the monies for the extra police and tools was
> cut off (had to pay for those tax cuts).

You don't "pay" for tax cuts - they increase tax revenue!  Our nation is 
going through record levels of tax income.  Last month, with the Bush 
tax cuts in full swing, they broke the record!

http://news.yahoo.com/s/nm/20070425/us_nm/usa_treasury_taxes_dc_1

Pay for tax *cuts*?  How would you pay for a tax *hike*?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-16T09:16:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<so7m43hc8b4a3bsbrh09al39v5qlnl6lmb@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com> <pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com> <SI-dnWisOIZRpNfbnZ2dnUVZ_i2dnZ2d@comcast.com>`

```
On Tue, 15 May 2007 16:52:51 -0600, LX-i <lxi0007@netscape.net> wrote:

>You don't "pay" for tax cuts - they increase tax revenue!  Our nation is 
>going through record levels of tax income.  Last month, with the Bush 
>tax cuts in full swing, they broke the record!

They can increase tax revenue, or not, depending on where our economy
is on the Laffer curve.   In this case, it would have worked...

But Bush's tax cuts were more than compensated by the deficit, which
was a tax increase.     Well, admittedly, the wealthy got cuts that
were bigger than their share of the deficit - but the rest of us
weren't so fortunate.

The Republicans have been telling us for decades that a deficit budget
is a tax - and they were very correct.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-16T12:19:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<laam43t0d4j92rqtb8o4bjj2c4jdg6irlp@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com> <pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com> <SI-dnWisOIZRpNfbnZ2dnUVZ_i2dnZ2d@comcast.com>`

```
On Tue, 15 May 2007 16:52:51 -0600, LX-i <lxi0007@netscape.net> wrote:

>SkippyPB wrote:
>> Once Bush got in office, the monies for the extra police and tools was
…[8 more quoted lines elided]…
>Pay for tax *cuts*?  How would you pay for a tax *hike*?

Oh this is just too much for me to ignore.  The problem with the tax
cuts is they didn't help the people they were intended to help, the
middle class.  In fact the only people who really benefited from the
tax cuts are the .3% of the population that make more $1 million a
year.  They are able to rake in nearly 25 cents for every dollar they
make.  By contrast the largest wage group in the US are those that
make between $20-50 thousand dollars a year (33.2 % of the
population).  They get to pocket a whopping 14 cents of every dollar
they make.  How about the middle class?  Those making between 50 - 100
thousand a year get to pocket a whole 10 cents on the dollar.

Every millionaire I've heard interviewed has said they didn't need (or
want) a tax cut.  They can do just fine on their own.  It is the
middle class and the small business people that make the economy go
and they're getting screwed.  Bush's tax cuts shaved only a few
hundred dollars off of the tax bills of most Americans.

Here's something else for you to ponder.  The income gap in this
country has been widening since before Ronald Regan took office and it
has continued through all of the presidents since.  But what is
happening under Bush is unprecedented.  For the first time in our
history, so much growth has been siphoned off to a small wealthy
minority that most Americans are failing to gain ground even during a
time of economic growth and most recognize it.

Here's what the income gap really is about.  In 1969, General Motors
was the largest employer in the US (not counting AT&T which was a
government sponsored monopoly at the time).  GM paid its chief
executive, James M. Roche, a salary of $795,000 - equivalent of $4.2
million today adjusting for inflation.  GM workers at the time were
paid pretty well.  The average paycheck for a production worker in the
auto industry was $8,000 a year - more than $45,000 today.  GM workers
also received excellent health and retirement benefits (which are
hurting the company today).  The GM workers were considered solid
middle class then.

Today, Wal-Mart is the largest US employer with 1.3 million employees.
H.Lee Scott, its chairman, is paid almost $23 million - more than 5
times Roche's inflation adjusted salary.  Yet Scott's compensation is
not exceptional for the CEO of a large corporation these days.  The
wages paid to Wal-Mart employees, on the other hand, are low even by
current standards.  On average Wal-Mart's non-supervisory employees
are paid $18,000 a year, far less than half what GM workers were paid
35 years ago, adjusted for inflation.  And Wal-Mart is notorious for
how few of its workers receive health benefits and for the stinginess
of those few benefits some do get.  According to the federal Bureau of
Labor Statistics, the hourly wage of the average American
non-supervisory worker is actually lower, adjusted for inflation, than
it was in 1970.  Meanwhile CEO pay has soared from less than 30 times
the average wage to almost 300 times the typical workers wage.    

These people really need tax cuts?  These people need a break?  I
don't think so.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-18T08:06:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hLGdnY20vpGfLtDbnZ2dnUVZ_rHinZ2d@comcast.com>`
- **In-Reply-To:** `<laam43t0d4j92rqtb8o4bjj2c4jdg6irlp@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <f2a0k2$b1q$1@reader2.panix.com> <utah43hico8av2dkiq30ja8p9v9scladvv@4ax.com> <pmhj43ddkcva2p955psi1jndulns9obm8n@4ax.com> <SI-dnWisOIZRpNfbnZ2dnUVZ_i2dnZ2d@comcast.com> <laam43t0d4j92rqtb8o4bjj2c4jdg6irlp@4ax.com>`

```
SkippyPB wrote:
> On Tue, 15 May 2007 16:52:51 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[11 more quoted lines elided]…
> Oh this is just too much for me to ignore.

As is your reply - however, I'm going to be out of town for a few days. 
  I'll post a proper rebuttal when I return.  ;)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-14T18:52:06-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cmh43l64iqf7ahpsti3r3j81v2oajrc1n@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>`

```
On Mon, 14 May 2007 08:56:03 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Sat, 12 May 2007 20:49:56 -0600, LX-i <lxi0007@netscape.net> wrote:
>
…[6 more quoted lines elided]…
>fewer criminals.

Keeping career criminals behind bars longer would increase the
incarceration total while decreasing the crime rate assuming that each
career criminal commits on average n crimes where n is significantly
greater than 1 during the period the criminal is out of prison.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-15T07:49:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beej43dcn1t5pqg3lulb2f39pkokvm7smp@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <3cmh43l64iqf7ahpsti3r3j81v2oajrc1n@4ax.com>`

```
On Mon, 14 May 2007 18:52:06 -0300, Clark F Morris
<cfmpublic@ns.sympatico.ca> wrote:

>>Can you cite figures that support what you see?   It seems so
>>counter-intuitive that there would be more prisoners when there are
…[5 more quoted lines elided]…
>greater than 1 during the period the criminal is out of prison.

As long as the supply of criminals is a constant, and that the
criminals in prison don't learn new techniques and contacts to become
more effective criminals when they get out.

As with any reasonable sounding theory, the test is in the results.
What is the correlation between various levels of crime and these
policies?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-14T19:11:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2-KdnYpiTrdVldTbnZ2dnUVZ_hadnZ2d@comcast.com>`
- **In-Reply-To:** `<42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <f25ib8$2ag$1@reader2.panix.com> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 12 May 2007 20:49:56 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[4 more quoted lines elided]…
> Can you cite figures that support what you see?

I'll look for them when I finish my homework...  :)  I know I've seen 
some, but I can't remember exactly where.

> It seems so
> counter-intuitive that there would be more prisoners when there are
> fewer criminals.

Ah - not that there are fewer criminals, the crime rate is lower.  Those 
aren't exchangeable.  In fact, given that the number of criminals 
remains the same, as the prison population grows, the greater the 
percentage of criminals who are not on the streets committing more 
crimes.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-15T09:17:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2btqn$4ba$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <5vGdnWaTr9RD4dvbnZ2dnUVZ_jSdnZ2d@comcast.com> <42ug43lkkat75p9d107j1pt0ahblu5i42p@4ax.com> <2-KdnYpiTrdVldTbnZ2dnUVZ_hadnZ2d@comcast.com>`

```
In article <2-KdnYpiTrdVldTbnZ2dnUVZ_hadnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Howard Brazee wrote:

[snip]

>> It seems so
>> counter-intuitive that there would be more prisoners when there are
…[6 more quoted lines elided]…
>crimes.  :)

Is that it?  How curious... I guess the overall size and age of the 
population remains the same, too.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-12T23:07:48-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ofsc43t780tl0jbq8fh66r2kh7f0uka03c@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`

```
On Sat, 12 May 2007 08:22:18 -0600, LX-i <lxi0007@netscape.net> wrote:

>docdwarf@panix.com wrote:
>> In article <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>,
…[17 more quoted lines elided]…
>asking, "If I'm sweating so much, why am I so hot?"

If violent criminals are behind bars, they aren't out committing
violent crimes.  Keeping repeat offenders behind bars longer should do
good things for the crime rate.  On the other hand, jail sentences for
drug use seem to be random given the LARGE number of high profile
entertainers and athletes who are claimed to be users.  I would like
to see an amnesty for all convicted solely for possession and use
(this excludes dealers and traffickers).
>
>> (I believe it was Gladstone who said 'Liberalism is trust of the people, 
…[4 more quoted lines elided]…
>off on that one.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-13T05:22:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179058942.213126.32100@l77g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`

```
On 12 May, 15:22, LX-i <lxi0...@netscape.net> wrote:
> docdw...@panix.com wrote:
> > (I believe it was Gladstone who said 'Liberalism is trust of the people,
…[4 more quoted lines elided]…
> off on that one.  :)

Gladstone, male, former prime minister of the UK. Rescued fallen
women, as a hobby. nudge-nudge.

>
> --
…[14 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T08:54:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fptg43tj4i73k38t47r5rbrhtijmsj2mh3@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com>`

```
On Sat, 12 May 2007 08:22:18 -0600, LX-i <lxi0007@netscape.net> wrote:

>> Oh... is *that* why the USA has such a high percentage of the population 
>> incarcerated?
…[3 more quoted lines elided]…
>asking, "If I'm sweating so much, why am I so hot?"

We don't want to pay for crime, and we don't want to pay for jails -
what we want is to decrease the amount of crime.

That means give people hope and jobs and more to lose by risking what
they have by committing crimes.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-14T16:00:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2a13m$bpq$1@reader2.panix.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <fptg43tj4i73k38t47r5rbrhtijmsj2mh3@4ax.com>`

```
In article <fptg43tj4i73k38t47r5rbrhtijmsj2mh3@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Sat, 12 May 2007 08:22:18 -0600, LX-i <lxi0007@netscape.net> wrote:
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-14T19:08:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2-KdnYtiTreEldTbnZ2dnUVZ_hadnZ2d@comcast.com>`
- **In-Reply-To:** `<fptg43tj4i73k38t47r5rbrhtijmsj2mh3@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com> <DOGdneB1jp49UNjbnZ2dnUVZ_vrinZ2d@comcast.com> <fptg43tj4i73k38t47r5rbrhtijmsj2mh3@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 12 May 2007 08:22:18 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[10 more quoted lines elided]…
> they have by committing crimes.

Why is it my responsibility to give someone else hope?  Are they not 
capable of manufacturing it on their own?  I'm all for charity, don't 
get me wrong - but someone sitting around waiting to be given hope has 
the wrong mindset.

There are means whereby people can better their lives, and you touched 
on a few above.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T08:49:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mktg43d8iu9upk431ke8d1eetvgsbjr8ap@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <f23t3c$lsi$1@reader2.panix.com>`

```
On Sat, 12 May 2007 08:15:41 +0000 (UTC), docdwarf@panix.com () wrote:

>>Yes - increased enforcement makes more people obey the law; not because 
>>they think it's a good law, but because they want to avoid the penalties 
…[3 more quoted lines elided]…
>incarcerated?

We have lots of instances where a mayor increases the budget of the
law enforcement, but the statistics are much less convincing that this
sensible seeming premise is true.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T08:47:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hbtg435e0f2poiemt9e36fp20klpakjfg8@4ax.com>`
- **References:** `<0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com>`

```
On Fri, 11 May 2007 16:41:38 -0600, LX-i <lxi0007@netscape.net> wrote:

>> But if you care about both issues (crime & abortion), it would be
>> worth analyzing to see if the root cause shown here (fewer hopeless
…[7 more quoted lines elided]…
>would that law be?!?)

Think of alternatives to "it was caused by abortion", such as "it was
caused by fewer children growing up unwanted and without hope".   It
can be very useful to look at the problem and desired result in a
different way.     The same data looked at this way can lead to
alternative solutions that are more satisfying.

>Besides, if we start trying to pre-judge people, we're in very dangerous 
>territory.  The entire concept of "innocent until proven guilty" would 
>go out the window.

I don't see the connection between this paragraph and the thread.
Who's being pre-judged?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-14T19:04:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2-KdnYhiTretmtTbnZ2dnUVZ_hadnZ2d@comcast.com>`
- **In-Reply-To:** `<hbtg435e0f2poiemt9e36fp20klpakjfg8@4ax.com>`
- **References:** `<0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <3u0943h7qhvtimhlu325hri6rsabmv1q39@4ax.com> <NqednWVQANW4bNnbnZ2dnUVZ_uejnZ2d@comcast.com> <hbtg435e0f2poiemt9e36fp20klpakjfg8@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 11 May 2007 16:41:38 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[11 more quoted lines elided]…
> caused by fewer children growing up unwanted and without hope".

But what about "it was caused by fewer babies being conceived"? 
Responsible behavior goes a long way toward eliminating crime.

> It
> can be very useful to look at the problem and desired result in a
> different way.     The same data looked at this way can lead to
> alternative solutions that are more satisfying.

I agree.

>> Besides, if we start trying to pre-judge people, we're in very dangerous 
>> territory.  The entire concept of "innocent until proven guilty" would 
…[3 more quoted lines elided]…
> Who's being pre-judged?

The babies being aborted - convicted before they even left the womb.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-14T15:11:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<134hgk64mehrieb@news.supernews.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
LX-i wrote:

> Ah - the Roe effect.  :)  I don't think it would account for a 50%+
> drop in crime in 8 years...

In 1982 there were an estimated 75,000 abortions in Florida. That's 75,000 
fewer potential voters in the 2000 election - where Bush carried Florida by 
a mere 500-odd votes.

While there are many good arguments on both sides of the abortion issue, I'm 
afraid I have to come down in favor since it manifestly reduces the number 
of eventual Democratic voters. Abortion is the Democrats version of eating 
the seed corn.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-15T10:59:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5as7v9F2ppmjeU1@mid.individual.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:134hgk64mehrieb@news.supernews.com...
> LX-i wrote:
>
…[13 more quoted lines elided]…
>
Republicans have abortions too... They just do it quietly behind closed 
doors and  are more likely to exercise this option when a baby would be 
"inconvenient".

The reasons for having an abortion or not don't really matter. Anyone 
considering one, will have what they believe is at least one good reason.

Ultimately, a woman has the same right to have a baby or not as she has to 
undergo surgery or not.

I reckon this whole nine months of humping a great lump around is not a 
reasonable proposition, and anyone who hasn't done it, (or hasn't got  the 
capability to do it), shouldn't get to vote. One of my close friends (who is 
a girl of very slight stature) is carrying a huge lump that should have 
arrived on Sunday but is still not ready to present itself. Seeing her 
discomfort (and she and her husband really WANT this second baby) made me 
think about what women have to endure... I can tell you now, I don't reckon 
I could do it (even if the appropriate plumbing was in place). Men should 
butt out of this argument. It should be decided by women and women alone.

If men really want to earn a place in this argument, then we should engineer 
things so that women can lay an egg  a few weeks into pregnancy, and the 
nurture of said egg would be a joint responsibility. Men could then 
legitimately have a say in whether or not the egg gets to hatch.

Oviparous mammals are not a new thing, both the echidna and the platypus 
reproduce this way...

(You don't see echidnas ambushing abortion clinics, murdering surgeons,  or 
platypuses marching on Canberra to get abortion laws changed...)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-15T07:59:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net>`

```
On Tue, 15 May 2007 10:59:53 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Republicans have abortions too... They just do it quietly behind closed 
>doors and  are more likely to exercise this option when a baby would be 
>"inconvenient"

One abortion position which is pretty common, is the one espoused by
our President's father while in office.    That was that abortion
should be illegal except in the case of rape, incest, or to save a
mother's life.

Pretty much all positions agree that it is acceptable to kill to save
one's life, so I won't go into that.    But the other arguments bother
me.    Since nobody believes that we have the right to kill a person
produced by rape or incest, then people who have that belief do not
believe embryos (or maybe even fetuses) are people.    If they aren't
people, then the argument is "I don't think it is right, therefore I
will make it illegal".    And what's worse is that there is an
argument of "good girls can have abortions, bad girls should be
punished with motherhood".   Both of these arguments are wrong, wrong,
wrong.

The person who believes that an embryo or a fetus is a person have a
much stronger moral position.   (As are those who don't believe this,
and act accordingly).    That "compromise" doesn't work.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-15T12:24:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179257062.191706.296220@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com>`

```
On 15 May, 14:59, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 15 May 2007 10:59:53 +1200, "Pete Dashwood"
> One abortion position which is pretty common, is the one espoused by
> our President's father while in office.    That was that abortion
> should be illegal except in the case of rape, incest, or to save a
> mother's life.

All this argument about abortion is really a waste of time. NONE OF US
IS A WOMAN. As my mother used to say, "If men had to give birth then
abortion would be available on demand".

In the case of a woman being harmed by carrying to term a child, then
it is right to permit abortion.

In the case of a rape victim, where her rights have been ignored by
the perpetrator (who should be in the over crowded jails anyway), it
is not morally justifiable to force her to carry to full term and deny
her an abortion. Are the rights of the rapiust to be held above that
of the unwilling mother?

In the case of incest, there are good health grounds for permitting
abortion. You only have to look at the products of the various
European Royal houses to know that abortion should be compulsory for
incest (and that marriage between cousins, uncles and nieces, etc.,
should be discouraged).

Finally to the case of abortion on demand: as a means of birth control
this should be avoided (there are morning-after pills which cover this
situation), in part because of the risk to the parent and to
discourage profligacy. However, unless there is a track record with
the mother of using abortiuon as a means of birth control, then
abortion should be on demand.

As to the question of what is a foetus and what is a child. Bertrand
Russell points out that with 95% of all conceptions ending in
spontaneous abortions then the Roman Catholic church should be very
busy burying all of the lost souls. A foetus is not a child. The
medical successes in enabling premature births to live from 24 weeks
onwards (and earlier?) is not mirrored in nature and usually results
in serious adverse medical condition for the foetus (such as under-
developed lungs and vestigial brains). Just because we can keep a
premature baby alive does not mean that we have the right to condemn
that foetus to ill health and a poor standard of life. And what about
the parents and nurses who have to look after the prematures? A
substantially premature birth of a non-viable (outside of an incubator
and life support machine) foetus can not be considered to be a baby
if only because you would have to handle all spontaneous abortions as
premature deaths. If you want to call a foetus a baby, then you should
start at the point of conception and accord the foetus (and the
blastula) human rights. After all, if chimpanzees are soon to be given
human rights then so should blastulae.

One classic argument for abortion is that picture referenced on this
newsgroup showing Bush giving the devils horns hand signal. If the
picture is not a fake then the man should make a full and public
apology before resigning from office and returning to the bottle.

>
> Pretty much all positions agree that it is acceptable to kill to save
…[12 more quoted lines elided]…
> and act accordingly).    That "compromise" doesn't work.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-15T13:39:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com>`
- **References:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com>`

```
On 15 May 2007 12:24:22 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

I am limiting my response to a couple of statements you made:

>All this argument about abortion is really a waste of time. NONE OF US
>IS A WOMAN. 

I'm not a member of an endangered species, but I have opinions about
them.   I'm not a sailor, but I can have an opinion on naval defense.
I'm not a child, but I support protecting children.   I am not in a
nursing home, but have opinions about them.   I am not a soldier, but
I have an opinion about Iraq.    I have never been a slave, but I have
an opinion on slavery.

That is a bogus argument.

>As my mother used to say, "If men had to give birth then
>abortion would be available on demand".

But lots of women are anti-abortion.   Women are as split on this
issue as men are.

=====
The rest of your discussions were about the abortion issue in general,
not the specific compromise position that I addressed.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-16T11:57:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5auvmmF2q9i8jU1@mid.individual.net>`
- **References:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com...
> On 15 May 2007 12:24:22 -0700, Alistair
> <alistair@ld50macca.demon.co.uk> wrote:
…[4 more quoted lines elided]…
>>IS A WOMAN.

Well, there are certain posts here that make me wonder... :-)
>
> I'm not a member of an endangered species, but I have opinions about
…[6 more quoted lines elided]…
> That is a bogus argument.

I understand what you are saying Howard, but I think this is a "special 
case"... Here's why I think that:

In all of the examples you cite above, your opinion about it doesn't change 
it. (It could if you join an action group and try to get some particular 
policy implemented, but simply having an opinion about it doesn't affect it, 
and we all have a right to our opinions, in a free society.)  Most 
importantly, you COULD be involved in any of the situations you outline and 
the arguments could therefore apply to you.

However, when it comes to abortion or giving birth, ANY opinion held by 
non-participants is simply muddying the water. It would be like you having a 
strong opinion about who should be the Mayor of my local council. You are a 
non-participant. That doesn't mean you can't have an opinion, but if there 
was a heated political debate going on here (...that's an amusing idea... 
:-)) any contribution you made would be seen as inflammatory by those 
opposed to it, and pointless by those in favour, because you cannot vote...

In all of your examples above you have as much right to an opinion as anyone 
else, (because you are a possible participant) but when it comes to a 
process that ONLY women can undergo do you (or any of us) still have the 
same moral right?

I don't think so, (but I agree it is arguable.)

>
> But lots of women are anti-abortion.   Women are as split on this
> issue as men are.
>

Yes, but the difference is that they have a right to argue it; the rest of 
us, in my opinion, don't.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-16T07:09:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179324598.447260.300990@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5auvmmF2q9i8jU1@mid.individual.net>`
- **References:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <5auvmmF2q9i8jU1@mid.individual.net>`

```
On 16 May, 00:57, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Howard Brazee" <how...@brazee.net> wrote in message
>
…[58 more quoted lines elided]…
> .

Well said Pete. For the second time, I agree with you and therefore
you must be right.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-16T09:25:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<048m43dolo0425r22vcjhk2a17qdsp75m4@4ax.com>`
- **References:** `<i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <5auvmmF2q9i8jU1@mid.individual.net>`

```
On Wed, 16 May 2007 11:57:09 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>In all of your examples above you have as much right to an opinion as anyone 
>else, (because you are a possible participant) but when it comes to a 
…[11 more quoted lines elided]…
>us, in my opinion, don't.

First they came for the Jews
and I did not speak out
because I was not a Jew.
Then they came for the Communists
and I did not speak out
because I was not a Communist.
Then they came for the trade unionists
and I did not speak out
because I was not a trade unionist.
Then they came for me
and there was no one left
to speak out for me.
-Attributed to Pastor Martin Niemoller
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-17T14:05:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b1rirF2qs18kU1@mid.individual.net>`
- **References:** `<i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <5auvmmF2q9i8jU1@mid.individual.net> <048m43dolo0425r22vcjhk2a17qdsp75m4@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:048m43dolo0425r22vcjhk2a17qdsp75m4@4ax.com...
> On Wed, 16 May 2007 11:57:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[26 more quoted lines elided]…
> Then they came for me

... and found me long gone. I took the hint after the Jews, Commies, and 
Unionists. Decided to go and live somewhere else, where nobody comes for 
anybody, and being different is seen as valuable... :-)

Pete.



> and there was no one left
> to speak out for me.
> -Attributed to Pastor Martin Niemoller
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-17T12:29:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179430194.581121.56160@l77g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<5auvmmF2q9i8jU1@mid.individual.net>`
- **References:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <5auvmmF2q9i8jU1@mid.individual.net>`

```
On 16 May, 00:57, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

> >>All this argument about abortion is really a waste of time. NONE OF US
> >>IS A WOMAN.
>
> Well, there are certain posts here that make me wonder... :-)
>

Did my propensity for wearing womens' undies give me away?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-18T09:53:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b4176F1ejsgtU1@mid.individual.net>`
- **References:** `<0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <5auvmmF2q9i8jU1@mid.individual.net> <1179430194.581121.56160@l77g2000hsb.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1179430194.581121.56160@l77g2000hsb.googlegroups.com...
> On 16 May, 00:57, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[8 more quoted lines elided]…
>

No, but thanks for telling us that... :-)

Pete
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-16T12:29:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com>`
- **References:** `<EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com>`

```
On Tue, 15 May 2007 13:39:43 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On 15 May 2007 12:24:22 -0700, Alistair
><alistair@ld50macca.demon.co.uk> wrote:
…[23 more quoted lines elided]…
>not the specific compromise position that I addressed.   

As a Roman Catholic I'm at odds with my church's position that all
abortions are wrong, that stem cell research is wrong.  The problem I
guess I have is that neither science nor religion (bible) defines when
an embryo becomes a person.  The Catholic church says embryo's are
persons but doesn't tell us when it is imbued with a soul.  The bible
is all over the place on this.

My personal belief is the same as Rudi Gulliani's, I'm morally opposed
to abortion because I'd rather err on the side of caution - i.e. a
soul is imbued and an embryo becomes a person at the moment of
conception - but it is the woman's decision.  She's the one carrying
the fetus, she's the one that will birth it, she's the one who would
have to live with whatever decision she makes.  Yes that decision
effects other people, but not to the same extent as the mother.  

If Roe vs Wade is ever overturned and there must be a law regarding
abortion, George H. Bush's offer is the most sensible.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-16T10:41:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fpcm4392q1ubbekplbpffmfmia6s9lagi3@4ax.com>`
- **References:** `<i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com>`

```
On Wed, 16 May 2007 12:29:30 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>As a Roman Catholic I'm at odds with my church's position that all
>abortions are wrong, that stem cell research is wrong.  The problem I
…[3 more quoted lines elided]…
>is all over the place on this.

Actually, the Bible has when the head passes the birth canal.   But
churches are very good at picking and choosing what parts of the Bible
apply - the poster child of this is in the anti-homosexual tirades.

>My personal belief is the same as Rudi Gulliani's, I'm morally opposed
>to abortion because I'd rather err on the side of caution - i.e. a
…[4 more quoted lines elided]…
>effects other people, but not to the same extent as the mother.  

If it is just a moral "abortion is wrong", then it certainly is a
woman's decision.   If it is determined that an embryo or a fetus is a
person, then it no longer is just her choice.

>If Roe vs Wade is ever overturned and there must be a law regarding
>abortion, George H. Bush's offer is the most sensible.

That it is a person except in case of rape or incest?  or is it that
"good girls should be allowed to have abortions, but bad girls should
be punished with motherhood"?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-17T13:16:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m73p43hojp2pt9bduudfcrum634mi69css@4ax.com>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com> <fpcm4392q1ubbekplbpffmfmia6s9lagi3@4ax.com>`

```
On Wed, 16 May 2007 10:41:33 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Wed, 16 May 2007 12:29:30 -0400, SkippyPB
><swiegand@Nospam.neo.rr.com> wrote:
…[11 more quoted lines elided]…
>

That's what Leviticus (old testment says).  There are a few places
where it says it is at conception.  I don't have the passages handy.

>>My personal belief is the same as Rudi Gulliani's, I'm morally opposed
>>to abortion because I'd rather err on the side of caution - i.e. a
…[9 more quoted lines elided]…
>

If it can be definitely stated and proven that an embryo is a person,
then abortion is certainly murder and should be illegal.  That level
of definition has not happened, so we are left with our own opinions
and morals on the issue.


>>If Roe vs Wade is ever overturned and there must be a law regarding
>>abortion, George H. Bush's offer is the most sensible.
…[3 more quoted lines elided]…
>be punished with motherhood"?

No, I guess the right thing would be to legislate that abortion is
only legal in a case to save the mother's life.  No other reason makes
sense.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-18T09:59:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b41h9F2q2jelU1@mid.individual.net>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com> <fpcm4392q1ubbekplbpffmfmia6s9lagi3@4ax.com> <m73p43hojp2pt9bduudfcrum634mi69css@4ax.com>`

```

"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:m73p43hojp2pt9bduudfcrum634mi69css@4ax.com...
> On Wed, 16 May 2007 10:41:33 -0600, Howard Brazee <howard@brazee.net>
> wrote:
…[48 more quoted lines elided]…
>

Ouch! Even if I couldn't think of any "other reasons" (and I can...) I'd 
still hesitate to make such a statement. (There could be "other reasons" I 
simply haven't thought of...)

This is an issue that obviously generates fiercely intense feelings on both 
sides.

Best left to those who are in the "qualified set" (women), in my opinion.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-16T19:57:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KO6dnd5XI9cJK9bbnZ2dnUVZ_i2dnZ2d@comcast.com>`
- **In-Reply-To:** `<atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com>`
- **References:** `<EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com>`

```
SkippyPB wrote:
> The problem I
> guess I have is that neither science nor religion (bible) defines when
> an embryo becomes a person.

"For it was You who created my inward parts; You knit me together in my 
mother's womb.  I will praise You, because I have been remarkably and 
wonderfully made." - Psalm 139:13-14a
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-17T13:38:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m3p43llct5a7061ocdth9e6kmod5vkbab@4ax.com>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <0k2k43th2jb1h24h6kvh6p4l0ocjeeudhp@4ax.com> <atbm439je1geqqdsviglkjl1jqv34lpq5j@4ax.com> <KO6dnd5XI9cJK9bbnZ2dnUVZ_i2dnZ2d@comcast.com>`

```
On Wed, 16 May 2007 19:57:34 -0600, LX-i <lxi0007@netscape.net> wrote:

>SkippyPB wrote:
>> The problem I
…[5 more quoted lines elided]…
>wonderfully made." - Psalm 139:13-14a

Psalm 139 has nothing to do with being born or when you are formed or
when you become a sentient human.  It is a hymnic meditation on God's
omnipresence and omniscience. The psalmist is keenly aware of God's
all-knowing gaze ( Psalm 139:1-6 ), of God's presence in every part of
the universe (Psalm 139:7-12), and of God's control over the
psalmist's very self (Psalm 139:13-16). Summing up Psalm 139:1-16,
17-18 express wonder. There is only one place hostile to God's
rule--wicked people. The psalmist prays to be removed from their
company (Psalm 139:19-24).  Read the whole thing, not just two
sentences.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-15T16:58:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com>`
- **In-Reply-To:** `<1179257062.191706.296220@o5g2000hsb.googlegroups.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com>`

```
Alistair wrote:
> One classic argument for abortion is that picture referenced on this
> newsgroup showing Bush giving the devils horns hand signal. If the
> picture is not a fake then the man should make a full and public
> apology before resigning from office and returning to the bottle.

It wasn't President Bush, it was his wife Laura.  The "devil horns" is 
actually a common gesture among fans of the University of Texas 
Longhorns.  It is usually accompanied by the exhortation to "hook 'em, 
horns!"

Context is everything...
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-16T07:08:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179324480.375305.229160@n59g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com>`

```
On 15 May, 23:58, LX-i <lxi0...@netscape.net> wrote:
> Alistair wrote:
> > One classic argument for abortion is that picture referenced on this
…[9 more quoted lines elided]…
> Context is everything...

The context was that the gesture was used in the precence of Her Most
Britannic Majesty Queen Elizabeth II and is wholly inappropriate.
Additionally, the horns gesture is viewed in some countries as
offensive and representing the devil. Is that really the action of a
moral Christian in the presence of royalty? What would his reaction
have been if the Queen had lifted her skirts, urinated and used the
USA flag to wipe her fanny?

>
> --
…[12 more quoted lines elided]…
> a man who's offended by a God he doesn't believe in?" - Brad Stine
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-17T14:23:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b1slfF2phfiaU1@mid.individual.net>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1179324480.375305.229160@n59g2000hsh.googlegroups.com...
> On 15 May, 23:58, LX-i <lxi0...@netscape.net> wrote:
>> Alistair wrote:
…[13 more quoted lines elided]…
> Britannic Majesty Queen Elizabeth II and is wholly inappropriate.

Perhaps. If she never saw the gesture, is it still offensive? Given the 
differences in culture and the fact that Ms Bush intended no disrespect, is 
it still offensive?

I think the Queen should decide what is offensive to her. If she didn't 
depart immediately or make some comment to an aide, then it's a fair bet she 
wasn't offended. If she wasn't offended, why should anyone else be? You may 
be overreacting, Alistair.

> Additionally, the horns gesture is viewed in some countries as
> offensive and representing the devil.

So is what we might consider a friendly wave, or the baring of knees... What 
is offensive in some cultures is not pertinent to the case in point. I'm 
sure Her Majesty keeps her knees covered and refrains from waving in 
cultures where this is considered offensive.


>Is that really the action of a
> moral Christian in the presence of royalty?

Er....it wasn't the Bush's royalty, Alistair. The Republic doesn't recognize 
such and affords respect out of courtesy, not from duty. As for the actions 
of a moral Christian, the gesture was NOT intended to be Satanic, so cannot 
be considered "unChristian".

> What would his reaction
> have been if the Queen had lifted her skirts, urinated and used the
> USA flag to wipe her fanny?

Well, she didn't, did she?

Hypothetical questions are best left unanswered. (especially ones that 
really boggle the mind :-))

Perhaps more is being read into an innocent gesture that was aimed at Bush 
supporters as a sign of solidarity, rather than as an offense to Her Majesty 
Queen Elizabeth.

My understanding is that the Queen wasn't bothered by it, why should we be?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-17T13:25:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net>`

```
On Thu, 17 May 2007 14:23:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
…[60 more quoted lines elided]…
>

I think the Queen was more bothered by Bush saying she was in
Washington DC in 1776 during her recent visit.  Of course he meant to
say 1976, but in true Bush faux pax it came out 1776.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-17T12:50:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179431406.860263.11520@y80g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com>`

```
On 17 May, 18:25, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
>
> I think the Queen was more bothered by Bush saying she was in
> Washington DC in 1776 during her recent visit.  Of course he meant to
> say 1976, but in true Bush faux pax it came out 1776.
>
These faux pas (plural?) seem to run in the Presidency. Or is it just
the Republican side of the Presidency?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-17T14:25:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uaep43l94i762d9abfqmvcc17d4csdn4st@4ax.com>`
- **References:** `<Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com> <1179431406.860263.11520@y80g2000hsf.googlegroups.com>`

```
On 17 May 2007 12:50:06 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> I think the Queen was more bothered by Bush saying she was in
>> Washington DC in 1776 during her recent visit.  Of course he meant to
…[3 more quoted lines elided]…
>the Republican side of the Presidency?


"Ich bin ein Berliner"


While we will never know what the Queen thought, I suspect she wasn't
insulted.   Her skin isn't that thin, and 1776 does fit easier on US
American tongues than 1976 does.    

In Heinlein's novel _Double Star_, the hero uses Farley files to check
up on everybody he needs to talk to, and it works fine - until he
talks naturally with the emperor.   He never took notes about him.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-18T12:07:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ehjr439a8s3n2svqbdkm33vvist96i7fjm@4ax.com>`
- **References:** `<Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com> <1179431406.860263.11520@y80g2000hsf.googlegroups.com>`

```
On 17 May 2007 12:50:06 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 17 May, 18:25, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
>>
…[6 more quoted lines elided]…
>

Just this Bush.  Others, I'm sure, have had similar misstatements, but
not with the same regularity.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I shot an arrow into the air, and it stuck."
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-18T10:08:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b422uF2qk4krU1@mid.individual.net>`
- **References:** `<LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com>`

```

"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:gt3p43dca4dic4t6htb8o10ceddpkiiq19@4ax.com...
> On Thu, 17 May 2007 14:23:42 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[77 more quoted lines elided]…
>

Yeah, that would have placed her age at around 231 years... Most ladies get 
sensitive about having their age over called... :-)

Don't know if you watch Dave Letterman. We get it here a few days after it 
airs in the US. He has a section of the show where he shows quick clips of 
inspiring Presidential speeches (Truman, Kennedy etc.) then shows Dubya 
stuttering, stumbling, getting names wrong, and generally behaving like a 
bumbling idiot. Sadly, he has a new clip every time the show airs (some of 
them are hilarious...even George must laugh when he sees it) and it doesn't 
seem like he is going to run out of material any time soon. It makes me 
wonder how someone who is so blatantly hopeless can hold the most powerful 
office on Earth. Guess it's who you know... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-17T12:42:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179430951.588683.101700@u30g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<5b1slfF2phfiaU1@mid.individual.net>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net>`

```
On 17 May, 03:23, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[65 more quoted lines elided]…
> - Show quoted text -

I do not know whether HMQE2 was offended or not. I believe that she
did not see the gesture but that the image would have been brought to
her attention. Add it to the "Yo! Blair!" and it raises the question
as to what constitutes the much vaunted special relationship and
whether the UK should continue to do business with puerile
democratically elected heads of state when there are some much better
behaved dictators that we can do business with (eg that nice Robert
Mugabe of Zimbabwe).
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-17T20:05:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9A23i.189149$DE1.183654@pd7urf2no>`
- **In-Reply-To:** `<1179430951.588683.101700@u30g2000hsc.googlegroups.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <1179430951.588683.101700@u30g2000hsc.googlegroups.com>`

```
Alistair wrote:
> On 17 May, 03:23, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[85 more quoted lines elided]…
> 
There's a famous photograph of our Quebec friend Pierre Elliott Trudeau, 
at Buck House I think, doing a dancing pirouette behind QE2's back while 
she is talking to some other diplomat.

There was also an incident where Pierre was talking to a crowd and one 
young 'Anglo' interloper prefixed his question with, "Well as the Mother 
Country.......... ?". P.E.T seethed and replied, "Well it *might* be 
your Mother Country but it's not mine !".

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-18T10:14:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b42daF2nf0l4U1@mid.individual.net>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com> <5b1slfF2phfiaU1@mid.individual.net> <1179430951.588683.101700@u30g2000hsc.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1179430951.588683.101700@u30g2000hsc.googlegroups.com...
> On 17 May, 03:23, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[87 more quoted lines elided]…
>
Yes, I take your point...

At least Dubya is a basically nice guy and mostly harmless...

Mugabe will fall. Such evil cannot persist indefinitely. Look at Amin...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-18T08:10:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hLGdnYy0vpFeLtDbnZ2dnUVZ_rHinZ2d@comcast.com>`
- **In-Reply-To:** `<1179324480.375305.229160@n59g2000hsh.googlegroups.com>`
- **References:** `<6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <mmej435c0ri3sf1mc319im622dt3fqd4fr@4ax.com> <1179257062.191706.296220@o5g2000hsb.googlegroups.com> <A8CdnRTuQoqMptfbnZ2dnUVZ_jWdnZ2d@comcast.com> <1179324480.375305.229160@n59g2000hsh.googlegroups.com>`

```
Alistair wrote:
> On 15 May, 23:58, LX-i <lxi0...@netscape.net> wrote:
>> Alistair wrote:
…[15 more quoted lines elided]…
> moral Christian in the presence of royalty?

Maybe he was showing her what it meant in Texas.  I don't think it's 
nearly as much as you're making it out to be...

> What would his reaction
> have been if the Queen had lifted her skirts, urinated and used the
> USA flag to wipe her fanny?

Who knows?  Bush is at his best when he skips the script and shoots from 
the hip (pardon the pun)...

(Oddly enough, flag desecration has been ruled to be protected 
expression under the First Amendment to our Constitution.  So, while 
some people would probably be righteously indignant, nothing much would 
have happened.)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-17T12:25:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179429943.754723.29130@e65g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<5as7v9F2ppmjeU1@mid.individual.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net>`

```
On 14 May, 23:59, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

> (You don't see echidnas ambushing abortion clinics, murdering surgeons,  or
> platypuses marching on Canberra to get abortion laws changed...)
>
> Pete.- Hide quoted text -
>
Shouldn't that be platypii?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-18T10:16:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b42hpF2qjcjlU1@mid.individual.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <1179429943.754723.29130@e65g2000hsc.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1179429943.754723.29130@e65g2000hsc.googlegroups.com...
> On 14 May, 23:59, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[8 more quoted lines elided]…
>
What colour are your knickers...?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-18T09:47:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179506824.281399.172540@n59g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<5b42hpF2qjcjlU1@mid.individual.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <1179429943.754723.29130@e65g2000hsc.googlegroups.com> <5b42hpF2qjcjlU1@mid.individual.net>`

```
On 17 May, 23:16, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[13 more quoted lines elided]…
> Pete.

Black today. I don't quite understand the sudden strong interest in my
underwear, unless you are referring to the other post. And maybe
echidnas should be echidnae.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-19T11:23:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b6qr5F2r3n89U1@mid.individual.net>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <1179429943.754723.29130@e65g2000hsc.googlegroups.com> <5b42hpF2qjcjlU1@mid.individual.net> <1179506824.281399.172540@n59g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1179506824.281399.172540@n59g2000hsh.googlegroups.com...
> On 17 May, 23:16, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[22 more quoted lines elided]…
>

I really hate explaining things, but, as I'm not Mary Poppins, I guess I'll 
have to...

1. A comment was made that some of the posts in this forum might be 
considered as coming from women (in the sense of "old women").

2. You responded that you sometimes like to wear women's underwear.

3. You then made a post that is trivial and pedantic (modern idiom does not 
require latin plurals in everyday speech; you can say indexes or indices, 
just as you can say platytpuses, octopuses, or echidnas... The Latin forms 
are more often used in a formal, technical, or scientific context; 
"antennas" (common speech referring to TV aerials), "antennae" (a technical 
paper on entomology)).

 In fact, publicly correcting to the Latin form might be considered as 
supercilious, if it were serious. (I'm hoping it wasn't and took it as a 
joke...)

4. Given the correction was a joke, I then linked to the previous reference, 
as a lighthearted response. The implication of my extremely rhetorical 
question (I certainly don't care about your underwear) was purely: "you are 
being an old woman; get a life".

Hope that covers it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-19T00:40:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2lh1s$nee$1@reader2.panix.com>`
- **References:** `<_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5b42hpF2qjcjlU1@mid.individual.net> <1179506824.281399.172540@n59g2000hsh.googlegroups.com> <5b6qr5F2r3n89U1@mid.individual.net>`

```
In article <5b6qr5F2r3n89U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I really hate explaining things, but, as I'm not Mary Poppins, I guess I'll 
>have to...
…[22 more quoted lines elided]…
>Hope that covers it... :-)

It appears to cover a few things, Mr Dashwood... perhaps including 'a joke 
explained is a joke lost'.

(... so it's getting dark, see, and the traveling percussion-instrument 
salesman - a real drummer's drummer! - stops by a farmhouse.  The farmer 
has two daughters, one named Lefty Echidna, on account of an accident she 
had resulting in the loss of two toes on her left foot, and the other 
named Righty Sloth, on account of an accident she had resulting...)

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-20T09:03:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179677003.051183.192070@w5g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5b6qr5F2r3n89U1@mid.individual.net>`
- **References:** `<xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <0c0c33h1fuaohs6s52mk70miaj4o3e9p1n@4ax.com> <EaadnfhA6NONAqvbnZ2dnUVZ_tijnZ2d@comcast.com> <i1me339j12t455lu2f78hht0gldrfioiv8@4ax.com> <LNGdnT7JUaJXjaXbnZ2dnUVZ_jqdnZ2d@comcast.com> <xvadnTMhBr5C197bnZ2dnUVZ8smonZ2d@pipex.net> <Q7WdnYV7r6RLdd7bnZ2dnUVZ_jednZ2d@comcast.com> <134hgk64mehrieb@news.supernews.com> <5as7v9F2ppmjeU1@mid.individual.net> <1179429943.754723.29130@e65g2000hsc.googlegroups.com> <5b42hpF2qjcjlU1@mid.individual.net> <1179506824.281399.172540@n59g2000hsh.googlegroups.com> <5b6qr5F2r3n89U1@mid.individual.net>`

```
On 19 May, 00:23, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[59 more quoted lines elided]…
> - Show quoted text -

It does. Thanks. I'm sorry but I insist on fora, indices, echidnae,
and octopii.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-21T01:52:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2qu1a$8iv$1@reader2.panix.com>`
- **References:** `<xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <1179506824.281399.172540@n59g2000hsh.googlegroups.com> <5b6qr5F2r3n89U1@mid.individual.net> <1179677003.051183.192070@w5g2000hsg.googlegroups.com>`

```
In article <1179677003.051183.192070@w5g2000hsg.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 19 May, 00:23, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
>wrote:

[snip]

>>  In fact, publicly correcting to the Latin form might be considered as
>> supercilious, if it were serious. (I'm hoping it wasn't and took it as a
>> joke...)

[snip]

>> Hope that covers it... :-)

[snip]

>It does. Thanks. I'm sorry but I insist on fora, indices, echidnae,
>and octopii.

'All at the same meal?'

'All on the same plate!' - B. Hill

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 17)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-30T10:34:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177954440.699544.303810@e65g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
On 30 Apr, 01:53, LX-i <lxi0...@netscape.net> wrote:
>
> And, I find it really strange that Pelosi and company didn't have time
…[4 more quoted lines elided]…
> terrorism)

<blood boiling mode>

And I presume that the good-ole US of A has not ever nor does it now
sponsor terrorism? Need I remind you of arms to Iran or of the
Contras? How about the continued support for the IRA and the
inconsistent support for the NI peace process ?

</blood boiling mode>
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 18)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-30T12:03:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<phbc33pko2c4fn22qmvkofbq2e7209aapq@4ax.com>`
- **References:** `<1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com>`

```
On 30 Apr 2007 10:34:00 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

><blood boiling mode>
>
…[5 more quoted lines elided]…
></blood boiling mode>

You know that virtually every politician defines "terrorism" as what
the other guys do.    Look at all the two-bit dictators who call their
revolutionaries by that "in" term now.

In the first half of the U.S.'s history, they almost always sided with
the "freedom fighters" - the revolutionaries.    The last half, the
U.S. was a big guy, and has sided with the establishment, unless that
revolution was against an established enemy.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 19)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-02T12:56:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178135794.772745.6990@c35g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<phbc33pko2c4fn22qmvkofbq2e7209aapq@4ax.com>`
- **References:** `<1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <phbc33pko2c4fn22qmvkofbq2e7209aapq@4ax.com>`

```

Howard Brazee wrote:
> On 30 Apr 2007 10:34:00 -0700, Alistair
> <alistair@ld50macca.demon.co.uk> wrote:
…[17 more quoted lines elided]…
> revolution was against an established enemy.

So General Pinochet being supported by the USA and CIA in an illegal
coup was supporting the establishment?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-30T20:50:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com>`
- **In-Reply-To:** `<1177954440.699544.303810@e65g2000hsc.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com>`

```
Alistair wrote:
> On 30 Apr, 01:53, LX-i <lxi0...@netscape.net> wrote:
>> And, I find it really strange that Pelosi and company didn't have time
…[13 more quoted lines elided]…
> </blood boiling mode>

Yes - we also supported the Taliban against the Russian-controlled 
Afghanistan government, for the same reason we supported the Contras - 
they fight against Communism.  We can only fight so many battles at a 
time, and have traditionally relied on diplomacy and the diplomacy of 
others to handle regional disputes.

I looked and didn't find anything describing US support of the IRA or 
the Northern Ireland peace process.  Maybe we screwed up - it certainly 
wouldn't be a first for our nation.  But the failures of the past are 
*no* excuse for continued failure.  Failure only stays failure if you 
fail to learn - and I'd like to think that we're learning as we go 
along.  (In Afghanistan, we knew what kind of weapons the Taliban had, 
because we had probably sold it to them!)

And, to the best of my knowledge, the IRA hasn't threatened our national 
security.  Though it makes for entertaining cinema, we're *not* the 
world police.

And a final point about Pelosi's trip - Syria harbors terrorists, is 
sympathetic to them, and is even letting them cross into Iraq to fight 
our (US) soldiers!  Why go see Assad?  Was Satan unavailable?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-01T16:20:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59ntg4F2lssg8U1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com...
> Alistair wrote:

>
> And a final point about Pelosi's trip - Syria harbors terrorists, is 
> sympathetic to them, and is even letting them cross into Iraq to fight our 
> (US) soldiers!  Why go see Assad?  Was Satan unavailable?
>
Well, during our daily chat ... (He comes to me for advice because I'm not 
Judgemental...)...He let it slip that He is pretty tied up with Africa right 
now, and that BBC documentary refuting "An inconvenient truth" is taking a 
lot of promotion, although He seemed pretty smug about the inroads it is 
making into undermining the global warming myth. ('Course, we'd expect that 
from someone who prefers it hot...).

What with all that, and the Four Horsemen not really trying... (a few penny 
ante skirmishes; no decent Global conflict for over half a century now), 
some minor famines and pestilences. The Death stats are pretty steady but 
that's only because of the increasing birth rate globally. The Pale Horse is 
about ready for the knacker's yard and there is a real risk He could be 
stripped of His title of Lord of the Flies... (Evil doesn't have the appeal 
it once had in a repressed population; kids now can go to a concert and get 
it all out of their systems...). You should have heard Him moaning about how 
hard it is to get good help, and what a miserable job it is to be a 
Manager...Then there are the Powers-that-Be to whom He must answer... (hints 
have been dropped that if the World doesn't get worse, they may be looking 
for a new entity to bring a fresh new image to the business of Evil...)

He's really got  a lot on His mind...

And Assad is a perfectly good stand in...

Pete.

> "Who is more irrational?  A man who believes in a God he doesn't see, or a 
> man who's offended by a God he doesn't believe in?" - Brad Stine

I still think they both need help... :-)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-30T23:00:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`
- **In-Reply-To:** `<59ntg4F2lssg8U1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com...
…[11 more quoted lines elided]…
> from someone who prefers it hot...).

ha!  You mean he's trying to keep it from being seen...  :)  (The idea 
that we as humans can control the planet is absolutely arrogant and 
untrue - and I'll leave it at that.)

> What with all that, and the Four Horsemen not really trying... (a few penny 
> ante skirmishes; no decent Global conflict for over half a century now), 
…[11 more quoted lines elided]…
> He's really got  a lot on His mind...

Sounds like it.  I bet you charge him a pretty penny for judgment-free 
consulting!

> And Assad is a perfectly good stand in...

OK - I suppose...  I still don't see why we can't charge her with 
treason, though. (Well, following the Vietnam precedent, I guess we can't.)

Let me just say that if *I* were in Baghdad, fighting these al-Qaeda 
guys from Syria, and the Speaker of the House of *my* nation went over 
there to make nice with their president - I'd be even more upset than I 
am now.  Differing with the President on the merits or prosecution of 
the war is perfectly fine, but when we do commit, we need to follow 
through.  A headline on an article I saw today pretty much echoes what 
I've said before; "Even if going to Iraq was a mistake, leaving now 
would be an even bigger one."

(yes, I know your original post was in jest...  I didn't mean to turn it 
back from that, this is just something that I simply cannot believe is 
being allowed to happen in the country that I know, love, and defend. 
There is an entire party that has, as their platform, the downfall of 
one man.  They don't care what that man's downfall does to our nation. 
Somehow, in November last year they convinced enough people that they 
got a little power, and they started abusing that power almost from day 
one.  On my blog*, I wrote about why I thought this change in power took 
place, so I won't rehash it here, especially in response to a 
light-hearted post.)

* http://www.djs-consulting.com/personal/2006/why-the-republicans-lost

>> "Who is more irrational?  A man who believes in a God he doesn't see, or a 
>> man who's offended by a God he doesn't believe in?" - Brad Stine
> 
> I still think they both need help... :-) 

Have you ever seen the wind?  I've seen the trees moving and the 
tumbleweeds tumbling, but I don't think I've ever seen the wind.  Just 
because something is invisible doesn't mean it's not real.  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-01T09:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f170o0$1p3$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`

```
In article <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>OK - I suppose...  I still don't see why we can't charge her with 
>treason, though.

Plural majestatus est; I do not know what 'we' you refer to but I've heard 
that, in general, attorneys like to pick fights they believe they can win.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-02T01:14:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59osq4F2l93pkU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[36 more quoted lines elided]…
>

Well, I like to help, and I can relate to some of His problems...

(There was talk of a deal involving my immortal soul, but Mephistopheles had 
it appraised (Mordecai's Demonic Cash Conversion - three brass balls and old 
gold bought and sold...) and it was found to completely worthless, so I'm 
pretty safe really...)


>> And Assad is a perfectly good stand in...
>
…[5 more quoted lines elided]…
> make nice with their president - I'd be even more upset than I am now.

Seriously, Daniel, I completely understand this. Most of the time I am proud 
to be a Kiwi (although I am aware that patriotism and blindly following the 
people in power is a major contributing factor to War and heartbreak), but 
there have been two occasions in my life when I was ashamed for my country. 
One of them was when our current Prime Minister went and embraced the 
President of France (after they had committed terrorist acts on our shores 
and never apologised for it; the same nation that feted the bombers as 
heroes and decorated them when they returned home.)  Very much like the 
"cozying up to the enemy" you are describing.

[The other time was when a now dead ex Prime Minister reneged on the ANZUS 
treaty in order to fulfill his own political aspirations and buy the 
anti-nuclear/anti-American vote. (As if anyone actually WANTS nuclear 
weapons; but they have served their purpose for over 50 years now and it is 
just strupid to pretend we don't need them.). To me, that made our whole 
contribution to VietNam a farce (very personal... I lost a good friend 
there, was trained for it, and only missed going by the skin of my 
teeth...), and it simply dismissed the sacrifice of young Americans who died 
at Coral Sea to keep us free. Even the Australians were ashamed of us and 
that's pretty hard for any Kiwi to take... :-)]

I would feel exactly as you would under these circumstances.

It IS treason. Looking for peace is one thing; (sometimes you have to visit 
the enemy to do that) but making political capital is quite another.


>Differing with the President on the merits or prosecution of the war is 
>perfectly fine, but when we do commit, we need to follow through.  A 
>headline on an article I saw today pretty much echoes what I've said 
>before; "Even if going to Iraq was a mistake, leaving now would be an even 
>bigger one."

I'm still not persuaded it was a mistake to go there. Someone had to stop 
Saddam. Who else had the capability?

I do think that it wasn't thought through properly (it could've been 
resolved with Desert Storm if they had let Stormin' Norman have his way... 
he wanted to take Saddam out then, but was forbidden, for fear they might 
get someone worse...), and I also think that the feelings and culture of the 
Iraqi people were neither considered properly, nor understood. That is why 
it is such a problem even now. As long as you have people who believe they 
will go to Heaven for killing and maiming others, there is not much you can 
do.

The only way to "win" in Iraq is for the Iraqi people to have their minds 
changed. This happens by example and education.They need to see that 
Democracy and a Secular State is not perfect, but is way better than a 
feudal system based on religious intolerance.

Exactly this process is occurring in Turkey at the moment. Kemal Ataturk 
imposed a Secular State in 1923 and prohibited the wearing of Muslim dress 
by women, or any form of public "parading"of Islam (although, of course, 
people were free to practice their religion in private.) Now there is a move 
by a vocal fundamental minority, riding the Middle Eastern Islamic political 
bandwagon, to set Turkey back a couple of hundred years and make it another 
Islamic state.

I was very relieved to see there have been huge (peaceful) public protests 
against this, and the numbers are making the political Islamists think 
again. The Turks love Democracy and are happy to be for the most part, 
Muslim, but with a Secular State. This is probably the best future for 
Islam. They deserve the support of all of us.

>
> (yes, I know your original post was in jest...  I didn't mean to turn it 
…[19 more quoted lines elided]…
> because something is invisible doesn't mean it's not real.  :)

It isn't about visibility, it's about perception. What is real for us is 
what we perceive to be real. There are fundamental blocks to my perception 
of God, that are nothing like perceiving the wind (even if you can't see it, 
you can certainly feel it). Because perception is a very personal thing, I 
know that different people will have different views on this, and I'm really 
fine with that. My failure to believe in God or Satan or any other such 
entities, in no way undermines anyone else's right to do so, and I treat all 
such beliefs with respect. (If faith was adhered to only because other 
people did so, or because that was the finding of the majority, it wouldn't 
be much of a faith, would it?)

My respect stems, not from the fact that these are great beliefs (although 
some of them certainly are, and can cause people to do the most 
extraordinary things for good as well as bad), but rather from the fact that 
I spent nearly 30 years investigating belief systems and faiths and realised 
that they are currently woven into our society and are part of what makes us 
Human Beings.

I would like to see them slowly disentangled from our lives and see people 
living in harmony without the fear of Hellfire, or requiring imaginary 
friends to prop them up in adversity, but that won't happen in my lifetime 
and I currently estimate around another 1500 years.

It will be a long, slow process and the key is education. As people become 
educated they ask more pertinent questions. They are unsatisfied with the 
arguments from priestly authority, or the dogma served up by a church. In 
other words, as people gain the yearning for learning they start to think 
and question. If there really is a divine power it will eventually become a 
personal one, and each man will know why he believes  (or doesn't). At this 
point, each person accepts his faith (or lack of it) as personal and sees no 
desire to inflict it on others or go and kill them for not sharing it. That 
would be a "mature" faith, in my opinion.

I don't think people who see flying saucers or even who claim alien 
abduction are necessarily irrational.  (See... non-judgemental... :-)) 
Experience has taught me that our perceptions can be misled, and sometimes 
downright tricked. I've seen white tigers disappear before my eyes, I've 
watched a person cut in half with a chain saw and saw the two halves 
separated, I've seen an Indian magician produce limitless quanties of water 
from a small ewer, I've seen a man actually have his tongue cut off (and I 
handled the piece of tongue to ensure it was real... it was...), I saw 
Copperfield vanish the Statue of Liberty, and I've been totally convinced 
that one shape is larger than the other when they are both the same. Does 
that make me irrational? I hope not.

I don't think people who believe in a God they cannot perceive are 
necessarily irrational. (Even though that doesn't work for me...)

I don't think people who are offended by a God they don't believe in, are 
necessarily irrational, even though THAT doesn't work for me either.

The question is a loaded one and really is just a rhetorical device. It is a 
pity such devices are even considered necessary when defending the faith....

I understand your tag lines, Daniel, but it irritates me a bit because it 
implies that there are only two options. I see more than that.

(Nevertheless, I will defend to the death your right to post them... :-))

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-01T22:00:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M4ydnYL2jNttkaXbnZ2dnUVZ_uSgnZ2d@comcast.com>`
- **In-Reply-To:** `<59osq4F2l93pkU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <59osq4F2l93pkU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com...
…[12 more quoted lines elided]…
> there have been two occasions in my life when I was ashamed for my country. 
[snip]
> I would feel exactly as you would under these circumstances.
> 
> It IS treason. Looking for peace is one thing; (sometimes you have to visit 
> the enemy to do that) but making political capital is quite another.

I appreciate the stuff I snipped; it's good to know that someone outside 
the country sees it the same way I do.

>> Differing with the President on the merits or prosecution of the war is 
>> perfectly fine, but when we do commit, we need to follow through.  A 
…[5 more quoted lines elided]…
> Saddam. Who else had the capability?

There was a quote in today's OpinionJournal.com's Best of the Web - I'll 
paste it here so I don't miss anything...

[quote]
Meanwhile, the Star-News of Wilmington, N.C., reports that "a 
17-year-old Swansboro High School student was in jail Friday on $1 
million bond after being charged with having a weapon of mass 
destruction--an assault rifle--on the school's campus."

If an "assault rifle" is a weapon of mass destruction, it seems likely 
that Saddam Hussein had them.
[/quote]

I don't think it was a mistake either.  But, bickerin...er, debating 
that is really pointless, seeing as how it is in the past.  That article 
was basically saying that even IF it was a mistake, we shouldn't 
compound them by leaving before the job is done.

> I do think that it wasn't thought through properly (it could've been 
> resolved with Desert Storm if they had let Stormin' Norman have his way...

Schwartzkopf is awesome!  :)  One of the coolest generals I can 
remember.  And, our incursion and retreat from Iraq in 1991 is a perfect 
illustration of what could (and most likely would) happen if we just 
packed up and left now.

> The only way to "win" in Iraq is for the Iraqi people to have their minds 
> changed. This happens by example and education.They need to see that 
> Democracy and a Secular State is not perfect, but is way better than a 
> feudal system based on religious intolerance.

They're coming around.  The locals are starting to work together with 
the Iraqi police against the increasingly-foreign-supplied terrorists, 
which is a first.

> Exactly this process is occurring in Turkey at the moment.
[snip]

I've been reading some Dinesh D'Souza columns lately.  His latest book 
contends that there is a large moderate Muslim group of people in the 
world, and that we (westernized people) should stop doing things to 
intentionally antagonize them.  (I'm not doing the concept justice - 
dineshdsouza.com has his columns, including his 4-column series on 
conservatives' criticism of his book.  It's pretty thought-provoking.)

[snip]
> The question is a loaded one and really is just a rhetorical device. It is a 
> pity such devices are even considered necessary when defending the faith....

In this particular one's case, though, this wouldn't even be an issue if 
some folks would just grow a bit thicker skin.  I wouldn't be offended 
by a Bhuddist prayer in public, or even at a government hosted event. 
(And, even if I *was* offended, I wouldn't dare say anything, so I 
wouldn't endure the wrath of the PC police!)  But, let it be a 
Protestant prayer, let it be something that's gone on for 200 years, and 
one thin-skinned, unhappy-with-the-world atheist decides to stop reading 
the First Amendment at the word "religion"*, now all of a sudden the 
99.999% of people who didn't care are now being told by .001% what they 
have to do.  I blame the people for being thin-skinned, and I blame the 
ridiculous interpretations of our laws for letting these hissy-fits 
stand in court.**

* Full text of Amendment 1 - "Congress shall make no law respecting an 
establishment of religion, or prohibiting the free exercise thereof; or 
abridging the freedom of speech, or of the press; or the right of the 
people peaceably to assemble, and to petition the government for a 
redress of grievances."

** For those of you who want to have fun with that paragraph, go ahead - 
I probably won't respond, but feel free...  :)

> I understand your tag lines, Daniel, but it irritates me a bit because it 
> implies that there are only two options. I see more than that.

No it doesn't.  :)  It just compares two different options.  It doesn't 
address people who don't care whether there's a God or not, or people 
who are offended at those who don't believe in God.  It doesn't even 
*begin* to address the poor dyslexic agnostic insomniac who can't get to 
sleep at night for wondering if there's a dog...

> (Nevertheless, I will defend to the death your right to post them... :-))

:)  I appreciate that.  Hopefully that will be a very long time.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-02T09:18:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f19l0m$p1j$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <59osq4F2l93pkU1@mid.individual.net> <M4ydnYL2jNttkaXbnZ2dnUVZ_uSgnZ2d@comcast.com>`

```
In article <M4ydnYL2jNttkaXbnZ2dnUVZ_uSgnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>There was a quote in today's OpinionJournal.com's Best of the Web - I'll 
>paste it here so I don't miss anything...
…[9 more quoted lines elided]…
>[/quote]

The article being cited is, I believe, the Police Blotter page of the 
Wilmington Star, 
<http://www.wilmingtonstar.com/apps/pbcs.dll/article?AID=/20070428/NEWS/704280389/1051/NEWS>

This shows, once again, that calling something (x) does not make it (x); 
Abraham Lincoln pointed that out over a century back using an example of a 
tail and a leg.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-01T09:47:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cvne33dfof0hab7ahd7ianco7eab97e2f0@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`

```
On Mon, 30 Apr 2007 23:00:07 -0600, LX-i <lxi0007@netscape.net> wrote:

>ha!  You mean he's trying to keep it from being seen...  :)  (The idea 
>that we as humans can control the planet is absolutely arrogant and 
>untrue - and I'll leave it at that.)

For various values of "control" and of "planet".    Obviously a dam
has an effect - as do farms, irrigation, chopping down forests and
jungles, etc.     They don't change the planet's path around the sun -
but they are changes nevertheless - caused by us.

Certainly there are things we do which effect where we live, and it is
possible to foul our nest.    I believe it is our moral duty to take
care of our planet - and there is a sufficient Biblical mandate to
back this up.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-01T22:26:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com>`
- **In-Reply-To:** `<cvne33dfof0hab7ahd7ianco7eab97e2f0@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <cvne33dfof0hab7ahd7ianco7eab97e2f0@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 30 Apr 2007 23:00:07 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[4 more quoted lines elided]…
> For various values of "control" and of "planet".

For the values that say we caused global warming.  :)  Dang - I guess I 
can't "leave it at that"...

> Obviously a dam
> has an effect - as do farms, irrigation, chopping down forests and
> jungles, etc.     They don't change the planet's path around the sun -
> but they are changes nevertheless - caused by us.

It turns out that another planet, Mars, has warmed in a similar manner 
as we have.  Hmm - no SUVs up there (unless you count the Mars Rover), 
no Halliburton, no carbon offsets.  (Although I *do* think the Martians 
use more than one square of toilet paper each time - maybe it's time for 
a Sheryl Crow Mars Summer Tour...)

The one thing we do have in common?  The sun, which is going through a 
"hotter" cycle right now.

> Certainly there are things we do which effect where we live, and it is
> possible to foul our nest.    I believe it is our moral duty to take
> care of our planet - and there is a sufficient Biblical mandate to
> back this up.

Good stewardship is one thing - radical environmentalism and the Church 
of Global Warming are entirely different.  I don't dump oil down a 
drain, I don't litter (and even make the neighborhood kids pick up trash 
they're trying to leave in my yard), I reuse as much as possible (easy 
on the wallet as well as the planet); heck, I don't even pee in the 
pool!  However, I refuse to be "guilted" into completely changing my 
lifestyle because someone thinks that all the advancements that we've 
made over that past few decades are going to kill our planet.  And, if 
you rewind the clock 30 years, it's global *cooling* that's going to 
kill us all.  I just find all of it ludicrous.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-02T09:22:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f19l8u$ibt$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <cvne33dfof0hab7ahd7ianco7eab97e2f0@4ax.com> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com>`

```
In article <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>And, if 
>you rewind the clock 30 years, it's global *cooling* that's going to 
>kill us all.  I just find all of it ludicrous.

Odd... didn't you say something along the lines of it would be a Good 
Thing were interactions between the sexes should be similarly 'unwound' by 
fifty years so that the Degradations of Womens' Liberation might be undone 
and barefoot, pregnant defenders-of-their-menfolk once again roam the 
land?

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-02T16:49:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com>`
- **In-Reply-To:** `<f19l8u$ibt$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <cvne33dfof0hab7ahd7ianco7eab97e2f0@4ax.com> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[11 more quoted lines elided]…
> land?

Uhh...  Not that I remember.  I may have said something that could be 
spun that way if pieces were taken out of context...  Do you remember 
what it was that I said?  :)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-03T00:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1b9n5$jru$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com>`

```
In article <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com>,
…[16 more quoted lines elided]…
>what it was that I said?  :)

I barely remember what *I* say, let alone anyone else... that might be a 
reason for my asking.  It is pleasant to learn that you don't believe that 
the changes made in the United States by the Women's Liberation Movement 
(espousers of the concept of feminism) need to be altered in the least.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-02T19:07:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`
- **In-Reply-To:** `<f1b9n5$jru$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[21 more quoted lines elided]…
> (espousers of the concept of feminism) need to be altered in the least.

Heh - and there's the spin.  Just because I didn't say we needed to go 
back 50 years doesn't mean that I agree with everything the feminist 
movement has done.  :)  You know it's not that cut-and-dried.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-02T22:05:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net>`
- **In-Reply-To:** `<tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`

```
LX-i wrote:
> 
> Heh - and there's the spin.  Just because I didn't say we needed to go 
> back 50 years doesn't mean that I agree with everything the feminist 
> movement has done.  :)  You know it's not that cut-and-dried.
> 
You confuse "feminist" with "feminist movement", and "specific feminist" 
or even use the terms interchangeably. I think that a huge mistake.  How 
can a "movement" do something?  *People* do things.  Movement is just a 
word that people make up for political reasons. They want to discredit 
Jane by pointing to Mary. The spin makers already control your thinking 
when you allow them to control your language.

Donald
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-03T20:18:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com>`
- **In-Reply-To:** `<MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net>`

```
donald tees wrote:
> LX-i wrote:
>>
…[9 more quoted lines elided]…
> when you allow them to control your language.

I believe you may have lost me a bit here.  If someone identifies 
themselves as a "feminist," there are certain assumptions you can make 
about their beliefs as they relate to gender issues.  "Feminism" or the 
"feminist movement" was the term given to a group of like-minded people 
working together to achieve a goal, the biggest of which was the Equal 
Rights Amendment.  Maybe I should have said "accomplished" instead of 
"done", but the movement of feminists working together accomplished some 
changes in this country - some good, some not so much.

The feminists I have met have been very, very angry people who thought 
very little of themselves.  Their way to compensate for that was to 
blame the "patriarchy," or try to denigrate men as a whole.  The 
feminists I have seen on TV strike me as similar people - thus, there 
seems to be some commonality there.

Some examples of issues I've heard raised from "feminists":
  - Equal pay for equal work?  Works for me - but compare apples to 
apples to ensure you actually are comparing "equal work."
  - Abortion on demand?  Nope.
  - Voting rights?  Sure - no problem.
  - Saying "man" to reference humankind is sexist?  Nope - that's a lack 
of education.
  - Change "semester" to "ovester" because "semester" must come from 
"semen", which is more of the patriarchy putting us down?  Ridiculous - 
are they *trying* to be silly?
  - Change "Valentine's Day" to "V-Day" for "Vagina Day", then get 
really upset when men objectify women.  Do they really think that 
identifying themselves by their reproductive organs *helps* people see 
them as whole persons and not sex objects?

So, like I said - some things have been good, some not.  Does that 
clarify what I meant?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-04T11:53:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1f6rs$li$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com>`

```
In article <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>donald tees wrote:
>> LX-i wrote:
…[17 more quoted lines elided]…
>Rights Amendment.

Mr Summer, I read your posting in its entirety before responding... but I 
have to stop here.

Even the smallest bit of research into the subject might have revealed to 
you that the word 'feminism' can be found in literature of the late 19th 
century; prior to the coining of the term the references were to 
'women's rights'.

(In 1870 Queen Victoria of England wrote to Sir Theodore Martin about 
'this mad, wicked folly of 'Women's Rights' which he described as '... a 
subject which makes the Queen so furious that she cannot contain herself'; 
this was a few months prior to Parliament's passing of the Married Women's 
Property Act which allowed married women to actually *keep* the money they 
have earned on their own rather than have it assumed, by law, as the 
property of their husbands.)

The assertion you make of '"Feminism" or the "feminist movement" was the 
term given to a group of like-minded people working together to achieve a 
goal, the biggest of which was the Equal Rights Amendment' is contradicted 
by evidence such as this, evidence of which you appear to be utterly 
ignorant; it may be hoped that once you are in possession of a set of data 
other than those upon which you presently build your conclusions that your 
conclusions might be other as well.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-04T18:48:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com>`
- **In-Reply-To:** `<f1f6rs$li$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <f1f6rs$li$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> 
> The assertion you make of '"Feminism" or the "feminist movement" was the 
…[3 more quoted lines elided]…
> ignorant;

If it wasn't the term given to them, then it was the term that they 
themselves appropriated for their uses.  Just because a word *used* to 
be used in a particular was doesn't mean it still is.  If someone talks 
about "getting a wheel" today, they're probably talking about rims for 
their car, not spinning the tires when they take off.

http://www.dictionary.com  -> Feminism

1. the doctrine advocating social, political, and all other rights of 
women equal to those of men.
2. (sometimes initial capital letter) an organized movement for the 
attainment of such rights for women.
3. feminine character.

The ERA was the summation of the principles described in #1 above, and 
those who push for it fit right into #2.  Am I missing something?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-05T01:36:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1gn2l$b4q$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <f1f6rs$li$1@reader2.panix.com> <euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com>`

```
In article <euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> 
…[7 more quoted lines elided]…
>themselves appropriated for their uses.

If my Sainted Maternal Grandmother - may she sleep with the angels! - had 
wheels then she would have been a trolley-car, Mr Summers; as noted above 
the evidence contradicts your assertion and of this evidence you appear to 
be utterly ignorant. 

>Just because a word *used* to 
>be used in a particular was doesn't mean it still is.  If someone talks 
…[12 more quoted lines elided]…
>those who push for it fit right into #2.  Am I missing something?

You are missing the facts that you snipped.  Equating a goal regarding a 
single law in a single country is not the same as the definition of a 
group which existed for nearly a century before that law was dreamt of.

Please, Mr Summers... *first* curiousity, *then* research, *then* 
thinking, *then* discussion... and maybe *after* all those, conclusions 
and assertions.  You appear to have had insufficient curiousity 
regarding feminism to do the most basic of research, you appear not to 
have done any research, I barely know what *I* think, let alone anyone 
else... is it any wonder that the assertion you made above is contradicted 
by readily-found data?

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-05T00:09:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VMqdnQGqJe8ygqHbnZ2dnUVZ_rTinZ2d@comcast.com>`
- **In-Reply-To:** `<f1gn2l$b4q$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <f1f6rs$li$1@reader2.panix.com> <euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com> <f1gn2l$b4q$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> Please, Mr Summers... *first* curiousity, *then* research, *then* 
> thinking, *then* discussion... and maybe *after* all those, conclusions 
…[4 more quoted lines elided]…
> by readily-found data?

The facts regarding the history of the term "feminism" do not change the 
facts as I've presented them in this forum.  What it used to be doesn't 
matter nearly as much as what it has become, and what it is today.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-05T12:03:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1hrqj$1h2$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com> <f1gn2l$b4q$1@reader2.panix.com> <VMqdnQGqJe8ygqHbnZ2dnUVZ_rTinZ2d@comcast.com>`

```
In article <VMqdnQGqJe8ygqHbnZ2dnUVZ_rTinZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> Please, Mr Summers... *first* curiousity, *then* research, *then* 
…[9 more quoted lines elided]…
>matter nearly as much as what it has become, and what it is today.

The fact that one sees a square when one looks at the face of a cube, Mr 
Summers, does not change the fact that one is dealing with a cube.  You 
have taught your children that a lie is a lie, whether by commission or by 
ommission; now that you know feminism has a history much longer than you 
asserted in your posting you may need to reconsider what you consider 
truthful action.

(as for 'what it ised to be doesn't matter nearly as much as wht it has 
become'... remember that the next time you assert something based on 
Constitutional authority, so many people say it has changed)

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-07T08:53:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hveu33p7idm3on191lm7ifi20jaem3hhu2@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <f1f6rs$li$1@reader2.panix.com> <euydnUj_V9zrSabbnZ2dnUVZ_rmdnZ2d@comcast.com> <f1gn2l$b4q$1@reader2.panix.com> <VMqdnQGqJe8ygqHbnZ2dnUVZ_rTinZ2d@comcast.com>`

```
On Sat, 05 May 2007 00:09:01 -0600, LX-i <lxi0007@netscape.net> wrote:

>The facts regarding the history of the term "feminism" do not change the 
>facts as I've presented them in this forum.  What it used to be doesn't 
>matter nearly as much as what it has become, and what it is today.

How did you determine what the term means today - and why do we have a
different understanding of the term than you do?

My wife "knows" a lot of things that I don't about this country, but
she listens to hate radio a lot, and believes that some of it has to
be true.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-04T08:06:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o4fm33140hbqqedecqck19qovann2a85ij@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com>`

```
On Thu, 03 May 2007 20:18:08 -0600, LX-i <lxi0007@netscape.net> wrote:

>I believe you may have lost me a bit here.  If someone identifies 
>themselves as a "feminist," there are certain assumptions you can make 
>about their beliefs as they relate to gender issues.  

OK, I will identify myself as a feminist.   Assume away.

>"Feminism" or the 
>"feminist movement" was the term given to a group of like-minded people 
>working together to achieve a goal, the biggest of which was the Equal 
>Rights Amendment.  

That it one of the meanings of the term.

>Maybe I should have said "accomplished" instead of 
>"done", but the movement of feminists working together accomplished some 
>changes in this country - some good, some not so much.

As is the case with anything.

>The feminists I have met have been very, very angry people who thought 
>very little of themselves.  Their way to compensate for that was to 
>blame the "patriarchy," or try to denigrate men as a whole.  The 
>feminists I have seen on TV strike me as similar people - thus, there 
>seems to be some commonality there.

They are the people that get the media attention.    Manipulating the
media is not feminism.    But burning bras certainly will get someone
15 minutes of fame.

>Some examples of issues I've heard raised from "feminists":
>  - Equal pay for equal work?  Works for me - but compare apples to 
>apples to ensure you actually are comparing "equal work."

Also, equal careers, and equal supply and demand.    Taking time off
to raise children makes a difference.   Choosing to be in the child
care business makes a difference.

>  - Abortion on demand?  Nope.
>  - Voting rights?  Sure - no problem.
…[11 more quoted lines elided]…
>clarify what I meant?

Skipping the abortion question because the issues tend to be a
religious issue, the things that you disagree with are about media
manipulation of a few, not the issues of feminism.

Don't confuse the spokesman with the issues.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-04T19:27:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wpednY19n4g4QKbbnZ2dnUVZ_rmdnZ2d@comcast.com>`
- **In-Reply-To:** `<o4fm33140hbqqedecqck19qovann2a85ij@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <MpOdnTIM-vTL3qTbnZ2dneKdnZydnZ2d@golden.net> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <o4fm33140hbqqedecqck19qovann2a85ij@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 03 May 2007 20:18:08 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[8 more quoted lines elided]…
> 15 minutes of fame.

But the people I knew weren't getting media attention.  True, some 
people will do things just for attention, but when they continue doing 
it when they don't, one may begin to believe that they actually believe 
the hate they're spewing.

>> Some examples of issues I've heard raised from "feminists":
>>  - Equal pay for equal work?  Works for me - but compare apples to 
…[4 more quoted lines elided]…
> care business makes a difference.

Bingo - that's what I meant by apples to apples.  :)

>>  - Abortion on demand?  Nope.
>>  - Voting rights?  Sure - no problem.
…[15 more quoted lines elided]…
> manipulation of a few, not the issues of feminism.

Then what are the issues?  I don't mean this to sound adversarial - but 
several people on this thread have said what it isn't, but no one gives 
some good examples on what it is.

My opinion - the feminist movement and the civil rights movement both 
have the same problem.  Both accomplished pretty much all they 
originally set out to - but oppression has become big business.  Rather 
than settle for an even playing field, their goals changed.  Now, 
modern-day feminism holds that women are *superior* to men, not equal; 
and the modern-day civil rights movement would end tomorrow if white 
people would shed the guilt over what their ancestors did, and blacks 
would thicken their skin about 1/64 of an inch.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-05T01:39:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1gn8f$q2s$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <k7qdnbbfn7poCqfbnZ2dnUVZ_rylnZ2d@comcast.com> <o4fm33140hbqqedecqck19qovann2a85ij@4ax.com> <wpednY19n4g4QKbbnZ2dnUVZ_rmdnZ2d@comcast.com>`

```
In article <wpednY19n4g4QKbbnZ2dnUVZ_rmdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>My opinion - the feminist movement and the civil rights movement both 
>have the same problem.  Both accomplished pretty much all they 
>originally set out to - but oppression has become big business.

'Everything that can be invented has already been invented... so let's 
close the Patent Office'.

'The books in that library can do only two things.  They can repeat (holy 
text), which makes them superfluous or they can contradict (holy text), 
which makes them heresy.  Burn them all.'

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-03T09:12:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1c91t$43i$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`

```
In article <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com>,
…[26 more quoted lines elided]…
>movement has done.  :)  You know it's not that cut-and-dried.

There's a bit of difference between cut-and-dried, Mr Summers, and 'let's 
go back n years and keep this... and leave out that... and take one from 
Column A and two from Column B'; like them or not every era has what are 
seen as benefits and detriments.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-03T20:26:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SsydnYeEWMVwBKfbnZ2dnUVZ_rfinZ2d@comcast.com>`
- **In-Reply-To:** `<f1c91t$43i$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <f1c91t$43i$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[31 more quoted lines elided]…
> seen as benefits and detriments.

Right - but you're saying that by saying what I said above, I favored a 
return to fifty years ago.  I don't.  (Especially given my line of work 
- COBOL hadn't even been invented yet, much less Java / Apache / Struts!)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-04T09:25:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1eu6d$nui$1@reader2.panix.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <f1c91t$43i$1@reader2.panix.com> <SsydnYeEWMVwBKfbnZ2dnUVZ_rfinZ2d@comcast.com>`

```
In article <SsydnYeEWMVwBKfbnZ2dnUVZ_rfinZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>,
…[35 more quoted lines elided]…
>return to fifty years ago.

*No*, Mr Summers, I said, earlier, that I recalled your having said 
something about how relations between men and women should be 'unwound' to 
the way there were a half-century back... my memory may be, I admit, 
porous and you've cleared that up.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-03T08:56:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgtj3395qvjjdtphe7p855eo50k4ir6s3c@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`

```
On Wed, 02 May 2007 19:07:02 -0600, LX-i <lxi0007@netscape.net> wrote:

>Heh - and there's the spin.  Just because I didn't say we needed to go 
>back 50 years doesn't mean that I agree with everything the feminist 
>movement has done.  :)  You know it's not that cut-and-dried.

Anybody who believes in everything that any "movement" or "political
party" or "church" or any other group or person is not thinking for
himself.

Heck at least the groups, and probably the individuals have
contradictory beliefs.

And we can see how political party platforms are created - with much
compromising and disagreement.   Anybody who agrees with the party
platform doesn't agree with any one politician who helped produce that
party platform.

It's easy to point to self-appointed leaders of various groups and
agree with him that what he says defines the movement - but this is
the lazy way of doing things.    Ask an average Arapaho if  Russell
Means is speaking for him.

What is irritating is when someone speaks for a cause that is
important to me - but in such a way as to produce enemies for my
cause.    It doesn't make my cause less valid because some
self-serving fool agrees with it.   It just provides a target for
those who oppose my cause.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-03T20:28:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SsydnYaEWMXaB6fbnZ2dnUVZ_rfinZ2d@comcast.com>`
- **In-Reply-To:** `<bgtj3395qvjjdtphe7p855eo50k4ir6s3c@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <bgtj3395qvjjdtphe7p855eo50k4ir6s3c@4ax.com>`

```
Howard Brazee wrote:
> What is irritating is when someone speaks for a cause that is
> important to me - but in such a way as to produce enemies for my
> cause.    It doesn't make my cause less valid because some
> self-serving fool agrees with it.   It just provides a target for
> those who oppose my cause.  

Excellent words, Howard.  I feel the same way.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-03T23:52:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Bu_h.6688$Ut6.6226@newsread1.news.pas.earthlink.net>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com...


So how do you feel about Condi meeting with the Syrians? Should she be tried 
for treason along with Pelosi?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-03T20:39:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Op-dnWM85rCUAKfbnZ2dnUVZ_q2pnZ2d@comcast.com>`
- **In-Reply-To:** `<4Bu_h.6688$Ut6.6226@newsread1.news.pas.earthlink.net>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <eYidnaCSG4-wjqXbnZ2dnUVZ_sWdnZ2d@comcast.com> <f19l8u$ibt$1@reader2.panix.com> <7aqdndecBf3ziKTbnZ2dnUVZ_tHinZ2d@comcast.com> <f1b9n5$jru$1@reader2.panix.com> <tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com> <4Bu_h.6688$Ut6.6226@newsread1.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:tIKdnYcyEIJeqKTbnZ2dnUVZ_t3inZ2d@comcast.com...
…[3 more quoted lines elided]…
> for treason along with Pelosi? 

As the Secretary of State (part of the *executive* branch), she *is* the 
one who should be meeting with foreign nations.  And there are several 
qualities that make her new mission different that what Pelosi did.

First of all, this new initiative has been initiated by the Iraqi 
government - they want to establish diplomatic ties with their 
neighbors.  The Iraqi government has asked for our assistance, and as 
the one responsible for those sorts of things, she's working with them.

http://www.msnbc.msn.com/id/17364686/

The third paragraph under "Iran faces growing pressure" illustrates that 
last point.  Also, under the heading "Waiting for RSVPs", it's not just 
Iran and Syria - the Arab League nations and the 5 permanent UN security 
council nations are also invited.  The first council meeting is at the 
sub-ministerial level, and future ones at the ministerial level.

That's a *big* difference from a member of the opposition political 
party meeting the president of a state sponsor of terrorism while troops 
are on the ground.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-02T13:10:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178136627.157207.43520@c35g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`
- **References:** `<1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`

```

LX-i wrote:

> Pete Dashwood wrote:

Nice piece Pete.

> > What with all that, and the Four Horsemen not really trying... (a few penny
> > ante skirmishes; no decent Global conflict for over half a century now),
> > some minor famines and pestilences. The Death stats are pretty steady but
> > that's only because of the increasing birth rate globally. The Pale Horse is
> > about ready for the knacker's yard

Binky (Death's horse) can't be fit for the knacker's yard. I suspect
it is that damned pub that the four horsemen keep stopping off at that
is the problem (see the discworld series of books).

and there is a real risk He could be
> > stripped of His title of Lord of the Flies... (Evil doesn't have the appeal
> > it once had in a repressed population; kids now can go to a concert and get
> > it all out of their systems...). You should have heard Him moaning about how
> > hard it is to get good help, and what a miserable job it is to be a
> > Manager...

Yeah, everyone has an opinion about their management. Try doing the
job yourself and it ain't so easy....

> Then there are the Powers-that-Be to whom He must answer...

That must be The Auditors then (more discworld stuff).

> (hints
> > have been dropped that if the World doesn't get worse, they may be looking
…[15 more quoted lines elided]…
> am now.

I got that way about the British government talking to the IRA but it
has resulted in a much reduced level of hostilities. Sooner or later,
we will have to talk to the Syrians and the Iranians and (this makes
me seethe) the Taliban.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-03T12:12:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59snn9F2mag88U1@mid.individual.net>`
- **References:** `<1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1178136627.157207.43520@c35g2000hsg.googlegroups.com...
>
> LX-i wrote:
…[3 more quoted lines elided]…
> Nice piece Pete.

Thanks, glad you enjoyed :-)

>
>> > What with all that, and the Four Horsemen not really trying... (a few 
…[11 more quoted lines elided]…
> is the problem (see the discworld series of books).

Binky??!!  That's brilliant... I can see I'll have to add Discworld to my 
reading list...:-)
>
> and there is a real risk He could be
…[14 more quoted lines elided]…
> That must be The Auditors then (more discworld stuff).

I kind of saw it as a committee, with God as the Chairman of the Board. 
Ultimately, Creation is God's responsibility and He knows that Satan is 
necessary to maintain balance, even though He doesn't approve of this 
necessity. (There are obviously some things that even God has no power over, 
once they are set in motion.) It's like the old question: Can God make a 
stone so huge that even HE cannot move it?

Simple peasant folk have been spun on this one for hours... The Communists 
used it in the early 20th century to sow doubt among the faithful...

(I never understood why Marx, understanding that Religion is the opium of 
the masses, would want to take away that opium...seems to me he was looking 
for trouble. He certainly found it.)



>
>> (hints
…[24 more quoted lines elided]…
>
Maybe not. If people can change their minds, the Taliban will cease to 
exist. It is possible to be Muslim without being fanatical or militant. Many 
people had little choice OTHER than to follow the Taliban. Now they do. 
Unfortunately, it is very easy for the Taliban to make the argument: "Well, 
you might not have liked us, but at least we were Afghan. Now you hand the 
country over to foreigners and consider that is better?"

Hopefully, as people realise it is safe to have alternative opinions, and 
with support and help from the world community, we can expect to see the 
Afghanis taking responsibility for themselves. It will be a long slow 
process but it can be done.

I don't see negotiating with the Taliban as an option. Who could believe 
anything they promised, anyway?

My hope is in the women... once they get to shop I think they can influence 
the men :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-03T09:00:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o2uj33l7e6c9j985q8envla3fsr0b04o1b@4ax.com>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com> <59snn9F2mag88U1@mid.individual.net>`

```
On Thu, 3 May 2007 12:12:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I kind of saw it as a committee, with God as the Chairman of the Board. 
>Ultimately, Creation is God's responsibility and He knows that Satan is 
…[3 more quoted lines elided]…
>stone so huge that even HE cannot move it?

That is a problem with the deity inflation that Churches have had. To
increase their power and authority, they kept increasing their deity's
power and authority beyond what was described in their Holy books.
Eventually, it no longer makes sense, in the same way that it doesn't
make sense that Superman didn't do anything significant to win WWII.

>Simple peasant folk have been spun on this one for hours... The Communists 
>used it in the early 20th century to sow doubt among the faithful...
…[3 more quoted lines elided]…
>for trouble. He certainly found it.)

Marx was an intellectual above all else, not a politician.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-04T13:52:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59vhv2F2mmcuuU1@mid.individual.net>`
- **References:** `<CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com> <59snn9F2mag88U1@mid.individual.net> <o2uj33l7e6c9j985q8envla3fsr0b04o1b@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:o2uj33l7e6c9j985q8envla3fsr0b04o1b@4ax.com...
> On Thu, 3 May 2007 12:12:24 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> make sense that Superman didn't do anything significant to win WWII.

Excellent Howard! I really liked this paragraph, and the last sentence is 
just...perfect. :-)

>
>>Simple peasant folk have been spun on this one for hours... The Communists
…[7 more quoted lines elided]…
> Marx was an intellectual above all else, not a politician.

Maybe politics is not for the intelligent.... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 23)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-03T10:54:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178214899.781963.175340@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<59snn9F2mag88U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com> <59snn9F2mag88U1@mid.individual.net>`

```

Pete Dashwood wrote:

> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1178136627.157207.43520@c35g2000hsg.googlegroups.com...
> >

> > Binky (Death's horse) can't be fit for the knacker's yard. I suspect
> > it is that damned pub that the four horsemen keep stopping off at that
…[3 more quoted lines elided]…
> reading list...:-)

Start with "The Light Fantastic" and "The Colour of Magic". They are
the best novels. I can not remember which novel Death and the other
horsemen ride out on the Apocalypse and stop off at a Real Ale pub and
get bladdered.


> >
> (I never understood why Marx, understanding that Religion is the opium of
> the masses, would want to take away that opium...seems to me he was looking
> for trouble. He certainly found it.)

I think that he expected his opiate (politics) to replace the standard
opiate (religion); after all, politics is really only an extension of
religion.

> >
> > I got that way about the British government talking to the IRA but it
…[20 more quoted lines elided]…
> the men :-)

It is not working in Iran so why should it work next door in
Afghanistan?

If the West had been more supportive of the Mujahideen then, possibly,
the problem of the Taliban would never have come into being?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-03T14:30:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SMmdnZTfZvPGt6fbnZ2dnUVZ_riknZ2d@golden.net>`
- **In-Reply-To:** `<1178214899.781963.175340@q75g2000hsh.googlegroups.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com>`

```
Alistair wrote:
> Pete Dashwood wrote:
> 
…[51 more quoted lines elided]…
> 

Funny how the US created the Taliban to fight the Russians, then got all 
moral about it when the Taliban decided they did not like the US either. 
   Maybe that had to do with getting stabbed in the back when it became 
politically expedient to do so.

Seems that everyone shooting back is somebody they set up with guns in 
the first place.  You would think they'd learn, but apparently not. Not 
that our cluster-fuck of a prime minister is any better.

Donald
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 24)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-04T14:40:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59vkpgF2mphveU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com> <1178136627.157207.43520@c35g2000hsg.googlegroups.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1178214899.781963.175340@q75g2000hsh.googlegroups.com...
>
> Pete Dashwood wrote:
…[27 more quoted lines elided]…
>

Sadly, you're probably right.

>> >
>> > I got that way about the British government talking to the IRA but it
…[27 more quoted lines elided]…
> Afghanistan?

It hasn't had time to work in Iran...most of the bright Iranis are living in 
exile. I said it will be a long, slow process. Iran has a more enlightened 
Islamic state than that which was enforced on Afghanistan by the Taliban, 
but it is still a repressive system. Even though we may not like what's 
happening in Iran, they are showing signs of growth. The nuclear issue is 
problematic for everyone, but negotiation continues...

Remember, the Peacock throne and the tyranny of the Shah is still within 
living memory for most Iranians. They preferred the tyranny of the Ayatollah 
Khomeini because at least he was representative of a simple dogmatic 
philosophy that was not Western and UnGodly.

It's no wonder they are confused about how to govern; they have seen the 
worst of the separate systems they have endured.

They want a place in the World but they are afraid of  their neighbours and 
the West. It's a bit like teenage angst. Unfortunately, it will take some 
decades to grow out of it.

Despite all the unrest and trouble, if you look at the Middle East over the 
last 50 years it is possible to see some growth and progress. Eventually, 
they will learn to get along, but, as I said elsewhere, it will require the 
changing of minds. I believe that process is under way but it will be long 
and slow.

I have travelled a bit. I've met and spoken with people who are Jewish, 
Palestinian, Iranian, Kuwaiti, Saudi, and Egyptian. They all want 
fundamentally the same things, and it isn't for their children to live in 
fear.

The ideals enshrined in the American Constitution, The United Nations 
Charter, and just plain common sense tell us that all men should have 
justice and freedom. How can these ideas be resisted? They can't... and even 
the great religions of the world teach this. The resistance to them in the 
Middle East is because they are perceived as Western and Foreign and 
anti-Islamic. You would have a pretty hard job selling the US Constitution 
to the ruling assembly in Iran or Iraq or the Gaza. Not because it isn't 
sensible, just because it has the red, white, and blue on it.

The tragedy here is that the USA, with the best of intentions, has inflamed 
the situation. Now it needs to settle. I know there are people in the US 
administration who cynically serve what they perceive to be their country's 
interest above all else, but there are others with a broader view also, and 
my experience has been that the average American wants to see people treated 
fairly and decently.

Every day, in small ways in the theatres of action, western troops (mostly 
American, though I don't want to dismiss the contribution of others also) 
are showing in mundane daily living that life can be better.  Protection 
from looters and thugs, assistance with schools, medical treatment, 
rebuilding, living the way of life we take for granted. As many tiny drops 
eventually become a river, we will see change in the attitudes of these 
areas. History has shown that power and repression are no match long term 
for a "better idea". Democracy is a better idea, even if it isn't perfect.

What saddens me is the human cost and the time it takes.

>
> If the West had been more supportive of the Mujahideen then, possibly,
> the problem of the Taliban would never have come into being?
>
Unlikely. The Mujahideen would have been every bit as bad as the Taliban. It 
is all based on the politics of power, as represented by weapons. Until they 
learn that enforcing the will of the leader on the population at gunpoint is 
not a solution, it really doesn't matter who is in power. It is a Mediaeval 
mindset with 21st century weaponry. Hardly surprising the results are pretty 
shocking.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 25)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-04T09:47:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1evf0$g1t$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net>`

```
In article <59vkpgF2mphveU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>You would have a pretty hard job selling the US Constitution 
>to the ruling assembly in Iran or Iraq or the Gaza. Not because it isn't 
>sensible, just because it has the red, white, and blue on it.

Mr Dashwood, there's already a pretty hard job selling the US Constitution 
to the US Government; were that not the case there would not be a constant 
series of attempts by various members and brances of said Government to 
ignore what it states, what its framers intended or how it has been 
interpreted by those who came after.

Consider, say, the treatment of the Church of Jesus Christ of Latter-Day 
Saints insofar as polygamy is concerned, or the treatment of certain 
Native American/Indian/Red Indian/Guys Who Fought The Cowboys - I am not 
sure which is the correct term nowadays - who used hallucinogenic plants 
as sacraments of worship... in light of the first clause of the First 
Amendment.

Consider, say, the regulations against the interstate transportation of 
firearms or restrictions placed on the purchase of such... in light of the 
entirety of the Second Amendment.

Consider, say, the acceptability of evidence now given to materials seized 
in searches which have been approved by officials with no public 
accountability who have made the making-known of warrants a crime... in 
the light of the entirety of the Fourth Amendment.

Consider many things when reading the Fifth Amendment and the Sixth 
Amendment... in light of recent developments.

When I was a lad it was 'Common Knowledge' that 'someone' had changed the 
language of the Bill of Rights and circulated among the less-educated 
Americans who lived in (area in which the teller of the anecdote wished to 
denigrate) under the rubric that it was 'a new bill Congress was 
considering passing'... and that people universally said it was a bad 
thing, too 'liberal' and not good for Decent Americans.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 26)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-05T02:34:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a0uirF2muhfjU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1evf0$g1t$1@reader2.panix.com...
> In article <59vkpgF2mphveU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[40 more quoted lines elided]…
>

As someone who doesn't live there, I find that very disturbing. If I 
actually lived there, I'd very likely be doing something about it.

I know things have changed since 911 and many infringements of liberty and 
rights are occurring under the blanket of "Homeland Security" but no-one 
should be letting Civil Servants be unaccountable... That way lies 
madness... It is only the threat of losing their pension that ever stirs 
them into any kind of action; take that away and you are indeed doomed.

(There was a recent episode of "Boston Legal" aired here where Denny wasn't 
able to fly because the name "Denny Crane" was on a "list" and he was 
considered a Terrorist. At first, I thought that some of the stuff that came 
out had been made up for the show, (like, no possible recourse to establish 
your identity and get removed from the list; the reason given was that if 
that name was removed, all Denny Cranes would be able to fly, including the 
one who actually was a suspected terrorist. The DHS did not have computer 
systems capable of identifying individuals, or if they did, no-one had 
worked out how to get names removed off the list....) but I was assured by 
an American friend when discussing the show a few days later, that it is 
accurate.)

I was fingerprinted on entry to the USA a few months ago. First time in my 
life. (I don't remember them doing it when I did military service, but they 
may have, so perhaps it was the second time in my life...). I had mixed 
feelings about it. As a visitor, I'm prepared to abide by the Host's rules 
and it was done very efficiently and without fuss. But now there is a part 
of me that knows I'm on file somewhere in the USA... it's a bit like they 
own part of me... :-)  See, my OWN Government (the one I get to vote for) 
doesn't have that, but I s'pose it'll come. If it helps in any way to 
prevent a terrorist attack, and given I have nothing to hide, I guess it is 
a minor inconvenience. But if they denied me access to aircraft because my 
name was on a "list",  I'd be making as much noise as possible about it :-)

I'm not sure of the gist of your post, Doc. If the foundations of American 
democracy are indeed being undermined, then I would expect SOMEONE to be 
making a noise about it...

If Civil Servants start believing they are above the Law, then that has to 
be stopped. Shine a light on it. If Branches of Government believe the Law 
does not apply to them, then it's time for a change of Government...(Or at 
least a change of Department Head)

Raise it. Write to the Head of Department  and if you get no satisfaction 
escalate it. Talk to your Congressman.Talk to your colleagues and 
associates; raise awareness.

It isn't OK to sit back and watch this.

Democracy has to work, because all the alternatives are not even options, 
for free people.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-04T15:00:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1fhr5$4n4$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net>`

```
In article <5a0uirF2muhfjU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f1evf0$g1t$1@reader2.panix.com...

[snip]

>> Consider, say, the acceptability of evidence now given to materials seized
>> in searches which have been approved by officials with no public
…[4 more quoted lines elided]…
>> Amendment... in light of recent developments.

[snip]

>I'm not sure of the gist of your post, Doc. If the foundations of American 
>democracy are indeed being undermined, then I would expect SOMEONE to be 
>making a noise about it...

There are those who do, Mr Dashwood... and there are others who sneer 
'Don'cha know there's a *war* on?  You're trying to give aid and comfort 
to Our Enemies!'

>
>If Civil Servants start believing they are above the Law, then that has to 
>be stopped. Shine a light on it. If Branches of Government believe the Law 
>does not apply to them, then it's time for a change of Government...(Or at 
>least a change of Department Head)

Mr Dashwood, I'm not sure you understand the logic that is applied in such 
cases... I'm not sure that *I* do, for that matter.

Recently (sometime a couple of years back) it was revealed that 
thirty-three years prior FBI official W Mark Felt was revealed to be the 
'Deep Throat' whose exposures of White House doings eventually lead to 
then-President Nixon's resignation.

The amount of vituperation released against Mr Felt in some circles 
astounced me... I recall hearing one interview with a fellow - I'll call 
him Mr Blank - who asserted that Mr Felt 'broke the code of the FBI' by 
his revelations and that Mr Felt should have 'gone up the ladder' and 
stayed within the boundaries of protocol and chain-of-command.

When it was pointed out that the President was corrupt, that the FBI was 
headed by Nixon's own man and that the Attorney General was busily carting 
off White House files and destroying them Mr Blank paused for a moment... 
and then re-asserted that Mr Felt should have gone up the ladder and by 
not doing so had 'broken the FBI code'.

Dealing with this kind of 'logic' is not the easiest... and it appears to 
me that the current climate is shaped less by an attitude of 'come, let us 
reason together' and more by one of 'either you're with us or against us'; 
the best thing seems to be to vote with my votes.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-05T11:18:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a1t9hF2nfubfU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1fhr5$4n4$1@reader2.panix.com...
> In article <5a0uirF2muhfjU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[24 more quoted lines elided]…
>

It is always difficult when the country is at war. The same thing happened 
in England during the War, although at least that was an open war and 
everyone understood that their survival was at stake. Some of the measures 
passed in the early 1940s, under the state of emergency, were not repealed 
until the late 60s and then only because enough people made a fuss about 
them.

(I heard about this from people who lived through it; it is hearsay, but I 
have no reason to doubt it.)

There are always some people who just want some kind of power. Many of them 
fail the police (or don't like the risks attached) so they end up at City 
Hall. These are the ones I think you were describing, the ones who see a 
chance to expand their little Empires, and grasp it. They are the ones who 
have to be watched and whistles need to be blown loud and clear.

>>
>>If Civil Servants start believing they are above the Law, then that has to
…[10 more quoted lines elided]…
> then-President Nixon's resignation.

I remember it well. Who could forget Nixon's resignation speech with his 
long-suffering "You won't have Richard Nixon to kick around any 
more..."attitude, like he was the victim, when the real victim was the 
Democratic process.

I remember the references to "Deep Throat", taken from the porn film of the 
same name which came out about that time, and made Linda Lovelace famous.

>
> The amount of vituperation released against Mr Felt in some circles
…[3 more quoted lines elided]…
> stayed within the boundaries of protocol and chain-of-command.

Not sure what 'astounced' means... perhaps a Carrollian 'portmanteau word' 
from 'astounded' and 'astonished'... anyway, I get the picture :-)

Codes of Conduct are important, but they shouldn't be secret codes. Maybe 
Felt should have 'gone up the ladder' even knowing it would be futile, and 
then blown the whistle after that failed. It's easy to sit back in an 
armchair with hindsight and suggest what people should have done; the man 
was probably in fear of his life and did what he could as he saw it at the 
time. At least SOMEONE saw it had to stop. He deserves credit. I think your 
point is that instead, he just got venomous attack.
>
> When it was pointed out that the President was corrupt, that the FBI was
…[3 more quoted lines elided]…
> not doing so had 'broken the FBI code'.

It is certainly not logical or reasonable. It is the Mr. Blanks of this 
world who pose the greatest danger, in my opinion. Bin Laden is open about 
his goals and we know what to expect and can take counter measures; the Mr. 
Blanks are covert, subservient, unthinking, and have no idea of the big 
picture and what is important, or what democracy really stands for.  It is 
all about "following orders" and advancing up the ladder towards the pension 
at the end. I see them like the knights who murdered Thomas A'Beckett in the 
hope of currying favour with the King.
>
> Dealing with this kind of 'logic' is not the easiest... and it appears to
> me that the current climate is shaped less by an attitude of 'come, let us
> reason together' and more by one of 'either you're with us or against us';
> the best thing seems to be to vote with my votes.

Yes, voting against it certainly helps. If you can encourage others to vote 
against it that's even better.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-05T13:38:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1i1cg$jsm$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net>`

```
In article <5a1t9hF2nfubfU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f1fhr5$4n4$1@reader2.panix.com...
>> In article <5a0uirF2muhfjU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>>I'm not sure of the gist of your post, Doc. If the foundations of American
>>>democracy are indeed being undermined, then I would expect SOMEONE to be
…[7 more quoted lines elided]…
>It is always difficult when the country is at war.

If someone can benefit from things being More Difficult rather than things 
being Easy then it might explain why, over the past few decades, Americans 
have had so many Wars... the War on Poverty, the War on Illiteracy, the 
War on Drugs and the War on Terror, to name a few.

I don't recall too many decisive victories being claimed in any of them.

[snip]

>There are always some people who just want some kind of power.

In the United States of America there are two primary political parties, 
the Democrats and the Republicans... never mind the fact that, at times, 
they shift positions on things with astonishing ease... but as my 
fifth-grade schoolteacher told us, lo, those many decades ago, 'The 
difference between Democrats and Republicans is that Democrats want 
government out of your bedroom and into your wallet while Republicans want 
government out of your wallet and into your bedroom.'

[snip]

>> Mr Dashwood, I'm not sure you understand the logic that is applied in such
>> cases... I'm not sure that *I* do, for that matter.
…[9 more quoted lines elided]…
>Democratic process.

I remember watching Mr Nixon's being interviewed by David Frost and 
responding (with what appeared to be complete sincerity) 'Well, when the 
President does it that means it is not illegal'... and thinking 'So no man 
is above the Law but some are more equal than others'.

[snip]

>> The amount of vituperation released against Mr Felt in some circles
>> astounced me... I recall hearing one interview with a fellow - I'll call
…[5 more quoted lines elided]…
>from 'astounded' and 'astonished'... anyway, I get the picture :-)

Meaning is the result of interpretation, Mr Dashwood; 'astounced' is the 
result of striking a key adjacent to the one intended (on my QWERTY 
keyboard the 'c' is below and slightly to the right of the 'd') and may be 
considered a typographical error.

[snip]

>> When it was pointed out that the President was corrupt, that the FBI was
>> headed by Nixon's own man and that the Attorney General was busily carting
…[4 more quoted lines elided]…
>It is certainly not logical or reasonable.

Logic is a game played by a particular set of rules, Mr Dashwood... 
although I am not A Professional in such matters I have heard the 'rules' 
evidenced above as being, at times, symptomatic of the logical system 
employed by delusional paranoids in which the questioning of suppositions 
is dangerous.  Consider:

A: 'There is a large group of enemies out there whose goal it is to paint 
my ears, and the ears of anyone who thinks like me, a bright green using a 
paint that only I can see.'

B: 'Maybe that deserves a bit of looking-at; a different conclusion might 
be come to.'

A: 'But... if I come to a different conclusion then I won't be able to see 
whose ears have been painted green... so it'c clear that you are in league 
with them and (I cannot speak with you any more)/(consider you to be an 
enemy, too).'

>It is the Mr. Blanks of this 
>world who pose the greatest danger, in my opinion.

It is symbiotic, Mr Dashwood.  The Blanks are nothing without a guiding 
force and a guiding force is nothing without Blanks to support it.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-06T08:47:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a48rbF2ndf80U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <f1i1cg$jsm$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1i1cg$jsm$1@reader2.panix.com...
> In article <5a1t9hF2nfubfU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>
<snip>

>It is certainly not logical or reasonable.
>
…[17 more quoted lines elided]…
>

Lol! Excellent! I really enjoyed that... :-)

>>It is the Mr. Blanks of this
>>world who pose the greatest danger, in my opinion.
…[3 more quoted lines elided]…
>

Not sure I agree, but I understand what you are saying.

I believe that even without a 'host' the Blanks of this world would still be 
with us. You could have a decent government or administration service and 
there would still be Blanks embedded in it. If the leadership is good, and 
the principles and goals are clear, there are likely to be fewer of them, 
but I odn't believe we can ever eradicate them completely. Still, it isn't 
really worth arguing. Our best defence is vigilance and non-tolerance of 
Blank behaviour.

Pete.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-07T09:05:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csfu33dk1i6ntj2d12r1ks33mcuk4plcmb@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <f1i1cg$jsm$1@reader2.panix.com>`

```
On Sat, 5 May 2007 13:38:24 +0000 (UTC), docdwarf@panix.com () wrote:

>In the United States of America there are two primary political parties, 
>the Democrats and the Republicans... never mind the fact that, at times, 
…[4 more quoted lines elided]…
>government out of your wallet and into your bedroom.'

Except that when the Republicans controlled both houses and the white
house, Big Government got bigger anyway.    Power corrupts.   The
Deficit budget is a deferred tax.   The Republicans are in my wallet
big time.    Goldwater Republicanism is dead.

And if the Libertarians ever got power, they would be corrupted as
well.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-07T18:32:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1nrcn$lnj$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a1t9hF2nfubfU1@mid.individual.net> <f1i1cg$jsm$1@reader2.panix.com> <csfu33dk1i6ntj2d12r1ks33mcuk4plcmb@4ax.com>`

```
In article <csfu33dk1i6ntj2d12r1ks33mcuk4plcmb@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Sat, 5 May 2007 13:38:24 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[9 more quoted lines elided]…
>house, Big Government got bigger anyway.

Now, now, Mr Brazee... just because a politician wants something doesn't 
mean that anyone gets it, eh?

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-07T09:01:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net>`

```
On Sat, 5 May 2007 11:18:09 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I remember it well. Who could forget Nixon's resignation speech with his 
>long-suffering "You won't have Richard Nixon to kick around any 
>more..."attitude, like he was the victim, when the real victim was the 
>Democratic process.

How was the Democratic process a victim when he made this speech in
1962?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-07T11:40:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1shu33h9b6r0jp647ee97qu7u2vc84juuv@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com>`

```
On Mon, 07 May 2007 09:01:38 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Sat, 5 May 2007 11:18:09 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>1962?

That's a real good question.  The constitution defines all the checks
and balances in the 3 branches of the government.  Nixon, facing an
impeachment, was an unwilling participant in the Democratic process
that is supposed to protect the government and its citizens from
abuses of power in the Executive Branch.  Score 1 for the
constitution.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I'd give my right arm to be ambidextrous!"
-- Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-07T09:52:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iniu3399jmp4dc88pt4ugr7q00d6g5cvcr@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <1shu33h9b6r0jp647ee97qu7u2vc84juuv@4ax.com>`

```
On Mon, 07 May 2007 11:40:19 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>>>I remember it well. Who could forget Nixon's resignation speech with his 
>>>long-suffering "You won't have Richard Nixon to kick around any 
…[11 more quoted lines elided]…
>constitution.

Although that wasn't when he made that famous quote.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-08T11:10:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a9pv1F2n9fknU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com...
> On Sat, 5 May 2007 11:18:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> 1962?

He had behaved in a perfectly despicable, indeed, criminal, manner, then, on 
being caught, instead of 'fessing up and taking responsibility for his 
actions, he tried to make it look like he was the victim.

The Democratic process suffered because he established a precedent that if 
the President did something it was OK and he was above the Law. He further 
reinforced this impression by his farewell speech, where he showed no 
remorse and instead tried to make it look like his enemies had been out to 
get him, and he was 'framed'. To this day there are probably people in the 
USA who believe the President is the Boss and can do anything.

I don't think that's good for Democracy.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-08T08:10:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l11143pre3jdpred1fevengcrj62t3agd5@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net>`

```
On Tue, 8 May 2007 11:10:25 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>>>I remember it well. Who could forget Nixon's resignation speech with his
>>>long-suffering "You won't have Richard Nixon to kick around any
…[8 more quoted lines elided]…
>actions, he tried to make it look like he was the victim.

When he made that speech, he hadn't yet been elected president.

>The Democratic process suffered because he established a precedent that if 
>the President did something it was OK and he was above the Law. He further 
…[3 more quoted lines elided]…
>USA who believe the President is the Boss and can do anything.

There have always been people who have believed that.   And way too
often there were presidents who believed that.

>I don't think that's good for Democracy.

But Democracy had one of its few victories over RMN.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-09T11:23:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5acf41F2nmvc1U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <l11143pre3jdpred1fevengcrj62t3agd5@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:l11143pre3jdpred1fevengcrj62t3agd5@4ax.com...
> On Tue, 8 May 2007 11:10:25 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> When he made that speech, he hadn't yet been elected president.

I'm talking about his resignation speech, after impeachment. I watched it on 
television in Auckland, New Zealand. (In fact, I was supposed to be at work, 
but went to a shop in Karangahape Road, near where I was working, so I could 
see the speech. He had certainly been elected President. Don't know what 
your referring to.)

I remember thinking at the time how pathetic it was.

>
>>The Democratic process suffered because he established a precedent that if
…[11 more quoted lines elided]…
> But Democracy had one of its few victories over RMN.

Yes, inasmuch as he was removed (or forced to resign).

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-09T08:02:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ok343hf9net9658vic9pncjrkgtkjh00l@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <l11143pre3jdpred1fevengcrj62t3agd5@4ax.com> <5acf41F2nmvc1U1@mid.individual.net>`

```
On Wed, 9 May 2007 11:23:45 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I'm talking about his resignation speech, after impeachment. I watched it on 
>television in Auckland, New Zealand. (In fact, I was supposed to be at work, 
>but went to a shop in Karangahape Road, near where I was working, so I could 
>see the speech. He had certainly been elected President. Don't know what 
>your referring to.)

You quoted "You won't have Richard Nixon to kick around anymore". That
was from his Checkers speech, when he was vice president before he ran
against Kennedy and way before he was president.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-09T12:21:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n2t3439fuo3jd3kru1bls6t7ue9boaeb5e@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <l11143pre3jdpred1fevengcrj62t3agd5@4ax.com> <5acf41F2nmvc1U1@mid.individual.net> <1ok343hf9net9658vic9pncjrkgtkjh00l@4ax.com>`

```
On Wed, 09 May 2007 08:02:16 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Wed, 9 May 2007 11:23:45 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>against Kennedy and way before he was president.

No, that's not correct.  It was after the 62 Cal Governor's race Nixon
lost that the "you wont have Richard Nixon to kick around any more"
bit came out.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I'd give my right arm to be ambidextrous!"
-- Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-09T14:49:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3sc4435ldp7ifmgf9pc77kmv4jk0o8tk38@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <l11143pre3jdpred1fevengcrj62t3agd5@4ax.com> <5acf41F2nmvc1U1@mid.individual.net> <1ok343hf9net9658vic9pncjrkgtkjh00l@4ax.com> <n2t3439fuo3jd3kru1bls6t7ue9boaeb5e@4ax.com>`

```
On Wed, 09 May 2007 12:21:07 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>>You quoted "You won't have Richard Nixon to kick around anymore". That
>>was from his Checkers speech, when he was vice president before he ran
…[4 more quoted lines elided]…
>bit came out.

I get those two speeches mixed up - and even said 1962 earlier in this
thread.   Then I Googled, and found it mentioned in a discussion of
Checkers - there are *lots* of mistakes that I can confirm as being
right on the web...

Thanks for my correction.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T10:05:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5aeutrF2nmus7U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <l11143pre3jdpred1fevengcrj62t3agd5@4ax.com> <5acf41F2nmvc1U1@mid.individual.net> <1ok343hf9net9658vic9pncjrkgtkjh00l@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:1ok343hf9net9658vic9pncjrkgtkjh00l@4ax.com...
> On Wed, 9 May 2007 11:23:45 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
>
No I didn't, Howard. Read it again. I said that  that phrase described his 
attitude during his resignation speech. I did not claim he said that during 
the speech. I wasn't sure when he said that and I couldn't positively 
remember whether he said it during his resignation speech or not, but it 
certainly summed up his "poor me" attitude.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-09T12:15:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net>`

```
On Tue, 8 May 2007 11:10:25 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>"Howard Brazee" <howard@brazee.net> wrote in message 
…[26 more quoted lines elided]…
>

Had he (Nixon) got away with it, you might be right.  But he was found
out and rather than face the impeachment he resigned.  What did harm
Democracy, in my opinion, was President Ford's pardon of Nixon.  That
was worse.  Another jab at democracy was Regan's escape of the whole
Iran-Contra affair.  But our democracy is strong and while it may have
been bruised by Nixon, Regan and now Bush, it will survive and prosper
so long as it stays intact.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I'd give my right arm to be ambidextrous!"
-- Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re:OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T10:36:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5af0mlF2oq2rnU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com>`

```

"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com...
> On Tue, 8 May 2007 11:10:25 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[33 more quoted lines elided]…
> out and rather than face the impeachment he resigned.

Yes, the only consolation is that he didn't get away with it. But supposing 
the Watergate breakins had never occurred? It was a near thing...

I had forgotten about the impeachment never actually happening; thanks for 
reminding me, Steve.

I suppose he does deserve some credit for at least doing the decent thing, 
once the game was up :-)

> What did harm
> Democracy, in my opinion, was President Ford's pardon of Nixon.  That
> was worse.

I think Ford was a "gentle" (in the sense of Forrest Gump...) man who was 
looking for reconciliation and to put the whole ugly business behind him. I 
agree his action was not good for Democracy.

Something that Americans may not realise is that many of the rest of us see 
the USA as a ("the"?) bastion of Freedom and Democracy. We know it is 
imperfect, but we expect the processes of Democracy to triumph there. (And, 
for the most part, they do...) But whether or not they will continue to do 
so is becoming increasingly uncertain.

When we see politics getting to the point where big business and money 
decide who will be the President (if you can't come up with 20 million you 
can't even stand), when successive Presidents show they are subject to 
manipulation by "interested parties", when people who are obviously not up 
to the job become President on the strength of their contacts and cronies, 
it is worrying for the World at large.

I want to see a healthy America because that's good for all of us.

There's an old saying that if you don't like cops, next time you're in 
trouble, call for a hippie...

I think America is a bit like that. It has the potential to do so much; it 
could be the friendly cop who you're not afraid to approach and ask 
directions from, the one who makes you feel glad he is protecting you, or it 
can be the Rodney King kind of cop who shames Humanity.

The danger is that if the choice truly slips away from the people, then it 
ISN'T a democracy any more; it is just a hollow sham and you can't blame 
emerging nations for rejecting it.


>Another jab at democracy was Regan's escape of the whole
> Iran-Contra affair.  But our democracy is strong and while it may have
> been bruised by Nixon, Regan and now Bush, it will survive and prosper
> so long as it stays intact.

I sincerely hope so, Steve. As long as ordinary men and women care about who 
governs them, as long as the attitude doesn't become: "What the Heck, 
whoever gets in it's all the same to me...there's nothing I can do about 
it..." there is hope.

Even just discussing it in an open forum like this, is, in my opinion, a 
step in the right direction.

Pete.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-09T21:35:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com>`
- **In-Reply-To:** `<5af0mlF2oq2rnU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I think Ford was a "gentle" (in the sense of Forrest Gump...) man who was 
> looking for reconciliation and to put the whole ugly business behind him. I 
> agree his action was not good for Democracy.

One could argue that it was - rather than continue down a path that 
would have been *the* story for months on end, he put a stop to it so 
that we could work on recovering from the aftermath of the Vietnam war. 
  True, getting a pardon before a conviction is a bit like putting the 
cart before the horse, but it did put the issue to bed.

> Something that Americans may not realise is that many of the rest of us see 
> the USA as a ("the"?) bastion of Freedom and Democracy. We know it is 
> imperfect, but we expect the processes of Democracy to triumph there. (And, 
> for the most part, they do...) But whether or not they will continue to do 
> so is becoming increasingly uncertain.

Don't believe the hype!  :)  We'll continue to do so, for a long, long 
time.  The biggest problem is that you've people that shout "Give us 
security!"  Then, when the security is provided, they shout "Give us 
freedom!"  They don't realize that, to have the freedom we have here, 
you're going to sacrifice security to some extent.  Nothing ventured, 
nothing gained.

I'm guessing by now you've heard about the uncovering of a terrorist 
plot on Fort Dix this week.  Our law enforcement is doing what it needs 
to do.  Sure, you're going to catch a few folks you weren't looking for, 
like was discussed earlier with the "no fly lists" and such.  With 
today's technology, every exception now has a very loud voice, and 90+% 
of our media willing to amplify it.

> When we see politics getting to the point where big business and money 
> decide who will be the President (if you can't come up with 20 million you 
…[3 more quoted lines elided]…
> it is worrying for the World at large.

To some extent, that's the nature of the beast.  I don't think big 
business and money decide the Presidency, but it definitely takes money 
to run a campaign.  Who wants it more, and who is able to convince 
others the part with their money to make it so?

(By "interested parties," I certainly hope that's not a veiled reference 
to Halliburton.  If so, change brands of Kool-Aid...  ;> )

> I want to see a healthy America because that's good for all of us.
> 
> There's an old saying that if you don't like cops, next time you're in 
> trouble, call for a hippie...

Whoa, man - that guy...  he just, like, took your wallet......

.....

..bummer....

> I think America is a bit like that. It has the potential to do so much; it 
> could be the friendly cop who you're not afraid to approach and ask 
> directions from, the one who makes you feel glad he is protecting you, or it 
> can be the Rodney King kind of cop who shames Humanity.

Heh - do you know the whole story behind the Rodney King beating?  How 
many times are the police supposed to tell you to lie down before they 
actually make you do it?  (They went too far - I'm not defending them; 
but, the fact is that they *were* provoked.)

> The danger is that if the choice truly slips away from the people, then it 
> ISN'T a democracy any more; it is just a hollow sham and you can't blame 
> emerging nations for rejecting it.

That certainly is the image projected by our media.  I can tell you 
that's untrue, but I don't quite know how to project a more positive 
image of our country, both what we're doing here and abroad.  There are 
sources that are much better than CNN-i and the BBC.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T22:26:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5agabeF2ojur7U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com...
> Pete Dashwood wrote:
<snip>>
>> Something that Americans may not realise is that many of the rest of us 
>> see the USA as a ("the"?) bastion of Freedom and Democracy. We know it is 
…[9 more quoted lines elided]…
> nothing gained.

I'm not so sure, Daniel. I believe it is possible to do what is right, 
respect the rights of all citizens, and still have "security".

I'm hesitating to write further on this because my country has not, so far, 
suffered a 911 style attack. It is therefore unfair for me to comment 
further; I don't know how I'd feel if we had. Certainly, it should make no 
difference to due process, but I have a feeling it might...

>
> I'm guessing by now you've heard about the uncovering of a terrorist plot 
> on Fort Dix this week.

No, but I'll check it out as soon as I complete these responses.

> Our law enforcement is doing what it needs to do.  Sure, you're going to 
> catch a few folks you weren't looking for, like was discussed earlier with 
> the "no fly lists" and such.  With today's technology, every exception now 
> has a very loud voice, and 90+% of our media willing to amplify it.

That's OK, PROVIDED the system is quick to recognise when it got things 
wrong and moves to correct them. (The no fly people had NO recourse; that's 
the bit that is dangerous...)


>
>> When we see politics getting to the point where big business and money 
…[12 more quoted lines elided]…
> to Halliburton.  If so, change brands of Kool-Aid...  ;> )

"Veiled reference"? Moi?!  When did that ever happen? Down here we call a 
spade a fucking shovel...

>
>> I want to see a healthy America because that's good for all of us.
…[8 more quoted lines elided]…
> ..bummer....

Exactly... :-)

>
>> I think America is a bit like that. It has the potential to do so much; 
…[7 more quoted lines elided]…
> but, the fact is that they *were* provoked.)

Don't let's go there. I saw the video...(So did most of the world...)  It 
isn't the behaviour we have a right to expect from those who protect and 
serve us.

>
>> The danger is that if the choice truly slips away from the people, then 
…[7 more quoted lines elided]…
>
As a fairly frequent visitor to the USA, with friends living there, I am 
aware that there is much of value going on. Most Americans (certainly the 
ones I've encountered) are generous and kind people who do have a sense of 
fair play, and many of them do what they can for those less fortunate than 
themselves. Without even being political, most Americans want to see a fair 
deal for all.

Nevertheless, as I mentioned above, I believe there is a real danger 
currently that choice is slipping away and, even worse, many are becoming 
disillusioned with the process and not participating to repair it. I'm not 
saying that everyone should be a political activist (Heaven forfend :-)) but 
people do need to be aware of what is happening, and should be prepared to 
speak out on what is wrong and see what can be done about it. No-one, not 
the President, not the people, and certainly not the Civil servants and 
politicians should be able to put themselves above the Law.

I don't know if it is really all about the media. I am quite capable of 
making my own mind up without having news "interpreted" for me. But when the 
actual events are flashed into your living room, it is not possible to 
dismiss it as "propaganda" by one side or another of the political spectrum. 
The best you can do is accuse them of unbalanced or biased reporting; the 
events themselves are a matter of record.

As long as the media DO continue to flash events to us, there is hope. When 
they are stopped from doing so, we all have a problem.

Pete.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-10T05:13:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178799207.666078.260990@e65g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<5agabeF2ojur7U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net>`

```
On 10 May, 11:26, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
>
> I'm not so sure, Daniel. I believe it is possible to do what is right,
…[3 more quoted lines elided]…
> suffered a 911 style attack.

But NZ citizens did die in the 9/11 attacks?
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-10T21:47:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **In-Reply-To:** `<5agabeF2ojur7U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com...
…[20 more quoted lines elided]…
> difference to due process, but I have a feeling it might...

No, you don't have to suffer an attack to have an opinion.  :)  That's 
another fallacy of the emotional.  You don't have to be a great musician 
to recognize a terrible song!

>> I'm guessing by now you've heard about the uncovering of a terrorist plot 
>> on Fort Dix this week.
> 
> No, but I'll check it out as soon as I complete these responses.

I blogged it a bit - using the title "Committing the Terrorism Americans 
Won't Commit".  (Wonder which side of the illegal immigration side I'm on?)

>> Our law enforcement is doing what it needs to do.  Sure, you're going to 
>> catch a few folks you weren't looking for, like was discussed earlier with 
…[5 more quoted lines elided]…
> the bit that is dangerous...)

On the show, or in real life?

>>> When we see politics getting to the point where big business and money 
>>> decide who will be the President (if you can't come up with 20 million 
…[13 more quoted lines elided]…
> spade a fucking shovel...

heh - touche...  I was just remember these two folks who got on Rush 
Limbaugh's show, back to back, saying that all we had to do to make Iraq 
go away is take the "profit" out of the war.  I won't go into that whole 
argument here (my online classes are calling my name), but it is based 
entirely on jealousy.  (I actually cringed when I first heard them say 
that, while listening to the podcast - Rush didn't really tear them 
apart like I thought he would.)

> Nevertheless, as I mentioned above, I believe there is a real danger 
> currently that choice is slipping away and, even worse, many are becoming 
…[5 more quoted lines elided]…
> politicians should be able to put themselves above the Law.

I do not know a previous time in our history where the sides were so 
evenly divided and so diametrically in opposition.  In an environment 
like that, there is going to be lots of fervor on both sides, so it 
becomes sort of a bidding war, to see who can raise the most money. 
Donating money to politicians is a power form of speech, and helps their 
speech be heard (AKA "getting the message out").

But, I'm generally an optimist.  I believe it is going to get better, 
and I have good reason to.  The only way the Democrats won control of 
Congress in the last election was to run a bunch of Democrats who 
claimed to be conservatives.  And, the Republicans that lost were mostly 
some of the most liberal in the country.  Though I'm not happy with the 
party breakdown (and would probably pop champagne if Joe Lieberman 
decided to switch parties), I'm very encouraged.

My biggest gripe with our current President is that he campaigned one 
way, then governed another.  We expect that from the Democrats - they 
don't take a leak without taking a poll, and the American opinion is 
often fickle.  But from Republicans, we expect them to govern using the 
principles for which we elected them.

> I don't know if it is really all about the media. I am quite capable of 
> making my own mind up without having news "interpreted" for me. But when the 
…[3 more quoted lines elided]…
> events themselves are a matter of record.

Right - but, there's even bias in story selection.  Take the news we get 
out of Iraq.  The only time it's good is when you're reading a military 
blogger, or a quote from one of our generals begging Congress for the 
money we need to continue.  Does that mean there's nothing good 
happening?  Of course not.  But those stories don't fit the mold (unjust 
war, "Bush lied people died", etc.), so they don't get broadcast.

> As long as the media DO continue to flash events to us, there is hope. When 
> they are stopped from doing so, we all have a problem.

That's what's so great about the new media.  You definitely have to do 
more checking to make sure the story's true (but you could say that for 
our mainstream networks these days as well).  But, the stories are 
getting out, and debate is occurring.  I think it's a good thing.  :)
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-11T09:17:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f21cai$gu5$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
In article <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>But, I'm generally an optimist.  I believe it is going to get better, 
>and I have good reason to.  The only way the Democrats won control of 
>Congress in the last election was to run a bunch of Democrats who 
>claimed to be conservatives.

Unless the democratic process is subverted or results in a tie, Mr 
Summers, the only way to win an election is to get more votes.

[snip]

>My biggest gripe with our current President is that he campaigned one 
>way, then governed another.  We expect that from the Democrats - they 
>don't take a leak without taking a poll, and the American opinion is 
>often fickle.  But from Republicans, we expect them to govern using the 
>principles for which we elected them.

Blessed is one who has few expectations, Mr Summers, as it makes 
disappointment more rare... but to say one thing and do another is how 
politicians - at least most I have experienced - behave.  If one takes the 
tactics of repeatedly pointing out how one is better because one is 
different than X... and then one behaves as X... then one may experience 
even more censure and approbrium.

DD
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-11T08:59:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s41943loboio7kmbheo03arufr875gfku2@4ax.com>`
- **References:** `<59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On Thu, 10 May 2007 21:47:10 -0600, LX-i <lxi0007@netscape.net> wrote:

>> I'm hesitating to write further on this because my country has not, so far, 
>> suffered a 911 style attack. It is therefore unfair for me to comment 
…[5 more quoted lines elided]…
>to recognize a terrible song!

Nor to be a woman to have an opinion on reproductive rights and
responsibilities.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-11T09:00:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v619435p0l6nkp4ikml0e905ki45eijagi@4ax.com>`
- **References:** `<59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On Thu, 10 May 2007 21:47:10 -0600, LX-i <lxi0007@netscape.net> wrote:

>My biggest gripe with our current President is that he campaigned one 
>way, then governed another.  We expect that from the Democrats - they 
>don't take a leak without taking a poll, and the American opinion is 
>often fickle.  But from Republicans, we expect them to govern using the 
>principles for which we elected them.

Power corrupts.    Principles seem to belong to those who are out of
power.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-05-11T10:51:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ri01i.2654$zj3.2320@newssvr23.news.prodigy.net>`
- **References:** `<59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com> <v619435p0l6nkp4ikml0e905ki45eijagi@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:v619435p0l6nkp4ikml0e905ki45eijagi@4ax.com...
> On Thu, 10 May 2007 21:47:10 -0600, LX-i <lxi0007@netscape.net> wrote:
>
> Power corrupts.    Principles seem to belong to those who are out of 
> power.

Power corrupts; absolute power... is actually pretty neat.

MCM
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-12T11:52:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5akdujF2pdm3gU1@mid.individual.net>`
- **References:** `<59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com> <v619435p0l6nkp4ikml0e905ki45eijagi@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:v619435p0l6nkp4ikml0e905ki45eijagi@4ax.com...
> On Thu, 10 May 2007 21:47:10 -0600, LX-i <lxi0007@netscape.net> wrote:
>
…[7 more quoted lines elided]…
> power.

Probably because that's all the powerless can afford... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-13T05:16:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179058586.743860.21790@y80g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On 11 May, 04:47, LX-i <lxi0...@netscape.net> wrote:
> Pete Dashwood wrote:
> > "LX-i" <lxi0...@netscape.net> wrote in message
…[17 more quoted lines elided]…
>

Good news doesn't sell papers. That is why you don't hear about
schools, hospitals or retractions of the lie about how many people
have died or been injured as a result of the invasion as opposed to
the numbers who would have been exterminated by a mad dictator.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-13T12:36:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f270o8$ofj$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com> <1179058586.743860.21790@y80g2000hsf.googlegroups.com>`

```
In article <1179058586.743860.21790@y80g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 11 May, 04:47, LX-i <lxi0...@netscape.net> wrote:
>> Pete Dashwood wrote:

[snip]

>> Does that mean there's nothing good
>> happening?  Of course not.  But those stories don't fit the mold (unjust
…[3 more quoted lines elided]…
>Good news doesn't sell papers.

As my Sainted Paternal Grandfather - may he sleep with the angels! - used 
to say, 'Mail Gets Delivered, Garbage Picked Up, Trains Run On Time... 
these aren't headlines, at least not usually.'

DD
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 38)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-13T15:43:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j8qdnUTM29XiG9rbnZ2dnUVZ_iydnZ2d@comcast.com>`
- **In-Reply-To:** `<f270o8$ofj$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5agabeF2ojur7U1@mid.individual.net> <Q7WdnYt7r6Tdet7bnZ2dnUVZ_jednZ2d@comcast.com> <1179058586.743860.21790@y80g2000hsf.googlegroups.com> <f270o8$ofj$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <1179058586.743860.21790@y80g2000hsf.googlegroups.com>,
> Alistair  <alistair@ld50macca.demon.co.uk> wrote:
…[13 more quoted lines elided]…
> these aren't headlines, at least not usually.'

Then doesn't that imply that one should not draw conclusions about how 
things are going (war, poverty, etc.) by reading the newspaper headlines?
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 39)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-14T09:26:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f299vo$k0u$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1179058586.743860.21790@y80g2000hsf.googlegroups.com> <f270o8$ofj$1@reader2.panix.com> <j8qdnUTM29XiG9rbnZ2dnUVZ_iydnZ2d@comcast.com>`

```
In article <j8qdnUTM29XiG9rbnZ2dnUVZ_iydnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:

[snip]

>> As my Sainted Paternal Grandfather - may he sleep with the angels! - used 
>> to say, 'Mail Gets Delivered, Garbage Picked Up, Trains Run On Time... 
…[3 more quoted lines elided]…
>things are going (war, poverty, etc.) by reading the newspaper headlines?

In the same manner, perhaps, that one should not judge a book by its 
cover... I didn't know that was news, perhaps a headline might be issued.

DD
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-10T08:29:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com>`

```
On Wed, 09 May 2007 21:35:30 -0600, LX-i <lxi0007@netscape.net> wrote:

>To some extent, that's the nature of the beast.  I don't think big 
>business and money decide the Presidency, but it definitely takes money 
>to run a campaign.  Who wants it more, and who is able to convince 
>others the part with their money to make it so?

I hope not.

It is interesting that the leading Democratic contenders are Senators.
The last time a U.S. President came directly from the legislature was
in 1960, when a first term Senator defeated Richard Nixon in a very
close race - and he had to have a Good Old Boy Texan as his running
mate while his opponent had the aristocrat Henry Cabot Lodge.   And he
still couldn't have won without Daly.

In that case, Nixon had the baggage of being known as a Congressman.
Making laws is a dirty business, full of compromises.   They have lots
of laws with pieces that people like and pieces that they don't like.
So it's easy for opponents to come up with votes that they can use.

All this money might create a shift though.   In a short attention
span world, lots of TV ads might make the difference for those who
might vote either way.

But the voting patterns in the last 2 presidential elections show that
we tend to vote for a president who we would be comfortable hanging
around with.   Rural counties voted for the guy who learned to talk
slowly.   Urban counties voted for the more urban candidate.

Which has nothing to do with policies nor effectiveness in running the
country...
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-10T21:49:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **In-Reply-To:** `<vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 09 May 2007 21:35:30 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[7 more quoted lines elided]…
> It is interesting that the leading Democratic contenders are Senators.

I actually find that encouraging!  :)  because...

> The last time a U.S. President came directly from the legislature was
> in 1960, when a first term Senator defeated Richard Nixon in a very
> close race - and he had to have a Good Old Boy Texan as his running
> mate while his opponent had the aristocrat Henry Cabot Lodge.   And he
> still couldn't have won without Daly.

And I see *no one* with the charisma of Kennedy.  Of course, all the 
dead people can still vote in Chicago - and 48 years later, there's a 
lot more of them!  :)  (It's hard to think of a better reason for 
keeping the Electoral College...)

> But the voting patterns in the last 2 presidential elections show that
> we tend to vote for a president who we would be comfortable hanging
> around with.   Rural counties voted for the guy who learned to talk
> slowly.   Urban counties voted for the more urban candidate.

You think that's why the vote broke the way it did?  Or was it just 
coincidence?
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-11T09:07:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a1943pp6hstf5k69lfsjmcm0beh9tkhge@4ax.com>`
- **References:** `<59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com> <Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On Thu, 10 May 2007 21:49:27 -0600, LX-i <lxi0007@netscape.net> wrote:

>> But the voting patterns in the last 2 presidential elections show that
>> we tend to vote for a president who we would be comfortable hanging
…[4 more quoted lines elided]…
>coincidence?

I think so very much.

Look at this map:
http://www.usatoday.com/news/politicselections/vote2004/countymap.htm


We don't elect presidents based upon competency nor even philosophy.
We elect presidents based upon which ticket has people we would be
more comfortable inviting to our home.

While running for Congress GWB lost an election where he was out
Good-old-Boy'd, and he learned his lesson.   He converted from a Yale
rich kid to a Texas folksy guy and started winning.

He won virtually all of the rural counties, and lost most all of the
urban counties.   That was enough to win.

Look at the following tickets of elections I paid attention to:


2004	Texas-Wyoming	           Massachusetts-North Carolina
2000 	Texas-Wyoming	           Tennessee-Connecticut
1996	Kansas-New York	         Arkansas-Tennessee
1992	Texas-Indiana	 	         Arkansas-Tennessee
1988	Texas-Indiana		         Massachusetts-Texas
1984	California-Texas	       Minnesota-New York
1980	California-Texas	       Georgia-Minnesota
1976	Michigan-Kansas	         Georgia-Minnesota
1972	California-Maryland	     South Dakota-Maryland
1968	California-Maryland	     Minnesota-Maine
1964	Arizona	-New York	       Texas-Minnesota
1960	California-Massachusetts Massachusetts-Texas

1.   In the elections featuring a Cowboy who we invited into our
living room once a week, the cowboy won. 1984, 1980

2.   In the presidential race, Northern beats Western, beats Southern.
2004, 1996, 1992, 1988, 1976, 1960

3.   Tie goes to the vice presidential candidate: 2000, 1968, 1964

Note:   In 1960, Massachusetts beat California (not much difference),
in a close race - the vice presidential candidates were a Texan vs an
aristocrat (Henry Cabot Lodge).   In 1972, Sargent Shriver was a
Kennedy guy, while Spiro Agnew was more of a Southerner.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-13T05:18:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179058709.062608.132300@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com> <Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com>`

```
On 11 May, 04:49, LX-i <lxi0...@netscape.net> wrote:
> Howard Brazee wrote:
> > On Wed, 09 May 2007 21:35:30 -0600, LX-i <lxi0...@netscape.net> wrote:
…[18 more quoted lines elided]…
> And I see *no one* with the charisma of Kennedy.


It is a shame that charisma is a pre-requisite for holding office.
Surely, ability should count for more? That is a rhetorical question.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-13T12:40:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2710r$pf4$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com> <Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com> <1179058709.062608.132300@k79g2000hse.googlegroups.com>`

```
In article <1179058709.062608.132300@k79g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 11 May, 04:49, LX-i <lxi0...@netscape.net> wrote:

[snip]

>> And I see *no one* with the charisma of Kennedy.
>
>
>It is a shame that charisma is a pre-requisite for holding office.
>Surely, ability should count for more? That is a rhetorical question.

... and this is not a pipe.  For an elected position, Mr Maclean, the 
prerequisite for holding offices (for the most part) is receiving more 
votes than anyone else.

For other jobs the requirements are a bit more strict... needing to be 
born into the right family, being able to lead a conquering army, et and 
cetera.

DD
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-13T15:41:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j8qdnUXM29WCG9rbnZ2dnUVZ_iydnZ2d@comcast.com>`
- **In-Reply-To:** `<1179058709.062608.132300@k79g2000hse.googlegroups.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com> <Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com> <1179058709.062608.132300@k79g2000hse.googlegroups.com>`

```
Alistair wrote:
> On 11 May, 04:49, LX-i <lxi0...@netscape.net> wrote:
>> Howard Brazee wrote:
…[10 more quoted lines elided]…
> Surely, ability should count for more? That is a rhetorical question.

But that's just it - Americans don't generally want legislators as the 
chief executive.  They prefer those who have had executive experience. 
It takes a *heap* of charisma on the legislator's part, or a large faux 
pas by their opponent, for them to obtain the Presidency.

It doesn't take charisma to hold office, but helps offset other things 
for some people.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 37)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-14T09:16:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cuug43d3c2k8ns0a755g7mgql7akvfmidb@4ax.com>`
- **References:** `<5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <6sydnYQ1sNmUDt_bnZ2dnUVZ_j-dnZ2d@comcast.com> <vba643d3rb5fsrichkfvqnugb5ifq50ng4@4ax.com> <Q7WdnYp7r6RUet7bnZ2dnUVZ_jednZ2d@comcast.com> <1179058709.062608.132300@k79g2000hse.googlegroups.com>`

```
On 13 May 2007 05:18:29 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> And I see *no one* with the charisma of Kennedy.
>
>
>It is a shame that charisma is a pre-requisite for holding office.
>Surely, ability should count for more? That is a rhetorical question.

But even charisma is partisan.    There were people who thought
Kennedy had the charisma of a used car salesman.   Anybody who talked
that quickly or who talked with an Eastern elite accent is not to be
trusted.    They prefer a slow talking "good old boy".

But those with more urban backgrounds, like the young, quick,
aristocrats.   To them "slow" is an euphemism for "idiot".

It is interesting that  Enron's "The Smartest Guys in the Room", can
be seen by both sides as belonging to the other side.
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-10T08:16:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l2a643prerhaj4l27ojl25eh6vi79s4kj8@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net>`

```
On Thu, 10 May 2007 10:36:05 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Something that Americans may not realise is that many of the rest of us see 
>the USA as a ("the"?) bastion of Freedom and Democracy. We know it is 
>imperfect, but we expect the processes of Democracy to triumph there. (And, 
>for the most part, they do...) But whether or not they will continue to do 
>so is becoming increasingly uncertain.

I suspect this is changing more quickly than we know.   

Within this country some of us are worried that we value security over
liberty, and with an endless war in sight, the Constitution doesn't
matter.

Maybe the rest of the world isn't concerned with the American
Constitution - but they don't see Freedom and Democracy enforced at
the end of a gun as being the same thing as Freedom and Democracy as
an example that works.   (The latter defeated the Soviets).
```

###### ↳ ↳ ↳ Re: OT America the beautiful? WAS OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-11T14:48:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ai3rgF2p5294U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <5af0mlF2oq2rnU1@mid.individual.net> <l2a643prerhaj4l27ojl25eh6vi79s4kj8@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:l2a643prerhaj4l27ojl25eh6vi79s4kj8@4ax.com...
> On Thu, 10 May 2007 10:36:05 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[18 more quoted lines elided]…
> an example that works.   (The latter defeated the Soviets).

Thank you Howard. I couldn't have expressed it better.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-09T18:55:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8KdnXJ1OoAs8N_bnZ2dnUVZ_h7inZ2d@comcast.com>`
- **In-Reply-To:** `<ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com>`

```
SkippyPB wrote:
> Another jab at democracy was Regan's escape of the whole
> Iran-Contra affair.

I didn't realize Alzheimer's was against the law...
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-10T12:57:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nj643hsemcfhcikh223tetih2gtbnh37t@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <f1fhr5$4n4$1@reader2.panix.com> <5a1t9hF2nfubfU1@mid.individual.net> <aifu33d1n2kt08qur9c8un1i9gmshsj0vr@4ax.com> <5a9pv1F2n9fknU1@mid.individual.net> <ems343pvl77e5j4bq3s54hbfram44j7rfg@4ax.com> <p8KdnXJ1OoAs8N_bnZ2dnUVZ_h7inZ2d@comcast.com>`

```
On Wed, 09 May 2007 18:55:58 -0600, LX-i <lxi0007@netscape.net> wrote:

>SkippyPB wrote:
>> Another jab at democracy was Regan's escape of the whole
>> Iran-Contra affair.
>
>I didn't realize Alzheimer's was against the law...

Well he did have Nancy :)

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I'd give my right arm to be ambidextrous!"
-- Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-04T20:24:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>`
- **In-Reply-To:** `<5a0uirF2muhfjU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> <docdwarf@panix.com> wrote in message news:f1evf0$g1t$1@reader2.panix.com...
>> In article <59vkpgF2mphveU1@mid.individual.net>,
…[43 more quoted lines elided]…
> actually lived there, I'd very likely be doing something about it.

Yeah, it sounds pretty bad, right?  I can't believe I'm agreeing with 
Doc on so many points here...  :)

I do know that enforcement on the Mormons has been somewhat recent, and 
there are still cases pending.  Regarding the Second Amendment, that 
isn't the only way the Commerce Clause* of the Constitution has been 
abused.  As part of the New Deal in the late 30's, quotas on grain 
production were imposed.  A farmer exceeded the quota, but claimed that 
the excess was only going to be used on his farm.  The Supreme Court 
found that, although his grain didn't enter into interstate commerce, it 
kept him from purchasing that grain on the market, which did.**  They 
also found that home-grown marijuana could be federally regulated under 
this clause.***

* http://en.wikipedia.org/wiki/Commerce_Clause
** http://en.wikipedia.org/wiki/Wickard_v._Filburn
*** http://en.wikipedia.org/wiki/Gonzales_v._Raich

On the Fourth Amendment, we part ways a bit.  Search and seizure is 
prohibited without a warrant.  Though it's a common claim of opponents 
of the "Patriot Act", seizures cannot be done without a warrant - the 
change in the act allows the warrant to be obtained and disclosed up to 
72 hours after the seizure.  If such warrants are not obtained, the 
inadmissibility of evidence comes into play just as much as it ever did. 
  To hear some people talk, you'd think that we're living in a police 
state - it is truly not as bad as some make it out to be.

> (There was a recent episode of "Boston Legal" aired here where Denny wasn't 
> able to fly because the name "Denny Crane" was on a "list" and he was 
…[8 more quoted lines elided]…
> accurate.)

It's not.  True, your name may get flagged, and you may have to answer a 
few questions, but there *are* other distinguishing characteristics. 
Have people ever had those fail?  Sure, there have been a couple - but 
you don't throw the baby out with the bath water.  Throwing that out 
would be like never doing heart surgery again, because sometimes people die.

> I was fingerprinted on entry to the USA a few months ago. First time in my 
> life. (I don't remember them doing it when I did military service, but they 
…[4 more quoted lines elided]…
> own part of me... :-)

Did you hear?  All your base are belong to us!

> I'm not sure of the gist of your post, Doc. If the foundations of American 
> democracy are indeed being undermined, then I would expect SOMEONE to be 
> making a noise about it...

There are two major groups making noise about it - Democrats and 
Republicans.  Democrat arguments are long on emotion, though often short 
on fact; Republican are grounded in fact, but can seem hard and 
uncaring.  The major media are very tilted towards the emotional (the 
whole "if it bleeds, it leads" syndrome).  I don't think their bias is 
intentional; even on Fox News (Sky's US network), the majority of 
employees are Democrats.

Each group has different things they think are the pressing issues to 
our republic.  Our President is a Republican, and the Democrat base is 
suffering from what one commentator calls BDS - Bush Derangement 
Syndrome.  They hate him so much that they're willing to bring him down 
at any cost.  However, every time they think they've got him on 
something, the fact prove otherwise, and this just makes them madder.

They had a big investigation about the release of Valerie Plame's name. 
  The emotion - "THEY LEAKED THE NAME OF A COVERT AGENT!"  The facts - 
Plame *wasn't* covert, and the "theys" they wanted to prosecute (Karl 
Rove, presidential advisor, and Dick Cheney, Vice-President) didn't do 
it.  A few years into the investigation, it was revealed that Richard 
Armitage, deputy Secretary of State, was the one who leaked it.  Shortly 
thereafter, Scooter Libby was indicted for perjury - a process crime 
brought about by his faulty memory, where instead of saying "I don't 
remember" tried to remember.

The latest involves Federal attorneys - these are political appointees 
that may be hired and fired for no reason.  Well, they fired 8 of them 
for a reason - they were not investigating voter fraud cases as they 
should.  There is nothing wrong with this, but these attorneys happen to 
be from mostly Democratic states, so this is a scandal.  Most 
frustrating as all is the fact that the Attorney General, Alberto 
Gonzales, is going up the the capital and testifying as if he's done 
something wrong.  Again, emotion over fact, yet the emotion gets all the 
airtime.

> It isn't OK to sit back and watch this.

Those of us who are in the know aren't sitting idly by.  We even take 
our cases to the Lords of COBOL!  ;)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-05T13:54:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1i2ae$9uv$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>`

```
In article <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Pete Dashwood wrote:
>> <docdwarf@panix.com> wrote in message news:f1evf0$g1t$1@reader2.panix.com...

[snip]

>>> Consider, say, the acceptability of evidence now given to materials seized
>>> in searches which have been approved by officials with no public
>>> accountability who have made the making-known of warrants a crime... in
>>> the light of the entirety of the Fourth Amendment.

[snip]

>Yeah, it sounds pretty bad, right?  I can't believe I'm agreeing with 
>Doc on so many points here...  :)

Hmmmmm... hasn't it been said that Satan can cite Scripture to suit His 
needs?

[snip]

>On the Fourth Amendment, we part ways a bit.  Search and seizure is 
>prohibited without a warrant.  Though it's a common claim of opponents 
…[5 more quoted lines elided]…
>state - it is truly not as bad as some make it out to be.

Mr Summers, to hear the owner of my ISP put it, a FISA court - the members 
of which are neither known nor accountable to the general public - can 
issue a warrant for my property which is in custody of the ISP (files) and 
not only must this property be surrendered but if the ISP notifies me of 
the warrant the owners are subject to arrest.

(interestingly enough, the FISA system was initiated after the Church 
Committee lambasted the FBI for COINTELPRO abuses)

[snip]

>They had a big investigation about the release of Valerie Plame's name. 
>  The emotion - "THEY LEAKED THE NAME OF A COVERT AGENT!"  The facts - 
>Plame *wasn't* covert, and the "theys" they wanted to prosecute (Karl 
>Rove, presidential advisor, and Dick Cheney, Vice-President) didn't do 
>it.

Mr Summers, I had a discussion about this the other day with a fellow... 
I'll call him Mr Blank.  It went something like this:

Bl: 'Plame wasn't covert.'

Me: 'Oh?  That's interesting, I thought that her employer, the Central 
Intelligence Agency (CIA), asked the Department of Justice (DOJ) to 
investigate the matter... wouldn't the CIA know that she wasn't covert and 
not have bothered to ask?'

Bl: 'The CIA asked because they were forced to do so by the shriekings of 
Democrat Congressfolks.'

Me: 'The Democratic Party was, at that time, in the minority in 
Congress... and wouldn't the CIA, having been headed by a Bush in recent 
years, have been able to tell the Congressfolks that Ms Plame wasn't 
covert at the time?'

Bl: 'They could have... but the CIA wanted to embarass the President so 
they called in the DOJ.'

Me: 'Oh... and then the DOJ did not ask, as its first question, 'what is 
the definition of a covert agent?' to see if Ms Plame fit it?'

Bl: 'No... they all wanted to embarass the President.'

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-06T08:56:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a49b5F2n92n8U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1i2ae$9uv$1@reader2.panix.com...
> In article <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[3 more quoted lines elided]…
>
<snip>>
> Bl: 'They could have... but the CIA wanted to embarass the President so
> they called in the DOJ.'
…[7 more quoted lines elided]…
>
Judging by the clips I see on Letterman, he does a pretty fair job of doing 
that all by himself...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-08T12:19:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178651948.257484.39320@y5g2000hsa.googlegroups.com>`
- **In-Reply-To:** `<f1i2ae$9uv$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com>`

```
On 5 May, 14:54, docdw...@panix.com () wrote:
>
> Hmmmmm... hasn't it been said that Satan can cite Scripture to suit His
> needs?
>

If Satan can recite scripture to suit his needs, does that not imply
that the scripture is in error or that it advocates evil deeds?

I have made attempts recently to read the Koran and am aware that
there are passages in the Koran which contradict each other. One such
advocates worship of three heathen Gods whilst the second denounces
such worship saying that the first passage was Satan speaking through
Mohammed. If Satan can speak through Mohammed once, then why not a
second time? Can any aspect of such a text be trusted?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-09T11:25:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5acf70F2nkdq3U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1178651948.257484.39320@y5g2000hsa.googlegroups.com...
> On 5 May, 14:54, docdw...@panix.com () wrote:
>>
…[13 more quoted lines elided]…
>

Faith is not about logic; you're supposed to accept it. That's the test.

(Sorry, you failed and the deal with the virgins is now off...:-))

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-09T09:15:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1s3g7$s30$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com>`

```
In article <1178651948.257484.39320@y5g2000hsa.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 5 May, 14:54, docdw...@panix.com () wrote:
>>
…[5 more quoted lines elided]…
>that the scripture is in error or that it advocates evil deeds?

Implication is in the mind of the beholder, Mr Maclean... the 
understanding I took from the aphorism was that Scripture encompassed so 
much that it could be used to the abovementioned ends.

>
>I have made attempts recently to read the Koran and am aware that
…[4 more quoted lines elided]…
>second time? Can any aspect of such a text be trusted?

You dance on the precipice of 'falsus in unum, falsus in omnia'... so it 
might be time to take a step back.  As was mentioned in another posting... 
first wonder, then research.  Can you cite the translation used and the 
passages in question?

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-09T11:50:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178736612.417596.27430@y80g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<f1s3g7$s30$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com>`

```
On 9 May, 10:15, docdw...@panix.com () wrote:
> In article <1178651948.257484.39...@y5g2000hsa.googlegroups.com>,
>
…[27 more quoted lines elided]…
> DD


>From http://www.vexen.co.uk/religion/index.html:



At one point Muhammad and his kin were opposed by the polytheists
around them. In particular, they were oppressed by the followers of 3
pagan gods in Mecca. When defeated, surrounded and under siege,
Muhammad 'seems to have even compromised his monotheism, at first, to
make peace with the Meccans'3, and suddenly recalled some text that
stated that the three pagan gods were valid intercessors [Q53:19-20],
after all! Lucky for Muhammad he remembered this important fact!

[53:19]   Compare this with the female idols Allaat and Al-`Uzzah.

[53:20]   And Manaat, the third one.

[53:21]   Do you have sons, while He has these as daughters?

and:

However Islamic tradition has it that these verses were not the result
of Muhammad's insincerity. They were verses that were sneaked into the
Koran by Satan. At an emotional moment Satan tricked Muhammad into
thinking that these verses were genuine, and it was only later that
"God annuls what Satan casts" (Q22:52).

[22:52]   We did not send before you any messenger, nor a prophet,
without having the devil interfere in his wishes. GOD then nullifies
what the devil has done. GOD perfects His revelations. GOD is
Omniscient, Most Wise.


I will admit that I do not place the same emphasis upon IDOL as does
the author of the criticism, but then I am not an Islamic scholar.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-09T19:03:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1t5tu$8sm$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com>`

```
In article <1178736612.417596.27430@y80g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 9 May, 10:15, docdw...@panix.com () wrote:
>> In article <1178651948.257484.39...@y5g2000hsa.googlegroups.com>,
…[47 more quoted lines elided]…
>[53:21]   Do you have sons, while He has these as daughters?

Mr Maclean, I do not know what to make of the scholarship of the sources 
posting at vexen.co.uk ... but a stroll over to 
http://www.submission.org/suras/sura53.html places these verses in what 
seems to be an entirely different context:

--begin quoted text:

[the Prophet speaks of a Divine Revelation of Paradise]

[53:13] He saw him in another descent. 

[53:14] At the ultimate point. 

[53:15] Where the eternal Paradise is located. 

[53:16] The whole place was overwhelmed. 

[53:17] The eyes did not waver, nor go blind. 

[53:18] He saw great signs of his Lord. 

The Flimsy Idols 

[53:19] Compare this with the female idols Allaat and Al-`Uzzah. 

[53:20] And Manaat, the third one. 

[53:21] Do you have sons, while He has these as daughters? 

[53:22] What a disgraceful distribution! 

[53:23] These are but names that you made up, you and your forefathers. 
GOD never authorized such a blasphemy. They follow conjecture, and 
personal desire, when the true guidance has come to them herein from their 
Lord.

[53:24] What is it that the human being desires? 

[53:25] To GOD belongs both the Hereafter, and this world. 

[53:26] Not even the angels in heaven possess authority to intercede. The 
only ones permitted by GOD are those who act in accordance with His will 
and His approval. 

--end quoted text

Now as I read this... the Prophet speaks of this vision and says to 
'compare this with the female idols... what a disgraceful distribution!', 
followed by the denunciation at 53:23 of 'These are but names you have 
made up... GOD never authorized such a blasphemy.  They follow conjecture, 
and personal desire, when the true guidance has come to them herein from 
their Lord.'

This, to my eyes, speaks of the 'female idols' *as opposed to* the 
Prophet's deity.

>
>and:
…[10 more quoted lines elided]…
>Omniscient, Most Wise.

... again, followed by '53. He thus sets up the devil's scheme as a test 
for those who harbor doubts in their hearts, and those whose hearts are 
hardened. The wicked must remain with the opposition.'

>
>I will admit that I do not place the same emphasis upon IDOL as does
>the author of the criticism, but then I am not an Islamic scholar.

I will admit that I usually place less emphasis on the commentary and more 
on the text and context... and those draw me to an entirely different 
conclusion.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-15T12:33:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179257635.289425.186730@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f1t5tu$8sm$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com>`

```
On 9 May, 20:03, docdw...@panix.com () wrote:
> In article <1178736612.417596.27...@y80g2000hsf.googlegroups.com>,
>
…[44 more quoted lines elided]…
> Prophet's deity.

I think that the Idols were thought to be deities too. There appears
to be some notion where the idols were accorded the status of angels
and that M is now backtracking. More reading is in order, especially
as the Vexen source seems, to my mind, to be less than impartial.

>
>
…[16 more quoted lines elided]…
>

As a rhetorical aside: The Koran that you refered to mentions, in one
of the annotations, that M travelled at millions of times the speed of
light. Wouldn't that have resulted in the universe becoming invisible?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-15T20:01:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<134kluhisf83a53@news.supernews.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com> <1179257635.289425.186730@k79g2000hse.googlegroups.com>`

```
Alistair wrote:
>
> As a rhetorical aside: The Koran that you refered to mentions, in one
> of the annotations, that M travelled at millions of times the speed of
> light. Wouldn't that have resulted in the universe becoming invisible?

Same problem as the inerrancy devotees. There are at least three problems 
with inerrancy:

1. When the text quotes someone, the text could be perfect but the speaker 
could be wrong (or lying).

2. The speaker could be exaggerating ("Solomon had treasures without end").

3. The translator or copyists could be wrong. The best example is the 
reverse of Occam's Razor: In Biblical translations, the more complex the 
text, the closer it is to being true. Often translators or copyists 
"simplified" the text to make it more palatable or understandable.

The basic rule is that it is not important what the Bible (or other sacred 
text) says. It is not even important what God (or other deity) says. What is 
important is what God meant! And often God did not say what He meant nor 
mean what He said.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-16T15:39:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5avcnbF2pr6jeU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com> <1179257635.289425.186730@k79g2000hse.googlegroups.com> <134kluhisf83a53@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:134kluhisf83a53@news.supernews.com...
> Alistair wrote:
>>
…[22 more quoted lines elided]…
>

I hope you have that out with Him when you stand before His Judgement 
Seat... :-)

I have my defence all ready; it doesn't include antagonizing a Deity who has 
on various occasions shown Himself to be spiteful, petty, unfair, and 
mentally unbalanced. I don't think telling Him he doesn't communicate well 
is going to help your case, Jerry :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-16T07:11:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179324718.233776.8870@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<134kluhisf83a53@news.supernews.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com> <1179257635.289425.186730@k79g2000hse.googlegroups.com> <134kluhisf83a53@news.supernews.com>`

```
On 16 May, 02:01, "HeyBub" <heybubNOS...@gmail.com> wrote:
> Alistair wrote:
>
…[20 more quoted lines elided]…
> mean what He said.

That makes all religions irrelevant (they can not possibly be
representing God's sayings/intent correctly and therefore must be
false).
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 36)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-16T09:28:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rl8m43dr01k22eske5guu686nbpm2ggq3n@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com> <1179257635.289425.186730@k79g2000hse.googlegroups.com> <134kluhisf83a53@news.supernews.com> <1179324718.233776.8870@k79g2000hse.googlegroups.com>`

```
On 16 May 2007 07:11:58 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>That makes all religions irrelevant (they can not possibly be
>representing God's sayings/intent correctly and therefore must be
>false).

Most Righteous Religions people believe that all of those other
religions are wrong, most of those other sects are wrong, and the guys
on the other pew are wrong.   But I am right.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-16T01:18:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2dm4f$qim$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1178736612.417596.27430@y80g2000hsf.googlegroups.com> <f1t5tu$8sm$1@reader2.panix.com> <1179257635.289425.186730@k79g2000hse.googlegroups.com>`

```
In article <1179257635.289425.186730@k79g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 9 May, 20:03, docdw...@panix.com () wrote:
>> In article <1178736612.417596.27...@y80g2000hsf.googlegroups.com>,
…[6 more quoted lines elided]…
>> --begin quoted text:

[snip]

>> [53:18] He saw great signs of his Lord.
>>
…[26 more quoted lines elided]…
>I think that the Idols were thought to be deities too.

Exactly, Mr Maclean... 'thought to be' is not the same as 'being'.  53:21 
is, as I read it, a rhetorical question, asking if his Lord has such (as 
the idols) as daughters in the same manner that the reader/listener has 
sons; 53:22 - 3, as I read them, are repudiations of such a thought.

>There appears
>to be some notion where the idols were accorded the status of angels
>and that M is now backtracking.

Given the context I read it as the Prophet is denying 'the female idols' 
any kind of divinity whatsoever, either directly (in that they are divine) 
or by descent (in that they are daughters.

>More reading is in order, especially
>as the Vexen source seems, to my mind, to be less than impartial.

You noticed that, too?  I like to read the text and then the 
commentaries... then again, perhaps I am partial to my own impartialities.

[snip]

>> >I will admit that I do not place the same emphasis upon IDOL as does
>> >the author of the criticism, but then I am not an Islamic scholar.
…[8 more quoted lines elided]…
>light. Wouldn't that have resulted in the universe becoming invisible?

Only according to some scientific standards, Mr Maclean... and religion is 
not, in my experience, science.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-09T11:52:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178736764.998198.245790@u30g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<f1s3g7$s30$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com> <f1s3g7$s30$1@reader2.panix.com>`

```
On 9 May, 10:15, docdw...@panix.com () wrote:
> In article <1178651948.257484.39...@y5g2000hsa.googlegroups.com>,
>
…[27 more quoted lines elided]…
> DD

The translation of the Koran was by: Dr. Rashad Khalifa; whoever he
is.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-09T18:41:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-I-dncmHqPnf99_bnZ2dnUVZ_s7inZ2d@comcast.com>`
- **In-Reply-To:** `<1178651948.257484.39320@y5g2000hsa.googlegroups.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <f1i2ae$9uv$1@reader2.panix.com> <1178651948.257484.39320@y5g2000hsa.googlegroups.com>`

```
Alistair wrote:
> On 5 May, 14:54, docdw...@panix.com () wrote:
>> Hmmmmm... hasn't it been said that Satan can cite Scripture to suit His
…[4 more quoted lines elided]…
> that the scripture is in error or that it advocates evil deeds?

No - only that the context in which words originate is very important to 
understanding their meaning.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-06T04:28:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178450932.894525.203550@u30g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>`

```
On 5 May, 03:24, LX-i <lxi0...@netscape.net> wrote:
>
> There are two major groups making noise about it - Democrats and
> Republicans.  Democrat arguments are long on emotion, though often short
> on fact; Republican are grounded in fact,

We know this to be true because the man at the top (GWBush) has the
ear of God.

>
> Each group has different things they think are the pressing issues to
…[3 more quoted lines elided]…
> at any cost.  

They should leave him alone and let his track record speak for itself.
That should be damning enough.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-07T09:12:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com>`

```
On Fri, 04 May 2007 20:24:07 -0600, LX-i <lxi0007@netscape.net> wrote:

>There are two major groups making noise about it - Democrats and 
>Republicans.  Democrat arguments are long on emotion, though often short 
…[4 more quoted lines elided]…
>employees are Democrats.

Some of the economic theories that Republicans had about how to help
the poor in the country made a lot of sense to me.    But once they
got power, they didn't do anything to help small business, they were
too beholden to big business.    Rural towns voted Republican, but
they are dying nevertheless.

I haven't found that the Republicans in power have been big on fact.
Certainly the poster boy Iraq war intelligence indicates not.

The Republicans certainly have big issues that are emotional in
nature.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-07T20:01:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com>`
- **In-Reply-To:** `<g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 04 May 2007 20:24:07 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[12 more quoted lines elided]…
> they are dying nevertheless.

Of course - see my earlier posts about why Presidential approval ratings 
are so low...  :)

> I haven't found that the Republicans in power have been big on fact.
> Certainly the poster boy Iraq war intelligence indicates not.

Yes, and who ran the intelligence agency?  A Clinton appointee that was 
not replaced.  No good deed goes unpunished.

> The Republicans certainly have big issues that are emotional in
> nature.

I'd be interested to hear your list - not necessarily to try to answer 
it, but to see what, in your perception, are the Republicans' "big 
emotional issues."
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-08T09:11:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1pesn$inr$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com>`

```
In article <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Howard Brazee wrote:
>> On Fri, 04 May 2007 20:24:07 -0600, LX-i <lxi0007@netscape.net> wrote:

[snip]

>> I haven't found that the Republicans in power have been big on fact.
>> Certainly the poster boy Iraq war intelligence indicates not.
>
>Yes, and who ran the intelligence agency?  A Clinton appointee that was 
>not replaced.  No good deed goes unpunished.

Quite right, Mr Summers... no decent Democrats would allow *anything* 
Republican to remain in an administration they controlled, and likewise no 
decent Republican should allow anything Democratic... including, it seems, 
the sentiment of Truman's 'The Buck Stops Here'.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-08T08:14:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com>`

```
On Mon, 07 May 2007 20:01:17 -0600, LX-i <lxi0007@netscape.net> wrote:

>> The Republicans certainly have big issues that are emotional in
>> nature.
…[3 more quoted lines elided]…
>emotional issues."

Certainly religious issues are emotional.   The gay marriage issue is
100% emotional.  Both sides of the abortion issue are emotional.   Any
"righteous" issue is basically emotional.    Despite the claim about
illegal aliens being solely about the "illegal" part, the
anti-immigration issue is the same as it has always been here, and
around the world - people feel their culture is threatened.

Humans are more driven by emotions than rationality.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-08T15:50:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1q67t$9l4$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>`

```
In article <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>Humans are more driven by emotions than rationality.

Oh, I *cannot* resist...

... and that feels like the only rational conclusion.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-09T11:30:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5acfgiF2kvsq8U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <f1q67t$9l4$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1q67t$9l4$1@reader2.panix.com...
> In article <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[10 more quoted lines elided]…
>
Resist, resist already... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-09T09:16:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1s3i7$a9c$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <f1q67t$9l4$1@reader2.panix.com> <5acfgiF2kvsq8U1@mid.individual.net>`

```
In article <5acfgiF2kvsq8U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f1q67t$9l4$1@reader2.panix.com...
…[11 more quoted lines elided]…
>Resist, resist already... :-)

Pfah... sounds like a *lot* of women I've met.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-09T11:29:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5acfejF2o3ougU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com...
> On Mon, 07 May 2007 20:01:17 -0600, LX-i <lxi0007@netscape.net> wrote:
>
…[14 more quoted lines elided]…
> Humans are more driven by emotions than rationality.

Yes, but I think we're getting better than we were... it's been quite a 
while since the emotional frenzy engendered by a mob caused us to burn 
someone as a witch, for instance.

At the least the fact that we are emotional and, therefore, sometimes 
irrational creatures, is now recognised. The first step towards dealing with 
something is to recognise it.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-09T09:37:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1s4p2$30$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net>`

```
In article <5acfejF2o3ougU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>"Howard Brazee" <howard@brazee.net> wrote in message 
>news:f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com...

[snip]

>> Humans are more driven by emotions than rationality.
>
…[6 more quoted lines elided]…
>something is to recognise it.

'... is *now* (emphasis added) recognised'?  Hang on a moment, let me use 
a few words and a search engine to make myself look wiser than I am... 
ahhhh, there you are.  From 
ftp://opensource.nchc.org.tw/gutenberg/etext99/phdrs10.txt :

--begin quoted text:

Of the nature of the soul, though her true form be ever a theme of large 
and more than mortal discourse, let me speak briefly, and in a figure.  
And let the figure be composite--a pair of winged horses and a charioteer.

[snip]

...the human charioteer drives his in a pair; and one of them is noble and 
of noble breed, and the other is ignoble and of ignoble breed; and the 
driving of them of necessity gives a great deal of trouble to him.

[snip]

As I said at the beginning of this tale, I divided each soul into three--
two horses and a charioteer; and one of the horses was good and the other
bad:

--end quoted text

(pardon my midsentence snippage; I believe that the author's intent was 
maintained - a description of a charioteer driving two horses, one good 
and the other bad - but a glance at the text will show some weighty 
sentences, indeed)

So... it gets even better, Mr Dashwood; about two-and-a-half millennia 
back not only was the disjunction between intellect (charioteer) and 
emotions (horses) noticed but the difficulties that the intellect has 
controlling and balancing the good emotions (the right-hand horse) and the 
base emotions (the left-hand horse) rather prettily described.

Oh... and forget that Nietszche fellow who commented 'Whoever said 'Alas, 
two souls dwell within my breast!' fell short... by a goodly number of 
souls.'

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T00:36:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5adti2F2n8175U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <f1s4p2$30$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1s4p2$30$1@reader2.panix.com...
> In article <5acfejF2o3ougU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[58 more quoted lines elided]…
>
Yes, Doc, I have read Bhagavad Gita (indeed, the entire Mahabharata) where 
similar analogy was made around 2000 years ago... Krishna seems to have been 
a fairly capable charioteer; Arjuna's chariot had 4 horses if I remember 
correctly...Coping with these in the midst of battle was no mean feat.

I guess I should have qualified what I wrote.

Here, I'll do it now...

"At least the fact that we are emotional and, therefore, sometimes
irrational creatures, is now MORE GENERALLY recognised.  The first step 
towards dealing with
something is to recognise it."

My point was that a rise in "education" has raised the general awareness of 
our imperfections. I did not mean to imply that no philosopers had ever 
questioned this before.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-09T13:24:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1si1o$nc6$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <f1s4p2$30$1@reader2.panix.com> <5adti2F2n8175U1@mid.individual.net>`

```
In article <5adti2F2n8175U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f1s4p2$30$1@reader2.panix.com...
…[21 more quoted lines elided]…
>> ahhhh, there you are.

[snip]

>> So... it gets even better, Mr Dashwood; about two-and-a-half millennia
>> back not only was the disjunction between intellect (charioteer) and
…[20 more quoted lines elided]…
>something is to recognise it."

Wow, now there's a neat trick... when a quantifiable specific is 
contradicted by documentation it is time to... change it to an 
unquantifiable generalisation!

('Oh, there's evidence to show 'is now recognised' is incorrect?  Change 
it to 'is MORE GENERALLY recognised', that'll take care of things.')

>
>My point was that a rise in "education" has raised the general awareness of 
>our imperfections. I did not mean to imply that no philosopers had ever 
>questioned this before.

My point was that lo, there is nothing completely new under the sun... but 
I think that's been said before.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T11:00:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5af24hF2ocetoU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <f1s4p2$30$1@reader2.panix.com> <5adti2F2n8175U1@mid.individual.net> <f1si1o$nc6$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1si1o$nc6$1@reader2.panix.com...
> In article <5adti2F2n8175U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[58 more quoted lines elided]…
> unquantifiable generalisation!

Watch and learn... :-)

>
> ('Oh, there's evidence to show 'is now recognised' is incorrect?  Change
> it to 'is MORE GENERALLY recognised', that'll take care of things.')
>

'is now recognised' is NOT incorrect. It is axiomatic... look around.

However, the inference drawn was not what I intended (I never intended to 
suggest that NO-ONE had ever recognised the imperfections of Humanity 
before; rather, that Behavioural sciences and the recognition and attempts 
to understand such imperfection is a comparatively recent phenomenon, and, 
with the increase in literacy and education over the last several thousand 
years, people are now more aware of their complexity than was previously the 
case.)

A perfectly reasonable and innocuous statement, I would've thought... 
(unless, of course, one is simply looking for an argument at any price)

At the time of the Sanskrit literature (even after the original Pali texts, 
which some suggest may be the oldest written record on the planet), people 
(most of whom could not read and write and so had not come into contact with 
philosophical wisdom except by listening to their priests) did not generally 
think about emotionality and rationality. Rather, whatever happened, 
(including the behaviour of Humans) was the Will of God (or Gods)

My statement simply suggests we have moved on from there.

>>
>
> My point was that lo, there is nothing completely new under the sun... but
> I think that's been said before.

I don't disagree. (Both with the statement and with its having been said 
before... :-))

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-09T08:07:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6l3431g55kd8ngues8q9nr8q2t3t6vt1t@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <f1s4p2$30$1@reader2.panix.com> <5adti2F2n8175U1@mid.individual.net>`

```
On Thu, 10 May 2007 00:36:16 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>"At least the fact that we are emotional and, therefore, sometimes
>irrational creatures, is now MORE GENERALLY recognised.  The first step 
>towards dealing with
>something is to recognise it."

Although in this smaller world, the wars of the irrationally Righteous
against the irrationally Righteous threaten us all.    How many wars
are between rational enemies these days?    (A rational war is when
famine forces someone to leave home and invade a richer land which
defends itself).

Even the so irrational, they're silly scams keep The Amazing Randi
working full time.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-09T04:14:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178709271.518274.237630@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5acfejF2o3ougU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net>`

```
On 9 May, 00:29, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Howard Brazee" <how...@brazee.net> wrote in message
>
…[26 more quoted lines elided]…
> someone as a witch, for instance.

No more than 200 years. And the last witchcraft trial in the UK was
(IIRC) this side of WW2.

For the record: some witches are remembered fondly (Lizzie Bryce in
Livingston near Edinburgh).

>
> At the least the fact that we are emotional and, therefore, sometimes
…[5 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-09T08:09:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6el343pfbouviba0ee0ilmotmm0u8il9kq@4ax.com>`
- **References:** `<59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <1178709271.518274.237630@h2g2000hsg.googlegroups.com>`

```
On 9 May 2007 04:14:31 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Yes, but I think we're getting better than we were... it's been quite a
>> while since the emotional frenzy engendered by a mob caused us to burn
…[3 more quoted lines elided]…
>(IIRC) this side of WW2.

For various values of "we".     People have been stoned within the
last year for witchcraft around the world.

And people were killed today for being the wrong flavor of Muslim.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 34)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T11:04:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5af2bjF2o1mneU1@mid.individual.net>`
- **References:** `<59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <1178709271.518274.237630@h2g2000hsg.googlegroups.com> <6el343pfbouviba0ee0ilmotmm0u8il9kq@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:6el343pfbouviba0ee0ilmotmm0u8il9kq@4ax.com...
> On 9 May 2007 04:14:31 -0700, Alistair
> <alistair@ld50macca.demon.co.uk> wrote:
…[11 more quoted lines elided]…
> And people were killed today for being the wrong flavor of Muslim.

Indisputably.

But somewhere, someone, today learned something about Mathematics, Art, 
Humanities, Science and Philosophy, too...

It isn't ALL bad.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-09T19:37:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1344qajja0ldjda@news.supernews.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Yes, but I think we're getting better than we were... it's been quite
> a while since the emotional frenzy engendered by a mob caused us to
> burn someone as a witch, for instance.

Or, it could be because we've burnt them all.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-10T14:31:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5afefnF2okii0U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <5acfejF2o3ougU1@mid.individual.net> <1344qajja0ldjda@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:1344qajja0ldjda@news.supernews.com...
> Pete Dashwood wrote:
>>
…[7 more quoted lines elided]…
>
Lol!

You haven't met my Aunt... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-09T18:39:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-I-dnc6HqPkp9N_bnZ2dnUVZ_s7inZ2d@comcast.com>`
- **In-Reply-To:** `<f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 07 May 2007 20:01:17 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[11 more quoted lines elided]…
> around the world - people feel their culture is threatened.

Man - I shouldn't have said I didn't want to parse the list...  :)

Illegal immigrants - committing the crimes that Americans won't commit!
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 32)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-13T17:06:15-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vqre43d47o1np84f0k65un2nji37anis58@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <haSdnUo1i6lhRKLbnZ2dnUVZ_gydnZ2d@comcast.com> <f711435v2r7aflq1ofc1rgct3ro112k8eg@4ax.com> <-I-dnc6HqPkp9N_bnZ2dnUVZ_s7inZ2d@comcast.com>`

```
On Wed, 09 May 2007 18:39:16 -0600, LX-i <lxi0007@netscape.net> wrote:

>Howard Brazee wrote:
>> On Mon, 07 May 2007 20:01:17 -0600, LX-i <lxi0007@netscape.net> wrote:
…[16 more quoted lines elided]…
>Illegal immigrants - committing the crimes that Americans won't commit!

Or being hired by various entities, government and otherwise to do the
dirty work for the entity.  This includes government of choice or
affliction and various NGO's including corporations.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-09T19:53:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1344r7nhr7fl42a@news.supernews.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com>`

```
Howard Brazee wrote:
>
> Some of the economic theories that Republicans had about how to help
> the poor in the country made a lot of sense to me.    But once they
> got power, they didn't do anything to help small business, they were
> too beholden to big business.

Huh? Three tax cuts in three years, including a dramatic reduction in the 
death tax? Holding the line on minimum wage? Putting a stop to the welfare 
teat helped small business by forcing people into the job market. Health 
Savings Accounts and reduced regulation are also Republican initiatives. 
Very many "big businesses" started out in recent times as "small businesses" 
(Google, Ebay, Microsoft, Yahoo, Enron, YouTube, well, maybe not Enron).

> Rural towns voted Republican, but they are dying nevertheless.

As did Houston and other major cities in the South and West - but they're 
not dying.

>
> I haven't found that the Republicans in power have been big on fact.
> Certainly the poster boy Iraq war intelligence indicates not.

Uh, the intelligence on the Iraq war build up was orchestrated by a 
Democratic appointee (George Tenent).

>
> The Republicans certainly have big issues that are emotional in
> nature.

Um, that's certainly true if you equate religious belief with emotion.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-10T08:37:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8b643ddgb5mb6711nn8sub847ndtp3149@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <FfmdnVe2QuNwd6bbnZ2dnUVZ_oKnnZ2d@comcast.com> <g5gu331fuos8jqjum8lv8l9npe5kd7kebp@4ax.com> <1344r7nhr7fl42a@news.supernews.com>`

```
On Wed, 9 May 2007 19:53:16 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>> I haven't found that the Republicans in power have been big on fact.
>> Certainly the poster boy Iraq war intelligence indicates not.
>
>Uh, the intelligence on the Iraq war build up was orchestrated by a 
>Democratic appointee (George Tenent).

I liked the way the Republicans praised Truman's "The Buck Stops Here"
sign.    Which presidents does it apply to?

>> The Republicans certainly have big issues that are emotional in
>> nature.
>
>Um, that's certainly true if you equate religious belief with emotion. 

What do you believe all of those other religion's belief that are
contrary to yours are based on?    Fact?

My religious beliefs are based upon fact, yours on emotion?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-06T04:17:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178450249.868709.299960@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<5a0uirF2muhfjU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net>`

```
On 4 May, 15:34, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:f1evf0$g1t$1@reader2.panix.com...
> (There was a recent episode of "Boston Legal" aired here where Denny wasn't
…[9 more quoted lines elided]…
> accurate.)

As accurate as the FBI system which had an innocent Britain arrested
in Africa and imprisoned for 6 months while he tried to convince the
authorities that he was not the man named on the FBI arrest warrant.
His crime? He had the same name as another British person wanted for
fraud. The local authorities were convinced quite quickly of his
innocence but the FBI dragged its' feet for 6 months before releasing
him. Of course, if your name is logged on a computer somewhere then
you must be a criminal.

>
> Raise it. Write to the Head of Department  and if you get no satisfaction
> escalate it. Talk to your Congressman.Talk to your colleagues and
> associates; raise awareness.

If you raise your head above the parapet then you will get it shot at.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-07T01:08:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a62a4F2nj0ucU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <1178450249.868709.299960@o5g2000hsb.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1178450249.868709.299960@o5g2000hsb.googlegroups.com...
> On 4 May, 15:34, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[33 more quoted lines elided]…
> If you raise your head above the parapet then you will get it shot at.

"All it takes for evil to prevail, is for good men to do nothing."

(And, speaking of parapets and being shot at, I had exactly this experience 
in BanglaDesh...There were bullets ricocheting off the concrete but 
miraculously I wasn't hit...  If I'd had a weapon I would've killed 
someone... being shot at by people who don't even know you tends to make you 
VERY angry :-))

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-06T14:58:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1kqf1$9go$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a0uirF2muhfjU1@mid.individual.net> <1178450249.868709.299960@o5g2000hsb.googlegroups.com> <5a62a4F2nj0ucU1@mid.individual.net>`

```
In article <5a62a4F2nj0ucU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
>news:1178450249.868709.299960@o5g2000hsb.googlegroups.com...
>> On 4 May, 15:34, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
>> wrote:

[snip]

>>> Raise it. Write to the Head of Department  and if you get no satisfaction
>>> escalate it. Talk to your Congressman.Talk to your colleagues and
…[4 more quoted lines elided]…
>"All it takes for evil to prevail, is for good men to do nothing."

Compare and contrast:

'The nail that sticks up gets hammered down.'

'The nail that sticks up is useful for hanging a coat.'

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-08T02:01:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a8ppgF2l79c2U1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a0uirF2muhfjU1@mid.individual.net> <1178450249.868709.299960@o5g2000hsb.googlegroups.com> <5a62a4F2nj0ucU1@mid.individual.net> <f1kqf1$9go$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f1kqf1$9go$1@reader2.panix.com...
> In article <5a62a4F2nj0ucU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[24 more quoted lines elided]…
>
OR...

"Too many cooks spoil the broth"  ...but...

"Many hands make light work"

OR

"Look before you leap" ...but...

"He who hesitates is lost"

etc.

Can/should we live our lives according to adages, or should we rather 
evaluate situations for ourselves and act accordingly?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-07T18:38:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1nrmv$n7f$1@reader2.panix.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <5a62a4F2nj0ucU1@mid.individual.net> <f1kqf1$9go$1@reader2.panix.com> <5a8ppgF2l79c2U1@mid.individual.net>`

```
In article <5a8ppgF2l79c2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f1kqf1$9go$1@reader2.panix.com...

[snip]

>> Compare and contrast:
>>
…[19 more quoted lines elided]…
>evaluate situations for ourselves and act accordingly?

Plural majestatus est, Mr Dashwood... I barely know what *I* can/should 
do, let alone anyone else.  Balancing what one learns from Ye Wisdome of 
Ye Ancientes with one's desire not to be a slave to the past might not be 
so easy a task...

... but those who remember what Santayana said about the mistakes of the 
past are condemned to repeat it.

DD
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 29)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-07T05:49:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178542172.049258.298830@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5a62a4F2nj0ucU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <1178450249.868709.299960@o5g2000hsb.googlegroups.com> <5a62a4F2nj0ucU1@mid.individual.net>`

```
On 6 May, 14:08, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[52 more quoted lines elided]…
> - Show quoted text -

That sounds like an interesting story. TELL ME.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-08T02:11:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a8qc8F2ndpbjU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net> <1178450249.868709.299960@o5g2000hsb.googlegroups.com> <5a62a4F2nj0ucU1@mid.individual.net> <1178542172.049258.298830@h2g2000hsg.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1178542172.049258.298830@h2g2000hsg.googlegroups.com...
> On 6 May, 14:08, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[65 more quoted lines elided]…
> That sounds like an interesting story. TELL ME.

Sorry, I have no intention of elaborating... (I don't come out of it very 
well if I did... and it was a long time ago) For me the important part was 
that (rather than being scared, which would have been a much more rational 
emotion), all I felt was anger (which is very rare for me). I can understand 
people who KNOW me wanting to shoot me :-), but total strangers? That's 
cruel and unnatural punishment...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 27)_

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-05-10T18:02:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ibadnW5PKPGCzd7bnZ2dnUVZ8qSnnZ2d@pipex.net>`
- **In-Reply-To:** `<5a0uirF2muhfjU1@mid.individual.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <59snn9F2mag88U1@mid.individual.net> <1178214899.781963.175340@q75g2000hsh.googlegroups.com> <59vkpgF2mphveU1@mid.individual.net> <f1evf0$g1t$1@reader2.panix.com> <5a0uirF2muhfjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> Democracy has to work, because all the alternatives are not even options, 
> for free people.
> 
> Pete.

It would be interesting to hear what 'democracy' and 'free' mean.

As far as I can tell, democracy means being able to vote for 
any of the candidates put before you .... by the oligarchy.

As for free - what comes first, civil freedom or economic freedom?
How do we see freedom 'in action', please?

It's a nice notion and kind of has an axiomatic ring - 
democracy has to work for free people - but I think it's a 
myth, so I don't subscribe.

If you subscribe to the idea, do please elucidate these 
fundamentals.

Michael
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-11T16:19:55-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73g943hedkovf2crjne8an6qe8qk29bv8l@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <59ntg4F2lssg8U1@mid.individual.net> <1tOdnVrcVNDsVKvbnZ2dnUVZ_hudnZ2d@comcast.com>`

```
On Mon, 30 Apr 2007 23:00:07 -0600, LX-i <lxi0007@netscape.net> wrote:

>Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[48 more quoted lines elided]…
>would be an even bigger one."

Yet the US uses Syria as one its torture destinations.  Check the
deportation of Mahar Arar, a Syrian born Canadian in transit in New
York (connecting flight to Canada from the Middle East or Europe) to
Syria.  I can see throwing him in jail if they have evidence he is a
terrorist.  I can see making sure that he gets on the plane to Canada.
I can't see flying him to Jordan and then driving him to Syria.  The
whole question of renditions which goes back many years and was
discussed in a Wall Street Journal I read in the 1980's or early
1990's shows a not so good side of the US.  

>> rest snipped
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 19)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-01T15:10:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com>`
- **References:** `<5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com>`

```
On Mon, 30 Apr 2007 20:50:31 -0600, LX-i <lxi0007@netscape.net> wrote:

>Alistair wrote:
>> On 30 Apr, 01:53, LX-i <lxi0...@netscape.net> wrote:
…[36 more quoted lines elided]…
>our (US) soldiers!  Why go see Assad?  Was Satan unavailable?

Then why did the US send Canadian citizens of Syrian birth to Syria
instead of allowing them to continue on to Canada?  Was Syria going to
be used to torture information out of them why the US issued pious
denials?  The hypocrisy in this case stinks.  I also believe that the
Bush rules of engagement endanger US citizens everywhere by making
renditions legitimate.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-01T09:51:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rfoe33t6fsqvpvp3anghuud5rp823qv5kr@4ax.com>`
- **References:** `<xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com>`

```
On Tue, 01 May 2007 15:10:08 GMT, Clark F Morris
<cfmpublic@ns.sympatico.ca> wrote:

>Then why did the US send Canadian citizens of Syrian birth to Syria
>instead of allowing them to continue on to Canada?  Was Syria going to
…[3 more quoted lines elided]…
>renditions legitimate.

For various values of "legitimate".
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-01T22:06:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t92dnfvElLXik6XbnZ2dnUVZ_segnZ2d@comcast.com>`
- **In-Reply-To:** `<3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com>`
- **References:** `<5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com>`

```
Clark F Morris wrote:
> 
> Then why did the US send Canadian citizens of Syrian birth to Syria
> instead of allowing them to continue on to Canada?  Was Syria going to
> be used to torture information out of them why the US issued pious
> denials?  The hypocrisy in this case stinks.

I'm not familiar with that case - though, if you have a good place to 
read up about it, I'll put it in the "to read" queue.  Nevertheless, as 
an E-6 in the USAF, I don't have much say in immigration and visitation 
policies.  :)  If our country has messed up, I'll admit it - no one's 
perfect.

> I also believe that the
> Bush rules of engagement endanger US citizens everywhere by making
> renditions legitimate.

It depends on how wedded to terrorism some of these countries are.  If 
that's their way of life, US citizens should probably stay out of those 
countries.

You're never going to be 100% safe, though.  I'm sure you heard about 
the shooting at Virginia Tech a few weeks ago.  When someone is intent 
on committing evil, and is willing to die in that commission, it's 
impossible to completely stop.  You can take safeguards, and if you make 
yourself a hard target, you'll probably be OK.  (This assertion is 
backed up by real-life information from US citizens stationed abroad.)
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 21)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2007-05-02T11:31:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<njbh33d7ubpkal2rneupvdb7ejdico4vja@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com> <t92dnfvElLXik6XbnZ2dnUVZ_segnZ2d@comcast.com>`

```
On Tue, 01 May 2007 22:06:52 -0600, LX-i <lxi0007@netscape.net> wrote:

>Clark F Morris wrote:
>> 
…[10 more quoted lines elided]…
>

See http://www.cbc.ca/news/background/arar/.


>> I also believe that the
>> Bush rules of engagement endanger US citizens everywhere by making
…[11 more quoted lines elided]…
>backed up by real-life information from US citizens stationed abroad.)

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"If you take an Oriental person and spin him around several times, 
does he become disoriented?"
--Geroge Carlin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 22)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-02T16:49:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aqdndacBf0UiKTbnZ2dnUVZ_tHinZ2d@comcast.com>`
- **In-Reply-To:** `<njbh33d7ubpkal2rneupvdb7ejdico4vja@4ax.com>`
- **References:** `<Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <3sle33tu89ashekkambbf0n76gqhp0rhsg@4ax.com> <t92dnfvElLXik6XbnZ2dnUVZ_segnZ2d@comcast.com> <njbh33d7ubpkal2rneupvdb7ejdico4vja@4ax.com>`

```
SkippyPB wrote:
> On Tue, 01 May 2007 22:06:52 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[12 more quoted lines elided]…
> See http://www.cbc.ca/news/background/arar/.

Thanks - I'll look into that...
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 19)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-02T13:01:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1178136076.844040.301060@y80g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com>`

```

LX-i wrote:

> Alistair wrote:
> > On 30 Apr, 01:53, LX-i <lxi0...@netscape.net> wrote:
…[23 more quoted lines elided]…
> the Northern Ireland peace process.

You need to look at Noraid and the repeated refusal of the USA
governments to move against Noraid.

> Maybe we screwed up - it certainly
> wouldn't be a first for our nation.  But the failures of the past are
…[3 more quoted lines elided]…
> because we had probably sold it to them!)

Just as well you didn't sell them Stinger missiles.

>
> And, to the best of my knowledge, the IRA hasn't threatened our national
> security.  Though it makes for entertaining cinema, we're *not* the
> world police.

I like the Thunderbirds style movie that came out a little while back.

>
> And a final point about Pelosi's trip - Syria harbors terrorists, is
> sympathetic to them, and is even letting them cross into Iraq to fight
> our (US) soldiers!  Why go see Assad?  Was Satan unavailable?

No, he's exclusively signed to appear with Saddam Hussein in South
Park.

>
> --
…[12 more quoted lines elided]…
> a man who's offended by a God he doesn't believe in?" - Brad Stine
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-02T16:53:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_uydnRXvQ875i6TbnZ2dnUVZ_h6vnZ2d@comcast.com>`
- **In-Reply-To:** `<1178136076.844040.301060@y80g2000hsf.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com> <GOadnXDqfvKWNqvbnZ2dnUVZ_tWhnZ2d@comcast.com> <1178136076.844040.301060@y80g2000hsf.googlegroups.com>`

```
Alistair wrote:
> LX-i wrote:
> 
…[4 more quoted lines elided]…
> governments to move against Noraid.

OK - I will.

>> Maybe we screwed up - it certainly
>> wouldn't be a first for our nation.  But the failures of the past are
…[5 more quoted lines elided]…
> Just as well you didn't sell them Stinger missiles.

heh - true...  Maybe we knew they were bad guys, so we didn't give them 
the good stuff.

>> And, to the best of my knowledge, the IRA hasn't threatened our national
>> security.  Though it makes for entertaining cinema, we're *not* the
>> world police.
> 
> I like the Thunderbirds style movie that came out a little while back.

It is hilarious.  "Durka Durka, Mohammed Jihad!"  I'm sure that's how 
the world views the US in certain situations.  I especially enjoyed the 
demise of several leftist puppets toward the end of the movie.

>> And a final point about Pelosi's trip - Syria harbors terrorists, is
>> sympathetic to them, and is even letting them cross into Iraq to fight
…[3 more quoted lines elided]…
> Park.

That's right - I forgot.  Mr. Dashwood said his schedule is also pretty 
busy when South Park isn't shooting!
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 18)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-01T19:59:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<133fojvsfdnk011@news.supernews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <FfSdncXcZZry_6zbnZ2dnUVZ_h2pnZ2d@comcast.com> <CrgYh.132963$DE1.61323@pd7urf2no> <6eadnVLlIfQDA6_bnZ2dnUVZ_sudnZ2d@comcast.com> <0uUYh.143628$aG1.81147@pd7urf3no> <k_idndX2V7Xbo6jbnZ2dnUVZ_jqdnZ2d@comcast.com> <1177954440.699544.303810@e65g2000hsc.googlegroups.com>`

```
Alistair wrote:
> <blood boiling mode>
>
…[5 more quoted lines elided]…
> </blood boiling mode>

Iran was not a sponsor of terrorism when the U.S. supplied it with arms; 
Iran was fighting Iraq - a sponsor of terrorism.

As for the Contras, they were fighting Communists (Sandinistas) which was a 
Good Thing (tm).
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-27T07:32:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com>`
- **References:** `<1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no>`

```
On Thu, 26 Apr 2007 22:11:53 GMT, "James J. Gavan"
<jgavandeletethis@shaw.ca> wrote:

>What the hell is an E-7 ? OK, so I used Google to find out.
>
…[4 more quoted lines elided]…
>plus the second shows RAF rank insignia, (presumably current ?).

Since I went to college and became a (USAF) pilot, I started off as an
officer.   But that wasn't really a management position.

It is interesting following history of ranks.   When George Washington
hired his staff, the various generals he hired had titles that showed
what their jobs were.    For most of history someone could be a good
soldier without having a rank - he was just a soldier.   Ranks were
titles dependent upon responsibility - although a nobleman was a
nobleman and were deemed unsuitable for anything but leadership.
Someone could switch units and switch ranks - depending on what jobs
needed to be done.

But as armies consolidated under control of states, so did management.
Promotion criteria were codified and the promotion gave titles that
went with pay - but with a wide variety of duties.

The bigger the civilian organization, the more it follows this
evolutionary development.    I work for the State of Colorado (and for
the University of Colorado), I know what a title means and earns.

When I worked for EDS, I wondered what my title meant.   Apparently it
meant "when EDS sends someone to work with your workers, you won't get
confused about where he ranks with your workers" - because he won't
have the same title as your workers.
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-27T18:23:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<scrYh.134020$DE1.61713@pd7urf2no>`
- **In-Reply-To:** `<s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com>`
- **References:** `<1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 26 Apr 2007 22:11:53 GMT, "James J. Gavan"
> <jgavandeletethis@shaw.ca> wrote:
…[12 more quoted lines elided]…
> officer.   But that wasn't really a management position.

Well it could have been a 'management position' if you had been a 
squadron commander - somebody has to be in charge :-).

Big assumption on my part - but get the impression you were only in USAF 
for a comparatively short period, say five/eight years ? Now even there 
had you been a flight commander within a squadron you would have been a 
sub-manager. (I'm not using the terminology you probably would, but I've 
no doubt you will get the gist).

If you think I'm being over sensitive about the caste system, (although 
I did get recommended for a cadetship at RAF Cranwell twice - RAF 
equivalent of Sandhurst or West Point), take the following :

Last years in RAF I was posted to NATO in Germany. Normally overseas 
postings are a 2.5 year stint. As I was leaving the RAF it was only 2 
years so that the last six months saw me back in UK to acclimatize and 
prepare for civvy street. This was 1959. Anyway had to get a civilian 
ferry boat from England's east coast at Harwich which took us to the 
Hook of Holland.

As we were preparing to board a message came over the ship's tannoy 
system. "Officers and their ladies can take refreshment in ....... 
Senior NCOs and their wives can take refreshment in ........ Soldiers 
and airmen and their women can take refreshment in...... ". I kid you not !

You might also recall I once wrote that in WWII two fighter pilots 
having shot down say two enemy planes apiece could be put forward for 
gallantry. One could be a Pilot or Flying Officer, and the other a 
sergeant pilot. They both roll up to Buckingham Palace to be presented 
with their medals by George VI.  What do they get respectively - DFC 
(Distinguished Flying Cross) for the commissioned officer and the DFM 
(Distinguished Flying Medal) for the non-comm. Slightly less 'brave' 
medal would have been the AFC or AFM. The 'Crosses' still exist but the 
'Medals' have been discreetly dropped from the official list of awards.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-27T13:07:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k9i433hb7ebeelrfjlmbumd956v8do3h1n@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com> <scrYh.134020$DE1.61713@pd7urf2no>`

```
On Fri, 27 Apr 2007 18:23:20 GMT, "James J. Gavan"
<jgavandeletethis@shaw.ca> wrote:

>As we were preparing to board a message came over the ship's tannoy 
>system. "Officers and their ladies can take refreshment in ....... 
>Senior NCOs and their wives can take refreshment in ........ Soldiers 
>and airmen and their women can take refreshment in...... ". I kid you not !

One thing I liked when I was in pilot training at Craig AFB - the
Officer's club wasn't open for breakfast.   That meant I was allowed
to eat in the dining hall - which was lots of good food fast.

I agree that the caste system is an abomination.   But even in America
in business and even politics - it exists.    Admittedly, we don't see
class in all of our movies (Loved _The Ruling Class_), the way Brits
do - we're not that caste ridden.  (And the Brits aren't to Indian
standards). 

Anybody doubt the American president's good old boy network isn't
caste?
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 15)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-27T15:11:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Sv-dnYLb9b5X16_bnZ2dnUVZ_vzinZ2d@golden.net>`
- **In-Reply-To:** `<k9i433hb7ebeelrfjlmbumd956v8do3h1n@4ax.com>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com> <scrYh.134020$DE1.61713@pd7urf2no> <k9i433hb7ebeelrfjlmbumd956v8do3h1n@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 27 Apr 2007 18:23:20 GMT, "James J. Gavan"
> <jgavandeletethis@shaw.ca> wrote:
…[17 more quoted lines elided]…
> caste?

My mother use to say(she grew up in Ireland) that the only difference 
between the North American and the British Isles caste systems was that 
the first was determined by money, while the second was determined by 
school and birth.

Donald
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 16)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-27T22:07:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QuuYh.134569$DE1.90591@pd7urf2no>`
- **In-Reply-To:** `<Sv-dnYLb9b5X16_bnZ2dnUVZ_vzinZ2d@golden.net>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com> <scrYh.134020$DE1.61713@pd7urf2no> <k9i433hb7ebeelrfjlmbumd956v8do3h1n@4ax.com> <Sv-dnYLb9b5X16_bnZ2dnUVZ_vzinZ2d@golden.net>`

```
Donald tees wrote:
> Howard Brazee wrote:
> 
…[28 more quoted lines elided]…
> Donald

I think I'd agree with your mother's observation Donald. Hey. You ain't 
all bad, although a Scot from your Empire Loyalist roots, just think 
what your mother's Irish blood/or domicile has given you :-)

As to Howard's reference to caste above - somebody sure got the mould 
formula wrong when they 'cast' the image of the current guy. It's to be 
hoped, like Madame Tussaud's (wax works, in London), that they 
eventually break the mould up so that the same accident can't happen twice.

Hadn't realized - the old lady has gone international - London, New 
York, Las Vegas, Amsterdam and Hong Kong. The first is a marketing blurb 
whereas Wikipedia gives you more in depth information :-

http://www.madame-tussauds.com/
http://en.wikipedia.org/wiki/Madame_Tussauds

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Military Ranks/Computers : WAS Re: newbie question on cobol syntax

_(reply depth: 17)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-27T20:43:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<raKdnY4FatVcBa_bnZ2dnUVZ_r-onZ2d@golden.net>`
- **In-Reply-To:** `<QuuYh.134569$DE1.90591@pd7urf2no>`
- **References:** `<bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <Js9Yh.131155$DE1.38614@pd7urf2no> <s2u3335r9uj5d2erphqk0jhtncnmjv3d24@4ax.com> <scrYh.134020$DE1.61713@pd7urf2no> <k9i433hb7ebeelrfjlmbumd956v8do3h1n@4ax.com> <Sv-dnYLb9b5X16_bnZ2dnUVZ_vzinZ2d@golden.net> <QuuYh.134569$DE1.90591@pd7urf2no>`

```
James J. Gavan wrote:
> Donald tees wrote:
> 
…[3 more quoted lines elided]…
> 

Empire Loyalist is apparently wrong. Right time frame, but it seems 
great-great-great granddaddy arrived straight from the old sod, complete 
with young bride in tow.

Funny, I have a picture of him, and he is the spitting image of my 
nephew. The men could be brothers, right down to hair and beard style.

In fact, the foreign blood comes in through my maternal grandmother, who 
was English Roman Catholic, as compared to my Protestant Irish maternal 
grandfather.  That grandfather was a sergeant major in the army of the 
Republic of Ireland.  Until he retired and became a publican. I can 
understand my mothers refusal to allow religion discussions at the 
dinner table quite well.

Donald
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-28T11:49:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59fgfcF2kfq6rU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[23 more quoted lines elided]…
> syntax, especially when it comes to properties.

Yes, me too. I hardly use Java these days.

But then, I was never deeply immersed in it. I managed people who were, and 
they could achieve very impressive results with it very quickly.

I am currently grappling with remote web services for my new product web 
site launch, which I really wanted to have up by the end of this month 
(unlikely...). It will be a week or so yet.  Yesterday, I was grizzling 
because the standard web service interface that people see if they link to 
the web service, does not permit testing of the service when it is accessed 
remotely. (If it is connected to a localhost, it does, and I find this very 
useful.) I thought I'd have to knock up a web page in C# just so I could do 
remote testing of the web service. Although it isn't really a big deal, I 
have so many other things to do currently (the site itself, the 
establishment and installation of COBOL for the COM engine, onto the web 
server, finishing the development of the downloadable client that will run 
the web service, and, most importantly, continung my education in C# and 
"Webarama" :-)) Anyway, the man who runs the host I'm using is a very 
experienced .NET/C# guy and he sent me a C# solution in minutes, that does 
exactly what I need and was about 10 lines of code. Every day I learn 
something more...:-)

>
> Our system uses Apache, Struts, and Velocity, along with Java and Oracle. 
…[3 more quoted lines elided]…
>

I like the "simplicity" of C#. I think straightforward is a good word...

>> These days it doesn't happen... :-)
>
> So there's hope for me yet - cool!  (Of course, this will probably be my 
> last "hands in the code" assignment, especially if I make E-7.  That'll 
> put me into management at that point.)

Shhhh!!! Don't tell Doc.... :-)

Pete.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 12)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-27T19:16:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>`
- **In-Reply-To:** `<59fgfcF2kfq6rU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
>> So far, it hadn't happened.  Of course, I'm just starting to get into the 
…[3 more quoted lines elided]…
> Yes, me too. I hardly use Java these days.

I'm actually feeling a bit better about it today - I'm actually 
understanding how its put together.  This project is also my first 
experience with CVS - three of us have been working on pretty much the 
same files for the past two days.  We just just have to make sure we 
update before we commit, so we don't introduce conflicts.

> I am currently grappling with remote web services for my new product web 
[snip]
> Anyway, the man who runs the host I'm using is a very 
> experienced .NET/C# guy and he sent me a C# solution in minutes, that does 
> exactly what I need and was about 10 lines of code. Every day I learn 
> something more...:-)

What did it do?

>> Our system uses Apache, Struts, and Velocity, along with Java and Oracle. 
>> I like the way it's laid out, but there are a lot of different pieces in 
…[3 more quoted lines elided]…
> I like the "simplicity" of C#. I think straightforward is a good word...

Well, it fits nicely.  Model = database or objects, View = ASP.net page, 
Controller = code-behind file.  In our environment, Model = database or 
objects, View = Velocity template, Controller = Struts action.  Of 
course, for each object you've got to have a service, then for each 
template you have to define the fields in the struts config file, the 
the labels are in an ApplicationResources.properties file...  !!!

I guess that's all the stuff that happens behind the scenes when you say 
"AutoEventWireup=true"...  :)

>> So there's hope for me yet - cool!  (Of course, this will probably be my 
>> last "hands in the code" assignment, especially if I make E-7.  That'll 
>> put me into management at that point.)
> 
> Shhhh!!! Don't tell Doc.... :-)

You know he wakes up when someone uses his name...  ;)

The other day, we were talking about something new that the customer 
wanted.  They didn't think we could do it in a month, so I said, "Well, 
is there a central, essential piece that we could build, along with an 
infrastructure that would support the future requirements?"

One of the developers looked at me and said "Man - you sound like a 
project manager!"  (As it turns out, it's not nearly as complex as we 
though, so we can give them the essentials plus an assortment of bells 
and whistles in this first iteration - sweet!)
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-28T10:45:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0v8jn$ink$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net> <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>`

```
In article <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 

[snip]

>>> So there's hope for me yet - cool!  (Of course, this will probably be my 
>>> last "hands in the code" assignment, especially if I make E-7.  That'll 
…[4 more quoted lines elided]…
>You know he wakes up when someone uses his name...  ;)

zzzzZZZZzzzzzz... eh? huh? whuh?  sorry, I was just... considering some 
weighty matters.

(and if you think horrid things happen when you mention *my* name you 
should meet my brood-mate... it's a bit more complicated but the results 
are more spectacular, you just have to darken the room's lights, stand in 
front of a mirror and say her name three times...)

>
>The other day, we were talking about something new that the customer 
…[5 more quoted lines elided]…
>project manager!"

Coming up with a different technical solution is not, in my experience, 
what most project managers do... some, but not most.  If you were allowed 
to then which would you rather do... spend time slinging code or spend 
time allocating, co-ordinating and motivating personnel and resources?

DD
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 14)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-28T09:00:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xP6dnd2veOdf_K7bnZ2dnUVZ_sfinZ2d@comcast.com>`
- **In-Reply-To:** `<f0v8jn$ink$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net> <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com> <f0v8jn$ink$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[17 more quoted lines elided]…
> front of a mirror and say her name three times...)

Heh - I didn't say horrid things happened - just that you woke up.  :) 
Sounds like you have some fun summoning your brood-mate though!

>> The other day, we were talking about something new that the customer 
>> wanted.  They didn't think we could do it in a month, so I said, "Well, 
…[9 more quoted lines elided]…
> time allocating, co-ordinating and motivating personnel and resources?

Slinging code, of course.  :)
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-29T12:21:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59i6ncF2l84kmU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net> <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com> <f0v8jn$ink$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f0v8jn$ink$1@reader2.panix.com...
> In article <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[32 more quoted lines elided]…
> what most project managers do... some, but not most.

Thank you for qualifying this, Doc.

>If you were allowed
> to then which would you rather do... spend time slinging code or spend
> time allocating, co-ordinating and motivating personnel and resources?
>

Sometimes the two choices are not mutually exclusive, and both activities 
have their pros and cons...

I write code because I am driven and obsessed to...:-)  I do management 
because it is a living and, sometimes, there are rewards in it that have 
nothing to do with money. (I enjoy watching myself and others grow...:-))

Pete.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-29T12:14:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59i6a5F2lbf2cU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net> <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message
…[20 more quoted lines elided]…
>

It allows me to test any webservice that is exposed anywhere, even though I 
am not running on that host. (The Web Service template used by VS 2005 
allows this, but only if you are running on the host where the service 
resides. It is really useful and, during development on IIS I came to rely 
on it quite a bit. Once I posted services to a host, I could no longer do 
this and it was a an irritation.) The main Web Service I have written has a 
COBOL COM component at the heart of it, wrapped in C#, and it is reassuring 
to be able to check that the component is running, from a Browser, before 
trying to access the service under program control. Whern I saw his C# code 
I immediately thought "Why didn't I think of that ?!" My experience has been 
that whenever this happens, I learn something... :-)

Here's the code...

using System;
using System.Data;
using System.Configuration;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;

public partial class _Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        AVSProxy.AVSWebService proxy = new AVSProxy.AVSWebService();
        Label2.Text = proxy.ValidateNZaddress(TextBox1.Text);
    }
}

(This is running the "ValidateNZaddress" method of an exposed web service 
called "AVSWebService"; it could be easily modified to run any method of any 
exposed service...)

...and here's the ASPX page it runs from...

<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" 
Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" >
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    <asp:Label ID="Label1" runat="server" Text="Enter Address to 
test:"></asp:Label><br />
        <asp:TextBox ID="TextBox1" runat="server" Height="148px" 
TextMode="MultiLine"
            Width="357px"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="Test" 
OnClick="Button1_Click" />
        <br />
        <br />
        <asp:Label ID="Label2" runat="server" 
Text="Label"></asp:Label></div>
    </form>
</body>
</html>

Obviously, there are a few support objects (like a proxy to my web service) 
generated by VS 2005, but the above is enough to give you the idea.

If anybody reading this has the same problem, I'll gladly forward the 
package by private mail, (but you must include references to your own web 
services (not mine... ;-)) when you build it ).



>>> Our system uses Apache, Struts, and Velocity, along with Java and 
>>> Oracle.

Yes, I remember some of my Java people getting excited about Struts. I'm not 
sure what this is... I'm unfamiliar with Velocity, too.

They also loved AJAX which I have as next on my list :-) (now it is 
available for C#)... I just haven't time to do the education I need to, 
until this web site is published, but after that I expect to relax and 
immerse myself in some of this "new-fangled high tech mumbo-jumbo"... :-)

Funny... I'm so busy doing stuff, I don't have time to learn it... :-)

I'm sure many here have been in that situation...


>>> I like the way it's laid out, but there are a lot of different pieces in 
>>> different places.  I'm beginning to understand MVC, but it seems that C# 
…[12 more quoted lines elided]…
> "AutoEventWireup=true"...  :)

Yep, see code above... :-)

>
>>> So there's hope for me yet - cool!  (Of course, this will probably be my 
…[13 more quoted lines elided]…
> project manager!"

Ah, so this developer is used to Project Managers with a positive, can-do, 
attitude...excellent!


 (As it turns out, it's not nearly as complex as we
> though, so we can give them the essentials plus an assortment of bells and 
> whistles in this first iteration - sweet!)

The first step to becoming legend... deliver more than they expect.

Pete.
```

###### ↳ ↳ ↳ Re: newbie question on cobol syntax

_(reply depth: 14)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-04-29T18:35:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_I2dnWTAr4aPp6jbnZ2dnUVZ_qWvnZ2d@comcast.com>`
- **In-Reply-To:** `<59i6a5F2lbf2cU1@mid.individual.net>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <KySWh.3317$ff2.277@fe08.news.easynews.com> <1hhp23lrbejcmn16429hp0pthh40pmn5fn@4ax.com> <Cm4Xh.9184$9i2.4154@fe06.news.easynews.com> <bklp235d03auknn51jp1rt477h2fhmk6dc@4ax.com> <1177356217.808102.76680@d57g2000hsg.googlegroups.com> <I76dnQUjPPpo9LDbnZ2dnUVZ_sTinZ2d@comcast.com> <1v5s23lhhe18h1crrt2itnbien01635o7c@4ax.com> <_N6dnZOqIvKHN7PbnZ2dnUVZ_vWtnZ2d@comcast.com> <5984nrF2jrmikU1@mid.individual.net> <xpKdnV3cTJn0nq3bnZ2dnUVZ_vKunZ2d@comcast.com> <59fgfcF2kfq6rU1@mid.individual.net> <8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com> <59i6a5F2lbf2cU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:8-qdnQ6YAf0SPa_bnZ2dnUVZ_sWdnZ2d@comcast.com...
…[4 more quoted lines elided]…
> am not running on that host.

[snipped implementation]

Cool.  I'm guessing AVSProxy is a connection to your proxy server?

>>>> Our system uses Apache, Struts, and Velocity, along with Java and 
>>>> Oracle.
> 
> Yes, I remember some of my Java people getting excited about Struts. I'm not 
> sure what this is... I'm unfamiliar with Velocity, too.

(Recognize that all these descriptions are from me as a two-month 
programmer with no formal training...)

Struts allows you to specify "actions" - these are Java classes with an 
"execute" method.  Struts invokes the execute method of the defined 
action, passing the form and it's data as a bean.  It's pretty cool - it 
will even recognize objects (if you defined a checkbox array, for 
example, based on an object) and recreate the ID and value fields.  (It 
doesn't do the full constructor - it basically calls the no argument 
constructor, and then puts the values in.  However, you can take that 
list and easily recreate the objects, presuming they came from a 
persistent data store.)

Velocity strikes me as SSH on speed.  :)  We have lists defined, and 
then in the code, there's something like

<tr>
     <td>
         $ExampleList
     </td>
</tr>

"$ExampleList" is replaced with a select box of "whatever"s.  You can 
also define macros, and I'm sure there's more to it than I've learned so 
far.  We also have "business-functions" (SQL statements, defined in 
several XML files) that are tied to security profiles as well.  I'm not 
sure which technology provides that infrastructure.

> They also loved AJAX which I have as next on my list :-) (now it is 
> available for C#)...

That's kind of a misnomer.  AJAX is available for everything.  :)  The 
AJAX toolkit makes it easy to integrate predefined AJAX functionality 
into .NET applications, but you don't have to use that to do what you 
need to do.  The AJAX toolkit actually implements it using the .NET 
standard "control" syntax (for example, the "accordion" control renders 
those cool sets of <div>s where when you click a heading, all the others 
shrink down and the one you clicked expands).

I haven't actually integrated them into any active code, but I looked at 
them quite a bit a few weeks ago.  :)

> I just haven't time to do the education I need to, 
> until this web site is published, but after that I expect to relax and 
…[4 more quoted lines elided]…
> I'm sure many here have been in that situation...

Tell me about it!  I've started back with college classes; I'm trying to 
learn the stuff at work; my two oldest kids are playing baseball/T-ball; 
I'd like to spend some leisure time with my family.  Where is the .NET 
playtime?  :P

> The first step to becoming legend... deliver more than they expect.

Heh - that would be a hoot.  Especially as inadequate as I'm feeling now 
at times...
```

#### ↳ Re: newbie question on cobol syntax

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-04-23T11:28:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<132pnkegtj8q49b@news.supernews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
Mayer wrote:
> Hello:
>
…[25 more quoted lines elided]…
> recommended.

Same as in English - it marks the end of a thought. It's the difference 
between Hemingway and ee cummigs.

If you don't want the instruction to stop, don't use a period.
```

##### ↳ ↳ Re: newbie question on cobol syntax

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-23T17:02:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0ioqd$krj$1@reader2.panix.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <132pnkegtj8q49b@news.supernews.com>`

```
In article <132pnkegtj8q49b@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>Mayer wrote:

[snip]

>> Can someone please explain to me the function of the period in cobol,
>> what is the basis for the difference in syntax, and what is
>> recommended.
>
>Same as in English - it marks the end of a thought.

This may not, in certain circumstances, be the case; if such a truth held 
universally then this would be two sentences.

[snip]

>If you don't want the instruction to stop, don't use a period. 

Ow... with all due respect, 'instruction', when it comes to computers and 
their languages, might have a slightly different definition that what can 
be seen from your statement.

DD
```

##### ↳ ↳ Re: newbie question on cobol syntax

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-04-23T12:27:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177356478.518277.232700@l77g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<132pnkegtj8q49b@news.supernews.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com> <132pnkegtj8q49b@news.supernews.com>`

```
On Apr 24, 4:28 am, "HeyBub" <heybubNOS...@gmail.com> wrote:
>
> > Can someone please explain to me the function of the period in cobol,
…[3 more quoted lines elided]…
> Same as in English - it marks the end of a thought.

I find that my thoughts often end without the benefit of
```

#### ↳ Re: newbie question on cobol syntax

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-04-23T19:44:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ca6dnbRbI6gbY7HbnZ2dnUVZ8turnZ2d@pipex.net>`
- **In-Reply-To:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`
- **References:** `<1177272149.938765.13260@o5g2000hsb.googlegroups.com>`

```
Top post:

The really significant context of where a full stop/period is 
placed is when it terminates an 'if' clause, by being present:

if a = b
  move xyz to mars.
move threesome to somewhere
(in this example, threesome gets moved to somewhere 
unconditionally; the period/full stop terminates the list of 
actions governed by the 'if'.)

   -- compared with ---

if a = b
  move xyz to mars
move threesome to somewhere.
(in this example, threesome gets moved to somewhere only when a 
= b.)

Similar effects apply when using 'at end' after 'read' and 
other non-if type conditionals.

My preference is to use as few periods/full stops as possible;
as I write in 'sections', that means just one at the end of a 
section (apart from the 'required' places, like after a section 
name.)

The reason for the preference? To avoid false conditional 
terminators (see above).

While we're at it, I don't like paragraphs, heartily dislike 
UPPER case, never use 'exit' or 'go' or 'perform thru', can't 
stand 88-levels and implicit value-assignments like set 
this-is-a-kludge to value true.

Bout it, really. Except for nested ifs ...... I won't go there.

Regards


Michael

Mayer wrote:
> Hello:
> 
…[30 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
