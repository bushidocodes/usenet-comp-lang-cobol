[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL and UNIX question

_5 messages · 4 participants · 1996-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL and UNIX question

- **From:** "lcor..." <ua-author-17086569@usenetarchives.gap>
- **Date:** 1996-05-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4mdcmr$r56@hopi.gate.net>`

```


We use MF COBOL on various UNIX platforms (all SVR4 flavors).
Our users are locked into our MF COBOL programs (they do not get
shell access). To read mail from COBOL, they type MAIL, F8 and
COBOL does a system call to run mailx. What would be nice is if
we could notify the users when they receive mail (rather than
they constantly checking or getting notified just when they log
on). However, I have no idea how to send a signal from the op sys
to COBOL when mail is received. We'd like to have something like
biff, but for COBOL.

Has anyone done something like this? If so, could you please give me
some indication as to how it's done or where I can get information?

Thanks.

- Laura Corriss


Laura Corriss  (lco··.@ga··e.net)
```

#### ↳ Re: MF COBOL and UNIX question

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1996-05-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a9d89e50ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4mdcmr$r56@hopi.gate.net>`
- **References:** `<4mdcmr$r56@hopi.gate.net>`

```

Laura,

I can't give you the coding specifics, but an idea would be to try to
use the users tty and echo something to their terminal.

You could write a shell program or C program that would monitor the
/usr/spool/mail directories. When someone got mail, you could
determine what /dev/tty they are using, and flash the word MAIL on the
lower right part of there screen or something. You could also use

tput bel > /dev/tty??

to have there terminal beep.

Hope this gives you some help or ideas.

Paul

lco··.@ga··e.net (Laura Corriss) wrote:


› We use MF COBOL on various UNIX platforms (all SVR4 flavors).
› Our users are locked into our MF COBOL programs (they do not get
…[6 more quoted lines elided]…
› biff, but for COBOL.
 
› Has anyone done something like this?  If so, could you please give me
› some indication as to how it's done or where I can get information?
 
› Thanks.
 
› - Laura Corriss
 
› -- 
 
› Laura Corriss  (lco··.@ga··e.net)
```

##### ↳ ↳ Re: MF COBOL and UNIX question

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-05-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a9d89e50ec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a9d89e50ec-p2@usenetarchives.gap>`
- **References:** `<4mdcmr$r56@hopi.gate.net> <gap-a9d89e50ec-p2@usenetarchives.gap>`

```

pdu··.@w··.com (DuuBeeWaa) wrote:
› Laura,
› 
…[10 more quoted lines elided]…
› to have there terminal beep.

You have to be a little bit careful when doing things like this, because if you
have two processes writing to the screen, then any screen handling package
which optimises screen output by keeping a memory map and only refreshing those
areas of the screen which have changed (like the one MF COBOL uses), will be
fooled by the extra output and will no longer operate properly (UNLESS the
second process can successfully restore the contents of the screen and place
the cursor back to where it found it).
The CALL "SYSTEM" facility in MF COBOL automatically adjusts for this (Note
that CALL "system" does not, as it binds directly to the OS system() call, and
we don't know it has happened).

Cheers, Kev.
```

#### ↳ Re: MF COBOL and UNIX question

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-05-03T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a9d89e50ec-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4mdcmr$r56@hopi.gate.net>`
- **References:** `<4mdcmr$r56@hopi.gate.net>`

```

lco··.@ga··e.net (Laura Corriss) wrote:
› 
› We use MF COBOL on various UNIX platforms (all SVR4 flavors).
› [snip]
› I have no idea how to send a signal from the op sys
› to COBOL when mail is received.
 
› Has anyone done something like this?  If so, could you please give me
› some indication as to how it's done or where I can get information?

Hi. Use the "cobpostsighandler" call to allow your code to catch signal.
Because the signal handler is going to be running as an interrupt, you have to
be VERY careful about what it actually does. For instance, allocating memory
will be extremely dangerous, as it might be the memory allocator that was
interrupted (and thus it's internal structures will not be in a sane state for
it to be reentered). For the same reason, it is extrement dangerous to call
COBOL within a signal handler or to write it in COBOL in the first place - the
COBOL RTS may have internal structures in a bad state when it was interrupted.

I'd suggest just setting a flag somewhere so that the main COBOL program can
check for it and put up a "mail waiting" message or something. The problem then
is to make sure the COBOL program wakes up to check the flag without coding a
tight system-unfriendly loop somewhere. Maybe just check for the flag each time
the user selects a menu option or something (or have a "Test for mail" menu
option ??).

If you have any problems with this, let me know.
```

#### ↳ Re: MF COBOL and UNIX question

- **From:** "king..." <ua-author-583169@usenetarchives.gap>
- **Date:** 1996-05-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a9d89e50ec-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4mdcmr$r56@hopi.gate.net>`
- **References:** `<4mdcmr$r56@hopi.gate.net>`

```

In article <4mdcmr$r.··.@hop··e.net>, lco··.@ga··e.net (Laura Corriss)
writes:

› Subject:	MF COBOL and UNIX question
› From:	lco··.@ga··e.net (Laura Corriss)
…[11 more quoted lines elided]…
› biff, but for COBOL.
I realize this isn't what you asked for, but I strongly recommend you give
up trying to incorporate this into your Cobol code and use one of the many
multi-terminal session packages available on Unix. We use a package
called CAI-Net and it operates on both PC's and dumb terminals over a
regular serial connection (or a network). CAI-Net reserves the top
(normally unused) status line on our PC or terminal and provides immediate
mail notification and access to our mail manager with a few keystrokes.
This is completely independent of our code. Another major benefit of this
environment is the ability to have different programs running in multiple
windows on a single workstation. Finally, we can send system spool files
to printers attached to the PC or dumb terminal with no program
modification and print streams are multiplexed with keyboard I/O so they
can occur concurrently. My users would walk out the door if they were
asked to work without these capabilities. Their web site is
http://www.cainc.com, although these capabilities are not described very
well and I have really described just a fraction of its feature set. I
have to admit, CAI-Net is a CPU hog and rather expensive, but well worth
the investment in our opinion. We also have successfully used a package
called FaceTerm with similar capabilities.

Dan Thomas
Kin··.@a··.com
Compuserve: 103514,2512
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
