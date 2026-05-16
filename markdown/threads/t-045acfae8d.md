[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol, hardware hooks and message queues

_6 messages · 4 participants · 2000-02_

---

### cobol, hardware hooks and message queues

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com>`

```
cobol is a pain when it comes to windows. windows currently is
non-preemptive, so i don't know if thread divisions work, and it has
messages and hardware hooks sitting above drivers.

is it possible to build an ISP and client in cobol which works on
non-preemptive scheduling?

if you only work on the client side, though, then example code
pertaining to getmessage function (that waits until a message, ie,
data) connected to a winsock port might be useful (plus the additional
gethost and other functions).

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: cobol, hardware hooks and message queues

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38b156de_1@news1.prserv.net>`
- **References:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com>`

```
Our company has an application that utilizes TCP/IP communications
(blocking calls) written in Micro Focus COBOL.  MF Cobol allows you to
interface with the Winsock API to perform these functions.  We also
utilize windows message queue functions in these programs, such as
SendMessage, PeekMessage, and PostMessage.  MF Workbench v4.0 and
NetExpress easily interface with the Win32 API.  Our applications run on
Win95/98/NT - haven't tested them on the new 2000 yet.
```

#### ↳ Re: cobol, hardware hooks and message queues

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B12B94.DE8F3EE9@zip.com.au>`
- **References:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com>`

```
G Moore wrote:
> 
> cobol is a pain when it comes to windows. windows currently is
> non-preemptive, so i don't know if thread divisions work, and it has
> messages and hardware hooks sitting above drivers.

Windows is certainly pre-emptive since NT / 95.  Cobol might not be
threaded depending upon your vendor.  Threading is in the windows API
I do not know how to use this and how is works with Cobol though.

I have never worked with windows sockets but I can be reasonably
certain that there are blocking and not blocking get message calls. 
Non blocking returns a failed status fairly quickly.

You would spawn a copy of you program and call that copy to do a
blocked wait, not threaded but 'forked'.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: cobol, hardware hooks and message queues

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1mh3bscfsgo2l3iobtifdabtooeqfdlmbs@4ax.com>`
- **References:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com> <38B12B94.DE8F3EE9@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>> cobol is a pain when it comes to windows. windows currently is
>> non-preemptive, so i don't know if thread divisions work, and it has
>> messages and hardware hooks sitting above drivers.

>Windows is certainly pre-emptive since NT / 95.  Cobol might not be
>threaded depending upon your vendor.  Threading is in the windows API
>I do not know how to use this and how is works with Cobol though.

oh, i was relying on my winsock for windows 3.11 help file. it talked
about non-preemptive windows. i knew nt was, but not 95. i could
check.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: cobol, hardware hooks and message queues

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Duxs4.4907$Wv2.60992@news2.mia>`
- **References:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com> <38B12B94.DE8F3EE9@zip.com.au> <1mh3bscfsgo2l3iobtifdabtooeqfdlmbs@4ax.com>`

```
G Moore wrote:
>Ken Foskey  wrote:
>>Windows is certainly pre-emptive since NT / 95.  Cobol might not be
…[5 more quoted lines elided]…
>check.

Actually, Windoes 3.1 is preemptive for DOS tasks.  It's easy enough
verify.  Just write a little QBasic program, something like this:

  DO
    I& = I& + 1
    PRINT I&;
  LOOP

Then run the program in several DOS windows and watch. :-)
```

###### ↳ ↳ ↳ Re: cobol, hardware hooks and message queues

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ingbs0shtinega4f0k4cc2mmi1h23il5t@4ax.com>`
- **References:** `<50o0bskl59b06a1cb3f7ps2g4qvmkfe2nl@4ax.com> <38B12B94.DE8F3EE9@zip.com.au> <1mh3bscfsgo2l3iobtifdabtooeqfdlmbs@4ax.com>`

```
G Moore <gvwmoore@spam.ix.netcom.com> wrote:

>Ken Foskey <waratah@zip.com.au> wrote:
>
…[10 more quoted lines elided]…
>check.


page 84, the essential client/server guide, second edition, by orfali
says:

Second, Windows 95 is still built on DOS; it is DOS with a pretty
face. This means that 16-bit applications have no crash proection, and
only have limited multi-tasking (it is not pre-emptive).


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
