[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# file status woes

_4 messages · 2 participants · 1999-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### file status woes

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n0db6$shn$1@news.igs.net>`

```
I have a file sharing problem that I would like to share (and cannot, which
is the problem in a nutshell).

Platform Fujitsu 4.0 on windows95/98.

I have a system using file locking on an Isam file on a server.  There are
about ten users using the file, at a fairly low transaction rate (30-40
updates per minute at absolute peak).  The system uses full file locking ...
that is, open file I-O, if busy wait and try again, else do update, close.
The system has been running in using this scheme and this hardware for about
three months, and on previous platforms for about twelve years.  The code is
solid. The problem is hardware.

I now have a computer in a moving vehicle that is connected via packet
switched radio Ethernet. It fades in and out.  If it locks the file, then
fades out for thirty or fourty seconds, it hangs the file, naturally enough.
I planned for that, as the design calls for that display to be display only.
I figured that the program running there could open the file in
non-exclusive read only mode, and there would be no problem.

However, I have not been able to open the file in such a way that it does
not lock out other users.  I get a status 93 on opening the file from any
other source whenever that program is running, regardless of how I open it.
I have tried each of the lock modes, plus the default.
I have tried unlocking the file immediately after opening it.  I have tried
changing all the reads to read-with-no-lock. The only way I seem to be able
to have both sources open it is by having both open it in input mode.  As
far as I know, a file opened in input mode only should be invisible to file
locking as long as the all_files_exclusive switch is not set (and it is
not).

Next step was to write a short test program to play with.  The DAMNED THING
WORKED right!  I removed the test FD, and substituted the real file.  It
reverted to exclusive mode only.  The only difference between the test file
and the real one is that the real one has multiple keys, and uses a split
key.

If anybody has any suggestions, I would appreciate it.
```

#### ↳ Re: file status woes

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3793c4ee.156785106@news1.ibm.net>`
- **References:** `<7n0db6$shn$1@news.igs.net>`

```
Posted and mailed.

On Mon, 19 Jul 1999 19:49:23 -0400, "donald tees"
<donald@willmack.com> wrote:

Simple tutorial:

Lock Mode Exclusive - 

in "General" - multiple programs can open the file input and read.
Single program can Open I-O - (for update) - but ONLY if No other
programs have it open for Read.

I question the need for exclusive file acces.  Why not make it "lock
mode is automatic".  You get record locking and anyone/everyone can
open/read/update.  

I am assuming there is SOME need for exclusive access.
```

##### ↳ ↳ Re: file status woes

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n0nn3$5a1$1@news.igs.net>`
- **References:** `<7n0db6$shn$1@news.igs.net> <3793c4ee.156785106@news1.ibm.net>`

```
Thane Hubbell wrote in message

>I question the need for exclusive file acces.  Why not make it "lock
>mode is automatic".  You get record locking and anyone/everyone can
>open/read/update.
>
>I am assuming there is SOME need for exclusive access.


If I were writing the code today, I would use record locking.
Unfortunately, it was converted to a PC in 1982-3, and the record locking
did not work.  At that time I converted it to full file-locking. The way it
was written/tested at that time, I was able to have users in input only, but
only a single user at a time open in I-O mode.  I hesitate to change that
because the code is somewhat dirty, and though all file I/O is in copies
(theoretically) I have seventy or eighty programs to re-test if I change the
file locking significantly.
```

#### ↳ Re: file status woes

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3793c67e.157185201@news1.ibm.net>`
- **References:** `<7n0db6$shn$1@news.igs.net>`

```
Posted and mailed.

On Mon, 19 Jul 1999 19:49:23 -0400, "donald tees"
<donald@willmack.com> wrote:

>I have a file sharing problem that I would like to share (and cannot, which
>is the problem in a nutshell).

Donald - I think I've solved this.  It's a question of defaults.  With
MicroFocus (your old language) not specifying a lock mode gave you
lock mode "Automatic" - which is shared access for Input and I-O, with
Fujitsu not specifying the lock mode defaults to lock mode EXCLUSIVE.
Try Lock Mode is Automatic and I bet it works now.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
