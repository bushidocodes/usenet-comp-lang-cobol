[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL <->Perl Interface...

_28 messages · 22 participants · 1996-01_

---

### COBOL <->Perl Interface...

- **From:** "khile t. klock" <ua-author-3435711@usenetarchives.gap>
- **Date:** 1996-01-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30EC297D.5579@wsadmin2.cv.hp.com>`

```
Howdy ho!

I got a rather interesting question I am trying to find the answer to.

We have a rather large software package running here that is written in COBOL. This program
as an overlaying user interface that is now written in C', creating an X-windows interface.

This software allows for user specified code to be input/compiled into certain points of it...

I've written a nice X-Type GUI interface for one of these user exits, written in perl5 w/Tk Exntentions.

Now the fun starts.. How to paste it all together.. I have information I need to compile C' code into
the COBOL, and have things work, but I really need to get the COBOL program variables/data into
the Perl program I've written.. I get this stuff into C with no problem.. So right now I'm thinking of
passing the stuff to a C' program via CALL "user_c" USING BLA-PARAMETER-LIST.
then having the C' code call perl to do it's stuff...

Is there a simply way to just pass data between perl and COBOL instead???

If Not... The question needs to be answered in the PERL groups... How can I access these variables
from PERL... Is there an easy way to simply access the C' .h data structures from perl with out the need
of C', or do I have the paste all three of these together...

Hope this makes sense....


Thanx'
Khile Klock
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Khile T. Klock                   |  klo··.@wsa··p.com
Software (CIM) Technician        |  klo··.@hpc··p.com
WorkStream Support               |  klo··.@hpc··p.com
Hewlett Packard                  |  klo··.@hot··t.org
InkJet Business Unit             |  hot··.@pro··s.com 
Corvallis, Oregon                |  (http://www.proaxis.com/~hotline)
---------------------------------+-----------------------------------
       Phone: (503) 715-1466            Pager: (503) 924-5575 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

#### ↳ Re: COBOL <->Perl Interface...

- **From:** "chris Mason" <ua-author-13442658@usenetarchives.gap>
- **Date:** 1996-01-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<30EC297D.5579@wsadmin2.cv.hp.com>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com>`

```
Someone asked about calling C and then perl. Could you call Perl
directly from COBOL? Does the linker/loader on unix support cross
language calls?

Try calling a perl function from COBOL. The mind boggles...

Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: COBOL <->Perl Interface...

- **From:** "tom Christiansen" <ua-author-13329161@usenetarchives.gap>
- **Date:** 1996-01-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<30EC297D.5579@wsadmin2.cv.hp.com>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com>`

```
In comp.lang.perl.misc, using X-Mailer: Mozilla 2.0b3 (X11; I; HP-UX
A.09.05 9000/715) "Khile T. Klock" writes:

[followups redirected]

:I got a rather interesting question I am trying to find the answer to.

:We have a rather large software package running here that is written in COBOL. This program as an overlaying user interface that is now written in C', creating an X-windows interface. This software allows for user specified code to be input/compiled into certain points of it... I've written a nice X-Type GUI interface for one of these user exits, written in perl5 w/Tk Exntentions. Now the fun starts.. How to paste it all together.. I have information I need to compile C' code into the COBOL, and have
things work, but I really need to get the COBOL program variables/data into the Perl program I've written.. I get this stuff into C with no problem.. So right now I'm thinking of passing the stuff to a C' program via CALL "user_c" USING BLA-PARAMETER-LIST. then having the C' code call perl to do it's stuff... Is there a simply way to just pass data between perl and COBOL instead??? If Not... The question needs to be answered in the PERL groups... How can I access these variables from PERL... Is there a
n easy way to simply access the C' .h data structures from perl with out the need of C', or do I have the paste all three of these together...

Lovely.

Someday I'm going to track down the nitwit at Netscape who thinks
infinite line lengths are nifty and box their ears for ever letting
people send out messages with more 80 characters per line. It's
not cool.

--tom
Tom Christiansen      Perl Consultant, Gamer, Hiker      tch··.@mox··l.com


Eschew polysyllabic glossolalia.
```

##### ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "klockk" <ua-author-31904520@usenetarchives.gap>
- **Date:** 1996-01-03T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p3@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap>`

```
Tom Christiansen wrote:
› 
› In comp.lang.perl.misc, using X-Mailer: Mozilla 2.0b3 (X11; I; HP-UX
…[9 more quoted lines elided]…
› --tom

That's nice.. The original message HAD every so many characters...
Makes me wonder what you are using for a reader?

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Khile T. Klock                   |  klo··k@wsa··p.com
Software (CIM) Technician        |  klo··k@hpc··p.com
WorkStream Support               |  klo··k@hpc··p.com
Hewlett Packard                  |  klo··k@hot··t.org
InkJet Business Unit             |  hot··e@pro··s.com 
Corvallis, Oregon                |  (http://www.proaxis.com/~hotline)
---------------------------------+-----------------------------------
       Phone: (503) 715-1466            Pager: (503) 924-5575 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "aa903" <ua-author-37149625@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p4@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p4@usenetarchives.gap>`

```
Khile T. Klock (klo··k@wsa··p.com) wrote:
: Tom Christiansen wrote:
: >
: > Someday I'm going to track down the nitwit at Netscape who thinks
: > infinite line lengths are nifty and box their ears for ever letting

: That's nice.. The original message HAD every so many characters...
: Makes me wonder what you are using for a reader?

I'm using TIN on a UNIX system (via a terminal emulator) and I
can only read the first 80 characters of each paragraph.

						Neil

Reply to: 710··3@com··e.com  or  aa··3@fre··m.org
Personal Home Page: http://www.dis.on.ca/~neil
```

##### ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "jevering" <ua-author-45857140@usenetarchives.gap>
- **Date:** 1996-01-03T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p3@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap>`

```
Tom Christiansen wrote:

› Someday I'm going to track down the nitwit at Netscape who thinks
› infinite line lengths are nifty and box their ears for ever letting
› people send out messages with more 80 characters per line.  It's
› not cool.

Hey! That's ME! What happens here is we cut the line at the width of the
window and we always bring up the window to be 72 columns wide. We made
a conscious decision to not save the window width because of this. We
allow people to stretch the window and make messages wider than 72
columns but do not encourage or harbor it... this is for those who want
to make some funky ascii table or something. Otherwise they shouldn't
be wider than 72 columns or so. It is actually other mailers such as MS
Exchange which send the infinite line length messages... This one should
be properly formatted... I am using the Netscape mailer.

Regards,
Jim

James Everingham 
Netscape Communications
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "bashley" <ua-author-9567024@usenetarchives.gap>
- **Date:** 1996-01-04T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p6@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap>`

```
I never saw the original post. The first copy I saw was a real mess and
started in several lines down from the top. The Netscape Guy's addendum
was properly formatted. For the record, I'm using tin.

Bev bas··y@cel··e.edu
*****************************************************************
"Let them eat shit."
-- Marcel Antoinette, Marie's little-known brother
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "amikkels" <ua-author-8214550@usenetarchives.gap>
- **Date:** 1996-01-04T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p6@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap>`

```
On Thu, 04 Jan 1996 15:06:27 -0800, James Everingham
wrote:

› Tom Christiansen wrote:
 
›› Someday I'm going to track down the nitwit at Netscape who thinks
›› infinite line lengths are nifty and box their ears for ever letting
›› people send out messages with more 80 characters per line.  It's
›› not cool.
 
› Hey! That's ME! What happens here is we cut the line at the width of the 
› window and we always bring up the window to be 72 columns wide.  We made 
…[6 more quoted lines elided]…
› be properly formatted... I am using the Netscape mailer.

Until I got your item, I thought "Good! At last Netscape has done
something right!).

Try looking at your message in a reader using a window about 65
characters wide. You have two options usually:-
lose the last 7 characters :-(
have every second line < 7 chars long which makes it hard to read.

Surely in this day and age it is the job of the READER to format the
message to fit in the current reading window, not the WRITER to make
assumptions about will be used to read it.

Who really still uses 80 character fixed font readers???


---------------------------------------------------------------
Allan Mikkelsen ami··s@mel··g.au
Melbourne PC User Group
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 4)_

- **From:** "arne" <ua-author-9384953@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p8@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p8@usenetarchives.gap>`

```
In article <30e··4@new··g.au>, ami··s@mel··g.au (Allan Mikkelsen) writes:
› Who really still uses 80 character fixed font readers???

More than you think !

Arne

Arne Vajh���j local DECNET: KO::ARNE
Computer Department PSI: PSI%23831001354030::ARNE
Southern Denmark Business School Internet: AR··E@KO.··S.DK
WWW URL: http://www.hhs.dk/~arne/arne.html
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 4)_

- **From:** "gary" <ua-author-20887107@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p8@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p8@usenetarchives.gap>`

```
ami··s@mel··g.au (Allan Mikkelsen) writes:
› Surely in this day and age it is the job of the READER to format the
› message to fit in the current reading window, not the WRITER to make
› assumptions about will be used to read it.

Be conservative in what you produce, liberal in what you accept.
In usenet circles, this means produce lines <80 characters long,
but be able to read lines of infinite size.

› Who really still uses 80 character fixed font readers???

Me, for one. The prettiness of the netscape news reader
can't compare with the power of nn.
http://www.cs.usyd.edu.au/~gary/
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "tbetz" <ua-author-9422366@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p6@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap>`

```
James Everingham wrote:
› 
› Tom Christiansen wrote:
…[7 more quoted lines elided]…
› window and we always bring up the window to be 72 columns wide. 

Okay, Jim. Just tell us... how does one know how many characters wide
the screen is (without typing a line and counting characters)? Also, you
are forgetting that many people (like me) have carefully-formatted
80-column-wide signature files, which, when Netscape imports them, are
badly-formatted in a 72-column editing window.

Unless you are prepared to put a ruler across the editing window marked in
characters, and which adjusts itself for the fixed-pitch font the user has
selected, Netscape should do what every other Usenet editing tool does:
provide a user-configurable (and user-defeatable) word wrap for the text
editor defined by the number the user places into a field.

And it should bring up the editing window in whatever width it was previously
used in, or at the width defined by the word-wrap value, whichever the user
selects.

-- Tom Betz ----------- <http://www.cloud9.net/~tbetz/> ---- (914) 375-1510 --
tb··z@clo··9.net | Now that the living outnumber the dead, | tb··z@pa··x.com
------------------+ I am one of many. -- Laurie Anderson +-----------------
- The whole world is a beautiful place to play music. -- Jerry Garcia, 1969 -
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 4)_

- **From:** "jef" <ua-author-37832100@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p11@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p11@usenetarchives.gap>`

```
Tom Betz wrote:

› James Everingham wrote:
›› 
…[8 more quoted lines elided]…
›› window and we always bring up the window to be 72 columns wide. 
 
› Okay, Jim.  Just tell us... how does one know how many characters wide
› the screen is (without typing a line and counting characters)? 

Windows will tell you exactly the width, in pxels, of each character
of a fixed-width font, and the average for a proportional font. From
there it's pretty easy to define a window a given number of characters
in width. Netscape does a pretty damn good job of it.

› Also, you
› are forgetting that many people (like me) have carefully-formatted 
› 80-column-wide signature files, which, when Netscape imports them, are 
› badly-formatted in a 72-column editing window.

And there are those of us who think your grandiose signature files can
go to hell.

› Unless you are prepared to put a ruler across the editing window marked in 
› characters, and which adjusts itself for the fixed-pitch font the user has 
› selected,
 
› Netscape doesn't have to, Windows provides it.
 
› Netscape should do what every other Usenet editing tool does:  
› provide a user-configurable (and user-defeatable) word wrap for the text 
› editor defined by the number the user places into a field.
 
› And it should bring up the editing window in whatever width it was previously 
› used in, or at the width defined by the word-wrap value, whichever the user 
› selects.

Agreed.

Jim Fuller
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 4)_

- **From:** "jwz" <ua-author-3689680@usenetarchives.gap>
- **Date:** 1996-01-05T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p11@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p11@usenetarchives.gap>`

```
It is a requirement that, in the message composition window, the user not be
required to hit return at the end of every line. Macintosh and Windows users
are used to system-standard editors which do not require this. To most
people, the notion that one would have to hit return at the end of every line
is ridiculous: it is just Not How It Is Done on these platforms.

It is also a requirement that, by the time the message is sent out over SMTP
or NNTP, it is not sent with CRLF only at the end of the paragraph: the fact
of life on Usenet is that it is a short-line medium. Lines should generally
be less than 80 columns wide, with explicit line breaks, unless there is a
specific need to exceed that (like a table.)

So, the Netscape composition window takes the following approach: let the
platform-specific text editor do display-time word-wrapping. If a paragraph
is typed, and then a word is inserted in the middle of that paragraph, the
rest of the paragraph should re-wrap. Hitting return is a "hard" line break
that will never be auto-filled.

This makes the editor behave like all the editors users are already used to.

However, when the time comes to deliver the message, Netscape takes all of
the "implicit" line breaks (where words have wrapped because they reached the
right edge of the window) and turns them into "explicit" line breaks. In
this way, the message which is sent over SMTP/NNTP is formatted in such a way
that a recipient using a fixed-width non-auto-filling display device will see
exactly what the author has typed, with line breaks in the same places.

There are several problems with this.

The first is that, when quoting messages using the conventional USENET style
(to set off each quoted line by preceeding it with "> ") the line lengths
tend to get longer with each subsequent quote. It is common, then, for lines
to exceed the width of the window. When seen in a word wrapping display,
they will often have an unattractive (some would say unreadable) long-short-
long-short wrapping style, like

> All work and no play makes Jack a dull boy. All work and no play makes
Jack a
> dull boy. All work and no play makes Jack a dull boy. All work and no
play
> makes Jack a dull boy. All work and no play makes Jack a dull boy.
All
> work and no play makes Jack a dull boy.

It would be horrible were Netscape to send out messages that looked like
this. Therefore, there is an additional hack in the formatting code which is
that we never wrap lines which have ">" as their first character. If the
line begins with ">", it is assumed to be a "quoted" line, and its implicit
line breaks are not converted to explicit line breaks.

This is a violation of the otherwise-WYSIWYG nature of the editor, in that
the person composing the message will see alternating long-short lines, but
the person reading the message will simply see some lines which are "long"
compared to the others.

Now, the next problem with this is that we wrap lines based on where the
system's built-in text editor has chosen to do display-time word-wrapping.
This, in turn, is based on the size of the window.

We create all composition windows 72 characters wide, on all platforms.
(The hard requirement is that the windows be 79 characters wide or less,
but it is traditional for the "fill column" to be set to 72 to allow room
for followups to quote this message several times before the lines begin
to exceed 80 characters.)

The problem is this: if the user drags the window wider, we will then wrap at
the current width of the window, which may well be excessively wide.

One solution to this, which we rejected, would be to disallow the window from
being made wider than 79 columns. That would be bad, because there are
situations when it is necessary and appropriate to send messages with long
lines: when formatting a table, for example.

Another solution would be to pop up a dialog box warning the user that their
window is too wide (probably just before the message is sent) which offered
to shrink it and allow the paragraphs to refill. We may yet do this, but
rejected it initially as too intrusive and annoying.

Another attractive and often-suggested solution is to cause the editor to
always do word-wrapping somewhere before 79 columns, regardless of the width
of the window. However, this assumes a much more sophisticated editor: one
with enough composition and formatting commands that the width of each
paragraph could be controlled individually. There is not a built-in editor
that is that powerful on all the platforms on which we must ship, which would
mean we'd have to write it ourself. But more importantly, it would then no
longer be "The Builtin Editor", meaning it would no longer be the editor (and
have the behavior) that the user expects.

A simpler version of this hypothetical "more sophisticated" editor would be
one which inserted "hard" newlines when the user typed a word which passed
the right edge. In this editor, typing a paragraph and then inserting a word
in the middle of it would leave the paragraph with ragged margins. It would
then need to provide a "refill paragraph" command to discard and recompute
the line breaks of that paragraph. That's a fine idea, but the builtin
editors don't work this way, and don't provide such a command. Regardless of
how hard it would be to make them behave that way (and it might be hard, or
it might be easy) the fact remains that we would have changed the behavior of
the editor in a rather fundamental way, way which would surprise users
already accustomed to it from its use in other applications.

Other alternatives are to provide a "ruler" at the top of the window, or to
draw a vertical "line of death" behind the text at 72 (or 79) columns,
reminding the user that they should avoid having lines longer than that.
We tried the "line of death" approach for a while, but most people didn't
understand what it was: they assumed it was some kind of redisplay glitch,
and reported it as a bug!

Also, both of these approaches assume the user notices the subtle graphical
information we're showing them, and that they care/understand that <80
columns is a Good Thing (this isn't obvious at all to novice users.)

Note also, that all of these problems/solutions apply only to the case of
generating messages of type text/plain, which is all that the Netscape mail
composition window can directly do at this time. If someday the composition
window allows generation of something other than text/plain, for example,
text/html or text/enriched, then the generated messages would contain
formatting information, and these problems all go away. (Well, get traded
for an orthogonal set of problems. :-))

Jamie Zawinski    j··@net··e.com   http://www.netscape.com/people/jwz/
``A signature isn't a return address, it is the ASCII equivalent of a
  black velvet clown painting; it's a rectangle of carets surrounding
  a quote from a literary giant of weeniedom like Heinlein or Dr. Who.''
                                                         -- Chris Maeda
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 5)_

- **From:** "amikkels" <ua-author-8214550@usenetarchives.gap>
- **Date:** 1996-01-06T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p13@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p11@usenetarchives.gap> <gap-eec6a017a9-p13@usenetarchives.gap>`

```
On Sat, 06 Jan 1996 22:20:06 -0800, Jamie Zawinski
wrote:

[snip]
› However, when the time comes to deliver the message, Netscape takes all of
› the "implicit" line breaks (where words have wrapped because they reached the
…[3 more quoted lines elided]…
› exactly what the author has typed, with line breaks in the same places.

Your excellent description would be a little more correct if you used
"a recipient using a fixed width non-auto-filling display device THAT
CAN DISPLAY AT LEAST 72 (or 79 or 80) CHARACTERS PER LINE ..."

Not all displays, fixed or windowed, are 80 columns wide.

› There are several problems with this.
 
› The first is that, when quoting messages using the conventional USENET style
› (to set off each quoted line by preceeding it with "> ") the line lengths
…[3 more quoted lines elided]…
› long-short wrapping style, like
 
›  > All work and no play makes Jack a dull boy.  All work and no play makes
›  Jack a
…[4 more quoted lines elided]…
›  > work and no play makes Jack a dull boy.  
 
› It would be horrible were Netscape to send out messages that looked like
› this. 

But you do!! This is EXACTLY how your original message appears on my
display! I read my news while having to "keep an eye on" another
process running in the background. I thus have only about 60 columns
available to display your message and have several unpalatable
options:-

. lose everything beyond column 60 :-(
. try and make sense of a revolting jagged mess
. reduce the font so that more characters will fit - not very
satisfactory for someone with poor eyesight.

I realise the problems (I have designed and written systems for years)
but just want to point out that satisfying the 80 character
traditionalists will result in poor formatting for the other users.

Surely the formatting should be done in the displaying system - not
the writing system. If a system cannot wrap lines at column 79 (or
any reader chosen margin), then get a new reader.


---------------------------------------------------------------
Allan Mikkelsen ami··s@mel··g.au
Melbourne PC User Group
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 6)_

- **From:** "jwz" <ua-author-3689680@usenetarchives.gap>
- **Date:** 1996-01-07T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p14@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p11@usenetarchives.gap> <gap-eec6a017a9-p13@usenetarchives.gap> <gap-eec6a017a9-p14@usenetarchives.gap>`

```
Allan Mikkelsen wrote:
›
› Not all displays, fixed or windowed, are 80 columns wide.

That's true, but the vast majority are. People will complain if you
post lines longer than 79. People will generally *not* complain if you
post lines longer than 72. Whether right or wrong, this is the current
state of the world.

› But you do!!  This is EXACTLY how your original message appears on my
› display!  I read my news while having to "keep an eye on" another
› process running in the background.  I thus have only about 60 columns
› available to display your message and have several unpalatable
› options:-

However, you *have* those options. The thing I was talking about would
have removed from you even those options.

› Surely the formatting should be done in the displaying system - not
› the writing system.

That would be nice. If you want that to happen, compose all of your
messages in such a way that they get delivered with a content-type of
text/html, or text/enriched, or any of the plethora of other formatting
options that are available.

But good luck getting the whole world to switch at once!

All I'm saying is that trying to change the current status-quo
interpretation of text/plain is not going to work; and the status quo
says that text/plain means <80 columns with explicit line breaks.

I agree that text/plain is not the best format to use. But *if* you're
going to use it, you should follow the conventions of the last two
decades to avoid alienating a huge portion of your readers
unnecessarily.

Jamie Zawinski    j··@net··e.com   http://www.netscape.com/people/jwz/
``A signature isn't a return address, it is the ASCII equivalent of a
  black velvet clown painting; it's a rectangle of carets surrounding
  a quote from a literary giant of weeniedom like Heinlein or Dr. Who.''
                                                         -- Chris Maeda
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "jef" <ua-author-29532082@usenetarchives.gap>
- **Date:** 1996-01-06T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p6@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap>`

```
James Everingham wrote:
› =
 
› Tom Christiansen wrote:
› =
 
›› Someday I'm going to track down the nitwit at Netscape who thinks
›› infinite line lengths are nifty and box their ears for ever letting
›› people send out messages with more 80 characters per line.  It's
›› not cool.
› =
 
› Hey! That's ME! What happens here is we cut the line at the width of the
› window and we always bring up the window to be 72 columns wide.  We made
…[7 more quoted lines elided]…
›  =

This part of the mailer works great, Jim, once one knows what =

it's doing with the quotes. =


While you're here, ... With the 32-bit version on NT and Win95, =

when I set it to bring up both the browser and the newsreader at =

start-up, the news window comes up covering the whole damn =

screen (almost). It sets itself to leave a small sliver of =

screen space on the left-hand side, top, and bottom, and extends =

all the way across the screen. No amount of re-sizing, saving, =

regeditting, or otherwise will affect it.

Set to launch only the browser, then accessing the newsreader =

through the "Window" menu item brings up the news window in the =

saved size, as desired.

On NT, the problem is severe. On Win95, it comes up bigger, but =

not covering the entire screen. This may be because I have a =

smaller screen on the Win95 machine.

This is new in =DF5.

I just wanted to make your day.

Thanks,
Jim Fuller
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 4)_

- **From:** "braden" <ua-author-3917957@usenetarchives.gap>
- **Date:** 1996-01-08T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p16@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap>`

```
"James E. Fuller" wrote:


› This part of the mailer works great, Jim, once one knows what =
 
› it's doing with the quotes.  =
 
 
› While you're here, ... With the 32-bit version on NT and Win95, =
 
› when I set it to bring up both the browser and the newsreader at =
 
› start-up, the news window comes up covering the whole damn =
 
› screen (almost).  It sets itself to leave a small sliver of =
 
› screen space on the left-hand side, top, and bottom, and extends =
 
› all the way across the screen.  No amount of re-sizing, saving, =
 
› regeditting, or otherwise will affect it.
 
› Set to launch only the browser, then accessing the newsreader =
 
› through the "Window" menu item brings up the news window in the =
 
› saved size, as desired.
 
› On NT, the problem is severe.  On Win95, it comes up bigger, but =
 
› not covering the entire screen.  This may be because I have a =
 
› smaller screen on the Win95 machine.
 
› This is new in =DF5.
 
› I just wanted to make your day.

One might also mention that it's putting an "=" at the end of each
line and adding an unnecessary linefeed. Or was that implied?

Braden
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 5)_

- **From:** "jef" <ua-author-29532082@usenetarchives.gap>
- **Date:** 1996-01-09T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p17@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap>`

```
Braden N. McDaniel wrote:
› 
› "James E. Fuller"  wrote:
…[8 more quoted lines elided]…
›  
It was unnoticed. I have absolutely no clue as to how that
happened. Have you ever seen it before?

I don't even remember if that message was posted with Free Agent
or Netscape.

Jim Fuller
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 6)_

- **From:** "knutsp" <ua-author-45862736@usenetarchives.gap>
- **Date:** 1996-01-09T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p18@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap> <gap-eec6a017a9-p18@usenetarchives.gap>`

```
"James E. Fuller" wrote:

› Braden N. McDaniel wrote:
›› One might also mention that it's putting an "=" at the end of each
…[3 more quoted lines elided]…
› happened.  Have you ever seen it before?
 
› I don't even remember if that message was posted with Free Agent 
› or Netscape.

It was posted with Netscape 2.0���5 using MIME "quoted printable". One
could see that from the header fields and the way your "beta" (���)
character was encoded. Turn on "Allow 8 bit" and this will not happen.

When is somebody going to tell Netscape there is different standards for
mail and news? In the Norwegian groups the use of "quoted printable" is
a pain in teh ass. The only ones using this for news is the one posting
articles with Netscape Navigator. QP belongs in email and allows for 7
bit transfer if necessary. It sholud never be used in news as this
medium handles 8 bit characters. The Netscape programmers has not done
their homework in this matter and the result is a lot of fuzz about this
especially in non-English newgroups.

Knut Sparhell, Norway
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 7)_

- **From:** "jwz" <ua-author-3689680@usenetarchives.gap>
- **Date:** 1996-01-14T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p19@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap> <gap-eec6a017a9-p18@usenetarchives.gap> <gap-eec6a017a9-p19@usenetarchives.gap>`

```
Braden N. McDaniel wrote:
› 
›› It was posted with Netscape 2.0�5 using MIME "quoted printable".  One
…[6 more quoted lines elided]…
› Braden

Excuse me? How is this a hole? You turned on the preferences option
which told Netscape that it should follow the MIME standard, and not
send unencoded 8-bit characters. And it did exactly what you told it
to do.

Jamie Zawinski    j··@net··e.com   http://www.netscape.com/people/jwz/
``A signature isn't a return address, it is the ASCII equivalent of a
  black velvet clown painting; it's a rectangle of carets surrounding
  a quote from a literary giant of weeniedom like Heinlein or Dr. Who.''
                                                         -- Chris Maeda
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 8)_

- **From:** "jef" <ua-author-29532082@usenetarchives.gap>
- **Date:** 1996-01-15T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p20@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap> <gap-eec6a017a9-p18@usenetarchives.gap> <gap-eec6a017a9-p19@usenetarchives.gap> <gap-eec6a017a9-p20@usenetarchives.gap>`

```
James E. Fuller wrote:
› 
› "James E. Fuller"  wrote:
…[57 more quoted lines elided]…
› Now, what changed? 
Ah Ha! When an article contains straight ASCII characters, it
gets sent with charset=us-ascii, content-transfer-encoding:
7bit. Use an extended character, like the Beta character
(alt-225) and the article gets sent with charset=iso-8859-1,
content-transfer-encoding: quoted-printable, which causes
problems.
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 8)_

- **From:** "knutsp" <ua-author-45862736@usenetarchives.gap>
- **Date:** 1996-01-15T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p20@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap> <gap-eec6a017a9-p18@usenetarchives.gap> <gap-eec6a017a9-p19@usenetarchives.gap> <gap-eec6a017a9-p20@usenetarchives.gap>`

```
Jamie Zawinski wrote:

› Braden N. McDaniel wrote:
›› 
…[7 more quoted lines elided]…
›› Braden
 
› Excuse me?  How is this a hole?  You turned on the preferences option
› which told Netscape that it should follow the MIME standard, and not
› send unencoded 8-bit characters.  And it did exactly what you told it
› to do.

Netscape Navigator should not do this on news, only email. The "hole"
is that it does not know the difference in standards for those two
services. Only email shold be affected by this setting.

Knut Sparhell, Norway
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

_(reply depth: 9)_

- **From:** "onn" <ua-author-45918362@usenetarchives.gap>
- **Date:** 1996-01-17T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p22@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p6@usenetarchives.gap> <gap-eec6a017a9-p16@usenetarchives.gap> <gap-eec6a017a9-p17@usenetarchives.gap> <gap-eec6a017a9-p18@usenetarchives.gap> <gap-eec6a017a9-p19@usenetarchives.gap> <gap-eec6a017a9-p20@usenetarchives.gap> <gap-eec6a017a9-p22@usenetarchives.gap>`

```
Knut Sparhell wrote:

› Netscape Navigator should not do this on news, only email.  The "hole"
› is that it does not know the difference in standards for those two
…[3 more quoted lines elided]…
› Knut Sparhell, Norway

I agree that there are two separate standards for news and mail messages,
but one should borrow from the other as necessary to progress into the
present day. MIME headers in news messages are happening now. It is
arguably better to send a multipart news posting using the MIME standard
than splitting a message up and trying to encode the part information in
the subject line, as is common practice (and has been for over 10 years).

The MIME standard, when applied to news postings, can only enhance those
postings (given that you have a compliant reader. It can look like crap
of you don't.)

Brian.
Brian A. Onn (o··@t··.com)	\|/	voice: (415) 833-2549
Teknekron Software Systems	 @	  fax: (415) 328-5524
Palo Alto, CA			/|\	pager: (800) SKY-PAGE PIN 1203596
```

##### ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "russell..." <ua-author-505839@usenetarchives.gap>
- **Date:** 1996-01-07T19:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p3@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap>`

```
tch··.@mox··l.com (Tom Christiansen) writes:

› Someday I'm going to track down the nitwit at Netscape who thinks
› infinite line lengths are nifty and box their ears for ever letting
› people send out messages with more 80 characters per line.  It's 
› not cool.

and, like I've mentioned to Tom in mail, it's so trivial to handle them
when displaying the article and wrapping them when following up that
they're not worth complaining about.

if you write a newsreader, you might as well handle this. it's just not
that tough (which just makes it look silly to complain about as much
as Tom does, but he gives away Perl help for free, so what are you
going to do. hmm... who has source for the newsreader he uses?).

who writes text-browsing software with just a simple `fgets()' loop?
Rus··.@loc··B.ORG  Shad 86c
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "tm..." <ua-author-6258440@usenetarchives.gap>
- **Date:** 1996-01-16T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p24@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p24@usenetarchives.gap>`

```
In article <960··.@loc··B.ORG>,
Russell Schulz wrote:
› tch··.@mox··l.com (Tom Christiansen) writes:
›› Someday I'm going to track down the nitwit at Netscape who thinks
…[4 more quoted lines elided]…
› they're not worth complaining about.

Sometimes people post code to the Net. Sometimes the language is
sensitive to line endings (e.g. FORTRAN; comments in C++ and Perl;
formats in Perl, and comp.lang.perl.misc *is* one of the newsgroups
here). I don't want the system to insert line breaks on its own.

                             Tim McDaniel
                        Reply-To: tm··.@c··.com
                  (mcd··.@d··.net is the backup.)
              Never use mcd··.@mcd··x.us.
```

##### ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "lw..." <ua-author-510606@usenetarchives.gap>
- **Date:** 1996-01-16T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p3@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap>`

```
In article <960··.@loc··b.org>,
Russell Schulz wrote:
: tch··.@mox··l.com (Tom Christiansen) writes:
:
: > Someday I'm going to track down the nitwit at Netscape who thinks
: > infinite line lengths are nifty and box their ears for ever letting
: > people send out messages with more 80 characters per line. It's
: > not cool.
:
: and, like I've mentioned to Tom in mail, it's so trivial to handle them
: when displaying the article and wrapping them when following up that
: they're not worth complaining about.
:
: if you write a newsreader, you might as well handle this. it's just not
: that tough (which just makes it look silly to complain about as much
: as Tom does, but he gives away Perl help for free, so what are you
: going to do. hmm... who has source for the newsreader he uses?).
:
: who writes text-browsing software with just a simple `fgets()' loop?

I do.

Larry Wall
lw··.@se··s.com
```

###### ↳ ↳ ↳ Re: COBOL <->Perl Interface...

- **From:** "sbb" <ua-author-36027955@usenetarchives.gap>
- **Date:** 1996-01-20T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-eec6a017a9-p26@usenetarchives.gap>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com> <gap-eec6a017a9-p3@usenetarchives.gap> <gap-eec6a017a9-p26@usenetarchives.gap>`

```
One quick and dirty way to get wrapping in Netscape is just to make a
table with one row and one column. The user can then adjust the browser if
the text is wrapped where it shouldn't be.

Steve Bronstein



In article <199··4@net··s.com>, lw··l@se··s.com wrote:

› In article <960108.230130.4c6.rnr.w164w_-_··@loc··b.org>,
› Russell Schulz  wrote:
…[21 more quoted lines elided]…
› lw··l@se··s.com
```

#### ↳ Re: COBOL <->Perl Interface...

- **From:** "jadestar" <ua-author-2168612@usenetarchives.gap>
- **Date:** 1996-01-04T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eec6a017a9-p28@usenetarchives.gap>`
- **In-Reply-To:** `<30EC297D.5579@wsadmin2.cv.hp.com>`
- **References:** `<30EC297D.5579@wsadmin2.cv.hp.com>`

```
In days of yore (Thu, 04 Jan 1996 11:24:45 -0800)
Khile T. Klock (klo··k@wsa··p.com) proclaimed:

:Howdy ho!

:I got a rather interesting question I am trying to find the answer to.

:We have a rather large software package running here that is written
: in COBOL. This program
:as an overlaying user interface that is now written in C', creating an
: X-windows interface.

You want to control an interactive Unix program with a
script. That spells: 'expect'

         />	           JaDe     |     Star                 <\
        /<                         \|/                          >\
 *[/////|:::====================- --*-- -=====================:::|\\\\\]*
        \<                         /|\                          >/ 
         \>    jad··r@net··m.com  |  sta··e@net··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
