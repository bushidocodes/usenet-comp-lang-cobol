[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cyrillic characters

_8 messages · 3 participants · 2009-10_

---

### Cyrillic characters

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-10-26T14:41:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com>`

```
Some time back I asked for advice on typing Cyrillic characters in a 
PowerCOBOL Text Box. When attempting to do so, the typed characters all got 
entered and changed to "?".

I got some interesting tips, and this post is a follow-up on how to make the 
son-of-a-bitch work.

It wasn't COBOL.

In over 200 hours of tinkering, trying various solutions (including 3rd 
party Text Boxes), and research (the Visual Basic people have the SAME 
problem), it turned out to be a single, piddly, incomprehensible check box 
in Windows XP.

The "Regional & Language Options" of Control Panel has a "Languages" Tab. 
Selecting that tab provides a push button for "Details."

Under "Details" is an opportunity to add additional languages. In our case, 
we added "Russian" as an installed service. That much is pretty obvious, but 
it obviously didn't help matters much, except that it allowed us to TYPE the 
Russian (Cyrillic) characters. These typed characters still got swept away 
as soon as focus was lost on the Text Box into which they were typed.

Here's the trick: On that same screen where you add languages, pick the 
"Advanced" tab. When that tab opens, you'll see two check boxes. The first 
check box is denoted (actual quote)

"Extend support of advanced text services to all programs - Select this 
check box to turn on advanced text services in Notepad and other programs 
that do not normally support speech and handwriting recognition or other 
advanced input services."

THIS IS THE FRIGGIN' BOX THAT NEEDS TO BE CHECKED!

After XP digested this single change to its system (re-boot required), 
EVERYTHING magically started working as we hoped-against-hope it would. No 
changes to our programs, no incantations, no nothing!

We of course have no "speech and handwriting recognition" stuff, so you can 
see why this option was bypassed in all the previous permutations. This is 
about the only case in my entire career where the "change something and see 
if works now" trouble-shooting technique has proved to work.

I don't know whether to stab the cat or raise my glass in celebration.

At least I can get some modicum of satisfaction by sharing.

Use this tip in good health.
```

#### ↳ Re: Cyrillic characters

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-27T11:34:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kmmf5F3a6hvpU1@mid.individual.net>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Some time back I asked for advice on typing Cyrillic characters in a
> PowerCOBOL Text Box. When attempting to do so, the typed characters
…[45 more quoted lines elided]…
> Use this tip in good health.

This is really spooky...:-)

Yesterday I was cleaning up a virtual COBOL machine and found a directory 
called "Cyrillic" where I had done some experiements when you first raised 
this.

I thought to myself, "must contact Jerry and see if he ever resolved 
that..." and today your post appears.

Thanks a lot for posting it. As you say, sharing can enhance the 
satisfaction in solving.

Good job!

Pete.
```

##### ↳ ↳ Re: Cyrillic characters

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-10-26T21:22:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drGdnYBy5KAaxHvXnZ2dnUVZ_vadnZ2d@earthlink.com>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kmmf5F3a6hvpU1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> Some time back I asked for advice on typing Cyrillic characters in a
…[55 more quoted lines elided]…
>

Well, Halloween IS upon us....

We have software installations pending in Azerbijan, Kazakistan, and Moscow, 
so there was some pressure to get this figured out.

We've run through the whole suite and PowerCOBOL is happily indifferent to 
the character set used, whether just plain text, indexes in ISAM files, 
collating sequence, forms and captions, whatever.

Lovely.

And, by the way, thanks for thinking on the problem.
```

###### ↳ ↳ ↳ Re: Cyrillic characters

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-27T16:22:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kn7biF3b6ubdU1@mid.individual.net>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kmmf5F3a6hvpU1@mid.individual.net> <drGdnYBy5KAaxHvXnZ2dnUVZ_vadnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> HeyBub wrote:
…[60 more quoted lines elided]…
> Moscow, so there was some pressure to get this figured out.

Fantastic!
>
> We've run through the whole suite and PowerCOBOL is happily
…[3 more quoted lines elided]…
> Lovely.

I've always had a high opinion of PowerCOBOL and agree it is an excellent 
product.

I have a client who uses it, and modifying Toolset Transformation for him 
was quite an exercise... every scriptlet had to be identified and processed. 
(fortunately they are tagged in the .PRC file... but there is no easy 
automatic way I could find to add them back to the project once they are 
modified. His people do it manually, cutting and pasting them out of the 
Migration Environment and back into the PowerCOBOL project... it is very 
unsatisfactory in my opinion but they don't seem to mind.)

He is moving to Web Based .NET, not because there is anything wrong with 
PowerCOBOL, but he is finding it increasingly difficult to get COBOL 
programmers with knowledge of it and because he believes that moving to C# 
is a better option. (I may have had some nfluence on this...:-))

I'd like to see Fujitsu (Alchemy) make a clear statement on whether it will 
continue to be supported or not, and for how long.

I really like the idea of using COBOL for the interrupt code instead of a 
special scripting language like DIALOG, and PowerCOBOL systems have proven 
to be very robust in production.

Your Eastern European clients are running Windows, or will it be a virtual 
Windows environment? (I heard that Eastern Europe is very fond of Linux... )


 >
> And, by the way, thanks for thinking on the problem.

No problem. Only sorry I never found a solution... :-) (I DID find some very 
useful "stuff"; nothing is ever wasted...:-))

Pete.
```

###### ↳ ↳ ↳ Re: Cyrillic characters

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-27T14:25:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hc6vte$hlb$1@reader1.panix.com>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kmmf5F3a6hvpU1@mid.individual.net> <drGdnYBy5KAaxHvXnZ2dnUVZ_vadnZ2d@earthlink.com> <7kn7biF3b6ubdU1@mid.individual.net>`

```
In article <7kn7biF3b6ubdU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I have a client who uses it, and modifying Toolset Transformation for him 
>was quite an exercise... every scriptlet had to be identified and processed. 
…[4 more quoted lines elided]…
>unsatisfactory in my opinion but they don't seem to mind.)

This is similar to something I ran across the other day.  Awaaaaaayyyy 
back when (2005 or so) I wrote a utility-job using DFSORT to do something 
then derided as 'nice, but not needed'.

A week or so back someone came to my cube... with a copy of that report in 
his hand.  Now it was Very Useful but... he wanted a second report, Just 
Like the First BUT... selecting a sub-set, sorted/broken differently and 
certain data blacked out.

While chatting with him about the request I discovered that he received 
the Original Report via hardcopy... AND THEN RE-TYPED CERTAIN DATA FOR 
CERTAIN GROUPS BY HAND INTO EMAILS TO BE SENT TO... someone in the groups 
to deal with it.

I cringed.  I had been taught, e'er-so-long ago, that 'data are to be 
entered once and only once' (EXCEPT for projects requiring double-entry 
accuracy, where one operator's keying-in was compared to a second's and 
discrepancies down to the typo were researched and clarified before final 
submission).  I toyed with the idea of adding an IEBGENER step to send the 
output of the New Report directly to this fellow...

... and told him I could do it IF and ONLY IF he could give me not a 
'named' email address (john.smith@anycompany.nothere. etc.) but a 
'positional' email address (rejects.teamlead@anycompany. etc).

He looked confused for a moment and I jumped in with the explanation of 
'people come and go but positions remain... you could be hit by a Mac 
truck tomorrow but - more or less - there'll always be a team lead for 
this project team.  *People* should not get regularly-scheduled production 
reports, *positions* should.'

(no, this is not Standard Practise at this site... but it is a lovely 
idea, I'd say)

DD
```

###### ↳ ↳ ↳ Re: Cyrillic characters

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-28T13:38:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kpi55F39f65cU1@mid.individual.net>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kmmf5F3a6hvpU1@mid.individual.net> <drGdnYBy5KAaxHvXnZ2dnUVZ_vadnZ2d@earthlink.com> <7kn7biF3b6ubdU1@mid.individual.net> <hc6vte$hlb$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7kn7biF3b6ubdU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> something then derided as 'nice, but not needed'.

The shortsightedness of non-IT people is often a cause for me grinding my 
teeth... I guess it is understandable. Most jobs people do, they cope with 
the immediate problems and that is enough. For IT people we are trying to 
obviate future effort at the same time as solving the current problem. I'm 
sure most people here have experienced the resistance when the need to 
capture something is not immediately obvious, but you know in your bones it 
will be needed further down the track, even if you can't explain immediately 
how and why.

'Nice, but not needed' is a phrase which most system developers and 
designers have come to dread... I usually combat this by saying: "maybe not 
needed TODAY, but if we do this now it will save a large amount of time and 
effort later and the effort to do it now is minimal." Quite often I lose on 
this one and, invariably, down the track, it becomes necessary and is a lot 
more trouble to retrofit than if we had done it in the first place...
>
> A week or so back someone came to my cube... with a copy of that
…[7 more quoted lines elided]…
> someone in the groups to deal with it.

Aw, Man! Doesn't your heart just go out to them... :-)

>
> I cringed.  I had been taught, e'er-so-long ago, that 'data are to be
…[18 more quoted lines elided]…
> idea, I'd say)

It is a very sensible idea. Places I have worked where they do this 
(particularly in smaller companies) refer to them as "hat" addresses. 
(Somebody must wear the team leader's hat for example. Often in a small 
company, a single person may wear multiple hats. Probably the most common 
hat address is info@anycompany.com).

Pete.
```

###### ↳ ↳ ↳ Re: Cyrillic characters

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-28T14:40:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hc9l5p$mpc$1@reader1.panix.com>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kn7biF3b6ubdU1@mid.individual.net> <hc6vte$hlb$1@reader1.panix.com> <7kpi55F39f65cU1@mid.individual.net>`

```
In article <7kpi55F39f65cU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> This is similar to something I ran across the other day.  Awaaaaaayyyy
>> back when (2005 or so) I wrote a utility-job using DFSORT to do
…[5 more quoted lines elided]…
>obviate future effort at the same time as solving the current problem.

I'm not sure what you intend by an 'IT person', Mr Dashwood, but in my 
experience IT folks are about the same as any others: one in ten has 'The 
Touch' and the other nine are just kind of getting along, praying that 
they don't get found out.

>I'm 
>sure most people here have experienced the resistance when the need to 
>capture something is not immediately obvious, but you know in your bones it 
>will be needed further down the track, even if you can't explain immediately 
>how and why.

In the case at hand it was not even 'the back of my neck told me'.  
Consider: a bunch o' data comes in from Source A.  Another bunch o' data 
that's supposed to match the first, more-or-less, comes in from Source B.  
The two bunches o' data are to be sliced, diced, chopped, prettily 
decorated with herbs (this is a Financial System so I avoided use of 
'garnished') and sent back to Source A for further processing.

Two sets of data from two sources in a Financial System which are supposed 
to match... wouldn't it be nice to see all from A that aren't on B and 
vice-versa?  I've seen/done that at so many other places o'er the decades 
that doing it for my current client was in-my-sleep stuff.

>
>'Nice, but not needed' is a phrase which most system developers and 
…[4 more quoted lines elided]…
>more trouble to retrofit than if we had done it in the first place...

I liken this to a non-IT discipline with which more folks might be 
familiar: 'It is easier to put in the bathrooms when you are building the 
house than it is to put them in after you've taken residence.' (there was 
a six-P alliteration I was taught that began 'Prior Planning Prevents...')

When such things arise in COBOL programs I've picked up the habit of 
coding for them... and then placing a 'D' in column 7 and including

*SOURCE-COMPUTER. IBM-3090 WITH DEBUGGING MODE.
 SOURCE-COMPUTER. IBM-3090.                    

... where it should be.  In this case it was a DFSORT job which I kind of 
slipped into the Production stream... didn't cost much to run, nobody 
noticed the extra stack of paper except for Ops.

I was later notified 'in the hallway' that the 'nice, but not needed' 
person moved into a different job-position her replacement almost 
immediately asked if such a thing could be done.

[snip]

>> While chatting with him about the request I discovered that he
>> received the Original Report via hardcopy... AND THEN RE-TYPED
…[3 more quoted lines elided]…
>Aw, Man! Doesn't your heart just go out to them... :-)

Not really... but that may be a sign that I am not easily moved by folks 
who court keying-errors so freely.  They seem not to know that the 
keypunch-girls are very busy and that costs are so high I'm allowed only 
two compiles per day (three if I can come in at night and hang out with 
the Ops crew)... and don't get me started on what they're callin' 'music', 
neither... buncha durned *noise*, 'f'ya ask me.

[snip]

>> He looked confused for a moment and I jumped in with the explanation
>> of 'people come and go but positions remain... you could be hit by a
…[8 more quoted lines elided]…
>(particularly in smaller companies) refer to them as "hat" addresses. 

A lovely bit of terminology and one that I might appropriate in future; 
since you source the quote imprecisely ('(p)laces I have worked where they 
do this') I will follow suit and say 'At some places these are called 
'hat' addresses (etc)').

DD
```

###### ↳ ↳ ↳ Re: Cyrillic characters

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-10-28T11:31:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P6ednaaY7KpP7HXXnZ2dnUVZ_tGdnZ2d@earthlink.com>`
- **References:** `<75udnT8ptv3-ZnjXnZ2dnUVZ_jOdnZ2d@earthlink.com> <7kmmf5F3a6hvpU1@mid.individual.net> <drGdnYBy5KAaxHvXnZ2dnUVZ_vadnZ2d@earthlink.com> <7kn7biF3b6ubdU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Your Eastern European clients are running Windows, or will it be a
> virtual Windows environment? (I heard that Eastern Europe is very
> fond of Linux... )
>

Real Windows. There are, I think, two reasons:

1. Linux is much like the Celtic warriors hired by English kings of old as 
mercenary warriors: They did a few things and did them well, there were 
(relatively) cheap, and they were completely incomprehensible. You just 
didn't want them, you know, to actually RUN things.

2. The difference in price between Windows and Linux in Central Asia (not 
Eastern Europe) is nil.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
