[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF cobol 3.2 relative file 9/065-File Locked.

_3 messages · 3 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF cobol 3.2 relative file 9/065-File Locked.

- **From:** "Michael ValeCruz" <mvalecruz1@mcyber.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o7jiv$r8e$1@nntp4.atl.mindspring.net>`

```
The program seems to be getting a lot of these errors....I think it is
related to a timing problem with the server communication... NT Servers and
Novell Servers.
There are points in the program were it closes the file then turns around
and  re-opens the  file for Output but my guess is that the file has not
fully closed on the server but  the server is going ahead and processing the
open statement and returning a 065-File Locked after seeing the file not
closed....These are temporary single user files for external sorting so
there is no multi-user accessing of the file.

Any experience in this file-status is appreciated....
```

#### ↳ Re: MF cobol 3.2 relative file 9/065-File Locked.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tcLp3.554$n66.26183@dfiatx1-snr1.gtei.net>`
- **References:** `<7o7jiv$r8e$1@nntp4.atl.mindspring.net>`

```
You know, a couple of months ago Jill McLeester started a thread on the
PowerBASIC web BBS about network problems in peer-peer networks. There was a
sort of similar problem which resulted from a change by a certain major
software developer in located in Redmond WA.

It seems this developer changed the network file access from a synchronous
to an asynchronous operation, and any file functions which assumed that a
previous operation invoked from a program would already be completed (as
they would have been when the operation was synchronous) were now failing,
because the operating system was now performing them asynchronously and
just had not got around to it yet.

I am not a network/synchronicity guy by any stretch of the imagination, but
if you go to the PowerBASIC web bbs at
www.powerbasic.com/cgi-bin/ultimate.cgi and use the "search" for topic
"Windows 95/98 Networking Havoc " in the "programming" section you might
find something of interest. The first entry in the thread was posted 2-2-99.
(You may have to register to have access to the BBS. But they don't spam you
or anything).

Or, I have the entire thread in html format (size 59K) , and would be happy
to e-mail it or post it somewhere.
```

#### ↳ Re: MF cobol 3.2 relative file 9/065-File Locked.

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37a7b3f6.174338680@news1.ibm.net>`
- **References:** `<7o7jiv$r8e$1@nntp4.atl.mindspring.net>`

```
I used to see the 065 errors when an Windows 95 Pentium workstation
was connected to a novell server and the files resided onthe novell
server.

1. Get the Client 32 drivers from Novell, don't use the Microsoft
drivers.
2.  In the Performance tab of System in control panel, go to
Diagnostics and "Disable new record locking semantics".

That seemed to cure the problem.



On Tue, 3 Aug 1999 16:28:52 -0400, "Michael ValeCruz"
<mvalecruz1@mcyber.com> wrote:

>The program seems to be getting a lot of these errors....I think it is
>related to a timing problem with the server communication... NT Servers and
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
