[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# okay, what now?

_5 messages · 2 participants · 1998-10_

---

### okay, what now?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vjqmh$j1d$1@news.igs.net>`

```
I have a rather strange problem that I have been fiddling
with for half a day, and I was wondering if anybody can point
me in a new direction.  It is Fujitsu Cobol, Version 4

I need to update a screen, plain screen section type of data,
every ten seconds or so.  The application will run in the
background, so to speak, and present an airport style
schedule ... the data being referenced constantly for work
in other windows.

The approach I decided to use was to write a stub in
power Cobol with a single timer on a form. When the timer
times out, I call a subroutine that is a Cobol program
with a screen section.  On the first pass, it displays the
background, then the data, as well as a flag saying that
it has been there. It then exits. Ten seconds later, it is
called again, sees it is not the first pass, updates the
screen, etc.  All works perfectly, and exactly as I require.

Until I want to stop it.  Now, the main form is
not visible, only the "screen" of the subprogram.  If I click
on its "stop" tab, I get a windows illegal reference. It then
stops. It stops quite gracefully.  However, I could do
without the "this program has produced an illegal reference,
please call your software vendor" message.  The only way
that I have been able to make it stop correctly is to make
the form visible, and have a stop button on it.  The "stop"
control on the screen causes an error, and it appears
that I cannot turn it off(either error or control).  Oh yes,
if I put an "accept" statement into the subroutine, then
it appears that I can stop it.  Of course, if I do that, then
it no longer works.

Any ideas?  About the only thing I can think of at this stage
is to turn it around backwards ... make the current subroutine
into the main program, and attempt to write a power Cobol
subroutine that is a timer.
```

#### ↳ Re: okay, what now?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-KgviNyQ3gUqE@Dwight_Miller.iix.com>`
- **References:** `<6vjqmh$j1d$1@news.igs.net>`

```
On Fri, 9 Oct 1998 02:10:14, "Donald Tees" <donald@willmack.com> 
wrote:

 
> Any ideas?  About the only thing I can think of at this stage
> is to turn it around backwards ... make the current subroutine
…[3 more quoted lines elided]…
> 

I know Fujitsu V3 does not support it, but what about V4? - The Accept
with TIMEOUT that MicroFocus has.  

Optionally you could write your own timer loop - or call the "Sleep" 
api function that has been discussed here in some detail.
```

##### ↳ ↳ Re: okay, what now?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vlg3n$4n5$1@news.igs.net>`
- **References:** `<6vjqmh$j1d$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-KgviNyQ3gUqE@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...

>I know Fujitsu V3 does not support it, but what about V4? - The Accept
>with TIMEOUT that MicroFocus has.

As far as I know, they do not have it.  Of course, you never know
with Fujitsu ... I'll give it a try.  That timeout would solve a lot of
problems.  I am somewhat worried, actually, about the lack of
exception handling under Fujitsu.  The "stop" button at the upper
right hand corner is another that worries me.  It seems to be
the equivalent of a power switch ... like press here and destroy
this system by aborting without closing files.  As far as I can tell,
there is absolutely no way to disable or trap it.


>Optionally you could write your own timer loop - or call the "Sleep"
>api function that has been discussed here in some detail.
>
I don't want the loop; I need this to be as low a priority as I can
get. I am also not too worried about data harm, as the files are
all opened in read only mode.  I may just have to fall back on the
sleep API, though the timer function as a subroutine should
be the same thing.  I am finding the incompatibilities between
the power Cobol and the Cobol97 rather frustrating, to tell the
truth.  You do not expect to have conversion problems between
what is supposedly two variations of the same compiler, yet
intermixing Fujitsu regular Cobol and Fujitsu power Cobol is
proving to be a huge pain in the ass.

I hope that in the next version they can decide what a line
of source code looks like. The line number/tab idiocy is enough
to drive one to drink.  It seems to be their major design problem.
```

###### ↳ ↳ ↳ Re: okay, what now?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-yu1HKs3WzzcF@Dwight_Miller.iix.com>`
- **References:** `<6vjqmh$j1d$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-KgviNyQ3gUqE@Dwight_Miller.iix.com> <6vlg3n$4n5$1@news.igs.net>`

```
On Fri, 9 Oct 1998 17:22:01, "Donald Tees" <donald@willmack.com> 
wrote:

---- snipped a bunch-o-stuff ----
 
> I hope that in the next version they can decide what a line
> of source code looks like. The line number/tab idiocy is enough
> to drive one to drink.  It seems to be their major design problem.
> 

I'll have to confess to not having these problems.  When I jumped to 
Fujitsu, I was already using a GUI interface with Realia COBOL - Since
I use SP2 and it supports both compilers, the move was virtually 
painless.  I had to convert some of the realia specific stuff I was 
using for file I-O, and a few calls used to read the directory 
structure, but the CBL calls handled that.  I am not done yet - but I 
know I CAN do it.  By using the GUI overall I avoid the problem of the
text mode window and the X close button that terminates the 
application.  Wish I could help you with that.  

I think your problems with Power COBOL vs COBOL 97 may be related to 
the OO syntax in Power COBOL - although I thought the same compiler 
was under the hood.  Interesting.  

Looks like the Sleep API call is your best answer.
```

###### ↳ ↳ ↳ Re: okay, what now?

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vtlch$8ja$1@news.igs.net>`
- **References:** `<6vjqmh$j1d$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-KgviNyQ3gUqE@Dwight_Miller.iix.com> <6vlg3n$4n5$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-yu1HKs3WzzcF@Dwight_Miller.iix.com>`

```
>I think your problems with Power COBOL vs COBOL 97 may be related to
>the OO syntax in Power COBOL - although I thought the same compiler
>was under the hood.  Interesting.


    Actually, I think they are the same compiler.  I think what is
happening is that the project manager, which actually writes the
PowerCobol code, is setting a whole bunch of compiler options
differently, and then setting the code up in very specific ways
so that it will work.

>Looks like the Sleep API call is your best answer.

Though I have a post from Fujitsu saying the same thing, I get
a link error every time I try to use it. I am still trying to find out
what library or linkage options are required to make it work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
