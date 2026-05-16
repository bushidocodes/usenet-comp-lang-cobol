[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO Coding Techniques

_8 messages · 6 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO Coding Techniques

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CDE2AE.8F85F8F2@home.com>`

```
This one should interest you Howard - maintenance !

This was triggered off by Thane having some of my source code in OO
COBOL. He followed it through but with some difficulty. (Ken - I really
don't understand his problem - mind you I had forgotten to send him my
DBIMthd.cbl :-) )

Traditional structured - probably most of us use the technique, or
similar :-

	A1-Mainline
	 perform A100
	 perform B100
	 perform C100

	A100.
	 perform A101
	 perform A102

So our eye catches the reference to the paragraph numbering sequence and
we can work our way through the logic.

Others might use :-

	MainLine
	 Perform GetaRecord
	 Perform ReadARecord
	 Perform ........

Nothing wrong with the latter EXCEPT when they aren't listed
alphabetically - then your eyes are trolling all over the source, and
you just get madder and madder - I hate it.

Now on to OO. If I'm writing a program(class) for printing I can still
use the traditional method of naming my methods as :-

	method-id.  "P1-print-begin"
	method-id. "P900-print-heading"
	method-id. "P20-process-detail"

That's fine if you are referencing methods contained within this
class/source/self - but numbering methods is not at all a good idea if
you are going to invoke another class. While you can remember you wrote
:-

	invoke MYCustomerFile "get-name-and-address"

unless you are a real whiz, I doubt you are going to remember :-

	invoke MYCustomerFile "C100-get-name-and-address"

Now I've taken the approach in 'callable' classes of listing the
methods  for the most part, in strict alphabetical sequence. And to keep
it alphabetical I always start the OBJECT off with  :-

	method-id. "begin".

QUESTION - many (or some) of you dabble in C or C++ and maybe even some
of the other OO languages. What coding techniques do you use to easily
skip to what you are after ?

Jimmy
```

#### ↳ Re: OO Coding Techniques

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE4AC9.2E472F57@cusys.edu>`
- **References:** `<38CDE2AE.8F85F8F2@home.com>`

```


"James J. Gavan" wrote:
> 
> This one should interest you Howard - maintenance !
> 

It does - that could be a very useful thread, allowing us to set up
standards based upon real world experience - before we have that
experience ourselves.

Stress the "real world experience".  (My other need is for it to be
"enterprise level", but I will take what I can get).

(actually my biggest need on the subject really has nothing to do with
you'll (I'm not southern, so I don't know how to spell "you all") - it
will be more political)
```

#### ↳ Re: OO Coding Techniques

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE3828.C51C771A@zip.com.au>`
- **References:** `<38CDE2AE.8F85F8F2@home.com>`

```
"James J. Gavan" wrote:
> 
> QUESTION - many (or some) of you dabble in C or C++ and maybe even
> some of the other OO languages. What coding techniques do you use to
> easily skip to what you are after ?

Typically each object has it's own file.  Each file has a copybook to
define the interface.

This means that you open the copybook to find the method list.  You
should never have to open the source file except for maintenance of
extending the class.  Order of the methods in the class file are
irrelevant since you should never look at them once you have debugged
them.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: OO Coding Techniques

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE6783.176EDF59@home.com>`
- **References:** `<38CDE2AE.8F85F8F2@home.com> <38CE3828.C51C771A@zip.com.au>`

```


Ken Foskey wrote:
> 
> "James J. Gavan" wrote:
…[13 more quoted lines elided]…
> 

Sorry Ken I don't buy that one - and I damned sure Howard wont ! In
theory what you say is true BUT (a) How does a 'learner' like Thane get
a handle on how the thing is put together, where are his eyes supposed
to wander and (b) If you have destruction tested - then you shouldn't
need to crawl all over the thing. But I'm with Howard on this - (b) is
not the real world.

OK - put it another way Ken. Trying to assimilate the source I gave you,
the version prior to the one I've given Thane - did you grasp what my
code was about or did you have real difficulty sorting it out - if the
latter, then there is something missing.

So come on folks just how do you code in OO to help the 'reader' ?

Jimmy
```

###### ↳ ↳ ↳ Re: OO Coding Techniques

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ce6f73.482412782@news.cox-internet.com>`
- **References:** `<38CDE2AE.8F85F8F2@home.com> <38CE3828.C51C771A@zip.com.au> <38CE6783.176EDF59@home.com>`

```
On Tue, 14 Mar 2000 16:27:08 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:
Posted and mailed.
>
>
>Ken Foskey wrote:
>> 
>> "James J. Gavan" wrote:

>Sorry Ken I don't buy that one - and I damned sure Howard wont ! In
>theory what you say is true BUT (a) How does a 'learner' like Thane get
…[4 more quoted lines elided]…
>

*IF* the MF source was source compatible with Fujitsu I could have
loaded the repository information into the Fujitsu class browser
(really neat BTW) and viewed the structure.

Understanding your code was no harder, or easier, than any one of a
number of alien systems I have examined and/or ported to my
enviornment.  In almost all cases I have been able to simplify these
systems to a great degree.  That is because these systems developed
and extended over time, while I have the luxury of looking at how
things are now.

At any rate, I was able to understand your code once I had all the
source.  Makes a big difference.

Also, I was looking for something in particular.  I wanted to see what
it would take to extend your file access methods for a new file -- the
rest of it was just distraction to my exercise.
```

###### ↳ ↳ ↳ Re: OO Coding Techniques

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8am3gk$n22$1@slb0.atl.mindspring.net>`
- **References:** `<38CDE2AE.8F85F8F2@home.com> <38CE3828.C51C771A@zip.com.au> <38CE6783.176EDF59@home.com> <38ce6f73.482412782@news.cox-internet.com>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in message
>
> *IF* the MF source was source compatible with Fujitsu I could have
> loaded the repository information into the Fujitsu class browser
> (really neat BTW) and viewed the structure.
>

For those who haven't read my IBM "enhancement request" post, you probably
should see that having a GOOD "class browser" is critical to any OO
implementation.  Having a "cross-language" one seems the only way to move to
multi-language use of "common" class libraries.
```

###### ↳ ↳ ↳ Re: OO Coding Techniques

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE9FA0.605AD5C@home.com>`
- **References:** `<38CDE2AE.8F85F8F2@home.com> <38CE3828.C51C771A@zip.com.au> <38CE6783.176EDF59@home.com> <38ce6f73.482412782@news.cox-internet.com> <8am3gk$n22$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Thane Hubbell <thaneH@softwaresimple.com> wrote in message
…[9 more quoted lines elided]…
> multi-language use of "common" class libraries.

Like Fujitsu, NetExpress also has a nifty class browser - but I don't
use it. Different strokes for different folks. Duh, duh, duh. To get the
hang of it, I really need to follow it through, laboriously,
step-by-step. As an overall concept of how the thing is put together -
well perhaps I should have used the browser to do that.

Reassuring that Thane didn't find my code confusing. Let's see how Ken
responds. Let's chuck another one into the pot. Bob, what is your shop
standard for putting SP2 together with C. No, this isn't a plug for SP2
so you can happily contribute - just what are your techniques. 

Just to show we aren't being narrow minded down to one product, Kevin,
if you're looking in, how are you doing it with Norcom - but I think you
are using the CA version of Visual Basic.

Let's also see if we can get the artist to demonstrate how he uses his
paintbrush. Michael, what sort of coding technique do you use with Basic
to jump to the equivalent of a perform etc., so that I can easily follow
the logic of your code ?

Perhaps there is one area we should zero in on because the concept
applies to both structured or OO. You must make the distinction between
:-

- Business classes/programs (the ones you and I are writing so 	we can
edit, process, print etc.)

- 'Support' classes/programs - either invoked or called - read files,
get date routines, whatever

The 'Support' category doesn't have quite the same urgency as 'Business'
for standardization - you can probably follow your way through the logic
from one method/paragraph to another, because it is all related to one
topic.

Back to the 'Business' group - The guy in maintenance is given a
problem, "The program is doing this and it shouldn't be.......". Now
depending upon his familiarity with the application, he might have the
savvy to twig from your description that the problem might be in one of
the 'support' classes, and goes directly to it. I would suggest most
times though, that he will start with the 'Business' program/class that
is causing the problem.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Coding Techniques

_(reply depth: 6)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cfb996.12966698@news.epix.net>`
- **References:** `<38CDE2AE.8F85F8F2@home.com> <38CE3828.C51C771A@zip.com.au> <38CE6783.176EDF59@home.com> <38ce6f73.482412782@news.cox-internet.com> <8am3gk$n22$1@slb0.atl.mindspring.net> <38CE9FA0.605AD5C@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

>
>
…[23 more quoted lines elided]…
>so you can happily contribute - just what are your techniques. 

If you are asking how sp2.dll is written, interestingly enough we
don't use any C++ class libraies (no MFC42.DLL's in our distribution
files).  We write plain vanilla C language modules which invoke
individual Windows API code directly.  In character mode, we either
write directly to the video buffer (DOS) or utilize terminal
information files (termcap, terminfo, etc.) in UNIX environments.
That allows us to remain independent of any Microsoft or vendor
specific libraries which may come back to bite us in the rear end in
the future.

>Just to show we aren't being narrow minded down to one product, Kevin,
>if you're looking in, how are you doing it with Norcom - but I think you
…[30 more quoted lines elided]…
>Jimmy



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
