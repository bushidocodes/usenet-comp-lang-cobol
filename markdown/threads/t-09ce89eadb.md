[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is TSO/JCL?

_47 messages · 27 participants · 1999-05 → 1999-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### What is TSO/JCL?

- **From:** jerrygas@aol.com (JERRYGAS)
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```
         I have heard that it works in conjunction with COBOL and there is
on-line training for it. Anybody know how to find it? I couldn't find any books
on it at the bookstore.        Thanks
```

#### ↳ Re: What is TSO/JCL?

- **From:** Matthew Son <esmks@email.ais.unc.edu>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37398177.C6567562@email.ais.unc.edu>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```
TSO stands for Time Share Option.
JCL stands for Job Control Language.

As an application programmer (on a mainframe), you don't really need to
know very much about TSO.  ISPF is used with TSO and is akin to DOS for
a PC.  It would be helpful to know ISPF commands.  It is nothing you
really need to "learn."  It is pretty simple stuff and you should be
able to pick it up within a day or two of using it.  There are other
things like CLIST, REXX, DFSORT, and FILE-AID you could learn to
strengthen your MF skills.  CLIST and REXX are programming languages
which are used in a variety of different ways.  FILE-AID is a powerful
utility for manipulating files.  DFSORT is another utility.

JCL is a very unfriendly language - until you get the hang of it.  It is
used to run most anything on the mainframe.  It would be quite helpful
if you had a good command of JCL.  



JERRYGAS wrote:
> 
>          I have heard that it works in conjunction with COBOL and there is
> on-line training for it. Anybody know how to find it? I couldn't find any books
> on it at the bookstore.        Thanks
```

##### ↳ ↳ Re: What is TSO/JCL?

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990513100338.17404.00000058@ng-fe1.aol.com>`
- **References:** `<37398177.C6567562@email.ais.unc.edu>`

```
 Matthew Son <esmks@email.ais.unc.edu> writes ...

>TSO stands for Time Share Option.
>JCL stands for Job Control Language.
…[5 more quoted lines elided]…
>able to pick it up within a day or two of using it.  

This mind set really frosts me. Yes, lots of ISPF is pretty simple stuff, but
there is a lot of sophisticated stuff in there, too. All too often management
has the attitude that programmers new to OS/390 don't need ISPF training. But
when I teach classes I find most programmers woefully inadequate in their ISPF
skills.

For example, few programmers know all the features of even such basic skills as
'find' and 'change' commands much less the techniques of more than 2 split
screens, appending entries to a dslist, and so on. These simply are not the
kinds of skills you find by spending a few hours playing with ISPF: you simply
wouldn't even think to ask questions that would lead you to these techniques.

This is why I created my "Advanced ISPF" course: to do a fast and thorough run
through of all the useful features as well as some of the advanced features of
ISPF, for experienced ISPF users. Sometimes management will pay for an
'Advanced' class where they will not pay for an 'Introduction' class, even
though the 'Introduction' class is what a person may really need.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374018F6.960E09E6@hotmail.com>`
- **References:** `<37398177.C6567562@email.ais.unc.edu> <19990513100338.17404.00000058@ng-fe1.aol.com>`

```
> This mind set really frosts me. Yes, lots of ISPF is pretty simple stuff, but
> there is a lot of sophisticated stuff in there, too. All too often management
…[14 more quoted lines elided]…
> though the 'Introduction' class is what a person may really need.

Perhaps I don't understand enough of ISPF to gauge its complexity, but
I've used overlays, column shifts, and searches between labels within a
week of first using ISPF.  I read the directions and there doesn't seem
to be much to it.  Most of the team I worked with was pretty competent
as well.  I'm curious what topics would be covered in "Advanced ISPF". 
I don't understand how ISPF could be considered sophisticated in
comparison to Assembler, CICS, IDMS, IMS, DB2, COBOL, and JCL.  It took
me 3 months to get comfortable with JCL.  I used IMS for 6 months and I
still don't feel comfortable with it.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 4)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990517210448.04826.00001750@ng138.aol.com>`
- **References:** `<374018F6.960E09E6@hotmail.com>`

```
MKS <m_k_s@hotmail.com> writes ...

>
>Perhaps I don't understand enough of ISPF to gauge its complexity, but
…[3 more quoted lines elided]…
>as well.  I'm curious what topics would be covered in "Advanced ISPF". 

First, congratulations. My experience in the class room is that most
programmers who have worked with ISPF for five years or more still don't have a
clue about the kinds of techniques you mention. Either they just don't bother
to keep up with changes, they don't have (make) time to learn, or they are
somewhat lazy. There are exceptions, of course.

So first, I focus on catching experienced people up with facilities introduced
since about ISPF 3.1. If you didn't know you could "do that", even though
you've been using IPSF every workday for five years, then it's "advanced" to
you. 

That was my earlier point: there are a lot of productivity techniques that even
experienced people aren't aware of (even though they should be); many such
people would even want to use these techniques, if they new they existed; using
the rubric of "Advanced ISPF" you might get both their attention and management
funding to have a 2 day intensive class to make their folks more productive.

I've always been wary of the term "advanced" because it means such widely
different things to different people. If everybody could, or would, take the
time to read the relevant IBM documentation, and if they had the time to "play
with" the products, to test and deepen their understanding, I'd be out of work.
But what we trainers do is the synthesis, organizing the information for
learning (instead of just for reference) and provide relevant hands-on
experience through the course labs. In this way, a person can gain as much
understanding in, say, two days in a class as he or she could in maybe five to
ten days reading books and trying to make up labs on their own.

In terms, then, of topics that are not necessarily truly "advanced" (at least
in some people's eyes) but that might help programmers use ISPF more
effectively, I would include at least these:

* referral lists
* saving lists of members or data set names
* appending data set names to 3.4 lists
* named screens and related commands
* various command retrieval techniques
* basic edit macros

>I don't understand how ISPF could be considered sophisticated in
>comparison to Assembler, CICS, IDMS, IMS, DB2, COBOL, and JCL.  It took
>me 3 months to get comfortable with JCL.  I used IMS for 6 months and I
>still don't feel comfortable with it.

I agree. ISPF isn't "sophisticated" relative to those much richer products and
tools. But again I am looking at things in a relative manner. The vast majority
of applications programmers simply don't know how to use ISPF effectively,
especially the newer capabilities.

Over the last two years, my observations on the usenet groups has been that the
folks who communicate on them regularly are the brightest and the best: they
are always searching for (and sharing) deeper understanding, new techniques,
and better ways to do things. In some areas, I can help, although there always
seems to be someone who knows more than I do. In some areas, especially writing
applications programs using LE services, I have tried to maintain a leading
edge level of understanding. In areas such as ISPF skills, I can help, but it's
usually a different audience than you find subscribing to newgroups.

That's all.

Regards,



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37416850.C6786120@NOSPAMhome.com>`
- **References:** `<374018F6.960E09E6@hotmail.com> <19990517210448.04826.00001750@ng138.aol.com>`

```
> That was my earlier point: there are a lot of productivity techniques that even
> experienced people aren't aware of (even though they should be); many such
> people would even want to use these techniques, if they new they existed; using
> the rubric of "Advanced ISPF" you might get both their attention and management
> funding to have a 2 day intensive class to make their folks more productive.

It's important to have a how-to list, because people forget what they
don't use.  Let's say the class shows the very useful feature on how to
use exclude to make editing easier.   You start using it, and remember
the FLIP command, but not what it's called.  Try drilling down the help
command to find FLIP.  It's not easy.

Or edit a file with a string in columns 1-10, by moving columns 8-10 to
9-11.  (use bounds command then ")" as a line command).   Forget the
ZOOM or SHOWPROC command?  How do we find them?   And TSO doesn't come
with a single standard sysout viewer.

I hate the fact that I have to type in KEYS a dozen places, but I do
always change the first 12 Fkeys to as follows:
F1 . . .  HELP       
F2 . . .  start      
F3 . . .  EXIT       
F4 . . .  return     
F5 . . .  RFIND      
F6 . . .  RCHANGE    
F7 . . .  UP         
F8 . . .  DOWN       
F9 . . .  SWAP next  
F10  . .  LEFT       
F11  . .  RIGHT      
F12  . .  retrieve   

The F12 is essential.  I didn't know about start & swap next until
recently.  I had to give up SWAP, which I like, but having more sessions
is more valuable.

Most shops default semicolon to a delimiter, and I always do.  But how
do we turn it off for a command to use it in a search?  Do people
understand the colon?  =2;:file

Certainly they need to know pictures:   c p'<' p'>' all nx
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<REe03.1099$Ku4.39843@iad-read.news.verio.net>`
- **References:** `<374018F6.960E09E6@hotmail.com> <19990517210448.04826.00001750@ng138.aol.com>`

```
In article <19990517210448.04826.00001750@ng138.aol.com>,
S Comstock <scomstock@aol.com> wrote:

[snippolinio]

>Over the last two years, my observations on the usenet groups has been that the
>folks who communicate on them regularly are the brightest and the best

... and yet they still permit *me* here!

DD
```

##### ↳ ↳ Re: What is TSO/JCL?

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373CDF12.8A9679A0@acm.org>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <37398177.C6567562@email.ais.unc.edu>`

```


Matthew Son wrote:
> 
> TSO stands for Time Share Option.
…[5 more quoted lines elided]…
> really need to "learn."  It is pretty simple stuff and you should be
...
  Time Sharing Option used to be an  "Option" -- hasn't been for years,
but the name persists.  TSO is one of the main interactive interfaces to
MVS for programming developement (there are a number of other
interactive interfaces, but they are used more often for interactive
applications).  It used to be possible to run TSO from character-mode
terminals and maybe still is, but I have not seen it used that way in
years.  It is normally used from a 3270-capable device, which is a
capable of full-screen, fully buffered I/O, with hardware support for
subdividing the screen into fields (to restrict what part of the display
can be changed by the user for input fields), mostly used for text but
with occasional use of limited raster or vector graphics. 
  TSO by itself (not ISPF) bears some superficial resemblance to DOS,
more like a DOS window under Windows, in that it has a set of standard
"commands" you can key in and execute one at a time, but the
"environment" that you can pass from one command to the next is vast by
comparison with PC DOS, the scripting languages (CLIST and REXX), unlike
DOS BAT files, are full-fledged programming languages, and the
protections to prevent the [ordinary or non sysprog] user from
deliberately or accidentally causing damage to the underlying operating
system are absolute.  
  However, hardly anyone these days (except a sysprog in an emergency
situation) runs in stand-alone TSO anymore.  Almost everyone executes an
IBM application called ISPF/PDF under TSO, which provides a full-screen
user interface which it would be more accurate to compare with windows
than with DOS (sort of like Windows without the glitzy, and expensive,
graphics).  The user is guided via "panels" containing menus, entry
fields, pull-down menu lists, help panels and help pop-up windows
through all the various functions required for program development in
the MVS world. There are also some ISPF commands, although the one most
commonly used is a "fast-path" command to quickly jump to another dialog
panel.  
  The full-screen editor in ISPF puts MicroSoft PC text editors to shame
(in fact, there are vendors who have ported the ISPF editor user
interface to Windows platforms); and if you find some "feature" lacking,
there is an editor API you can use to extend the editor's function by
designing your own commands, which can be implemented in the language of
your choice (CLIST, REXX, Assembly, COBOL, PL/I, Fortran, C++).  ISPF is
itself extendable as well.  You can write your own panel dialogs and
ISPF "commands", and again the logic can be implemented in essentially
any language.
  Although in principle you can execute almost any program from a TSO
session, things which are expected to take a long time (like a compile
of a huge program) would normally be submitted to run as a batch job in
the background. 
    Job Control Language is used to control the sequenced execution of
programs in a non-interactive (batch job) environment in MVS, the files
or data sets which are to be used during the execution of those
programs, and the routing of any "printed" reports generated by the
batch "job".  There is some limited ability to make execution of a
program dependent on success or failure of earlier programs in the same
job, or to terminate the entire job on certain errors; but the logic
capabilities of JCL are very limited.  Based on empirical evidence,
experienced JCL coders are a rarity.  Most commonly, functional JCL is
cloned and adapted; and redundant, questionable, or unnecessary
specifications which don't cause obvious problems tend to be retained
without full understanding.  In one sense JCL is simple -- there are
only about 10 statement types, and only 3 or 4 of these are heavily
used.  Unfortunately the lists of possible operands and their
interactions run 100's of pages, and keyword, positional, and positional
keyword parameters are indiscriminantly mixed in a way designed to
confuse and confound.  
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373D2CB8.C7E8DCD4@att.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <37398177.C6567562@email.ais.unc.edu> <373CDF12.8A9679A0@acm.org>`

```
(not a response to Joel's useful post, but a general comment on this
thread)

It's probably a good idea to keep (or place) in mind that what we call
"MVS", or even "OS/390", began life as "OS/360" and "OS/360" was
designed & optimized for heavy batch work. The initial versions did not
include TSO (or any other interactive service I can recall), which hit
the marketplace circa '67-'68 (I'm sure there are folks on the NG who
can be specific on this point). It took IBM a looong time to develop an
interactive/online orientation. I first encountered ISPF in 1976, or so,
and I believe this was an early version.

IIRC, the early versions of TSO were enormous pigs and didn't catch on
quickly in the user community. It took IBM several iterations and lots
of money to get an acceptable version (kind of like Windows, now that I
think about it <g>).

Bill Lynch
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373ed976.225526066@news1.ibm.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <37398177.C6567562@email.ais.unc.edu> <373CDF12.8A9679A0@acm.org>`

```
On Fri, 14 May 1999 21:42:26 -0500, "Joel C. Ewing" <jcewing@acm.org>
wrote:

>
>
…[11 more quoted lines elided]…
>but the name persists. 

I always thought it was "Time Sharing Online" - but I could be
misinformed!
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 4)_

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373EFEF8.11429EF1@ix.netcom.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <37398177.C6567562@email.ais.unc.edu> <373CDF12.8A9679A0@acm.org> <373ed976.225526066@news1.ibm.net>`

```
OPTION is correct. Also, TSO/E is TIME SHARING OPTION / EXTENDED.

Thane Hubbell wrote:

> On Fri, 14 May 1999 21:42:26 -0500, "Joel C. Ewing" <jcewing@acm.org>
> wrote:
…[17 more quoted lines elided]…
> misinformed!
```

#### ↳ Re: What is TSO/JCL?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```
I missed the question, but TSO is a datacomm product for IBM mainframes,
kind of like "the C prompt" of MS-DOS. A lot of development software is
written for "the TSO environment." (Most common: ISPF)

JCL is Job Control Language, also for IBM mainframes. It's a lot like MS-DOS
batch files or Unix scripts, except JCL has all the user-friendliness
removed.


You can try some of the resources at http://www.mvshelp.com if you are
interested in pursuing this further.
```

##### ↳ ↳ Re: What is TSO/JCL?

- **From:** "Dennis Griffith" <dgriffit@admin.usf.edu>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hbr7u$r1k$1@news.usf.edu>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net>`

```
I do not know Unix or DOS that well....  What little I do know what not that
"user friendly"....

Michael Mattias wrote in message ...
>I missed the question, but TSO is a datacomm product for IBM mainframes,
>kind of like "the C prompt" of MS-DOS. A lot of development software is
>written for "the TSO environment." (Most common: ISPF)
>
>JCL is Job Control Language, also for IBM mainframes. It's a lot like
MS-DOS
>batch files or Unix scripts, except JCL has all the user-friendliness
>removed.
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net> <7hbr7u$r1k$1@news.usf.edu>`

```
Next to JCL, MS-DOS batch language and Unix scripts *are* user-friendly.

JCL is "user-hostile."
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 4)_

- **From:** dprichards@uswest.net (Dave Richards)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373ae367.70742592@news.uswest.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net>`

```
So take some time to learn it.  Nothing is 'user hostile' if you spend
some time with it.  Any environment where JCL is used will have a JCL
checker.  Play with it, work with it and learn from it.  C or C++ or
Java or Assembler aren't terribly 'user friendly' but people manage to
muddle through.

If you really are a programmer you should be able to learn.  Just pull
up your socks and get on with it.

If anyone could do this stuff no one would really need us, now would
they?

>Next to JCL, MS-DOS batch language and Unix scripts *are* user-friendly.
>
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NKB_2.112$Ku4.6206@iad-read.news.verio.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net>`

```
In article <373ae367.70742592@news.uswest.net>,
Dave Richards <dprichards@uswest.net> wrote:
>So take some time to learn it.

What *are* you, some kind of manager?  So allocate some time so it can be
learned!

>Nothing is 'user hostile' if you spend
>some time with it.

Patently absurd.  The amount of time one spends influences one's
familiarity with a situation, not the situation's friendliness or
hostility... or are you saying that hostility is a matter of
interpretation only?

> Any environment where JCL is used will have a JCL
>checker.

This is not my experience... then again, I've worked in shops that don't
have FileAid or ABENDAid, either, and this has been within the past three
years.

>Play with it, work with it and learn from it.

If the company wants you to learn something then the company allocates
time/money for it... one gets what one pays for, remember?

>C or C++ or
>Java or Assembler aren't terribly 'user friendly' but people manage to
>muddle through.

Oh boy, just what I want... a bunch of 'muddled through' JCL controlling
the nightly batch runs!  Dear me, Mr Richards, this is not for an 8088
with a NEC V20 speedup chip... these are the payroll runs that cut *your*
checks!

>
>If you really are a programmer you should be able to learn.  Just pull
>up your socks and get on with it.

... and if you *can* do such things then I suggest going the Independent
Route as quickly as posible... so one might earn what one is worth.

>
>If anyone could do this stuff no one would really need us, now would
>they?

Who am 'us'... and who be 'they'?

DD

>
>>Next to JCL, MS-DOS batch language and Unix scripts *are* user-friendly.
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 6)_

- **From:** dprichards@uswest.net (Dave Richards)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373b3a23.1233049@news.uswest.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net>`

```
You make all this sound like JCL is the company's way of penalizing
employees who have better things to do like writing COBOL or taking
coffee breaks.  

Wrong.  There is more to being a programmer than just writing COBOL
or, God forbid, a tough language.

>>So take some time to learn it.
>
>What *are* you, some kind of manager?  So allocate some time so it can be
>learned!

I have been a Junior Programmer, Programmer/Analyst (batch and real
time), Senior Programmer/Analyst, Systems Analyst, Senior Network
Analyst, and, yes, a manager.  I didn't start out knowing everything I
needed any more than you or anyone else did.

I started writing COBOL code in 1969, right out of college and I write
it today, with only minor time taken out for learning other, unrelated
skills.  It's like learning anything else: it takes time and patience,
mentoring is nice if there's a mentor around, but it can be learned by
anyone with the aptitude to write tight, efficient software.

And above all, it can't be learned without wanting to learn it.  I
taught myself DOS JCL (that's IBM mainframe DOS on a System/360-30)
and, when it became necessary, OS JCL on a 360-65 running MFTII.  I
also taught myself all the system utilities I needed as I needed them
and I taught myself IBM mainframe Assembler because it looked like
fun.  None of these were 'user friendly.'  In fact, the term hadn't
been invented yet.  I taught them to myself because there wasn't
anyone else with the time to teach them to me.  I worked weekends and
an occasional evening.  

Why?  Because it was my job to learn them, not because it was my
employer's job to teach them.  Because they were survival skills, like
knowing how to drive a car or balance a checkbook or talk to a
dangerous man with a gun.   Because it's my career and there are too
many good programmers with superior skills and knowledge willing to
work longer hours for less money.  Because I always knew that I wasn't
irreplacable and if I didn't take responsibility for my knowledge base
no one else would.

BTW, for the first several years I worked as a COBOL programmer there
was no such thing as a cross-reference dictionary.  We managed to do
the job despite the lack of 'friendly' tools.

>>Nothing is 'user hostile' if you spend
>>some time with it.
…[5 more quoted lines elided]…
>

No, patently true.  One perceives of something as hostile because they
don't understand it or afraid of it.  JCL isn't intuitive but it is
efficient and concise and despite what you may think, it really isn't
out to get you.

>> Any environment where JCL is used will have a JCL
>>checker.
…[3 more quoted lines elided]…
>years.

JCL should be built while the application code is being tested.  It
doesn't just materialize the night before the application goes into
production.  Plenty of time to build and test it.  No JCL checker?
Well, just submit the job and let the OS tell you where the problem
is.  Don't be afraid to test.  It won't hurt you.

Something else you may want to try.  Find the best JCL mechanic in the
shop and ask for help.  Trade your knowledge for theirs.  You probably
have skills they don't.  Don't try to work in a vacuum.

>
>>Play with it, work with it and learn from it.
>
>If the company wants you to learn something then the company allocates
>time/money for it... one gets what one pays for, remember?

It's your career.  You sound like it's the company's responsibility to
make you marketable.

Grow up.  Companies will give you the minimum resources you need to do
their job.  No company will give you more than they think you need
because (1) it costs them money and any money they spend on you is
money they can't spend on themselves, and (2) the more you know the
easier it is for you to leave, taking all that company-funded
knowledge with you.

>
>>C or C++ or
…[6 more quoted lines elided]…
>checks!

JCL isn't like C or Assembler.  There is very little logic involved.
Except for condition code testing it's all straight-line 'code'.  I'd
be a lot more worried about application software written by someone
who thinks JCL is too tough.

By the way, the V20 was NEC's equivalent to the Intel 8088.
Originally it ran at 4.77 Mhz, like the 8088, but later versions would
run at 4.77 and 8.0 Mhz, generally through the activation of a toggle
switch or some such.  I don't believe there was a 'speedup chip'
involved.  I believe it was all inherent in the chip, although I could
be wrong.  I have one in the basement if you would like it.  You pay
shipping.

>>
>>If you really are a programmer you should be able to learn.  Just pull
…[3 more quoted lines elided]…
>Route as quickly as posible... so one might earn what one is worth.

I prefer the relative stability of working for someone.  Being an
independant contractor takes too much additional time and resources to
please me.  I work to live and I give up my free time very grudgingly.
The people I know who do it well are lucratively rewarded but they
spend a great deal of uncompensated time traveling, searching out
contracts or managing themselves as a business.  I sat down once with
a former coworker who went the indie route to discuss the financial
aspects of his choice.  On a per-hour basis he didn't make much more
than I did, but I had a hell of a lot more free time and a lot less
stress.

>>
>>If anyone could do this stuff no one would really need us, now would
>>they?
>
>Who am 'us'... and who be 'they'?

'Us'  are you and me and all the other programmers out there.  (Duh)
'They' are the people who pay your salary.  Only a fool would pay
someone to do something they have the time, talent and resources to do
themself.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cW_2.253$Ku4.13706@iad-read.news.verio.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net>`

```
In article <373b3a23.1233049@news.uswest.net>,
Dave Richards <dprichards@uswest.net> wrote:
>You make all this sound like JCL is the company's way of penalizing
>employees who have better things to do like writing COBOL or taking
>coffee breaks.  

This is what you may be hearing, granted, but this is *not* how I attempt
to 'make it sound'... but let's see.

>
>Wrong.  There is more to being a programmer than just writing COBOL
>or, God forbid, a tough language.

Then there should be more to the payscale to match this... or are you
asking for freebies?

>
>>>So take some time to learn it.
…[6 more quoted lines elided]…
>Analyst, and, yes, a manager.

Bingo... I tell ya, I can smell 'em.

>I didn't start out knowing everything I
>needed any more than you or anyone else did.

I do not believe this claim was made, either... but onwards.

[snippage of history]

>I
>also taught myself all the system utilities I needed as I needed them
…[7 more quoted lines elided]…
>employer's job to teach them.

Ahhhhh... but there is a difference between your learning them and your
using them for your employer.  If your employer is not paying you for the
skill then I would say that the employer is unethical in asking you to
have the skill *unless* the employer is willing to pay for your acquiring
it.

A person who can 'do something' has a certain value.  A person who can 'do
something' *and* learn to do 'something else' has, in my opinion, a
greater value.  An employer who expects greater value in return for no
increase in compensation is, to me, as unethical as an employee who
expects a paycheck for doing No Work.

> Because they were survival skills, like
>knowing how to drive a car or balance a checkbook or talk to a
>dangerous man with a gun.

And, of course, your employer frequently asked you to do these things as a
part of your job, right?  Utter bosh... excuse me, make that 'Utter bosh,
Mr Manager, Sir'.

>Because it's my career and there are too
>many good programmers with superior skills and knowledge willing to
>work longer hours for less money.  Because I always knew that I wasn't
>irreplacable and if I didn't take responsibility for my knowledge base
>no one else would.

Once again, there's a difference between learning something and then using
that learning for someone who does not pay.  Here's an example:

A secretary has a job which pays $x.  He falls in love with a woman of
Hispanic descent and *in his spare time* learns Spanish so that they might
speak to each other.

One day, while on his lunch-break, his manager walks past while he is
speaking to his wife on the pay-phone; later that week, invoking the
'other duties as assigned' part of the job-description the manager
joyously announces that this fellow will now function as a bilingual
secretary... for the same salary.

Calll this A and compare it to B: the manager walks past in the lunch-room
and sees the fellow, nose buried in his 'Learn Spanish in 21 Days' book.
The manager then offers a tuition rebate if the secretary passes the
course with a grade above a certain average and offers a job-change to
Official Multilingual Secretary (with a $y% increase in salary) upon
completion.

I see you as looking at A and saying 'This Is A Good Thing'... and I say
that it is not, that B is a Good Thing.. *especially* since the skill we
speak of here, JCL, has *no* application outside of a mainframe computer
environment which is being used to Make A Company More Money.

>
>BTW, for the first several years I worked as a COBOL programmer there
>was no such thing as a cross-reference dictionary.  We managed to do
>the job despite the lack of 'friendly' tools.

Oh, for the Oldene Dayse, when a Coder could Code Code such as *ten*
Coders cannot Code today!

>
>>>Nothing is 'user hostile' if you spend
…[9 more quoted lines elided]…
>don't understand it or afraid of it.

Quite right, of course... once one understands or is no longer afraid then
there's *nothing* hostile about that methane atmosphere of Jupiter,
right?... or are you saying that this atmosphere is not a 'something'?

You may have been a coder, Mr Richards, but you seem to have replaced the
rigorous logic of a Programmer with the banalities of ManagementSpeak.

>JCL isn't intuitive but it is
>efficient and concise and despite what you may think, it really isn't
>out to get you.

To be 'hostile' is not the same as being 'antagonistic', I believe.

>
>>> Any environment where JCL is used will have a JCL
…[8 more quoted lines elided]…
>production.  Plenty of time to build and test it.  No JCL checker?

That's right.. no JCL checker, contrary to your assertion above.

>Well, just submit the job and let the OS tell you where the problem
>is.  Don't be afraid to test.  It won't hurt you.

That's right.. don't be afraid of a typo of, say, a 'B' for an 'N' so that
your job is not updating all the files for Duluth instead of Des Moines...
after all, the Manager won't be called in to fix it!

>
>Something else you may want to try.  Find the best JCL mechanic in the
>shop and ask for help.  Trade your knowledge for theirs.  You probably
>have skills they don't.  Don't try to work in a vacuum.

You mean the guy with the big, long line outside of his cubicle who also
has a full-time Job to do?  What happens when one finally gets to the head
of the line and a Manager comes storming in, bellowing about a job that's
updating Duluth instead of Des Moines?

>
>>
…[6 more quoted lines elided]…
>make you marketable.

No, I make it sound like it is the company's responsibility to pay for
what it demands be done... a radical concept, granted.

>
>Grow up.

I thought that expecting mutuality between Employer and Employee *was*
being 'grown up'... guess I was wrong.

>Companies will give you the minimum resources you need to do
>their job.

.. and they will get *exactly* what they pay for, no more and no less...
what is wrong with that?  If they want more, let them pay more.

>No company will give you more than they think you need
>because (1) it costs them money and any money they spend on you is
>money they can't spend on themselves, and (2) the more you know the
>easier it is for you to leave, taking all that company-funded
>knowledge with you.

That is why a pay increase is associated with the successful completion of
a course... or is that too complex a solution?

>
>>
…[9 more quoted lines elided]…
>JCL isn't like C or Assembler.  There is very little logic involved.

EXEC PGM=IEBGENER,COND=((0,NE,QLBK0010),EVEN)... oh, excuse me, I was in
the other window... so, tell me, why is it that you mention the
user-friendliness of Java or Assembler and then state that JCL isn't like
C or Assembler... what is the relevance here, please?

>Except for condition code testing it's all straight-line 'code'. I'd 
>be a lot more worried about application software written by someone
>who thinks JCL is too tough.

Given that you have expressed concerns about someone who cna learn and
apply new skills jumping ship for a better-paying job (instead, of course,
of paying more) this is understandable... me, I've met folks who can make
CICS jump up and *sing* and yet cannot code a GENER to save their lives.

>
>By the way, the V20 was NEC's equivalent to the Intel 8088.
…[5 more quoted lines elided]…
>shipping.

I have my own, thanks; it is attached to a Kaypro 8088 and is invoked only
when the switch is pressed.  Un-pressed the speed is slower, pressed and
it is sped-up.  Thanks for your information, it is greatly appreciated.

>
>>>
…[6 more quoted lines elided]…
>I prefer the relative stability of working for someone.

'Employment at Will' is, I believe, the law here in the United States of
America... there was a recent posting here from a coder who unexpectedly
found himself on the street after 14 years or so on the job.  Ask the
programming crew at Drexel, Burham, Lambert about 'stability'.

>Being an
>independant contractor takes too much additional time and resources to
>please me.  I work to live and I give up my free time very grudgingly.

... and yet you advise others to do just that and learn on their own
hours; why do I read that as rank hypocrisy?

>The people I know who do it well are lucratively rewarded but they
>spend a great deal of uncompensated time traveling, searching out
>contracts or managing themselves as a business.

This speaks volumes of the folks you know, not of how the business can be
practised.

>I sat down once with
>a former coworker who went the indie route to discuss the financial
…[10 more quoted lines elided]…
>'Us'  are you and me and all the other programmers out there.  (Duh)

Let's make a deal here... I won't speak for you, you don't speak for me.

>'They' are the people who pay your salary.

I receive no salary, I receive an hourly rate from my clients for the
services I render them.

>Only a fool would pay
>someone to do something they have the time, talent and resources to do
>themself.

That depends, Mr Richards, on the relative values said 'fool' places on
money, time, talent and resources... it is usually best speak for
yourself, Mr Richards, unless you've been elected to be a mouthpiece for
others.


(alright... what are the odds that I get accused of a 'bad attitude'
next?)

DD
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 8)_

- **From:** JDR <beta1@bigfoot.com>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373C4336.1F33218E@bigfoot.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net> <7cW_2.253$Ku4.13706@iad-read.news.verio.net>`

```


docdwarf@clark.net wrote:

> In article <373b3a23.1233049@news.uswest.net>,
> Dave Richards <dprichards@uswest.net> wrote:
…[141 more quoted lines elided]…
> That's right.. no JCL checker, contrary to your assertion above.

Every heard of the "TYPERUN=SCAN" option on the JOB card?  That is a built-in
JCL checker.

>
>
…[153 more quoted lines elided]…
> DD

The reality of employment is -- in almost ALL, if not all, states in the U.S.,
the EMPLOYER-EMPLOYEE relationship is defined BY LAW to be that of
MASTER-SERVANT.  Ergo .... employers have a pretty free hand in what they
demand you do to earn your generally paltry salary.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 9)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fOX_2.265$Ku4.14309@iad-read.news.verio.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373b3a23.1233049@news.uswest.net> <7cW_2.253$Ku4.13706@iad-read.news.verio.net> <373C4336.1F33218E@bigfoot.com>`

```
In article <373C4336.1F33218E@bigfoot.com>, JDR  <beta1@bigfoot.com> wrote:

[snippage]

>Every heard of the "TYPERUN=SCAN" option on the JOB card?  That is a built-in
>JCL checker.

Only insofar as it verifies syntax; it will not tell me that the SYSIN
card, 28 steps into the job, does not exist or that I mis-spelled and
typed PGM=AKZQM521 instead of PGM=AZKQM521 (anyone for an 806?)

[more snippage]

>The reality of employment is -- in almost ALL, if not all, states in the U.S.,
>the EMPLOYER-EMPLOYEE relationship is defined BY LAW to be that of
>MASTER-SERVANT.  Ergo .... employers have a pretty free hand in what they
>demand you do to earn your generally paltry salary.

I do not make any claims on 'reality'... but I do know that I have
concluded that it is just as unethical for me to demand money for work I
have not done as it is for a client to demand from me skills for which
they do not pay.

DD
```

###### ↳ ↳ ↳ Re: Employer-Employee discussion (Was: What is TSO/JCL?)

_(reply depth: 9)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hhhra$9cr$1@news.ses.cio.eds.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net> <7cW_2.253$Ku4.13706@iad-read.news.verio.net> <373C4336.1F33218E@bigfoot.com>`

```
> The reality of employment is -- in almost ALL, if not all, states in
the U.S.,
> the EMPLOYER-EMPLOYEE relationship is defined BY LAW to be that of
> MASTER-SERVANT.  Ergo .... employers have a pretty free hand in what
they
> demand you do to earn your generally paltry salary.
>

And in much of the world there are absolute dictators who do whatever
they want, order executions, participate openly in activities that
would be viewed as criminal here in the US, support other nations who
act in a similar manner.

This does not make these things moral or ethical.  They still exist,
though, regardless of general (or at least my) opinion of them.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 9)_

- **From:** Matthew Son <esmks@email.ais.unc.edu>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373C5548.73D7A1EC@email.ais.unc.edu>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net> <7cW_2.253$Ku4.13706@iad-read.news.verio.net> <373C4336.1F33218E@bigfoot.com>`

```
I bet poor JERRYGAS is sorry he ever posted his simple question...
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 10)_

- **From:** jerrygas@aol.com (JERRYGAS)
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990515140044.25558.00000700@ng64.aol.com>`
- **References:** `<373C5548.73D7A1EC@email.ais.unc.edu>`

```
That's just what I was thinking five seconds before I read your post.   --
JERRYGAS
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373D66A0.7B5AF5FF@zip.com.au>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net> <7cW_2.253$Ku4.13706@iad-read.news.verio.net>`

```
Regarding learning something for free.  I have always worked on
this premise, since I reasonably regularly vote with my feet I
find that yes it does always pay to know these things.  I would
not be paid half as much as I am if I waited for someone to spoon
feed me.

The argument is valid in that request some support from
managment.  Two reasons:  

One: It pays to advertise.  When reviews come up enthusiastic
people get more money (mostly appart from scrooge companies).

Two: If they are not very supportative and it is something that
you want to do, it is time to get out "Tuesday's Australian"
(Subsistute the paper with all the Computer job adverts in it).

Put the hard yards in and the money will follow.


Regarding the TYPRUN=SCAN.  This is the difference between keyword
highlighting in the editor and not having it.  Yes you can compile
and get a result but it is better to have instant feedback.  When
you wait for 3 hours for the job to start to see it cumple due to
a miss typed DSN then you really could cry.  A JCL checker is a
must have it saves a lot of waiting and frustration, you do not
have to figure out how to actually restart the job in the middle
and when you do it quickly notes the GDG's that you have to change
from +1 to 0.

Ken
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 7)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hhb0i$mut$1@news.cerf.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net>`

```
Dave Richards wrote in message <373b3a23.1233049@news.uswest.net>...
>Wrong.  There is more to being a programmer than just writing COBOL
>or, God forbid, a tough language.

It is too much to quote here, so, rather than missing something, I would
like to say that I share your view.

Cheesle
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 7)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373b9631.16288283@netnews>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net> <NKB_2.112$Ku4.6206@iad-read.news.verio.net> <373b3a23.1233049@news.uswest.net>`

```
'Twas Thu, 13 May 1999 21:50:46 GMT, when dprichards@uswest.net (Dave
Richards) illuminated comp.lang.cobol thusly:

> You make all this sound like JCL is the company's way of penalizing
> employees who have better things to do like writing COBOL or taking
> coffee breaks.  

That's a very good description of JCL.

> None of these were 'user friendly.'  In fact, the term hadn't
> been invented yet.

And if only IBM made computers it never would have.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hf01t$msg$1@news.ses.cio.eds.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net>`

```
Dave Richards <dprichards@uswest.net> wrote in message
news:373ae367.70742592@news.uswest.net...
> <snip>  Any environment where JCL is used will have a JCL
> checker.  <snip>

Until two years ago, our shop's JCL checker was TYPRUN=SCAN, and it
had been that way since about 1970.  Our shop wasn't too small to get
one, either.

<snip>
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** ENOJON <enojon@delphi.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3744248A.17DA6E24@delphi.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <hQ3_2.1716$Yy4.43533@dfiatx1-snr1.gtei.net> <7hbr7u$r1k$1@news.usf.edu> <T5q_2.1550$m83.41078@dfiatx1-snr1.gtei.net> <373ae367.70742592@news.uswest.net>`

```
With all due respect, JCL has three basic commands that should get
any programmer up and running, but the varied permutations on the
basics could send a 747 pilot screaming in horror.

For example, let's get down and dirty with one simple COBOL "Display"
verb.

It is simple //SYSOUT DD SYSOUT=*   [and, already we have
at least 40 variations on SYSOUT class].   disposition, if you're
not going to settle for installation default?  copies?  destination?
free'd on close of dataset? checkpointing? output limit?   forms
control? printer character set (font)? and, then, maybe there's a
JES2 or JES3 entry system to handle with another 60 variants.

But maybe you want to do a hardcopy, microfiche and CDROM
imaging, send a copy across the LAN to user workstation and
to the remote printer in Fargo, ND?

ej



Dave Richards wrote:

> So take some time to learn it.  Nothing is 'user hostile' if you spend
> some time with it.  Any environment where JCL is used will have a JCL
…[53 more quoted lines elided]…
> >
```

#### ↳ Re: What is TSO/JCL?

- **From:** fletcher.adams@eudoramail.com (Fletcher Adams)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373b507b.1899230@news-server>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```
On 11 May 1999 20:48:04 GMT, jerrygas@aol.com (JERRYGAS) wrote:

>         I have heard that it works in conjunction with COBOL and there is
>on-line training for it. Anybody know how to find it? I couldn't find any books
>on it at the bookstore.        Thanks


Well, there's no such thing as TSO/JCL as such.  TSO is an environment
that runs on MVS, or OS/390 as it is now called, on IBM and Amdahl
mainframes.

JCL is Job Control Language , which uses TSO commands to do things
like allocate resources, execute programs (or "load modules," as we
say), and deal with the output.

That, of course, is a dramatically oversimplified version of what TSO
is.  A better (but not perfect) discussion of TSO can be found in a
pair of books published by Mike Murach and Associates.  The last
number I had for them was 800/221-5528 - but please bear in mind that
number is a decade old (though they're still going strong), and for
all I know they may have a web site.

If you have any specific questions, I'll be glad to answer them to the
best of my ability.

Luck -
F
```

#### ↳ Re: What is TSO/JCL?

- **From:** Laura Sabourin <laura@ragdolls.net>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373B8DB8.47597AF9@ragdolls.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```


JERRYGAS wrote:

>          I have heard that it works in conjunction with COBOL and there is
> on-line training for it. Anybody know how to find it? I couldn't find any books
> on it at the bookstore.        Thanks
> go to the Museum :-)

TSO - time sharing option used on dump terminals (3270 emulation?)
running on IBM mainframes
JCL = job control language also IBM 360 -----> stuff
```

#### ↳ Re: What is TSO/JCL?

- **From:** rkowalc@my-dejanews.com
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7if7gh$j1r$1@nnrp1.deja.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com>`

```
As a new Cobol programmer, I have found the follow books to be
invaluable:

System 390 JCL by Gary Deward Brown    and
MVS TSO, Part 1 by Doug Lowe.

Both are available at Amazon and Buy.com.  Buy.com was a couple of bucks
cheaper.


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

##### ↳ ↳ Re: What is TSO/JCL?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ikuo5$dh8@enews3.newsguy.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com>`

```
I have the same JCL book and it is an invaluable resource.

JCL is what runs the COBOL programs.  It is strange at first but after
seeing enough of it, it will become very easy to you.  Kind of like driving
a stick shift car.  JCL is a very, very powerful language.   I have cut the
run times of small MVS jobs down by 90% just by tweaking the JCL.

TSO stands for Time Sharing Option.  It allows users to take a small portion
of the mainframe's resources for development, testing, and maintenance of
jobs.  It kind of sits between MVS and whatever editor or workbench you use
(ISPF, Roscoe, etc.)

Later,
Jeff

----------
In article <7if7gh$j1r$1@nnrp1.deja.com>, rkowalc@my-dejanews.com wrote:


> As a new Cobol programmer, I have found the follow books to be
> invaluable:
…[9 more quoted lines elided]…
> ---Share what you know. Learn what you don't.---
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374f2f1d.638173@netnews>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com>`

```
'Twas Thu, 27 May 1999 22:24:37 -0400, when "Jeff Baynard"
<union27@macconnect.com> illuminated comp.lang.cobol thusly:

> I have cut the
> run times of small MVS jobs down by 90% just by tweaking the JCL.

Or put the other way around, you can make a small MVS job take ten times
as long by writing poor JCL.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3753F00C.E519E13E@NOSPAMhome.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews>`

```
> > I have cut the
> > run times of small MVS jobs down by 90% just by tweaking the JCL.
> 
> Or put the other way around, you can make a small MVS job take ten times
> as long by writing poor JCL.

I thought I knew JCL, but I am not picturing what can be done in JCL to
change performance this way.  Could you provide examples?
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j1e0t$dhd@dfw-ixnews8.ix.netcom.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com>`

```
Howard Brazee wrote in message <3753F00C.E519E13E@NOSPAMhome.com>...
>> > I have cut the
>> > run times of small MVS jobs down by 90% just by tweaking the JCL.
…[5 more quoted lines elided]…
>change performance this way.  Could you provide examples?

Certainly, a "classic case" is providing too small a set of sort-work
datasets.  Another is where you use multiple step utilities to "copy" then
"sort" then "gener" then "copy" again the same file.  I think most of these
have to do with "mis-using" the IBM (and 3rd party) utilities and their
datasets, but they are closely tied into "bad" JCL.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 6)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37547D0C.3A5D@saif.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com>`

```
Another JCL tuning consideration is dataset blocksizes.
   DCB=(RECFM=FB,LRECL=80,BLKSIZE=80)
performs MUCH slower than...
   DCB=(RECFM=FB,LRECL=80,BLKSIZE=26960)

There are also BUFNO= parameters that can improve performance by
allocating more dataset buffers than your system defaults to.

I have gotten in trouble for using BUFNO too much however, because the
batch performance gain I experienced was at the expense of the online
systems.  :-)   I'm not sure that BUFNO makes much difference anymore
with System Managed Storage(SMS) in effect.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 7)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j283b$mff@enews2.newsguy.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com>`

```
Yes, blocksize makes a big difference in performance.  Our shop (tries to)
uses BLKSIZE=0 in the DCB and a space parameter like
SPACE=(0,(2000,200),RLSE) or similar.  I had a job that was allocating
SPACE=(CYL,(200,60),RLSE) and the dataset was going across several volumes
and was very slow.  By changing to block allocation and letting MVS allocate
the blocksize, the job ran in 1/10th the time, no joke.  One line of code.

BTW, we use SyncSort and it grabs as much extended secondary memory that it
needs and automatically extends region up by 4096k so, at least with this
sort package, there is little benefit from coding more SORTWORK and region.

I've also found large datasets to work better from tape than from DASD, at
least sequential datasets.  One reporting job we have has 1.5 million 500
byte records and it was very slow sorting on DASD, but going to UNIT=TAPE,
SPACE =(0,0), and 0 blocksize, the sort times dropped in half.

So I guess it's not so much more efficient coding, it's more just using your
resources better.

Jeff, the Newby

----------
In article <37547D0C.3A5D@saif.com>, Pete Wirfs <petwir@saif.com> wrote:


> Another JCL tuning consideration is dataset blocksizes.
>    DCB=(RECFM=FB,LRECL=80,BLKSIZE=80)
…[9 more quoted lines elided]…
> with System Managed Storage(SMS) in effect.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 8)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com> <7j283b$mff@enews2.newsguy.com>`

```
You must be nuts! Sorry but I have always found disk quicker than tape.

In article <7j283b$mff@enews2.newsguy.com>, Jeff Baynard
<union27@macconnect.com> writes
>I've also found large datasets to work better from tape than from DASD, at
>least sequential datasets.  One reporting job we have has 1.5 million 500
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 9)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eE3daXur#GA.348@nih2naad.prod2.compuserve.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com> <7j283b$mff@enews2.newsguy.com> <3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk>`

```
    Reguards the sort job that ran faster on tape than disk:

    You did not say WHEN that job ran.  1.5 million 500 byte records take up
750Meg roughly.  Sorting could take twice that much work space.  Could the
system you were running on have been short on disk space?  If it was, than
using tape might easily be faster, assuming that the sort program avoids
using tape for work space.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 10)_

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37595B15.7DB7A479@acm.org>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com> <7j283b$mff@enews2.newsguy.com> <3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk> <eE3daXur#GA.348@nih2naad.prod2.compuserve.com>`

```
Russell Styles wrote:
>     Reguards the sort job that ran faster on tape than disk:
>     You did not say WHEN that job ran.  1.5 million 500 byte records take up
…[3 more quoted lines elided]…
> using tape for work space.

  Insufficient DASD for SORTWRK would most likely cause sort failure not
degraded performance.  I'm sure the earlier post was referring to just
having the input/output files on tape vs. DASD.  For an unloaded 3490
tape controller, tape is inherently faster than native 3390 on large
sequential unstriped datasets because not only is the tape native data
transfer rate high but there is no delay for seek or rotational latency
(in fact, response is best when you keep the drive busy enough so that
physical tape movement is never interrupted).  I'm not sure about the
physical disk transfer rates in IBM RAMAC or IBM RVA, but at least in
our experience it is difficult to avoid at least some contention which
restricts the effective sustained transfer rate for sequential access,
and even on native 3390 the max sustained physical data transfer is
limited to 1 cylinder of data before one is forced to incur seek and
latency delays.  Note we are talking about large enough files that
physical disk I/O would be required, not just transfers from DASD cache.
  Now the catch is that tape controllers in a busy shop are rarely
"unloaded".  Four concurrent dump processes to 4 drives on a 16-drive,
two-path 3490E string can pretty well tie up both the controller and
channel paths.  The Load on both tape and DASD subsystems can
significantly alter response times of both these subsystems, so for
systems under normal system workload, sequential access may sometimes be
faster from tape and at other times faster from DASD.  
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375BC847.8F77CEC1@NOSPAMhome.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com> <7j283b$mff@enews2.newsguy.com> <3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk> <eE3daXur#GA.348@nih2naad.prod2.compuserve.com>`

```
Russell Styles wrote:
> 
>     Reguards the sort job that ran faster on tape than disk:
…[5 more quoted lines elided]…
> using tape for work space.


Have you ever had an environment in which you sorted pieces of a file to
a bunch of tapes, then merged the tapes to get a file which was too big
to sort otherwise?  I have.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 9)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j9nj4$1soh@enews1.newsguy.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com> <7j283b$mff@enews2.newsguy.com> <3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk>`

```
On DASD, the dataset was going across multiple volumes.  On tape, it's all
in one big stream.

Jeff

----------
In article <3GEpHCAo$wV3Ewqa@ld50macca.demon.co.uk>, Alistair Maclean
<LD50Macca@ld50macca.demon.co.uk> wrote:


> You must be nuts! Sorry but I have always found disk quicker than tape.
>
…[14 more quoted lines elided]…
> Alistair Maclean
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3755305C.56C93D12@NOSPAMhome.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com> <37547D0C.3A5D@saif.com>`

```
Pete Wirfs wrote:
> 
> Another JCL tuning consideration is dataset blocksizes.
…[10 more quoted lines elided]…
> with System Managed Storage(SMS) in effect.

I have only used BUFNO a couple of times.   A parameter which I plan on
using on my next sort is OPTION DYNALLOC.  Right now, I am doing a lot
of on-line work though.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37552F84.F7DDE20E@NOSPAMhome.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <7j1e0t$dhd@dfw-ixnews8.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Howard Brazee wrote in message <3753F00C.E519E13E@NOSPAMhome.com>...
…[13 more quoted lines elided]…
> datasets, but they are closely tied into "bad" JCL.

I remember having charts assisting me in finding optimal sort work
sizes.  I haven't seen one used in some time - it's easier to allocate
way more space than is needed.  I don't think I've seen the multiple
copy - except when the same parm file is to be read by multiple programs
in a proc.  Then the first step copies the parm file to a temporary data
set which is read by the different programs.  Anyway, these go real fast
compared to the programs themselves.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 5)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3754A5ED.73EE9DFC@att.net>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> > > I have cut the
…[6 more quoted lines elided]…
> change performance this way.  Could you provide examples?

Providing sufficient buffers for VSAM & QSAM datasets can make this kind
of difference, e.g., 8 hrs to 30 mins.

Bill Lynch
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375530AB.C3D9D16B@NOSPAMhome.com>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <3754A5ED.73EE9DFC@att.net>`

```
William Lynch wrote:
> 
> Howard Brazee wrote:
…[13 more quoted lines elided]…
> Bill Lynch

I've been working in IDMS shops too many years.  Don't use these very
often.
```

###### ↳ ↳ ↳ Re: What is TSO/JCL?

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37558CCA.33850433@zip.com.au>`
- **References:** `<19990511164804.22393.00000709@ng-cc1.aol.com> <7if7gh$j1r$1@nnrp1.deja.com> <7ikuo5$dh8@enews3.newsguy.com> <374f2f1d.638173@netnews> <3753F00C.E519E13E@NOSPAMhome.com> <3754A5ED.73EE9DFC@att.net>`

```
William Lynch wrote:
> 
> 
…[3 more quoted lines elided]…
> Bill Lynch

Look up batch LSR pools.  Does amazing things to random read write
VSAM clusters.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
