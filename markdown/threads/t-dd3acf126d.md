[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# An SP2 bug.

_31 messages · 14 participants · 2000-09_

---

### An SP2 bug.

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-12T11:27:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pl3u5$4io$1@nnrp1.deja.com>`

```
Hi:

Here is a story about a funny bug in SP2.

My vertical-market POS systems use a three-character
(SECURE) password. People started calling me up and
saying that they could only enter one or two characters
into the three-character password field.

I tried it and it worked fine. Some people had a
problem and some didn't. Some people could type one
character, some people could type two, but they
couldn't type three.

I normally use 'SAM' as my password, and, for no
particular reason, I used 'JOE' instead. Now, all
I could do was type in one character.

Turns out that typing a lower-case 'o' (ASCII 111)
terminates the accept (CONVERSE) of the field.

This is what happened. . .

Programs are selected from a System Menu. The Menu
expects a password for certain programs. For reasons
not worth going into, I had put two pushbuttons on
the Menu panel. Later, I changed my mind and removed
them both and recompiled.

The SP2 manual gives the KEY-VALUES as ranging from 001
to 404. To avoid conflict I always use numbers like 711
712, and so on for the KEY-VALUE of the pushbuttons.

I had made a typo when assigning the value to the first
button and made it 111 (lower-case 'o').

Even though the button was DELETED, the program now
terminates when you type a lower-case 'o'.

So, as soon as you go to type in 'joe', the 'o'
terminates the accept. 'JOE', of course, works fine.

Note to Bob and Andy:  I manufactured a test program
which demonstrates this phenomenon if you want it. . .

Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: An SP2 bug.

- **From:** "Joshua Seltzer" <jseltzer@larich.com>
- **Date:** 2000-09-12T09:54:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<srsdgla7ct623@corp.supernews.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com>`

```
We use SP2 for our in-house POS systems as well.  We have found no problems
at all
with password fields such as described here.  We do not use standard SP2
converse logic
an add on product to generate all of our SP2 related code.  This
inexpensive, wonderful tool
has saved us untold hours of coding work over the last 2 years and I
strongly recommend it for
all SP2 developers.  The product is called Interface Developer from the
Business Assistance
Group.  For more info see www.bagtools.com .


Joshua Seltzer
Larich Distributors, Inc.


Foodman wrote in message <8pl3u5$4io$1@nnrp1.deja.com>...
>Hi:
>
…[51 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: An SP2 bug.

- **From:** "Paul Raulerson" <praul@cegi.no-spam-net>
- **Date:** 2000-09-12T18:54:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bec273_2@news5.newsfeeds.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <srsdgla7ct623@corp.supernews.com>`

```
SP2 is a purely wonderful tool. I turn off the code generator(s)
and just use the BMS and copybooks, and it is incredible how much
time it saves.

It tickles me pink to see that someone has actually got a product built
on Bob's SP2 -  more power to 'em! :)


Joshua Seltzer wrote in message ...
>We use SP2 for our in-house POS systems as well.  We have found no problems
>at all
…[71 more quoted lines elided]…
>




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: An SP2 bug.

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-13T10:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pnj7j$3g6$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <srsdgla7ct623@corp.supernews.com> <39bec273_2@news5.newsfeeds.com>`

```
In article <39bec273_2@news5.newsfeeds.com>,
  "Paul Raulerson" <praul@cegi.no-spam-net> wrote:
> SP2 is a purely wonderful tool. I turn off the code generator(s)
> and just use the BMS and copybooks, and it is incredible how much
> time it saves.
>
> It tickles me pink to see that someone has actually got a product
built
> on Bob's SP2 -  more power to 'em! :)

Hi:

Happy to see you in the pink.  I couldn't agree more about SP2
it is wonderful.

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: An SP2 bug.

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-12T20:33:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39be8fcc.28905401@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com>`

```
Tony:

It's actually not a bug.  Here's how it works in sp2:

When you create a pushbutton and assign a function key (ASCII Decimal
key value to return control to the application), THAT specific key
value is added to a list of control keys in the panel definition.

Even though you delete the pushbutton field, we don't want to
necessarily assume that you also want to get rid of the control key as
well, therefore we leave it intact in the control key list.

The reason that the application is prematurely returning control to
your COBOL program from sp2 when "Joe" is entered is because you have
established the "o" as a control key.  sp2 encounters the "o" and
passes control back.

If you access the control key list, you can delete the ASCII 111 key
definition and it will no longer return control to your application
when the "o" key is pressed.

Again, we don't like to assume that you want to get rid of a control
key just because you delete a pushbutton field.

You simply need to modify the control key list after deleting the
pushbutton.

Please let me know if this fixes the problem.

Thanks!


Foodman <foodman123@aol.com> wrote:

>Hi:
>
…[51 more quoted lines elided]…
>Before you buy.

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: An SP2 bug.

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-12T20:36:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gtwv5.33$l35.2181@iad-read.news.verio.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net>`

```
In article <39be8fcc.28905401@news.epix.net>,
Bob Wolfe <flexus.stop.the.spam at epix dot net> wrote:
>Tony:
>
>It's actually not a bug.

... it's a feature!

DD
```

##### ↳ ↳ Re: An SP2 bug.

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-13T10:09:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pnjnk$41t$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net>`

```
In article <39be8fcc.28905401@news.epix.net>,
  flexus.stop.the.spam at epix dot net wrote:
> Tony:
>
> It's actually not a bug.

Hi:

As DD pointed out, it's not a bug it's a feature.

It may be a feature but it certainly walked like a bug,
talked like a bug. . .

I don't entirely agree that SP2 should work as you described.
Surely, if, when creating a new button with a new control key
value, then, if you delete the button and the associated value
had not been established in some other way, then the value should
be deleted too.

Anyway, now that I know what the problem is. . .

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bfd8f2.65096157@207.126.101.100>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com>`

```
I have control keys defined with no associated buttons.  I don't want
them removed whilly nilly.

On Wed, 13 Sep 2000 10:09:02 GMT, Foodman <foodman123@aol.com> wrote:

>In article <39be8fcc.28905401@news.epix.net>,
>  flexus.stop.the.spam at epix dot net wrote:
…[25 more quoted lines elided]…
>Before you buy.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8por0l$ki8$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100>`

```
I'm with you, Thane. We do the same thing. We like the fact that we can
remove a pushbutton without removing the control key functionality.

Seems like someone once said something like "You can please some of the
people all the time and all of the people some of the time but you
can't please all the people all the time." As software developers, we
should all be aware of this.

If Bob and Andy change the way pushbuttons and control keys work in
SP2,I know of at least 5 people that won't like it.

I think that we can sometimes ask too much of a tool. The more it does,
the less control we have. I would rather have a tool that took care of
the basics and let me be creative as needed. We've all thrown away
tools that took control out of our hands, now haven't we?

John Chafin

In article <39bfd8f2.65096157@207.126.101.100>,
  thaneH@softwaresimple.com (Thane Hubbell) wrote:
> I have control keys defined with no associated buttons.  I don't want
> them removed whilly nilly.
…[35 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NE5w5.9645$XS1.59645@news2.atl>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com>`

```
John, you've touched on a fundamental issue here.  There are two very
different schools of thought on software tools, which I call 'monolith
tools' and 'simple tools'.  The 'monolith tools' folks want their tools
to support every function known to man, with every conceivable complex
function already available, so they only have to 'push a button' to get
it done.  The 'simple tools' folks (of which I am one) want a complete
set of essentially one function tools, which can be combined in many ad
hoc ways to do whatever tasks they want (e.g. "Software Tools" by Brian
W. Kernighan and P. L. Plauger).  What the monolith folks don't seem to
realize, or perhaps don't mind, is that complexity inevitably results
in inflexibility.  If you don't believe it, just look at how long it
takes to do simple things like delete all .BAK files in a subdirectory
with Windows as opposed to DOS.  To my mind, with software tools, the
word 'flexibility' is virtually synonymous with 'power'.  Just give me
the pieces, I'll figure out how to put them together. :-)
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C0EE4F.61649B9D@brazee.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl>`

```


Judson McClendon wrote:

> John, you've touched on a fundamental issue here.  There are two very
> different schools of thought on software tools, which I call 'monolith
…[12 more quoted lines elided]…
> the pieces, I'll figure out how to put them together. :-)

There are compromise positions.  The Windows API seems to me to be too tight
for most use.  And of course, compiled languages have taken over assembly for
most applications.  What we really want is to pick our tools.  Dragging and
dropping a button works fine if we have the opportunity to get behind it and
change it as need be.  Calling a library function works - as long as we can
use alternatives when we want.

As it is, I like command line functions.  It is like typing vs using a
dictaphone - harder to learn, but easier to use.  I hated it when my dos
editor went GUI and it doesn't automatically know where I want my files
anymore.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C8AF99897BCBEACC.9B0F5266CB7D8AE8.D752EF85262AA022@lp.airnews.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl> <39C0EE4F.61649B9D@brazee.net>`

```
On Thu, 14 Sep 2000 09:27:11 -0600, Howard Brazee <howard@brazee.net>
enlightened us:

>
>
…[28 more quoted lines elided]…
>anymore.

You've all hit on a pet peeve of mine.  I loved DOS because I could
really control what it did.  Sure it took a little effort and some
knowledge, but once learned, it was consistent.  So much of that
control was taken away with each permutation of Windows for the sake
of the non-technical user.  Good or bad that's the way it is but I
still don't like it.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 8)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pr3v3$a1o$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl> <39C0EE4F.61649B9D@brazee.net> <C8AF99897BCBEACC.9B0F5266CB7D8AE8.D752EF85262AA022@lp.airnews.net>`

```
.
>
> You've all hit on a pet peeve of mine.  I loved DOS because I could
…[5 more quoted lines elided]…
>

Hi:

Amen.

See thread "Only for newbies" for a perfect example. . .

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 9)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-09-15T04:31:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qChw5.28467$M37.639275@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl> <39C0EE4F.61649B9D@brazee.net> <C8AF99897BCBEACC.9B0F5266CB7D8AE8.D752EF85262AA022@lp.airnews.net> <8pr3v3$a1o$1@nnrp1.deja.com>`

```
Or/And... Find the Fred Langa page, and read about his discussion of batch
files and DOS.  He has four batch files for download to "clean up" your
system that you might find of interest also.

Warren Simmons
"Foodman" <foodman123@aol.com> wrote in message
news:8pr3v3$a1o$1@nnrp1.deja.com...
> .
> >
…[20 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 8)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pr3uh$a1i$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl> <39C0EE4F.61649B9D@brazee.net> <C8AF99897BCBEACC.9B0F5266CB7D8AE8.D752EF85262AA022@lp.airnews.net>`

```
.
>
> You've all hit on a pet peeve of mine.  I loved DOS because I could
…[5 more quoted lines elided]…
>

Hi:

Amen.

See thread "Only for newbies" for a perfect example. . .

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 6)_

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pt3h3$hbl$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bfd8f2.65096157@207.126.101.100> <8por0l$ki8$1@nnrp1.deja.com> <NE5w5.9645$XS1.59645@news2.atl>`

```
Judson,

You are asolutely correct. Well said.

John

In article <NE5w5.9645$XS1.59645@news2.atl>,
  "Judson McClendon" <judmc@bellsouth.net> wrote:
> John, you've touched on a fundamental issue here.  There are two very
> different schools of thought on software tools, which I call 'monolith
> tools' and 'simple tools'.  The 'monolith tools' folks want their
tools
> to support every function known to man, with every conceivable complex
> function already available, so they only have to 'push a button' to
get
> it done.  The 'simple tools' folks (of which I am one) want a complete
> set of essentially one function tools, which can be combined in many
ad
> hoc ways to do whatever tasks they want (e.g. "Software Tools" by
Brian
> W. Kernighan and P. L. Plauger).  What the monolith folks don't seem
to
> realize, or perhaps don't mind, is that complexity inevitably results
> in inflexibility.  If you don't believe it, just look at how long it
…[11 more quoted lines elided]…
> > I'm with you, Thane. We do the same thing. We like the fact that we
can
> > remove a pushbutton without removing the control key functionality.
> >
> > Seems like someone once said something like "You can please some of
the
> > people all the time and all of the people some of the time but you
> > can't please all the people all the time." As software developers,
we
> > should all be aware of this.
> >
…[3 more quoted lines elided]…
> > I think that we can sometimes ask too much of a tool. The more it
does,
> > the less control we have. I would rather have a tool that took care
of
> > the basics and let me be creative as needed. We've all thrown away
> > tools that took control out of our hands, now haven't we?
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-13T14:44:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bf8f74.6104881@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com>`

```
Foodman <foodman123@aol.com> wrote:

>In article <39be8fcc.28905401@news.epix.net>,
>  flexus.stop.the.spam at epix dot net wrote:
…[6 more quoted lines elided]…
>As DD pointed out, it's not a bug it's a feature.

It's actually not a feature either.  It was designed to work that way.
There is a good reason for the software to continue working the way it
does currently.  Please read on......

>It may be a feature but it certainly walked like a bug,
>talked like a bug. . .
…[5 more quoted lines elided]…
>be deleted too.

Tony:

The problem is that the control key value is stored in a single
location and the editor doesn't check other pushbutton or icon fields
to see if the same control key has been assigned to more than one
field.

For example.....You create a pushbutton and assign a key value of
ASCII 317 (F3 key).

Next you create an icon with a bitmap pushbutton, and assign it an
ASCII 317 (F3 key).

The end user can click on a pushbutton or on an icon to accomplish the
same result.

Now the user interface designer decides to scrap the pushbutton
because of the duplicity or perhaps they really meant to assign the F2
key to the pushbutton and accidently assigned the F3 key.

If the F3 key gets automatically deleted from the control key list
when the pushbutton is deleted, the icon field will no longer work
properly.

That's why the elimination of control keys has been separated from the
elimination of pushbutton or icon fields.

It's not a bug or a feature.  I'm sure that it is a headache to delete
the key separately, but it would also be a headache to have to
remember to go back and reassign a control key to the screen.

Perhaps we should pop up a little box when a pushbutton or icon field
is deleted, displaying the message......

"Do you want the Control Key to also be deleted?"

This would solve the problem, but then that annoying pop up message
box would be displayed every time you want to delete an icon or
pushbutton field.

Or we could check all other fields on the panel to make sure that the
control key hasn't been assigned to multiple fields.

I'll pass on the enhancement suggestion.



Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8podl9$3f8$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net>`

```
Bob,

Why don't you take the enhancement request a little further. I'm sure
Andy is omniscient and should be able to code SP2 to know what we want
and automatically generate the required panels whenever we fire it up.
This way we don't ever have to think. Oops, just thought of a catch.
We'd still have to remember to start SP2. Maybe he could make SP2 know
when to generate something without our involvement. Then it would all
be there when we sat down to write the program. Wait a minute, maybe
Andy could have it write the program too......... Yeah, that's the
ticket!

In article <39bf8f74.6104881@news.epix.net>,
  flexus.stop.the.spam at epix dot net wrote:
> Foodman <foodman123@aol.com> wrote:
>
…[69 more quoted lines elided]…
> When replying by e-mail, make sure that you correct the e-mail
address.
> Check out The Flexus COBOL Page at http://www.flexus.com
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 5)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bfbdeb.7284997@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net> <8podl9$3f8$1@nnrp1.deja.com>`

```
John Chafin <jchafin@cgwinc.com> wrote:

>Bob,
>
…[8 more quoted lines elided]…
>ticket!

John:

All of your enhancement requests above have already been scheduled for
version 73.6 which will be released on June 30, 2572.

The bad news is that it won't support Microsoft Windows anymore.
We'll only be supporting the latest and greatest operating system,
Microsoft Peephole, which allows you to really see what's going on
"behind the scenes."

You'll be happy to know that the newest version will anticipate when
you are ready to work on the software and launch itself.  It will also
include a feature which detects when you are bored and launches a web
browser which automatically takes you to your favorite entertainment
portal.

It can also be configured to automatically switch back from the
browser to your COBOL source code editor, if it senses that your boss
is on his way to your cubicle.

Oh....and at 11:55 AM each day, it will also prepare an excellent
gourmet lunch for you.  Early beta test results show that the chicken
marsala is excellent!

;-)


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ponfk$iug$1@slb6.atl.mindspring.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net>`

```
Bob,
  If you add a "pop-up" for this type of thing, why not include an "always
show" (or "never show") option on the pop-up - the way that SOME MS stuff
does?  This would allow the "user" to decide whether they do or do not want
to "default" to seeing the pop-up.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 5)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bfe28f.16666267@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net> <8ponfk$iug$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

>Bob,
>  If you add a "pop-up" for this type of thing, why not include an "always
>show" (or "never show") option on the pop-up - the way that SOME MS stuff
>does?  This would allow the "user" to decide whether they do or do not want
>to "default" to seeing the pop-up.

Bill:

Good idea.  I'll pass it on to Andy....the "keeper of the list."

Thanks!!

>
>--
…[82 more quoted lines elided]…
>

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2000-09-13T11:31:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g_Nv5.1277$Y34.625@client>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net>`

```
Bob Wolfe <flexus@epix.net> wrote in message
news:39bf8f74.6104881@news.epix.net...

> I'll pass on the enhancement suggestion.

It always comes down to this, does it not?

:-)

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 5)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bfb383.4620335@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <8pnjnk$41t$1@nnrp1.deja.com> <39bf8f74.6104881@news.epix.net> <g_Nv5.1277$Y34.625@client>`

```
"Tom Morrison" <t.morrison@liant.com> wrote:

>Bob Wolfe <flexus@epix.net> wrote in message
>news:39bf8f74.6104881@news.epix.net...
…[3 more quoted lines elided]…
>It always comes down to this, does it not?

Yup!  It's generally a matter of maintaining a list of requests
prioritized based upon the number of "votes" any particular request
receives.

It's the most democratic way to satisfy enhancement requests.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: An SP2 bug.

- **From:** "Jason S. Adams" <jsa@kona.homeip.net>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000915.001901.28819@kona.homeip.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net>`

```
In article <39be8fcc.28905401@news.epix.net>, flexus@epix.net (Bob Wolfe)
wrote:

> Tony:
> 
…[4 more quoted lines elided]…
> is added to a list of control keys in the panel definition.
 
It appears that the bug here was that the system let Tony assign
a normal letter key as function key on a panel that supported 
alphabetic data entry without even warning him that doing so would
prevent using that key to generate a normal character.  
Allowing such an assignment is fundamentally incompatible with
a data entry screen.

Yes, tony made the typo, but the degree of testing he would have to
do to prevent this bug getting out into the wild (every possible letter
and number keyed into every panel) would seem to warrant a 
check for reasonableness by the editor, and the generation of
a warning message.

Of course, you would want to be able to override the warning if
you had some valid reason not to let "Joe" enter his name in
that particular panel.  

>>I had made a typo when assigning the value to the first button and made
>>it 111 (lower-case 'o').
>>
>>Even though the button was DELETED, the program now terminates when you
>>type a lower-case 'o'.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c21dcd.479068@news.epix.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net>`

```
"Jason S. Adams" <jsa@kona.homeip.net> wrote:

>In article <39be8fcc.28905401@news.epix.net>, flexus@epix.net (Bob Wolfe)
>wrote:
…[14 more quoted lines elided]…
>a data entry screen.

Jason:

In this specific case, the pressing of the alphabetic function key
could indeed serve both purposes...i.e. 1) returning control back to
the COBOL application from the screen handler as well as 2) passing
back the actual key value to the COBOL application.

While I do agree that it is used very infrequently on data entry
screens (only when data validation must be done on a
character-by-character basis), it is used more often on entry fields
for password entry screens.

>Yes, tony made the typo, but the degree of testing he would have to
>do to prevent this bug getting out into the wild (every possible letter
>and number keyed into every panel) would seem to warrant a 
>check for reasonableness by the editor, and the generation of
>a warning message.

The only difficulty is the fact that what is reasonable for one
application may not be for another application.  Judson probably
expressed the philosophy best in his prior post when he indicated that
there are two schools of thought.  One is that the development tool
should attempt to do all things for all programmers in a pushbutton
approach and the other is that the tool should provide all of the
fundamental building blocks and allow the programmer to assemble them
in the desired fashion.  The danger of tools which try too hard to
protect the programmer from a typo is that they tend to grow into
massive applications that become restrictive rather than flexible.

A 15 second check of the panel control key list before saving the
screen definition would have displayed all control keys which have
been established for the specific screen.

The other capability offered is that the programmer has the ability to
check every panel property for each and every panel through the panel
maintenance functions.  Instead of slogging through every panel to
check the control key list, a COBOL program supplied (SP2GLOB) can be
modified to read the control key list (or any other panel
characteristic) and report the control key list back to the programmer
on a panel-by-panel basis for one panel, select panels or all panels.


In other words, the capability is there for the programmer to write
their own customized panel verification, testing and maintenance tools
for any panel property or properties desired....in COBOL.  This puts
more control in the hands of the programmer who may wish to check
every panel (and even modify every characteristic of every panel)
globally for control keys, pushbuttons captions or any other panel
characteristic.

>Of course, you would want to be able to override the warning if
>you had some valid reason not to let "Joe" enter his name in
…[6 more quoted lines elided]…
>>>type a lower-case 'o'.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: An SP2 bug.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c38366.2710566@207.126.101.100>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net>`

```
And again - there are situations where "normal" keys should return
directly to the program - and are valid as control keys.  I want to be
able to make the o return immediately.

This reminds me of the SUVs that shut off the engine if you go over 90
MPH.  Uh - I might have a REASON for doing that!  Don't protect me
from myself.

On Fri, 15 Sep 2000 00:19:02 -0800, "Jason S. Adams"
<jsa@kona.homeip.net> wrote:

>In article <39be8fcc.28905401@news.epix.net>, flexus@epix.net (Bob Wolfe)
>wrote:
…[30 more quoted lines elided]…
>>>type a lower-case 'o'.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FB97B0059D03AC96.77499B7D4653F211.BAD8A5514FF2D8A0@lp.airnews.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net> <39c38366.2710566@207.126.101.100>`

```
On Sat, 16 Sep 2000 14:29:17 GMT, thaneH@softwaresimple.com (Thane
Hubbell) enlightened us:

>And again - there are situations where "normal" keys should return
>directly to the program - and are valid as control keys.  I want to be
…[5 more quoted lines elided]…
>

Haven't you heard?  That feature on SUV's has been replaced with the
new, unselectable "SHRED TIRE WHEN GOING OVER 90" feature.


>On Fri, 15 Sep 2000 00:19:02 -0800, "Jason S. Adams"
><jsa@kona.homeip.net> wrote:
…[37 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/

          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44Rw5.6097$Ds.40651@news4.atl>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net> <39c38366.2710566@207.126.101.100>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote:
>
> This reminds me of the SUVs that shut off the engine if you go over 90
> MPH.  Uh - I might have a REASON for doing that!  Don't protect me
> from myself.

Are you kidding?  People do occasionally have to take snakebite or
severely bleeding people to the hospital.  There are places in the
American West where 100+ MPH would not be at all out of line under
those circumstances, where there isn't a hill or tree for 100 miles,
and the first tree is right beside the nearest hospital!  And in
Montana, you wouldn't even be breaking any speed limit.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q2ath$8s9$1@nnrp1.deja.com>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net> <39c38366.2710566@207.126.101.100>`

```
In article <39c38366.2710566@207.126.101.100>,
  thaneH@softwaresimple.com (Thane Hubbell) wrote:
> And again - there are situations where "normal" keys should return
> directly to the program - and are valid as control keys.  I want to be
…[4 more quoted lines elided]…
> from myself.

Hi:

Personally I think that SUVs should shut off their engines as
they reach the end of the driveway.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60F4FF896B0E4289.37A44B8E11FA4872.5C1847484F3977BC@lp.airnews.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net> <39c38366.2710566@207.126.101.100> <8q2ath$8s9$1@nnrp1.deja.com>`

```
On Sun, 17 Sep 2000 11:45:56 GMT, Foodman <foodman123@aol.com>
enlightened us:

>In article <39c38366.2710566@207.126.101.100>,
>  thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[16 more quoted lines elided]…
>

Tony, while I may not agree with your programming style, I
wholeheartedly agree with you on that.  Here in the US we have
forgotten about our dependance on foreign oil which drove gas prices
sky high in the 70's.  This prompted the car companies, with a little
nudging from the government, to produce more fuel efficient
automobiles and trucks.  But now that things are better, that has gone
out the window.   SUVs, besides being a pain in the a** to be parked
next to or be behind in traffic, are one of the most fuel inefficient
things on the planet.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: An SP2 bug.

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C61440.62007F66@brazee.net>`
- **References:** `<8pl3u5$4io$1@nnrp1.deja.com> <39be8fcc.28905401@news.epix.net> <20000915.001901.28819@kona.homeip.net> <39c38366.2710566@207.126.101.100> <8q2ath$8s9$1@nnrp1.deja.com> <60F4FF896B0E4289.37A44B8E11FA4872.5C1847484F3977BC@lp.airnews.net>`

```
SkippyPB wrote:

> Tony, while I may not agree with your programming style, I
> wholeheartedly agree with you on that.  Here in the US we have
…[6 more quoted lines elided]…
> things on the planet.

If they are taking one person down the highway to work.  But there are
occasions when they are the right tool for the job - and even instances where
they average out to be the right tool for the job (being more efficient than
two vehicles).

Programming languages have these same trade-offs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
