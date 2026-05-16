[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Disappearing data on screen

_9 messages · 3 participants · 2005-06_

---

### Disappearing data on screen

- **From:** "Colonel_Buck" <bkeith@alumni.utexas.net>
- **Date:** 2005-06-05T15:57:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com>`

```
How do you keep input data from disappearing from the screen from one
display to
the next? I'm using Fujitsu COBOL 5.0. Thanks.
```

#### ↳ Re: Disappearing data on screen

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-06T13:33:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ghnffFcb28sU1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com>`

```

"Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
news:1118012259.831407.79890@g43g2000cwa.googlegroups.com...
> How do you keep input data from disappearing from the screen from one
> display to
> the next? I'm using Fujitsu COBOL 5.0. Thanks.
>
Code 'USING' instead of 'FROM' .

Pete
```

##### ↳ ↳ Re: Disappearing data on screen

- **From:** "Colonel_Buck" <bkeith@alumni.utexas.net>
- **Date:** 2005-06-06T13:18:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118089118.034063.125400@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<3ghnffFcb28sU1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net>`

```


Pete Dashwood wrote:
> "Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
> news:1118012259.831407.79890@g43g2000cwa.googlegroups.com...
…[6 more quoted lines elided]…
> Pete
```

##### ↳ ↳ Re: Disappearing data on screen

- **From:** "Colonel_Buck" <bkeith@alumni.utexas.net>
- **Date:** 2005-06-06T13:19:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118089192.398974.77920@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3ghnffFcb28sU1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net>`

```


Pete Dashwood wrote:
> "Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
> news:1118012259.831407.79890@g43g2000cwa.googlegroups.com...
…[6 more quoted lines elided]…
> Pete
Works perfect! Thanks. I wonder why the TO and the FROM don't work
together???
```

###### ↳ ↳ ↳ Re: Disappearing data on screen

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-07T10:33:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gk19uFcf02fU1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net> <1118089192.398974.77920@g44g2000cwa.googlegroups.com>`

```

"Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
news:1118089192.398974.77920@g44g2000cwa.googlegroups.com...
>
>
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Disappearing data on screen

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-07T10:57:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gk2nhFcs507U1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net> <1118089192.398974.77920@g44g2000cwa.googlegroups.com>`

```
Sorry for previous blank post...finger trouble.

See below...

"Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
news:1118089192.398974.77920@g44g2000cwa.googlegroups.com...
>
>
…[12 more quoted lines elided]…
>
You have missed the point of these constructs. (I don't blame you because
the concepts are not even mentioned in the manual).

TO allows you to protect fields so that they become 'read only'.  It is
intended to emulate devices in mainframe environments that have attributes
to do this (like IBM 3270).

Having decided that your field will be 'read only', it would be a
contradiction to then place output data in it. So FROM cannot work with TO.

In the same way, an output only field can be defined with FROM, and, in the
same way it will be incompatible with TO.(If the field is defined for output
only, you cannot accept input from it.)

USING allows both input and output of the field, as you have seen.

SUMMARY:
You may find it helpful to think of these constructs in the following way:

TO = input only. Will not be refreshed after data is collected from it.
FROM = output only. Will not allow input of data in the same field. The
field is refreshed when redisplayed.
USING = input/output. Allows data collection and can be updated. The field
is refreshed with its current contents on subsequent displays.

ADVICE: (Opinion that is arguable, but I have no intention of arguing it;
make up your own mind.)

Screen sections in COBOL, particularly in Client/Server environments, are an
obsolete cop out for people who can't deal with event driven GUI
programming, and are hanging desperately to the command line interface
because 'we've always done it that way'. COBOL programmers tend to think in
terms of procedural programming and are used to controlling the process, so
ACCEPT and DISPLAY is simple and familiar.

Get into event driven programming; it is fun and satisfying.

You have a superb environment for developing  'quick build' GUI
applications: PowerCOBOL. (It comes with Fujitsu NetCOBOL version 5).

Do the PowerCOBOL tutorial. You won't be sorry.

Pete.
```

###### ↳ ↳ ↳ Re: Disappearing data on screen

_(reply depth: 4)_

- **From:** "Colonel_Buck" <bkeith@alumni.utexas.net>
- **Date:** 2005-06-10T21:06:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118462797.976806.84850@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3gk2nhFcs507U1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net> <1118089192.398974.77920@g44g2000cwa.googlegroups.com> <3gk2nhFcs507U1@individual.net>`

```
OK Pete, you shamed me into looking at the PowerCOBOL Getting Started
book. The problem is that all of my experience with business
applications have dealt with only 4 different data types; character,
numeric, date and time.

 I just don't see the up-side of a real-life business application
having bunny rabbits hop across the screen. Don't get me wrong, it's
nice that it can be done, but I don't see where it might fit in with
applications that I'm designing, building and testing.

Have you any examples of a PowerCOBOL application written for a bank,
or insurance company, or hospital, etc.....?

If I could take a look at one of those, I could see how one is put
together, how the forms work and feed each other, how the data flows,
logic, etc.....

Thanks, blk...
```

###### ↳ ↳ ↳ Re: Disappearing data on screen

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-11T09:10:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8ensa$hi3$1@panix5.panix.com>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <1118089192.398974.77920@g44g2000cwa.googlegroups.com> <3gk2nhFcs507U1@individual.net> <1118462797.976806.84850@g14g2000cwa.googlegroups.com>`

```
In article <1118462797.976806.84850@g14g2000cwa.googlegroups.com>,
Colonel_Buck <bkeith@alumni.utexas.net> wrote:

[snip]

> I just don't see the up-side of a real-life business application
>having bunny rabbits hop across the screen. Don't get me wrong, it's
>nice that it can be done, but I don't see where it might fit in with
>applications that I'm designing, building and testing.

Hmmmmm... reminds me, long ago, of a memo I was forced to write comparing 
an IBM mainframe and an IBM PC - this must have been in the mid-late 1980s 
or so - that had, as its target readership, a fellow who was known for 
blustering 'A mainframe can do anything a PC can do!'

It contained the immortal line of 'Mainframe and PCs are rather different 
in their processing focus and application capabilities; this might be why 
one rarely sees a flying-toaster screensaver on a 3270 terminal.'

DD
```

###### ↳ ↳ ↳ Re: Disappearing data on screen

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-12T10:41:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3h17ljFep2n9U1@individual.net>`
- **References:** `<1118012259.831407.79890@g43g2000cwa.googlegroups.com> <3ghnffFcb28sU1@individual.net> <1118089192.398974.77920@g44g2000cwa.googlegroups.com> <3gk2nhFcs507U1@individual.net> <1118462797.976806.84850@g14g2000cwa.googlegroups.com>`

```

"Colonel_Buck" <bkeith@alumni.utexas.net> wrote in message
news:1118462797.976806.84850@g14g2000cwa.googlegroups.com...
> OK Pete, you shamed me into looking at the PowerCOBOL Getting Started
> book. The problem is that all of my experience with business
> applications have dealt with only 4 different data types; character,
> numeric, date and time.
>

There is no shame in seeking knowledge.

PowerCOBOL uses the same data types you are used to; it simply adds some
more. The COM terminology has a different name for them, but that is
transparent to the PowerCOBOL programmer. (for example... I2 in COM is Pic
s9(4) comp in COBOL. They both represent an integer stored in two bytes, as
binary. But none of that is of concern to the novice.)

The COM representations are designed to work across all platforms; a simple
move in COBOL will translate these fields into whatever picture they are
compatible with.  Does it matter whether you think of a data type as
'CURRENCY' or PIC s9(14)v9(4)? Either way it represents the same thing. The
only difference is that CURRENCY will be recognised across many platforms,
PIC s9(14)v9(4) is only meaningful to COBOL.

>  I just don't see the up-side of a real-life business application
> having bunny rabbits hop across the screen.

Personally, I have never written a powerCOBOL application (or any other
kind) where bunny rabbits hop across the screen. However, it could be done
easily by using the animation component in PowerCOBOL. I think this comment
reveals more of an attitude about using GUI than it does about seriously
extending your knowledge. Many of us resist change and once we have a
successful way of doing things, it requires some energy to keep expanding
the horizons.  It is sometimes better to proactively seek knowledge that can
be used for, as yet, unrecognised solutions, than it is to wait until
something requiring this knowledge is dropped on us with a deadline that
means frantically trying to acquire the knowledge under pressure. It's a bit
like scouting the road ahead; there may be forks in it that you have no
intention of taking, but circumstances change and you find yourself
travelling a road you thought you never would.

Of course, if you don't want to go, then don't get in the car... I'm a firm
believer that people should do what they feel comfortable with (it doesn't
stop me prodding occasionally :-))

> Don't get me wrong, it's
> nice that it can be done, but I don't see where it might fit in with
…[4 more quoted lines elided]…
>
No. But I do have PowerCOBOL applications that are running in businesses and
one of these is connected with health care.

> If I could take a look at one of those, I could see how one is put
> together, how the forms work and feed each other, how the data flows,
> logic, etc.....

If you do the tutorial and build yourself a form with event driven processes
on it, I'll gladly do as you ask. Send me your test project and I'll respond
with a real life application. (I don't have time to indulge you unless you
are serious...). Realise that these applications can have many forms
associated with them, can require RDB design that is every bit as demanding
as in a mainframe environment, and will run in business environments where
they get hammered every day. PowerCOBOL is extremely stable and I have never
had an application crash in live because of bugs in the run time or other
Fujitsu flaws. (I HAVE had problems with advanced application development
where things did not work as documented, and error diagnostics were
meaningless. I also found the support abysmally lacking on this particular
occasion. Nevertheless, we survived and got the application implemented. It
put years on me and I worked day and night to do it. I have had similar
experiences in mainframe environments where it isn't the software or support
that is at fault, but the user department. Nothing is perfect.  The
documentation from release 6 improved out of sight. It is experiences like
this that make me advocate continuing to learn; you don't need the
additional stress of a learning curve when you are under pressure.

Wahever you decide to do, I wish you the best.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
