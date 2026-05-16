[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus COBOL and WIN2000

_8 messages · 5 participants · 2000-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus COBOL and WIN2000

- **From:** "Rich Cullen" <rich@sparksit.com>
- **Date:** 2000-09-11T13:13:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pilpv$cg4@dispatch.concentric.net>`

```
We have an application written in MicroFocus COBOL that we are trying to run
on a WIN2000 server system.

From workstations, we can run the application fine with the files on the
server.  When we try to run the application on the server, we get the
message "COBOL run time library not installed - file not found."  Our
application developer is not any help.  They essentially say, "We don't do
windows; run it on NetWare."

We need to be able to run the application on WIN2000 in order to use Windows
Terminal Server for a remote office.

Is there a simple fix for this problem?  We know very little about COBOL.

Thanks for any help.

Rich Cullen
```

#### ↳ Re: MicroFocus COBOL and WIN2000

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-09-11T11:52:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XJ9v5.1938$kB1.3693@newsfeed.slurp.net>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net>`

```
Rich,

It sounds like the Run-Time System files are missing.  You might try
installing Micro Focus on the server - this should fix the problem.  You
could also just copy the RTS, but you would have to pay for another
developer license due to MF license constraints - unless you are running
NetExpress v3.0 (not 3.1!), which allows you to ship the RTS free of
charge.

Hope it helps

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net
Web:   http://www.c-cubed.net


Rich Cullen <rich@sparksit.com> wrote in message
news:8pilpv$cg4@dispatch.concentric.net...
> We have an application written in MicroFocus COBOL that we are trying
to run
> on a WIN2000 server system.
>
> From workstations, we can run the application fine with the files on
the
> server.  When we try to run the application on the server, we get the
> message "COBOL run time library not installed - file not found."  Our
> application developer is not any help.  They essentially say, "We
don't do
> windows; run it on NetWare."
>
> We need to be able to run the application on WIN2000 in order to use
Windows
> Terminal Server for a remote office.
>
> Is there a simple fix for this problem?  We know very little about
COBOL.
>
> Thanks for any help.
…[3 more quoted lines elided]…
>
```

#### ↳ Re: MicroFocus COBOL and WIN2000

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-09-11T12:08:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pjak2$pf0$1@news.cerf.net>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net>`

```
"Rich Cullen" <rich@sparksit.com> wrote in message
news:8pilpv$cg4@dispatch.concentric.net...
> From workstations, we can run the application fine with the files on the
> server.  When we try to run the application on the server, we get the
…[4 more quoted lines elided]…
> We need to be able to run the application on WIN2000 in order to use
Windows
> Terminal Server for a remote office.
>
> Is there a simple fix for this problem?  We know very little about COBOL.

This sounds like an installation issue. The thing is, when you attach as a
remote user to the Windows terminal server. You get your own separate system
directory, which differs from the standard directory that you get when
accessing locally. This effectively affects the searchpath for your
applications. There are various ways of solving this issue. But first of all
you will have to determine what files are missing for the remote connection,
then you will have to decide where is the appropriate location for the
files. Due to security issues, you can't just give access to all over, and
copying the files around probably ain't a good solution either due to
possible maintenance problems. I guess you should discuss this issue with
Merant, as they sooner or later must target this issue, unless they already
have (likely).

To put it straight, your remote connection is to be considered a computer
that does not have your application installed yet because the initial
installation executed locally on the server did not pay attention to being
installed on a Windows Terminal Server.

Note: Depending on the application, this may not only apply to DLL's, but
also registry settings and other files. It is pretty simple to fix when you
know what you have to fix, but if you don't know what is impacted by the
remote connection, it is hard.

Cheesle
```

##### ↳ ↳ Re: MicroFocus COBOL and WIN2000

- **From:** "Rich Cullen" <rich@sparksit.com>
- **Date:** 2000-09-11T21:58:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pjkht$cfe@dispatch.concentric.net>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net> <8pjak2$pf0$1@news.cerf.net>`

```
Cheesle,

Thanks for the help; but I don't think it is really a terminal server issue.
I get the same message if I try to run application from a DOS box on the
server.

I seem to be dealing with a DOS version of this application.  I copied the
files from the old NetWare directory to the new directory on the W2K server
and the application runs fine from the workstations.  It runs just like it
did on the old NetWare server.

Could there be some files on the workstations that are not on the server?
The more I think about it, the more I think that could be the problem.  What
would the files be, and where would they be located?  Maybe this "run time
library" file needs to be on the server in order to run the application on
the server or on terminal server.

Thanks again.
Rich


Cheesle <cheesle@online.NoSpamPlease.no> wrote in message
news:8pjak2$pf0$1@news.cerf.net...
> "Rich Cullen" <rich@sparksit.com> wrote in message
> news:8pilpv$cg4@dispatch.concentric.net...
…[3 more quoted lines elided]…
> > application developer is not any help.  They essentially say, "We don't
do
> > windows; run it on NetWare."
> >
…[4 more quoted lines elided]…
> > Is there a simple fix for this problem?  We know very little about
COBOL.
>
> This sounds like an installation issue. The thing is, when you attach as a
> remote user to the Windows terminal server. You get your own separate
system
> directory, which differs from the standard directory that you get when
> accessing locally. This effectively affects the searchpath for your
> applications. There are various ways of solving this issue. But first of
all
> you will have to determine what files are missing for the remote
connection,
> then you will have to decide where is the appropriate location for the
> files. Due to security issues, you can't just give access to all over, and
> copying the files around probably ain't a good solution either due to
> possible maintenance problems. I guess you should discuss this issue with
> Merant, as they sooner or later must target this issue, unless they
already
> have (likely).
>
…[6 more quoted lines elided]…
> also registry settings and other files. It is pretty simple to fix when
you
> know what you have to fix, but if you don't know what is impacted by the
> remote connection, it is hard.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL and WIN2000

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-09-12T09:28:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pkt82$h8d$1@hyperion.mfltd.co.uk>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net> <8pjak2$pf0$1@news.cerf.net> <8pjkht$cfe@dispatch.concentric.net>`

```
Rich,

> I seem to be dealing with a DOS version of this application.  I copied the
> files from the old NetWare directory to the new directory on the W2K
server
> and the application runs fine from the workstations.  It runs just like it
> did on the old NetWare server.
>

I don't think you are necessarily missing any files. On old Micro Focus
products eg 2.5 or 3.4, the executables produced could run on either DOS or
OS/2. 32-bit Windows platforms, including Win2000, will default to trying to
run the OS/2 part of the executable and in order to do that you need to have
the directory containing the run-time DLLs eg COBLIB.DLL added to the
Os2LibPath system environment variable. Alternatively, you can use the
FORCEDOS command to run the DOS part of the application.
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL and WIN2000

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-13T00:38:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pn36l$as8$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net> <8pjak2$pf0$1@news.cerf.net> <8pjkht$cfe@dispatch.concentric.net> <8pkt82$h8d$1@hyperion.mfltd.co.uk>`

```

Gael Wilson <gael.wilson@merant.com> wrote in message
news:8pkt82$h8d$1@hyperion.mfltd.co.uk...
> Rich,
>
> > I seem to be dealing with a DOS version of this application.
I copied the
> > files from the old NetWare directory to the new directory on
the W2K
> server
> > and the application runs fine from the workstations.  It runs
just like it
> > did on the old NetWare server.
> >
>
> I don't think you are necessarily missing any files. On old
Micro Focus
> products eg 2.5 or 3.4, the executables produced could run on
either DOS or
> OS/2. 32-bit Windows platforms, including Win2000, will default
to trying to
> run the OS/2 part of the executable and in order to do that you
need to have
> the directory containing the run-time DLLs eg COBLIB.DLL added
to the
> Os2LibPath system environment variable. Alternatively, you can
use the
> FORCEDOS command to run the DOS part of the application.
>
>
>
    I think that the dos only run.exe is named run.dle.  Try
renaming it
to EXE, and the FORCEDOS command will not be needed.
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL and WIN2000

_(reply depth: 5)_

- **From:** "Rich Cullen" <rich@sparksit.com>
- **Date:** 2000-09-13T15:20:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8po60j$di6@dispatch.concentric.net>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net> <8pjak2$pf0$1@news.cerf.net> <8pjkht$cfe@dispatch.concentric.net> <8pkt82$h8d$1@hyperion.mfltd.co.uk> <8pn36l$as8$1@sshuraab-i-1.production.compuserve.com>`

```
Russell,

Thanks for the help, but I don't have a file named run.dle or anything close
to that.

Rich

Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote in message
news:8pn36l$as8$1@sshuraab-i-1.production.compuserve.com...
>
> Gael Wilson <gael.wilson@merant.com> wrote in message
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL and WIN2000

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-09-12T08:02:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8plgih$2b5$1@news.cerf.net>`
- **References:** `<8pilpv$cg4@dispatch.concentric.net> <8pjak2$pf0$1@news.cerf.net> <8pjkht$cfe@dispatch.concentric.net>`

```
"Rich Cullen" <rich@sparksit.com> wrote in message
news:8pjkht$cfe@dispatch.concentric.net...
> Could there be some files on the workstations that are not on the server?

I am sorry, but I don't know NetExpress, so I am out of clues.

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
