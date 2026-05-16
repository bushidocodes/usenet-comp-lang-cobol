[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# execute os-commands win nt

_4 messages · 4 participants · 2000-08 → 2000-09_

---

### execute os-commands win nt

- **From:** Dirk Drexler <dirk.drexler@gmx.de>
- **Date:** 2000-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8o54pv$n6g$1@nnrp1.deja.com>`

```
A wonderful good morning!

How can I execute os-commands with my programm under win nt (still
using merant netexpress 3.0) ?
I want to inform some friendly user, blocking the oracle database with
the net send command like this:

net send user-var message-var

Thanx
```

#### ↳ Re: execute os-commands win nt

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 2000-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8o5cp1$2ek$1@hyperion.mfltd.co.uk>`
- **References:** `<8o54pv$n6g$1@nnrp1.deja.com>`

```
Hi Dirk,

You couild either use the X"91" function 35 call which is documented in the
online help.

Or use the Windows API CreateProcess. There is a demo of this available at:-

http://support.merant.com/websupport/netx/nesamp.asp#win32api

Hope this helps
David.


Dirk Drexler <dirk.drexler@gmx.de> wrote in message
news:8o54pv$n6g$1@nnrp1.deja.com...
> A wonderful good morning!
>
…[14 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: execute os-commands win nt

- **From:** "Thomas Veit" <Thomas.Veit@tectum.de>
- **Date:** 2000-09-08T10:19:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39b8a065$0$29240@businessnews.de.uu.net>`
- **References:** `<8o54pv$n6g$1@nnrp1.deja.com>`

```
Use the X'91'-Call

Greetings

Thomas Veit

Dirk Drexler <dirk.drexler@gmx.de> schrieb in im Newsbeitrag:
8o54pv$n6g$1@nnrp1.deja.com...
> A wonderful good morning!
>
…[14 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: execute os-commands win nt

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-09-08T09:43:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cy8u5.822$Ek.4283@newsfeed.slurp.net>`
- **References:** `<8o54pv$n6g$1@nnrp1.deja.com> <39b8a065$0$29240@businessnews.de.uu.net>`

```
The following code will do what you need.  It also shows you how to
start a process asynchronously (ws-exec-type='ASYNC') or synchronously
(ws-exec-type='SYNC').  It should also be noted that the return-code
returned by the x'91' function 35 call DOES NOT indicate that the
command itself was successful, but rather that the command was
interpreted (syntax, etc.) successfully!  It should also be noted that
only 120 characters can be passed on a command-line in Windows 3.x.  I
believe Win 9x/NT will pass more, but the example below only uses 120
bytes - increase the "args-120" definition if you want to change this.

Hope it helps.

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net

C-Cubed Inc.
3629 North Morning Dove
Mesa, AZ  85207

Phone:  (888) 962-8233
Fax:    (888) 962-4658
Web:   http://www.c-cubed.net


Working-Storage Coding:

       01  ws-miscellaneous.
           03  ws-exec-type            pic x(5).
           03  ws-exec-name            pic x(255).
           03  ws-exec-parm            pic x(255).
           03  ws-exec-type            pic x(5).
           03  ws-exec-name            pic x(255).
           03  ws-exec-parm            pic x(255).

       01  args                        pic x(255).
       01  args-120                    pic x(120).

       01  func-35                     pic x     comp-x value 35.
       01  resultcode                  pic x     comp-x value 0.
       01  parm-group.
           03  name-len                pic x     comp-x value 0.
           03  parm-string             pic x.


Procedure Division coding:

      *----------------------------------------------------------------*
      * This section will call the Micro Focus x'91' function-35       *
      * routine to start a .CMD / .BAT batch file for execution.       *
      *----------------------------------------------------------------*
       1030-cmd-file  section.
           move spaces                 to args.
           move 'notepad.exe'      to ws-exec-name.
           move 'c:\config.sys'     to ws-exec-parm.
           move 'ASYNC'             to ws-exec-type.

           evaluate true

      * Command-line for Asyncronous process:
               when ws-exec-type equal 'ASYNC'
                   string
                       'start '            delimited by size
                       ws-exec-name        delimited by '  '
                       ' '                 delimited by size
                       ws-exec-parm        delimited by '  '
                       into args
                   end-string

      * Command-line for Syncronous process:
               when other
                   string
                       ws-exec-name        delimited by '  '
                       ' '                 delimited by size
                       ws-exec-parm        delimited by '  '
                       into args
                   end-string
           end-evaluate.

           move args                   to args-120.
           display args-120            upon command-line.

      * Call Micro Focus API to execute command-line:
           call x'91' using resultcode
                            func-35
                            parm-group
           end-call.

           move resultcode             to return-code.

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net
Web:   http://www.c-cubed.net


Thomas Veit <Thomas.Veit@tectum.de> wrote in message
news:39b8a065$0$29240@businessnews.de.uu.net...
> Use the X'91'-Call
>
…[10 more quoted lines elided]…
> > I want to inform some friendly user, blocking the oracle database
with
> > the net send command like this:
> >
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
