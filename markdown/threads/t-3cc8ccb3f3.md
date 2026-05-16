[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# They said it couldn't be done.

_56 messages · 12 participants · 2010-01 → 2010-02_

---

### They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-25T00:19:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s2om7Fmu2U1@mid.individual.net>`

```
Here's a couple of intellectual exercises if anyone is bored or wants to 
think about something else for a break...

Two problems relating to COBOL... (Assume Fujitsu NetCOBOL for both 
solutions, or whatever version of COBOL you use if you can solve them with 
your current compiler.)

1. Imagine you have a couple of thousand COBOL programs, all written in ANSI 
74 procedural COBOL.  Almost every one of these programs makes static calls 
to a number of subroutines (say there are around 20 of these subroutines).

sample call :   CALL "X1" using p1, p2, p3, p4.

Obviously, because of the static linkage, there is HUGE duplication of these 
subroutines throughout the environment. (Every other program has the same 
subroutines statically linked into it, and some of these "subroutines" are 
"large"...) Changing any of the called routines means a nightmare of 
identifying and recompiling every program that uses it.

For reasons connected with a new environment, you need these routines to be 
dynamically called, but you cannot change all the calling programs. (In 
fact, the client has insisted that the calling program code must remain 
EXACTLY as it is.)

Can you get to a dynamic environment WITHOUT recoding or amending the 
calling programs?

2. You are replacing a service routine (a called program, not in COBOL) with 
a new routine, in COBOL. The new routine has the same signature as the old 
one and receives several parameters from the calling programs. Here is its 
signature:

procedure division using
                             p1, p2, p3, p4.

p1, p3, and p4 are always the same type and length.

But, p2 can vary in length (it is a record buffer). It could be defined in 
the working storage of each calling program as anything from 20 to 8000 
bytes. (Not with OCCURS... DEPENDING, just different fixed length records.)

Your called routine has to update this buffer; if you set a wrong length in 
the Linkage section you will immediately crash on a storage violation as 
soon as you try to write the record back.

You might think it is pretty easy to pass a record length or some other 
clue) as another parameter.  Nope. The same rules as above; you cannot 
modify the existing code, and it doesn't have a "p2-length" in its parameter 
list.

Clue: You MIGHT be able to derive the p2 length from an existing 
"dictionary", accessible by your new program.

Any thoughts on how the called program could be coded to accommodate these 
requirements?

FINALLY, as inspiration, some poetry...

"They said it couldn't be done
  But he, with a smile, denied it
  He said:'How do you know that it cannot be done?'
  Until you, at least, have tried it.

  So he rolled up his sleeves
  And he gritted his teeth
  And where there was doubt
  He hid it.

  And he tackled that job that
  'Couldn't be done'....
  And, Whaddya know?!!
  He couldn't bloody do it..."

Pete.
```

#### ↳ Re: They said it couldn't be done.

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-24T10:37:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```
On Jan 25, 12:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Here's a couple of intellectual exercises if anyone is bored or wants to
> think about something else for a break...
…[23 more quoted lines elided]…
> calling programs?

That is not a COBOL problem but is an implementation issue. Given that
all CALLs would have to be using a literal to get static linkage then
it is a matter of specifying the compiler and linking options
applicable to the particular system being used. For Fujitsu it is
DLOAD. Recompile and relink as a set of libraries and main program(s).

Anyway, identifying the calling programs is not a 'nightmare', a
simple 'grep -i "call \"name\"" *.cbl' will pick them up because with
static linking the CALL must be of a literal.

With dynamic linking there may be a problem because the CALL can be a
variable and the name may come from anywhere: in the case of most of
my systems they can come from a system file that holds the menus and
options, or can even be typed in directly.


> 2. You are replacing a service routine (a called program, not in COBOL) with
> a new routine, in COBOL. The new routine has the same signature as the old
…[25 more quoted lines elided]…
> requirements?

You do it exactly the same way as the original (non-COBOL) program
does currently.
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-25T11:28:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s3vsoFv26U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com>`

```
Richard wrote:
> On Jan 25, 12:19 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[33 more quoted lines elided]…
> DLOAD. Recompile and relink as a set of libraries and main program(s).

Yes, that is good. But you forgot to mention the ENTRY file that equates the 
entry point to a .DLL at run time.

DLOAD implements "dynamic program linkage" (as opposed to "dynamic linkage") 
and is a Fujitsu facility that allows the static calls to be processed 
dynamically at run time, via an ENTRY file which equates the entry points ot 
the respective libraries.

>
> Anyway, identifying the calling programs is not a 'nightmare', a
> simple 'grep -i "call \"name\"" *.cbl' will pick them up because with
> static linking the CALL must be of a literal.

As the site in question doesn't HAVE grep or an equivalent facility, for 
them, it is a nightmare.

>
> With dynamic linking there may be a problem because the CALL can be a
> variable and the name may come from anywhere:

That's why the ENTRY file is important.


> in the case of most of
> my systems they can come from a system file that holds the menus and
> options, or can even be typed in directly.

The Fujitsu ENTRY file is a text file that can be managed externally in a 
similar way. The PRIMA Toolset analyses any .DLL you specify and generates 
this file for you.

>
>
…[31 more quoted lines elided]…
> does currently.

No. The existing (non-COBOL program) has facilities that COBOL doesn't have, 
so you CAN'T do that.

No more clues... :-)

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-24T16:38:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net>`

```
On Jan 25, 11:28 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Jan 25, 12:19 am, "Pete Dashwood"
…[37 more quoted lines elided]…
> entry point to a .DLL at run time.

I didn't 'forget' it, it is not needed. The CALLs are literals so if
each called routine is named as, say, libX1.so then CALL "X1" will
find it without an ENTRY file.

> DLOAD implements "dynamic program linkage" (as opposed to "dynamic linkage")
> and is a Fujitsu facility that allows the static calls to be processed
> dynamically at run time, via an ENTRY file which equates the entry points ot
> the respective libraries.

It only needs the ENTRY file if you have bundled the routines into one
library file that needs to be identified.


>
> > Anyway, identifying the calling programs is not a 'nightmare', a
…[4 more quoted lines elided]…
> them, it is a nightmare.

If it doen't have grep or equivalent then _everything_ is a nightmare.

If they have Rexx or PERL or even AWK then they do have an equivalent
to grep. Writing a simple COBOL program to search source code for
CALLs should not be beyond them.

Your "doesn't HAVE grep or an equivalent" sounds exactly like like "it
couldn't be done".

> > With dynamic linking there may be a problem because the CALL can be a
> > variable and the name may come from anywhere:
>
> That's why the ENTRY file is important.

The problem as given was that currently the CALLs were static. This
means that it was CALL literal, thus no problem. But even with CALL
variable the system finds libNAME.so without any ENTRY file being
required.


> > in the case of most of
> > my systems they can come from a system file that holds the menus and
…[4 more quoted lines elided]…
> this file for you.

Not needed.

> >> 2. You are replacing a service routine (a called program, not in
> >> COBOL) with a new routine, in COBOL. The new routine has the same
…[34 more quoted lines elided]…
> No more clues... :-)

Fujitsu has ANY LENGTH
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T02:39:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5l9hF6q8U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com>`

```
Richard wrote:
> On Jan 25, 11:28 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[44 more quoted lines elided]…
> find it without an ENTRY file.

But then you wouldn't be using a library for your solution and yiour 
statement: "Recompile and relink as a set of _libraries _ " is not correct.
>
>> DLOAD implements "dynamic program linkage" (as opposed to "dynamic
…[5 more quoted lines elided]…
> library file that needs to be identified.

Or several library files, which ios what you siuggested.
>
>
…[8 more quoted lines elided]…
> If it doen't have grep or equivalent then _everything_ is a nightmare.

Perhaps...:-)

You'd be amazed the number of sites that actually function without tools a 
"good" site would take for granted.
>
> If they have Rexx or PERL or even AWK then they do have an equivalent
> to grep. Writing a simple COBOL program to search source code for
> CALLs should not be beyond them.
>
It was suggested.

> Your "doesn't HAVE grep or an equivalent" sounds exactly like like "it
> couldn't be done".

No, I didn't say that.
>
>>> With dynamic linking there may be a problem because the CALL can be
…[7 more quoted lines elided]…
> required.

Only if each subroutine is it's own module.
>
>
…[8 more quoted lines elided]…
> Not needed.

Funny, the solution doesn't run wthout it. (All of the claaed stubs arein a 
single .DLL)
>
>>>> 2. You are replacing a service routine (a called program, not in
…[37 more quoted lines elided]…
> Fujitsu has ANY LENGTH

That's a good point and I hadn't thought of it.

As I mentioned in a different post, there is usually more than one 
solution...

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-25T13:49:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjk7i7$lb9$4@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net>`

```
In article <7s5l9hF6q8U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Richard wrote:
>> On Jan 25, 11:28 am, "Pete Dashwood"
>> <dashw...@removethis.enternet.co.nz> wrote:

[snip]

>>> As the site in question doesn't HAVE grep or an equivalent facility,
>>> for them, it is a nightmare.
…[6 more quoted lines elided]…
>"good" site would take for granted.

As recently as 1996 I had a contract in an IBM mainframe shop where 
ABEND-Aid was not available and core-dumps had to be read.

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-01-25T15:14:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5qqlF6j8U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <hjk7i7$lb9$4@reader1.panix.com>`

```
In article <hjk7i7$lb9$4@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <7s5l9hF6q8U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
> ABEND-Aid was not available and core-dumps had to be read.

I remember clearly from my days doing COBOL in an IBM 360 environment
(actually, VM370) and reading core-dumps from an IBM was easy and
very useful.  The best I ever worked with and I have worked in a
lot of different environments.  I could easily take it right back to
the offending source statement.  

bill
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-01-25T08:53:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5efrl5ds51pmbbs4lcqo0d0s1p9uk6tfcd@4ax.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <hjk7i7$lb9$4@reader1.panix.com> <7s5qqlF6j8U1@mid.individual.net>`

```
On 25 Jan 2010 15:14:29 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>> As recently as 1996 I had a contract in an IBM mainframe shop where 
>> ABEND-Aid was not available and core-dumps had to be read.
…[5 more quoted lines elided]…
>the offending source statement.  

I remember liking having ABEND-Aid, but having everything on-line
makes core-dumps easier to use.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-25T17:24:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjkk59$as5$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s5l9hF6q8U1@mid.individual.net> <hjk7i7$lb9$4@reader1.panix.com> <7s5qqlF6j8U1@mid.individual.net>`

```
In article <7s5qqlF6j8U1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <hjk7i7$lb9$4@reader1.panix.com>,
>	docdwarf@panix.com () writes:
…[25 more quoted lines elided]…
>the offending source statement.  

You seem to be using yourself as a comparative, Mr Gunshannon, and my 
Sainted Paternal Grandfather - may he sleep with the angels! - warned 
against that, as mentioned recently.

The point I attempted to make was that even recently (by COBOL standards) 
there were shops that did not have tools which enhanced programmer 
productivity.  Certainly, one of a particular set of skills would know to 
check the PSW and find out where things blew up... but stuff like 
ABEND-Aid and MAX and FileAid and the like were (supposedly) created to 
make things easier.

I, for one, do not recall ever looking at the clock and saying 'Whoops, 
10:02am... time to set everything aside, grab a cup of coffee and catch up 
on the sports page'... and yet I've worked in shops where a goodly number 
of folks did just that.  I also find that some of my best work gets done 
when I stare at a screen and say 'Oh... don't tell *me* that I can't do 
that!'... then again, I try not to use myself as a comparative.

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-01-25T10:53:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mgmrl518t0lr67ufbnrf65qh9c1ak2bqkn@4ax.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s5l9hF6q8U1@mid.individual.net> <hjk7i7$lb9$4@reader1.panix.com> <7s5qqlF6j8U1@mid.individual.net> <hjkk59$as5$1@reader1.panix.com>`

```
On Mon, 25 Jan 2010 17:24:57 +0000 (UTC), docdwarf@panix.com () wrote:

>I, for one, do not recall ever looking at the clock and saying 'Whoops, 
>10:02am... time to set everything aside, grab a cup of coffee and catch up 
>on the sports page'... and yet I've worked in shops where a goodly number 
>of folks did just that.

That's silly, the sports page is in the other window on one's computer
(what's a newspaper?).    If one can't get caught up with sports and
celebrity gossip at one's desk, what will one talk about on one's
break?
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-25T18:35:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjko8l$qs8$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s5qqlF6j8U1@mid.individual.net> <hjkk59$as5$1@reader1.panix.com> <mgmrl518t0lr67ufbnrf65qh9c1ak2bqkn@4ax.com>`

```
In article <mgmrl518t0lr67ufbnrf65qh9c1ak2bqkn@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 25 Jan 2010 17:24:57 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[6 more quoted lines elided]…
>(what's a newspaper?).

The thing you use to try and block some of the radiation pouring out of 
the 3270 terminal, of course.

>If one can't get caught up with sports and
>celebrity gossip at one's desk, what will one talk about on one's
>break?

Where one is spending one's vacations... this was back when folks still 
worked in places long enough to get vacations, instead of getting 
Engulfed, Devoured and right-sized.

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-25T10:06:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1011c59a-0272-4019-a515-6855c0c4d325@e25g2000yqh.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net>`

```
On Jan 26, 2:39 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Jan 25, 11:28 am, "Pete Dashwood"
…[49 more quoted lines elided]…
>

A libNAME.so _is_ a dynamic link library on Unix/Linux (so = shared
object) on Windows it would be named libNAME.DLL

It may be that my set of libraries has one module per library but that
was not excluded as a solution, it is just that you were unaware of
that option.


> >> DLOAD implements "dynamic program linkage" (as opposed to "dynamic
> >> linkage") and is a Fujitsu facility that allows the static calls to
…[7 more quoted lines elided]…
>

You had specified there were about 20 called routines, I suggested
about 20 dynamic load libraries with naming that reflected the
routine's call name so no ENTRY file needed.

How hard is that ?

>
> >>> Anyway, identifying the calling programs is not a 'nightmare', a
…[22 more quoted lines elided]…
> No, I didn't say that.

What you implied was that 'an equivalent couldn't be done'.



> >>> With dynamic linking there may be a problem because the CALL can be
> >>> a variable and the name may come from anywhere:
…[8 more quoted lines elided]…
> Only if each subroutine is it's own module.

Each subroutine is in its own dynamic library, yes. Your point being ?


> >>> in the case of most of
> >>> my systems they can come from a system file that holds the menus and
…[9 more quoted lines elided]…
> single .DLL)

_YOUR_ solution may not run without it. _MY_ solution does not need
it. The problem as stated was to get "_a_ dynamic environment", and
did not require it to be identical to yours.


>
> >>>> 2. You are replacing a service routine (a called program, not in
…[46 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T10:51:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s6i3oFnf3U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <1011c59a-0272-4019-a515-6855c0c4d325@e25g2000yqh.googlegroups.com>`

```
Richard wrote:
> On Jan 26, 2:39 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[60 more quoted lines elided]…
>
What makes you think I was unaware of it? I was totally aware of it.  We 
opted for a single .DLL because it is a better solution.

>
>>>> DLOAD implements "dynamic program linkage" (as opposed to "dynamic
…[14 more quoted lines elided]…
> How hard is that ?

Not hard, just a poorer solution.

It means 20 different objects to be looked after when they can be in a 
single .DLL. (Library)

Just to avoid the use of an Entry file which is generated by a tool anyway?
>
>>
…[27 more quoted lines elided]…
>

Whatever inference you took is entirely a matter for you. There was no 
implication.

>
>
…[31 more quoted lines elided]…
>

No, of course not and there are a number of possible solutions.

If you like yours, that's fine. I don't care.

But be aware that I chose the solution I did in full awareness of the facts 
surrounding Fujitsu's Dynamic Program Linkage model both with and without 
the use of  an Entry file.

>
>>
…[44 more quoted lines elided]…
>>
Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-25T14:26:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4720d7ae-03dc-481b-8866-8eb123e2c9c9@h34g2000yqm.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <1011c59a-0272-4019-a515-6855c0c4d325@e25g2000yqh.googlegroups.com> <7s6i3oFnf3U1@mid.individual.net>`

```
On Jan 26, 10:51 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Jan 26, 2:39 am, "Pete Dashwood"
…[62 more quoted lines elided]…
> opted for a single .DLL because it is a better solution.

If you were "totally aware" that my solution did not require an ENTRY
file then why did you claim that I "forgot" it and that it was
"important" ?

Anyway whether a bundled DLL/so is 'better' or not was not part of the
problem you specified.


> >>>> DLOAD implements "dynamic program linkage" (as opposed to "dynamic
> >>>> linkage") and is a Fujitsu facility that allows the static calls to
…[14 more quoted lines elided]…
> Not hard, just a poorer solution.

No, it isn't. Just because it is not the same as _YOUR_ solution does
not make it "poorer".

In particular you had "a couple of thousand programs" so 20 or so
separate dlls is not a burden but if unit testing is a requirement for
production release then if one routine changed, or another routine was
added, then before distributing the one bundled dll file, every
routine in that file would need to be tested and signed off.

> It means 20 different objects to be looked after when they can be in a
> single .DLL. (Library)

It is called modularity.

> Just to avoid the use of an Entry file which is generated by a tool anyway?
>

No, it is not to _avoid_ the use of an ENTRY file, it is to have a
_better_ system (IMHO), one that incidentally does not require an
ENTRY file.


> >>>>> Anyway, identifying the calling programs is not a 'nightmare', a
> >>>>> simple 'grep -i "call \"name\"" *.cbl' will pick them up because
…[71 more quoted lines elided]…
>

So, why did you claim that I "forgot" it ?


>
>
…[47 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T00:56:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s83k6F9l3U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <1011c59a-0272-4019-a515-6855c0c4d325@e25g2000yqh.googlegroups.com> <7s6i3oFnf3U1@mid.individual.net> <4720d7ae-03dc-481b-8866-8eb123e2c9c9@h34g2000yqm.googlegroups.com>`

```
Richard wrote:
> On Jan 26, 10:51 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
>>>>>>> <dashw...@removethis.enternet.co.nz> wrote:
<snipped>
>>> _YOUR_ solution may not run without it. _MY_ solution does not need
>>> it. The problem as stated was to get "_a_ dynamic environment", and
…[11 more quoted lines elided]…
> So, why did you claim that I "forgot" it ?

Because you stated:

 "For Fujitsu it is DLOAD. Recompile and relink as a set of
 libraries and main program(s).
"
"Libraries" in this environment requires an Entry file.

Individual, separately called modules do not.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-26T10:17:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8aaf7b7-b0f4-4dde-b92a-30574d9ac119@c29g2000yqd.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <06760c68-cfd5-46d7-b011-733caded0fa0@m16g2000yqc.googlegroups.com> <7s5l9hF6q8U1@mid.individual.net> <1011c59a-0272-4019-a515-6855c0c4d325@e25g2000yqh.googlegroups.com> <7s6i3oFnf3U1@mid.individual.net> <4720d7ae-03dc-481b-8866-8eb123e2c9c9@h34g2000yqm.googlegroups.com> <7s83k6F9l3U1@mid.individual.net>`

```
On Jan 27, 12:56 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Jan 26, 10:51 am, "Pete Dashwood"
…[32 more quoted lines elided]…
> Individual, separately called modules do not.

The Fujitsu Cobol systems that I use can only produce and use two
types of files through the mechanism of '(re)compile and (re)link':
executables for main programs and shared object libraries (or DLLs). A
'module' is not a file type that can be created or loaded by a call.

It happens that a library can contain multiple programs (subroutines)
or just one. If each library contains a single program then, as I
stated, a _set_ of libraries is required, one for each program. If I
had said "_A_ library" then an entry file would be required but,
according to the manual:

"""The entry information may be omitted if the shared object file name
is "libprogram-name.so""".
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-01-25T13:48:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b5d933d$0$277$14726298@news.sunsite.dk>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net>`

```
Pete Dashwood wrote:

> Richard wrote:
>> On Jan 25, 12:19 am, "Pete Dashwood"
…[20 more quoted lines elided]…
>>> program that uses it.

<<snip>>

>> Anyway, identifying the calling programs is not a 'nightmare', a
>> simple 'grep -i "call \"name\"" *.cbl' will pick them up because with
>> static linking the CALL must be of a literal.

Minor change to the grep command :
  grep -E -i "call *\"name\"" *.cbl
so more than 1 space between call and literal will fit.

> As the site in question doesn't HAVE grep or an equivalent facility,
> for them, it is a nightmare.

Then a download at http://www.cygwin.com/ of the Free Software Cygwin
might be your solution in case they're running a version of MS-Windows.

FYI, I've never used Cygwin because of lack of such an OS here.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T02:44:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5lhcF8baU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <4b5d933d$0$277$14726298@news.sunsite.dk>`

```
Fred Mobach wrote:
> Pete Dashwood wrote:
>
…[41 more quoted lines elided]…
> FYI, I've never used Cygwin because of lack of such an OS here.

Thanks Fred. I think the lack of source management (or even versioning) in 
this place is a source of problems for them (it certainly would be for 
me:-)), but it is not something they are concerned about, especially as they 
will be replacing COBOL anyway.

I believe they will move to full source management as part of the new 
environment. (It is likely they will standardise on Visual Studio for 
teams.)

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-01-26T11:33:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b5ec4f2$0$275$14726298@news.sunsite.dk>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <4b5d933d$0$277$14726298@news.sunsite.dk> <7s5lhcF8baU1@mid.individual.net>`

```
Pete Dashwood wrote:

> Fred Mobach wrote:
>> Pete Dashwood wrote:
…[27 more quoted lines elided]…
> teams.)

Perhaps a recommendation to read 
http://en.wikipedia.org/wiki/Comparison_of_revision_control_software
before actually spending time and money on a new software environment ?
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T00:58:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s83mrFa72U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <4b5d933d$0$277$14726298@news.sunsite.dk> <7s5lhcF8baU1@mid.individual.net> <4b5ec4f2$0$275$14726298@news.sunsite.dk>`

```
Fred Mobach wrote:
> Pete Dashwood wrote:
>
…[34 more quoted lines elided]…
> ?

Certainly couldn't do any harm :-)

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-25T09:44:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9c296207-79da-4545-8003-7ebe10279e66@k19g2000yqc.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <4b5d933d$0$277$14726298@news.sunsite.dk>`

```
On Jan 26, 1:48 am, Fred Mobach <f...@mobach.nl> wrote:
> Pete Dashwood wrote:
> > Richard wrote:
…[37 more quoted lines elided]…
> might be your solution in case they're running a version of MS-Windows.

grep has available for decades on almost all systems including Windows
and IBM mainframes. For example http://www.dignus.com/freebies/

>
> FYI, I've never used Cygwin because of lack of such an OS here.

I would regard that as a bonus.


> --
> Fred Mobach - f...@mobach.nl
> website :https://fred.mobach.nl
>  .... In God we trust ....
>  .. The rest we monitor ..
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-01-26T10:53:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjn4re01ce6@news4.newsguy.com>`
- **In-Reply-To:** `<9c296207-79da-4545-8003-7ebe10279e66@k19g2000yqc.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <1c9304ab-6921-4f3d-8982-160b7fea7bae@b9g2000yqd.googlegroups.com> <7s3vsoFv26U1@mid.individual.net> <4b5d933d$0$277$14726298@news.sunsite.dk> <9c296207-79da-4545-8003-7ebe10279e66@k19g2000yqc.googlegroups.com>`

```
Richard wrote:
> On Jan 26, 1:48 am, Fred Mobach <f...@mobach.nl> wrote:
>> Pete Dashwood wrote:
>>
>>> As the site in question doesn't HAVE grep or an equivalent facility,
>>> for them, it is a nightmare.

What *are* they running on? A 1401?

>> Then a download athttp://www.cygwin.com/of the Free Software Cygwin
>> might be your solution in case they're running a version of MS-Windows.
> 
> grep has available for decades on almost all systems including Windows
> and IBM mainframes. For example http://www.dignus.com/freebies/

For that matter, Windows has included findstr.exe as part of the core
OS for many years, and it includes regular-expression support. findstr
is somewhat more awkward than grep, lacks the egrep-mode EREs, and has
some odd limitations (mostly due to the brain-dead parser in cmd.exe),
but for most purposes it's a usable grep substitute on Windows systems.

I have multiple Unix emulators on my Windows dev machines (typically
Microsoft's SFU / SUA, Cygwin, and MinGW), but I don't bother
switching to a bash or ksh window just for things like file searching.
The Windows commandline tools still aren't great (though Powershell is
coming along), but they're often adequate.
```

#### ↳ Re: They said it couldn't be done.

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2010-01-24T13:42:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:7s2om7Fmu2U1@mid.individual.net...
> Here's a couple of intellectual exercises if anyone is bored or wants to 
> think about something else for a break...
…[72 more quoted lines elided]…
>
I remember two times when I was able to do something that "couldn't" be 
done.  Afterwards the people who had said that (they were users) were very 
unhappy because they had previously be receiving large amounts of overtime 
for doing this manually.
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-25T12:05:02+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s420vFav7U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:7s2om7Fmu2U1@mid.individual.net...
…[78 more quoted lines elided]…
> amounts of overtime for doing this manually.

My experience, garnered over many installations and cultures, has been that 
when tech guys say: "You can't do that." what they really mean is: "I don't 
know how to do that."

The most memorable case of this in my experience was in Spain when IBM told 
a client that 3270 screens in conversational mode cannnot be automatically 
refreshed. (The client wanted a chief dealer's screen to be automatically 
updated when other dealers did a deal.). They were right; it says so in the 
manual...

I provided a solution and 2 weeks later IBM were invited to a demo where 
screens were automatically updated without Enter needing to be pressed, 
exactly as the client required.

The IBM guys were shocked and claimed I must have modified their software 
and it could no longer be supported by them. I hadn't. The solution was 
implemented, in standard IBM COBOL at the time (I think it was MVS/OS), 
using the standard IBM software without modification. I showed them how I 
did it and they said: "Awww...Well, of course... if you do it like THAT..." 
:-)

The point here is that because a company like IBM has huge credibility, 
clients have little option but to believe what they say.

Management in most companies is similarly dependent on the advice they 
receive from their tech leads. But sometimes those tech leads are not 
imaginative. They have found a way of doing things and it works. Anything 
outside that "cannot be done".

Some people have a major problem admitting that they don't know something, 
or they can't imagine a solution.

The actual number of things you would want to do that actually "can't be 
done" is very tiny. Most tech people get constrained by working in a given 
environment with given tools and come to believe there is only one effective 
approach and, if that can't be applied, then the problem is insoluble.

I learned many years ago to say: "I can't see a solution to that, but there 
might be one. Maybe we should get someone else to take a look."

Sometimes the results have been amazing and a very good learning experience 
for all concerned.

Sometimes a completely different approach can provide a solution. Setting 
technology aside and looking only at what is needed can be fruitful.

All too often solutions are tailored to the technology currently in place, 
simply because that is the technology currently in place. (Like, it isn't 
possible to buy additional tools or expertise (or depart from the current 
norm, because the benefits justify the departure...); that's not a tech. 
decision.)

The bottom line is that, at least in my opinion, it is completely 
unprofessional to say: "That can't be done." unless you qualify the 
statement.

("That can't be done within the constraints of the toolset we have 
available, BECAUSE...")

Much safer to simply say:"I don't know how to do that."

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-01-25T00:50:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2oednR0Vo6TcosDWnZ2dnUVZ_rWdnZ2d@giganews.com>`
- **In-Reply-To:** `<7s420vFav7U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com> <7s420vFav7U1@mid.individual.net>`

```
On 1/24/2010 5:05 PM, Pete Dashwood wrote:
> (snip)
> My experience, garnered over many installations and cultures, has been that
…[18 more quoted lines elided]…
> :-)

I'm not sure how to do it in Conversational CICS, but we did that in 
pseudo-conversational CICS.  The program waits on an ATTN key (such as 
ENTER), in order to accept 3270 input and display 3270 output, but it 
can be written to wait for either an ATTN key or a message sent to 
itself as a started task with a time delay.  You press enter to get the 
screen updated, or wait for the event/message to force a screen update.

I have worked with long-running conversational CICS programs, but only 
to service VTAM or TCP/IP ports.  None of those do screen dialogs with a 
human being.   I'm very curious how it's done with fully conversational 
CICS.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T02:48:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5lq6Fa0cU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com> <7s420vFav7U1@mid.individual.net> <2oednR0Vo6TcosDWnZ2dnUVZ_rWdnZ2d@giganews.com>`

```
Arnold Trembley wrote:
> On 1/24/2010 5:05 PM, Pete Dashwood wrote:
>> (snip)
…[31 more quoted lines elided]…
> conversational CICS.

This was IMS/DC, running in full conversational mode with serial 
reusability.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-25T13:28:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjk6ar$lb9$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com> <7s420vFav7U1@mid.individual.net>`

```
In article <7s420vFav7U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>The most memorable case of this in my experience was in Spain when IBM told 
>a client that 3270 screens in conversational mode cannnot be automatically 
…[9 more quoted lines elided]…
>and it could no longer be supported by them.

[snip]



We have different approaches, Mr Dashwood; after hearing 'You must have 
modified our software' my response would have been 'I have not done so and 
I find it insulting, unprofessional and unimaginative for you to blatantly 
misrepresent the facts demonstrated here in an effort to cover your lack 
of knowledge by impugning, belittling and attempting to dismiss my skills 
by asserting such a thing.  I will be more than willing to supply sample 
code as soon as your check clears the bank.'

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T02:54:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5m5eFc1bU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <N4udnfv-Wef2CcHWnZ2dnUVZ_gidnZ2d@earthlink.com> <7s420vFav7U1@mid.individual.net> <hjk6ar$lb9$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7s420vFav7U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[27 more quoted lines elided]…
> the bank.'

Well, I DID tease them a little bit before revealing the solution. :-)

My Boss was grinning ear to ear at their amazed gasps as terminals around 
the room started pinging, without anybody touching them.

I didn't want to alienate them too mch because I would be moving on and the 
customer would need their support after I was gone.

In terms of credibility it was amazing. After that I walked on water and got 
anything I wanted for the tech team :-)

And it wasn't really a lack of knowledge (they completely understood the 
solution once it was revealed); rather, a lack of imagination...

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-25T14:28:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjk9r3$iut$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s420vFav7U1@mid.individual.net> <hjk6ar$lb9$1@reader1.panix.com> <7s5m5eFc1bU1@mid.individual.net>`

```
In article <7s5m5eFc1bU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7s420vFav7U1@mid.individual.net>,
…[30 more quoted lines elided]…
>Well, I DID tease them a little bit before revealing the solution. :-)

As I said, Mr Dashwood, we see it differently.  As I see it you had a set 
of skills and experiences which could be combined in a manner which 
generated a solution which someone else - in this case IBM, an 
organisation which has a rather large profit-motive - could use to make 
money.

No problem there... you want to make money from my abilities, *I* want to 
make money from my abilities.  Works both ways, I'd say.

(Note that this is for another party involved.  IBM, I believe, was not 
collecting your timesheets nor paying for your invoices.  If your Boss 
wants to give away trade secrets then that's his concern; under most 
contracts I've worked *anything* I've developed for the paying client is 
the paying client's property.)

>
>My Boss was grinning ear to ear at their amazed gasps as terminals around 
…[3 more quoted lines elided]…
>customer would need their support after I was gone.

If 'playing by the same set of rules as you do' is seen as 'alienating' 
then a request for explanation - in as public a setting as possible - is a 
reasonable attempt to clarify the groundrules from which all members of 
the team are working.  After all, We're All In This Together, right?

(they absolutely *hate* it when their own buzzwords are thrown back at 
them, or so I've noticed)

[snip]

>And it wasn't really a lack of knowledge (they completely understood the 
>solution once it was revealed); rather, a lack of imagination...

They may have had all the pieces, Mr Dashwood, but they did not know how 
you managed to put them together.  If OCO (Object Code Only) is good 
enough for their programs them it is good enough for yours; give them the 
load modules and say 'it's all in there'.

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T11:32:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s6kgdF5etU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s420vFav7U1@mid.individual.net> <hjk6ar$lb9$1@reader1.panix.com> <7s5m5eFc1bU1@mid.individual.net> <hjk9r3$iut$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7s5m5eFc1bU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[45 more quoted lines elided]…
> not collecting your timesheets nor paying for your invoices.

Nobody collected timesheets from me as I worked on a daily basis, and was 
contracted direct to the client. However, the client did pay my invoices and 
I did my very best to justify the not insignificant amounts on those 
invoices, by ensuring that he got what he wanted rather than what IBM said 
was possible. I went there on a 6 month contract to design a database and 
ended up staying 2 years. My wife instigated it as she spoke a little 
Spanish and she was tired of living in Germany. We could have stayed in 
Madrid indefinitely but after 2 years she was ready to return to the U.K. I 
never wanted to go there but I have to say they treated us very well and it 
was a good place to live and work.

> If your
> Boss wants to give away trade secrets then that's his concern;

No, he just wanted to get his screens refreshed and was amused when we were 
able to do it after IBM assured him it was not possible. I think if I had 
refused to divulge the code, he would have supported me (we got on really 
well), but then he would have been left with "reluctant" support from IBM 
(or none at all), and having a hostile vendor is not something any site can 
endure for long.



>under
> most contracts I've worked *anything* I've developed for the paying
> client is the paying client's property.)

I always crossed that clause out in the contract and gave them a 
non-exclusive right to anything I did, retaining the Intellectual Property 
myself..

Agent: "But it's a STANDARD clause...it's in ALL of our contracts."

Me: "Sorry, a contract is an AGREEMENT and I cannot AGREE to a restrictive 
condition which affects my ability to make a living in the future."

Boss of Agency is fetched. I explain that if I am precluded from the use of 
stuff I originated (which could be better ways to do things), then the next 
contract I go to, I can't use that experience. Certainly, the client is 
paying for it and should enjoy full and unhindered rights to it, but those 
rights are non-exclusive and I would NEVER release Intellectual Property 
rights unless a very large sum of money changed hands.

Boss of Agency thinks about the fact that the client will never see this 
contract anyway, it will be filed in a draw and never looked at once it is 
signed, then thinks about all the lovely money he is going to make if I am 
placed on site, and initials the contract change.

I have never had a single Agency refuse to place me because I refused that 
clause, and if they did, I'd go down the road to another agency. Why would 
you make money for people who have no idea what's going on? There was one 
occasion where the Agent wouldn't do it and couldn't get to his Boss, who 
was out of town. I had already been interviewed by the client and we were 
both quite keen to start. They phoned me and asked what the problem was. I 
told them. Three hours later the Agent came back and said that his Boss had 
authorised it by fax...

>
>>
…[13 more quoted lines elided]…
> them, or so I've noticed)

Absolutely. :-)

It is a bit ironic and as a friend of mine once remarked: "That which you 
resist, you often connect with." I spent years of my life as a contractor 
"skirmishing" with IBM. The above is not an isolated instance :-)

Then, one day, I found myself working for them, on site at North Harbour in 
Southampton (England) and later at the famous Hursley Park where CICS was 
invented. It was an interesting experience which I could never have 
anticipated. Like all large organizations they have good people (sometimes 
actually outstanding people) and they have not-so-good people. They also 
have their share of Corner Office Idiots and I was forced to work for one of 
them for a while. The whole business was a growth experience and I don't 
regret any of it.
>
> [snip]
…[7 more quoted lines elided]…
> them the load modules and say 'it's all in there'.

In reality, I couldn't have them refusing to support the client because they 
believed their standard code had been bent. There was really no option but 
to show them what was done. Still, it was fun and I did enjoy it... :-)
>
> DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-26T14:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjmtu7$5uc$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s5m5eFc1bU1@mid.individual.net> <hjk9r3$iut$1@reader1.panix.com> <7s6kgdF5etU1@mid.individual.net>`

```
In article <7s6kgdF5etU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7s5m5eFc1bU1@mid.individual.net>,
…[60 more quoted lines elided]…
>> Boss wants to give away trade secrets then that's his concern;

[snip]

>Why would 
>you make money for people who have no idea what's going on?

That was my point exactly, Mr Dashwood... IBM not only had no idea what 
was going on (insofar as your manipulation of their technology was 
concerned) and stated that your techniques must have required modification 
of their software to the point of unsupportability.

To learn that this conclusion is Just Plain Wrong is, I would say, a 
valuable thing and not to be given away without due recompense.

DD
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T17:22:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s9tbqF323U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s5m5eFc1bU1@mid.individual.net> <hjk9r3$iut$1@reader1.panix.com> <7s6kgdF5etU1@mid.individual.net> <hjmtu7$5uc$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7s6kgdF5etU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[78 more quoted lines elided]…
> DD

I understand your point, Doc, but there was more at stake here than 
"teaching IBM a lesson..."

I walked away happy (all the way to the bank), IBM were let off the hook, so 
they were happy, and My Boss was happy because all he wanted was certain 
screens refreshed when certain events happened... :-)

(In a non-mainframe world, that would really be standard procedure...)

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-01-27T14:39:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjpj7k$4tp$1@reader1.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7s6kgdF5etU1@mid.individual.net> <hjmtu7$5uc$1@reader1.panix.com> <7s9tbqF323U1@mid.individual.net>`

```
In article <7s9tbqF323U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7s6kgdF5etU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>> Why would
>>> you make money for people who have no idea what's going on?
…[10 more quoted lines elided]…
>"teaching IBM a lesson..."

My apologies for being so obscure, Mr Dashwood, but what I saw at stake 
here was not 'teach(ing) IBM a lesson', it was adhering to the rather 
ancient tradition of barter/trade/sale of 'I have something you would like 
to have, you have something I would like to have... perhaps arrangements 
might be made for an exchange.'

As I formulated, long ago, when I was more bitter and less kindly and 
altruistic than I am now... 'Knowledge is Power but Information is Money.'

DD
```

#### ↳ Re: They said it couldn't be done.

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-01-24T11:26:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```
On Jan 24, 11:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Here's a couple of intellectual exercises if anyone is bored or wants to
> think about something else for a break...
…[24 more quoted lines elided]…
>

How about renaming the called programs and replacing the original
called program with a stub program to dynamically call the renamed
program. I don't know if that would work under MVS as I don't know if
a static recompile can call a program which executes a dynamic call.


But don't tease, give us solutions not problems (as a really shite
manager of mine used to say).
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-01-24T14:52:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com>`
- **In-Reply-To:** `<54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com>`

```
On 1/24/2010 1:26 PM, Alistair wrote:
> On Jan 24, 11:19 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz>  wrote:
…[10 more quoted lines elided]…
> manager of mine used to say).

It should be possible to do this under MVS (now z/OS).  The 
Binder/Linkage editor has a feature that allows you to relink an 
existing program, removing a statically bound subprogram and replacing 
it with a new statically bound subprogram.  If that program is COBOL it 
can turn around and call any subprogram dynamically.

You don't need to recompile the main calling program.  But you would 
need to write two programs to replace each static subprogram, the first 
would be a stub with the same name, to call the second dynamically with 
whatever name you choose.

It would help quite a bit if the main COBOL program uses COBOL or 
Language Environment runtime libraries.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-25T12:20:41+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s42uaFfk5U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com> <ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com>`

```
Arnold Trembley wrote:
> On 1/24/2010 1:26 PM, Alistair wrote:
>> On Jan 24, 11:19 am, "Pete Dashwood"
…[25 more quoted lines elided]…
> Language Environment runtime libraries.

Interesting post, Arnold. That is along the lines of what we actually did in 
the end. We wrote a single .DLL that contained the stubs, and these called 
the new subroutines dynamically.

The Fujitsu "Dynamic Program Linkage" model (implemented via the DLOAD 
compiler option and with a suitable ENTRY file containing all the stub names 
and equating them to the stub .DLL) , means there were no changes required 
to the existing source, but it had to be batch recompiled with the DLOAD 
option.

Only difference I can see from your solution is that we collected all the 
stubs under one "umbrella" .DLL, rather than as separate called modules.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2010-01-26T17:07:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vlul5htdbu4dq2jhsie6aatrh2esdnsat@4ax.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com> <ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com> <7s42uaFfk5U1@mid.individual.net>`

```
On Mon, 25 Jan 2010 12:20:41 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Arnold Trembley wrote:
>> On 1/24/2010 1:26 PM, Alistair wrote:
…[39 more quoted lines elided]…
>stubs under one "umbrella" .DLL, rather than as separate called modules.

Unless none of the components change, I don't see the advantage of the
single DLL but then I'm used to the IBM MVS environment.  For that
environment, assuming that the subroutines were all separately
compiled, the change would be re-compile the calling programs changing
the compile option from NODYNAM to DYNAM.  This would not work for
CICS programs.  The second part means that the length of parameter 2
must have been determinable based on data passed in the other
parameters and action could then be taken based on that data.  If the
field had a prefix, there are cute tricks to allow getting at that
prefix.
>
>Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T17:14:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s9stqF12iU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com> <ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com> <7s42uaFfk5U1@mid.individual.net> <2vlul5htdbu4dq2jhsie6aatrh2esdnsat@4ax.com>`

```
Clark F Morris wrote:
> On Mon, 25 Jan 2010 12:20:41 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[35 more quoted lines elided]…
>> stubs, and these called the new subroutines dynamically.

That was misleading. The .dll actually contains the routines. They are
called dynamiclly through the DLOAD.
>>
>> The Fujitsu "Dynamic Program Linkage" model (implemented via the
…[3 more quoted lines elided]…
>> batch recompiled with the DLOAD option.

That's pretty much what we did.

>>
>> Only difference I can see from your solution is that we collected
…[4 more quoted lines elided]…
> single DLL but then I'm used to the IBM MVS environment.

As it happens they mostly don't change, but the whole .dll is managed as a
single project. That makes it easy to manipulate.


>  For that
> environment, assuming that the subroutines were all separately
> compiled, the change would be re-compile the calling programs changing
> the compile option from NODYNAM to DYNAM.

I seem to remember NORENT has to become RENT, but that may not be true any
more.

>This would not work for
> CICS programs.

Yes. I DO remember that... :-)



>The second part means that the length of parameter 2
> must have been determinable based on data passed in the other
> parameters and action could then be taken based on that data.

No, I specifically stated that that was not the case. Nothing in the passed
parameters indicates the length of P2.

However, it can be derived separately from an available dictionary.


 If the
> field had a prefix, there are cute tricks to allow getting at that
> prefix.

I seem to recall using negative subscripting, but I'd be surprised if that
still works.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-01-26T15:09:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<effb2c15-7008-4a2b-ae50-ed2965fac5e0@f12g2000yqn.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com> <ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com> <7s42uaFfk5U1@mid.individual.net>`

```
On Jan 25, 12:20 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Arnold Trembley wrote:
> > On 1/24/2010 1:26 PM, Alistair wrote:
…[39 more quoted lines elided]…
>

I am not sure that you are using the term 'stubs' as I understand it.
A stub is code that satisfies a CALL, for example during development,
in place of the actual called program. It seems that you have written
stubs for each called program and this, in turn, simply does a dynamic
call of actual subroutine program.

Why did you need to write 'stubs' that you collected "under one
"umbrella" .DLL" when "these [stubs] called the new subroutines
dynamically".

   PROGRAM
   CALL "X1"  -->  STUB.DLL
                   X1: CALL "X1ROUTINE"  --> X1ROUTINE ??
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T17:18:41+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s9t53F20nU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com> <ttadnSjRz_xhL8HWnZ2dnUVZ_omdnZ2d@giganews.com> <7s42uaFfk5U1@mid.individual.net> <effb2c15-7008-4a2b-ae50-ed2965fac5e0@f12g2000yqn.googlegroups.com>`

```
Richard wrote:
> On Jan 25, 12:20 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[50 more quoted lines elided]…
> call of actual subroutine program.

Yes, what I wrote does look like that. It isn't what we did.
>
> Why did you need to write 'stubs' that you collected "under one
…[5 more quoted lines elided]…
>                    X1: CALL "X1ROUTINE"  --> X1ROUTINE ??

please see response to Arnold.

Pete.
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-25T12:12:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s42e9Fd6rU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <54f8647b-3394-4b7e-89b5-42cf7d9d3b71@c34g2000yqn.googlegroups.com>`

```
Alistair wrote:
> On Jan 24, 11:19 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[34 more quoted lines elided]…
>
That would certainly be one solution. Maybe not elegant, but it would 
definitely reduce all the staticaly linked code.

I can't see any reason why a statically linked program shouldn't call a 
program that makes dynamic calls, but it is many years since I worked in 
that environment.

>
> But don't tease, give us solutions not problems (as a really shite
> manager of mine used to say).

Like many classes of problem, there is more than ONE way to do this. It 
isn't a tease; these are real life examples taken from actual work I am 
currently doing. The actual solutions implemented will be posted in a few 
days after people who want to have a go at it have done so.

It is interesting to see how different environments would provide for a 
solution, also.

Pete.
```

#### ↳ Re: They said it couldn't be done.

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-01-25T13:56:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b5d950c$0$280$14726298@news.sunsite.dk>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```
Pete Dashwood wrote:

> Here's a couple of intellectual exercises if anyone is bored or wants
> to think about something else for a break...
…[3 more quoted lines elided]…
> with your current compiler.)

<<1 is discussed enough I think>>

> 2. You are replacing a service routine (a called program, not in
> COBOL) with a new routine, in COBOL. The new routine has the same
…[27 more quoted lines elided]…
> these requirements?

In case you use a data definition in the linkage section with a 
01  THISGROUPITEM.
  03  THISITEM PIC X OCCURS 8000.
and you can get the length to be processed from an existing "dictionary"
and don't access the THISGROUPITEM nor any byte in THISGROUPITEM beyond
the indicated length on mainframes known to me no crash will occur.
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T03:00:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5mgcFe63U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <4b5d950c$0$280$14726298@news.sunsite.dk>`

```
Fred Mobach wrote:
> Pete Dashwood wrote:
>
…[46 more quoted lines elided]…
> no crash will occur.

I agree that would work. I assume you would refmod the group level when 
updating the buffer?

move changed-stuff to THISGROUPITEM (1: derived-length)  ?

Fujitsu provides a slightly more elegant way to do it which I'll post later.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-01-26T11:48:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b5ec87e$0$279$14726298@news.sunsite.dk>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <4b5d950c$0$280$14726298@news.sunsite.dk> <7s5mgcFe63U1@mid.individual.net>`

```
Pete Dashwood wrote:

> Fred Mobach wrote:
>> Pete Dashwood wrote:
…[52 more quoted lines elided]…
> move changed-stuff to THISGROUPITEM (1: derived-length)  ?

Yes, after checking if the derived-length is not out of range. 
Or the old way with 
  PERFORM ... VARYING ... FROM 1 BY 1 UNTIL ... > LENGTHFIELD.
 
> Fujitsu provides a slightly more elegant way to do it which I'll post
> later.
 
The Fujitsu compiler is unknown to me, the Siemens (later Fujitsu
Siemens) COBOL compilers on the other hand ...

But then again, I'm still eager to learn. :-)
```

#### ↳ Re: They said it couldn't be done.

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-01-25T11:24:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjkgkp02fff@news4.newsguy.com>`
- **In-Reply-To:** `<7s2om7Fmu2U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> 1. Imagine you have a couple of thousand COBOL programs, all written in ANSI 
…[11 more quoted lines elided]…
> calling programs?

In MF COBOL, I'd just repackage the called programs as dynamic-load
modules (ie, as DLLs on Windows or CSOs on Unix). No source changes
necessary.

If source changes *were* necessary in the COBOL environment, this
would seem to be a simple matter of shimming. (Rename called program
"A" to "A-dynamic" or some such thing. Create a new "A" that does the
dynamic call to "A-dynamic". Old caller calls the new "A" shim.) Am I
missing something?

> 2. You are replacing a service routine (a called program, not in COBOL) with 
> a new routine, in COBOL. ...
…[14 more quoted lines elided]…
> requirements?

There isn't enough information in the problem.

Either the length of the buffer is available out-of-band, or it isn't.
The problem says it "MIGHT" be available from a dictionary. That's not
a useful statement. It might be available from magic computer elves,
too; but either we don't have to accommodate the case where it is not
available from that source, in which case the problem is solved, or we
do, in which case we are no closer to a general solution.

In some environments the information might be available from the
environment in some fashion. We don't know if that's the case here,
since the problem doesn't specify it.

Other metadata might be available in the buffer or the other
parameters. Again, the problem doesn't specify.

In short, this second problem reduces to "datum X may not be
available; how do you acquire datum X?". Clearly underdetermined.

The phrasing of the problem does open one possibility:

> Your called routine has to update this buffer; if you set a wrong length in 
> the Linkage section you will immediately crash on a storage violation as 
> soon as you try to write the record back.

I'll assume any other access idiom, such as reference modification,
would be equivalent to "set a wrong length" here - that the key is an
attempt to write past the end of the record.

Then, *if* the environment provides a mechanism for detecting and
handling exception conditions at the application level, your routine
or code it invokes could probe the record to find the trap point.
Again, this is not specified in the problem, so we can't rely on this
as a general solution. But, for example:

- In Windows, use the pointer-testing routines or SEH to probe
locations in the buffer to see if they're writable

- In Unix, use a SIGSEGV handler that sets a flag to detect when a
probe fails. In some Unix implementations, you can also use the EFAULT
trick - perform I/O from and to the buffer (saving the contents first
in the latter case) against a descriptor for /dev/null, and look for
an EFAULT error return. This behavior isn't guaranteed by SUS, though.

- On the AS/400, call a subprogram that probes the buffer and handles
the appropriate message.

And so forth. It might be tempting to binary-search for the buffer
length, but given the likely overhead of a faulting miss (ie, a probe
that strikes past the end of the buffer), a linear probe from the
beginning is likely to be faster. (With more information about the
platform architecture, you might do better - for example, on a typical
paged-memory system you only need to check each page - but the problem
definition excludes that: it says any attempt to write past the end of
the buffer will fail, so this must not be a paged system. Note that
rules out Windows and Unix, so the strategies suggested for those
platforms above are irrelevant.)
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T11:35:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s6kleF69gU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[23 more quoted lines elided]…
> missing something?

Thanks Michael. (Nice to see you back, BTW :-))

That is pretty much what we did. I'm glad it can work in a MF environment 
too.

>
>> 2. You are replacing a service routine (a called program, not in
…[73 more quoted lines elided]…
> platforms above are irrelevant.)
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T11:40:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s6kukF7tuU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com>`

```

Sorry, my response was posted prematurely :-) more below...

> Pete Dashwood wrote:
>>
…[50 more quoted lines elided]…
> do, in which case we are no closer to a general solution.

Yes, that is fair comment. I used MIGHT because there was some doubt about 
whether the "dictionary" would actualy be built and accessible. Also, this 
is meant to be a fun exercise and not to be taken too literally (I should 
have known that posting it here would preclude any element of fun... :-( )

Take it, for the sake of the exercise that a it IS possible to derive the 
length of the buffer in the calling program, from a dictionary.
>
> In some environments the information might be available from the
…[46 more quoted lines elided]…
> platforms above are irrelevant.)
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-01-26T11:05:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjn4re11ce6@news4.newsguy.com>`
- **In-Reply-To:** `<7s6kukF7tuU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com> <7s6kukF7tuU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[18 more quoted lines elided]…
> whether the "dictionary" would actualy be built and accessible.

OK, but we still don't know whether we can use it in our solution...

> Also, this
> is meant to be a fun exercise and not to be taken too literally (I should 
> have known that posting it here would preclude any element of fun... :-( )

I didn't say I wasn't having fun with it! Just that there wasn't
enough information to solve the problem. (Clearly, there was enough to
speculate at some length... :-)

> Take it, for the sake of the exercise that a it IS possible to derive the 
> length of the buffer in the calling program, from a dictionary.

OK. In that case I'd probably use reference modification to operate on
the buffer using the correct length, assuming standard procedural COBOL.

In our comms code, it's pretty common to have linkage like:

	01  incoming-record.
	  03  rec-length		pic x(4) comp-x.
	  03  rec-data		pic x.

Then "rec-data" is actually processed with refmod, for example:

	move rec-data(1:rec-length) ...

Obviously that's a highly simplified version - with no length
validation, you'd have a nifty stack-smashing opportunity here - but
you get the idea.

(In .NET managed code, I could declare a working-storage "binary-char
unsigned occurs any" item, then set its length and contents from the
linkage item. Then I'd have an Array object with the correct length
and all the other Array methods available, which would make the
subsequent code safer and cleaner.)
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T17:25:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s9thbF3ndU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com> <7s6kukF7tuU1@mid.individual.net> <hjn4re11ce6@news4.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
…[59 more quoted lines elided]…
> subsequent code safer and cleaner.)

Excellent!

Fujitsu has some special facilities that make this easy. We used those.

Pete.
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-26T11:49:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s6lg4FavtU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com>`

```
Oh Crap! Premature response again! (had the cursor in the wrong place, 
sorry... :-)

see below...

Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[79 more quoted lines elided]…
> locations in the buffer to see if they're writable

I hadn't thought of that one. Not elegant but a possibility.

>
> - In Unix, use a SIGSEGV handler that sets a flag to detect when a
…[17 more quoted lines elided]…
> platforms above are irrelevant.)

I did consider trying to detect the end of the buffer by checking characters 
and trapping a storage violation, but it is pretty awful isn't it? (As the 
buffer could be 8000 characters this approach was ruled out fairly early on 
in the piece.)

Another possibility would be to drop into Assembler and get the parameter 
length from the stack (this is Windows), assuming COBOL puts it there. (I 
have a feeling the calling program pushes each parameter and its length onto 
the stack  (the calling mode determines who cleans up the stack afterwards 
if I remember rightly),but it is ages since I worked at that level and I 
simply don't have time for the experiments I would need to do to confirm it.

Pete.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-01-26T12:00:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b5ecb60$0$273$14726298@news.sunsite.dk>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com> <7s6lg4FavtU1@mid.individual.net>`

```
Pete Dashwood wrote:

> I did consider trying to detect the end of the buffer by checking
> characters and trapping a storage violation, but it is pretty awful
> isn't it? (As the buffer could be 8000 characters this approach was
> ruled out fairly early on in the piece.)

Trapping storage violations is a time consuming process that you really
don't want to see as a solution. You are right on that one.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-01-26T11:21:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjn4rf21ce6@news4.newsguy.com>`
- **In-Reply-To:** `<7s6lg4FavtU1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com> <7s6lg4FavtU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[4 more quoted lines elided]…
> I hadn't thought of that one. Not elegant but a possibility.

Yes, it's rather a hack. And the Windows IsBadReadPtr / IsBadWritePtr
functions are deprecated (and particularly dangerous in a
multithreaded process), so SEH would be the way to go - but it's
difficult to use in a language that doesn't have built-in support.

> I did consider trying to detect the end of the buffer by checking characters 
> and trapping a storage violation, but it is pretty awful isn't it? (As the 
> buffer could be 8000 characters this approach was ruled out fairly early on 
> in the piece.)

Agreed. It's inelegant and the overhead is bad. It can be improved by
only testing each page, on a paged-memory system - with a maximum
length of 8000 bytes, you'd only have to test three addresses on the
typical 4KB-page OS. (8000 bytes could begin partway through one page,
contain all of a second, and stretch into a third.)

But deliberately trapping, however popular with the "use exceptions
for control flow" crowd, really isn't something you want to do on
every call.

> Another possibility would be to drop into Assembler and get the parameter 
> length from the stack (this is Windows), assuming COBOL puts it there. (I 
…[3 more quoted lines elided]…
> simply don't have time for the experiments I would need to do to confirm it.

Depends on the implementation, and in many cases on compiler options
or language extensions. The standard Windows calling conventions don't
put parameter lengths on the stack, but compilers can implement other
calling conventions. They can even be interoperable (ie, a COBOL
implementation could include length info without breaking calls to C,
for example), if the length information doesn't change the layout of
the normal parameter values. For example, a COBOL implementation could
put length info after the last parameter, effectively making it a
"hidden" parameter, as long as it's using a convention where the
caller cleans up the stack.
```

###### ↳ ↳ ↳ Re: They said it couldn't be done.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-27T17:28:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s9to2F4e4U1@mid.individual.net>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <hjkgkp02fff@news4.newsguy.com> <7s6lg4FavtU1@mid.individual.net> <hjn4rf21ce6@news4.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
…[45 more quoted lines elided]…
> caller cleans up the stack.

Thanks for the comments Michael. I've never used SEH and have put it on my 
"homework" list... :-)

(A chance'd be a fine thing... :-))

Pete.
```

#### ↳ Re: They said it couldn't be done.

- **From:** "john@wexfordpress.com" <john@wexfordpress.com>
- **Date:** 2010-02-13T06:21:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e4c53ff-7c49-4dc0-9c17-279b44164fb8@b18g2000vbl.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net>`

```
On Jan 24, 6:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Here's a couple of intellectual exercises if anyone is bored or wants to
> think about something else for a break...
…[73 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

In Open Office COBOL the choice between static and dynamic linking is
made at compile time
and not in the programs themselves.  The main program is compiled as
usual:
cobc -x -o main main.cob

The called program is compiled as a module:
cobc -m subr.cob

Next you take the subprogram and install it in a library of such:
cp subr.so /your/cobol/lib

Now you set a variable:
export COB_LIBRARY_PATH=/your/cobol/lib

Finally you run the program:
./main

The variable length buffer can be defined in LINKAGE SECTION as a data
item of
ANY LENGTH
and the picture clause must be defined as a single byte of 9, X or A.

OK, that was easy.


The above is taken from the Open Cobol Manual and the Open Cobol
Programmer's Guide. It should work on Linux and on Windows running
cygwin, a faux Linux environment.

Obviously these methods are not transportable to environments that
don't run Open Cobol.
But it does show the functional capability and user friendliness of
the OC compiler.

John Culleton
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-13T16:24:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hl6jog$n4v$1@reader2.panix.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7e4c53ff-7c49-4dc0-9c17-279b44164fb8@b18g2000vbl.googlegroups.com>`

```
In article <7e4c53ff-7c49-4dc0-9c17-279b44164fb8@b18g2000vbl.googlegroups.com>,
john@wexfordpress.com <john@wexfordpress.com> wrote:

[snip]

>In Open Office COBOL the choice between static and dynamic linking is
>made at compile time
>and not in the programs themselves.

If you are converting mainframe programs you might want to watch out for 
this; I seem to recall working with a bunch o' programs, some of which 
began with

 IDENTIFICATION DIVISION.

... and others with stuff like

 CBL NODYNAM,TEST(NONE),MAP,FASTSRT
 IDENTIFICATION DIVISION.

This was long ago... and my inquiry of 'what is the reason or benefit for 
these variations?' was met with 'They've always been that way so we just 
leave them alone.'

I have since learned that there might have been other reasons for having 
done things in this manner, ranging from optimising COBOL-F performance to 
someone's hoping to keep their job due to idiosyncratic knowledge... and 
more than those, as well!

DD
```

##### ↳ ↳ Re: They said it couldn't be done.

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-13T10:44:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80dabed6-7bf8-4e19-8f70-e92bf75f30b0@z10g2000prh.googlegroups.com>`
- **References:** `<7s2om7Fmu2U1@mid.individual.net> <7e4c53ff-7c49-4dc0-9c17-279b44164fb8@b18g2000vbl.googlegroups.com>`

```
On Feb 14, 3:21 am, "j...@wexfordpress.com" <j...@wexfordpress.com>
wrote:
> On Jan 24, 6:19 am, "Pete Dashwood"
>
…[80 more quoted lines elided]…
> In Open Office COBOL

OpenCobol.

> the choice between static and dynamic linking is
> made at compile time
> and not in the programs themselves.  

That is not entirely true, If the source code has:

    01  Program-Name       PIC X(20),
    ....
        MOVE something   TO Program-Name
        CALL Program-Name USING ....

Then the call will technically be dynamic regardless of what the
compiler was told.

> The main program is compiled as
> usual:
…[19 more quoted lines elided]…
> OK, that was easy.

Note that the standard (2002) and implementations such as Fujitsu only
allow ANY LENGTH in a method, not in a (sub)program.

> The above is taken from the Open Cobol Manual and the Open Cobol
> Programmer's Guide. It should work on Linux and on Windows running
…[7 more quoted lines elided]…
> John Culleton
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
