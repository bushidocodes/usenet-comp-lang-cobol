[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inspect...

_36 messages · 17 participants · 2005-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Inspect...

- **From:** "EBille" <billard.eric@free.fr>
- **Date:** 2005-10-17T05:59:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```
Hello,
I'm looking for a solution to validate datas :
Suppose you got first-name and want to display error message when you
encounter two spaces (and some other characters).
For exemple 'MIKE DANIEL    ' is good (because there is only one space
between Mike and Daniel) but 'MIKE  DANIEL   ' is not. The problem is
trailing spaces. I have tried this :
inspect ws-firstname tallying ws-mytally for characters before '  '
but it doesn't works : first-name never validates because of trailing
spaces.  Anybody has a solution ?
Thanks,
EB
Grenoble
France
```

#### ↳ Re: Inspect...

- **From:** "Mike B" <mxbNoSpam@ev1.net>
- **Date:** 2005-10-17T08:21:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11l79ar1h880afe@corp.supernews.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```
"EBille" <billard.eric@free.fr> wrote in message
news:1129553966.407455.254520@f14g2000cwb.googlegroups.com
> Hello,
> I'm looking for a solution to validate datas :
…[7 more quoted lines elided]…
> spaces.  Anybody has a solution ?

I am not the world's greatest COBOL programmer, but I've recently had to 
solve a similar problem. I used COBOL reference modification and started at 
the back of the data, reading forward until I found the first non-blank 
character and then using a loop to the beginning of the field to check for 
two adjacent spaces.

If you can't figure it out, post back. I need to dash off now and don't have 
time to look for the code, but I'll check back this afternoon and post some 
code if you need it.
```

##### ↳ ↳ Re: Inspect...

- **From:** bmuralidharan@gmail.com
- **Date:** 2005-10-17T06:50:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129557021.323601.247260@g47g2000cwa.googlegroups.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <11l79ar1h880afe@corp.supernews.com>`

```
Try this...

Move "MIKE DANIEL  " to ws-name
Unstring ws-name delimited by all spaces
    INTO First-name
         Last-name
-Murali

Mike B wrote:
> "EBille" <billard.eric@free.fr> wrote in message
> news:1129553966.407455.254520@f14g2000cwb.googlegroups.com
…[22 more quoted lines elided]…
> Mike B
```

#### ↳ Re: Inspect...

- **From:** howard.brazee@cusys.edu
- **Date:** 2005-10-17T07:45:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```
On 17 Oct 2005 05:59:26 -0700, "EBille" <billard.eric@free.fr> wrote:

>I'm looking for a solution to validate datas :

"datas"?

>Suppose you got first-name and want to display error message when you
>encounter two spaces (and some other characters).
…[5 more quoted lines elided]…
>spaces.  Anybody has a solution ?

There are several solutions for this, but my favorite is using
reference modification loops here.
```

##### ↳ ↳ Re: Inspect...

- **From:** "Mike" <MPBrede@gmail.com>
- **Date:** 2005-10-17T08:23:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129562629.617650.44890@z14g2000cwz.googlegroups.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com>`

```

howard.brazee@cusys.edu wrote:
> On 17 Oct 2005 05:59:26 -0700, "EBille" <billard.eric@free.fr> wrote:
>
> >I'm looking for a solution to validate datas :
>
> "datas"?

You should forgive him, he is French. Data has a plural in French. ;)

>
> >Suppose you got first-name and want to display error message when you
…[9 more quoted lines elided]…
> reference modification loops here.

Here is a sample I wrote. Serves two purposes. Solves your problem and
I can also get some feedback on my way of writing COBOL. Be kind,
gentle reader. :-)
       IDENTIFICATION DIVISION.
       PROGRAM-ID.    NameTest.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  GoodName                pic x(20) value 'Daniel Miller'.
       01  BadName                 pic x(20) value 'Daniel  Miller'.
       01  Ptr                     pic 9(02) value zero.
       01  Ptr2                    pic 9(02) value zero.
       01  EndLoopFlag             Pic x(01) value '0'.
           88  EndLoop                       value '1'.
           88  RunLoop                       value '0'.
       01  DblSpace                pic xx    value '  '.
       PROCEDURE DIVISION.

           If BadName not = space
               Perform varying ptr from length of BadName
                           by -1
                           Until EndLoop
                   if Badname(ptr:1) = space
                       Continue
                   else
                       Set EndLoop to true
                   End-If
               End-perform

               Set runloop to true
               Perform varying ptr2 from ptr
                           by -1
                           Until EndLoop
                   If BadName(ptr2:2) = DblSpace
                       Display "Name is rotten at " ptr2
                       set EndLoop to True
                   Else
                       if ptr2 = 0
                           Set EndLoop to true
                       End-if
                   End-if
               End-perform
           End-if

           Display 'End of Run'
           Stop Run.
```

###### ↳ ↳ ↳ Re: Inspect...

- **From:** Donald Tees <donald-tees@sympatico.ca>
- **Date:** 2005-10-17T11:31:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YsP4f.18645$GH1.138255@news20.bellglobal.com>`
- **In-Reply-To:** `<1129562629.617650.44890@z14g2000cwz.googlegroups.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com>`

```
Mike wrote:
> howard.brazee@cusys.edu wrote:
> 
…[10 more quoted lines elided]…
> 

Data *is* plural in english.  The singular is datum.

Donald
;<)
```

###### ↳ ↳ ↳ Re: Inspect...

- **From:** howard.brazee@cusys.edu
- **Date:** 2005-10-17T09:34:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com>`

```
On 17 Oct 2005 08:23:49 -0700, "Mike" <MPBrede@gmail.com> wrote:

>> "datas"?
>
>You should forgive him, he is French. Data has a plural in French. ;)

Interesting.   We use the Latin in English, where data *is* the plural
of datum.   While I knew that the French fight the inclusion of
foreign words and grammar, but didn't know it went back that far.    I
suspect it was a retro-fit.   Having a consistent grammar is
attractive to programmers such as myself.

But we're well in the process of forgetting that "data" is plural -
people in data processing rarely use the word "datum" and often say
"my data indicates that..."

But even worse, people in the media rarely use the word "medium".

I like the optional plural for "schema" of "schemata".   As in "I
modified some subschemata in our database".
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 4)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-10-18T00:17:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com>`

```
howard.brazee@cusys.edu wrote:

> On 17 Oct 2005 08:23:49 -0700, "Mike" <MPBrede@gmail.com> wrote:
> 
…[12 more quoted lines elided]…
> "my data indicates that..."

In current usage in English "data" is both the singular and the plural. Some
purists still say "the data are" but it sounds affected to me. 

I flunked French enough times to be careful about criticizing any native
speaker of that or any other language. I speak only English, COBOL and
profane languages, not necessarily in that order. 
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-18T08:17:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wz65f.24389$MG.14681@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com>`

```
"John Culleton" <john@wexfordpress.com> wrote:
>
> In current usage in English "data" is both the singular and the plural. 
> Some
> purists still say "the data are" but it sounds affected to me.


The distinction between data and datum implies that data are in discreet 
units, which is not always true. I prefer the connotation that data is, at 
least potentially, not in discreet units, such as is implied in the names 
for liquids (e.g. milk, water), where there is no singular/plural, at least 
in English.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 6)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2005-10-18T14:29:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r4u9l1dhi0c1gdiq2r1j2pjhre75i9kr65@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net>`

```
On Tue, 18 Oct 2005 08:17:13 -0500, "Judson McClendon"
<judmc@sunvaley0.com> wrote:

>"John Culleton" <john@wexfordpress.com> wrote:
>>
…[9 more quoted lines elided]…
>in English.

Used any half bits lately?
;-)
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-18T09:00:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ob75f.24400$MG.13809@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <r4u9l1dhi0c1gdiq2r1j2pjhre75i9kr65@4ax.com>`

```
"Ian Dalziel" <iandalziel@lineone.net> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>
…[8 more quoted lines elided]…
> ;-)


Data isn't bits, of course. We only use bits to represent (sometimes 
approximate) data. :-)
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 7)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-10-19T15:08:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj5nhg02k1o@news2.newsguy.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <r4u9l1dhi0c1gdiq2r1j2pjhre75i9kr65@4ax.com>`

```

In article <r4u9l1dhi0c1gdiq2r1j2pjhre75i9kr65@4ax.com>, Ian Dalziel <iandalziel@lineone.net> writes:
> On Tue, 18 Oct 2005 08:17:13 -0500, "Judson McClendon"
> <judmc@sunvaley0.com> wrote:
…[7 more quoted lines elided]…
> Used any half bits lately?

Seriously, partial bits come up quite often in information theory,
compression, and other areas of study.  There's a surprising amount
of work done on trits (unbiased three-state entities), which encode
the same amount of information as lg(3) = 1.5849... bits.  I think
I've seen some references to work using notional information quanta
equivalent to e (= 2.7182...) bits - so there you have irrational
(even transcendental) partial bits.

While the bit is clearly the smallest discrete integral information
quantum, and thus "natural" in that sense, it's not the only
conceivable or useful information quantum.

Moreover, as I noted in another post, while digital computers by
definition work on discrete data, analog computers do not, and for
them using data as a continuous noun is quite sensible.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-18T13:39:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj2tv5$djt$1@reader2.panix.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net>`

```
In article <wz65f.24389$MG.14681@bignews2.bellsouth.net>,
Judson McClendon <judmc@sunvaley0.com> wrote:
>"John Culleton" <john@wexfordpress.com> wrote:
>>
…[4 more quoted lines elided]…
>units, which is not always true.

How interesting... I usually think that the difference between datum and 
data is similar to the difference between rope and ropes.

>I prefer the connotation that data is, at 
>least potentially, not in discreet units, such as is implied in the names 
>for liquids (e.g. milk, water), where there is no singular/plural, at least 
>in English.

Odd... I recall hearing reference to 'the waters of (body of water)', as 
in 'the waters of the Atlantic' or 'the waters of the mighty Niagara'... 
NNNIIIIAAAAGGGAAARRRAAAA FFFAAAALLLLSSSSS!... *sloooooowly* I turned, 
*step* by step, *inch* by inch... sorry... where was I?  Oh yes... and it 
would seem to be appropriate to use the plural when referring to different 
kinds of milk ('mare's milk has a specific gravity of (m) while hamster's 
milk has a specific gravity of (n); if the two milks are mixed to obtain a 
specific gravity of (o) the aggregate fat content is found to be...')... 

... while on the other hand an individual's age, for instance, is a datum 
and whether a person had an automobile-accident in a given age-range is a 
datum (accident while 16 - 24 (Y/N)?  accident while 25 - 38 (Y/N)?, etc.) 
but 'the data on accidents during ages (y - z)' refers to 
multiples/plurals.

DD
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-18T09:06:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i75f.24401$MG.8798@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <dj2tv5$djt$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote:
> Judson McClendon <judmc@sunvaley0.com> wrote:
>>I prefer the connotation that data is, at
…[12 more quoted lines elided]…
> specific gravity of (o) the aggregate fat content is found to be...')...

You're begging the issue here, as you well know. One can always make a 
plural of a noun by creating subsets. It also has nothing to do with my 
point, again as you well know.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-10-18T08:56:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k13al15sa9nl4l8jkdhjsn6k2ak82q0i2f@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <dj2tv5$djt$1@reader2.panix.com> <7i75f.24401$MG.8798@bignews2.bellsouth.net>`

```
On Tue, 18 Oct 2005 09:06:56 -0500, "Judson McClendon"
<judmc@sunvaley0.com> wrote:

>You're begging the issue here, as you well know. 

Hmm.   Google shows "begging the issue" is a common phrase.   I'm
familiar with "begging the question", both the official definition
"The fallacy of reasoning committed when one assumes the truth of what
one is attempting to prove in an argument.", and the assumed meaning
of "encouraging a question".      

But I'm not finding a definition of "begging the issue".
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-18T15:25:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj344o$l0$1@reader2.panix.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <dj2tv5$djt$1@reader2.panix.com> <7i75f.24401$MG.8798@bignews2.bellsouth.net>`

```
In article <7i75f.24401$MG.8798@bignews2.bellsouth.net>,
Judson McClendon <judmc@sunvaley0.com> wrote:
><docdwarf@panix.com> wrote:
>> Judson McClendon <judmc@sunvaley0.com> wrote:
…[6 more quoted lines elided]…
>> in 'the waters of the Atlantic' or 'the waters of the mighty Niagara'...

[snip - today I feel free to interrupt myself]

>> and it
>> would seem to be appropriate to use the plural when referring to different
…[6 more quoted lines elided]…
>point, again as you well know.

Perhaps I am confused, Mr McClendon; your point, as I read it, was 
supported by 'as is implied in the names for liquids (e.g. milk, water), 
where there is no singular/plural, at least in English', which, I believe, 
is demonstrated above to be inaccurate.

DD
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-18T11:25:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ak95f.85005$5l.11643@bignews6.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <dj2tv5$djt$1@reader2.panix.com> <7i75f.24401$MG.8798@bignews2.bellsouth.net> <dj344o$l0$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote:
>
> Perhaps I am confused, Mr McClendon;

"Ornery" would be a better description, I suppose.

> your point, as I read it, was
> supported by 'as is implied in the names for liquids (e.g. milk, water),
> where there is no singular/plural, at least in English', which, I believe,
> is demonstrated above to be inaccurate.


Have you ever posted a legitimate contribution, or are you only capable of 
harping on others? Offhand, I can't recall you ever giving sample code, or 
instructions on how to do a useful thing in programming. I would be 
pleasantly surprised to be shown otherwise.

Technically, you are correct. But with the exception of archaic and 
contrived (pointless?) examples like yours, the usage of words for liquids, 
such as water and milk are not differentiated by singular and plural, as 
classical English rules say data and datum should be. When do you hear 
someone saying in English "I gave him several waters?" You may hear "I gave 
him water several times" or "I gave him several glasses of water." This, as 
you certainly know, was the meaning of my statement. Your comments 
contributed nothing of value. Typical. Too bad you apply your intellect and 
education to such paltry purpose, and not for meaningful contribution.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-18T16:36:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj389i$3ie$1@reader2.panix.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <7i75f.24401$MG.8798@bignews2.bellsouth.net> <dj344o$l0$1@reader2.panix.com> <ak95f.85005$5l.11643@bignews6.bellsouth.net>`

```
In article <ak95f.85005$5l.11643@bignews6.bellsouth.net>,
Judson McClendon <judmc@sunvaley0.com> wrote:
><docdwarf@panix.com> wrote:
>>
>> Perhaps I am confused, Mr McClendon;
>
>"Ornery" would be a better description, I suppose.

One does not rule out the other, Mr McClendon.

>
>> your point, as I read it, was
>> supported by 'as is implied in the names for liquids (e.g. milk, water),
>> where there is no singular/plural, at least in English', which, I believe,
>> is demonstrated above to be inaccurate.

[snip]

>
>Technically, you are correct.

Thanks much for acknowledging this, most gracious of you.

>But with the exception of archaic and 
>contrived (pointless?) examples like yours, the usage of words for liquids, 
>such as water and milk are not differentiated by singular and plural, as 
>classical English rules say data and datum should be. When do you hear 
>someone saying in English "I gave him several waters?"

Such a thing can be heard during comparison-tastings of bottled beverages, 
Mr McClendon, and I've seen such events more than once... did you know 
that what comes out of the taps in New York City is often a taste-test 
winner?

[snip]

>Too bad you apply your intellect and 
>education to such paltry purpose, and not for meaningful contribution.

Meaning, as Wittgenstein tells it, is the result of interpretation, Mr 
McClendon; that you see none may speak more of your ability to interpret 
than of the phenomenon.  Thanks much, though, for your most... charitable 
evaluations.

DD
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 10)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-10-18T21:21:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uHd5f.456861$5N3.134893@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<ak95f.85005$5l.11643@bignews6.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <dj2tv5$djt$1@reader2.panix.com> <7i75f.24401$MG.8798@bignews2.bellsouth.net> <dj344o$l0$1@reader2.panix.com> <ak95f.85005$5l.11643@bignews6.bellsouth.net>`

```


Judson McClendon wrote:
> <docdwarf@panix.com> wrote:
> 
…[16 more quoted lines elided]…
> pleasantly surprised to be shown otherwise.

Judson, don't be so hard on the Doc.  Sure, he's a character 
sometimes, but I find him entertaining.  And I have seem him post code 
examples in this forum, and also instructions on how to do useful, on 
topic, things in programming.  He's very polite in private email.

Although I have never met the Doc in real life, I consider him a friend.

With kindest regards,
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-19T17:18:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj5v5q$jfe$1@reader2.panix.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <dj344o$l0$1@reader2.panix.com> <ak95f.85005$5l.11643@bignews6.bellsouth.net> <uHd5f.456861$5N3.134893@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <uHd5f.456861$5N3.134893@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>Although I have never met the Doc in real life, I consider him a friend.

Pfoo, you'se jes' easily impressed... I'd blush, were I able to remember 
how.

DD
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 6)_

- **From:** john@wexfordpress.com
- **Date:** 2005-10-18T12:49:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129664973.366304.317280@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<wz65f.24389$MG.14681@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net>`

```

Judson McClendon wrote:

> The distinction between data and datum implies that data are in discreet
> units, which is not always true. I prefer the connotation that data is, at
> least potentially, not in discreet units, such as is implied in the names
> for liquids (e.g. milk, water), where there is no singular/plural, at least
> in English.

Sometimes data is discreet, and sometimes it is most indiscreet. It
depends on the subject matter. However a single item of information,
whatever the subject, is a discrete quantity or value.

Have you never heard of the bridge over troubled waters? Perhaps you
are too young...

John Culleton
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-19T05:22:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E5p5f.37134$Lp.37101@bignews5.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <1129664973.366304.317280@g47g2000cwa.googlegroups.com>`

```
<john@wexfordpress.com> wrote:
>
> Judson McClendon wrote:
…[14 more quoted lines elided]…
> are too young...


Hardly, John.  I enjoyed S&G in real-time. :-)
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 7)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-10-19T15:51:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj5q2302cpd@news3.newsguy.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net> <1129664973.366304.317280@g47g2000cwa.googlegroups.com>`

```

In article <1129664973.366304.317280@g47g2000cwa.googlegroups.com>, john@wexfordpress.com writes:
> Judson McClendon wrote:
> 
…[5 more quoted lines elided]…
> whatever the subject, is a discrete quantity or value.

A single item of information, like a single item of anything, is by
definition discrete; but information is not partitioned into items
ab initio.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-10-19T14:59:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj5n0002a3b@news3.newsguy.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <qpg7l1tfl8sfi3fidc6brcvhjertovrmpv@4ax.com> <nMudnSukgN4-osnenZ2dnUVZ_s-dnZ2d@adelphia.com> <wz65f.24389$MG.14681@bignews2.bellsouth.net>`

```

In article <wz65f.24389$MG.14681@bignews2.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> writes:
> "John Culleton" <john@wexfordpress.com> wrote:
> >
…[7 more quoted lines elided]…
> in English.

It's certainly possible that many speakers view "data" as a
continuous entity - though in this context it's ironic, since the
very definition of digital computation is that it treats data as
discrete.  It'd be more logical to say "the data is ..." if we were
using analog computers.

It's also reasonable to argue that "data" is popularly treated as a
"collective noun", that is a noun which names a group but "occur[s]
in the singular", as _The Oxford Companion to the English Language_
puts it.  (And since there is no generally-recognized authority for
English usage, popular treatment is arguably the most eligible metric
for "correct" use.)

In British English, collective nouns often have plural number and
take a plural verb, etc; but in American English, they generally have
singular number.  Thus in the US it's common to say for example "the
audience was quiet", while in the UK "the audience were quiet" would
be preferred by many speakers.

_The Oxford Companion_, incidentally, has this to say about "data":

   *Data* is currently both plural ('The data are available') and
   collective ('How much data do you need?'), and is often therefore
   a controversial usage issue.

and goes on to note:

   Such usages ... are disliked (often intensely) not only by purists
   but by many who consider themselves liberal in matters of usage.
   Purism, however, also has its barbarisms, such as the quasi-
   classical plurals *octopi* and *syllabi*...
   ("Classical Ending", 218)

(Of course the "correct" plural for "syllabus", which is a Greek
derivation and not a Latin one, would be something like
"syllabontes".  I expect all teachers to begin using it immediately.)

The most important ideas there, I think, are that some usages are
controversial, and that "purism also has its barbarisms".
```

###### ↳ ↳ ↳ Re: Inspect...

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2005-10-17T16:05:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2005.10.17.22.05.09.223820@starband.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com>`

```
Adding comment inline with CJP prefix....

On Mon, 17 Oct 2005 08:23:49 -0700, Mike wrote:
> 
> Here is a sample I wrote. Serves two purposes. Solves your problem and
…[14 more quoted lines elided]…
>        01  DblSpace                pic xx    value '  '.

CJP - Not sure what compiler you use and how it processes in this
light....but on MVS, each 01 level starts on a doubleword boundary (8 byte
boundary).  So your Working storage would take up 
24+24+8+8+8+2 = 74 bytes 
vs.
20+20+2+2+1+2 = 47 bytes

Also make sure your pointers are in a format that does not need to be
changed in order for the compiler to use them efficiently.  On MVS, PIC
9(2) would need to be converted from character to binary, manipulated,
then converted back to put it back into the variable.

Not horrible items given the program's purpose, but food for thought when
writing your programs.  Always write with efficiency of the runtime in
mind. 

>        PROCEDURE DIVISION.
> 
…[10 more quoted lines elided]…
> 

CJP  I'd write this:
CJP              Perform varying ptr from length of BadName
CJP                                    by -1
CJP                Until ptr < 1
CJP                   or Badname (ptr:1) not = space
CJP                  Continue
CJP              End-perform
CJP You are doing the comparison already in the IF statement so you lose
nothing putting it in the PERFORM, but you gain the loss of the ELSE and
manipulation of the flag which in THIS case is not really necessary (but
handy sometimes).

>                Set runloop to true
>                Perform varying ptr2 from ptr
…[10 more quoted lines elided]…
>                End-perform

CJP When ptr2 makes it to 0, the refmod will be attempted first....
CJP Try...
CJP              Perform varying ptr2 from ptr 
CJP                         by -1
CJP                Until ptr2 < 1 
CJP                   or BadName(ptr2:2) = Spaces 
CJP                  continue
CJP              End-perform
CJP
CJP              if ptr2 > 0
CJP                  Display "Name is rotten at " ptr2 
CJP              End-if
CJP
CJP Note also, that DblSpace is not necessary in this example as the
SPACES word can be use to the same effect.  Again a space issue.

>            End-if
> 
>            Display 'End of Run'
>            Stop Run.

CJP:
I also like to make flag settings in code rather than rely on VALUE
clauses for the initial setting.  Again on MVS, you can be set to reuse
the working storage so COBOL does not have to reallocate it every time. 
It is also better documentation as to what is happening in the program if
you set data items in the run.  Otherwise you need to go back to W-S to
figure out what you're initialized to.  In a large program, that can be a
lot of scrolling to find it out.  It is also safer if you have a runtime
environment that may reuse the W-S as-is without re-initializing it. 
Initialize it yourself.  

I usually only use VALUE clauses for items that I know will not change in
the code.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-17T15:52:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129589548.692126.235240@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<pan.2005.10.17.22.05.09.223820@starband.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <pan.2005.10.17.22.05.09.223820@starband.net>`

```
>>            If BadName not = space
>>                Perform varying ptr from length of BadName
…[7 more quoted lines elided]…
>>                End-perform

CJP  I'd write this:
CJP              Perform varying ptr from length of BadName
CJP                                    by -1
CJP                Until ptr < 1
CJP                   or Badname (ptr:1) not = space

If efficiency is what you require then the initial 'If badname not =
spaces' eliminates the need to check for 'ptr < 1' as there is
guaranteed to be a non-space character.

If efficiency is what you require then your compiler may do better with
an OCCURS and an index rather than reference notation.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-10-18T07:36:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6iu9l1p3tqhjrrapdofslf9dhmq9a8o7u0@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <pan.2005.10.17.22.05.09.223820@starband.net> <1129589548.692126.235240@f14g2000cwb.googlegroups.com>`

```
On 17 Oct 2005 15:52:28 -0700, "Richard" <riplin@Azonic.co.nz> wrote:

>CJP  I'd write this:
>CJP              Perform varying ptr from length of BadName
…[6 more quoted lines elided]…
>guaranteed to be a non-space character.

With all compilers?
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-18T11:25:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129659944.447430.53300@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<6iu9l1p3tqhjrrapdofslf9dhmq9a8o7u0@4ax.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <4la7l1h93tejsjgupbr9vtco6tjd91if08@4ax.com> <1129562629.617650.44890@z14g2000cwz.googlegroups.com> <pan.2005.10.17.22.05.09.223820@starband.net> <1129589548.692126.235240@f14g2000cwb.googlegroups.com> <6iu9l1p3tqhjrrapdofslf9dhmq9a8o7u0@4ax.com>`

```
>If efficiency is what you require then the initial 'If badname not =
>spaces' eliminates the need to check for 'ptr < 1' as there is
>guaranteed to be a non-space character.

> With all compilers?

Yes, after an 'If badname not = >spaces' there is guaranteed to be a
non-space character if the field with all compilers.
```

#### ↳ Re: Inspect...

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-17T09:16:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20051017101613.206$sY@news.newsreader.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```
"EBille" <billard.eric@free.fr> wrote:
> Suppose you got first-name and want to display error message when you
> encounter two spaces (and some other characters).
…[5 more quoted lines elided]…
> spaces.  Anybody has a solution ?


It's a little more complete than your example, but you can download file 
NAME.ZIP from my website below under "COBOL Source Files." It was programmed 
to work using COBOL 74, COBOL 85 or COBOL 2002.
```

#### ↳ Re: Inspect...

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-10-17T21:32:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11l8kb2v5obc62@corp.supernews.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```

"EBille" <billard.eric@free.fr> wrote in message
news:1129553966.407455.254520@f14g2000cwb.googlegroups.com...
> Hello,
> I'm looking for a solution to validate datas :
…[11 more quoted lines elided]…
> France

           move 1 to ws-mytally
           inspect ws-firstname tallying ws-mytally
             for characters before '  '
           if ws-firstname (ws-mytally:) not = spaces
               display 'bad name'
           end-if
```

#### ↳ Re: Inspect...

- **From:** "EBille" <billard.eric@free.fr>
- **Date:** 2005-10-18T05:39:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129639187.506336.228660@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com>`

```
Hello,
Thanks for all your response. I will try all your solutions, but
thought INSPECT was faster than any hand-written code...  the program
i'm writing has a lot of data to validate (name, age, address and
more...).
You're right also for my poor usage of grammar. I use lots of english
terms, (sorry, Mr Toubon) and apply plural to them, even when they are
yet... And the worst of it is that I have learn Latin when I was 11 to
14. Forgot it quickly. Have better PHP or FoxPro... ;-)) and cobol.
Have a nice day,
EB
Grenoble
France
```

##### ↳ ↳ Re: Inspect...

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-18T08:45:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MZ65f.24393$MG.12590@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <1129639187.506336.228660@g14g2000cwa.googlegroups.com>`

```
"EBille" <billard.eric@free.fr> wrote:
> ... but [I] thought INSPECT was faster than any hand-written code...


Bad assumption. In some speed tests we did in this newsgroup a few years 
ago, it turned out that hand coded loops using reference modification were 
usually faster (sometimes significantly so), than most of the intrinsic text 
manipulation functions. This was surprising to many of us. Below is a 
message Peter Dashwood posted during that exchange, including a sample 
benchmark program.
```

###### ↳ ↳ ↳ Re: Inspect...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-18T11:33:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129660428.768569.99290@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<MZ65f.24393$MG.12590@bignews2.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <1129639187.506336.228660@g14g2000cwa.googlegroups.com> <MZ65f.24393$MG.12590@bignews2.bellsouth.net>`

```
>> ... but [I] thought INSPECT was faster than any hand-written code...

> Bad assumption. In some speed tests we did in this newsgroup a few years
> ago, it turned out that hand coded loops using reference modification were
> usually faster (sometimes significantly so), than most of the intrinsic text
> manipulation functions.

That is a misleading statement because the only use of INSPECT being
tested was with FUNCTION REVERSE.

There is nothing in the test program that compares the general use of
INSPECT with hand coded loops except where REVERSE is likely to mask
the performance.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-19T05:30:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdp5f.37135$Lp.3439@bignews5.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <1129639187.506336.228660@g14g2000cwa.googlegroups.com> <MZ65f.24393$MG.12590@bignews2.bellsouth.net> <1129660428.768569.99290@o13g2000cwo.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
>>> ... but [I] thought INSPECT was faster than any hand-written code...
>
…[12 more quoted lines elided]…
> the performance.


Richard, that was one example test program out of several. In every case, 
IIRC, hand coded loops using reference modification were at least as fast 
as, or faster than, intrinsic text functions. But, it is easy enough to 
write a small benchmark program to verify this. I was not making a specific 
point about INSPECT, but simply pointing out the error of assuming an 
intrinsic would be faster than hand coded logic.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-10-19T11:09:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11lcokc6e63oi39@corp.supernews.com>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <1129639187.506336.228660@g14g2000cwa.googlegroups.com> <MZ65f.24393$MG.12590@bignews2.bellsouth.net> <1129660428.768569.99290@o13g2000cwo.googlegroups.com> <vdp5f.37135$Lp.3439@bignews5.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:vdp5f.37135$Lp.3439@bignews5.bellsouth.net...
> "Richard" <riplin@Azonic.co.nz> wrote:
> >>> ... but [I] thought INSPECT was faster than any hand-written code...
> >
> >> Bad assumption. In some speed tests we did in this newsgroup a few
years
> >> ago, it turned out that hand coded loops using reference modification
> >> were
…[15 more quoted lines elided]…
> write a small benchmark program to verify this. I was not making a
specific
> point about INSPECT, but simply pointing out the error of assuming an
> intrinsic would be faster than hand coded logic.

Test program using Micro Focus COBOL V3.24
----
       program-id. inspect1.
      * find position of two consecutive spaces in text
      * using different methods
      * 2 - inspect statement
      * 3 - loop with reference modification
      * 4 - unrolled loop
      * 5 - generally faster unrolled loop
       data division.
       working-storage section.
       1 loop-count comp-5 pic 9(9) value 100000000.
       1 str pic x(20) value space.
       1 pos comp-5 pic 9(4) value 0.
       1 x comp-5 pic 9(4) value 0.
       1 clock-times.
        2 occurs 5.
         3 clock-time.
          4 time-hour pic 99.
          4 time-minute pic 99.
          4 time-second pic 99v99.
         3 final-pos comp-5 pic 9(4).
       1 elapsed-time pic 9(7)v99.
       1 elapsed-time-display pic z(6)9.99.
       procedure division.
       mainline section.
           move spaces to str
           perform time-test
           move "MIKE DANIEL" to str
           perform time-test
           move "MIKE  DANIEL" to str
           perform time-test
           move "ABCDEFGHIJKLMNOPQRST" to str
           perform time-test
           stop run
           .
       time-test section.
           accept clock-time (1) from time
           perform in-spect loop-count times
           move pos to final-pos (2)
           accept clock-time (2) from time
           perform loop loop-count times
           move pos to final-pos (3)
           accept clock-time (3) from time
           perform unrolled-loop loop-count times
           move pos to final-pos (4)
           accept clock-time (4) from time
           perform faster-unrolled-loop loop-count times
           move pos to final-pos (5)
           accept clock-time (5) from time
           display clock-time (1) space str
           perform varying x from 2 by 1 until x > 5
               if clock-time (x - 1) > clock-time (x)
                   move 86400 to elapsed-time
               else
                   move 0 to elapsed-time
               end-if
               compute elapsed-time = elapsed-time
                 + (time-hour (x - 1) - time-hour (x)) * 3600
                 + (time-minute (x - 1) - time-minute (x)) * 60
                 + (time-second (x - 1) - time-second (x))
               move elapsed-time to elapsed-time-display
               display clock-time (x)
                   space x
                   space elapsed-time-display
                   space final-pos (x)
           end-perform
           .
       in-spect section.
           move 1 to pos
           inspect str tallying pos
             for characters before "  "
           .
       loop section.
           perform varying pos from 1 by 1
             until pos > 19
               if "  " = str (pos:2)
                   exit perform
               end-if
           end-perform
           if pos > 19
               move 21 to pos
           end-if
           .
       unrolled-loop section.
           evaluate space
             when = str (1:2) move 1 to pos
             when = str (2:2) move 2 to pos
             when = str (3:2) move 3 to pos
             when = str (4:2) move 4 to pos
             when = str (5:2) move 5 to pos
             when = str (6:2) move 6 to pos
             when = str (7:2) move 7 to pos
             when = str (8:2) move 8 to pos
             when = str (9:2) move 9 to pos
             when = str (10:2) move 10 to pos
             when = str (11:2) move 11 to pos
             when = str (12:2) move 12 to pos
             when = str (13:2) move 13 to pos
             when = str (14:2) move 14 to pos
             when = str (15:2) move 15 to pos
             when = str (16:2) move 16 to pos
             when = str (17:2) move 17 to pos
             when = str (18:2) move 18 to pos
             when = str (19:2) move 19 to pos
             when other move 21 to pos
           end-evaluate
           .
       faster-unrolled-loop section.
           evaluate space
             when = str (1:1) and str (2:1) move 1 to pos
             when = str (2:1) and str (3:1) move 2 to pos
             when = str (3:1) and str (4:1) move 3 to pos
             when = str (4:1) and str (5:1) move 4 to pos
             when = str (5:1) and str (6:1) move 5 to pos
             when = str (6:1) and str (7:1) move 6 to pos
             when = str (7:1) and str (8:1) move 7 to pos
             when = str (8:1) and str (9:1) move 8 to pos
             when = str (9:1) and str (10:1) move 9 to pos
             when = str (10:1) and str (11:1) move 10 to pos
             when = str (11:1) and str (12:1) move 11 to pos
             when = str (12:1) and str (13:1) move 12 to pos
             when = str (13:1) and str (14:1) move 13 to pos
             when = str (14:1) and str (15:1) move 14 to pos
             when = str (15:1) and str (16:1) move 15 to pos
             when = str (16:1) and str (17:1) move 16 to pos
             when = str (17:1) and str (18:1) move 17 to pos
             when = str (18:1) and str (19:1) move 18 to pos
             when = str (19:1) and str (20:1) move 19 to pos
             when other move 21 to pos
           end-evaluate
           .
       end program inspect1.
-----

Results
-----
10502395
10502522 00002       1.27 00001
10502632 00003       1.10 00001
10502730 00004       0.98 00001
10502829 00005       0.99 00001
10502829 MIKE DANIEL
10503736 00002       9.07 00012
10504658 00003       9.22 00012
10504938 00004       2.80 00012
10505120 00005       1.82 00012
10505120 MIKE  DANIEL
10505482 00002       3.62 00005
10505845 00003       3.63 00005
10505993 00004       1.48 00005
10510103 00005       1.10 00005
10510103 ABCDEFGHIJKLMNOPQRST
10511476 00002      13.73 00021
10512827 00003      13.51 00021
10513239 00004       4.12 00021
10513503 00005       2.64 00021
-----

In this case, I find little difference between INSPECT and
loop; but, if "faster is better", there are other alternatives.
```

###### ↳ ↳ ↳ Re: Inspect...

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-10-20T21:15:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8019$43584f24$45491c57$5973@KNOLOGY.NET>`
- **In-Reply-To:** `<vdp5f.37135$Lp.3439@bignews5.bellsouth.net>`
- **References:** `<1129553966.407455.254520@f14g2000cwb.googlegroups.com> <1129639187.506336.228660@g14g2000cwa.googlegroups.com> <MZ65f.24393$MG.12590@bignews2.bellsouth.net> <1129660428.768569.99290@o13g2000cwo.googlegroups.com> <vdp5f.37135$Lp.3439@bignews5.bellsouth.net>`

```
Judson McClendon wrote:
> "Richard" <riplin@Azonic.co.nz> wrote:
> 
…[9 more quoted lines elided]…
> intrinsic would be faster than hand coded logic.

 From what I've seen, in my environment, the best speed is done by 
defining the data area as a table of characters (hey, wonder where that 
idea came from!), with an index, then using the index to spin through 
the data... i.e.,

01  my80charLine           pic X(80).
01  my80charBreakout.
     12  mySingleChar  occurs 80 times
                         indexed by myCharIdx
                            pic X(01).
...
if my80charLine = spaces then
     *> We've got a blank line
     move [CR]      to mySingleChar (1)
     move [LF]      to mySingleChar (2)
     set  myCharIdx to 2
else
     if mySingleChar (80) > space then
         *> The line is full
         set myCharIdx to 80
     else
         perform varying myCharIdx from 79 by -1
           until  myCharIdx < 2
               or mySingleChar (myCharIdx) > space
             continue
         end-perform
     end-if
end-if

Once this code has executed, myCharIdx now points to the last character 
in the string.  This has tested quicker on our mainframe (although I 
can't put my hands on the exact numbers) than any other method, 
including reference modification and "inspect function reverse".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
