[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Scrolling banners?

_3 messages · 1 participant · 1999-09_

---

### Scrolling banners?

- **From:** "Robert Annandale" <REMOVE SPACES rob _ a @ unipharm . com>
- **Date:** 1999-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d69221$0$17811@fountain.mindlink.net>`

```
Greetings,

I am using AcuCOBOL 4.2 on a Windows NT client.
My data is on a UNIX file server and the client and filesever interact via
AcuServer.

I have an application that checks a file every 5 seconds for record content.
If there is a record it displays the record to all the users of the system.
The users are expected to 'take' the record from the file and process it.

I want to make some changes though, I'd like to use a scrolling banner
that scrolls the record found from the very right most column of the
window to the very left most column of the screen.
Take a stock ticker for example.

Currently the routine that checks for record content and displays it
is a threaded routine from the main application thread.
This thread runs and checks for a record whilst allowing users to interact
with the main thread.

I can get the scrolling to work using a PERFORM TEST and PERFORM VARYING
routine that decreases the column size by 1 until it equals 2, but the speed
at which
the label scrolls by is lightening fast.
A call to C$SLEEP seems like the only way to do this... and I not too crazy
about sleeps.
Does anyone have an algorithm or suggestions on how to to do this without
slowing
down the performance of my application or interfering with thread operation?

Regards,

----------------------------------------------------------------------------
----
Robert Annandale

Please remove spaces and 'NO SPAM' from address to reply.
All replies will be appreciated.  Replies to newsgroup will be appreciated
more.
```

#### ↳ Re: Scrolling banners?

- **From:** "Robert Annandale" <REMOVE SPACES rob _ a @ unipharm . com>
- **Date:** 1999-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d6ae03$0$24629@fountain.mindlink.net>`
- **References:** `<37d69221$0$17811@fountain.mindlink.net>`

```
Okay I've found a way to do this, I can even allow the user to set different
scrolling speeds... I did the following.

This is still unpolished...

       77  Ws-Column              Pic 99v99.
       77  Ws-Speed               Pic Sv99 Value -.02.

           Perform Varying Ws-Column From 47.00 By Ws-Speed
                   Until Ws-Column = 2
                   Display Main-LA-80-Screen
           End-Perform.

If anyone has a different or better way, I'd love to hear from you.

Regards,

RBA.

> Greetings,
>
…[4 more quoted lines elided]…
> I have an application that checks a file every 5 seconds for record
content.
> If there is a record it displays the record to all the users of the
system.
> The users are expected to 'take' the record from the file and process it.
>
…[11 more quoted lines elided]…
> routine that decreases the column size by 1 until it equals 2, but the
speed
> at which
> the label scrolls by is lightening fast.
> A call to C$SLEEP seems like the only way to do this... and I not too
crazy
> about sleeps.
> Does anyone have an algorithm or suggestions on how to to do this without
> slowing
> down the performance of my application or interfering with thread
operation?
>
> Regards,
>
> --------------------------------------------------------------------------
```

##### ↳ ↳ Re: Scrolling banners?

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7r6h7g$ge4$2@aklobs.kc.net.nz>`
- **References:** `<37d69221$0$17811@fountain.mindlink.net> <37d6ae03$0$24629@fountain.mindlink.net>`

```
Robert Annandale <REMOVE SPACES rob _ a @ unipharm . com> wrote:
:> A call to C$SLEEP seems like the only way to do this... and I not too
: crazy
:> about sleeps.

I bet the other users are not too crazy about you then.
The point about doing a 'sleep' is that it releases the
CPU resource so that other processes, or other users on
a multiuser system, can have their program run.

If you program in such a way that it uses all the CPU it can
get hold of to do trivial tasks then this will detract from
all other processes including servers and print spoolers or
even network responders.

While it can be determined an effective rate of scrolling on
one machine by experimentation this will vary for different
machines.  Using a 'sleep' function should give a stepping
rate that is effective for all machines.


A
that one machine 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
