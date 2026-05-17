[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Possibly humorous

_6 messages · 3 participants · 2015-07_

---

### Possibly humorous

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2015-07-03T04:02:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com>`

```
This is vaguely work related but definitely COBOL related.

The company mentioned sells products/services for analyzing software
source code. They will also analyze mainframe COBOL legacy code. I
thought this blog was worth a chuckle.

http://qualilogy.com/en/sonar-cobol-what-you-need-to-know/

== begin quote ==

Now, as someone said recently: “We’ve got Sonar analysis well under way
there. We’re contemplating putting Cobol under analysis as well, but I
don’t understand the mainframe side and the Cobol-ers don’t understand
the Jenkins & Sonar side”.

So, let’s try to help. This post (and following ones) has the objective
to describe what you should know to implement a process of Cobol code
analysis with Sonar and Jenkins.

I will not do a presentation of what is Mainframe-Cobol or a training
about it, I guess you can find this probably on Internet, and it would
take several posts.

No. The idea is: you must set up this process of analysis of Cobol code.
A meeting is planned with some people of the Mainframe world. To prepare
for this meeting:

What you need to know?
Which questions should you ask?

(snip)

There is virtually no quality standards for CICS transactions or JCL
files, and the few existing ones are not critical, so we will avoid the
effort to extract and analyze these files.

There are other object types and other types of code (Assembler, PL1, …)
in the Mainframe world, but nobody will criticize you if you do not know
what it is (furthermore, Mainframe people are nice people). All you need
to remember is that we will analyze the components based on Cobol code,
programs and Copy-books. And being able to say at your meeting that the
JCL and the ‘KiKs’ are not really interesting to evaluate the quality of
Mainframe applications.

== end quote ==

Here are some other links for this product. I don't derive any
financial benefit from this company, but their services might be
worthwhile.

http://www.sonarsource.com/products/plugins/languages/cobol/

http://nemo.sonarqube.org/coding_rules#languages=cobol



http://www.arnoldtrembley.com/
```

#### ↳ Re: Possibly humorous

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-06T06:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3319bffa4e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com>`
- **References:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com>`

```
Arnold Trembley wrote:
› This is vaguely work related but definitely COBOL related.
› 
…[5 more quoted lines elided]…
› 

This is a very rare opportunity to see COBOL through the eyes of someone who
has to deal with it, but doesn't really understand it.

The man is doing his best to tie the reality base of a modern programmer
into COBOL. It doesn't work (if you are strict about how you use
terminology) but he gets kudos for trying.

OK, it is flawed, and I agree that some of the statements are amusing, but
he's not completely wrong in much of what he says.

I cringed at the idea of COPY books being re-usable objects; but the concept
IS similar. (The major differences are that if you change a COPY book you
have to recompile every program that uses it; if you change a Class, you
just recompile it once (unless you use early binding and I never met anyone
who does...), and COPY books are SOURCE code while objects are... well,
OBJECT code...)

Some people reading this will remember source BOOKS, relocatable MODULES,
and core-image LIBRARIES on System 360. People working in that environment
knew immediately what you were talking about because if you said "module"
you were talking about relocatable OBJECT code, if you said "book" you were
talking about SOURCE code, and if you said "library" you were talking about
executable code. If you just use these terms to mean whatever you choose
them to mean (like Humpty-Dumpty in "Through the Looking Glass") then there
will probably be tears before bed time.

It's like when people say that OO COBOL is just modular programming
re-invented; it's wrong, but there ARE similarities.

When I was required to teach some of this stuff I used "ITSA" when it was
exactly the same and "ITSLIKE" when there were similarities, but also
important differences.

I'm planning to spend some of my future time addressing these very issues so
I'm not going to be hard on the guy. It really isn't easy to explain COBOL
in modern terms without a deal of experience in both environments.

Thanks for posting this, Arnold.

It was interesting.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Possibly humorous

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2015-07-07T03:22:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3319bffa4e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3319bffa4e-p2@usenetarchives.gap>`
- **References:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com> <gap-3319bffa4e-p2@usenetarchives.gap>`

```
On 7/6/2015 5:03 AM, Pete Dashwood wrote:
› Arnold Trembley wrote:
›› This is vaguely work related but definitely COBOL related.
…[9 more quoted lines elided]…
› has to deal with it, but doesn't really understand it.
 
› That's exactly why I liked it.  I'm glad you enjoyed it too.
 
› 
› The man is doing his best to tie the reality base of a modern programmer
…[11 more quoted lines elided]…
› OBJECT code...)

I don't really understand OO programming, but I know that a COBOL
copybook is not the same thing as a "reusable object". The closest
concept that I can relate to is a dynamically called subprogram. I'm
pretty sure that is not exactly the same thing. I still cannot
understand a "class hierarchy" well enough to explain it to another
procedural COBOL Programmer.

› 
› Some people reading this will remember source BOOKS, relocatable MODULES,
…[9 more quoted lines elided]…
› re-invented; it's wrong, but there ARE similarities.

I can understand modular programming in a procedural COBOL environment.
If I ever learn OO programming I would have to start with something I
understand, and try to learn how OO is different.

› 
› When I was required to teach some of this stuff I used "ITSA" when it was
…[7 more quoted lines elided]…
› Thanks for posting this, Arnold.
 
› You're welcome!
 
› 
› It was interesting.
› 
› Pete.
› 


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: Possibly humorous

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-07T20:25:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3319bffa4e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3319bffa4e-p3@usenetarchives.gap>`
- **References:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com> <gap-3319bffa4e-p2@usenetarchives.gap> <gap-3319bffa4e-p3@usenetarchives.gap>`

```
Arnold Trembley wrote:
› On 7/6/2015 5:03 AM, Pete Dashwood wrote:
›› Arnold Trembley wrote:
…[34 more quoted lines elided]…
› procedural COBOL Programmer.

A dynamically called subprogram is similar, but there are still very
important differences (mainly to do with shared usage, instances, and
encapsulation - I had an idea the other day that would demonstrate all of
this in a very practical and easy way and I'm hoping to do it when the new
site is launched.)

I'm planning to provide very easy walk-throughs and conceptual background on
the new COBOL21 side of the PRIMA web site when it opens.

There are many COBOL guys who want to understand stuff but are put off by
all the jargon, and there are some key things in OO that just aren't
apparent in standard COBOL..

Having made this transition myself, I realize the things that are
problematic, and will enjoy sharing some of this.


› 
›› 
…[14 more quoted lines elided]…
› with something I understand, and try to learn how OO is different.

That is the approach most of us take (self included...) But it isn't the
only way and there may actually be some better ways to pick up new
knowledge. It has to do with models. We like to use a model we know and
understand to assist us learning something new, but it might be possible to
construct a completely new model and use that instead. You cannot forget
what you already know (neither should you try to), but you CAN set it aside
while you look at a new model.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Possibly humorous

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-07T08:28:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3319bffa4e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3319bffa4e-p2@usenetarchives.gap>`
- **References:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com> <gap-3319bffa4e-p2@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› Arnold Trembley wrote:
 
› [snip]
 
›› http://qualilogy.com/en/sonar-cobol-what-you-need-to-know/
›› 
› 
› This is a very rare opportunity to see COBOL through the eyes of someone who 
› has to deal with it, but doesn't really understand it.

Maybe similar-like to with English dealing also really-not Her
understoodness has.

Translation: maybe if one is going to translate one needs a knowledge of
the target-language sufficient to the task. This might be one of the
author's greatest shortcomings.

› 
› The man is doing his best to tie the reality base of a modern programmer 
› into COBOL. It doesn't work (if you are strict about how you use 
› terminology) but he gets kudos for trying.
 
› [snip]
 
› Some people reading this will remember source BOOKS, relocatable MODULES, 
› and core-image LIBRARIES on System 360. People working in that environment 
…[5 more quoted lines elided]…
› will probably be tears before bed time.

Learning the environment in which the language is used might not be
necessary... but it may prevent situations like 'I asked for ground-up
muscles of cow and you speak to me of 'hamburger steak'.'

(my first impulse was 'Gosh, Mr Inuit, what kind of snow is this?')

DD
```

###### ↳ ↳ ↳ Re: Possibly humorous

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-07T20:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3319bffa4e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3319bffa4e-p5@usenetarchives.gap>`
- **References:** `<B9CdnfhD29kI3AvInZ2dnUVZ5ridnZ2d@giganews.com> <gap-3319bffa4e-p2@usenetarchives.gap> <gap-3319bffa4e-p5@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[38 more quoted lines elided]…
› (my first impulse was 'Gosh, Mr Inuit, what kind of snow is this?')

Do you know what Eskimos get from rubbing noses?

Sniffilis.

(Snow joke...)

Pete.
"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
