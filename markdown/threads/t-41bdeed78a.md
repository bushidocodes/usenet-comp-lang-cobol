[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 98,90

_9 messages · 3 participants · 2008-08_

---

### Error 98,90

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-08-19T03:02:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com>`

```
Hi Everybody,
I'm using Acucobol 4.3 and experiencing a strange corruption error
98,90.
All the workstations are running WindowsXPpro and the Server is
running 2003Server.
Did anyone ever face this problem before ?
Thanks for your help.

Giovanni
```

#### ↳ Re: Error 98,90

- **From:** sgbojo@gmail.com
- **Date:** 2008-08-19T07:23:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161da6e-9592-49d8-ae77-87c769747062@r35g2000prm.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com>`

```
98,90 is pretty well known as a file locking issue when using mapped
drives.

The main reason for file error 98,90's is when runtimes terminate
incorrectly.  Normally when the runtime shuts down it will update some
information in the Vision file header and subtract itself from the
user count that is also in the Vision File header.  If the information
in the header is incorrect the runtime will report a corruption
error.

An invalid user count in the Vision File header can cause the error
98,90 to be returned as well.  You can check Vision files to determine
if they have a non-zero user count by using the vutil -check -a
{filename} command.  Non-zero user counts when no one is accessing the
file indicate improper shutdown.

•Recommendations.

You could try setting the runtime configuration variable FLUSH_ON_OPEN
to "1" as this will cause the runtime to flush the system buffers on
the first WRITE, REWRITE or DELETE on an indexed file opened for I/O.
The purpose of this is to keep the user count in the header
accurate.

You might also wish to Set V_BUFFERS 0 and V_LOCK_METHOD 0 in the
runtime configuration files.  The default setting for V_LOCK_METHOD of
"0" (zero) causes Vision to lock the first byte of the file for every
access to the file (both reads and updates). This ensures that the
process is not interfered with by another process.

V_BUFFERS sets the number of indexed block buffers to allocate. These
buffers are used to improve the performance of indexed files. Each
buffer is 512 bytes plus some overhead. Increasing the number of
buffers can improve file performance. Decreasing the number conserves
memory. The value of V_BUFFERS has no effect on versions of ACUCOBOL-
GT that do not use Vision files. The value of V_BUFFERS can range from
zero (no buffering) to 2097152. The default value is 64.
```

##### ↳ ↳ Re: Error 98,90

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-08-20T01:01:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea321ec-e6b0-4fe1-a172-764bd9857cec@r66g2000hsg.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <1161da6e-9592-49d8-ae77-87c769747062@r35g2000prm.googlegroups.com>`

```
On Aug 19, 4:23 pm, sgb...@gmail.com wrote:
> 98,90 is pretty well known as a file locking issue when using mapped
> drives.
…[34 more quoted lines elided]…
> zero (no buffering) to 2097152. The default value is 64.

Many thanks for the hints.
I'll try to set the configuration flags.
Don't you think that can also be something system related ?
I have other companies with the same environment that are not
experiencing the same problem.
Thanks again.

G
```

###### ↳ ↳ ↳ Re: Error 98,90

- **From:** sgbojo@gmail.com
- **Date:** 2008-08-20T06:43:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dee8669d-ccc3-4b3a-8ddb-9ef9046f761b@n38g2000prl.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <1161da6e-9592-49d8-ae77-87c769747062@r35g2000prm.googlegroups.com> <3ea321ec-e6b0-4fe1-a172-764bd9857cec@r66g2000hsg.googlegroups.com>`

```
It is a system issue due to that you are using Windows mapped drives
to have a program execute on PC-A while the data files reside on a
mapped drive to server b.

A Microsoft Windows feature called opportunistic locking (or
“oplocks”) for shared files is available for multi-user network
environments to improve system performance.  Opportunistic locking is
a file access method that allows the caching of data files on a user’s
workstation while that user reads or updates the files.  This feature
is intended to optimize network performance by reducing the number of
read and write operations that travel across the network when data
files are modified.
Opportunistic locking may cause problems in peer-to-peer networks that
accommodate a large number of users and heavy database activity
without a dedicated server.  We have observed that opportunistic
locking may result in file corruption of shared files.  When a second
user opens a particular file, the system retrieves the file from the
first user’s local machine and allows file access to the second user.
The possibility for corruption exists in the “handoff” of the file
among the users who share it.
Recognizing that file integrity is an important issue for any company,
Microsoft has recommended disabling this feature in any network that
uses its Access database.  (Refer to Microsoft Knowledge Base Article
300216 at support.microsoft.com for more details.)  Similarly, Novell
currently distributes its systems with this feature disabled by
default.  Acucorp also recommends disabling this feature to ensure
file integrity. Disabling opportunistic locking may degrade
application performance significantly, particularly if the application
reads and writes data across a network at a rate of only a few bytes
at a time.  In contrast, Acucorp’s runtime reads and writes indexed
files in blocks of 512 or 1024 bytes each, depending on the block size
set at file creation.  It uses standard C file access routines—open(),
read(), write(), seek(), and close()—to accomplish file-handling
operations.  This behavior allows several bytes at a time to be
transmitted across a network. Users should note that file OPENs are
relatively expensive operations, especially on Windows systems.
Eliminating non-essential file OPENs could make an application more
efficient and in turn improve application performance.  Users might
also consider the acquisition of a dedicated server for networks that
facilitate database access.
```

###### ↳ ↳ ↳ Re: Error 98,90

_(reply depth: 4)_

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-08-20T09:15:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3705b7f3-a0d3-497c-889e-3effe84507d3@s50g2000hsb.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <1161da6e-9592-49d8-ae77-87c769747062@r35g2000prm.googlegroups.com> <3ea321ec-e6b0-4fe1-a172-764bd9857cec@r66g2000hsg.googlegroups.com> <dee8669d-ccc3-4b3a-8ddb-9ef9046f761b@n38g2000prl.googlegroups.com>`

```
On Aug 20, 3:43 pm, sgb...@gmail.com wrote:
> It is a systemissuedue to that you are using Windows mapped drives
> to have a program execute on PC-A while the data files reside on a
…[36 more quoted lines elided]…
> facilitate database access.

I'll check the server configuration as well.
Many thanks for your detailed description of the problem.
Grazie.
```

#### ↳ Re: Error 98,90

- **From:** Lothar Krauss <news5@m2008.lkrauss.de>
- **Date:** 2008-08-21T00:10:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g8i4o6$hdk$00$1@news.t-online.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com>`

```
Gio wrote:

> Hi Everybody,
> I'm using Acucobol 4.3 and experiencing a strange corruption error
…[6 more quoted lines elided]…
> Giovanni

We get sometimes the same error code when the user count is zero but someone
access this file. An other error code in the same situation is 98,89. 

I've written a small C programm to change the user count of a vision file
without rebuilding this file and while runtimes are accessing the file. You
can get the source code from

http://www.lkrauss.de/vuserset/vuserset.c

(the comments a in german language). It will compile under Unix and Linux
systems, but I don't know if it will work on a windows system.

Lothar
```

##### ↳ ↳ Re: Error 98,90

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-08-21T06:48:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ace05368-c133-4a4d-a552-26ec71571524@e53g2000hsa.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <g8i4o6$hdk$00$1@news.t-online.com>`

```
On Aug 21, 12:10 am, Lothar Krauss <ne...@m2008.lkrauss.de> wrote:
> Gio wrote:
> > Hi Everybody,
…[21 more quoted lines elided]…
> Lothar

Thanks Lothar,
how do you use this C program?
Unfortunately I'm not used to german.
Can you give more informations? Did you solve the problem with this ?
In which way ?

Thanks
Gio
```

##### ↳ ↳ Re: Error 98,90

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-08-21T06:48:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d2655fa5-9b53-4ca9-ad3f-48d4012c0683@a70g2000hsh.googlegroups.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <g8i4o6$hdk$00$1@news.t-online.com>`

```
On Aug 21, 12:10 am, Lothar Krauss <ne...@m2008.lkrauss.de> wrote:
> Gio wrote:
> > Hi Everybody,
…[21 more quoted lines elided]…
> Lothar

Thanks Lothar,
how do you use this C program?
Unfortunately I'm not used to german.
Can you give more informations? Did you solve the problem with this ?
In which way ?

Thanks
Gio
```

###### ↳ ↳ ↳ Re: Error 98,90

- **From:** Lothar Krauss <news5@m2008.lkrauss.de>
- **Date:** 2008-08-21T19:02:27+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g8k733$lu4$03$1@news.t-online.com>`
- **References:** `<c4b861d9-54cc-4099-8c4c-0e34256b381a@m73g2000hsh.googlegroups.com> <g8i4o6$hdk$00$1@news.t-online.com> <d2655fa5-9b53-4ca9-ad3f-48d4012c0683@a70g2000hsh.googlegroups.com>`

```
Gio wrote:
> 
> Thanks Lothar,
…[6 more quoted lines elided]…
> Gio

Hello Gio,

this program does not really solve the problem, but it prevents negative
impact. The user count of Vision files counts up one when a process opens
the file and count down one if the file is closed or then runtime shuts
down in a regular way. But if the runtime does not shut down regular (for
example if the client is killed) this counter grows. Since it is a 16 bit
number it will grow to 32767, then jump to -32768 and some day it will be 0
even though someone accesses the file. In this situation other processes
trying to open the file will get the error code 98,89 or 98,90.

The regular way would be a "vutil -rebuild" with the vutil tool from
AcuCorp. But this means you have to shut down the application and with
large files this may take several hours.

With my vuserset tool you may call i.e.

vuserset filename 100

to set the user count of a file to 100. Before you use this program you
shuld verify with "vutil -check filename" that it is really the user count
wich causes your problem.

If you have a Vision V.4 or V.5 file you must not use this tool on the
extension files (*.v??, *.d??). Run the program only on the main file and
make sure you have a backup. The number must not be lower than the actual
number of opens on the file and it should not be unnecessary high. When I
use the program I count the number of running processes, multiply it with
the number of opens on this file in a process and add about 20%.

If this solves your problem you may use this tool also prophylactical.

Lothar
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
