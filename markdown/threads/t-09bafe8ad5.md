[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus animator and CALL statements

_18 messages · 5 participants · 2010-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus animator and CALL statements

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-01T12:34:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com>`

```
Any idea how I can step INTO a CALL's code block using Microfocus
Server Express 4.0 SP2 on HP-UX B11.11?
Right now when I step on the CALL statement the animator executes the
CALL by stepping over and not into.
```

#### ↳ Re: Microfocus animator and CALL statements

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T17:15:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R8K9n.11814$3n2.11140@newsfe01.iad>`
- **In-Reply-To:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com>`

```
Derek Schrock wrote:
> Any idea how I can step INTO a CALL's code block using Microfocus
> Server Express 4.0 SP2 on HP-UX B11.11?
> Right now when I step on the CALL statement the animator executes the
> CALL by stepping over and not into.

You don't indicate - but it looks like you must be CALLing something 
other than M/F COBOL.

When first cutting my teeth on DBs with M/F (Net Express) and MS Access, 
I had problems understanding what was sometimes going wrong; that led me 
to having a separate OO class per Table within an MS Access xxxx.MDB. 
Even with the Animator it stepped over any errors in SQL Statements and 
I had to set Breakpoints on the nearest COBOL syntax immediately 
following a particular END-EXEC, to establish what I had done wrong in 
the SQL syntax.

The only qualifier - I don't work with Procedural or CALLs, so I've 
never tested via the Animator Procedural-COBOL-A CALLing 
Procedural-COBOL-B using .... returning .....  If the Animator can stand 
on its head animating a whole series of OO classes, (WITHOUT 
limitations), jumping backwards and forwards between my own classes and 
the M/F support classes, it doesn't make sense that you wouldn't be able 
to do that with Procedural applications.

Just a thought - any DIRECTIVES you can set, or options within the 
ANIMATOR itself that you can use ? I'm referring to the Dialog "Animate 
Settings" which comes from the drop-down menu 'Animate' in the IDE menu bar.

Jimmy, Calgary AB
```

#### ↳ Re: Microfocus animator and CALL statements

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-02T13:39:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7spaihFdriU1@mid.individual.net>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com>`

```
Derek Schrock wrote:
> Any idea how I can step INTO a CALL's code block using Microfocus
> Server Express 4.0 SP2 on HP-UX B11.11?
> Right now when I step on the CALL statement the animator executes the
> CALL by stepping over and not into.

Make sure that what you are CALLing (if it is COBOL) has been compiled for 
debugging.

Pete.
```

##### ↳ ↳ Re: Microfocus animator and CALL statements

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T17:51:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kGK9n.35649$BV.29152@newsfe07.iad>`
- **In-Reply-To:** `<7spaihFdriU1@mid.individual.net>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Derek Schrock wrote:
> 
…[7 more quoted lines elided]…
> debugging.

Jeez ! That WOULD be quite helpful, wouldn't it ? :-)
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-01T17:35:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad>`

```
On Feb 1, 7:51 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Pete Dashwood wrote:
> > Derek Schrock wrote:
…[9 more quoted lines elided]…
> Jeez ! That WOULD be quite helpful, wouldn't it ? :-)

To All,
Thanks for the prompt replies.  IRC has been a drag for COBOL support
and Microfocus forums have maybe three users.
But yes it's COBOL calling COBOL; I'll check tomorrow on how to build
the calling program for debugging.  I remember seeing this option int
the man page.
However, what type of file is a CALL executing?  .int? .gnt? If I have
both in $PATH should I make sure to only have the .int to ensure the
debuggable one is executed.
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T19:42:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HiM9n.77505$uH1.58738@newsfe25.iad>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
>>>Make sure that what you are CALLing (if it is COBOL) has been compiled for
>>>debugging.
…[12 more quoted lines elided]…
> debuggable one is executed.

It's not that complicated - well it isn't once somebody spells it out 
for you. At this stage you are in the IDE, writing source and then 
compiling and testing.

1. Ensure the box at the top left of the IDE 'Type of Build' shows 
"Generic Debug Build" in the dropdown list.

2. The first program you want executed in the project should be the 
first one that you use this feature for : Dropdown Menu : Project---->
"Add files to Project"------> gives you a list of files - select
Program-1.

3. Having added that first program, you can now do the following. 
File----> Open----> and open Program-1. (Alternatively in the RIGHT Pane 
- alphabetical list of files - select the source you want. (Don't select 
the ***.int from the Left Pane Treeview - anyway the Left Pane 'is a 
pain' - doesn't show entries in alphabetical sequence).

4. Now go to Project----> and you should see Program-1 Specified against 
'Compile', (or as a quickie you can use CTRL + F7 for a Build/Rebuild of 
Program-1).

5. You can follow Steps 3 and 4 for each program added, if you wish.

6. You are not quite sure what you have changed over time, then from 
Project----->select "Rebuild" which rebuilds all source which may have 
been changed.

6. At some stage at completion, (or earlier if you prefer), Project----> 
select "Rebuild ALL".

7. All these 'Builds' generate your ...INT and ....IDY files in the 
\DEBUG sub-folder for the Project. (They are used by the ANIMATOR). I 
recommend that for the developing stage, you ignore reference to files 
....GNT - I've never specifically used them.

8. Running data tests against the whole shebang - you find a program 
croaks with a logic error. You may be aware of which programs or 
situation where the error occurs, so you can zero in on that source for 
correction. Establish where in the appropriate source, that the error 
occurs and set an Animator BREAKPOINT just before it goes awry. Use the 
'EXAMINE' feature (Magnifying glass Icon) to see the values in variables 
causing you problems. As you get into the swing of things you can 
monitor variables or record fields and even put them into a temporary 
WatchList.

9. Building an executable - a different topic; you can read up on that 
later, but you have a fair bit to comprehend without worrying about that 
at this stage. When it comes to building the Executable(s) and support 
DLL libraries, you switch that Top Left 'Type of Build' ---> to read 
'Generic Release Build'.

I would recommend that you don't use the Release feature until you are 
more than satisfied that the project will work without any errors - that 
of course you can only find out by throwing spurious data at the 
project. But I might add, using the Animator feature EXAMINE you can 
change a value like "Tom Jones" to "Thomas Jones", '123.45' to '932.67',
or just for fun put alphabetics into numeric fields.

HTH

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 5)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-02T05:26:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<859274e8-abd6-4430-9cad-b1f55daa6d3c@k41g2000yqm.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com> <HiM9n.77505$uH1.58738@newsfe25.iad>`

```
On Feb 1, 9:42 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Derek Schrock wrote:
> >>>Make sure that what you are CALLing (if it is COBOL) has been compiled for
…[75 more quoted lines elided]…
> Jimmy, Calgary AB

I'm not using an IDE; it's vim to edit and cob to compile.
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T22:04:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4B67B273.1070705@shaw.ca>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
> To All,
> Thanks for the prompt replies.  IRC has been a drag for COBOL support
> and Microfocus forums have maybe three users etc.....

Derek,

I've posted this to you direct as well, in case you don't come here 
looking any more :-).

Having sent my previous message I reflected on "IRC" above - is that one 
of those cryptic e-mail abbreviations or did you buy and get support 
from something called IRC, or are you referring to Chat groups which I 
found googling on 'IRC'.

Why I ask, is because Rene in the Philippines made reference to vendors 
selling and supporting Micro Focus products. I found these 'vendors' by 
googling. I don't remember the name, but part of the Pentagon, something 
like ITNSC department, (Information Technology Navy Software Control), 
or some such name. The lady in the Control Branch was putting out a 
request for tenders to get info from Vendors selling Net Express, and 
defining the tech support they would provide.

Yep Micro Focus forums - they have become real dicey since Net Express V 
5.0, 5.1 - M/F are putting their money on .Net (let COBOL users ask the 
.Net folks for support). If you aren't aware there are two M/F forums -

(1) originally called Answer Exchange, and as Alan Wheeler the 
Administrator informed me, they can't currently use 'Answer Exchange' 
because it is copyrighted to the departed Merant - abysmal, but Micro 
Focus joined with one other to form Merant - but now M/F are back on 
their own. I'm not sure what the forum is now called. (I've still got it 
in my Bookmarks as 'Answer Exchange').

This is what I use to get in -

http://forum.microfocus.com/~Micro_Focus_Products/login

If successful and it prompts you for info, put in your Name and a 
password. If that doesn't work, backtrack to the Micro Focus main page 
to see if you can get at it as a new user.

It has sub-sets per topic and you are interested in Net Express. You can 
also check out an archive of messages which you can view, but those you 
can't respond to. A year or so back N/E used to have a busy time, say 
some 6 threads created per day, with suggested or finite solutions 
coming from other users and M/F employees; the M/F people are all over 
the place, (or were !), U.S, east and west coasts, Quebec, UK (Newbury) 
etc. Unfortunately like all commercial organizations and in the name of 
'rationalization' (musical chairs) some real M/F stalwarts have 
disappeared. It is quite some time since I've seen an M/F employee kick 
in - who knows, they may have been informed 'from above' - "Don't 
respond; anything before V 5.1, we just want it to die !". My suggestion 
may sound outrageous but from my own career I KNOW that sort of thing 
can happen in the commercial world.

They do have another forum - covering ALL their software and compilers, 
but I suspect you are supposed to be signed up for technical support 
($$$$$$ !) to be able to ask questions. It's a bit clinical - your 
question is presented anonymously and a solution is given. The link I 
found that will take you to that one is :-

http://www.support.microfocus.com/xmlloader.asp?type=home#

It will probably prompt you to log-in but select 'Knowledge Base' from 
the Left Pane in the page. True there's not a great deal in here about 
Net Express; and as I use OO , about four topics.

Your best bet to see what's available is the 'Answer Exchange'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T22:06:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4B67B2E3.80208@shaw.ca>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
> To All,
> Thanks for the prompt replies.  IRC has been a drag for COBOL support
> and Microfocus forums have maybe three users etc.....

Derek,

I've posted this to you direct as well, in case you don't come here
looking any more :-).

Having sent my previous message I reflected on "IRC" above - is that one
of those cryptic e-mail abbreviations or did you buy and get support
from something called IRC, or are you referring to Chat groups which I
found googling on 'IRC'.

Why I ask, is because Rene in the Philippines made reference to vendors
selling and supporting Micro Focus products. I found these 'vendors' by
googling. I don't remember the name, but part of the Pentagon, something
like ITNSC department, (Information Technology Navy Software Control),
or some such name. The lady in the Control Branch was putting out a
request for tenders to get info from Vendors selling Net Express, and
defining the tech support they would provide.

Yep Micro Focus forums - they have become real dicey since Net Express V
5.0, 5.1 - M/F are putting their money on .Net (let COBOL users ask the
.Net folks for support). If you aren't aware there are two M/F forums -

(1) originally called Answer Exchange, and as Alan Wheeler the
Administrator informed me, they can't currently use 'Answer Exchange'
because it is copyrighted to the departed Merant - abysmal, but Micro
Focus joined with one other to form Merant - but now M/F are back on
their own. I'm not sure what the forum is now called. (I've still got it
in my Bookmarks as 'Answer Exchange').

This is what I use to get in -

http://forum.microfocus.com/~Micro_Focus_Products/login

If successful and it prompts you for info, put in your Name and a
password. If that doesn't work, backtrack to the Micro Focus main page
to see if you can get at it as a new user.

It has sub-sets per topic and you are interested in Net Express. You can
also check out an archive of messages which you can view, but those you
can't respond to. A year or so back N/E used to have a busy time, say
some 6 threads created per day, with suggested or finite solutions
coming from other users and M/F employees; the M/F people are all over
the place, (or were !), U.S, east and west coasts, Quebec, UK (Newbury)
etc. Unfortunately like all commercial organizations and in the name of
'rationalization' (musical chairs) some real M/F stalwarts have
disappeared. It is quite some time since I've seen an M/F employee kick
in - who knows, they may have been informed 'from above' - "Don't
respond; anything before V 5.1, we just want it to die !". My suggestion
may sound outrageous but from my own career I KNOW that sort of thing
can happen in the commercial world.

They do have another forum - covering ALL their software and compilers,
but I suspect you are supposed to be signed up for technical support
($$$$$$ !) to be able to ask questions. It's a bit clinical - your
question is presented anonymously and a solution is given. The link I
found that will take you to that one is :-

http://www.support.microfocus.com/xmlloader.asp?type=home#

It will probably prompt you to log-in but select 'Knowledge Base' from
the Left Pane in the page. True there's not a great deal in here about
Net Express; and as I use OO , about four topics.

Your best bet to see what's available is the 'Answer Exchange'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T22:08:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4B67B362.9090401@shaw.ca>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
> To All,
> Thanks for the prompt replies.  IRC has been a drag for COBOL support
> and Microfocus forums have maybe three users etc.....

Derek,

I've posted this to you direct as well, in case you don't come here
looking any more :-).

Having sent my previous message I reflected on "IRC" above - is that one
of those cryptic e-mail abbreviations or did you buy and get support
from something called IRC, or are you referring to Chat groups which I
found googling on 'IRC'.

Why I ask, is because Rene in the Philippines made reference to vendors
selling and supporting Micro Focus products. I found these 'vendors' by
googling. I don't remember the name, but part of the Pentagon, something
like ITNSC department, (Information Technology Navy Software Control),
or some such name. The lady in the Control Branch was putting out a
request for tenders to get info from Vendors selling Net Express, and
defining the tech support they would provide.

Yep Micro Focus forums - they have become real dicey since Net Express V
5.0, 5.1 - M/F are putting their money on .Net (let COBOL users ask the
.Net folks for support). If you aren't aware there are two M/F forums -

(1) originally called Answer Exchange, and as Alan Wheeler the
Administrator informed me, they can't currently use 'Answer Exchange'
because it is copyrighted to the departed Merant - abysmal, but Micro
Focus joined with one other to form Merant - but now M/F are back on
their own. I'm not sure what the forum is now called. (I've still got it
in my Bookmarks as 'Answer Exchange').

This is what I use to get in -

http://forum.microfocus.com/~Micro_Focus_Products/login

If successful and it prompts you for info, put in your Name and a
password. If that doesn't work, backtrack to the Micro Focus main page
to see if you can get at it as a new user.

It has sub-sets per topic and you are interested in Net Express. You can
also check out an archive of messages which you can view, but those you
can't respond to. A year or so back N/E used to have a busy time, say
some 6 threads created per day, with suggested or finite solutions
coming from other users and M/F employees; the M/F people are all over
the place, (or were !), U.S, east and west coasts, Quebec, UK (Newbury)
etc. Unfortunately like all commercial organizations and in the name of
'rationalization' (musical chairs) some real M/F stalwarts have
disappeared. It is quite some time since I've seen an M/F employee kick
in - who knows, they may have been informed 'from above' - "Don't
respond; anything before V 5.1, we just want it to die !". My suggestion
may sound outrageous but from my own career I KNOW that sort of thing
can happen in the commercial world.

They do have another forum - covering ALL their software and compilers,
but I suspect you are supposed to be signed up for technical support
($$$$$$ !) to be able to ask questions. It's a bit clinical - your
question is presented anonymously and a solution is given. The link I
found that will take you to that one is :-

http://www.support.microfocus.com/xmlloader.asp?type=home#

It will probably prompt you to log-in but select 'Knowledge Base' from
the Left Pane in the page. True there's not a great deal in here about
Net Express; and as I use OO , about four topics.

Your best bet to see what's available is the 'Answer Exchange'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T23:37:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4B67C81F.9090006@shaw.ca>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
> To All,
> Thanks for the prompt replies.  IRC has been a drag for COBOL support
> and Microfocus forums have maybe three users etc.....

Derek,

I've posted this to you direct as well, in case you don't come here
looking any more :-).

Having sent my previous message I reflected on "IRC" above - is that one
of those cryptic e-mail abbreviations or did you buy and get support
from something called IRC, or are you referring to Chat groups which I
found googling on 'IRC'.

Why I ask, is because Rene in the Philippines made reference to vendors
selling and supporting Micro Focus products. I found these 'vendors' by
googling. I don't remember the name, but part of the Pentagon, something
like ITNSC department, (Information Technology Navy Software Control),
or some such name. The lady in the Control Branch was putting out a
request for tenders to get info from Vendors selling Net Express, and
defining the tech support they would provide.

Yep Micro Focus forums - they have become real dicey since Net Express V
5.0, 5.1 - M/F are putting their money on .Net (let COBOL users ask the
.Net folks for support). If you aren't aware there are two M/F forums -

(1) originally called Answer Exchange, and as Alan Wheeler the
Administrator informed me, they can't currently use 'Answer Exchange'
because it is copyrighted to the departed Merant - abysmal, but Micro
Focus joined with one other to form Merant - but now M/F are back on
their own. I'm not sure what the forum is now called. (I've still got it
in my Bookmarks as 'Answer Exchange').

This is what I use to get in -

http://forum.microfocus.com/~Micro_Focus_Products/login

If successful and it prompts you for info, put in your Name and a
password. If that doesn't work, backtrack to the Micro Focus main page
to see if you can get at it as a new user.

It has sub-sets per topic and you are interested in Net Express. You can
also check out an archive of messages which you can view, but those you
can't respond to. A year or so back N/E used to have a busy time, say
some 6 threads created per day, with suggested or finite solutions
coming from other users and M/F employees; the M/F people are all over
the place, (or were !), U.S, east and west coasts, Quebec, UK (Newbury)
etc. Unfortunately like all commercial organizations and in the name of
'rationalization' (musical chairs) some real M/F stalwarts have
disappeared. It is quite some time since I've seen an M/F employee kick
in - who knows, they may have been informed 'from above' - "Don't
respond; anything before V 5.1, we just want it to die !". My suggestion
may sound outrageous but from my own career I KNOW that sort of thing
can happen in the commercial world.

They do have another forum - covering ALL their software and compilers,
but I suspect you are supposed to be signed up for technical support
($$$$$$ !) to be able to ask questions. It's a bit clinical - your
question is presented anonymously and a solution is given. The link I
found that will take you to that one is :-

http://www.support.microfocus.com/xmlloader.asp?type=home#

It will probably prompt you to log-in but select 'Knowledge Base' from
the Left Pane in the page. True there's not a great deal in here about
Net Express; and as I use OO , about four topics.

Your best bet to see what's available is the 'Answer Exchange'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 5)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-02T05:25:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<abfc2821-8183-4009-9d84-10adb1e02ad6@u41g2000yqe.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com> <4B67C81F.9090006@shaw.ca>`

```
On Feb 2, 1:37 am, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Derek Schrock wrote:
> > To All,
…[68 more quoted lines elided]…
> Jimmy, Calgary AB

IRC as in Internet Relay Chat.
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 4)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-02-02T10:55:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hk9ou109n0@news7.newsguy.com>`
- **In-Reply-To:** `<5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com>`

```
Derek Schrock wrote:
> On Feb 1, 7:51 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
>> Pete Dashwood wrote:
>>> Derek Schrock wrote:
>>>> Any idea how I can step INTO a CALL's code block using Microfocus
>>>> Server Express 4.0 SP2 on HP-UX B11.11?

That's a rather old release, and I'm sure I don't remember everything
that's changed since then, so take this with a grain of salt.

>>>> Right now when I step on the CALL statement the animator executes the
>>>> CALL by stepping over and not into.

To summarize the other replies:

- Animator (like most debuggers) supports step-over and step-into.
Make sure you're using the latter.

- Animator only supports COBOL programs. If the target of the CALL
statement isn't COBOL, you can't debug it in Animator. (Actually,
there are mixed-language debugging options in Net Express, but I've
never looked at them, and I don't know that there's anything similar
in Server Express. Probably not, given the vagaries of debugging on
various Unix platforms.)

- Animator won't step into COBOL code that isn't compiled for debugging.

In short: the thing you're calling has to be a COBOL program compiled
for debugging, and you have to be sure you're using the correct
Animator command.

> However, what type of file is a CALL executing?  .int? .gnt? If I have
> both in $PATH should I make sure to only have the .int to ensure the
> debuggable one is executed.

The target of a CALL statement can be any of:

- an entry point (including COBOL programs, ENTRY statements, and
public symbols in non-COBOL code) in the current process - ie,
statically linked or already loaded

- the name of a .gnt module that has not yet been loaded into the
current process, but is in the current directory, or on $COBPATH
(*not* $PATH), or in the directory containing the calling program, or
in $COBDIR/dynload. (Once it's loaded, the default entry point will be
called; this is discussed in more detail in the docs. Subsequent calls
to this name fall under the previous case.)

- the name of a .int module that has not yet been loaded into the
current process, but is found using the search order listed above for .gnt

- the name of a COBOL Shared Object (CSO) module that has not yet been
loaded into the current process, but is on the OS library loader path
($LD_LIBRARY_PATH, $SHLIB_PATH, and/or $LIBPATH, depending on Unix flavor)

The search order, and the preference for .gnt over .int, can be
modified using run-time tunables. See the SX documentation on Run-time
Configuration.

.gnt modules and CSOs can be built for debugging, by the way. Also,
note that .gnt is a deprecated format. It's still supported, but it's
inferior to CSO.
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 5)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-03T06:27:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e398818c-1bef-4983-a4a1-6cd3242b96f1@g1g2000yqi.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com> <hk9ou109n0@news7.newsguy.com>`

```
On Feb 2, 10:55 am, Michael Wojcik <mwoj...@newsguy.com> wrote:
> Derek Schrock wrote:
> > On Feb 1, 7:51 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
…[63 more quoted lines elided]…
> Micro Focus

Thanks for the lengthy response Michael this is very valuable
information.  However, some of the items you sited I don't have
control over only because I'm only a poor luser.

We're stuck in B11.11, and can't switch to CSO.

But making use of $COBCONFIG and runtime turnables should turn out
very well for testing.
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

_(reply depth: 6)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-02-04T11:04:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hker7h2n4m@news1.newsguy.com>`
- **In-Reply-To:** `<e398818c-1bef-4983-a4a1-6cd3242b96f1@g1g2000yqi.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <7spaihFdriU1@mid.individual.net> <kGK9n.35649$BV.29152@newsfe07.iad> <5c9f1e89-e11c-4917-8428-71e729db042e@m4g2000vbn.googlegroups.com> <hk9ou109n0@news7.newsguy.com> <e398818c-1bef-4983-a4a1-6cd3242b96f1@g1g2000yqi.googlegroups.com>`

```
Derek Schrock wrote:
> 
> Thanks for the lengthy response Michael this is very valuable
> information.  However, some of the items you sited I don't have
> control over only because I'm only a poor luser.

Understood. It's rare to have complete control over the problem space,
and we're all subdued to what we work in, eh?

> But making use of $COBCONFIG and runtime turnables should turn out
> very well for testing.

Yes, I think you'll be able to control everything you need to, in
order to get your debugging to work.
```

#### ↳ Re: Microfocus animator and CALL statements

- **From:** CoboLero <cmarinos@gmail.com>
- **Date:** 2010-02-02T00:44:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0287d2c4-1ef8-4e19-a36d-1626fe523b97@n7g2000yqb.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com>`

```
On Feb 1, 10:34 pm, Derek Schrock <derekschr...@gmail.com> wrote:
> Any idea how I can step INTO a CALL's code block using Microfocus
> Server Express 4.0 SP2 on HP-UX B11.11?
> Right now when I step on the CALL statement the animator executes the
> CALL by stepping over and not into.

Just press F11 to step into the call or any other procedure, instead
of F10.
Christos.
```

##### ↳ ↳ Re: Microfocus animator and CALL statements

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-02T05:25:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5a42223-5aca-4f50-9355-7b0c6a7507a9@a32g2000yqm.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <0287d2c4-1ef8-4e19-a36d-1626fe523b97@n7g2000yqb.googlegroups.com>`

```
On Feb 2, 3:44 am, CoboLero <cmari...@gmail.com> wrote:
> On Feb 1, 10:34 pm, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[7 more quoted lines elided]…
> Christos.

I don't have an F11 commannd

http://supportline.microfocus.com/Documentation/books/sx40sp2/udpubb.htm
```

###### ↳ ↳ ↳ Re: Microfocus animator and CALL statements

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-02-02T07:27:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2ca325f-8d4f-4c35-85f7-fda02649c79f@f11g2000yqm.googlegroups.com>`
- **References:** `<3abd8110-ef87-49b2-a4fb-61c1ee65f638@m16g2000yqc.googlegroups.com> <0287d2c4-1ef8-4e19-a36d-1626fe523b97@n7g2000yqb.googlegroups.com> <a5a42223-5aca-4f50-9355-7b0c6a7507a9@a32g2000yqm.googlegroups.com>`

```
On Feb 2, 8:25 am, Derek Schrock <derekschr...@gmail.com> wrote:
> On Feb 2, 3:44 am, CoboLero <cmari...@gmail.com> wrote:
>
…[13 more quoted lines elided]…
> http://supportline.microfocus.com/Documentation/books/sx40sp2/udpubb.htm

Ok so the problem was resolved!  CALL is executing .gnt files hence
the reason why the debugger didn't step into the CALL's code.  Moving
the .gnt file[s] allows the debugger to load the .int file and I am
now debugging the CALL's code.

Thanks for the help guys.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
