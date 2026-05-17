[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol, HPUX, and crontab

_4 messages · 4 participants · 1997-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Cobol, HPUX, and crontab

- **From:** "john haver" <ua-author-17073455@usenetarchives.gap>
- **Date:** 1997-06-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1>`

```

We have a MF COBOL program that runs just fine under HP UX 9.x when run
from an interactive terminal session... but the same command will not work
when scheduled via a crontab entry.

It is receiving an RTS 191 error ADIS, terminal type not recognized.

Does anyone know how to run a MF COBOL program under CRON, and redirect the
output to a file instead having to run it interactively (what TERM setting
to use to make MF COBOL happy)?

Thanks in advance, John
```

#### ↳ Re: MicroFocus Cobol, HPUX, and crontab

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-06-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fcf8be6a1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1>`
- **References:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1>`

```

John Haver wrote:
› 
› We have a MF COBOL program that runs just fine under HP UX 9.x when run
…[7 more quoted lines elided]…
› to use to make MF COBOL happy)?

Hi John.

The thing about cron jobs is that they run under a very restricted
environment, and I suspect that TERM is not set up by default, or is
set to some very basic generic terminal type. You
would have to set it up explicitly (either in the cron script, or in
the shell script/program the cron script executes). Just set it to
a $TERM setting that works interactively. Of course, the resulting
file will only look good when viewed on the correct terminal type (and
it could be difficult to read if there is more than one screen of
output anyway).

I'm a bit confused as to why you are running a program which uses ADIS
as a cron job - certainly if it contains any ACCEPTs! If it contains
only DISPLAYs, you would be better off making them ANSI DISPLAYs
rather than ADIS DISPLAYs if possible (no $TERM neccessary, easy
redirection etc).

Cheers,
Kev.

PS. The reason you get the 191 error in the first place is that there
is a basic subset of terminfo capabilities that the COBOL RTS needs in
order to do any non-ANSI screen output. I don't have a full list to
hand, but they include things like clear-screen and a couple of cursor
movement sequences. If they are missing in the current TERM, then the
RTS will report error 191 as it doesn't have enough information to
control the screen.
```

#### ↳ Re: MicroFocus Cobol, HPUX, and crontab

- **From:** "sean moore" <ua-author-2359009@usenetarchives.gap>
- **Date:** 1997-06-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fcf8be6a1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1>`
- **References:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1>`

```

John Haver wrote:
› 
› We have a MF COBOL program that runs just fine under HP UX 9.x when run
…[3 more quoted lines elided]…
› Thanks in advance, John

Hi John,
This may or may not help, as I am not familiar with Unix or even know
what a crontab is.
But if your trying to run it from a scheduled state, I presume you are
refering to some type of batched Job Control Language.
If that is the case, then the problem you are describing sounds like
one I encountered some years ago.
That is, if the program is trying to ACCEPT or DISPLAY data from/to a
terminal it will never work unless a terminal is interactive to it.
So if that's what it's doing, you need to change the source code or
depending on the sophistication of your Job Control Language, you
may be able to include a line of JCL to direct the ACCEPT or DISPLAY
to a serial disk file. If its just DISPLAY you may be able to direct
it to a Printer, but that printer(or a print spool) must be available.
Also, if you don't have access to the source the terminal may be
assigned
(hard coded) in the program, but usually a programmer lets it default to
a terminal called 'Display' or 'Console'.
However. not knowing your JCL I couldn't tell you what to add to it.
But it would be something like $$ASSIGN DISPLAY = FILE-OUT or PRINTER1.
Anyway, I hope this helps.
Regards.
B.H. alias S.M.
```

##### ↳ ↳ Re: MicroFocus Cobol, HPUX, and crontab

- **From:** "bl..." <ua-author-17072051@usenetarchives.gap>
- **Date:** 1997-06-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fcf8be6a1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fcf8be6a1-p3@usenetarchives.gap>`
- **References:** `<01bc7ab5$279337c0$2439bdc7@command-ctr1> <gap-1fcf8be6a1-p3@usenetarchives.gap>`

```

Sean Moore wrote:

› John Haver wrote:
›› 
…[4 more quoted lines elided]…
›› Thanks in advance, John

We had a similar problem with RM-Cobol under UNIX. Look a redirecting
the standard input and/or output. Also, be aware that crontab does not
set any environmental variables, so you may want to create a shell
script that sets any environmental variables then calls your cobol
program.
Hope this helps.

Glenn Estes bl··.@ep··x.net * My opinions do not reflect those
Accounting Manager * of my boss - unless he happens
B Levy & Son * to be right!
Scranton, PA USA Sol III *
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
