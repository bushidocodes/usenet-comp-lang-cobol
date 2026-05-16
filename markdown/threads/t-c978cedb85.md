[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Nested "Occurs Depending On"

_39 messages · 15 participants · 2010-12 → 2011-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Nested "Occurs Depending On"

- **From:** Pakku <pakku@soccermail.com>
- **Date:** 2010-12-23T11:30:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com>`

```
Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING ON?  

Is this some compiler limitation or machine limitation?  Or just an arbitrary decision?
```

#### ↳ Re: Nested "Occurs Depending On"

- **From:** Richard Luketich <rluketich@rlyxx.com>
- **Date:** 2010-12-23T19:06:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oor7h6dn50b18mk07k1bscl8ufb50ofiok@4ax.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com>`

```
Last I checked, it does. However, it does have some rules around the
ODO, or you may have a compiler option set that is disallowing the use
of nested OCCURS DEPENDING ON. Due to the amount of housekeeping and
the fact that I haven't come across an application that truly requires
such a data structure, I've never used it. (Although, I could see it
being very useful when processing an XML file.)

The Enterprise COBOL for z/OS LRM
(http://publibfp.boulder.ibm.com/epubs/pdf/igy3lr50.pdf) even mentions
this explicitely:

Certain uses of the OCCURS DEPENDING ON clause result in complex
OCCURS DEPENDING ON (ODO) items. The following constitute complex ODO
items:
- A data item described with an OCCURS DEPENDING ON clause that is
ollowed by a nonsubordinate elementary data item, described with or
without an OCCURS clause
- A data item described with an OCCURS DEPENDING ON clause that is
followed by a nonsubordinate group item
****************
- A group item that contains one or more subordinate items described
with an OCCURS DEPENDING ON clause
****************
- A data item described with an OCCURS clause or an OCCURS DEPENDING
ON clause that contains a subordinate data item described with an
OCCURS DEPENDING ON clause (a table that contains variable-length
elements)
- An index-name associated with a table that contains variable-length
elements



On Thu, 23 Dec 2010 11:30:45 -0800 (PST), Pakku <pakku@soccermail.com>
wrote:

>Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING ON?  
>
>Is this some compiler limitation or machine limitation?  Or just an arbitrary decision?
```

#### ↳ Re: Nested "Occurs Depending On"

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-12-26T19:05:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com>`

```
Pakku wrote:
> Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING
> ON?
>
> Is this some compiler limitation or machine limitation?  Or just an
> arbitrary decision?

It's quite logical. And common.

Imagine
01  Mydata.
   02  Mydata-really OCCURS 1 TO 100 DEPENDING ON My-Num  PIC X.
   02  Wally  PIC X.

So, where's Wally in memory?

At byte-101 in Mydata? Or somewhere between 2 and 101 depending on My-Num?

If the latter, does Wally get moved in the background every time My-Num 
changes?
```

##### ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-12-27T04:27:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b6fe044-c77f-4aa5-934c-798ca071f627@g27g2000vbl.googlegroups.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com>`

```
On Dec 27, 1:05 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Pakku wrote:
> > Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING
…[17 more quoted lines elided]…
> changes?

You simplified that. The OP said NESTED OCCURS DEPENDING ON which adds
another order of complexity.

BTW, loved the Al Qaeda/Israeli passport joke.
```

##### ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** Richard Luketich <rluketich@rlyxx.com>
- **Date:** 2010-12-28T22:55:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com>`

```
On Sun, 26 Dec 2010 19:05:24 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>Pakku wrote:
>> Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING
…[18 more quoted lines elided]…
>

In zOS COBOL, Wally is at the location immediately following
Mydata-really(My-Num). My recollection is that Wally is NOT moved
automatically when you increase My-Num, which is where using nested or
multiple ODO in the same structure becomes complex.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-12-29T02:05:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GZBSo.61639$Mg5.39410@en-nntp-06.dc1.easynews.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com> <fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com>`

```
"Richard Luketich" <rluketich@rlyxx.com> wrote in message 
news:fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com...
> On Sun, 26 Dec 2010 19:05:24 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[26 more quoted lines elided]…
> multiple ODO in the same structure becomes complex.

Just a little clarification, in IBM mainframe COBOL (Enterprise COBOL and 
all compilers that I know of in the past),

The compiler/run-time LOOKS for WALLY at the "address" jsut after the 
CURRENT size of Mydata-erally (my-num).  This is used for both receiving ans 
ending references to WALLY, i..e it looks at that address to update or send 
from the field.

The DATA at that location is never implicitly moved.  So that when/if my-num 
changes, then the compiler/run-time will look at the "new" address for data 
(either to use as a sending or receivinhg item).  For some examples of how 
this wokrs (and man NOT be what is intended, check out the Micro Focus 
ODOSLIDE compiler directive).  OTOH, when Micro Focus uses NO-ODOSLIDE, then 
the MAXIUM size of the ODO fields is unsed and "WALLY" is always found at 
the same place (and with the expected content) - but that means that the 
actual "phsucial" size of the group MYDATA never chenges.

Either approah may well lead to "unexpected results" - but both are 
supported by their respective compiler.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-01-01T21:31:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com> <fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com>`

```
Richard Luketich wrote:
> On Sun, 26 Dec 2010 19:05:24 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[27 more quoted lines elided]…
> multiple ODO in the same structure becomes complex.

If it's not moved, it's already complex. Consider:

Assume My-num = 3, we have.

x x x W . . .

Now
MOVE 4 TO My-Num.
MOVE "Z" TO Mydata-Really (My-Num)

If Wally is not moved, you must have either

x x x Z W . . . (which generates immense run-time complexity)
or
x x x Z . . . (Wally has left the building)

I suggest the only way a field subordinate to an ODO can exist efficiently 
is when the succeeding field exists at a location GREATER than the max of 
the ODO variable, viz:

x x x x . . . . . Wally

Even this might generate funky code when you MOVE the group somewhere. Does 
the MOVE include the implied slack bytes or does the MOVE work like the 
STRING verb?

I'm reminded of a discussion in the Talmud. The tax on a newborn male is 1 
Shekel per head, payable to the Temple priests. The discussion was over what 
must the tax be if a TWO-HEADED child was born? Was the tax one Shekel or 
two?

The whole business was put to rest when one rabbi, evidently wiser than the 
rest, said "Put the child under a cherem (banished as impure) and the 
problem goes away."

The analogy here is obvious.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-03T01:52:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ifra4u$chb$1@reader1.panix.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com> <fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com>`

```
In article <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Richard Luketich wrote:
>> On Sun, 26 Dec 2010 19:05:24 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
>> wrote:

[snip]

>>> Imagine
>>> 01  Mydata.
…[41 more quoted lines elided]…
>STRING verb?

I am not a compiler author nor am I familiar with compiler intracies but 
it would make sense if Wally were placed at the outermost bound of the ODO 
field which depends on it.  Were the ODO field to change in size then 
either slack bytes out to its limits would have to be preserved at compile 
or *all* the WS fields after it would be subject to movement as the 
'depending' value changes.

How a MOVE of such a field works might be readily determined by compiling 
something with a PMAP... errr, LIST or other Assembley-generating 
equivalent.

>
>I'm reminded of a discussion in the Talmud. The tax on a newborn male is 1 
>Shekel per head, payable to the Temple priests.

I'm reminded of the Wife of Bath making things up whole cloth and 
supporting it with 'And you can look it up in your Almagest'.  The 
redemption of the firstborn, as best I recall it, is based on Ex.XIII.2 
and the sum specifically mentioned in Num.III.47 is five shekels (100 
gerahs).

Do you have a cite for this 'Talmudic discussion' or did it occur around 
the place where it is discussed what happens when two men fall down a 
chimmney and one comes out clean while the other is dirty?

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-01-03T09:25:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com> <fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com> <ifra4u$chb$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
>
> I'm reminded of the Wife of Bath making things up whole cloth and
…[8 more quoted lines elided]…
>

You are correct. The redemption price is five shekalim.

You are incorrect in assuming - or at least suggesting - a) that this is the 
Jewish equivalent of an old-wives-tale, or b) that I make this shit up.

The discussion on the two-headed child can be found in (Babylonian) Menahot 
37a-b.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-03T18:28:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ift4ga$ae1$1@reader1.panix.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com> <ifra4u$chb$1@reader1.panix.com> <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com>`

```
In article <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>>
…[14 more quoted lines elided]…
>Jewish equivalent of an old-wives-tale, or b) that I make this shit up.

I made no assumptions and explicitly stated that I was reminded of 
something; last time I looked in the United States of America one was 
still permitted a bit of freedom of association.

>
>The discussion on the two-headed child can be found in (Babylonian) Menahot 
>37a-b. 

This is a difficult often encountered with languages with other alphabets; 
the 'h' in Menahot might be a soft h (Hebrew alphabet 'heh' or 'hay') or 
an aspirated 'h' (Hebrew alphabet 'chet' or 'ches', where 'ch' is 
pronounced as in the Scottish 'loch').  According to 
http://www.mediafire.com/file/ytnetzdmjno/Menachoth.pdf this reads:

--begin quoted text:

[37a]

In the meantime there came a man [to the school] saying, I have begotten a 
first-born child with two heads, how much must I give the priest?11 An old 
man came forward and ruled that he must give [the priest] ten sela's. But 
this is not so! For Rami b. Hama learnt: From the verse. The firstborn of 
man thou shalt surely redeem,12 I might conclude that this would apply 
even when the firstborn was rendered trefah13 within thirty days [of his 
birth]. Scripture therefore added,

[37b]

Howbeit,1 limiting thereby [the general application]!2  In this case it is 
different since the Divine Law declared [the law of redemption] to be 
governed by the expression per head.3

--end quoted text

Now, should this leave any doubts to even the most occluded eye note that 
footnote 3 for 37b reads '(3) Num. III, 47. Consequently as this child has 
two heads and is now living there must be a payment of ten sela's for his
redemption.'

It is left to the reader to determine whether the aforementioned (but 
clipped from this post) declaration of impurity was 'the Jewish equivalent 
of an old-wives-tale', fabricated whole cloth, misread, misremembered or 
the ever-popular E) Some of the Above.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-03T19:17:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o05i65bkdj75hj6ubmrbvqfg473s56v1j@4ax.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com> <ifra4u$chb$1@reader1.panix.com> <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com> <ift4ga$ae1$1@reader1.panix.com>`

```
On Mon, 3 Jan 2011 18:28:26 +0000 (UTC), docdwarf@panix.com () wrote:

>
>I made no assumptions and explicitly stated that I was reminded of 
>something; last time I looked in the United States of America one was 
>still permitted a bit of freedom of association.


That may be changing.   A lot of people seem to not value our freedoms
as much as other, more nebulous things.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-04T19:18:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ifvrqe$jh4$1@reader1.panix.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com> <ift4ga$ae1$1@reader1.panix.com> <7o05i65bkdj75hj6ubmrbvqfg473s56v1j@4ax.com>`

```
In article <7o05i65bkdj75hj6ubmrbvqfg473s56v1j@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 3 Jan 2011 18:28:26 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>as much as other, more nebulous things.

I am not sure which is better, 'a lot of people (who) seem not to value 
our freedoms as much as other, more nebulous things' or 'a lot of people 
who seem to value what they believe our freedoms to be to the point where 
said freedoms are to be hoarded and dealt out on grounds of personal 
prejudice or favor rather than law.'

Nevertheless, last time I looked it was as I described.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-01-04T09:40:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eYOdnX02we36or7QnZ2dnUVZ_vOdnZ2d@earthlink.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com> <ifra4u$chb$1@reader1.panix.com> <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com> <ift4ga$ae1$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[23 more quoted lines elided]…
>

I simply do not believe you about your assumptions.

You said [implicitly] that my post reminded you of the Wife of Bath 
inventing stories, presumably for entertainment. By extension, my 
observation seemingly had some sort of equivalence, in your mind, with 
on-the-fly fiction.

Then you ask for a citation by putting "Talmudic discussion" in scare 
quotes, a further implication that you are calling me out.

I gave you the citation.

You then digress on various transliteration schemes. Then quote a snippet 
from the tractate. Then wander off into freedom of association(?). Nowhere 
in your post was there a "thanks" or "Oops, I jumped to the wrong 
conclusion," or any other mollification.

In the future, if something seems odd to you, I suggest a simple "That 
sounds fascinating. Can you please provide a citation?" is less likely to 
engender ill-will than meanderings that decode as: "You'd lie when the truth 
sounded better. I dare you to prove that statement."
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-04T19:33:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ifvsn0$pu0$1@reader1.panix.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com> <ift4ga$ae1$1@reader1.panix.com> <eYOdnX02we36or7QnZ2dnUVZ_vOdnZ2d@earthlink.com>`

```
In article <eYOdnX02we36or7QnZ2dnUVZ_vOdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <waCdnWD7VNXCd7zQnZ2dnUVZ_qydnZ2d@earthlink.com>,
…[26 more quoted lines elided]…
>I simply do not believe you about your assumptions.

That might be due to the fact that I stated no assumptions, I stated a 
condition of being-reminded (associating).  The mechanisms and reasons for 
memory are, according to those who have studied such things, 
ill-understood and subject for marvel... did you know that memories can be 
recalled during surgery simply by touching a portion of the brain?

>
>You said [implicitly] that my post reminded you of the Wife of Bath 
>inventing stories, presumably for entertainment.

Please read carefully.  I said *explicitly* that I was reminded of the 
Wife of Bath's 'And you can look it up in your Almagest'.  I then 
explicitly asked for a citation; your presumptions are your own.

>By extension, my 
>observation seemingly had some sort of equivalence, in your mind, with 
>on-the-fly fiction.

By extension a mouse's neck is the equivalent of a giraffe's because they 
contain the same number of bones.  *I* barely know what goes on in my mind 
and I wonder at the accuracy of other folks' finding stuff in there such 
as 'equivalence' and 'presumption'.

>
>Then you ask for a citation by putting "Talmudic discussion" in scare 
>quotes, a further implication that you are calling me out.

My apologies if a few quotation marks caused you fright; I put them around 
'Talmudic discussion' because at that time the only evidence I had of such 
a thing being in the Talmud was that Some Guy on the UseNet Said It Was.

>
>I gave you the citation.
…[4 more quoted lines elided]…
>conclusion," or any other mollification.

That is because, I believe, that you were wrong.  In your version of 
Menachot 37a-b someone stated that a newborn was to be declared not 
subject to redemption fees whereas in the citation I gave (and link to 
Soncino text) the footnote clearly and unambiguously states that the 
newborn is considered subject to double-fees.

You stated the text said zero tax.  It is pointed out, with URLs, that the 
text states double tax.  Whom do you expect to admit error?

>
>In the future, if something seems odd to you, I suggest a simple "That 
>sounds fascinating. Can you please provide a citation?" is less likely to 
>engender ill-will than meanderings that decode as: "You'd lie when the truth 
>sounded better. I dare you to prove that statement."

Thanks e'er-so-much for your suggestion and rest assured that it will be 
given all the due consideration that it so richly appears to deserve.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 5)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-03T14:39:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cuqUo.86591$Ud7.16395@en-nntp-16.dc1.easynews.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com> <xu2dne7cMfvJe4rQnZ2dnUVZ_vKdnZ2d@earthlink.com> <fiflh6t8dnnu5qrpn7kpo2eoa27uv66ep3@4ax.com> <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com> <ifra4u$chb$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ifra4u$chb$1@reader1.panix.com...
> In article <6OCdnXNcg73pbILQnZ2dnUVZ_gSdnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[58 more quoted lines elided]…
>
<snip>
 What you describe (placing the item AFTER the ODO) is what happens with 
Micro Focus with NO-ODOSLIDE specified, i.e. the maxium size of the table is 
always "allocated".  SEARCH (and subscript checking) is based on the CURRENT 
size of the item, but the other items are allcoated after or with the 
maximum size.

This is not how any current (or past) IBM compiler works.
```

#### ↳ Re: Nested "Occurs Depending On"

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-12-27T21:52:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jadSo.99196$UC6.85137@en-nntp-08.dc1.easynews.com>`
- **References:** `<6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com>`

```
IBM Enterprise COBOL very definitely DOES allow for nested OCCURS DEPENDING 
on statements.  This is a (well documented) IBM extension.  Please provide 
the sample code and what compiler message you get.

This is EXPLICITLY disallowed by the '85 (and later) ANSI/ISO Standards.

Many "workstation" compilers also allow this as an extension.  See (for 
example) the Micro Focus "ODOSLIDE compiler directive.


"Pakku" <pakku@soccermail.com> wrote in message 
news:6c2b59b6-6235-46e9-87c5-6c54dc46f3db@glegroupsg2000goo.googlegroups.com...
> Why does MVS(zOS) Cobol not allow a nested OCCURS to be a DEPENDING ON?
>
> Is this some compiler limitation or machine limitation?  Or just an 
> arbitrary decision?
>
```

##### ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** pakku <pakku@artlover.com>
- **Date:** 2011-01-03T13:34:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ed3c68c7-15e1-45d8-9ccf-d0fffc43f07e@glegroupsg2000goo.googlegroups.com>`
- **In-Reply-To:** `<jadSo.99196$UC6.85137@en-nntp-08.dc1.easynews.com>`

```
Thanks all who replied.  I followed the link to the Cobol Language reference on Complex ODO which in turn pointed me to Appendix 2 of the Cobol Programming guide.  I can see where he talks about my situation (Bullet 3: "Table that has variable-length elements: A data item described by an OCCURS clause contains a subordinate data item describled by an OCCURS clause with the DEPENDING ON phrase")
But I couldn't determine what I was supposed to do different to handle this.

This is a snippet from the Compiler Listings that has the error message.  Due to the length limitations I'm afraid it's all wrapped around rather confusingly.

    01  LK-RRBF021.                                                     
        05  LK-COMM-SEND-TEST-OCCURS   PIC S9(03)   COMP-3.             
                                                                        
        05  LK-COMM-TEST-AREA  OCCURS 5 TIMES.                          
            10  LK-COMM-RTN-TEST-RET-CODE          PIC X(02).           
            10  LK-COMM-RTN-CPT-OCCURS           PIC S9(03)   COMP-3.   
            10  LK-COMM-RTN-CPT-BREAKDOWN      OCCURS 500 TIMES         
                             DEPENDING ON LK-COMM-RTN-CPT-OCCURS        
 ==000687==> IGYGR1263-S "OCCURS DEPENDING ON" object "LK-COMM-RTN-CPT-OCCURS" was defined as a 
                         table element.  The "DEPENDING ON" phrase was discarded. 
 ==000687==> IGYGR1116-S The "DEPENDING ON" object for table "LK-COMM-RTN-CPT-BREAKDOWN" was 
0                        invalid.  The "DEPENDING ON" phrase was discarded. 
                                   INDEXED BY LK-COMM-CPT-INDX.           
                15  LK-COMM-RTN-CPT-CODE           PIC X(06).
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2011-01-03T17:14:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4D220406.6F0F.0085.0@efirstbank.com>`
- **References:** `<ed3c68c7-15e1-45d8-9ccf-d0fffc43f07e@glegroupsg2000goo.googlegroups.com>`

```
Perhaps move LK-COMM-RTN-CPT-OCCURS (x) to a WS area outside of LK-RRBF021
and have the occurs depend on that field instead?

Frank
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-04T00:38:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iftq72$qgl$1@reader1.panix.com>`
- **References:** `<ed3c68c7-15e1-45d8-9ccf-d0fffc43f07e@glegroupsg2000goo.googlegroups.com>`

```
In article <ed3c68c7-15e1-45d8-9ccf-d0fffc43f07e@glegroupsg2000goo.googlegroups.com>,
pakku  <comp.lang.cobol@googlegroups.com> wrote:

[snip]

>    01  LK-RRBF021.                                                     
>        05  LK-COMM-SEND-TEST-OCCURS   PIC S9(03)   COMP-3.             
…[14 more quoted lines elided]…
>                15  LK-COMM-RTN-CPT-CODE           PIC X(06).                

LK-COMM-TEST-AREA occurs 5.  LK-COMM-RTN-CPT-OCCURS is subordinate to 
LK-COMM-TEST-AREA, meaning it occurs five times.

Which of these five initial values possible for LK-COMM-RTN-CPT-OCCURS is 
to be used to determine how many times LK-COMM-RTN-CPT-BREAKDOWN occurs?

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 4)_

- **From:** pakku <pakku@artlover.com>
- **Date:** 2011-01-04T14:17:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com>`
- **In-Reply-To:** `<iftq72$qgl$1@reader1.panix.com>`

```
OK- now I begin to understand what the problem is.  I didn't read the error message closely enough.  In the example in the programming guide, the DEPENDING ON was on a variable declared OUTSIDE the higher level OCCURS. (Like Frank suggested doing).

My situation is like so- Each Test is broken down into a different number of CPT-Codes, i.e the data store has a different number of children rows for each parent row.
I read the database and find that Test(1) has 4 CPTs
So I'd like to populate LK-COMM-RTN-CPT-OCCURS(1) with 4 and then create 4 occurrences of LK-COMM-RTN-CPT-BREAKDOWN below that
Test(2) has 10 CPTs
Then I'd like to populate LK-COMM-RTN-CPT-OCCURS(2) =10 and 10 occurrences of LK-COMM-RTN-CPT-BREAKDOWN below that and so on.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-04T22:47:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig081p$kso$1@reader1.panix.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com>`

```
In article <6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com>,
pakku  <comp.lang.cobol@googlegroups.com> wrote:
>OK- now I begin to understand what the problem is.  I didn't read the
>error message closely enough.  In the example in the programming guide,
…[11 more quoted lines elided]…
>occurrences of LK-COMM-RTN-CPT-BREAKDOWN below that and so on.

If that is what you'd like to do - and knowing, now, that the DEPENDING ON 
field cannot be a part of a field which OCCURS - then what prevents you 
from writing the code to do what you want?

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-06T02:11:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8oj901FetmU1@mid.individual.net>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <ig081p$kso$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com>,
…[8 more quoted lines elided]…
>> children rows for each parent row.

This describes a data structure commonly referred to as a "node". Techniques 
for processing nodes are pretty standard and generally involve recursion of 
the children.

Here's a description in English:

1. Access  a node root.

2. Access each child of that root  and process it, until no more children 
are returned. (if there are children of each child, recurse through them in 
exactly the same way, treating the current child as a "temporary root" and 
using the same process code. Repeat this to as many levels as there are 
children of children.

3. Move to the next node root.

4. Continue doing this until all roots (or the ones you are interested in, 
if you are accessing them randomly or filtering them) have been processed.


A very typical use of node structures would be in building a Treeview...

You don't know how many "branches" there may be at each level, and it could 
vary... (Trees don't have to be "balanced"...)

Once you recognise the structure and the recursive nature of the processing, 
you can see that there is absolutely NO NEED FOR OCCURS DEPENDING ON at 
all...

(The only exception to this would be where some deluded idiot has already 
created the structure as an ODO, instead of a normailzed set of repeating 
groups or node collection. If you have control over it, or it exists on a 
DB, there is NO reason at all to use ODO, and there are actually a good 
number of reasons NOT to do so... see other posts in this thread.)

Apart from consideration of implementations of ODO varying on different 
platforms, ANY ODO solution simply introduces complexity and cumbersome data 
storage management to what is essentially a simple and recognised data 
structure (NODE).

>> I read the database and find that Test(1) has 4 CPTs

"Test" is a table and CPT is a linked table?

CPTs are connected to "Test" by a foreign key, right? (A standard "repeating 
group" on a relational database. This supports any number of CPTs per 
"Test")

You have decided you want all the connected rows in a single data structure, 
defined in COBOL.   In fact, the data is already available in a normalized 
form (The repeating group (CPT) has been written to a separate table joined 
on a foreign key back to Test. (This constitutes 1st Normal form, and, 
coincidentally,also complies with 2nd and 3rd Normal form, because the key 
used to link the tables is unique). You could get what you appear to be 
wanting with a simple SQL Query:

SELECT  TestArea, CPTCode
FROM TestTable x, CPTTable y
WHERE x.KEY = y.KEY
GROUP BY TestArea

(Or somethng similar... there are minor differences in SQL depending on your 
RDBMS)

This should list the Test Areas with the CPTs for each one, irrespective of 
the number of them.



>> So I'd like to populate LK-COMM-RTN-CPT-OCCURS(1) with 4 and then
>> create 4 occurrences of LK-COMM-RTN-CPT-BREAKDOWN below that.

If you are really determined to have this in a COBOL data structure you are 
setting yourself a difficult task.

Here's the data structure you posted:

    01  LK-RRBF021.
        05  LK-COMM-SEND-TEST-OCCURS   PIC S9(03)   COMP-3.

        05  LK-COMM-TEST-AREA  OCCURS 5 TIMES.
            10  LK-COMM-RTN-TEST-RET-CODE          PIC X(02).
            10  LK-COMM-RTN-CPT-OCCURS           PIC S9(03)   COMP-3.
            10  LK-COMM-RTN-CPT-BREAKDOWN      OCCURS 500 TIMES
                             DEPENDING ON LK-COMM-RTN-CPT-OCCURS
 ==000687==> IGYGR1263-S "OCCURS DEPENDING ON" object 
"LK-COMM-RTN-CPT-OCCURS" was defined as a
                         table element.  The "DEPENDING ON" phrase was 
discarded.
 ==000687==> IGYGR1116-S The "DEPENDING ON" object for table 
"LK-COMM-RTN-CPT-BREAKDOWN" was
0                        invalid.  The "DEPENDING ON" phrase was discarded.
                                   INDEXED BY LK-COMM-CPT-INDX.
                15  LK-COMM-RTN-CPT-CODE           PIC X(06).

It is ugly, limited (500 occurrences hard coded in it), and unnecessary.

If your compiler doesn't support standard actions against NODE collections 
(Fujitsu does...), then you COULD build a "record" containing a given Test 
with its corresponding CPTs but you WOULDN'T  use ODO.

Instead you would recognise root and child nodes and use STRING to add them 
to a single "record" which is really just a big block (and can be defined as 
a variable length record in COBOL without any need for OCCURS...)

Consider this:

(WORKING-STORAGE)

    01  LK-COMM-TEST-AREA.  *> root node
            10  LK-NODE-KEY              (whatever field(column) is used to 
join the Test and CPT tables on the RDB.)
            10  LK-COMM-RTN-TEST-RET-CODE          PIC X(02).

    01  LK-COMM-CPT.  *> child node.
                  15  LK-COMM-RTN-CPT-CODE           PIC X(06).



(FILE SECTION)

01 LK-OUT-RECORD   PIC X(32000) <or whatever...> SELECT  NODE-FILE has it as 
VARYING FROM 1 TO 32000.


(PROCEDURE DIVISION)

(Get the Test row from the DB)
...

  INITIALIZE-NODE-OUTPUT.
           MOVE SPACES TO LK-OUT-RECORD.

 CREATE-NODE-FILE.

           PERFORM PROCESS-NODES  UNTIL DB-FINISHED
           WRITE LK-OUT-RECORD
           CLOSE NODE-FILE

PROCESS-NODES.
           PERFORM STRING-ROOT-NODE
           PERFORM STRING-CHILD-NODE UNTIL  DB-CPT-FINISHED
           ...


STRING-ROOT-NODE.
           (GET "TEST" ROW FROM DB INTO LK-COMM-TEST-AREA ...)
           IF NOT DB-FINISHED
                STRING LK-OUT-RECORD
                                DELIMITED BY SPACE
                          LK-COMM-TEST-AREA
                                DELIMITED BY SPACE
                          (ADD A "NODE DELIMITER" CHARACTER HERE IF YOU WANT 
ONE...)
                                        INTO LK-OUT-RECORD
               END-STRING
          END-IF
         ...

STRING-CHILD-NODE.
           (GET "CPT" ROW FROM DB INTO LK-COMM-CPT...      Check for a 
change of key on the CPT rows as well as physical end)
           IF NOT CPT-FINISHED
                STRING LK-OUT-RECORD
                                DELIMITED BY SPACE
                          LK-COMM-CPT
                                DELIMITED BY SPACE
                          (ADD A "NODE DELIMITER" CHARACTER HERE IF YOU WANT 
ONE...)
                                        INTO LK-OUT-RECORD
               END-STRING
          END-IF
         ...


The above is VERY basic code and is designed to illustrate a concept, not to 
be implemented.

Having considered the very basic NODE processing above, it might occur to 
you that this is just a pale imitation of XML processing.

XML is a NODE structure and perfectly fits your requirement.

If I were you, I 'd read the Database and provide the NODE structure as an 
XML file. This is transportable across platforms and can be encoded and 
decoded using existing standard software, that can be called from COBOL. An 
XML handler will automatically encode your nodes so that they can be read by 
any XML editor. If a report is required it can be produced using standard 
tools like Crystal Reports, specifying the XML file as the data source.

The LAST thing you need is COBOL ODO.

Pete.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 7)_

- **From:** pakku <pakku@artlover.com>
- **Date:** 2011-01-05T13:33:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`
- **In-Reply-To:** `<8oj901FetmU1@mid.individual.net>`

```
Thanks Pete for a detailed note on the best way to do this.  Your surmise about the data structure is correct.
I have some constraints which might prevent me from doing this the optimal way.
a) There exists a subroutine that gets me the CPT codes for a Test.  The process of going from Test to CPT is not that straightforward hence a subroutine for this purpose.  I have to use this.
b) This subroutine has a linkage section that is defined as capable of accepting 1 to 75 tests using ODO and returning a fixed 500 CPTs per test.   
05  LK-SEND-TEST-OCCURS               PIC S9(03)   COMP-3.
05  LK-TEST-AREA  OCCURS 1 TO 75 TIMES
                  DEPENDING ON LK-SEND-TEST-OCCURS
                  INDEXED BY LK-TEST-INDX.
    10  LK-RTN-TEST-PRICE             PIC S9(5)V99 COMP-3.
    10  LK-RTN-CPT-OCCURS             PIC S9(03)   COMP-3.
    10  LK-RTN-CPT-BREAKDOWN      OCCURS 500 TIMES
                                  INDEXED BY LK-CPT-INDX.

c) I am writing a Web Service using CICS that will call this subroutine.  If the Interface Area for the Web Service Cobol Program that calls this  subroutine were the same format as the subroutine's own linkage section, then the XML file that is sent back to the client is going to be unnecessarily huge since it's going to have a bunch of "empty" entries.

So to answer Richard's question- I'm not trying to save memory here, but trying to minimise the amount of data being sent back to the client.

d) If I set up an interface copybook for just 1 Test-Area with the CPT-Breakdown occuring from 1 to 500 then the returned XML document doesn't have any "empty" entries.
e) I was hoping to be able to do the same but with more than 1 Test-Area, the 5 was just a random choice.  I could have used 75 if I wanted to.

If I used STRING and created a long record of CPT Breakdowns for each Test, then wouldn't I have to parse it and add back the tags for XML?
Right now the Web Service tools at my disposal save me the trouble of creating an XML document.  The tools use the OCCURS clauses in the interface copybook to create the CPT Breakdown elements in the XML.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-05T16:48:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig2ovp$tll$1@news.eternal-september.org>`
- **In-Reply-To:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`

```
On 1/5/2011 4:33 PM, pakku wrote:
> Thanks Pete for a detailed note on the best way to do this.  Your surmise about the data structure is correct.

...snipped most of post


You should consider 'replying' to the post that you refer to [as I have 
just done] - thereby maintaining the "thread" - rather than creating a 
new post with a similar title. The presence of "re:" in the subject is 
normally not sufficient for relating your post to other similar posts 
(in most newsreaders).

cheers
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-05T14:07:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87bfe013-44a8-4c94-9fd1-378d790c31ef@u25g2000pra.googlegroups.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com> <ig2ovp$tll$1@news.eternal-september.org>`

```
On Jan 6, 10:48 am, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/5/2011 4:33 PM, pakku wrote:
>
…[8 more quoted lines elided]…
> (in most newsreaders).

On Google groups his reply is located correctly and is not a 'new
post'. Perhaps you should consider a better newsreader.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 10)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2011-01-06T13:37:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d25b776$0$23754$14726298@news.sunsite.dk>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com> <ig2ovp$tll$1@news.eternal-september.org> <87bfe013-44a8-4c94-9fd1-378d790c31ef@u25g2000pra.googlegroups.com>`

```
Richard wrote:

> On Jan 6, 10:48ï¿œam, Kerry Liles
> <"kerry.liles[minus_the_spam]"@gmail.com> wrote:
…[14 more quoted lines elided]…
> post'. Perhaps you should consider a better newsreader.

A webbrowser cannot be compared with a newsreader. And while some may
prefer to use Google groups for NNTP (reading and/or writing) Kerry hit
the nail on the head with his comments as not everybody is assumed to
be willing to substitute proven newsreaders with Google groups.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 11)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-01-06T12:07:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kltbi6t5qhukjgigkgb95c7m558qj93np2@4ax.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com> <ig2ovp$tll$1@news.eternal-september.org> <87bfe013-44a8-4c94-9fd1-378d790c31ef@u25g2000pra.googlegroups.com> <4d25b776$0$23754$14726298@news.sunsite.dk>`

```
On Thu, 06 Jan 2011 13:37:09 +0100, Fred Mobach <fred@mobach.nl>
wrote:

>Richard wrote:
>
…[21 more quoted lines elided]…
>be willing to substitute proven newsreaders with Google groups.

Frankly, I hate Google Groups.  I much prefer using a newsreader
(Agent).

Regards,
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 9)_

- **From:** pakku <pakku@artlover.com>
- **Date:** 2011-01-05T18:39:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91bc12b8-ee92-46cd-a545-731c6df42847@l22g2000vbp.googlegroups.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com> <ig2ovp$tll$1@news.eternal-september.org>`

```
On Jan 5, 4:48 pm, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/5/2011 4:33 PM, pakku wrote:
>
…[10 more quoted lines elided]…
> cheers

Kerry,
I use Google Groups never having come to grips with Forte.  And I know
I replied directly to Pete's post.  So I'm not sure why you are not
seeing it threaded.  I'm directly replying to your post now- hopefully
it will show up correctly
Sorry!
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 10)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-06T09:34:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig4jsq$3o3$1@news.eternal-september.org>`
- **In-Reply-To:** `<91bc12b8-ee92-46cd-a545-731c6df42847@l22g2000vbp.googlegroups.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com> <ig2ovp$tll$1@news.eternal-september.org> <91bc12b8-ee92-46cd-a545-731c6df42847@l22g2000vbp.googlegroups.com>`

```
On 1/5/2011 9:39 PM, pakku wrote:
> On Jan 5, 4:48 pm, Kerry Liles
> <"kerry.liles[minus_the_spam]"@gmail.com>  wrote:
…[19 more quoted lines elided]…
> Sorry!

Thanks!! No need to be sorry - it was meant as a gentle reminder 
(although some folks might not have thought that the case...) This reply 
of yours is properly threaded, so I don't know what might be going on. 
FWIW, I am using Thunderbird 3.1.7 on Windows XP. It has some odd quirks 
about it, but it seems to get the threading right (most of the time!)

Regardless, the content of your messages is important over all; I should 
have sent you an email about the threading (or just sucked it up!)

Have a great day.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-07T03:04:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8om0gdFj1qU1@mid.individual.net>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`

```
pakku wrote:
> Thanks Pete for a detailed note on the best way to do this.  Your
> surmise about the data structure is correct.

Good. The main reason I responded to you was because you explained your 
problem well (with examples) and because I REALLY HATE ODO!

(Not that I would ever get emotional about computer code, you understand... 
;-))

> I have some constraints which might prevent me from doing this the
> optimal way.
…[5 more quoted lines elided]…
> per test.

Ah, I see...(So the calling program has the same structure defined in WS or 
ITS LS?)

> 05  LK-SEND-TEST-OCCURS               PIC S9(03)   COMP-3.
> 05  LK-TEST-AREA  OCCURS 1 TO 75 TIMES
…[6 more quoted lines elided]…
>           15 LK-RTN-CPT                       PIC X(6).

This is the exception I referred to previously. You are stuck with what has 
already been done. However, it is not as black as it looks... (To be fair, 
this may be the only way it can be done in COBOL; I honestly don't know, 
because I'm not dealing with CICS web services.)

The LINKAGE Section actually occupies no space at all. This suggests a 
solution outlined below...


> c) I am writing a Web Service using CICS that will call this
> subroutine.  If the Interface Area for the Web Service Cobol Program
…[3 more quoted lines elided]…
> bunch of "empty" entries.

Yes, you're absolutely right about the emptiness, but the overall size is 
not SO bad. It will be (75 x 6)  = 450  + (75 x 500 x 6) = 225000... 
er...lots

In context, you probably wouldn't hesitate to attach a 225K jpg to an email 
and send it over the net...

Still, as I'm writing web services quite a lot lately I understand your 
point and I would be looking hard for ways to make it smaller, just as you 
are...
>
> So to answer Richard's question- I'm not trying to save memory here,
> but trying to minimise the amount of data being sent back to the
> client.

A noble aspiration :-)

I take it "the XML being sent back to the client" is SOAP? As far as I know 
there is no way to provide a variable length SOAP field other than with a 
string, or by manipulating the WSDL (there are MAX and MIN tags available). 
BUT, I would expect the code writing the SOAP to NOT write "empty" entries. 
In fact, it should suppress generation (including tags) altogether if it has 
nothing to say...

It's a long time (30 years :-)) since I used CICS but I understand that it 
now contains routines which allow it to generate SOAP/WSDL for web services. 
Depending how comprehensive these facilities are, it should be possible to 
tell the routine that the generated XML is not to have tags generated for 
"empty" entries and that variable strings are not to be padded.

Have a read of this: 
http://www-01.ibm.com/support/docview.wss?uid=swg21248612

If it is a bit too deep see if you can get into the Web Service and see how 
it talks to CICS


> d) If I set up an interface copybook for just 1 Test-Area with the
> CPT-Breakdown occuring from 1 to 500 then the returned XML document
> doesn't have any "empty" entries.

Yes, that is what I would expect. There is only one variable field and the 
WSDL generated by CICS knows not to pad it. When you add more occurrences of 
TEST, the block being passed is larger (because ODO always allocates the 
maximum size). What you need is to get it closer to a "dynamic allocation" 
(COBOL is hopeless at this, but CICS isn't...)


> e) I was hoping to be able to do the same but with more than 1
> Test-Area, the 5 was just a random choice.  I could have used 75 if I
> wanted to.

In fact, you actually WANT 75 as an ODO :-)

I have a possible solution to this but don't beat me up if it doesn't 
work... :-) I'm not working in a mainframe environment so I can't test it.

If I understand correctly you have a COBOL Web Service which calls a 
subroutine and gets back the block you have defined. The subroutine doesn't 
generate the XML, does it? It is the program which calls it?

The WSDL for the service defines the shape of the XML and you are correct 
that if it just uses the same interface as was passed to the subroutine, the 
data transmitted over the wire will be too large.

Presumably, you can control the SOAP, as this is being generated in the 
program which calls the subroutine? The SOAP has to comply with the WSDL 
used to define the data transfer (XML). Probably you generate the WSDL using 
CICS and passing it the interface block definition? (I'm not sure about this 
because CICS never had this facility when I was programming mainframes.) 
This, in effect, defines your Web Service.

If any of this is wrong, please clarify. Given that it is so (or generally 
correct), here's a thought...

Although the SOAP is being generated currently from the same interface block 
that was passed to the CPT subroutine, it actually doesn't HAVE to be.

Why not define the interface in the calling program exactly as it is defined 
in the subroutine (always a good move and it guarantees no interface 
problems), but DON'T pass this interface down the wire to the client?

Instead define a more dynamic structure as follows:

(WORKING-STORAGE)

01 SOAP-STRUCTURE.
 05  SOAP-SEND-TEST-OCCURS               PIC S9(03)   COMP-3.
 05  SOAP-TEST-AREA  OCCURS 1 TO 75 TIMES
                   DEPENDING ON WS-TEST-COUNT
                   INDEXED BY SOAP-TEST-INDX.
     10  SOAP-RTN-TEST-PRICE             PIC S9(5)V99 COMP-3.
     10  SOAP-RTN-CPT-OCCURS             PIC S9(03)   COMP-3.
     10  SOAP-RTN-CPT-BREAKDOWN      OCCURS 500 TIMES
                   DEPENDING ON WS-CPT-COUNT
                   INDEXED BY SOAP-CPT-INDX.
           15   SOAP-RTN-CPT   PIC X(6).

01  WS-TEST-COUNT  PIC S9(3) COMP-3.
01  WS-CPT-COUNT    PIC S9(3) COMP-3.

01  WS-CPT-MAX    PIC S9(3) COMP-3   VALUE ZERO.

01   WS-SOAP-PTR USAGE POINTER.
01   WS-SOAP-LENGTH   PIC S9(8) BINARY.

01    SUBSCRIPTS USAGE COMP-3.
        12 J   PIC S9(3).
        12 K  PIC S9(3).
...

Make sure the WSDL is generated from the SOAP-STRUCTURE, above.

Now "all ya gotta do is"   load THIS structure  with the data from the 
interface block passed to the CPT subroutine, and then send it down the 
wire. Because this needs to be a dynamic structure it would make sense to 
move it to LINKAGE (where it actually occupies no space,) ask CICS to 
allocate a chunk of memory to it, and set the address of that chunk of 
memory as what you pass down the line to the Client.

Summarising:

1. Call the CPT routine using the "large" definition it is expecting. It 
returns into the same area. (WS in the calling program).
2.  Load the SOAP-STRUCTURE in WS of the calling program from the interface 
block returned by the CPT subroutine.

Here's some sample code:

(PROCEDURE DIVISION)

LOAD-SOAP-STRUCTURE.
        PERFORM
                VARYING SOAP-TEST-INDX
                         FROM 1
                               BY 1
                         UNTIL  SOAP-TEST-INDX >  LNK-SND-TEST-OCCURS
                 AFTER    LK-CPT-INDX
                         FROM 1
                               BY 1
                         UNTIL  LK-RTN-CPT (LK-CPT-INDX) =  SPACES
                              *> SYNCHRONIZE THE 2 STRUCTURES

                               SET J TO SOAP-TEST-INDX
                               SET LK-TEST-INDX TO J
                               SET J TO LK-CPT-INDX
                               SET SOAP-CPT-INDX TO J

                              IF WS-CPT-MAX < SOAP-CPT-INDX
                                         SET WS-CPT-MAX TO SOAP-CPT-INDX
                              END-IF

                              *> SET THE SOAP DEPENDENCY VALUES

                              SET WS-TEST-COUNT TO SOAP-TEST-INDX
                              SET  WS-CPT-COUNT TO SOAP-CPT-INDX

                              *> MOVE THE DATA

                               MOVE LK-RTN-CPT (LK-TEST-INDX, LK-CPT-INDX) 
TO
                                            SOAP-RTN-CPT (SOAP-TEST-INDX, 
SOAP-CPT-INDX)
          END-PERFORM
          *> SET THE MAXIMUM CPT OCCURRENCE VALUE THAT WAS ENCOUNTERED
          *> INTO THE DYNAMIC SOAP STRUCTURE. THE MAXIMUM TEST VALUE  IS
          *> ALREADY  SET...

          MOVE  WS-CPT-MAX   TO WS-CPT-COUNT

          *> THE SOAP STRUCTURE IS NOW LOADED DYNAMICALLY AND CAN BE
          *> SENT TO THE CLIENT

3.  Move the SOAP-STRUCTURE to the LINKAGE SECTION. (It takes no space). On 
reflection, it would probably be OK to define the SOAP-STRUCTURE in LINKAGE 
SECTION, but the WS fields for ODO must be in WS. Use the LENGTH function to 
find out how long it is...

          MOVE LENGTH OF SOAP-STRUCTURE TO WS-SOAP-LENGTH

4. Ask CICS for some memory for it. (GETMAIN)

          EXEC CICS GETMAIN
               BELOW
               USERDATAKEY
               SET(WS-SOAP-PTR)
               FLENGTH(WS-SOAP-LENGTH)
         END-EXEC
         SET ADDRESS OF SOAP-STRUCTURE TO  WS-SOAP-PTR

That should give you a pseudo dynamic structure that will support as many 
TESTs as there actually were and the maximum number of CPTs actually 
encountered, for each TEST, rather than the fixed 500. (So it still isn't 
perfect because it can never be truly dynamic as long as it is based on 
ODO). I do something similar in C# and it is EXACTLY as large as it needs to 
be... COBOL is simply not intended for the Network, and trying to make it do 
Network stuff by fudging it with CICS and ODO is like putting lipstick on a 
pig.

Don't forget to issue CICS FREEMAIN once you have sent it :-)

> If I used STRING and created a long record of CPT Breakdowns for each
> Test, then wouldn't I have to parse it and add back the tags for XML?

Probably... I'm not sure because I don't know whether you write your own 
WSDL or CICS is doing it. I think we can safely discard that solution 
anyway.

> Right now the Web Service tools at my disposal save me the trouble of
> creating an XML document.  The tools use the OCCURS clauses in the
> interface copybook to create the CPT Breakdown elements in the XML.

OK, that sounds fine.

I have taken more time than I really should have to do this because it is an 
interesting exercise in COBOL and it gives me a break from some of the other 
stuff I am currently grappling with. :-)

I hope it is of some help.

Pete.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2011-01-07T21:47:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l9gfi6p1940lsg28sounuj0st1lvtsce0c@4ax.com>`
- **References:** `<8oj901FetmU1@mid.individual.net> <c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`

```
On Wed, 5 Jan 2011 13:33:41 -0800 (PST), pakku <pakku@artlover.com>
wrote:

>Thanks Pete for a detailed note on the best way to do this.  Your surmise about the data structure is correct.
>I have some constraints which might prevent me from doing this the optimal way.
…[19 more quoted lines elided]…
>Right now the Web Service tools at my disposal save me the trouble of creating an XML document.  The tools use the OCCURS clauses in the interface copybook to create the CPT Breakdown elements in the XML.

From this posting, I assume this project is for something running on
an IBM z series under zOS.  If so the current COBOL compiler has
significant XML capability an the next most current still had a fair
amount of it.  Rather than fiddling with OCCURS DEPENDING ON, I would
look at the XML tools available in the shop.  For the internal
processing just use the maximum size tables needed with counters that
tell the actual number of entries used.

Clark Morris
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** Chuck H <none@none.com>
- **Date:** 2011-03-06T16:44:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G7Ucp.71955$4c7.68187@newsfe06.iad>`
- **In-Reply-To:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`
- **References:** `<c2c5ecf1-d9fa-48cc-88fa-d8268b473ebe@glegroupsg2000goo.googlegroups.com>`

```
On 1/5/2011 15:33, pakku wrote:
> Thanks Pete for a detailed note on the best way to do this.  Your surmise about the data structure is correct.
> I have some constraints which might prevent me from doing this the optimal way.
…[19 more quoted lines elided]…
> Right now the Web Service tools at my disposal save me the trouble of creating an XML document.  The tools use the OCCURS clauses in the interface copybook to create the CPT Breakdown elements in the XML.


Pakku,

another way to accomplish this and reduce the memory requirement would 
be do use an "indirection table" as follows.

<code>
        01  LK1-TBL-1.
            05  LK1-ENTRIES-USED            PIC S9(4)   COMP.
            05  LK1-ENTRY    OCCURS 0 TO 75 TIMES
                               DEPENDING ON LK1-ENTRIES-USED
                               ASCENDING KEY IS LK1-KEY
                               INDEXED BY LK1-INDEX.
                10  LK1-KEY.
                    15  LK-RTN-TEST-PRICE   PIC S9(5)V99 COMP-3.
                    15  LK-RTN-CPT-OCCURS   PIC S9(03)   COMP-3.
                10  LK1-LK2-INDEX           USAGE INDEX.
                10  LK1-LK2-COUNT           PIC S9(4)  COMP.

        01  LK2-TBL-BREAKDOWNS.
            05  LK2-ENTRY     OCCURS 32000 TIMES
                                INDEXED BY LK2-INDEX.
                10  LK2-BREAKDOWN-FLD-1     PIC X(4).
                10  LK2-BREAKDOWN-FLD-2     PIC S9(5)   COMP-3.
                10  LK2-BREAKDOWN-FLD-3     PIC X(4).
                10  LK2-BREAKDOWN-FLD-4     PIC S9(8)   COMP.

</code>


I've used this technique successfully to minimize resources used. Also 
at the same time it provides very efficient access to the data via the 
indexes. This code is from a Z/OS environment.


Chuck Haatvedt


email   concatenate the following strings

       c + (my last name) + 1 @ charter.net
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-04T15:34:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com>`

```
On Jan 5, 11:17 am, pakku <pa...@artlover.com> wrote:
> OK- now I begin to understand what the problem is.  I didn't read the error message closely enough.  In the example in the programming guide, the DEPENDING ON was on a variable declared OUTSIDE the higher level OCCURS. (Like Frank suggested doing).
>
…[4 more quoted lines elided]…
> Then I'd like to populate LK-COMM-RTN-CPT-OCCURS(2) =10 and 10 occurrences of LK-COMM-RTN-CPT-BREAKDOWN below that and so on.

A decade or three ago there may have been a point to doing it that
way: saving disk space on a 20MegaByte drive, for example, or being
limited in the number of files that can be opened.

What assurance do you have that there are not more CPT than you have
allowed for in your OCCURS ? Or indeed that there are not more tests
than in the higher OCCURS ?

Why are you not storing the data in a normalised form with separate
files for the tests and the CPTS each keyed adequate to relate them ?
It would seem to me to be far less complicated and could cater for
almost unlimited tests, and it has the bonus of working.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-05T01:26:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig0hcp$k4n$1@reader1.panix.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com>`

```
In article <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:

[snip]

>What assurance do you have that there are not more CPT than you have
>allowed for in your OCCURS ? Or indeed that there are not more tests
>than in the higher OCCURS ?

Disproving logical negatives can be a dicey thing, Mr Plinston.

>
>Why are you not storing the data in a normalised form with separate
>files for the tests and the CPTS each keyed adequate to relate them ?

These may be wild guesses, Mr Plinston, but the answer might be along the 
lines of 'the specs don't allow for that' or 'the person who signs my 
timesheet wants to see it this way'.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-05T23:56:13+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8oj12fFurkU1@mid.individual.net>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com> <ig0hcp$k4n$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com>,
…[8 more quoted lines elided]…
> Disproving logical negatives can be a dicey thing, Mr Plinston.

So can proving them, but, if the need arises... :-)
>
>>
>> Why are you not storing the data in a normalised form with separate
>> files for the tests and the CPTS each keyed adequate to relate them ?

This is an infinitely superior "generic" solution than trying to map 
OCCURrences.

Given that the technology for normalized repeating groups of ANY size is 
readily available, I too have difficulty in understanidng why anyone would 
want to use a stulted solution like ODO (which is arguably obsolete, never 
at any time delivered what programmers hoped it would (a dynamically 
allocated variable length array in COBOL), and, at least in my book, is 
"best avoided". To consider nested ODO, even if it is technically available, 
just seems like compounding what is a dreadful solution to start with.

>
> These may be wild guesses, Mr Plinston, but the answer might be along
> the lines of 'the specs don't allow for that' or 'the person who
> signs my timesheet wants to see it this way'.

The specs. allow for whatever solves the problem, unless they are being 
specified to the level of  program code. (It has been many years since this 
level of specification was considered a "Good Thing"; the person writing the 
spec. might as well write the code and thereby ensure that it is a perfect 
match to one person's pre-conceived idea of what constitutes "good" COBOL 
code.) I believe the spec. is functional, rather than program code level.

I further believe that the "person who signs the OP's timesheet" wants a 
solution.

A quick review of the posts in this thread shows that using ODO in COBOL is 
simply a poor solution.

Using normalized repeating groups is a much better one and you can still 
implement it in COBOL if you are desperate to do that.


Pete.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-05T14:56:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig20rg$hvt$1@reader1.panix.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com> <ig0hcp$k4n$1@reader1.panix.com> <8oj12fFurkU1@mid.individual.net>`

```
In article <8oj12fFurkU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article
…[11 more quoted lines elided]…
>So can proving them, but, if the need arises... :-)

If the need arises, Mr Dashwood, it might be met... or might not; such is 
a definition of 'dicey' ( http://dictionary.reference.com/browse/dicey , 
'unpredictable, risky, uncertain')

[snip]

>> These may be wild guesses, Mr Plinston, but the answer might be along
>> the lines of 'the specs don't allow for that' or 'the person who
…[3 more quoted lines elided]…
>specified to the level of  program code.

Have you seen the specs, Mr Dashwood?  I haven't, hence my use of 'might 
be along the lines of'.  

(On a side note... is a spec which reads 'expand Linkage Section to allow 
for five occurrences' one which 'specifies to the level of program code'?)

>(It has been many years since this 
>level of specification was considered a "Good Thing"; the person writing the 
>spec. might as well write the code and thereby ensure that it is a perfect 
>match to one person's pre-conceived idea of what constitutes "good" COBOL 
>code.) I believe the spec. is functional, rather than program code level.

Some believe that pink unicorns live in underground cities on the far side 
of the moon, Mr Dashwood... until evidence can be had I find it best to 
remain in the realm of 'it is possible that/might be'.

>
>I further believe that the "person who signs the OP's timesheet" wants a 
>solution.

Pink unicorns with yellow tails and blue eye-shadow?  Again, Mr Dashwood, 
belief in absence of evidence.

>
>A quick review of the posts in this thread shows that using ODO in COBOL is 
>simply a poor solution.

A long, slow review of my experiences has shown the value of making the 
person who has the responsibility for signing the checks for the system.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-06T16:59:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8okt0pFljfU1@mid.individual.net>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com> <ig0hcp$k4n$1@reader1.panix.com> <8oj12fFurkU1@mid.individual.net> <ig20rg$hvt$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8oj12fFurkU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[30 more quoted lines elided]…
> 'might be along the lines of'.

As neither of us have seen the specs, "might be along the lines of" is just 
as useful as "specs allow for whatever solves the problem".

Both are speculative.
>
> (On a side note... is a spec which reads 'expand Linkage Section to
> allow for five occurrences' one which 'specifies to the level of
> program code'?)

Yes.

If it said: "Make sure that the program can cope with at least 5 
occurrences." then, no.
>
>> (It has been many years since this
…[8 more quoted lines elided]…
> best to remain in the realm of 'it is possible that/might be'.

Or, we might just consider that people who believe that have a different 
view of reality and not waste our time looking for things which only they 
can perceive. I see no point in staying "in the realm of 'it is possible 
that/might be' , when it clearly isn't. I limit that realm to things which 
are at least possible, in my opinion. As a sometime student of Physics, Doc, 
you should be well aware of the difference between a "small, but finite" 
probability, and a probability of zero...



>>
>> I further believe that the "person who signs the OP's timesheet"
…[3 more quoted lines elided]…
> Dashwood, belief in absence of evidence.

The evidence is that everyone who ever signed my Timesheet wanted a 
solution. People who didn't provide one tended not to get their Timesheets 
signe, or even have their contracts renewed...
>
>>
…[5 more quoted lines elided]…
> system.

I think some words may have been omitted in that last, but I catch your 
drift. Yes, keeping employers happy is not something I would argue against. 
We might have different opinions about HOW you do it.

Pete.
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-06T16:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig4oud$4f4$1@reader1.panix.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <8oj12fFurkU1@mid.individual.net> <ig20rg$hvt$1@reader1.panix.com> <8okt0pFljfU1@mid.individual.net>`

```
In article <8okt0pFljfU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8oj12fFurkU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>> A quick review of the posts in this thread shows that using ODO in
>>> COBOL is simply a poor solution.
…[7 more quoted lines elided]…
>We might have different opinions about HOW you do it.

Hmmmm... this might fall into the realm of Style Wars, We Agree So One of 
Us Must Be Wrong, or something else, entire.

DD
```

###### ↳ ↳ ↳ Re: Nested "Occurs Depending On"

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-05T14:07:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9n9i69lnanlof56q7d08sl21fvm736rtp@4ax.com>`
- **References:** `<6f1a9e6a-1383-4252-9bfc-e7a605aae74f@glegroupsg2000goo.googlegroups.com> <20a666d4-0ca5-493f-8330-ccdb2f4174f4@e16g2000pri.googlegroups.com>`

```
On Tue, 4 Jan 2011 15:34:41 -0800 (PST), Richard <riplin@Azonic.co.nz>
wrote:

>A decade or three ago there may have been a point to doing it that
>way: saving disk space on a 20MegaByte drive, for example, or being
>limited in the number of files that can be opened.

Over the years, my workplaces have migrated from variable length
records to header and body records to external databases as disk space
became cheaper and cheaper relative to other expenses - especially
labor.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
