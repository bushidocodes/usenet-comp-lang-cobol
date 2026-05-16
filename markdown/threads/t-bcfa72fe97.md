[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WinHelp in Realia 3.1

_5 messages · 3 participants · 2000-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### WinHelp in Realia 3.1

- **From:** "Stephen Plotnick" <thepla@attglobal.net>
- **Date:** 2000-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e88b16_4@news1.prserv.net>`

```
I have been developing a system in Realia Workbench 3.1 using Gui Screenio
and I am now ready to do the help system. I have downloaded a package "Four
Help 4" and it seems that this program will be able to create the help
files. The question I have is how do I call the windows help facility to
read these files when I am done? Thanks in advance.
```

#### ↳ Re: WinHelp in Realia 3.1

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E893D7.4AF5@NOSPAMguysoftware.com>`
- **References:** `<39e88b16_4@news1.prserv.net>`

```
Stephen Plotnick wrote:
> 
> I have been developing a system in Realia Workbench 3.1 using Gui Screenio
…[3 more quoted lines elided]…
> read these files when I am done? Thanks in advance.

To call WinHelp HLP files from a program written with a tool which doesn't do it for 
you, you need to call the WinHelp API.  It's not rocket science and many people call it 
directly even they use a programming tool which WOULD do it for them.

To compile WinHelp files you'll also need to install the Microsoft Help Workshop (you 
can get it from Microsoft directly via links on http://www.guysoftware.com/helllp.html 
or http://www.helpmaster.com/) and its help file gives you details about the API calls.
```

#### ↳ Re: WinHelp in Realia 3.1

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2000-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39eb26b4.634121@news>`
- **References:** `<39e88b16_4@news1.prserv.net>`

```
Hi, Steve,

There's a pretty neat way to do this, or to handle any other
system-wide event you want to use.

First, define the menu item, accelerator, or button you want to use on
your panels; Windows uses F1 for help, although I've also seen Alt+H
used.  Override the event-ID field to ensure that the same event
number is assigned  on every panel.  (We're presently discussing a
couple of ways of enhancing GUI ScreenIO so that you could assign
systemwide events like this more easily).

Now, modify the GS.COB stub that we provided so that it will examine
the event ID passed back by the runtime.  If it matches your Help
event, just invoke your help system from within GS. 

I'll email you a modified copy of GS.COB that shows how we'd do it. 

Actually, this is something that could be used for other things, too;
I'll look into adding the changes to the GS.COB stub that we
distribute for the benefit of others...

Any more questions, contact us at:  Support@ScreenIO.com

Kevin
-----------------------------
On Sat, 14 Oct 2000 11:32:07 -0500, "Stephen Plotnick"
<thepla@attglobal.net> wrote:

>I have been developing a system in Realia Workbench 3.1 using Gui Screenio
>and I am now ready to do the help system. I have downloaded a package "Four
…[4 more quoted lines elided]…
>

Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

##### ↳ ↳ Re: WinHelp in Realia 3.1

- **From:** "Stephen Plotnick" <thepla@attglobal.net>
- **Date:** 2000-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ebd5c2_3@news1.prserv.net>`
- **References:** `<39e88b16_4@news1.prserv.net> <39eb26b4.634121@news>`

```
Thanks for the information. I will do as you have suggested.

For anybody interest in how to call the help system from within Realia 3.1
do the following:

           MOVE SPACES TO PROG-NAME.
           MOVE SPACES TO COMMAND-LINE.

           STRING 'WINHELP.EXE' DELIMITED BY SIZE
                  X'00' DELIMITED BY SIZE
             INTO PROG-NAME.

           STRING 'HHHELP' DELIMITED BY SIZE
                  X'00' DELIMITED BY SIZE
             INTO COMMAND-LINE.

           CALL 'REALIA_EXEC_PROGRAM' USING PROCESS-HANDLE
                                            PROG-NAME
                                            COMMAND-LINE
                                     GIVING STATUS-CODE.

           IF STATUS-CODE = ZERO
               CALL 'REALIA_EXEC_DETACH' USING PROCESS-HANDLE
                                        GIVING STATUS-CODE.

HHHELP is the name of the help files (.hlp and .cnt and .lfg) files.

Kevin J. Hansen <Support@ScreenIO.com> wrote in message
news:39eb26b4.634121@news...
> Hi, Steve,
>
…[27 more quoted lines elided]…
> >I have been developing a system in Realia Workbench 3.1 using Gui
Screenio
> >and I am now ready to do the help system. I have downloaded a package
"Four
> >Help 4" and it seems that this program will be able to create the help
> >files. The question I have is how do I call the windows help facility to
…[6 more quoted lines elided]…
> http://www.screenio.com
```

###### ↳ ↳ ↳ Re: WinHelp in Realia 3.1

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39EC6FAC.5EBA@NOSPAMguysoftware.com>`
- **References:** `<39e88b16_4@news1.prserv.net> <39eb26b4.634121@news> <39ebd5c2_3@news1.prserv.net>`

```
This looks like it will start a new occurrence of WinHelp with each call.  Also it will 
leave it open when your program terminates.

If you want to avoid that, you'll need to use direct calls to the WinHelp API instead of 
just executing WinHelp with the help file name in the command line.  You'll find all the 
API parameter specs in help file that you installed with the Microsoft Help Workship 
(it's called something like "Help Author Guide" on the Start menu item).

Stephen Plotnick wrote:
> 
> Thanks for the information. I will do as you have suggested.
…[69 more quoted lines elided]…
> > http://www.screenio.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
