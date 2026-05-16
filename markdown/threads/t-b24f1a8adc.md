[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# as the case may be

_33 messages · 14 participants · 2009-03_

---

### as the case may be

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-03-05T16:11:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49AFF9C5.6F0F.0085.0@efirstbank.com>`

```
ISPF in z/OS, or at least how we have it set up, automatically does 'CAPS
ON' if you choose to edit a member that has no lower case in it.  On the
other hand it does 'CAPS OFF' if it does have lower case.  This causes data
entered in lower case in these programs to remain in lower case, where the
programmers here are used to it being automatically converted to upper
case.

Number one, is there a way to turn this 'feature' off?

Number two, should we turn it off?

As we migrate from VSE to z/OS I am almost thinking that we should convert
our ALL CAPS source code to all lower case.  Well, except for data within
quotes.  I find all lowercase much more pleasant to look at.

But not everyone agrees.  What do other shops do?

Frank
```

#### ↳ Re: as the case may be

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-03-05T17:43:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z9qdnfHbCqYc_i3UnZ2dnUVZ_vGdnZ2d@earthlink.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
> ISPF in z/OS, or at least how we have it set up, automatically does
> 'CAPS ON' if you choose to edit a member that has no lower case in
…[15 more quoted lines elided]…
>

Be very reluctant to cast aside the traditions of your forefathers. The 
ancients were closer to the revealed truths during the beginning times.
```

#### ↳ Re: as the case may be

- **From:** Joel C Ewing <jREMOVEcCAPSewing@acm.org>
- **Date:** 2009-03-14T13:46:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SXSul.120971$fM1.68482@newsfe14.iad>`
- **In-Reply-To:** `<49AFF9C5.6F0F.0085.0@efirstbank.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com>`

```
If one is going to insist on mono-case, for a given font size all caps 
is much easier for my old eyes to read than all lower case.  I don't 
perceive text that is all "whispering" any more aesthetically pleasing 
than text that is all "shouting".

Whether you do mono case or mixed case should depend on the context. 
For contexts where conventional use of capitalization is expected 
(documentation, or other text intended to be read by humans) there is 
usually no excuse these days for not using correct mixed case 
conventions.  Even with programming languages that are for the most part 
case-insensitive, installation conventions can choose to use selective 
capitalization to make it easier to visually distinguish constants, 
variables, keywords, etc.; and I am convinced that consistent use of 
such visual assists makes it easier for others to follow the code.  I 
would very much discourage a one-solution-fits-all approach.

ISPF provides a number of mechanisms for encouraging edit conventions. 
The principal mechanism is the edit profile, based on the Low-Level 
Qualifier of the dataset name (and whether the DS is FB or VB format). 
It greatly simplifies things in ISPF if you use a consistent and limited 
number of LLQ names for datasets which should have the same editing 
conventions.  For things that can't be done easily with the profiles 
alone, we also have a REXX Site Edit Macro, which is invoked with each 
edit initiation and which can do such things as use the DSN LLQ to 
determine if it would be appropriate to issue edit commands under the 
covers to override user edit profile values or other editor assumed 
defaults.

By the combination of setting up some standard "locked" installation 
default edit profiles and setting up a site macro, it is possible to 
steer users to the desired conventions; but users can still deliberately 
override those conventions if it conflicts with their requirements.

Frank Swarbrick wrote:
> ISPF in z/OS, or at least how we have it set up, automatically does 'CAPS
> ON' if you choose to edit a member that has no lower case in it.  On the
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: as the case may be

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2009-03-14T12:46:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad>`

```
On 14 Mar, 18:46, Joel C Ewing <jREMOVEcCAPSew...@acm.org> wrote:
> If one is going to insist on mono-case, for a given font size all caps
> is much easier for my old eyes to read than all lower case.  I don't
…[51 more quoted lines elided]…
>

I like it! What sort of being is it that reads program code in caps if
not humans?
```

###### ↳ ↳ ↳ Re: as the case may be

- **From:** Joel C Ewing <jREMOVEcCAPSewing@acm.org>
- **Date:** 2009-03-14T15:58:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%TUul.50873$Tp5.19525@newsfe13.iad>`
- **In-Reply-To:** `<7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com>`

```
Robert Jones wrote:
> On 14 Mar, 18:46, Joel C Ewing <jREMOVEcCAPSew...@acm.org> wrote:
>> If one is going to insist on mono-case, for a given font size all caps
…[49 more quoted lines elided]…
> not humans?

Programmers, of course, a breed unto ourselves! :)

Stuff that could potentially be read by end-user humans must adhere to 
higher aesthetic and clarity standards than that which will only be 
viewed by gurus with enhanced interpretive skills.  :)

In an ideal world I would like to see more programming conventions to 
use mixed case in meaningful and consistent ways, even in COBOL; but 
when we have 10,000+ existing COBOL programs plus additional copybooks 
in mono case, who is going to foot the bill for case-enhancing existing 
code when there is no syntactic or functional requirement to force it? 
There goes consistency, which would unfortunately make things more 
confusing rather than less if we tried to switch at this stage in the 
game.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-16T16:06:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpltf3$ejb$2@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad>`

```
In article <%TUul.50873$Tp5.19525@newsfe13.iad>,
Joel C Ewing  <jREMOVEcCAPSewing@acm.org> wrote:
>Robert Jones wrote:
>> On 14 Mar, 18:46, Joel C Ewing <jREMOVEcCAPSew...@acm.org> wrote:

[snip]

>>> Frank Swarbrick wrote:
>>>> ISPF in z/OS, or at least how we have it set up, automatically does 'CAPS
…[17 more quoted lines elided]…
>Programmers, of course, a breed unto ourselves! :)

And machines... I've seen much head-scratching result from folks who tried 
to code JCL in mixed case.

DD
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-16T12:26:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpm44702qqa@news6.newsguy.com>`
- **In-Reply-To:** `<gpltf3$ejb$2@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <%TUul.50873$Tp5.19525@newsfe13.iad>,
> Joel C Ewing  <jREMOVEcCAPSewing@acm.org> wrote:
…[7 more quoted lines elided]…
> to code JCL in mixed case.

Indeed. Programmers often forget about the human audience for their
code, but sometimes they forget about the machine audience.

Just last Wednesday I gave a presentation on the readability of code,
and treating coding as technical writing, at the annual conference of
the Association of Teachers of Technical Writing. My focus was
primarily on mixing information for those two audiences (human and
machine), though, and I didn't have time to take up visual-design
issues like letter case.

(If anyone's curious, you can see a PDF of the slides and my speaker
notes at http://ideoplast.org/code/index.html.)

If I had to guess, I'd hypothesize that more practitioners would show
best comprehension (fewer errors, faster reading time, or both) with
mixed case - because then case can serve as an additional channel. I'd
expect lower case to outperform upper case, because there's more
variety of letter form in lower case (thanks mostly to ascenders and
descenders), especially when using monospace fonts. More-varied letter
forms make it easier for the eye to track within the line of text.

But I don't know offhand of any empirical studies that have tested
that. There probably are some, but I don't have 'em handy.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-16T18:20:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpm59i$qv9$1@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com>`

```
In article <gpm44702qqa@news6.newsguy.com>,
Michael Wojcik  <mwojcik@newsguy.com> wrote:
>docdwarf@panix.com wrote:
>> In article <%TUul.50873$Tp5.19525@newsfe13.iad>,
…[11 more quoted lines elided]…
>code, but sometimes they forget about the machine audience.

Mustn't forget the Eternal Balance between Maintainability and Elegance... 
with today's machines Speed isn't as much of a factor.

[snip]

>If I had to guess, I'd hypothesize that more practitioners would show
>best comprehension (fewer errors, faster reading time, or both) with
…[4 more quoted lines elided]…
>forms make it easier for the eye to track within the line of text.

If I had to guess... I'd say 'depends on what the individual is accustomed 
to'.

DD
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 7)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-17T12:45:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sl_vl.42300$eT1.37513@newsfe20.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com>`

```
Hear, hear.  I'd suggest that once a person is aware of the reserved words
for the language that there's very little to be gained.  Me, I'd prefer
unmixed case, lower or upper, but that's what Im used to.

PL


<docdwarf@panix.com> wrote in message news:gpm59i$qv9$1@reader1.panix.com...
> In article <gpm44702qqa@news6.newsguy.com>,
> Michael Wojcik  <mwojcik@newsguy.com> wrote:
…[5 more quoted lines elided]…
> >>>> I like it! What sort of being is it that reads program code in caps
if
> >>>> not humans?
> >>> Programmers, of course, a breed unto ourselves! :)
> >>
> >> And machines... I've seen much head-scratching result from folks who
tried
> >> to code JCL in mixed case.
> >
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 8)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-19T11:55:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gptsed0e4e@news3.newsguy.com>`
- **In-Reply-To:** `<sl_vl.42300$eT1.37513@newsfe20.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad>`

```
tlmfru wrote:
> Hear, hear.  I'd suggest that once a person is aware of the reserved words
> for the language that there's very little to be gained.  Me, I'd prefer
> unmixed case, lower or upper, but that's what Im used to.

I'll note only that empirical studies of readability often produce
results that contradict readers' common-sense assumptions about their
own reading practices. In short, what you expect may well not be the
case, and what you prefer may not be optimal.

Of course, that doesn't mean your preference is "wrong" - just that
you may prefer something that's not optimal for reading speed and/or
accuracy. We choose to compromise reading speed, ease, and accuracy
all the time for a variety of reasons.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-19T17:07:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gptu3t$ljv$2@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com>`

```
In article <gptsed0e4e@news3.newsguy.com>,
Michael Wojcik  <mwojcik@newsguy.com> wrote:

[snip]

>We choose to compromise reading speed, ease, and accuracy
>all the time for a variety of reasons.

It sounds remarkably similar to the compromise, writing code, for speed of 
execution, ease of maintenance and accuracy of output... and lo, Man hath 
made Machines in His own image.

DD
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-20T08:36:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72fl5gFpfvsqU1@mid.individual.net>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com> <gptu3t$ljv$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <gptsed0e4e@news3.newsguy.com>,
> Michael Wojcik  <mwojcik@newsguy.com> wrote:
…[8 more quoted lines elided]…
> lo, Man hath made Machines in His own image.

My notebook is much better looking than I am... :-)

Pete
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-20T13:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq041i$7io$1@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <gptsed0e4e@news3.newsguy.com> <gptu3t$ljv$2@reader1.panix.com> <72fl5gFpfvsqU1@mid.individual.net>`

```
In article <72fl5gFpfvsqU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <gptsed0e4e@news3.newsguy.com>,
…[11 more quoted lines elided]…
>My notebook is much better looking than I am... :-)

Not having seen either I cannot generate an informed conclusion, 
concurring or disagreeing... but I was doing a bit of musing regarding the 
difference between 'Overman' and 'Superman' as translations of 
'Uebermensch' that you might find interesting.

Both have, as their base, a derivation from the same Ancient Greek word 
'huper'.  Since Ancient Greek did not have a letter representing the 'h' 
sound it was indicated by an accent-mark indicating they are to be 
'aspirated' (exhaled, 'huuuhhhh'd before pronouncing); the word is 
rendered as (aspirated-upsilon)-pi-episilon-rho and pronounced (as is 
taught nowadays) as 'huper' (HOO-pehr).

Upsilon has two forms, upper- and lower-case; uppercase looks like a 
modern 'Y' and lowercase like a 'u'.  A consonant-shift in the aspiration 
and use of the uppercase form brought this word into Latin as 'super'; 
retaining the aspiration and using the uppercase form is found, still, in 
the modifying prefix of 'hyper'... but that's a bit of trivia.

'Huper' also worked its way northward, dropping its aspiration but gaining 
a consonant-shift, into the German 'ueber'... which is the predecessor of 
the Old English 'ofer', whence is derived 'over'.

So... hyper, super, ueber, over... all from the same, yet all different.

DD
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-21T10:02:18+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72ieisFq73e2U1@mid.individual.net>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <gptsed0e4e@news3.newsguy.com> <gptu3t$ljv$2@reader1.panix.com> <72fl5gFpfvsqU1@mid.individual.net> <gq041i$7io$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <72fl5gFpfvsqU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[41 more quoted lines elided]…
> DD
Fascinating. Thanks for that.

I think that, for me, anyway, I try not to be too literal when translating 
between languages.  Tools like Babelfish are really excellent insofar as 
they allow us to at least get insight into what someone is trying to say in 
a language we are not familiar with. But they don't convey the true nuances 
and rich background of the meaning. Language, as an expression of thought, 
has subtleties that are cultural and sometimes regional. Mechanical 
translation rarely picks that up.

Sometimes when you learn a new language it has words which translate to 
something in your own language, but after using the new language for a while 
you realise that the literal translation is not adequate, and it doesn't 
mean what you thought it did.

(The Sicilian villain in "The Princess Bride" keeps saying 
"Inconceivable".Finally, Inigo, the Spaniard says to him:"You keep using 
that word. I do no think it means what you think it means...") [BTW, if any 
of you haven't seen this try and rent it on video... It is a beautifully 
written and delightful story that people of all ages can enjoy and 
appreciate at different levels. The music is by Mark Knopfler of "Dire 
Straits" and it has some hauntng melodies in it.]

An example from German could be "schadenfreude". "schaden" to damage, 
"freude" joy  so, literally:" Joy at damage" A close English approximation 
could be "glee" or "gleeful" but the true meaning requires a full phrase in 
English to convey the subtleties and overtones: "revelling in another's 
misfortune."

The case in point is about how we should translate "Uebermensch". 
Literally, "Overman" is fine and it certainly conveys the idea. But for me, 
it is just too literal. The idea, (I believe; I am no expert on 
Nietzsche...) is the extension of Human power beyond where it is normally 
at, not with the idea of "lording it over" others, but to become the 
ultimate human possible. (A human in this state has rendered God redundant; 
hence God being "killed" by Humanity. It is as if God were a "collateral 
damage" casualty of the inexorable human struggle for growth... I really 
like this idea.) In this context, I think "Superman" is a more apt 
translation.

However, I would agree it is a matter of opinion and mine is not well 
informed on the subject.

Nevertheless, I did enjoy "Also sprach Zarathrustra" and I'll never be able 
to watch "2001 - A Space Odyssey" in quite the same way again... :-)

Thanks for the interesting and erudite background on the prefix, Doc.

Pete.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-23T23:57:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq97m4$inl$1@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <72fl5gFpfvsqU1@mid.individual.net> <gq041i$7io$1@reader1.panix.com> <72ieisFq73e2U1@mid.individual.net>`

```
In article <72ieisFq73e2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Both have, as their base, a derivation from the same Ancient Greek
>> word 'huper'.

[snip]

>Fascinating. Thanks for that.

T'warn't nothin'... you'se jes' easily pleased, that's all.

[snip]

>Thanks for the interesting and erudite background on the prefix, Doc.

You're quite welcome, Mr Dashwood.

DD
```

###### ↳ ↳ ↳ [OT] "super" (was: as the case may be

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-03-20T16:28:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3UTwl.9204$5Z3.5275@en-nntp-05.dc1.easynews.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <gptsed0e4e@news3.newsguy.com> <gptu3t$ljv$2@reader1.panix.com> <72fl5gFpfvsqU1@mid.individual.net> <gq041i$7io$1@reader1.panix.com>`

```
Doc,
  Mostly, I found this interesting and (mostly) agree.  I was a little concerned 
by the statement,

"A consonant-shift in the aspiration  and use of the uppercase form brought this 
word into Latin as 'super';  ..."

There are certainly MANY cases of things coming directly from  Greek to Latin, 
but I questioned this one.  I have done some internet searching, and I *think* 
that I am correct in concluding that the Greek and Latin "forms" both came from 
a common Indo-European root - but that the Latin did NOT come from the Greek. 
See (for example),

http://www.etymonline.com/index.php?term=super-

which lists a number of PIE (Proto-Indio European) derived forms for this.

You may not have been "implying" a direct borrowing (movement) from Greek to 
Latin, but I did want to express my opinion on this specific topic.

NOTE:  I was searching for a general constant "shift" rule for a PIE consonant 
to Greek aspirated Ypsilon and Latin initial S, but couldn't find one.  I would 
actually be interested if anyone can find information on this.
```

###### ↳ ↳ ↳ Re: [OT] "super" (was: as the case may be

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-24T00:16:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq98od$slt$1@reader1.panix.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <72fl5gFpfvsqU1@mid.individual.net> <gq041i$7io$1@reader1.panix.com> <3UTwl.9204$5Z3.5275@en-nntp-05.dc1.easynews.com>`

```
In article <3UTwl.9204$5Z3.5275@en-nntp-05.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Doc,
>  Mostly, I found this interesting and (mostly) agree.  I was a little
…[8 more quoted lines elided]…
>but I questioned this one.

Only this one?  I'm doing well... as for moving from one language to 
another, in the words of my Junior-year French professor - may he sleep 
with the angels! - a lapsed Greek Orthodox monk with a degree (MA, I 
recall... but that might have been Nietzsche, Mr Venable (my professor) 
might have had his doctorate) and a bit of an ephebephile, 'When it comes 
to words going from one language to another just remember... any vowel 
can, quite often, become any other vowel and any consonant become any 
other consonant'.

(I've found this to be *almost* the case... types of sounds (surrants, 
dental fricatives, labials, etc.) tend to be kind of close... but at other 
times... anything becomes anything else.)

>I have done some internet searching, and I *think* 
>that I am correct in concluding that the Greek and Latin "forms" both came from 
…[5 more quoted lines elided]…
>which lists a number of PIE (Proto-Indio European) derived forms for this.

I don't do this much... so I blew the dust off my OED Compact Edition 
(20th printing, US, 1981) and found on page 3157, pg 156, col 3, second 
complete entry (one carrying over from column 2, then another, then the 
one to which I refer)... in parenthesis, the exact same wording as found 
as given on the text from the URL above.  It seems that the OED compilers 
must have had web-access.

>
>You may not have been "implying" a direct borrowing (movement) from Greek to 
>Latin, but I did want to express my opinion on this specific topic.

E'en amongst The Experts there are disagreements on such matters, Mr 
Klein... and 'Vass you dere, Charlie?' won't do for my response.  If the 
OED does not say there is descent - 
http://www.merriam-webster.com/dictionary/over does not say 'from', but 
'akin' - then I sit, corrected.

>
>NOTE:  I was searching for a general constant "shift" rule for a PIE consonant 
>to Greek aspirated Ypsilon and Latin initial S, but couldn't find one.  I would 
>actually be interested if anyone can find information on this.

I don't think breath-holding would be advisable, Mr Klein... thanks much.

DD
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 9)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-19T12:14:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4vwl.125100$EO2.119770@newsfe04.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com>`

```

Michael Wojcik <mwojcik@newsguy.com> wrote in message
news:gptsed0e4e@news3.newsguy.com...
> tlmfru wrote:
> > Hear, hear.  I'd suggest that once a person is aware of the reserved
words
> > for the language that there's very little to be gained.  Me, I'd prefer
> > unmixed case, lower or upper, but that's what Im used to.
…[11 more quoted lines elided]…
> --


Quite so, no argument.  But "optimal" for any given person depends upon what
s/he's most used to reading - presumably literature, news, etc., in his or
her own language.  The obvious example is English vs. German - German
capitalizes all nouns (correct me if necessary on that) whereas English does
so much more sparingly - names, mostly.  Imagine your last paragraph being
written in pseudo-German style:

> Of course, That doesn't mean your Preference is "wrong" - just that
> You may prefer Something that's not optimal for Reading Speed and/or
> Accuracy. We choose to compromise Reading Speed, Ease, and Accuracy
> all the time for a Variety of Reasons.

For readers not used to it, the capital letters seem to imply extra
importance to the words - extra emphasis - which is certainly going to make
them slow up and blink at least occasionally; also that words are usually
capitalized in English at the beginning of the sentence might cause slight
problems.  I agree that with enough experience a person can become equally
fluent with programs written mixed-case following definite rules.  I suppose
the concept  "optimal" must include a time dimension as well.

From this it "follows" that unmixed case is optimal for me since I am most
used to reading English, and unmixed case is the closest to English style
(n.b., talking only of speed here).  You could argue that this means I ought
to capitalize all data names but I'll fall back on my comment about reserved
words.

PL
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 10)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-20T12:10:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq0kv80i78@news4.newsguy.com>`
- **In-Reply-To:** `<c4vwl.125100$EO2.119770@newsfe04.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com> <c4vwl.125100$EO2.119770@newsfe04.iad>`

```
tlmfru wrote:
> Michael Wojcik <mwojcik@newsguy.com> wrote in message
> news:gptsed0e4e@news3.newsguy.com...
…[7 more quoted lines elided]…
> s/he's most used to reading

That's a common assumption, but it's contradicted by the best
available evidence - empirical studies that use a variety of methods
to gauge reading success in terms of speed, accuracy, comprehension,
and effort. (Those methods range from timing and testing readers to
tracking their eye movements with various kinds of equipment, and
these days some researchers are even moving into using fNMRI analysis
of brain activity while people read.)

For example, people who read mostly magazines and newspapers are
generally most used to reading prose in narrow columns; but even those
readers have shown performance improvements with longer line lengths.

Until relatively recently, German newspapers were typically set in
Blackletter or a similar typeface. When they finally moved to a more
modern typeface, even long-time readers (who were used to reading text
set in Blackletter) found them easier to read.

> From this it "follows" that unmixed case is optimal for me since I am most
> used to reading English, and unmixed case is the closest to English style
> (n.b., talking only of speed here).

But English is my primary language as well, and I find mixed case more
readable than either monocase option. So other literacies can't have
that simple a relationship to source-code literacy.

This is just another example of the phenomenological gulf - we don't
actually know all that much about how we do what we do, and we don't
know that much about how much we don't know, and we often don't even
know we don't know it.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-21T10:06:34+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72ieqsFbgaciU1@mid.individual.net>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com> <c4vwl.125100$EO2.119770@newsfe04.iad> <gq0kv80i78@news4.newsguy.com>`

```
Michael Wojcik wrote:
> tlmfru wrote:
>> Michael Wojcik <mwojcik@newsguy.com> wrote in message
…[38 more quoted lines elided]…
> know we don't know it.

" I don't know..."
"What don't you know?"
"If I knew what I don't know then I couldn't not know it, could I?"
"I don't know..."

Pete.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 11)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-21T12:13:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qf9xl.992$HF6.941@newsfe08.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com> <c4vwl.125100$EO2.119770@newsfe04.iad> <gq0kv80i78@news4.newsguy.com>`

```
Very interesting!

Do any of these studies go into sentence length?  Or paragraph lengths?  It
drives me bonkers to have to read so much that is in
one-sentence-per-paragraph style; even moreso when it's 17 words or less per
sentence.  (I have lots of complaints about all these writing guides that
propound grade 6 rules).

Now here's a "theory" about reading speed & comprehension which I came up
with 10 minutes ago.  To wit:

- in any given font, upper-case letters are larger than lower-case.  (Are
there exceptions?)
- bigger letters are easier to read than smaller ones.
- THEREFORE, ALL WRITING SHOULD BE DONE IN UPPER-CASE BECAUSE IT'S EASIER TO
READ.

(Apologies to all of you who aren't aflicted with no-longer-youthful
eyesight!)

PL

Michael Wojcik <mwojcik@newsguy.com> wrote in message
news:gq0kv80i78@news4.newsguy.com...
> tlmfru wrote:
> > Michael Wojcik <mwojcik@newsguy.com> wrote in message
…[10 more quoted lines elided]…
> Rhetoric & Writing, Michigan State University
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 12)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-23T12:13:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gq8gc702c5l@news1.newsguy.com>`
- **In-Reply-To:** `<qf9xl.992$HF6.941@newsfe08.iad>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <gpm59i$qv9$1@reader1.panix.com> <sl_vl.42300$eT1.37513@newsfe20.iad> <gptsed0e4e@news3.newsguy.com> <c4vwl.125100$EO2.119770@newsfe04.iad> <gq0kv80i78@news4.newsguy.com> <qf9xl.992$HF6.941@newsfe08.iad>`

```
tlmfru wrote:
> 
> Do any of these studies go into sentence length?  Or paragraph lengths?

I imagine there are a number that do, though I can't cite any off the
top of my head. In the '40s and '50s, there were a lot of articles
that made recommendations about sentence length and such, but I'm not
sure how many of those were based on empirical data. (And I think eye
tracking studies came along later.)

Google Scholar found some interesting hits in ACM Journal of Computer
Documentation, but I'm not a SIGDOC member (at the moment - I probably
ought to join) so I can't read them at home. I'd have to be at school.

> It
> drives me bonkers to have to read so much that is in
> one-sentence-per-paragraph style; even moreso when it's 17 words or less per
> sentence.  (I have lots of complaints about all these writing guides that
> propound grade 6 rules).

Agreed. I'm dubious about style guides in general; they rarely seem to
be based on much more than the author's preferences, and even those
are often unexamined. (Richard Ohman did a great critique of the
Strunk and White commandment to "use concrete, specific language".)

> Now here's a "theory" about reading speed & comprehension which I came up
> with 10 minutes ago.  To wit:
> 
> - in any given font, upper-case letters are larger than lower-case.  (Are
> there exceptions?)

There are so many typefaces that you can find an exception to pretty
much any rule. Algerian, for example, has basically only one letter
height - but that's because it has essentially the same letterforms
for both cases. For some typefaces, such as Tunga, the difference in
letter height for the two cases is negligible. I don't think I have a
typeface installed on this machine that has lower-case letters that
are larger than upper-case ones, but it wouldn't surprise me if there
was one, especially among the "fantasy" typefaces (such as "graffiti"
fonts).

> - bigger letters are easier to read than smaller ones.

Are they? I just set the default font size in my browser to 72-point,
and it was pretty hard to read, mostly because very little text was
actually visible in the viewport.

True, the individual letters were still pretty visible. I bet that if
I set the x-height to, say, 1 mile, though, they would be tough to
read. At least until I get that really big monitor. (And then I'll
have to sit too far from the keyboard...)

> - THEREFORE, ALL WRITING SHOULD BE DONE IN UPPER-CASE BECAUSE IT'S EASIER TO
> READ.

Sure, all else being equal. But of course it isn't, so that doesn't
follow. :-)

I suspect - but have no data to support - that a majority of English
readers would find either mixed-case or all-lowercase easier to read
than all-uppercase, in the same typeface at the same letter height
(excluding bizarre fantasy typefaces).

I'm hypothesizing that based solely on the greater variety of
letterforms in lower- and mixed-case text; most typefaces have less
variety of form in uppercase, because uppercase letters tend to all be
the same height (while lowercase offer ascenders and descenders), have
less variation in width, have fewer opportunities for kerning, and
have fewer curves (contrast A and E with a and e, for example). Less
variety means fewer visual cues for letter recognition, maintaining
position on the line, etc.

But I could well be wrong. And there are different dimensions to
readability; readers might find all uppercase slower going, but have
improved accuracy or retention, for example (perhaps because the
unfamiliarity of all-uppercase prevented them from making as many
assumptions about the text).

And, of course, this could differ for other languages. Japanese
doesn't have case, but I wonder if anyone's compared readability of
hiragana and katakana.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-16T12:31:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<im6tr4hmf04jb1trvkkk29u982me136em2@4ax.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com>`

```
I've edited some JCL with mixed case comments in it - forgetting that
it doesn't update my JCL commands.   
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-17T15:06:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<728etmFodgjdU1@mid.individual.net>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com>`

```
Michael Wojcik wrote:
> docdwarf@panix.com wrote:
>> In article <%TUul.50873$Tp5.19525@newsfe13.iad>,
…[22 more quoted lines elided]…
>

Interesting and enjoyable. Thanks for the link.

While I wouldn't argue with what you said, it hinges on a single 
supposition: That what is written will be read.

That raises 2 further considerations:

1. What if people don't WANT to read it (can't be bothered... struggle with 
language anyway... etc...)?

As I am sure you are aware, there is a huge diversity in the way that Humans 
learn. Some people really struggle with language, but can look at intricate 
computer code and visualise it in an instant. Others (like me...) prefer to 
have a verbal description before getting down to nitty gritty.

2. What if there is never any NEED to read it?

I have some components which have not been maintained for over 10 years and 
are never likely to be. I don't get out the source code and read it for the 
entertainment value :-). There is an argument that says encapsulated 
functionality can be "write only"... (I have heard some uninformed people 
describe C as a "write only " language... don't even think about trying to 
decipher it in a year's time; just write the modified function again...)

(From personal experience, the very first C program I ever wrote that dealt 
with recursion over directory structures, was something I was quite proud of 
. I spent several days studying and testing until it worked. I was amazed at 
how few lines of code (compared to the COBOL  I was normally using) it took. 
It was very powerful with nested functionality within single statements. 18 
months later I needed to extend it and it was just a mystery. I spent half a 
day trying to figure out what it did and how it did it, then simply rewrote 
it... The experience made me think.)

In a COBOL environment where the source code is sacrosanct and large chunks 
of it must be maintained regularly, this idea seems to be Heresy. But I 
don't think it is. If the granularity of the system architecture is very 
small, encapsulated (pieces/units/bits of code/component methods/modules... 
or what have you), then it may indeed be quicker to simply rewrite without 
consulting the existing code. It might even be "desirable" if you don't want 
the previous approach to influence the new one...

Even if you DO consult the existing code, if it is small, it probably 
doesn't matter too much how "readable" it is.

I think the "rule" you quoted about having each idea on a single page is 
excellent. (Hadn't seen that before...). Certainly, I know that in C# the 
smaller and "tighter" the code, the easier it is to assimilate what it does 
quickly when uder pressure. I never thought I'd say this, but I DO find 
COBOL verbose now... It's like when someone is talking and you wish they'd 
get to the point.

> If I had to guess, I'd hypothesize that more practitioners would show
> best comprehension (fewer errors, faster reading time, or both) with
…[5 more quoted lines elided]…
>

I don't have any metrics for this either, but I "feel" it is probably 
true...

> But I don't know offhand of any empirical studies that have tested
> that. There probably are some, but I don't have 'em handy.

I noticed that APL was markedly missing from your discussion. I have seen 
people who are fluent in this do absolutely amazing things with a few 
seconds of typing. (I saw a demo done for my benefit where something that 
would have taken at least 500 lnes of COBOL required less than half a dozen 
lines in APL) However, what they write might as well be Swahili... I 
discussed this with a guy in Madrid who I am quite sure used to think in 
APL. He said he had always liked symbols and just had a natural flair for 
APL. (The point I mentioned above about different people having different 
affinities and facility across different learning channels.) He had no 
problem manipulating apparently abstract symbols, rather than words. I read 
an interview with Stephen Hawking where he said he visualises the problems 
he is dealing with using images and symbols and THEN "translates" the 
solution into standard math notation. In other words, he doesn't "think" in 
math...

The conclusions I would draw are as follows:

1. Programming (at least in most of the commonly used languages) IS 
technical writing. However, there may be some exclusions to this. (APL may 
be one...)
2. It is desirable to do what we can to make program code easily 
intelligible, WHETHER WE ARE LIKELY TO MAINTAIN IT OR NOT! BUT...  not at 
the expense of large amounts of writing that just add to the verbosity. 
There are "break even" points. Deciding what they are is part of the "Art" 
of computer programming; difficult to quantify.
3. Don't use APL. It is "dangerous" in every sense of the word... :-)

Pete.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-17T13:45:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gponjj21bol@news7.newsguy.com>`
- **In-Reply-To:** `<728etmFodgjdU1@mid.individual.net>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>>
…[4 more quoted lines elided]…
> Interesting and enjoyable. Thanks for the link.

Thanks. It was a fun presentation to write and deliver.

> While I wouldn't argue with what you said, it hinges on a single 
> supposition: That what is written will be read.

Yes, though I do talk a bit at the end about the economic drivers,
which are described in terms of the probability that code will be
read. It's true that not all code is read, but the available evidence
suggests that enough will to be worthwhile.

> 1. What if people don't WANT to read it (can't be bothered... struggle with 
> language anyway... etc...)?

Often a problem. Of course, sometimes there is no good alternative -
reading the code may be the only practical way of retrieving certain
information (eg about business rules that aren't well-documented, or
to do forensic analysis on a problem incident).

> 2. What if there is never any NEED to read it?

And yes, this comes up sometimes too. Of course, a component that's in
use and doesn't need to be maintained for 10 years might be worth
reading as an exemplar.

[snip some good examples of cases where reading the code might not be
necessary or desirable]

> I noticed that APL was markedly missing from your discussion.

Too far in the wrong direction.

I've done a bit of programming in APL, just to see what it was like. I
tend to agree with Djikstra: it encourages clever obscurantism. Dense
function composition, obscure symbolic tokens, right-to-left binding,
and so forth are actively hostile to human readers.

> I have seen
> people who are fluent in this do absolutely amazing things with a few 
> seconds of typing. (I saw a demo done for my benefit where something that 
> would have taken at least 500 lnes of COBOL required less than half a dozen 
> lines in APL) However, what they write might as well be Swahili...

Yes. I've seen a number of discussions by APL coders where they
decipher APL programs for entertainment. When reading code becomes a
puzzle-solving exercise, you have a maintenance problem.

APL's successor J, which uses ASCII, fewer symbols, and more words, is
better. But I don't think it's really usable as a general production
language. APL and J have some good ideas; the "function-oriented
programming" Backus describes is a nice alternative to LISP-style
functional programming. Those ideas need to be implemented in a
friendlier language, though.

> 1. Programming (at least in most of the commonly used languages) IS 
> technical writing. However, there may be some exclusions to this. (APL may 
> be one...)

Sure.

> 2. It is desirable to do what we can to make program code easily 
> intelligible, WHETHER WE ARE LIKELY TO MAINTAIN IT OR NOT! BUT...  not at 
> the expense of large amounts of writing that just add to the verbosity. 
> There are "break even" points. Deciding what they are is part of the "Art" 
> of computer programming; difficult to quantify.

Agreed, though that's true of technical writing as well. It's very
easy to produce a document that's too verbose for the reader.

> 3. Don't use APL. It is "dangerous" in every sense of the word... :-)

For just that reason, shouldn't everyone use it once? :-)
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-17T13:09:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com>`

```
Readable code?  You want *readable* code?

Well, it just so happens I once *won* a "readable code"  contest (of sorts) 
.....

---------- Forwarded Message ----------
From: INTERNET:iobcc@ptd.net, INTERNET:iobcc@ptd.net
TO: Michael Mattias, mcmattias
DATE: 5/16/98 9:06 PM

RE: Re: Entry

>5/2/98
>
…[8 more quoted lines elided]…
>Sturtevant WI

Hello Michael,

   Thankyou for entering the IOBCC. Believe it or not, you were the
_only_ person to submit an entry. I guess you win. Congratulations.
The IOBCC website will be removed from its server before the end of
the day.

C'ya,
John G.


$IF 0
  Obfuscation Contest Entry
  Email to: oibcc@ptd.net
  Author: Michael Mattias, Sturtevant WI USA ( mcmattias@compuserve.com)
  Date: 5.02.98
  Requires: PowerBASIC/DOS version 3.2 or 3.5
  Rated: PG-13 (D)
$ENDIF
$LIB ALL OFF
DEFINT A-Z
DIM V AS BYTE PTR
READ N: REDIM Z(N-1) AS DWORD: DIM ABSOLUTE B(N*4-1) AS BYTE AT VARSEG 
(Z(0))
COLOR 7,1:CLS:V=pbvScrnBuff+1800
FOR I=0 TO N-1: READ Z(I):FOR J=0 TO 3:@V=B(I*4+J): INCR V:DELAY .05:INCR 
V:NEXT,
END
DATA 9,1936943435,544820512,544437057,1293971017,662266721
DATA 1917198451,544501359,1684957527,538998639



No muss, no fuss, no bother.

MCM
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 9)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-03-18T15:33:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SC7wl.22517$Ws1.9518@nlpi064.nbdc.sbc.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com>`

```
In article <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com>, "Michael Mattias" <mmattias@talsystems.com> wrote:
>Readable code?  You want *readable* code?
>
…[3 more quoted lines elided]…
>DATA 1917198451,544501359,1684957527,538998639

It was LBJ that said that, wasn't it?
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 10)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-03-18T10:00:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G08wl.20747$YU2.666@nlpi066.nbdc.sbc.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com> <SC7wl.22517$Ws1.9518@nlpi064.nbdc.sbc.com>`

```
"Doug Miller" <spambait@milmac.com> wrote in message 
news:SC7wl.22517$Ws1.9518@nlpi064.nbdc.sbc.com...
> In article <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com>, "Michael Mattias" 
> <mmattias@talsystems.com> wrote:
…[8 more quoted lines elided]…
> It was LBJ that said that, wasn't it?

Not sure... but based on all the history of LBJ I've read,  it sure sounds 
like something he would have said!



MCM
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 10)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-03-18T12:07:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p072s41vmji8imhfefl97gcd7h2lc5lhb6@4ax.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com> <SC7wl.22517$Ws1.9518@nlpi064.nbdc.sbc.com>`

```
On Wed, 18 Mar 2009 15:33:03 GMT, spambait@milmac.com (Doug Miller)
wrote:

>In article <THRvl.9964$jZ1.3464@flpi144.ffdc.sbc.com>, "Michael Mattias" <mmattias@talsystems.com> wrote:
>>Readable code?  You want *readable* code?
…[6 more quoted lines elided]…
>It was LBJ that said that, wasn't it?

Too short.  Must've been Zachary Taylor that said it.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"Is there life before death?"
--  Graffito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 8)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-03-18T15:20:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com>`

```
In article <gponjj21bol@news7.newsguy.com>, Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>I've done a bit of programming in APL, just to see what it was like. I
>tend to agree with Djikstra: it encourages clever obscurantism. Dense
>function composition, obscure symbolic tokens, right-to-left binding,
>and so forth are actively hostile to human readers.

While I agree with most of what you say about APL, I have to wonder if 
right-to-left binding is "actively hostile to [all] human readers" or only to 
the large majority of us whose native languages read left to right.

It would be interesting to see if native readers of Hebrew or Arabic feel the 
same way about APL.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 9)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-03-18T10:57:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpr24u$b38$1@news.motzarella.org>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com>`

```
"Doug Miller" <spambait@milmac.com> wrote in message 
news:gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com...
> In article <gponjj21bol@news7.newsguy.com>, Michael Wojcik 
> <mwojcik@newsguy.com> wrote:
…[13 more quoted lines elided]…
> same way about APL.

Interesting idea - I too wonder if folks who normally read right to left 
would have issues with APL (maybe they would then have issues with Cobol and 
the like?)

However, as a long time APLer (well, it was mostly in the 70s and early 80s 
I worked on APL...) I'd like to point out:

  It is possible to write obscurely in any language [and far too many 
programmers do so!]

One advantage that APL may have, in that regard, is use the conciseness of 
APL and its indifference to the structure of the data (vector, matrix, array 
etc) to carefully write code that is both readable and understandable.

It doesn't help unfortunately, when people publish idioms that showcase the 
obscure tricks that give APL the reputation it doesn't deserve.

I am also reminded of the old adage: 'dont use a hammer with screws' - eg: 
use the correct tool for the job. SO many shops/organizations pick the tools 
then go looking for jobs to do...

regards
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-24T12:02:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1u7is417i4th6vr16jgqbsq6s4ch3u6ogk@4ax.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com> <gpr24u$b38$1@news.motzarella.org>`

```
On Wed, 18 Mar 2009 10:57:32 -0400, "Kerry Liles"
<kerry.removethisandoneperiod.liles@gmail.com> wrote:

>I am also reminded of the old adage: 'dont use a hammer with screws' - eg: 
>use the correct tool for the job. SO many shops/organizations pick the tools 
>then go looking for jobs to do...

But picture the hobbyist who has the best tool for every task -
filling up his work shop and emptying out his wallet.

We all need to compromise between such extremes.
```

###### ↳ ↳ ↳ Re: as the case may be

_(reply depth: 9)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-19T12:00:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gptsed1e4e@news3.newsguy.com>`
- **In-Reply-To:** `<gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com>`
- **References:** `<49AFF9C5.6F0F.0085.0@efirstbank.com> <SXSul.120971$fM1.68482@newsfe14.iad> <7eb01b59-21f8-41cc-adf2-13b0d7527519@o11g2000yql.googlegroups.com> <%TUul.50873$Tp5.19525@newsfe13.iad> <gpltf3$ejb$2@reader1.panix.com> <gpm44702qqa@news6.newsguy.com> <728etmFodgjdU1@mid.individual.net> <gponjj21bol@news7.newsguy.com> <gr7wl.22514$Ws1.1213@nlpi064.nbdc.sbc.com>`

```
Doug Miller wrote:
> In article <gponjj21bol@news7.newsguy.com>, Michael Wojcik <mwojcik@newsguy.com> wrote:
>> I've done a bit of programming in APL, just to see what it was like. I
…[6 more quoted lines elided]…
> the large majority of us whose native languages read left to right.

That's an interesting suggestion, but APL is typically written, and
meant to be read, left-to-right. Lines of APL source generally start
at the left edge of the screen, and so on.

Also, even in RTL languages, technical information (mathematical
formulas and so forth) are often written left-to-right. Japanese
prose, for example, is traditionally written vertically top-to-bottom,
with subsequent lines advancing from the right to the left (like
Chinese and Korean); but for technical documents, it's often written
horizontally, left-to-right, with lines advancing down. That makes it
easier to incorporate European-style mathematical notation.

So even people with an RTL first language might be more used to code
running left-to-right.

That's pure speculation on my part, though. I've met a few programmers
whose primary written language was RTL, but I don't know any well.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
