[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VisOC and /SUBSYSTEM:CONSOLE

_3 messages · 2 participants · 2005-06_

---

### VisOC and /SUBSYSTEM:CONSOLE

- **From:** "jlcaverlyca@yahoo.ca" <jlcaverlyca@yahoo.ca>
- **Date:** 2005-06-28T03:58:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119956312.683120.21030@z14g2000cwz.googlegroups.com>`

```
Hi,
  I am using Micro Focus Visual Object COBOL Version 1.0.

  I am using the product to re-compile some of my Microsoft COBOL 4.5
dos programs to 32-bit console programs.

  Everything works okay, except for the final .EXE

  Instead of running in the current console, a new console is started.

  The way around this is to re-link the .EXE with the
/SUBSYSTEM:CONSOLE option from the command line.

  Is there any way to do this from the VisOC interface?

Thanks,

Joe
```

#### ↳ Re: VisOC and /SUBSYSTEM:CONSOLE

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2005-06-29T18:17:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9up0f$svk$1@hyperion.microfocus.com>`
- **References:** `<1119956312.683120.21030@z14g2000cwz.googlegroups.com>`

```

<jlcaverlyca@yahoo.ca> wrote in message 
news:1119956312.683120.21030@z14g2000cwz.googlegroups.com...
> Hi,
>  I am using Micro Focus Visual Object COBOL Version 1.0.
<snip>
>  The way around this is to re-link the .EXE with the
> /SUBSYSTEM:CONSOLE option from the command line.
>
>  Is there any way to do this from the VisOC interface?

Hi Joe,

Unfortunately I don't have a copy of VisOC available to answer your 
question, though I *suspect* there's an option within the Project Properties 
to specify whether it's a character-mode or graphical-mode executable 
(presumably within a 'Link' tab).

If you can't find such a property dialog within the IDE project properties, 
please post your question to the Micro Focus forum under 
http://www.cobolportal.com/ , and one of our SupportLine colleagues should 
be able to assist further.

SimonT.
```

##### ↳ ↳ Re: VisOC and /SUBSYSTEM:CONSOLE

- **From:** "jlcaverlyca@yahoo.ca" <jlcaverlyca@yahoo.ca>
- **Date:** 2005-06-29T15:39:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120084756.037541.245520@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<d9up0f$svk$1@hyperion.microfocus.com>`
- **References:** `<1119956312.683120.21030@z14g2000cwz.googlegroups.com> <d9up0f$svk$1@hyperion.microfocus.com>`

```
Hi,
  Thanks for the reply. I've discovered a new command in VisOC,
CBLLINK.EXE, which does what I want. Quite a nifty command, as it has
the smarts to know if your program is using any externals (ADIS for
example), and with the -t option, create a stand-alone executable that
links in the libraries so that your program doesn't need any external
support libraries. It also makes it a true 32-bit console .EXE that
doesn't open a new console window when executed, which solves my
problem.

  While I like the GUI interface for project management, I still prefer
the good ole' console, so I'm compiling and ANIMating in MF Cobol 4.5,
and when it comes time to create the final .EXE, I'm using CBLLINK.EXE.

  I'm quite impressed that I didn't have to change any of my old DOS
Cobol 4.5 source code files before making them into 32-bit console apps
with CBLLINK.EXE. It's the smoothest upgrade I've ever done.

Thanks,

Joe
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
