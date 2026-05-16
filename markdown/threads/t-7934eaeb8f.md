[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CreateProcess Win32API Part 2

_2 messages · 2 participants · 2000-06_

---

### CreateProcess Win32API Part 2

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000619110601.18141.00003609@ng-co1.aol.com>`

```
Good Morning,

By using the the CreateProcess or CBL_EXEC_RUN_UNIT I am able to run programs
like NOTEPAD and WORDPAD.  I have also been able to execute other third party
software.  But, the software that I am trying to execute seems to hang until I
exit the COBOL program.  I am trying to execute a program called "QUICKCAM.EXE"
from LogiTech.  This program provides an interface to a USB internet video
camera.  I execute the program with the CreateProcess API and receive back a
return code that indicates that the QUICKCAM.EXE has been started.  I get an
hour glass mouse pointer that last about one minute.  The system then stops at
the WaitforSingleObject API waiting for the termination of the "QUICKCAM"
program.  If I then stop animating my COBOL program the QUICKCAM software will
startup and appear on my screen.  I have tried using the application name
instead of the command line in the API but the results are the same.  Has
anyone had this type of problem before with this API ?

Thanks,
Bob Hennessey
```

#### ↳ Re: CreateProcess Win32API Part 2

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8iljvn$j9b$1@news.chatlink.com>`
- **References:** `<20000619110601.18141.00003609@ng-co1.aol.com>`

```
This sounds exactly like a problem I am having, though I start the
Workbench v4.x Animator ANIM2WG.EXE.  The splash screen for the animator
will hang for @30 seconds, then the animator will start.  This only
happens when I use the "WaitForSingleObject" API call to wait for
execution to finish.  If I just use the "CreateProcess" call by itself,
the splash screen displays for about 3 seconds and the animator starts
immediately.

I think it is an issue with animator...

TL


Bob7536 <bob7536@aol.com> wrote in message
news:20000619110601.18141.00003609@ng-co1.aol.com...
> Good Morning,
>
> By using the the CreateProcess or CBL_EXEC_RUN_UNIT I am able to run
programs
> like NOTEPAD and WORDPAD.  I have also been able to execute other
third party
> software.  But, the software that I am trying to execute seems to hang
until I
> exit the COBOL program.  I am trying to execute a program called
"QUICKCAM.EXE"
> from LogiTech.  This program provides an interface to a USB internet
video
> camera.  I execute the program with the CreateProcess API and receive
back a
> return code that indicates that the QUICKCAM.EXE has been started.  I
get an
> hour glass mouse pointer that last about one minute.  The system then
stops at
> the WaitforSingleObject API waiting for the termination of the
"QUICKCAM"
> program.  If I then stop animating my COBOL program the QUICKCAM
software will
> startup and appear on my screen.  I have tried using the application
name
> instead of the command line in the API but the results are the same.
Has
> anyone had this type of problem before with this API ?
>
> Thanks,
> Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
