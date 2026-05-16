[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help needed !

_9 messages · 5 participants · 2000-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help needed !

- **From:** BF <bfloresh@ort.org.il>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C8146E.6348C43B@ort.org.il>`

```
I am an 18 year old cobol student from Israel.
Currently I am working on my project that is supposed to be finished in
two months. the cobol version that we use in school is a old version.

In my project i am designing a system that will handle data in a Burger
store (like MacDonald's and Burger-King).
i have some problems in my current program. - the current program i am
working on is a program that will accept the orders from the customers.
in that program i am supposed to do a window that will pop up when I am
going to accept the number of the product. in that window there will be
shown all the products and beside them their numbers - that way the
system's user will be able to know what is the products number.
my problem is that this window will not be very large and what i intend
on doing is that it will contain all the products and the user will be
able to press the down arrow key or the up arrow key and see ALL the
products in the window.  the problem is that i do not know how to
create such a window.

please help me ASAP.
any source codes will be gracefully accepted.

Barak.
```

#### ↳ Re: help needed !

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C8DA85.B91F616@home.com>`
- **References:** `<38C8146E.6348C43B@ort.org.il>`

```




>BF wrote:
> 
…[4 more quoted lines elided]…
>

Barak, Welcome to the club. The immediate reaction from most of us will
be here's a newbie who wants us to do his homework. So for starters :-

	1. Which machine, which COBOL and Version Number ..AND......
	2. This is a kinda "you show me yours, and I'll show you mine".
	   I'm afraid you wont get any help until we see some of your
	   code as proof that you have made an attempt.

Please don't reply to me direct - but to the NewsGroup.

Jimmy, Calgary AB

 In my project i am designing a system that will handle data in a Burger
> store (like MacDonald's and Burger-King).
> i have some problems in my current program. - the current program i am
…[14 more quoted lines elided]…
> Barak.
```

##### ↳ ↳ Re: help needed !

- **From:** BF <bfloresh@ort.org.il>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C8F0B7.59D0E40D@ort.org.il>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com>`

```
Dear James and every body whom read my e-mail,

first, i will answer your questions:

>1. Which machine, which COBOL and Version Number

I have a pentium II 450, but as for my cobol version i am not very sure of
which version is it. when i enter the editor it says "Personal Editor Version
1.0" and it is written that it is from 1982. i hope this info helps.

>2. This is a kinda "you show me yours, and I'll show you mine".
>I'm afraid you wont get any help until we see some of your
>code as proof that you have made an attempt.

hei,  i am not asking any of you cobol experts to do my homework
or something...  you see, it would be very complicated (even
impossible) for you to run my programs in your computers because
i have hebrew special codes in my program that will appear as errors in non
enabled cobol editors.  but i am only asking for help in something specific
that is a bit hard to do for a beginner like me .
as i have written before what i am trying to accomplish is a window that will
pop when the user is asked to enter the product's number - that window will
contain all the product's names and their numbers (now comes the hard part) -
this small window will be controlled by the user and he could go over all the
products by pressing on the down and up arrows and going over all the
products.

what i do not know how to accomplish is to make all the data lines of the
products move inside the small pop-up window when the user presses the arrow
keys.
i really need professional help in this.
i have attached the CBL file of the program.
i will really appreciate an help that you could offer on this.

Barak.

"James J. Gavan" wrote:

> >BF wrote:
> >
…[35 more quoted lines elided]…
> > Barak.
```

###### ↳ ↳ ↳ Re: help needed !

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C9288E.6A7D4E6E@home.com>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com> <38C8F0B7.59D0E40D@ort.org.il>`

```


BF wrote:
> 
> Dear James and every body whom read my e-mail,
…[7 more quoted lines elided]…
> 1.0" and it is written that it is from 1982. 

Am I correct in assuming that the Editor you talk about is nothing to do
with the compiler - that they are two separate pieces of software ?
Wow the Hrebrew bit I can buy. But thank you, your source gave me a
clue, PARTICULARLY :-

	CALL "COLORCNG.COM" USING .......

Are you using Ryan McFarland COBOL ? When you compile do you compile
with :-

	RMCOBOL MyProgram

and when you run it (presumably from the DOS command line) do you enter
:-

	RUNCOBOL MyProgram 

If your answers to all of the above are "Yes" - Phew !!! Where on earth
did you get it ? Was it found buried with the Dead Sea Scrolls ?
Ryan McFarland haven't supported this now for about 5 years !!!

Now the other possibility is you are using an old editor but a more
up-to-date version of RM/COBOL.

If you confirm it is Ryan McFarland, (the very old version that I think
you have), seriously I think what you are trying to achieve is way
beyond this compiler. It was a good compiler back then but doesn't even
begin to approach what compilers can do now. Ryan McFarland is now part
of Liant - if you have a local Israeli office you should talk to them.

If you are intrigued about getting into COBOL check the FAQ(Frequently
Asked Questions). Bill can you pleasse give Barak the link ?

Jimmy
```

###### ↳ ↳ ↳ Re: help needed !

_(reply depth: 4)_

- **From:** BF <bfloresh@ort.org.il>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C93ED7.55D49C0D@ort.org.il>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com> <38C8F0B7.59D0E40D@ort.org.il> <38C9288E.6A7D4E6E@home.com>`

```
Dear James,

what you said is true - i have the old version you are talking about.
And YES it is an ancient version - we use it in our school mainly
because the computer subject in israel hasn't be reformed in the last
20 years because that will cost the government a lot of money and
all the old computer teachers which have rights will have to be removed
or they will have to study new material - that is the reason why we still
use this ancient program.

i was hoping that any of you genius cobol designers could help me in
this quite simple task i am working on.
please let me know if it is too ancient for you guys to know anything about.

Barak.


"James J. Gavan" wrote:

> BF wrote:
> >
…[43 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: help needed !

_(reply depth: 5)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1n8kcsorq3tnog07od7kfgkd1up6kh2346@4ax.com>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com> <38C8F0B7.59D0E40D@ort.org.il> <38C9288E.6A7D4E6E@home.com> <38C93ED7.55D49C0D@ort.org.il>`

```
well, i don't know if this will work, but my microfocus 2.0 edition
uses

CALL "CBL_READ_KBD_CHAR" using 	char
				return-code

*char is pic x
*return-code is pic xx comp-x


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

##### ↳ ↳ Re: help needed !

- **From:** Stefan Meyer <meyerst@my-deja.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ab7c4$kld$1@nnrp1.deja.com>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com>`

```

> Barak, Welcome to the club. The immediate reaction from most of us
will
> be here's a newbie who wants us to do his homework. So for starters :-

Sorry, but I think that we should help if we can...Many times I read:
Do your homework and if you don't get it done, we will help you. It can
be very hard for newbies to get hints. And please remember: Did you
learn all by yourself?! There was no helping hand?!

> 	2. This is a kinda "you show me yours, and I'll show you mine".
> 	   I'm afraid you wont get any help until we see some of your
> 	   code as proof that you have made an attempt.

I don't want to see any coding trials if I have something he is looking
for. In this case, I have a small subprogram which will do all the
screenhandling for him. He only has to code access to the file (read
first, next, previous) within an another subprogram, which will be
called from the ScreenHandler.

The program was written using MF COBOL 3.0. Now running with MF COBOL
4.1. There's nothing special in which can't be forwarded.

Barak (or someone else), if you would like to have this piece of
code...Please let me know (Post to the newsgroup only).

HTH - Stefan Meyer

P.S.: Next week, I'll be out of the office

> Please don't reply to me direct - but to the NewsGroup.
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: help needed !

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C942F3.437A5824@home.com>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com> <8ab7c4$kld$1@nnrp1.deja.com>`

```


Stefan Meyer wrote:
> 
> > Barak, Welcome to the club. The immediate reaction from most of us
…[6 more quoted lines elided]…
> learn all by yourself?! There was no helping hand?!

Just a quick answer to that - yes I did, and there was no helping hand -
not until I got Dan McCracken's 'Structured COBOL'. No, I'm not
bragging. Quite simple - with many years of systematizing under my belt
you can count on one hand the number of interviews I have had, (over a
25-year period), down in the glorious computer saturated oil patch of
Downtown Calgary.

So to earn a living, famine and feast, primarily famine, I doggedly sat
down and taught myself COBOL. (Now watch it - don't get me going - but
what really pisses me off are all those geniuses in the Downtown area -
who know tiddly-squat and earn THREE times what I make. Classic example
- had to send some info to one over-priced helper with the title Senior
Systems Analyst, "I'll send you a zipfile via modem", I said. "No. Don't
do that", he said, "Send it by courier". I'm convinced he didn't know
how to spell the word 'modem' let alone use one ! Now I'm giving you a
clue to why I get really ticked off with some of the messages in this
newsgroup - two particular gentlemen I can think of, who have their
minds closed like a vice to OO - and I've reached the conclusion that
people like Ken Foskey trying to illustrate to these jerks, are just
wasting their time. And I have absolutely no doubt the jerks are getting
my income x 3. Now people like Judson, Howard etc., yes they don't buy
into OO but at least they do state their case with reasoned arguments -
and I respect their stand - but the jerks - they should be put out to
pasture.)

In semi-retirement mode now, if offered a job in downtown Calgary, I
would tell them they can stick it where the sun don't shine ! It has
been tough at times, and certainly most recently (bloody Windows), but
being of the stubborn ilk (shamrock country) I persisted. And I really
love this language.

Your point is valid about helping - but we do have to sort the wood from
the trees; there are some smart assess who give us the come-on. As it
turns out, we know that Barak is not one of them because he has produced
code and quite rightly can ask for help.

But as you'll see in my other post, he's on a hiding to nothing if he is
using the obsolete compiler that I think he is. But I see later from
your message that you have code he could use - hope so - I hope you
haven't got fancy END-IFS, no in-line PERFORMS in it and is it
UPPERCASE, adheres strictly to Areas A and B, verbs starting in Column
13, I could go on and on - if I'm guessing correctly his 'old' compiler
is extremely fussy about these things.

Your charitable approach to his needs deserves credit. 

Jimmy, from the 'all singing, all dancing, all BS-ing' capital of
computing in Canada.

PS : Switch off ranting mode. Now I'll go have a smoke and cool down.
```

###### ↳ ↳ ↳ Re: help needed !

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CA5894.557CAD06@zip.com.au>`
- **References:** `<38C8146E.6348C43B@ort.org.il> <38C8DA85.B91F616@home.com> <8ab7c4$kld$1@nnrp1.deja.com> <38C942F3.437A5824@home.com>`

```
"James J. Gavan" wrote:

..snip..

> clue to why I get really ticked off with some of the messages in this
> newsgroup - two particular gentlemen I can think of, who have their
…[6 more quoted lines elided]…
> be put out to pasture.)

I do not mind the comments.  I will keep going until the discussions
just burn out.  Sometimes they get to circular.

If I can continue to come up with different approaches on the answers
to quench the latest flame I might gain another convert to the OO
'light' :-}  (Are you listening Judson and Howard).

There is a raging idiot on the OO group who flames a few people like
it is a religion, I am sure he has nothing better to do.  I have
learned quite a bit as a result, the reasoned responses to him were
great.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
