[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reverse Engineering a COBOL program

_10 messages · 7 participants · 2006-05_

---

### Reverse Engineering a COBOL program

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-05-03T11:54:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com>`

```
Hello:
As one of the last assignments of my career as a COBOL programmer, I am
supposed to reverse engineer some old COBOL programs.  Some of these
programs have some go to statements and are somewhat difficult to
understand.  Do you have any suggestions on how to understand COBOL
programs?  What I usually do is run the programs with display
statements of the paragraph names and variable comments.  I even dusted
off my old plastic green IBM flowchart template.  Any suggestions about
approaching this is appreciated.  I was thinking of using the next or
continue feature of modern loops to emulate the go tos...But I'm
getting somewhat frustrated and am tempted to put go tos in the design
spec...

Best Wishes,
Chris.
```

#### ↳ Re: Reverse Engineering a COBOL program

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2006-05-03T15:46:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RM76g.3099$ix6.241658@news20.bellglobal.com>`
- **In-Reply-To:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com>`

```
hcmason@sbcglobal.net wrote:
> Hello:
> As one of the last assignments of my career as a COBOL programmer, I am
…[13 more quoted lines elided]…
> 

I've converted a couple, and I've found the best approach is to convert
the data first.  That way, reports can be run (old and new) and
compared. Usually, with older systems, there is enough old data that
even years ends can be tested.  It makes life *much* easier if the old
and the new can be run side-by-side.

Donald
```

##### ↳ ↳ Re: Reverse Engineering a COBOL program

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-05-05T09:31:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146846688.566092.20350@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<RM76g.3099$ix6.241658@news20.bellglobal.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <RM76g.3099$ix6.241658@news20.bellglobal.com>`

```
Dear Donald:
Thanks for the suggestion.  I will try to get the BRIO developer to see
if we can compare the two systems.  The system I have had 6 COBOL
programs and 3 external sorts.  He might want to take a different
approach.  I was trying to represent the old code in something
structured that could be easier to implement using Oracle stored
procedures and/or Perl, which is what they have told me they can use
behind BRIO.  Apparently BRIO also uses javascript, but the heavy
processing uses the other tools mentioned.
```

#### ↳ Re: Reverse Engineering a COBOL program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-05-03T22:47:08+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<602i52hidt6hdjri8f1tnoicdn3t6oilmg@4ax.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com>`

```
On 3 May 2006 11:54:53 -0700 hcmason@sbcglobal.net wrote:

:>As one of the last assignments of my career as a COBOL programmer, I am
:>supposed to reverse engineer some old COBOL programs.  Some of these
:>programs have some go to statements and are somewhat difficult to
:>understand. 

How old are you?

How many years were in your "career as a COBOL programmer"?

Also, reverse engineer from source code????

Reverse engineering is from object code. 

What language are you supposed to rewrite them in?

:>             Do you have any suggestions on how to understand COBOL
:>programs?  What I usually do is run the programs with display
:>statements of the paragraph names and variable comments.  I even dusted
:>off my old plastic green IBM flowchart template.  Any suggestions about
:>approaching this is appreciated.  I was thinking of using the next or
:>continue feature of modern loops to emulate the go tos...But I'm
:>getting somewhat frustrated and am tempted to put go tos in the design
:>spec...

Read the code. Talk to the users to figure out the business logic.

Also, why violate the "if it ain't broke, don't fix it" rule?
```

##### ↳ ↳ Re: Reverse Engineering a COBOL program

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-05-05T09:44:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146847452.851210.176070@e56g2000cwe.googlegroups.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <602i52hidt6hdjri8f1tnoicdn3t6oilmg@4ax.com>`

```
I've been a cobol programmer for 20 years.  I turned 48 recently.  I
think I am having problems with these six programs as I am working on 3
unrelated tasks...But for a smart guy like you it would probably be
trivial.  I'll let the team know that the official definition of
reverse engineering is from Assembler.  The target system has brio as a
frontend.  I haven't gotten any training on it, but I've been told they
resort to oracle stored procedures (pl/sql, java?) and perl.
Thanks for the suggestion about reading the code.  I was resisting
that...The users are so busy get SAP R/3 to work now that it replaced
these programs that they are hard to interview..But I'll try to get
their attention...Maybe after all this trouble they will never really
look at the data in the data legacy archive...
Have a nice day in Isreal...
Chris.
```

###### ↳ ↳ ↳ Re: Reverse Engineering a COBOL program

- **From:** "gwlemyre@earthlink.net" <gwlemyre@earthlink.net>
- **Date:** 2006-05-07T17:48:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147049305.125856.46540@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<1146847452.851210.176070@e56g2000cwe.googlegroups.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <602i52hidt6hdjri8f1tnoicdn3t6oilmg@4ax.com> <1146847452.851210.176070@e56g2000cwe.googlegroups.com>`

```
Get in touch with Niels Veerman at http://www.cs.vu.nl/~nveerman/

Review one of his articles, Revitalizing Modifiability of Legacy
Assets, at
http://portal.acm.org/citation.cfm?id=1044313&dl=ACM&coll=ACM
or http://portal.acm.org/citation.cfm?id=873598&dl=GUIDE&coll=GUIDE
```

###### ↳ ↳ ↳ Cobol Research (was: Reverse Engineering a COBOL program)

_(reply depth: 4)_

- **From:** Niels <nveerman@cs.vu.nl>
- **Date:** 2006-05-15T15:51:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4a11p$n4p$1@star.cs.vu.nl>`
- **In-Reply-To:** `<1147049305.125856.46540@u72g2000cwu.googlegroups.com>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <602i52hidt6hdjri8f1tnoicdn3t6oilmg@4ax.com> <1146847452.851210.176070@e56g2000cwe.googlegroups.com> <1147049305.125856.46540@u72g2000cwu.googlegroups.com>`

```

gwlemyre@earthlink.net wrote:
> Get in touch with Niels Veerman at http://www.cs.vu.nl/~nveerman/
> 
…[4 more quoted lines elided]…
> 


Thanks for the advertisement Grant.
I would like to take this opportunity to draw this community's attention 
to our work.
Our research group at the Vrije Universiteit Amsterdam, which is a 
member of the Cobol Committee (ISO/IEC JTC1/SC22/WG4), is doing active 
research on Cobol. Our Cobol portal can be found here: 
http://www.cs.vu.nl/Cobol/
The research includes grammar engineering and automatic code 
transformations (analyses and reliable code modifications).
By adressing industrial applications, we work on techniques to preserve 
and support the evolution of existing legacy assets.

Some of our contributions are:
- A browsable VS Cobol II grammar:
http://www.cs.vu.nl/grammarware/browsable/vs-cobol-ii/

- A set of code restructuring transformations that extends and enriches 
the life of Cobol applications, and prepares them for future evolution 
(e.g. reuse, migration, integration, web-enabling):
http://www.cs.vu.nl/~nveerman/research/revitalizing/revitalizing.pdf


Our effort would not be possible without the active participation of the 
Cobol developers community, for instance, the people that read and post 
in this newsgroup.

To give an example, Grant, who posted the above message, was working on 
an evolved legacy application, which was initiated in the early 80s. 
Some parts of the system had to be reused, but the application's logic 
was severely intertwined, which made it difficult to identify and 
separate functionality.
We supported his work by restructuring the application into loosely 
coupled blocks of code, and he provided valuable feedback, which we used 
to improve our approach. A description of the case can be found here: 
(see figures 18/19 for visualisations of the particular application)
http://www.cs.vu.nl/~nveerman/research/minefield/minefield.pdf


We hope that we can all continue to benefit from the efforts that are 
done on both 'sides'. We see researchers that investigate more modern 
languages, like Java/C#, but applications written in these languages 
also suffer from the increasing complexity of evolving software, so 
these languages are no replacement for Cobol just for the reason that 
they would be 'easier to maintain'. The following presentation, held by 
a former member of the Cobol Committee, discusses Cobol as a research 
theme:
http://www.cs.vu.nl/Cobol/stop-bashing-cobol.pdf


The key is to keep Cobol applications in proper shape and up-to-date 
with new standards and insights, in a way that they can interoperate 
with other systems and allow to be adapted to the ever changing world in 
which they participate.
This way, Cobol assets are far from withdrawal and continue to provide 
crucial value to enterprises.


For comments, ideas and questions, do not hesitate to contact me by email.

With best regards,

Niels
nveerman@cs.vu.nl
```

#### ↳ Re: Reverse Engineering a COBOL program

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-05-03T22:13:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iW96g.5089$Fg4.1092@clgrps12>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com>`

```
<hcmason@sbcglobal.net> wrote in message 
news:1146682493.093027.308520@j73g2000cwa.googlegroups.com...
> Hello:
> As one of the last assignments of my career as a COBOL programmer, I am
…[9 more quoted lines elided]…
> spec...

    There's a guide on cleaning up COBOL code at 
http://home.swbell.net/mck9/cobol/style/rewrite.html

    - Oliver
```

##### ↳ ↳ Re: Reverse Engineering a COBOL program

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-05-05T03:32:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Hz6g.44819$eR6.15479@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<iW96g.5089$Fg4.1092@clgrps12>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <iW96g.5089$Fg4.1092@clgrps12>`

```


Oliver Wong wrote:

> (snip) 
> 
…[3 more quoted lines elided]…
>    - Oliver

Lots of good stuff there.  Thanks for sharing!
```

##### ↳ ↳ Re: Reverse Engineering a COBOL program

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-05-05T09:35:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146846933.423653.223360@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<iW96g.5089$Fg4.1092@clgrps12>`
- **References:** `<1146682493.093027.308520@j73g2000cwa.googlegroups.com> <iW96g.5089$Fg4.1092@clgrps12>`

```
Dear Oliver:
Thanks for your help.  We had some COBOL programmers leave Lockheed
years ago to work at Pacific Bell...
Maybe you might see their names in the change log of your programs...
Best wishes,
Chris.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
