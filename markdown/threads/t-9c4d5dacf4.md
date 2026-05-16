[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Printing in Columns

_22 messages · 11 participants · 2004-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Printing in Columns

- **From:** "Yiorgo Terzis" <gnterzis@otenet.gr>
- **Date:** 2004-08-24T19:42:37+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
Is it possible to print data in columns using only native PC_... routines ?
The known problem is the shifting of a column to the left or right
according to the data of the previous column.
Is it any way to avoid this problem ?
I would appreciate any idea.
Note. I want to avoid using tools such as RPV, CobView, TurboReports etc.


Yiorgo Terzis.
```

#### ↳ Re: Microfocus Printing in Columns

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-08-24T13:06:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zFKWc.19623$DG.731716@news20.bellglobal.com>`
- **In-Reply-To:** `<cgfr5v$2an$1@usenet.otenet.gr>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
Yiorgo Terzis wrote:
> Is it possible to print data in columns using only native PC_... routines ?
> The known problem is the shifting of a column to the left or right
…[8 more quoted lines elided]…
> 

Just go to a fixed size font.

Donald
```

##### ↳ ↳ Re: Microfocus Printing in Columns

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-08-25T02:38:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<412BFB6B.3070809@optonline.net>`
- **In-Reply-To:** `<zFKWc.19623$DG.731716@news20.bellglobal.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <zFKWc.19623$DG.731716@news20.bellglobal.com>`

```
Donald Tees wrote:
> Yiorgo Terzis wrote:
> 
…[16 more quoted lines elided]…
> 

And, perhaps, edit the numbers into a fixed size output field that will 
avoid the problem with fixed founts, also.

Warren Simmons
```

#### ↳ Re: Microfocus Printing in Columns

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-24T18:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<irLWc.198225$M95.197768@pd7tw1no>`
- **In-Reply-To:** `<cgfr5v$2an$1@usenet.otenet.gr>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
Yiorgo Terzis wrote:

>Is it possible to print data in columns using only native PC_... routines ?
>The known problem is the shifting of a column to the left or right
…[10 more quoted lines elided]…
>
If Donald's answer of going fixed font is your solution - go for it. But 
I'm getting kind of leery about answering questions like yours, without 
more specific detail. Somebody asked a question, I thought I gave him a 
neat solution. Not so. He is Italian and his reply,  "Sorry James. My 
English is not good. I'm talking about the Data File Editor". Had I 
known it *was* the DFE - I wouldn't have attempted to answer - I've 
never used it !

Assuming you want more info - go to Micro Focus site and sign up for 
Answer Exchange (freebie) and post your question under Net Express. But 
*PLEASE* be specific - illustrate what your current problem is., say, 
some sample print lines. Using PC-PRINT it is possible to use different 
styles, fonts *all* in one line.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Microfocus Printing in Columns

- **From:** "Yiorgo Terzis" <gnterzis@otenet.gr>
- **Date:** 2004-08-24T21:58:28+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgg34p$7l5$1@usenet.otenet.gr>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no>`

```

? "James J. Gavan" <jjgavan@shaw.ca> ?????? ??? ??????
news:irLWc.198225$M95.197768@pd7tw1no...
> Yiorgo Terzis wrote:
>
> >Is it possible to print data in columns using only native PC_... routines
?
> >The known problem is the shifting of a column to the left or right
> >according to the data of the previous column.
…[24 more quoted lines elided]…
> Jimmy, Calgary AB

Thank you both for your replies.

I do not want to restrict printings only to fixed font.

I am developing a program from which, among others, the user will design the
form of labels
to print. The problem is to left align labels of a second or third column.

Any case, I will try with Microfocus site.
Thanks.
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-24T15:41:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408241441.4698d676@posting.google.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no> <cgg34p$7l5$1@usenet.otenet.gr>`

```
"Yiorgo Terzis" <gnterzis@otenet.gr> wrote

> I do not want to restrict printings only to fixed font.

Then you must devise a mechanism that caters for specific placement of
data items by x and y co-ordinates measured in ems or similar.
 
> I am developing a program from which, among others, the user will design the
> form of labels
> to print. The problem is to left align labels of a second or third column.

You probably need a forms design tool such as FormPrint (Flexus) or
PowerForm (Fujitsu).  But then the user needs to buy the tool to
create their own versions of the labels.

I used JetForm for a number of years, specifically the JFMerge
product.  The Cobol program writes out a merge file with the data
items and then runs the merge program against the graphical template
to create the printout.

I then developed a simple merge program (in C as it happens) which can
take a postscript template and merge using the same sort of merge data
file as I output for JFMerge.  The postscript can be created using a
variety of freely available design tools (though some aren't suitable
for various reasons), such as impress on Linux (not the impress from
OO.o).  As Linux uses postscript as the common printing system the
print drivers all handle this even if the printer doesn't cope with it
natively.
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-25T00:05:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RIQWc.32727$9Y6.7350@newsread1.news.pas.earthlink.net>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no> <cgg34p$7l5$1@usenet.otenet.gr> <217e491a.0408241441.4698d676@posting.google.com>`

```
Although not a part of the '85 or '02 COBOL Standards, there is one vendor that
provides support for "fonts" with PC COBOL compilers using the Report Writer
feature.  This might (or might not) do what you want.  Check out:

 http://www.spc-systems.com/tutorial/tutorial_cobrwr3.htm#chap6s06p0

for some of what is available (via a COBOL add-on product)
```

##### ↳ ↳ Re: Microfocus Printing in Columns

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-24T16:34:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4wOWc.29589$5s3.9281@fe40.usenetserver.com>`
- **In-Reply-To:** `<irLWc.198225$M95.197768@pd7tw1no>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no>`

```
James J. Gavan wrote:
> Yiorgo Terzis wrote:
> 
>> Is it possible
[snip]
> go to Micro Focus site and sign up for Answer Exchange (freebie)

You need an autoresponder.  I think DD might have one - you could change 
the "please do your own homework" to "please go to Micro Focus and sign 
up for Answer Exchange".  ;)
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-24T22:45:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<byPWc.207529$J06.107311@pd7tw2no>`
- **In-Reply-To:** `<4wOWc.29589$5s3.9281@fe40.usenetserver.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no> <4wOWc.29589$5s3.9281@fe40.usenetserver.com>`

```
LX-i wrote:

> James J. Gavan wrote:
>
…[13 more quoted lines elided]…
>
I agree Daniel it gets a bit tiresome typing it each  time - for the 
life of me, why don't M/F do a mail out telling folks Answer Exchange 
exists. You really need to go there for specifics, and just like the 
others, oodles of examples they can point you at.. Example - I just 
asked, "The Animator (debugger) shows a Hex value for any objects 
created for OO, (i.e. the Hex Value is the object reference or 
'pointer').. While the Animator is great, in this particular instance, 
(no pun intended with last word),  I would have liked to do a DOS screen 
display to see if the objects matched - I got an answer, haven't tried 
it yet, but at least I'm not bamboozled.

What's an auto-responder ?. Allow for my age - you are still in the cusp 
of youth. Wait  until Mommy USAF doesn't look after you when you get out 
into the big wide, wide world. :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-25T08:54:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8043C6.08541825082004@knology.usenetserver.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no> <4wOWc.29589$5s3.9281@fe40.usenetserver.com> <byPWc.207529$J06.107311@pd7tw2no>`

```
An auto-responder will scan your incoming mailbox and issue responses 
depending upon the content of the message.

The simple example is the vacation deamon.  Turn it on and any incoming 
mail generates a response to sender "I'm sorry, Jimmy is out for 3 days.  
But your message is important, will contact when I return, yada, yada".

You would need one that could scan for the string "How do I" and change 
the response text to "contact answer exchange".




In article <byPWc.207529$J06.107311@pd7tw2no>,
 "James J. Gavan" <jjgavan@shaw.ca> wrote:
<snip>
> 
> What's an auto-responder ?. Allow for my age - you are still in the cusp 
…[3 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-25T12:53:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7m4Xc.29884$5s3.22430@fe40.usenetserver.com>`
- **In-Reply-To:** `<byPWc.207529$J06.107311@pd7tw2no>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <irLWc.198225$M95.197768@pd7tw1no> <4wOWc.29589$5s3.9281@fe40.usenetserver.com> <byPWc.207529$J06.107311@pd7tw2no>`

```
James J. Gavan wrote:
> LX-i wrote:
> 
…[24 more quoted lines elided]…
> it yet, but at least I'm not bamboozled.

Sounds great.  :)

> What's an auto-responder ?. Allow for my age - you are still in the cusp 
> of youth. Wait  until Mommy USAF doesn't look after you when you get out 
> into the big wide, wide world. :-)

heh - an auto-responder is a program that AUTOmatically RESPONDs to 
something.  It's usually used for mailing lists as such (i.e., email 
lists@mydomain.com with "info" as the subject to get information about 
this list).  Of course, you wouldn't want to reply to -every- message 
here with that - only maybe every 5th one.  ;)
```

#### ↳ Re: Microfocus Printing in Columns

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-24T14:51:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gZqdnWoRFoqmAbbcRVn-vA@giganews.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
Yiorgo Terzis wrote:
> Is it possible to print data in columns using only native PC_...
> routines ? The known problem is the shifting of a column to the left
…[4 more quoted lines elided]…
> etc.

I'm sure it's possible but the horror of it all!

Assuming (easy way) you have to build one line in memory. To do so, you've
got to know where the second label begins - in linear measure.

With a fixed font, this is trivial. With a proportional font, well:

1. You've got to know the width of the first column, so you've got to sum
the proportional widths of all the characters making up the printable area.

2. Then you must insert sufficient spaces (knowing the width of a space) to
get yourself to the beginning of column two.

3. As a bonus, the various character widths are not the same from font to
font. For example, an "e" may be 2/3rds the width of "w" in one font and
3/5ths the width in another font.

4. You must be precise in the above calculation. An error of 1/10 mm looks
wretched.

Suggestions:
1. Use a fixed-width font. The postal service recommends a fixed-width font
and all capitals for mailing labels anyway (speeds automation).

2. Use a label printer that only prints one column.
```

#### ↳ Re: Microfocus Printing in Columns

- **From:** "Stephen Gennard" <stephen.gennard@someone.somewhere.at.a.m.focus.company.com>
- **Date:** 2004-08-25T00:16:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cggi4q$l7u$1@hyperion.microfocus.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
If you have to use a proportional font,  you could separating the columns in
your report with a tab (0x09).
```

##### ↳ ↳ Re: Microfocus Printing in Columns

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-25T03:45:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408250245.4cbd53d0@posting.google.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <cggi4q$l7u$1@hyperion.microfocus.com>`

```
"Stephen Gennard" <stephen.gennard@someone.somewhere.at.a.m.focus.company.com>
wrote

> If you have to use a proportional font,  you could separating the columns in
> your report with a tab (0x09).

<shudder>

Tabs are no solution when proportional fonts are in use.  They will
either be interpreted as a number of spaces (and thus are no benefit
versus spaces), or they will go to the next fixed point if that can be
set somehow.  The problem then is 'which is the _next_ position'.  ie
if positions are at 10, 20, 30 then if the first colum takes up 8
(because it is a few 'i's) the next is 10, if it takes 12 (because it
is a few 'w's) the next is 20.

Still no consistency.
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

- **From:** "Stephen Gennard" <stephen.gennard@someone.somewhere.at.a.m.focus.company.com>
- **Date:** 2004-08-25T12:24:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cghsr6$q55$1@hyperion.microfocus.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <cggi4q$l7u$1@hyperion.microfocus.com> <217e491a.0408250245.4cbd53d0@posting.google.com>`

```
Tabs are *not* interpreted as spaces in the PC_PRINT* APIs.



Tab positions in the PC_PRINT* APIs are set at an average character width X
8.  The average character size is returned from Windows via the TEXTMETRIC
structure (tmMaxCharWidth).



The actual drawing of the characters is performed via the Windows API
TabbedTextOut().



This is consistent with any document created with proportional font and
tabs.



This I agree is not perfect but may help.



A brute force solution is to use PC_PRINTER_INFO to obtain the hDC for the
printer channel and then use the Windows API directly, this will allow you
complete control of what you print and where you print it.
```

#### ↳ Re: Microfocus Printing in Columns

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-25T20:10:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<412CF422.5000704@shaw.ca>`
- **In-Reply-To:** `<cgfr5v$2an$1@usenet.otenet.gr>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr>`

```
Yiorgo Terzis wrote:

>Is it possible to print data in columns using only native PC_... routines ?
>The known problem is the shifting of a column to the left or right
…[10 more quoted lines elided]…
>
Bill

 - I see you refer him to John at Wimbledon for spc - but note he says 
above he doesn't want to use RPV, Cobview or TurbReports - my guess $$$$ 
- what's a rough price tag for spc ?

Yiorgo,

Have you tried Answer Exchange yet - haven't seen anything from you.

Just a wild guess - are you trying to do something with ticketing for 
retail, pre-printed labels say 4 or 8 across the page ?
If it is retail, then you may well have to go googling looking for folks 
who specialize in ticketing.

If it's not that, exactly what are you doing that is causing you this 
alignment problem ? Donald's approach is closest. Here's what I do using 
PC_PRINT.

- my reports are landscape in condensed giving roughly a line capacity 
of 187 characters.
- Naturally I want header data to look a bit different from the text.
- I use a different font for the header from the detail lines. 
Surprisingly, two fonts, the combination looks better than sticking with 
one font !
- I can manipulate the header going bold, larger etc. do a 'Pause' and 
then change to something else.
- my individual print lines, and sub-total lines are set in particular 
styles or fonts - but I retain that format for detailed lines,
or total-lines as appropriate. I have no problem with alignment. It's 
sometime since I did it - so I'm a bit vague. I think I *may* have had a 
problem with alignment - say I wanted something like :-

this-is-the-description ........zz.zzz.........zz.zzz..... etc.

The dots/periods are spaces.

I can't recall, but I may have had problems with those numerics - so 
instead of  the line above, I substituted the following :-

this-is-the-descriptionzzzzzzz.zzzzzzzzzzz.zzz..... etc.

I expanded the numeric fields to include intervening spaces. As I say 
quite a while since I did it, so not absolutely sure.
I can only guess at what is happening above - seeing that  Stephen 
jumped in, perhaps he can confirm. Each of those 'z's' has the same 
width/pitch, whatever, and regardless of whether or not it contains a 
character to print, picks up on the anticipated width for printing 
(????). But it works.

Any help ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Microfocus Printing in Columns

- **From:** "Stephen Gennard" <stephen.gennard@someone.somewhere.at.a.m.focus.company.com>
- **Date:** 2004-08-25T23:22:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgj3bv$u00$1@hyperion.microfocus.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca>`

```
Hi Jimmy,

I can well imagine you would have alignment problem due to space, 0-9 all having different widths.   

For example:  (Hopefully you can see the text below is using a fixed pitch)
 
 this-is-the-description ........zz.zzz.........zz.zzz..... 

 this-is-the-description ........99.999.........99.999.....


And the same text above but with Aerial font... all the alignment is lost...

 this-is-the-description ........zz.zzz.........zz.zzz..... 

 this-is-the-description ........99.999.........99.999.....


then replace the large sections of spaces with a couple of tabs (align's reasonably well)
 this-is-the-description                zz.zzz               zz.zzz..... 

 this-is-the-description                99.999              99.999.....
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-25T18:20:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Y-dnasfYI86g7DcRVn-tg@giganews.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca> <cgj3bv$u00$1@hyperion.microfocus.com>`

```
Stephen Gennard wrote:
> Hi Jimmy,
>
> I can well imagine you would have alignment problem due to space, 0-9
> all having different widths.

In professionaly-designed fonts, all numbers are the same width.
111111111 =
999999999

>
> For example:  (Hopefully you can see the text below is using a fixed
…[104 more quoted lines elided]…
>> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 4)_

- **From:** "Stephen Gennard" <stephen.gennard@someone.somewhere.at.a.m.focus.company.com>
- **Date:** 2004-08-26T10:47:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgkbhv$2t4$1@hyperion.microfocus.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca> <cgj3bv$u00$1@hyperion.microfocus.com> <1Y-dnasfYI86g7DcRVn-tg@giganews.com>`

```
Hi Jerry,

I agree 0-9 should ALL have the same width but not all fonts are made equal!

I wrote a little program to examine the fonts on my machine, it found:
 I have 161 fonts,  80 fonts have equal 0-9 and  81 fonts have unequal 0-9 
digits.

I honestly would have expected to find the odd font that were bad... but 
hey.. nothing in life is that perfect.

For example, "Comic Sans MS" does not have equal 0-9 digits.

Comic Sans MS, 0-9 are not the same size
[0] = 16.02919
[1] = 13.28667
[2] = 16.02919
[3] = 16.02919
[4] = 16.02919
[5] = 16.02919
[6] = 16.02919
[7] = 16.02919
[8] = 16.02919
[9] = 16.02919

etc...
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-08-26T11:32:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TSjXc.5152$ZC7.4636@newssvr19.news.prodigy.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca> <cgj3bv$u00$1@hyperion.microfocus.com> <1Y-dnasfYI86g7DcRVn-tg@giganews.com> <cgkbhv$2t4$1@hyperion.microfocus.com>`

```
"Stephen Gennard"
<stephen.gennard@someone.somewhere.at.a.m.focus.company.com> wrote in
message news:cgkbhv$2t4$1@hyperion.microfocus.com...

> I agree 0-9 should ALL have the same width but not all fonts are made
equal!

Of course all fonts are not made equal. Proportional fonts were deliberately
made different to make output easier to read.

Or have we all forgotten about the USER here; you remember the USER, don't
you? The guy/gal whom programmers SERVE?

Proportional fonts are here to stay. Deal with it.

Bias Alert:
I have spent the last five days or so doing my first major report using
proportional fonts. What a mindset change! I had to really concentrate on "x
position, yposition IN INCHES"  but my brain kept saying, "Hey, Michael,
that's wrong: you *know* from 20+ years experience you should be thinking
'characters per inch, lines per page'."

But damn if that report doesn't look a hell of lot nicer than it used to!

MCM
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-26T07:27:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MfKdnecA4PaASrDcRVn-uw@giganews.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca> <cgj3bv$u00$1@hyperion.microfocus.com> <1Y-dnasfYI86g7DcRVn-tg@giganews.com> <cgkbhv$2t4$1@hyperion.microfocus.com> <TSjXc.5152$ZC7.4636@newssvr19.news.prodigy.com>`

```
Michael Mattias wrote:
> "Stephen Gennard"
> <stephen.gennard@someone.somewhere.at.a.m.focus.company.com> wrote in
…[6 more quoted lines elided]…
> deliberately made different to make output easier to read.

Right. I should have said: All professionally designed, textual fonts,
proportional or no, have equal-width numerics. Art, headline, and other
special-use fonts may deviate from this rule by their deviate designers.
```

###### ↳ ↳ ↳ Re: Microfocus Printing in Columns

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-26T21:17:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JQwXc.30173$5s3.27421@fe40.usenetserver.com>`
- **In-Reply-To:** `<TSjXc.5152$ZC7.4636@newssvr19.news.prodigy.com>`
- **References:** `<cgfr5v$2an$1@usenet.otenet.gr> <412CF422.5000704@shaw.ca> <cgj3bv$u00$1@hyperion.microfocus.com> <1Y-dnasfYI86g7DcRVn-tg@giganews.com> <cgkbhv$2t4$1@hyperion.microfocus.com> <TSjXc.5152$ZC7.4636@newssvr19.news.prodigy.com>`

```
Michael Mattias wrote:
 >
> I have spent the last five days or so doing my first major report using
…[5 more quoted lines elided]…
> But damn if that report doesn't look a hell of lot nicer than it used to!

I personally have an extreme dislike for the Courier font.  It was 
really cool on my IBM Selectric, but a Pentium 4?  :)  When I was put in 
charge of our CM system, I set up a page for one of our most common 
reports, and tried changing the specified font to Tahoma.  Since there's 
an easy column-making mechanism in HTML, I didn't have to change a whole 
lot, and it did look a lot better.  (I did have to change the pixel size 
on the columns a tad...)

Now, almost every report in that system specifies that class on their 
tables.  It catches on.  :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
