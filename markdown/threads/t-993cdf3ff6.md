[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# API & Cobol

_22 messages · 9 participants · 2003-02_

---

### API & Cobol

- **From:** "pty0" <xxx@clix.pt>
- **Date:** 2003-02-21T14:30:31
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt>`

```
It is possible to know how many users are to use an exe . If Yes how??

Many Thanks
```

#### ↳ Re: API & Cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-21T18:25:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt>`

```
"pty0" <xxx@clix.pt> wrote in message
news:nKq5a.3571$EM4.2033677@newsserver.ip.pt...
> It is possible to know how many users are to use an exe . If Yes how??

Not through 'native' COBOL there isn't.

But a COBOL program can account for it by maintaining a "user count"
external file.
```

##### ↳ ↳ Re: API & Cobol

- **From:** "pty0" <xxx@clix.pt>
- **Date:** 2003-02-21T18:30:10
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fu5a.3583$Ac1.2175044@newsserver.ip.pt>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com>`

```
I want to know  exactly in a net how many users are  accede a certain
program at the same time (EXE) .
The "exe" be in a server that is shared for the several users .
With API programing.

Thanks







"Michael Mattias" <michael.mattias@gte.net> escreveu na mensagem
news:7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com...
> "pty0" <xxx@clix.pt> wrote in message
> news:nKq5a.3571$EM4.2033677@newsserver.ip.pt...
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-02-21T14:43:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35vcl$2g1$1@nntp2-cm.news.eni.net>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <1fu5a.3583$Ac1.2175044@newsserver.ip.pt>`

```
See if you can use the EnumWindows API call and it's associated callback...

kenmullins
newnan ga USA


"pty0" <xxx@clix.pt> wrote in message
news:1fu5a.3583$Ac1.2175044@newsserver.ip.pt...
> I want to know  exactly in a net how many users are  accede a certain
> program at the same time (EXE) .
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-21T22:11:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hux5a.15176$UF6.1586255@newssrv26.news.prodigy.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <1fu5a.3583$Ac1.2175044@newsserver.ip.pt>`

```
"pty0" <xxx@clix.pt> wrote in message
news:1fu5a.3583$Ac1.2175044@newsserver.ip.pt...
> I want to know  exactly in a net how many users are  accede a certain
> program at the same time (EXE) .
> The "exe" be in a server that is shared for the several users .
> With API programing.

Windows systems?

AFAIK the ONLY way to do this is to code something into the server program
to keep track.  And for that, there are only about umpty-nine different ways
to do it, each perfectly valid and reasonable.

Maybe there is some kind of intrinsic utility or language element in the
.NET family, since crossing CPU boundaries is what .NET is all about. But
the standard Windows API does not have anything which can go out and query
how many users are running program "X" (unless you run an interrogation on
each CPU in the network and report it back to the server - which brings us
right back to where we started: you have to code "something" in the server
to do this. Maybe a disk file, maybe a memory-mapped file, maybe a semaphore
if you want to control the user count, lots of other ways.

Enumwindows (a suggestion you received) is only valid within a single CPU..
which brings us back to the above..you'd have to run EnumWindows on each CPU
on the network and have that enum report back somewhere - presumably the
server.

One last thought... maybe your network software has an API which keeps track
of this. Check there.

If that doesn't pan out and you need someone to design and write this for
your server, I'd be happy to offer a proposal.
```

##### ↳ ↳ Re: API & Cobol

- **From:** "Steve" <Steven_31@aol.com>
- **Date:** 2003-02-21T19:45:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ilv5a.186458$SD6.9913@sccrnsc03>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com>`

```
I have tried that too and an abend does not allow the file to be
updated/deleted and you can think that the program is still open

for example - on program start I create a file called "users.dat" - on exit
I remove the file to show not in use but if computer crashes the file is
still there - tricking me into thinking the program is still running


"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com...
> "pty0" <xxx@clix.pt> wrote in message
> news:nKq5a.3571$EM4.2033677@newsserver.ip.pt...
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-21T16:01:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302211601.7a601db5@posting.google.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <Ilv5a.186458$SD6.9913@sccrnsc03>`

```
"Steve" <Steven_31@aol.com> wrote

> I have tried that too and an abend does not allow the file to be
> updated/deleted and you can think that the program is still open
…[3 more quoted lines elided]…
> still there - tricking me into thinking the program is still running

With a reasonable operating system you can get each copy of the
program to open a single isam file on the server, create a unique
record there and then read it with lock.  At end of run delete record
and close.

If the program crashes or otherwise stops then the operating system
removes the lock.  The count would thus be, not the number of records,
but the number that are still locked, any unlocked record can be
deleted.

However, I don't think that Windows does this, record locks may
survive after the process has crashed.
```

###### ↳ ↳ ↳ Re: API & Cobol

_(reply depth: 4)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-02-21T18:36:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b36gn107h@enews1.newsguy.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <Ilv5a.186458$SD6.9913@sccrnsc03> <217e491a.0302211601.7a601db5@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0302211601.7a601db5@posting.google.com...
> "Steve" <Steven_31@aol.com> wrote
>
> > I have tried that too and an abend does not allow the file
to be
> > updated/deleted and you can think that the program is still
open
> >
> > for example - on program start I create a file called
"users.dat" - on exit
> > I remove the file to show not in use but if computer
crashes the file is
> > still there - tricking me into thinking the program is
still running
>
> With a reasonable operating system you can get each copy of
the
> program to open a single isam file on the server, create a
unique
> record there and then read it with lock.  At end of run
delete record
> and close.
>
> If the program crashes or otherwise stops then the operating
system
> removes the lock.  The count would thus be, not the number of
records,
> but the number that are still locked, any unlocked record can
be
> deleted.
>
> However, I don't think that Windows does this, record locks
may
> survive after the process has crashed.

File locks will be dropped, but I don't know about record
locks.  Wouldn't that be the domain of the database engine?
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-21T18:18:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Io6dnVe2kKe9X8ujXTWchA@giganews.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <Ilv5a.186458$SD6.9913@sccrnsc03>`

```

"Steve" <Steven_31@aol.com> wrote in message
news:Ilv5a.186458$SD6.9913@sccrnsc03...
> I have tried that too and an abend does not allow the file to be
> updated/deleted and you can think that the program is still open
>
> for example - on program start I create a file called "users.dat" - on
exit
> I remove the file to show not in use but if computer crashes the file is
> still there - tricking me into thinking the program is still running

Create the file every 'x' interval.

When it's time to check, if the time between now and the last time the file
was created is greater than 'x', the program responsible for creating the
file has crashed.
```

###### ↳ ↳ ↳ Re: API & Cobol

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-22T14:34:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b36k4a$99a$1@aklobs.kc.net.nz>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7au5a.15064$UF6.1559973@newssrv26.news.prodigy.com> <Ilv5a.186458$SD6.9913@sccrnsc03> <Io6dnVe2kKe9X8ujXTWchA@giganews.com>`

```
JerryMouse wrote:

>
> Create the file every 'x' interval.
…[3 more quoted lines elided]…
> the file has crashed.

That relies on the program actually being in a position to be able to do 
that within the end of the last interval 'x' and some allowance 'y'.

With a batch program, for example, this would be relatively easy because 
code could be put into the processing cycle to check whether the time is 
between 'x' and 'x+y'.

An interactive program may be waiting for user input and no code will 
execute until the user hits a key and the focus is on that program.  Even 
then it would be an onerous task to build the check into every possible 
part of the program that may be active.

It would be necessary to build in a timer interrupt routine and have the OS 
activate the program whenever the timer interval specified expired. This 
would require that it be written to, say, be a real Windows program so that 
the API and callbacks can be used.  It would also be necessary to ensure 
that the filehandling system is reentrant as the timer may expire during 
the program a file access.
```

#### ↳ Re: API & Cobol

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-21T18:07:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wfy5a.6238$hv3.580291@news20.bellglobal.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt>`

```
There are more questions here, only one of them being: is your exe ran from
the server or from individual workstations?

If it's from the server, maybe you can create a little app that you can
start as a service on your server to track the number of yourprogram.exe
that run at a certain time.  This app would have a "howManyUsers" entry
point/method that would return the required info.

If it's from the workstation, try taping into your service and call/invoke
the "addUser" entry point/method.

Good luck!
Calin, TORONTO


"pty0" <xxx@clix.pt> wrote in message
news:nKq5a.3571$EM4.2033677@newsserver.ip.pt...
> It is possible to know how many users are to use an exe . If Yes how??
>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: API & Cobol

- **From:** "pty0" <xxx@clix.pt>
- **Date:** 2003-02-24T09:56:22
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r%l6a.2954$kj1.1099808@newsserver.ip.pt>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <wfy5a.6238$hv3.580291@news20.bellglobal.com>`

```
But if PC crash?
I think exist an API functions to control this.

thanks


"Calin @ Work" <dontemailme@work.com> escreveu na mensagem
news:wfy5a.6238$hv3.580291@news20.bellglobal.com...
> There are more questions here, only one of them being: is your exe ran
from
> the server or from individual workstations?
>
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-24T10:00:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Aoq6a.1585$kf7.241772@news20.bellglobal.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <wfy5a.6238$hv3.580291@news20.bellglobal.com> <r%l6a.2954$kj1.1099808@newsserver.ip.pt>`

```
1. Update the users table at regular intervals.  If the user doesn't call
the service to update itself in the table, that user is dead.

2. I have no idea about an API that would allow you to see how many people
double-clicked an exe.

But again, I've been proved wrong before...

Calin, TORONTO


"pty0" <xxx@clix.pt> wrote in message
news:r%l6a.2954$kj1.1099808@newsserver.ip.pt...
> But if PC crash?
> I think exist an API functions to control this.
…[15 more quoted lines elided]…
> > If it's from the workstation, try taping into your service and
call/invoke
> > the "addUser" entry point/method.
> >
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: API & Cobol

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-24T17:01:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g8-cnbsPUrgNOcejXTWckA@giganews.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <wfy5a.6238$hv3.580291@news20.bellglobal.com> <r%l6a.2954$kj1.1099808@newsserver.ip.pt> <Aoq6a.1585$kf7.241772@news20.bellglobal.com>`

```

"Calin @ Work" <dontemailme@work.com> wrote in message
news:Aoq6a.1585$kf7.241772@news20.bellglobal.com...
> 1. Update the users table at regular intervals.  If the user doesn't call
> the service to update itself in the table, that user is dead.
…[5 more quoted lines elided]…
>

If you 'have no idea,' but might be proved wrong.....

Wait a minute while I flowchart this.....

Move along. There's nothing here to see.
```

###### ↳ ↳ ↳ Re: API & Cobol

_(reply depth: 5)_

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-24T18:19:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VIx6a.1866$kf7.317039@news20.bellglobal.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <wfy5a.6238$hv3.580291@news20.bellglobal.com> <r%l6a.2954$kj1.1099808@newsserver.ip.pt> <Aoq6a.1585$kf7.241772@news20.bellglobal.com> <g8-cnbsPUrgNOcejXTWckA@giganews.com>`

```
Common, show me the flowchart... Please? Please? Pretty please?

Calin, TORONTO


"JerryMouse" <nospam@bisusa.com> wrote in message
news:g8-cnbsPUrgNOcejXTWckA@giganews.com...
>
> "Calin @ Work" <dontemailme@work.com> wrote in message
> news:Aoq6a.1585$kf7.241772@news20.bellglobal.com...
> > 1. Update the users table at regular intervals.  If the user doesn't
call
> > the service to update itself in the table, that user is dead.
> >
> > 2. I have no idea about an API that would allow you to see how many
people
> > double-clicked an exe.
> >
…[9 more quoted lines elided]…
>
```

#### ↳ API & Cobol

- **From:** Gisle Forseth <GForseth@acucorp.com>
- **Date:** 2003-02-25T04:39:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7BDF3C5E711686498AC6685001541ECE25FDFE@arthur.acucorp.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt>`

```
> It is possible to know how many users are to use an exe . 
> If Yes how??

I have got the understanding that you are looking into this subject with
Windows as host. In which case there is an article of how to use the
Windows API to achieve this information from ACUCOBOL-GT. 

Obviously, the article and the related source examples has the angle of
ACUCOBOL-GT, I do believe however, that it should be possible to
translate this to other COBOLs with not too much effort.

Please take a look at:

	http://www.acucorp.com/company/newsletter

Choose:

	2002 Issue 3 - Cobol And The Need For Interoperability 
		(Adobe pfd file)

Look up the article: "Do You Speak Windows" on page 10.

This is the artcle.

To get to see the code, go to:

	http://www.acucorp.com/support/public/sample_programs/index.php

In the Combo Box, select "Programs Featured in Acucorp News"

Eventually get the zip archive "speaking.zip"
```

##### ↳ ↳ Re: API & Cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-25T15:17:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5OL6a.834$PK3.82549@newssrv26.news.prodigy.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7BDF3C5E711686498AC6685001541ECE25FDFE@arthur.acucorp.com>`

```
"Gisle Forseth" <GForseth@acucorp.com> wrote in message
news:7BDF3C5E711686498AC6685001541ECE25FDFE@arthur.acucorp.com...
> > It is possible to know how many users are to use an exe .
> > If Yes how??
…[15 more quoted lines elided]…
>

THANK YOU.

That "NetFileEnum" API looks like the ticket, and lead me to the whole
WinAPI "Network Management" functions in my copy of the PSDK.

Damn, now I have to give this thing a try....
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** "pty0" <xxx@clix.pt>
- **Date:** 2003-02-25T15:03:53
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JBL6a.3028$551.1074264@newsserver.ip.pt>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <7BDF3C5E711686498AC6685001541ECE25FDFE@arthur.acucorp.com> <5OL6a.834$PK3.82549@newssrv26.news.prodigy.com>`

```
I think i can do this with NetFileEnum and/or  NetFileGetInfo.
But my knowledge in programming API Cobol  are not many in this case Fujitsu
Power Cobol ...
Somebody could put here in the group how to use these functions ?

Thanks


"Michael Mattias" <michael.mattias@gte.net> escreveu na mensagem
news:5OL6a.834$PK3.82549@newssrv26.news.prodigy.com...
> "Gisle Forseth" <GForseth@acucorp.com> wrote in message
> news:7BDF3C5E711686498AC6685001541ECE25FDFE@arthur.acucorp.com...
…[34 more quoted lines elided]…
>
```

#### ↳ Re: API & Cobol

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-25T08:45:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302250845.730a089b@posting.google.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt>`

```
"pty0" <xxx@clix.pt> wrote in message news:<nKq5a.3571$EM4.2033677@newsserver.ip.pt>...
> It is possible to know how many users are to use an exe . If Yes how??
> 
> Many Thanks

Look at the process APIs.  One of the peices of information you can
recover is the image name.  Count the instances and you are in
business.

FWIW, I know you can do this on the WindowsNT family of OSes, I'm not
sure about the Windows9x family.
```

##### ↳ ↳ Re: API & Cobol

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-02-25T14:18:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3gj2k019de@enews1.newsguy.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <dcedb8d0.0302250845.730a089b@posting.google.com>`

```
> > It is possible to know how many users are to use an exe .
If Yes how??

> Look at the process APIs.  One of the peices of information
you can
> recover is the image name.  Count the instances and you are
in
> business.

This will only count the processes running on one machine,
though.
```

##### ↳ ↳ Re: API & Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-25T16:01:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302251601.5dcc41af@posting.google.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <dcedb8d0.0302250845.730a089b@posting.google.com>`

```
jzitzelb@tsys.com (Joe Zitzelberger) wrote 

> > It is possible to know how many users are to use an exe . If Yes how??
> 
…[5 more quoted lines elided]…
> sure about the Windows9x family.

Does this work over a network link ?  I think that he would have a
server holding the .EXE and several client machines.  How will the
server know how many of those client machines are running that .EXE ?
```

###### ↳ ↳ ↳ Re: API & Cobol

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-26T06:46:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302260646.5f1d5574@posting.google.com>`
- **References:** `<nKq5a.3571$EM4.2033677@newsserver.ip.pt> <dcedb8d0.0302250845.730a089b@posting.google.com> <217e491a.0302251601.5dcc41af@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0302251601.5dcc41af@posting.google.com>...
> jzitzelb@tsys.com (Joe Zitzelberger) wrote 
> 
…[11 more quoted lines elided]…
> server know how many of those client machines are running that .EXE ?

That gets very dependant upon it being a hydra setup, or executing on
client machine off of server dasd.  I don't have enough details.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
