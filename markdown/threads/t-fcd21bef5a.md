[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New to Fujitsu Cobol - need some help

_22 messages · 11 participants · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### New to Fujitsu Cobol - need some help

- **From:** "Hansjoerg Kaempf" <hjkaempf@wfeca.net>
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<930243064.873.28@news.remarQ.com>`

```
My Project:       Programming a Menu Structure

1. Main Menu with:     5 submenu-choices, Help, and Esc

2. Sub Menus:         calling programs

My Problem:    1. How do I accept a sub-program choice in the main menu?
                          2. How to program the Esc for exiting the program?

Thank you for any help.

Hansjoerg
```

#### ↳ Re: New to Fujitsu Cobol - need some help

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jxtc3.1682$4e1.79864@iad-read.news.verio.net>`
- **References:** `<930243064.873.28@news.remarQ.com>`

```
In article <930243064.873.28@news.remarQ.com>,
Hansjoerg Kaempf <hjkaempf@wfeca.net> wrote:
>My Project:       Programming a Menu Structure

Please do your own homework.

DD
```

##### ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** "Jason Bailey" <jbailey5@earthlink.net>
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ku4va$17c$1@ash.prod.itd.earthlink.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net>`

```
Docdwarf,
    I thought the whole purpose of newsgroups was to exchange information.
What is easy for me might not be easy for you and vice versa.
    Nearly 99% of everything asked here (and answered concisely, I might
add) need not be asked if the person posting had researched it themselves,
yet you say nothing to them.  When someone asks a question about escape key
logic and sub-menu routines you flame them, but I suppose if someone asks a
question about object-oriented design implementation then that's alright.
Strange where you draw the line.
    There are many students who visit this newsgroup for insight from pros
like ourselves.  They need nurturing as they grow not snide comments.  I for
one call for anyone to post any question relating to COBOL in this forum.
This is a forum of knowledge and as such there should never be a stunting of
exchange of commentary.
    Lighten up and if you don't want to help someone, then don't.  There's
certainly no guns to heads here.  But quit with the "Do your homework!"
posts.

    Regards,

    Jason Bailey
    Systems Analyst
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ku93j$3pk@dfw-ixnews4.ix.netcom.com>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net>`

```
Jason Bailey <jbailey5@earthlink.net> wrote in message
news:7ku4va$17c$1@ash.prod.itd.earthlink.net...
> Docdwarf,
  <all original comments snipped>

Althought I sometimes (often?) disagree with DD's posting of his standard
"Do your own homework," I agree with it completely in this case (where the
student did not show any process of getting where they were).  Should there
be any question about the general issue of "homework questions" in this NG,
the following is (verbatim) what the COBOL FAQ says on the topic.  (You be
the judge of how the original question fits this.)

"18.1 Can I get help with homework via the newsgroups?

Yes, you can get help with your homework via these newsgroups. HOWEVER, that
does mean that you will receive help - you will NOT find many participants
who will be very happy if you ask them to do your homework FOR YOU. Some
hints that you should consider when drafting your post for assistance with
homework include:

 - Make it clear from the beginning that you are asking for homework help.
(Most of the newsgroup participants are very good at sniffing out those who
try and pose homework questions as "business need" questions - and they are
not very polite in replying to such questions).

  - Make certain that you specify what compiler and operating system your
homework is targeted at. Solutions may vary significantly based on this.
(You might also want to include what text book you are using.)

 - The more information that you can give that demonstrates that you really
have tried to solve the problem yourself (using your text book, class
material/presentations, lab assistance, etc), the more likely it is that you
will get useful and friendly responses. If you let us know what you have
found on your own and why you are still uncertain or confused, you will
usually get helpful responses; if it looks like you are asking us questions
without trying to solve it yourself, you are likely to get very pointed
replies.

NOTE: if you are looking for a COBOL tutor, (and don't want to see the "Do
your own homework" notes that occur in the COBOL newsgroups), you might want
to try,

   http://www.tutoraid.org/

"
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37761c8a.288672584@news1.ibm.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <7ku93j$3pk@dfw-ixnews4.ix.netcom.com>`

```
Sometimes you don't know the whole store.  Hans is working "on his
own" and had an idea he wants to code.  He is not working on a
"School" homework assignment, and really does want a pointer in the
right direction. 

I have been in e-mail convresations with him since he bought my book.
I think, that if he will review chapter 23, he will find the answer to
his questions, with the esception of the ESC key.  

On Thu, 24 Jun 1999 16:47:46 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Jason Bailey <jbailey5@earthlink.net> wrote in message
>news:7ku4va$17c$1@ash.prod.itd.earthlink.net...
…[49 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rgpd3.13781$4e1.117086@iad-read.news.verio.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <7ku93j$3pk@dfw-ixnews4.ix.netcom.com> <37761c8a.288672584@news1.ibm.net>`

```
In article <37761c8a.288672584@news1.ibm.net>,
Thane Hubbell <redsky@ibm.net> wrote:
>Sometimes you don't know the whole store.  Hans is working "on his
>own" and had an idea he wants to code.  He is not working on a
…[5 more quoted lines elided]…
>his questions, with the esception of the ESC key.  

Mr Hubbel, a most interesting series of statements... now, pray tell,
given what has been available for all to read here on the newsgroup what,
outside of a Great Act of Charity, would have allowed anyone else to come
to a similar conclusion?

DD
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7l5d9k$m52$1@news.igs.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <7ku93j$3pk@dfw-ixnews4.ix.netcom.com> <37761c8a.288672584@news1.ibm.net> <Rgpd3.13781$4e1.117086@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message ...

>Mr Hubbel, a most interesting series of statements... now, pray tell,
>given what has been available for all to read here on the newsgroup what,
>outside of a Great Act of Charity, would have allowed anyone else to come
>to a similar conclusion?
>
Not to quibble Doc, but what, outside your preconceived ideas, led you to
believe otherwise? Note that there are lots of times I agree with you, and I
also tend to ignore rather stupid and/or trivial questions, particularly
when the answer can be found in any reference manual.

However, that is often not the case, and often even silly "problems" can
stump and experienced programmer for a variety of reasons, including simple
terminal blindness.  After all, every problem is trivial once you know the
answer.

An example is a similar answer that you gave yesterday on the status "02:"
problem for a sequential read.  Normally, I would have ignored it. You told
Mike to do his own homework.  I answered.  The reason is simple.  I know
that Mike is a *very* competent programmer.  I also knew he was coding in
the field, in a shack at the bottom of a quarry, with no manuals.  The
reason that I know all that is because he is my employee, and my phone was
off the hook.

Assumptions, Doc.
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3773088E.95714824@home.com>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net>`

```
Jason Bailey wrote:
> 
> Docdwarf,
…[20 more quoted lines elided]…
>     Systems Analyst

Hope Jason's comments don't turn into a free for all !

As a newcomer to the forum I quickly formed the impression that some
people were bloody rude - "Can we decompile our programs. Am I being
silly ?" to which came the reply "No, not silly. Ignorant." I laughed
but the reply was cruel.

Simple rule, "Do to others what you would like them to do to you".
I know only two languages, English and COBOL - and after some thirty
years I'm still learning both.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 4)_

- **From:** "Simon Hart" <hart1@technologist.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3yKc3.3074$BS6.2552@wards>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <3773088E.95714824@home.com>`

```
> Hope Jason's comments don't turn into a free for all !
>
…[9 more quoted lines elided]…
> Jimmy, Calgary AB


Its very simple, only post when you have useful information.

The orig, post,

You are talking about menus drop down menus, I presume, what compiler?
what type of technology?.

Simon Hart
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LwPc3.430$Br.4173@news1.mia>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <3773088E.95714824@home.com> <3yKc3.3074$BS6.2552@wards>`

```
Simon Hart wrote:
>
>You are talking about menus drop down menus, I presume, what compiler?
                                                         -------------


Look at the subject line in your reply. ;-)
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SvLc3.130$wC4.3932@dfiatx1-snr1.gtei.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net>`

```
Here, Here!
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hMc3.1849$4e1.92916@iad-read.news.verio.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net>`

```
In article <7ku4va$17c$1@ash.prod.itd.earthlink.net>,
Jason Bailey <jbailey5@earthlink.net> wrote:
>Docdwarf,
>    I thought the whole purpose of newsgroups was to exchange information.

What something's 'purpose' is and what it gets used for may or may not be
the same thing... but that is Philosophy and there's time for that later.

>What is easy for me might not be easy for you and vice versa.

Precisely... but what is easy for many folks, it seems, is the plea of 'Do
my homework/job for me'... sometimes they even manage to remember the
'please'!

>    Nearly 99% of everything asked here (and answered concisely, I might
>add) need not be asked if the person posting had researched it themselves,
…[3 more quoted lines elided]…
>Strange where you draw the line.

Strange what you remember and call 'flaming'; if you believe that the
statement of:

'Please do your own homework'

is 'flaming' then I wonder what you make of

'Please pass the salt'

... but, be that as it may, permit me to ask... do you recall seeing me
respond to a posting which contained a snippet of code, or even a URL
directing one towards code, with 'Do your own homework'?  I don't.

If effort has been shown I respond with effort... if someone asks 'Where
do I find sample code to do a match/merge program on two sequential input
files... just so I can read it, of course' or 'What does File Status 39
mean?... well, the first is a standard bit of homework and the second
found in a manual.

>    There are many students who visit this newsgroup for insight from pros
>like ourselves.  They need nurturing as they grow not snide comments.

'Nurturing'?  Do you *honestly* want to encourage folks into your
profession who show absolutely no initiative aside from 'How do I do
this?'?  It may make *you* feel all warm and fuzzy if you get treated as a
Walking Manual/Textbook... me, it leaves cold.

>I for
>one call for anyone to post any question relating to COBOL in this forum.

You can call for Phillip Morris, for all I care, and you are welcome to do
so... but if it appears to me that someone is asking me to do homework I
will request otherwise.

>This is a forum of knowledge and as such there should never be a stunting of
>exchange of commentary.

Ummmmm... why are you so concerned with the commentary I am exchanging?

>    Lighten up and if you don't want to help someone, then don't.  There's
>certainly no guns to heads here.  But quit with the "Do your homework!"
>posts.

Please do not stunt my commentary.

DD
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7l0msv$q19$1@news.igs.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <6hMc3.1849$4e1.92916@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message <6hMc3.1849
>
>If effort has been shown I respond with effort... if someone asks 'Where
…[3 more quoted lines elided]…
>found in a manual.


Hey Doc, do you know where I can find sample OOP code?  Just a mainline that
invokes a "hello world" as OOP method one and "goodbye world" as OOP method
two, along with the source for both the mainline and the OOP DLL?  Just so I
can read it, of course ...
<G>
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3773F639.153FCD45@home.com>`
- **References:** `<930243064.873.28@news.remarQ.com> <jxtc3.1682$4e1.79864@iad-read.news.verio.net> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <6hMc3.1849$4e1.92916@iad-read.news.verio.net> <7l0msv$q19$1@news.igs.net>`

```
donald tees wrote:
> 
> Hey Doc, do you know where I can find sample OOP code?  Just a mainline that
…[3 more quoted lines elided]…
> <G>

Some people can be really tiresome ! Yes I'm pro-OO, write in it all the
time. Can't stand the thought of you remaining uninformed any longer.
Don't you know that the following two-liner will compile and run in
Microfocus :-

		display "Hello World"
		display "Goodbye World"

Nah ! Aint gonna waste my time putting it in OO syntax for you - and a 
DLL - forget it.

<G> - Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CR4d3.8031$4e1.105564@iad-read.news.verio.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <7ku4va$17c$1@ash.prod.itd.earthlink.net> <6hMc3.1849$4e1.92916@iad-read.news.verio.net> <7l0msv$q19$1@news.igs.net>`

```
In article <7l0msv$q19$1@news.igs.net>,
donald tees <donald@willmack.com> wrote:
>
>docdwarf@clark.net wrote in message <6hMc3.1849
…[12 more quoted lines elided]…
><G>

Truth be known, Mr Tees... I wouldn't know such things if they jumped up
and bit me on... sensitive areas.  When I've the need to learn them, of
course, it will be another story; until then... well, until then I'm
working on a contract, *right now*,  where the Default Compiler i
IKFCBL00.

DD
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

- **From:** jamapo@webtv.net (Brandy Poo)
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<15269-377550E6-121@newsd-172.iap.bryant.webtv.net>`
- **References:** `<7ku4va$17c$1@ash.prod.itd.earthlink.net>`

```
I agree, if you're not willing to try to help someone, why bother to
respond at all.  I don't know the answer to his question, but I have
books to look it up.  As a student myself, I know that it takes some
VERY specific information to be able to "do someone else's homework."
My professors put in some very particular stipulations for doing an
assignment.  Someone could give you some guidelines, but it would be
pretty hard to "do it for them."
```

###### ↳ ↳ ↳ Re: New to Fujitsu Cobol - need some help

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xWed3.12453$4e1.112345@iad-read.news.verio.net>`
- **References:** `<7ku4va$17c$1@ash.prod.itd.earthlink.net> <15269-377550E6-121@newsd-172.iap.bryant.webtv.net>`

```
In article <15269-377550E6-121@newsd-172.iap.bryant.webtv.net>,
Brandy Poo <jamapo@webtv.net> wrote:
>
>--WebTV-Mail-725248485-7578
…[4 more quoted lines elided]…
>respond at all.

There are times when a reminder that one 'ain't gettin' away with that
here' is helpful... and to remind one that self-reliance is frequently
paramount can be helpful, as well; 'help' comes in a variety of types.

DD
k
```

#### ↳ Re: New to Fujitsu Cobol and to COBOL programming - need some help

- **From:** "Hansjoerg Kaempf" <hjkaempf@wfeca.net>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<930362951.962.18@news.remarQ.com>`
- **References:** `<930243064.873.28@news.remarQ.com>`

```
I bought 2 books (COBOL in 24 hours and COBOL unleashed) installed the
compiler
which came with the books and started to learn. So far all the examples of
the first
book work as expected. The second book is harder to understand for a
beginner
and it is not really a book to start with.
Then I tried to program a menu structure with submenus which call programs.
The menus and the submenus look the way they should, but they don't work.
After days and days trying to find a solution I decided to post the message
below
hoping somebody would give some advise how to come to the solution.
The first reaction came from an obviously retarded person, recommending
to do my homework even when this retardee didn't had any background
information
about me.
Other reactions were comments about the retardee and nobody seems to be
willing
to give advise. I wonder what usergroups are here for when not for helping
each
other.

And then there were the exceptions, some real nice people responded also and
one
of them sent me an address where I possible could get help for my problem.

I'm sure the reaction to my posting is not representative for COBOL
programmers
and I know there are more nice and professional people in this business but
maybe
not in this usergroup?

H. Kaempf


Hansjoerg Kaempf wrote in message <930243064.873.28@news.remarQ.com>...
>My Project:       Programming a Menu Structure
>
…[5 more quoted lines elided]…
>                          2. How to program the Esc for exiting the
program?
>
>Thank you for any help.
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: New to Fujitsu Cobol and to COBOL programming - need some help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37751C08.B6F257C6@home.com>`
- **References:** `<930243064.873.28@news.remarQ.com> <930362951.962.18@news.remarQ.com>`

```
Hansjoerg Kaempf wrote:

> ...........
> >My Project:       Programming a Menu Structure
…[13 more quoted lines elided]…
> >
Hans,

Your last set of comments were valid - BUT - given the many options,
when posting to this forum give us the Compiler and Operating System you
are using. There's a BIG difference if you are talking DOS text and
SCREEN SECTION as opposed to using Windows GUIs - and the toolkit used
to produce your menu. Then somebody who "matches" what you are using can
respond to your query.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: New to Fujitsu Cobol and to COBOL programming - need some help

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ry4d3.155$Lh3.4431@dfiatx1-snr1.gtei.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <930362951.962.18@news.remarQ.com>`

```
NG participants are much like used-car salesmen, lawyers and even
politicians.

The vast majority are honest, ethical, hardworking, ethical, helpful
professionals.

A very visible minority are not.
```

##### ↳ ↳ Re: New to Fujitsu Cobol and to COBOL programming - need some help

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B_4d3.8105$4e1.105692@iad-read.news.verio.net>`
- **References:** `<930243064.873.28@news.remarQ.com> <930362951.962.18@news.remarQ.com>`

```
In article <930362951.962.18@news.remarQ.com>,
Hansjoerg Kaempf <hjkaempf@wfeca.net> wrote:

[snippage]

>Then I tried to program a menu structure with submenus which call programs.
>The menus and the submenus look the way they should, but they don't work.
…[6 more quoted lines elided]…
>about me.

Gosh... you mean you 'tried to program a menu structure with submenus',
got told to do your own homework and you first response was *not* 'Look, I
*am* trying to do my own homework... *this* is what I've done and I cannot
get it to work!'?

Please do your own homework.

DD
```

##### ↳ ↳ Re: New to Fujitsu Cobol and to COBOL programming - need some help

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%Q5d3.3733$nN3.22476@news3.mia>`
- **References:** `<930243064.873.28@news.remarQ.com> <930362951.962.18@news.remarQ.com>`

```
Hansjoerg Kaempf wrote:
>I bought 2 books (COBOL in 24 hours and COBOL unleashed) installed the
>compiler which came with the books and started to learn. So far all
…[4 more quoted lines elided]…
>should, but they don't work.

When you say "they don't work", I'm not sure if you mean your menu
structure doesn't work, or that the subprograms aren't called when you
select them.  If the menu structure doesn't function properly, then
COBOL Unleashed chapter 25, "Character and Screen Based Interfaces",
covers this topic.  The sample program, a simple name and address
database, can be found on the CD as \source\CHAP25\NAMES.COB.  Of
course, there are a gazillion ways to do anything, but if you follow
the methods used in NAMES, your menu structure will work, just as
NAMES works.  If your menu structure works but the subprograms aren't
being executed, then it could be any of a whole range of possible
issues.  We need more info.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
