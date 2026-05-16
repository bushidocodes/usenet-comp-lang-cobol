[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMPARISON OF OO APPROACHES

_4 messages · 3 participants · 2010-02_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### COMPARISON OF OO APPROACHES

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-24T20:57:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cymhn.143613$OX4.134534@newsfe25.iad>`

```
Monsieur Dashwood,

OK. We don't need a pissing contest about the virtues of doing OO in a 
particular way. Early January, one of the RARE messages was posted in 
the M/F Forum, asking how the newcomer could handle what he wanted to do 
with messageboxes. Again one of those generalised questions showing no 
intent which path he was thinking of following. He referred to a 
zipfile. Well, when I found the zipfile, no wonder he couldn't 
comprehend. It did the job in three ways, but it was horrible and most 
certainly not OO in any shape or form. As best I could, I gave him the 
following demo for Messageboxes, in OO style, no dialogs required, just 
the M/F Messagebox class.

On reflection, I could have probably made it simpler, (using Procedural 
to get at the OO Classes). Here's a spec of what it does - produces 
various messageboxes of varying sizes and content, the type Icons, 
(Info, Warning etc.) and necessary Pushbuttons.

The sample messageboxes it churns out are as follows, no reference to 
Dialogs or files systems; A/C # and Names are hard coded-into the 
application; don't need to worry about names, but they are there to 
illustrate what the developer can do. Similarly file-status codes, (or 
could be SQLSTATE or SQLERROR) are not included.

1. Show Movable :
	Text saying use the Title bar to drag around the screen. "Try it
	before clicking OK Button"

2. Dialog Errors
	(a) Customer accidentally deleted existing name leaving it blank
	(b) Error on a Zipcode (assuming US numeric code)
	(c) Wrong value for a Credit Rating Code
	(d) User clicks on Delete button in the dialog -
		Message "Are you sure you want to Delete this
		record(Row)y/n ?"

3. File Processing :
	(a) File not found - after doing a CBL_CHECK_FILE_EXISTS.
	(b) Error - ISAM - found a Duplicate Key where NOT allowed

4. Final Message :
	That's it. Do you want to re-run demo or STOP RUN ?

As I indicated above, I'm not attempting to confuse the new developer 
with classes for file/DB handling or dialogs. The info is hard coded in 
the test. I do indicate universality, by including my FileErrors class, 
to come up with literals for file status codes - where these are passed 
to the same common MyErrors which ties into the M/F Messagebox class.
(The FileErrors is an addendum and not part of the project; same would 
apply using SQLERRORS/SQLSTATE).

Now above is in no way tricky - but it can be used to illustrate either 
  your component approach, or my class/method approach. I'm one step 
ahead, because I've already written above and it's in a zipfile dated 
2009 Jan 23 - which I promise I wont change, having seen your code.

Yes, this is by no means a priority so far as you are concerned. But 
given that you keep spieling about components, are you prepared to give 
it a shot in your own timescale. This would be the very first TIME I 
would have seen a full-fledged use of your components.

Firstly one very specific rule. This, like it or not is a COBOL User 
Group. I don't want to see a single line of Java, C or .Net. That 
approach just doesn't allow for a fair comparison. Now after you have 
done it, if you like, at a later date give us a .Net version.

Are you game ?

As you said to Richard "Put up or shut up". Silly challenge - we know 
what he did.

You first, then I show you mine :-). We could attach zipfiles to 
messages here, (which some wont like), or you could initially put yours 
on Prima Computing and once published for others to see, then add mine. 
Play it as you see fit.

- - - - - - - - -- - - - - - -- - - - - - - - -- - - - - - - -- - - - -

PS: Please don't try and get smart and throw in the suggestion we should 
tackle SQL usage, Dialogs and God knows what else. I side-stepped from 
my DateAndTime to produce above. I've done a considerable amount of 
backtracking thoughts on other topics in terms of fine tuning them, 
adding additional features etc., and I'm not going to rush around in 
circles competing - but am quite happy to show my re-vamps as and when 
ready after thorough testing.

The re-vamps and the objective. You know just as well as I do there are 
not sufficient examples which will help the uninitiated COBOL programmer 
to get into OO COBOL. Never mind you might reply, "Use .Net". 
Introductory material in a language they already understand allows them 
to then think in terms of Java, .Net or whatever. Very specifically my 
code is using M/F's Net Express plus every extension and trick in the 
book to simplify the coding. Richard's remark about you  being 
disingenuous when saying COBOL is just too verbose - I'm sure you've 
taken note of my very 'complex' Get Day or Month Names in the class 
DatesPortuguese. And as for End-Invoke - never used it, even if you 
claim it "is best practice'. That End-invoke can double your number of 
lines of code or very close to doubling.

Spent the year in the garden until a fairly early frost in September 
last year which zapped the zucchini/courgette leaves. Pick the few 
remaining runner beans and call it quits. Then in slow motion got back 
to programming.

Step 1 - MyDialog - as indicated elsewhere got into MyDialog which 
handles all controls, with the qualifier about Treeviews and ListViews. 
It works but I want to thoroughly test.

Step 2 - Common Dialogs - I wanted to add features to Step 1 - colouring 
and fonts. Thought on it and back stepped to # 2 to handle Common 
Dialogs, which of course also suggests doing demos on file 
opening/saving. For the colouring/fonts I worked on the idea to give a 
developer a choice of which colours/fonts he wants to hold as his 
'favourites' - write the appropriate combinations to an keyed file so 
they can be retrieved from MyDialog by their identifying code. I give a 
backup file on their favourites and date/time stamp it in the heading.

Step 3 - DateAndTime - sure I had a class for Dates related solely to 
CCYYMM - days not required for the Corrosion application; time 
calculations are measured in months. Similarly I already had a date 
routine to give me the header date block, but then I started looking at 
the ACCEPT FROM and Date Functions.

See where I'm coming from ? - Started in the 1,2 3 sequence as the 
initial thought process, but now I'm designing/programming in the 
forwards sequence 3, 2 and then 1.

As regards to what I'm doing with 1, 2 and 3 - The Brazilian who came in 
here a short while back, (Emerson Lopes, 100 Cool Things you can do in 
COBOL), quite happy to host OO stuff on his site; he's an IBM employee 
using Fujitsu for PC. The idea got mentioned way back in the past, Rene 
in the Philippines would also probably host it when I ask him.

Jimmy
```

#### ↳ Re: COMPARISON OF OO APPROACHES

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-26T04:03:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7unhqiFn3rU1@mid.individual.net>`
- **References:** `<Cymhn.143613$OX4.134534@newsfe25.iad>`

```
James J. Gavan wrote:
> Monsieur Dashwood,
>
> OK. We don't need a pissing contest about the virtues of doing OO in a
> particular way.

No. Absolutely.


>Early January, one of the RARE messages was posted in
> the M/F Forum, asking how the newcomer could handle what he wanted to
…[47 more quoted lines elided]…
>  either your component approach, or my class/method approach.

But the problem here,Jimmy, is that you really don't have a grasp of what 
component based design and programming is all about. If you did, you'd 
realise immediately that using components and classes/methods are not 2 
mutually exclusive choices; they are aspects of the same thng. I use "your" 
classes/methods approach (although not in exactly the same way you do) all 
the time. But I also find components extremely useful and have done for over 
a decade now. The Component Object Model is exactly that. A model easily 
implemented in Object Oriented Programming.. It EXTENDS your clases/methods 
so they can run anywhere and interect with similar components written in 
other languages. Why would that not be a good thing?

I'm not looking for a programming contest (even if I had the time, which I 
honestly don't...), and I don't understand why you are.

What are you seeking to prove?

That writing classes/methods in COBOL is a great way to develop computer 
systems? (I'll gree it isn't a bad way, but there are much better ways...)




>I'm one
> step ahead, because I've already written above and it's in a zipfile
> dated 2009 Jan 23 - which I promise I wont change, having seen your
> code.

I don't know what code you're referring to.

>
> Yes, this is by no means a priority so far as you are concerned. But
> given that you keep spieling about components,

Jimmy, you are hopelessly out of date. I gave up "spieling about components" 
around the same time I gave up "spieling about OO in COBOL".

(It was YEARS ago...)

I really DON'T CARE what approach other people use. (although I'm always 
interested to see stuff). I'm happy to mention what I'm trying to do and 
what tools I use to do that, and whether I find them useful or not, because 
it is a technical forum primarily (although the OT posts are often much more 
interesting than the technical ones) and, sometimes, people find stuff 
useful.

I already had private mail about the GUID stuff thanking me for posting it. 
There are people who don't want to participate publicly. (You can't really 
blame them, can you...? :-)). For example, of the couple of hundred people 
who have downloaded the COBOL structure tool, I recognised 5 names. There 
are a large number of  "lurkers" here.

Several people in Europe have requested the DECLGEN tool and I have promised 
to make it available. (It is currently integrated into the PRIMA Toolset and 
there is probably a day's work in "disintegrating" it and posting it to the 
web site. :-))

I had mail yesterday from someone in South America who wants to know how to 
send email from PowerCOBOL. I simply haven't got the time I would like to, 
to give detailed examples and there are already several things on the TODO 
list (including finding the ACE code for Philip - don't give up on it 
Philip; I haven't forgotten...)

The point I'm gently trying to make is that there are REAL thngs that people 
actually want to DO. That has to take priorty over an intellectual 
discussion on "COMPARISON OF OO APPROACHES". (Shouting original)



>are you prepared to
> give it a shot in your own timescale. This would be the very first
> TIME I would have seen a full-fledged use of your components.

Well, firstly, I don't care if you have never seen components in use, 
secondly, I don't know what you are referring to, thirdly, I have no reason 
to persuade you (or anybody else) as to the merits of COM objects (or even 
other types of component); all Iwill say is I find that approach to be 
extremely useful. No-one is paying me to Evangelize it... :-) So, I guess 
I'll have to decline...

(BTW, the component based approach is not "mine" any more than 
classes/methods is "yours". Thousands of people use these approaches every 
day and they are all quite able to peacefully co-exist... :-))


>
> Firstly one very specific rule. This, like it or not is a COBOL User
…[4 more quoted lines elided]…
> Are you game ?

No. It isn't about being game. It is about the best use of resources.
>
> As you said to Richard "Put up or shut up". Silly challenge - we know
> what he did.

Again, I have no idea what the context to this is. Can you not cite or quote 
stuff, Jimmy?
>
> You first, then I show you mine :-). We could attach zipfiles to
> messages here, (which some wont like), or you could initially put
> yours on Prima Computing and once published for others to see, then
> add mine. Play it as you see fit.

I see fit not to play. (I really don't understand what the game was supposed 
to be about and that is usually a disastrous way to approach any kind of 
game.)

<snipped >
```

##### ↳ ↳ Re: COMPARISON OF OO APPROACHES

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-25T10:56:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KQyhn.9481$AF1.528@newsfe12.iad>`
- **In-Reply-To:** `<7unhqiFn3rU1@mid.individual.net>`
- **References:** `<Cymhn.143613$OX4.134534@newsfe25.iad> <7unhqiFn3rU1@mid.individual.net>`

```
Pete Dashwood wrote:
> James J. Gavan wrote:
> 
…[8 more quoted lines elided]…
> 
Beautifully done. Chicken. So as you can't see any reason why you should 
"Put Up", I suggest you "Shut Up" ! I will merely say of the following 
that you have a neat way of using an On/Off button on being obtuse. You 
have it in the ON mode below.

Now back to your two latest snotty message. You hate Tony Dilworth - 
wait until you see my response to those !

Jimmy
> 
>>Early January, one of the RARE messages was posted in
…[168 more quoted lines elided]…
> <snipped >
```

##### ↳ ↳ Re: COMPARISON OF OO APPROACHES

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-25T18:04:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hm6e4b$bi4$2@reader2.panix.com>`
- **References:** `<Cymhn.143613$OX4.134534@newsfe25.iad> <7unhqiFn3rU1@mid.individual.net>`

```
In article <7unhqiFn3rU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>James J. Gavan wrote:
>> Monsieur Dashwood,
…[4 more quoted lines elided]…
>No. Absolutely.

[snip approx. 50 lines of technical explanation and three approaches]

>> Now above is in no way tricky - but it can be used to illustrate
>>  either your component approach, or my class/method approach.
>
>But the problem here,Jimmy, is that you really don't have a grasp of what 
>component based design and programming is all about.

Curious value of 'absolute' there, aye.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
