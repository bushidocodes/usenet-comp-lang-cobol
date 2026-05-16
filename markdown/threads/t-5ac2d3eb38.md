[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using toolbar.

_16 messages · 8 participants · 1999-10_

---

### Using toolbar.

- **From:** "Tommy Nilsen" <tommynilsen@yahoo.com>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EtFM3.213$kh.55@news1.online.no>`

```
Hi.

Im writing a program that uses the toolbar that comes with
Netexpress 3.0/Dialogsystem..

I can't figure out how to register a callback-event on "mouseover"
for a button on the toolbar.

I want the buttons on the toolbar to change it's appearance when the user
move's the mouse over the buttons.

Any help would be greatly appreciated.

Tommy Nilsen
```

#### ↳ Re: Using toolbar.

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u05c3$16o$1@plutonium.btinternet.com>`
- **References:** `<EtFM3.213$kh.55@news1.online.no>`

```
Tommy,

IM not sure, if the toolbar will respond to mouse events, as I
have never done it, but to register a call-back you can code the following:.


           move "ChangeButton" to messageName
           invoke CallBack "new" using self MessageName
               returning aCallback
           move p2ce-MouseMoved to Event
           invoke otoolbarButton "setEvent" using Event aCallback



Simon R Hart
Eaton, Ottery St. Mary, UK.



Tommy Nilsen wrote in message ...
>Hi.
>
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Using toolbar.

- **From:** "Tommy Nilsen" <tommynilsen@yahoo.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XzXM3.435$7G2.3787@news1.online.no>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com>`

```
I've tried it...  Doesn't  work..

I've posted the issue to my local support here in Norway, but it takes a
long time for them to respond...

Thanks,

Tommy Nilsen


Simon R Hart <hart1@technologist.com> wrote in message
news:7u05c3$16o$1@plutonium.btinternet.com...
> Tommy,
>
> IM not sure, if the toolbar will respond to mouse events, as I
> have never done it, but to register a call-back you can code the
following:.
>
>
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Using toolbar.

- **From:** "Tommy Nilsen" <tommynilsen@yahoo.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tRXM3.444$7G2.3509@news1.online.no>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no>`

```
When I perform a doEvent , it jumps to the callback I've registered.
This must mean that I've registered the callback correctly , or ??

If this is correct, I suspect that aToolbarButton doesn't respond to
mouse-over events...

Tommy Nilsen




Tommy Nilsen <tommynilsen@yahoo.com> wrote in message
news:XzXM3.435$7G2.3787@news1.online.no...
> I've tried it...  Doesn't  work..
>
…[39 more quoted lines elided]…
> > >I want the buttons on the toolbar to change it's appearance when the
user
> > >move's the mouse over the buttons.
> > >
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3804AF94.E68CE36D@home.com>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no>`

```
Come on Stephen Biggs - if your looking in. Bet you can give Tommy a
definitive answer <G>

Jimmy, Calgary AB


Tommy Nilsen wrote:
> 
> When I perform a doEvent , it jumps to the callback I've registered.
…[64 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 5)_

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u2j09$b1h$1@hyperion.mfltd.co.uk>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:
>Come on Stephen Biggs - if your looking in. Bet you can give Tommy a
>definitive answer <G>

Sorry, I've not been following this thread at all. :-)

My immediate comment is to ask why Tommy would want to change the 
appearance of the button as the mouse moves over it - 'flat' toolbars 
already indicate their "clickable" status (cf the TBARDS demo) by raising 
the border.

My limited knowledge of toolbars can only provide this:
If you trap the WM_NOTIFY/TBN_GETDISPINFO message (perhaps via 
subclassing the window class and implementing "wmGadgetNotify"?), you can 
set the image of the button requested using the image list associated with 
the toolbar. I'm not sure how easy this is to get to via the class library 
- it may require several extra methods in a new subclass. You'll probably 
have to send the toolbar TB_SETBUTTONINFO messages to change the default 
image for each button to I_IMAGECALLBACK, too.

This all avoids having to deal with individual control's mouse messages by 
leaving that work to the OS.

And there might even be an easier way - sorry, I've no definitive answers 
today :)

Steve.
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38052373.42595732@news1.attglobal.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk>`

```
On Wed, 13 Oct 1999 17:09:56 GMT, Stephen.Biggs@merant.com (Steve
Biggs) wrote:

>
>My immediate comment is to ask why Tommy would want to change the 
…[3 more quoted lines elided]…
>

Vendorspeak alert.  He wants to change it for the same reason I do.
It looks COOL.  I've seen it in other windows apps, and I want to do
it in mine.  I can change the mouse pointer (nice) but I want to
change the actual bitmap of the toolbar button when something is over
it.  (Flexus may very well be working on such an enhancement - I've
asked for it, right Bob?).

But I'll tell you one thing - whenever I have asked Flexus for a
feature they never asked "Why".  Kinda nice.  Done gloating.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38054E1F.A2B89614@home.com>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net>`

```


Thane Hubbell wrote:
> 
> On Wed, 13 Oct 1999 17:09:56 GMT, Stephen.Biggs@merant.com (Steve
…[18 more quoted lines elided]…
> 
Thane,

I was going to comment elsewhere, but in view of above...

Enough already ! As they say in New York. Thane - you are being non-
productive taking a swipe at Merant to which Stephen can't respond.
He contributes, to quote his own words "Because he cares" - AND - he is
a developer NOT tech support NOR a policy-maker. And this is not jumping
to the defence of Merant - Stephen is more than aware of my various
comments about what I personally consider is missing - BUT overall their
N/E product is SUPERB. Pete Dashwood commented the Animator was a superb
debugging tool - but he compromised and can get by with what's available
in Fujitsu. You might care to ask Donald Tees what he thinks about Fuji
IDE and Project control.

How come you haven't asked Fujitsu for the same feature - ahhh "24
Hours" covers the use of Screen Section - nice learning feature - but do
we really want 20-year olds designing systems in DOS mode for the coming
century; then I have to wait until Chapter 24 to see the reference to
SP2/Flexus. How come no mention of Fujitsu GUI handling. A footnote
would have sufficed, like "I think Merant's Dialog System is the pits,
and the same goes for Fujitsu GUI". 

And my friend Ray Leech left me with egg all over my face. From what he
had written to me privately some three/four months back, I thought he
was telllng me Dialog System was the best thing since sliced bread. He
has since expressed his thoughts clearly, and I understand.

Now here's the irony, and Stephen already knows - I don't like Dialog
System :-

a) It uses text tables - no good for me with OO where I want to use
collection/dictionary objects

b) It doesn't cover every single control and manipulation

c) You are very much tied-in to a compiler specific product, with the
ability to do a lot of validity within the GUI Interface as opposed to
the Business interface - and that is not a very good principle, as I see
it.. And your previous swipe " Tie you into their product...." So what's
wrong with that - perfectly good marketing ploy if you can pull it off -
but lousy from the consumers' perspective. Imagine the joy on Fujitsu
faces if you deleted Chapter 24 from the next re-print of "24 Hours" -
Fujitsu :) and Bob :(

d) And one of the points made by Ray - having gone so far, you can't
afford to change. Similarly, I'd already committed to OO/GUI before D/S
became available in N/E

And as regards your comment 'Why..." did he ask. Then suggest you start
reading some books up on systems analysis. (Frankly I think you've
either got it or you aint got it - no book is going to teach you to be
analytical). That's what got me into this game in the first place,
always asking why, both back in the RAF and subsequently. Don't just
jump in - start with a "Why....? I commented to Pete Dashwood that Thane
said DB was slow. His reply, "They probably don't know the first thing
about systems design". And I think their might be a smidgen of truth in
that. There is a VAST difference between system design and producing
clever program code - as many oil companies have found at a very high
cost. There are plenty of hot-shots in downtown Calgary. I briefly had
contact with one - he gets about $60K CDN a year - and the silly bugger
didn't know/or want to know about sending a zipfile by modem, "Send it
to me by courier". But they sound good - I call it verbal diarrhoea.

Any compiler/IDE is a compromise; they are conceived as the compiler
developer views the consumers' needs. As we all know too often they
don't quite do it for us. How I'd love to walk out of an auto showroom
with a custom-designed Jaguar/Porsche ! The result would make 007
salivate.

Nothing to do with Fujitsu or Merant - as I've already indicated to Bob,
third-party product(s) that address the needs of COBOL users to
interface with other modules is the way to go - PROVIDING they also
acknowledge the COBOL-xxx intent of OO and collections/classes. Saw the
term '3-tier system' recently, but in fact, in the context of
third-party products it is far more tiered :-

	Business Logic	- 	COBOL compiler & IDE

	User Interface	- 	a) GUIs
				b) Touch/Pen
				c) Verbal/Music
				d) Photographic
				e) Front-End devices - OCR/OMR/POS  	
				f) ??? etc...

	Storage Interface -	a) Flat-files COBOL
				b) DBs - endless list

	Printer Interface -     a) Another endless list or perhaps 
					Crystal ??


And we bloody-well don't need to jump into cutesey C++ or Java to get at
these devices from COBOL if third-party COBOL-oriented tools become
available.

And unless some genius dreams up a better way - the only tool I see
currently to merge this all together is OO with OPEN SOURCE available to
ALL developers to pick and choose the bits they want.

Now I've done ranting - but felt somebody had to respond.

PS: I'll still recommend your book <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u5s2k$q26$2@news.igs.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net> <38054E1F.A2B89614@home.com>`

```
James J. Gavan wrote in message
<pages and pages snipped>
>And unless some genius dreams up a better way - the only tool I see
>currently to merge this all together is OO with OPEN SOURCE available to
>ALL developers to pick and choose the bits they want.
>
>Now I've done ranting - but felt somebody had to respond.


I am thinking that all I/O of any sort should be done with standarized I/O
objects.  Unfortunately, of course, there is no way of doing that.
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380553fc.9970562@news1.attglobal.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net> <38054E1F.A2B89614@home.com>`

```
Caught you at a bad time?  Sorry I stepped on toes - didn't mean to!
But what a cat swipe I got back!

On Thu, 14 Oct 1999 03:21:06 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:



>Enough already ! As they say in New York. Thane - you are being non-
>productive taking a swipe at Merant to which Stephen can't respond.

No I answered the WHY question.  I also let out my frustration dealing
with OTHER vendors who keep asking me WHY instead of talking about HOW
to add/change something in their product.  And I'm not naming names.
I was also expressing my contentment with my relationship with one
vendor who does NOT ask WHY all the time.

>He contributes, to quote his own words "Because he cares" - AND - he is
>a developer NOT tech support NOR a policy-maker. And this is not jumping
>to the defence of Merant - Stephen is more than aware of my various
>comments about what I personally consider is missing - BUT overall their
>N/E product is SUPERB. 

Nothing in my post said it wasn't.  I've USED it.  I appreciate his
contributions to the group.

> Pete Dashwood commented the Animator was a superb
>debugging tool - but he compromised and can get by with what's available
>in Fujitsu. 

Again, I agree - NOTHING beats the MicroFocus Animator - at least that
I have used.

>You might care to ask Donald Tees what he thinks about Fuji
>IDE and Project control.

I like it better than what I was using.  

>
>How come you haven't asked Fujitsu for the same feature - ahhh "24
…[6 more quoted lines elided]…
>

Theres one cat swipe.  Let me defend myself - I am teaching the
beginner programmer.  You gotta walk before you can run.  The reason I
have not aske Fujitsu for the button feature is that I don't use
POWERCOBOL - and my Book does NOT ADDRESS POWERCOBOL.   It is by the
simplicity of Sp2 that I was able to introduce GUI at all in a
beginner book.  The GUI is important, but not as important as the
underlying COBOL foundation.

I had several goals when *I* designed and wrote the book.  The TOC was
not given to me, I started with a blank slate and *I* made the rules.

1.  A simple text that was easy to follow.
2.  Teach structured coding and design.
3.  Teach in a logical progression, each chapter reinforcing and
building on the previous chapter.
4.  NOT A Y2K Hype book.
5.  Give the reader a complete toolset - they can buy my book and
write COBOL programs that work.
6.  Teach STANDARD CURRENT COBOL - not the new standard that is under
Flux, and not the "old school" that needs to be updated.  This gives
me the added byproduct of TWO markets - NEW COBOL programmers and
COBOL programmers that want to update their skillset to the current
standard.  I did NOT use standard COBOL in the one respect of the
Screen Section.  But why the screen section - because it is simple.
We can get results right away.  And it works.

>And my friend Ray Leech left me with egg all over my face. From what he
>had written to me privately some three/four months back, I thought he
…[18 more quoted lines elided]…
>Fujitsu :) and Bob :(

Uh, what can I say, you know I agree.

>
>d) And one of the points made by Ray - having gone so far, you can't
…[16 more quoted lines elided]…
>to me by courier". But they sound good - I call it verbal diarrhoea.

Now that was personal and uncalled for.  Shame on you.  I didn't
design "my" slow database systems - I just have the pleasure of
working with them - others where I work did that.  I *DO* know system
design however, and I do know the value of asking WHY - but you are
overreacting a bit here.  We are talking about buttons on a toolbar -
and YES I have requested this exact same feature from Flexus.

>
>Any compiler/IDE is a compromise; they are conceived as the compiler
…[39 more quoted lines elided]…
>

Thanks I'm still your friend.  Let me lick my wounds and we'll get on
with life.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 9)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u5tg1$qnn$1@news.igs.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net> <38054E1F.A2B89614@home.com> <380553fc.9970562@news1.attglobal.net>`

```

Thane Hubbell wrote in message
>
>>You might care to ask Donald Tees what he thinks about Fuji
…[3 more quoted lines elided]…
>
I do not.  Two years back, I had a well organized library, where I could
find anything that I wanted.  I could simply type "compile systemname" and
be absolutely assured that any code I had written in 15 years in 3 languages
(mixed) and several lifetimes of version numbers would completely and
accurately generate themselves.  (I would have to preface that with a
statement like "MSCOBOL4.5" to indicate the generation, but that would be
it.

Today, with modern tools, I have stuff all over my disks, I have completely
revised my entire libraries three times trying to attain a manageable state,
and I cannot trust anything less than complete rebuilds of anything but
simple test programs.

Three quarters of what is on my disk is generated, and I seems to be
absolutely impossible to maintain a clean library of source code. There is
garbage everywhere; every piece of Cobol software on the market seems to
think it their right to place garbage anywhere and everywhere on my disk
with nary a thought about cleanup.

The IDE's all decide for me what my file naming conventions will be, and
their software enforces it.  Unfortunately, their naming conventions are so
weak that any project of more that sophomore standards becomes unmanageable
if you use it. Every copy file, for example, must have an identical
extension chosen by the Vendor, regardless of the type of copy.

Not to mention editors.  I have yet to see an IDE with a professional
quality editor.  50% of the IDE functionality disappears if you choose not
to use the editors provided.

I like my current compiler.  I am staring to like the oops extensions. The
Pstaff is useful, although it would be a thousand times better if iterative.

They all work well enough to get the job done, which is the bottom line.
However, I do not think them better than what I used to use.  I think they
have some real advantages, but also some real weaknesses. Maybe next
generation they'll be better.  Now they are worse.
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 8)_

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3806005b@eeyore.callnetuk.com>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net> <38054E1F.A2B89614@home.com>`

```
Jimmy,

you're obviously incensed about this, (I don't really understand why...Thane
is expressing an opinion which he has a right to do. Similarly, you are
responding to this expression, which you also have a right to do...). I am
posting this because you asked me to check out the thread and because you
are attributing statements to me which I need to be sure accurately reflect
my thoughts on the matter.

At the end of the day, has the original poster received help on his problem
with changing toolbar buttons?

Like so much of  this forum, people go immediately off-topic so they can
ride their own favourite hobby-horse. If all of you who post here want this
NG to really be a success you must enforce some self-discipline and address
the questions being asked BEFORE you get into gab-fest. Otherwise, what
could be a valuable interchange of ideas becomes simply a waste of time.
People come here for HELP. If you care about COBOL you will see that they
get it (and I'm not minimising the very valuable postings from a core of
highly experienced and able people...all I'm saying is keep the focus on
providing ON-TOPIC help.)

Now to your posting....

James J. Gavan wrote in message <38054E1F.A2B89614@home.com>...
>
>
…[8 more quoted lines elided]…
>> >already indicate their "clickable" status (cf the TBARDS demo) by
raising
>> >the border.
>> >
…[12 more quoted lines elided]…
>
I agree with the sentiments expressed. Looking COOL is a perfectly valid
reason for wanting something. A 2 paragraph indulgence on Thane's part to
express how good his particular vendor is, is really harmless and nothing to
get unwrapped about. We all have our favourites (except me, of course, I
hate 'em all...)

>I was going to comment elsewhere, but in view of above...
>
…[6 more quoted lines elided]…
>N/E product is SUPERB.

I'm not sure that Thane was casting aspersions on N/E as a product, Jimmy. I
understand your concern to see that someone who is donating his time and
expertise is not personally attacked, but I don't think that's what Thane
had in mind.


>Pete Dashwood commented the Animator was a superb
>debugging tool - but he compromised and can get by with what's available
>in Fujitsu.

Well, I can't fault you on that. That IS what I said, but it demonstrates
perfectly how meanings can be changed when taken out of context. The
Animator IS a superb debugging tool, but I don't feel that moving to Fujitsu
has necessitated a "compromise". Their debugger is very capable and meets my
needs; in other areas (especially GUI development) I believe their product
suits me better than what was MicroFocus. (I certainly would have no problem
with changing the appearance of toolbar buttons....[remember what this is
all about?]). Although I was very facile with DS, I prefer to write my event
processing in COBOL. This is simply a matter of preference and I accept that
other people will have other priorities...it's really silly to get into a
pissing contest over vendors...they ALL have their shortcomings.

>
>How come you haven't asked Fujitsu for the same feature
>
Maybe because there is no need to? Floating toolbars are handled very well
by Fujitsu COBOL.

>- ahhh "24
>Hours" covers the use of Screen Section - nice learning feature - but do
…[5 more quoted lines elided]…
>

Oh Dear, Jimmy, slagging Thane's book is not going to achieve anything
(unless you want to start a separate topic reviewing the publication?)

>
>And my friend Ray Leech left me with egg all over my face. From what he
…[3 more quoted lines elided]…
>

It's tough when you misunderstand people...I seem to recall it took some
time for you to realise that I wasn't averse to OO <grin>.

[SNIPPED downers on DS]...

>c) You are very much tied-in to a compiler specific product, with the
>ability to do a lot of validity within the GUI Interface as opposed to
>the Business interface - and that is not a very good principle, as I see
>it..

Hmmm...while I respect your right to an opinion, I would have to differ with
you here. I think it is a very good idea to remove format validation from
the Business Logic. Not sure that I would include validation of Business
rules, but ensuring that numbers are numbers, dates are dates, etc. let the
hardware do it.

>And your previous swipe " Tie you into their product...." So what's
>wrong with that - perfectly good marketing ploy if you can pull it off -
>but lousy from the consumers' perspective.

Well, if saying that's a "swipe", then count me in as number One "swiper"..!
You must be joking...I can't seriously believe what you are saying. It is
NOT, and never has been, OK for ANY vendor to tie us into their specific
platforms. We can't blame them for trying and if we are silly enough to fall
for it, then we deserve what we get (you know my feelings on this and have
quoted them in threads on this NG...in fact, I seem to recall you desiring
to take a Trans-Atlantic slug at me for being right...(curious concept; I
thought people got hit for being WRONG...<G>))

> Imagine the joy on Fujitsu
>faces if you deleted Chapter 24 from the next re-print of "24 Hours" -
>Fujitsu :) and Bob :(
>
Not having read Thane's book, I have no idea what Chapter 24 is about. But
is bringing joy to people (even Fujitsu...) a BAD thing, now?


>d) And one of the points made by Ray - having gone so far, you can't
>afford to change. Similarly, I'd already committed to OO/GUI before D/S
>became available in N/E
>
"can't afford to change..."?  For my company it was "can't afford NOT to
change..."

>And as regards your comment 'Why..." did he ask. Then suggest you start
>reading some books up on systems analysis. (Frankly I think you've
…[3 more quoted lines elided]…
>jump in - start with a "Why....?

"I keep six honest serving men
They taught me all I knew
Their names are "What?" and "Where?"
And "When?"
And "How?" and "Why?" and "Who?""

This reflects Kipling's background as a journalist. Whilst we may agree with
his sentiments, we must also accept that by and large, journalists are
pretty disagreeable people... Anyone who has spent time with a two year old,
knows how tiresome constant "Why?"s can become.
It is important to listen to the answers and think about them before
formulating the next "Why?"
So I guess when they told you in the RAF "Get in that plane and kill some
people" and you said "Why?", they figured you might be better suited to
computing..., right, Jimmy<G>?

>I commented to Pete Dashwood that Thane
>said DB was slow. His reply, "They probably don't know the first thing
>about systems design".

Now on this one, Mr Gavan, I really must protest. I have checked the
correspondence, and that is NOT what I said. (I thought it didn't sound like
me and was relieved to find that it wasn't...) Snips in Quotes, my responses
in square brackets...
The first time you raised it:

 "Thane said it was SLOW - his
emphasis, not mine.
[SLOW is always relative. The snail considers the tortoise fast.]"

The second time:
"Thane is still saying under
"Sorting" - that DBs are SLOWwwwww. Care to comment on the NG ?
<<<
[Already have. By now Thane will be sticking pins in a wax effigy of me.]

The comment you may have been thinking of when you "quoted" (again out of
context and NOT verbatim) me, was that when young ACCESS programmers are
thrown in at the deep end "they probably don't know much about DATABASE
design" I did make such a statement.

>And I think their might be a smidgen of truth in
>that. There is a VAST difference between system design and producing
…[5 more quoted lines elided]…
>

I heard that the hot-shots stampede to Calgary every year...

>Any compiler/IDE is a compromise; they are conceived as the compiler
>developer views the consumers' needs. As we all know too often they
…[3 more quoted lines elided]…
>
A camel is a horse designed by a committee...

>Nothing to do with Fujitsu or Merant - as I've already indicated to Bob,
>third-party product(s) that address the needs of COBOL users to
…[23 more quoted lines elided]…
>available.

They ARE available already, Jimmy. It's called Active-X, OCX, or CORBA.


>
>And unless some genius dreams up a better way - the only tool I see
>currently to merge this all together is OO with OPEN SOURCE available to
>ALL developers to pick and choose the bits they want.
>

Certainly a possibility but there are already "geniuses" around the planet
who are looking at better ways.

Open Source is irrelevant. OO is another fashion statement (even though I
like the way it fits, it is still just "programming"). Computer Programming
is a phenomenon of the late 20th Century. In fact "developers" will soon be
a thing of the past.

Ultimately, Jo Public will interact with his computer until it does what he
wants. A billion computer users are not going to be dictated to by a
technocracy, neither are they all going to become "computer programmers".
The machines will have to get smart enough for ordinary people to use
easily, and they will. Just as the marketplace drove the user interface on
automobiles to become simple, so will it be with computers.

>Now I've done ranting - but felt somebody had to respond.
>

There, there, Jimmy. Go and lie down in a darkened room...<G>. Hey, it does
no harm to get it off your chest...Much of what you wrote is pertinent. It
certainly came from the heart.

Unfortunately, none of this is getting our friend his toolbar images...

You see what I mean about this NG? Because it is not moderated (at least as
far as I can tell, apologies Mr. Moderator...if you're there.) it is
ESSENTIAL that self discipline be invoked by the contributors. There is a
place for fun and jollity, and "philosophical" discussion, and passing the
time of day, they are all important, but the most important function of this
group is to provide clear support for the COBOL language. That means HELP to
people who need it, if you have the ability to provide it.

For this NG to be effective and actually achieve something, it is necessary
for postings to stay ON-TOPIC. If you want to digress and explore another
avenue, do so by starting another topic.

(As this is one of the exceptional times when I shall post to this NG, I am
not taking my own advice...If I intended to post here regularly, I certainly
would have all of this under another topic...)

All of the above may or may not be valuable, but if anyone wants to refer
back to it he is unlikely to look for it under a topic called "using
Toolbar"....

Look back over this NG and you will find that the most successfull,
sustained threads were the ones which stayed on topic.

Unfortunately, I don't have time to maintain an involvement here (and
besides, there is something hairy with my news server which means I don't
get all the threads anyway) so it doesn't really make any difference to me,
personally, but there may be other people who  would post here if the group
was better organised. (More topics, smaller postings).

If you feel provoked, outraged or incensed by anything I have written, good.
Take it up with me personally. That way I can ensure we stick to the
point...<G>

Regards,

Pete.



I do not intend to participate in this NG because, frankly, it is a waste of
my time. It is a waste of time because threads go off-topic so fast that it
is not possible to follow them. Say, for instance I have particular
expertise which I'm happy to share in the area of "Indexed files". I see a
topic about Indexed files and find that it is now about
>PS: I'll still recommend your book <G>
>
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 7)_

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u48hl$h0f$1@hyperion.mfltd.co.uk>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net>`

```
thaneH@softwaresimple.com (Thane Hubbell) wrote:
>Vendorspeak alert.  He wants to change it for the same reason I do.
>It looks COOL.  I've seen it in other windows apps, and I want to do
>it in mine.  I can change the mouse pointer (nice) but I want to
>change the actual bitmap of the toolbar button when something is over
>it. 

Thane - I was merely wondering if there was something that Tommy wanted to 
do that would be better achieved another way; his reasons for wanting to 
change the toolbar are also important in determining what functionality he 
actually requires.

And I then went on to give some help (which you snipped out)!

As Jimmy said, I wasn't replying in any official capacity - merely 
responding to Jimmy's direct question. This isn't a technical support 
forum for MERANT Micro Focus and I am not a Technical Support team member. 
I'm just trying to help out!

Steve.
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3805cdfd.26091486@news1.attglobal.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net> <7u48hl$h0f$1@hyperion.mfltd.co.uk>`

```
On Thu, 14 Oct 1999 08:23:32 GMT, Stephen.Biggs@merant.com (Steve
Biggs) wrote:


>As Jimmy said, I wasn't replying in any official capacity - merely 
>responding to Jimmy's direct question. This isn't a technical support 
>forum for MERANT Micro Focus and I am not a Technical Support team member. 
>I'm just trying to help out!

Any help from any vendor is extremely appreciated by the group.  Sorry
I sounded critical of YOU which was not my intent, except in the area
that the first portion of your resoponse was to ask WHY, and I'm
afraid at that time of day, from experiences outside your control, the
remark just set me off a bit.  Sorry to have taken it out on you.  My
apologies.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 7)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3805da7b.3089120@news.enter.net>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no> <3804AF94.E68CE36D@home.com> <7u2j09$b1h$1@hyperion.mfltd.co.uk> <38052373.42595732@news1.attglobal.net>`

```
thaneH@softwaresimple.com (Thane Hubbell) wrote:

>On Wed, 13 Oct 1999 17:09:56 GMT, Stephen.Biggs@merant.com (Steve
>Biggs) wrote:
…[13 more quoted lines elided]…
>asked for it, right Bob?).

Flexus vendorspeak alert.  Thane...Yes, you did ask for it.  I'll
check on the status and get back to you!

;-)

>But I'll tell you one thing - whenever I have asked Flexus for a
>feature they never asked "Why".  Kinda nice.  Done gloating.

There's a good reason for this, Thane.  I've been told by others that
if I question your motives, you'll fly up to PA in your Mooney and
beat me up.  The rumor mill says that you've been solicited to work
for Governor Jesse Ventura as his bodyguard.

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Using toolbar.

_(reply depth: 4)_

- **From:** "Tommy Nilsen" <tommynilsen@yahoo.com>
- **Date:** 1999-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MBzO3.5378$7G2.26773@news1.online.no>`
- **References:** `<EtFM3.213$kh.55@news1.online.no> <7u05c3$16o$1@plutonium.btinternet.com> <XzXM3.435$7G2.3787@news1.online.no> <tRXM3.444$7G2.3509@news1.online.no>`

```
And the answer is ????


Tommy


Tommy Nilsen <tommynilsen@yahoo.com> wrote in message
news:tRXM3.444$7G2.3509@news1.online.no...
> When I perform a doEvent , it jumps to the callback I've registered.
> This must mean that I've registered the callback correctly , or ??
…[68 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
