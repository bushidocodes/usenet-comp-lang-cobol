[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Telenet Server

_8 messages · 4 participants · 2003-02_

---

### Telenet Server

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-11T12:12:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E495947.8090804@Sympatico.ca>`

```
Has anybody tried using Cobol through Telenet?  It seems to me that the 
old style character mode screens should work fine through a Telenet 
connection, but I know nothing about how the Cobol (or which Cobol, if 
any) would interface to the "communication port" at the server end.

Donald
```

#### ↳ Re: Telenet Server

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-12T06:41:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2bco8$5f0$1@aklobs.kc.net.nz>`
- **References:** `<3E495947.8090804@Sympatico.ca>`

```
Donald Tees wrote:

> Has anybody tried using Cobol through Telenet?  It seems to me that the
> old style character mode screens should work fine through a Telenet

It works fine, with X-Opwn or with text mode SP/2.  I use old 486 boxes 
with Floppy and NE2000 NIC booting under PocketLinux (from floppy-no HD) to 
give a network telnet terminal with 8 console sessions.

Telnet also works over VPNs to give private connection over the internet or 
via SSH.

> connection, but I know nothing about how the Cobol (or which Cobol, if
> any) would interface to the "communication port" at the server end.

Cobol does nothing, telnet deals with the grubby comms details.
```

##### ↳ ↳ Re: Telenet Server

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-11T15:05:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4981C5.6010106@Sympatico.ca>`
- **References:** `<3E495947.8090804@Sympatico.ca> <b2bco8$5f0$1@aklobs.kc.net.nz>`

```
Now that is interesting.  I use SP2 now, but have never really played 
with the character mode stuff.  In theory, then, I can take an old MS 
dos system, that uses console VT100 mode character I/O, and somehow 
automagically set it up to run under telent?

If I want to put something like an X-Opwn object on a web, page, does it 
simply shell out to the Cobol program on the server side?

Donald

Richard Plinston wrote:
> Donald Tees wrote:
> 
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Telenet Server

- **From:** "Rick S." <ricks123@hotpop.com>
- **Date:** 2003-02-11T19:53:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2bgqn$pjk$1@news-reader11.wanadoo.fr>`
- **References:** `<3E495947.8090804@Sympatico.ca>`

```

"Donald Tees" <Donald_Tees@Sympatico.ca> wrote

> Has anybody tried using Cobol through Telenet?  It seems to me that the
> old style character mode screens should work fine through a Telenet
> connection, but I know nothing about how the Cobol (or which Cobol, if
> any) would interface to the "communication port" at the server end.

I may have followed a different route than others, but during the last
10 years, all 5 of the IBM mainframe shops I seen, have been using "telnet"
to access the mainframe.

But I don't think it is regular telnet, but instead a special variant called
"tn3270". In fact, as far as I know, one cannot use the standard telnet
client that comes with Windows, or even with Linux for that matter.

I think one difference is 3270 screens are "asysncronous", and standard
telnet is a "syncronous" deal. That is to say, at least in the old days,
3270 terminals only sent data to the mainframe when enter, or one of
the PF keys, or PA1 or PA2 were pressed. The terminal and the
mainframe sent screen back and forth... but they rest of the time they
were "out of sync" (async).

But with regular "telnet" every keystroke is processed by the host
server computer. They are either "in sync", or busy trying to catch
up so they will be in sync.

But there is a special version of telnet called "tn3270" that works with
3270 screens.... that is, as far as I know, the usual way people
connect to mainframes now.
```

##### ↳ ↳ Re: Telenet Server

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-11T15:12:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E498344.60806@Sympatico.ca>`
- **References:** `<3E495947.8090804@Sympatico.ca> <b2bgqn$pjk$1@news-reader11.wanadoo.fr>`

```
Actually, I was thinking more of the old style programs that were used 
in the days of the Altos --- they essentially used VT-100 or ANSII 
serial terminal mode stuff.

What I am picturing in my head is a button on a web page that starts a 
cobol terminal mode program, and assigns an X*Y screen to it. The COBOL
program does some simple terminal mode I/O, and has the ability to 
"CLOSE" the screen window.

Donald

Rick S. wrote:
> "Donald Tees" <Donald_Tees@Sympatico.ca> wrote
> 
…[32 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Telenet Server

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-12T00:30:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302120030.17d29d77@posting.google.com>`
- **References:** `<3E495947.8090804@Sympatico.ca> <b2bgqn$pjk$1@news-reader11.wanadoo.fr>`

```
"Rick S." <ricks123@hotpop.com> wrote 

> I think one difference is 3270 screens are "asysncronous", and standard
> telnet is a "syncronous" deal. 

The other way around.

> That is to say, at least in the old days,
> 3270 terminals only sent data to the mainframe when enter, or one of
> the PF keys, or PA1 or PA2 were pressed. The terminal and the
> mainframe sent screen back and forth... 

Yes.

> but they rest of the time they were "out of sync" (async).

No.
 
> But with regular "telnet" every keystroke is processed by the host
> server computer. They are either "in sync", or busy trying to catch
> up so they will be in sync.

That's not why it is sync or async.
 
In synchronous transmition (chronous=clock) each character is
synchonised with a timer beat.  many characters are assembled together
into a block, a group of SYN characters (perhaps 30) are sent off so
that the two ends can synchronise their timers and then the sender
sends the characters with each starting on a timer beat.

With asynchronous each character is sent off separately without any
attempt at synchronising but the character has a start bit and 1 or
two stop bits added, the receiver has to be able to detect the start
bit and then take the next 8 bits as a data byte.
```

###### ↳ ↳ ↳ Re: Telenet Server

- **From:** "Rick S." <ricks123@hotpop.com>
- **Date:** 2003-02-12T22:06:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2ed0a$p2s$1@news-reader11.wanadoo.fr>`
- **References:** `<3E495947.8090804@Sympatico.ca> <b2bgqn$pjk$1@news-reader11.wanadoo.fr> <217e491a.0302120030.17d29d77@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message

> "Rick S." <ricks123@hotpop.com> wrote
>
…[3 more quoted lines elided]…
> The other way around.

Thanks for setting me straight. I'd rather have it be done here than in
a job interview, or face-to-face. :-)

Thanks, sincerely.
```

#### ↳ Re: Telenet Server

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2003-02-11T20:25:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x86dnd4A0JrIP9SjXTWc2Q@comcast.com>`
- **References:** `<3E495947.8090804@Sympatico.ca>`

```
Cobol doesn't need to know anything about telnet - it doesn't even need to
know it is running through a telnet server.

We run Unix-based Acucobol programs solely through a telnet client under
Windows.  Unix gives session a psuedo-tty, so it appears to the program that
it is running on a normal Unix tty device.

We also use a telnet server for Windows 2000 (called SLNet) and use that to
run the same Acucobol character screens off of a Windows 2000 server through
telnet clients.  Acucobol has an "alternate terminal manager" for its
Windows runtime that outputs to the screen in the same way a Unix runtime
would, using terminal escape codes to do cursor positioning, attributes,
etc.

"Donald Tees" <Donald_Tees@Sympatico.ca> wrote in message
news:3E495947.8090804@Sympatico.ca...
> Has anybody tried using Cobol through Telenet?  It seems to me that the
> old style character mode screens should work fine through a Telenet
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
