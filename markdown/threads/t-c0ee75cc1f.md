[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNIX COBOL interacting with WINDOWS programs/data

_8 messages · 5 participants · 2003-01_

---

### UNIX COBOL interacting with WINDOWS programs/data

- **From:** david@quantumcat.demon.co.uk (David Latimer)
- **Date:** 2003-01-20T06:37:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9026f4e.0301200637.1e97f67d@posting.google.com>`

```
Can anyone who runs COBOL on UNIX/LINUX but is connected to WINDOWS 
machines through a network help with the following 2 questions?

1. Is it possible to access data files from WINDOWS programs such as 
AUTOCAD, EXCELL, MS SQL? 
ie both reading the data into a COBOL program and writing data out to 
a new file.

2. Can you ever call WINDOWS programs from UNIX/LINUX?
Am I right in thinking that you can't call big programs like 
Outlook/Excell and that the only way would be to use a COBOL compiler 
on WINDOWS.

David
```

#### ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-20T11:33:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301201133.266840e@posting.google.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com>`

```
david@quantumcat.demon.co.uk (David Latimer) wrote 

> Can anyone who runs COBOL on UNIX/LINUX but is connected to WINDOWS 
> machines through a network help with the following 2 questions?
…[4 more quoted lines elided]…
> a new file.

Unix and Linux can mount Windows shares into the file system and thus
gain read/write access to the files on that machine(s).

 mount -t smbfs -o username=name,password=pw //winmachine/windir
/mnt/windir

smbfs = SMB file system (Windows/Samba).  Files in that share will be
accessed in the /mnt/windir directory.
 
> 2. Can you ever call WINDOWS programs from UNIX/LINUX?
> Am I right in thinking that you can't call big programs like 
> Outlook/Excell and that the only way would be to use a COBOL compiler 
> on WINDOWS.

Well you can't 'call' a program to cause it to run on another machine,
but you may talk to other programs using sockets.
```

##### ↳ ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-01-21T09:24:39
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b0j36o$8iv$1@hyperion.microfocus.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com> <217e491a.0301201133.266840e@posting.google.com>`

```
>
> Well you can't 'call' a program to cause it to run on another machine,
> but you may talk to other programs using sockets.
If you are using Micro Focus COBOL it's possible to use CCITCP2 to do remote
procedure calls to the other computer.

www.microfocus.com
```

##### ↳ ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** david@quantumcat.demon.co.uk (David Latimer)
- **Date:** 2003-01-21T08:08:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9026f4e.0301210808.d5b6cbd@posting.google.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com> <217e491a.0301201133.266840e@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0301201133.266840e@posting.google.com>...
> david@quantumcat.demon.co.uk (David Latimer) wrote 
> 
…[15 more quoted lines elided]…
> accessed in the /mnt/windir directory.

Thanks for that. Samba looks very interesting.

>  
> > 2. Can you ever call WINDOWS programs from UNIX/LINUX?
…[5 more quoted lines elided]…
> but you may talk to other programs using sockets.

Can you NEVER launch a Windows program (eg Excel on users local PC) from 
a COBOL program running on a server (which could be ANY of UNIX/LINUX/WINDOWS)?
```

###### ↳ ↳ ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-22T20:26:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301222026.7da95d1f@posting.google.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com> <217e491a.0301201133.266840e@posting.google.com> <a9026f4e.0301210808.d5b6cbd@posting.google.com>`

```
david@quantumcat.demon.co.uk (David Latimer) wrote 

> > smbfs = SMB file system (Windows/Samba).  Files in that share will be
> > accessed in the /mnt/windir directory.
> 
> Thanks for that. Samba looks very interesting.

You don't need to be running Samba in order to mount Windows shares. 
Samba allows Unix/Linux directories to be seen by Windows (or smbfs)
as shares.

That is: On Linux Samba is the server end of an SMB share, 'mount -t
smbfs ..' is the client end.

> > Well you can't 'call' a program to cause it to run on another machine,
> > but you may talk to other programs using sockets.
> 
> Can you NEVER launch a Windows program (eg Excel on users local PC) from 
> a COBOL program running on a server (which could be ANY of UNIX/LINUX/WINDOWS)?

You can launch a Windows program, but only by talking to a program on
the Windows machine in some way and asking that to launch it.


I sometimes use a very simple batch file that is in the startup of a
Windows machine.  This checks a specific directory on the server for
batch files:

       :DoAgain
       CD N:\REOMOTE\NODEnn
       FOR %%F IN ( *.BAT ) DO CALL RUNBAT %%F
       DOSSleep 60
       GOTO DoAgain

Where N: is a share on the local network server, nn=node numer for
this machine, RUNBAT.BAT will execute the .BAT file and will then
delete it.  Then all it takes is to dump a batch file into the server
directory for the appropriate machine.
This is used where I need to run a specifically Windows or DOS
program, the application just writes/copies the appropriate file.
Not sophisticated but it does the job.
```

#### ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-01-21T18:54:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<965r2vovf0cir7cpl48rjn3daufvvdiu77@4ax.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com>`

```
david@quantumcat.demon.co.uk (David Latimer) wrote:

>Can anyone who runs COBOL on UNIX/LINUX but is connected to WINDOWS 
>machines through a network help with the following 2 questions?
…[4 more quoted lines elided]…
>a new file.

David:

With the Flexus Thin Client, data files resident on the Windows client
machine can be copied to the server platform and made available to the
COBOL program running on the UNIX server.

The file can then be copied back down to the client machine.

>2. Can you ever call WINDOWS programs from UNIX/LINUX?

Thin Client allows you to execute remote programs.....either executing
client-side programs from the server or executing server-side programs
from the client.

>Am I right in thinking that you can't call big programs like 
>Outlook/Excell and that the only way would be to use a COBOL compiler 
>on WINDOWS.

Not true.  I'm quite sure that you could execute these programs
remotely.  With Thin Client and our COBOL sp2 product, you could even
embed Active X e-mail and spreadsheet objects into the client-side GUI
screens and control them from the UNIX server-based COBOL program.
This would allow you to have the e-mail and spreadsheet capabilities
directly in your COBOL program and avoid the necessity of calling the
external programs.......besides.....what if a particular client uses
Eudora or Quattro Pro?  That would create problems.  An embedded OCX
would be the same for all clients.

Thin Client and COBOL sp2 is a very powerful and easy-to-use method of
"Internet-enabling" your COBOL programs.  

The software is also COBOL compiler indpendent and operating system
independent.  Your choice of a UNIX server combined with Windows
clients is an outstanding choice.......in my opinion, an extremely
reliable and powerful client/server platform.  Our experience is that
it provides you with the best of both worlds.......a superior server
platform combined with the world's most popular desktop environment.

Send a private e-mail message to me at rtwolfe@flexus.com if you have
additional questions or would like to evaluate the software.





Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** david@quantumcat.demon.co.uk (David Latimer)
- **Date:** 2003-01-22T08:49:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9026f4e.0301220849.49a6d8df@posting.google.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com> <965r2vovf0cir7cpl48rjn3daufvvdiu77@4ax.com>`

```
Bob Wolfe <rtwolfe@flexus.com> wrote in message news:<965r2vovf0cir7cpl48rjn3daufvvdiu77@4ax.com>...
> david@quantumcat.demon.co.uk (David Latimer) wrote:
> 
…[34 more quoted lines elided]…
> would be the same for all clients.

WOW I didn't know that this might be possible!

Has anyone in this newsgroup experimented with Active X objects in SP2?

> 
> Thin Client and COBOL sp2 is a very powerful and easy-to-use method of
…[19 more quoted lines elided]…
> Check out The Flexus COBOL Page at http://www.flexus.com


I will email you soon Bob,
David
```

###### ↳ ↳ ↳ Re: UNIX COBOL interacting with WINDOWS programs/data

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-01-26T08:50:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0301260850.12d89fa@posting.google.com>`
- **References:** `<a9026f4e.0301200637.1e97f67d@posting.google.com> <965r2vovf0cir7cpl48rjn3daufvvdiu77@4ax.com> <a9026f4e.0301220849.49a6d8df@posting.google.com>`

```
david@quantumcat.demon.co.uk (David Latimer) wrote in message > 
> WOW I didn't know that this might be possible!
> 
> Has anyone in this newsgroup experimented with Active X objects in SP2?
> 

All the time - and the support for different types of controls is
constantly being enhanced.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
