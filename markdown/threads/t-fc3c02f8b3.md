[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Asyncronis processing using net express

_5 messages · 3 participants · 2000-04_

---

### Asyncronis processing using net express

- **From:** Craig <cyonkeNOcySPAM@sentry-direct.com.invalid>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<07ce3af4.fc040e72@usw-ex0103-019.remarq.com>`

```
We would like to know if anyone could assist us with our 32-bit
internet programming efforts.  We're using Merant Net Express
and hoping that someone may have some experience with this type
of process and type of code we're attempting to write.

We're putting together a process that opens an internet
connection, establishes a SSL (secure) connection to a HTTP
server, and performs a variety of file operations (get, put,
delete) - using Microsoft's WININET APIs provided with the
Internet Explorer browser.  We've written functional code that
does everything that we need to do synchronously (cbl pgm waits
until each call is complete, and no other functions can take
place during that time).

In order to prevent very long wait or hang situations, we're
writing the process to perform the internet functions
asynchronously so that we're able to monitor call status and be
able to shut down a task if our timeout limit is exceeded.  This
is proving to be quite complex and difficult, as all examples
(MSDN Online Web Workshop & elsewhere) and discussion (present
on Deja.com) found in exhaustive web searching lack the detail
we need and show that programmers writing these processes
primarily do so with the C language.  I've been unable to find
any examples on MF's site, and have not come across mention
anywhere of anyone doing this in MF Cobol.

If a more detailed description of our process and complete
working synchronous (as well as incomplete asynchronous) code is
necessary, I would be happy to provide it.

Any assistance would be greatly appreciated.

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Asyncronis processing using net express

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0a650e28.72a71562@usw-ex0101-005.remarq.com>`
- **References:** `<07ce3af4.fc040e72@usw-ex0103-019.remarq.com>`

```
This may be a good question for AnswerLab. Have you requested
information from Merant? If not, put a question on AnswerLab.

Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

##### ↳ ↳ Re: Asyncronis processing using net express

- **From:** Craig <cyonkeNOcySPAM@sentry-direct.com.invalid>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0e022795.2d625ab9@usw-ex0103-019.remarq.com>`
- **References:** `<07ce3af4.fc040e72@usw-ex0103-019.remarq.com> <0a650e28.72a71562@usw-ex0101-005.remarq.com>`

```
Already have posted to the answerlab and I received the response
that they are not familiar with the particular api's that we are
trying to use.
In article <0a650e28.72a71562@usw-ex0101-005.remarq.com>, Rich
Rohde <richNOriSPAM@richware.net.invalid> wrote:
>This may be a good question for AnswerLab. Have you requested
>information from Merant? If not, put a question on AnswerLab.
…[3 more quoted lines elided]…
>* Sent from RemarQ http://www.remarq.com The Internet's
Discussion Network *
>The fastest and easiest way to search and participate in Usenet
- Free!
>
>


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Asyncronis processing using net express

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3908cfa7_4@news1.prserv.net>`
- **References:** `<07ce3af4.fc040e72@usw-ex0103-019.remarq.com>`

```
We do something similar to this, but are connecting up to an MVS server
that I wrote in Assembler.  Basically it has a main task that simply
listens on a specific port, and then hands the incoming request off to a
waiting subtask for service.  Each client contacts the main "listener"
task, drops the connection, and then waits for the server subtask to
contact back.

We do the same thing with a Windows version, just doing a "Listen"
command, and then going through the same process.  If this sounds like
what you are trying to do then e-mail me off-line and I will see if I
can't send you some code.  The client pieces all work using Workbench,
NetExpress, or MFE, as well as the Windows version of the Server task.
The MVS version of the server task is written in Assembler.

TL
```

#### ↳ Re: Asyncronis processing using net express

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3908cfb3_4@news1.prserv.net>`
- **References:** `<07ce3af4.fc040e72@usw-ex0103-019.remarq.com>`

```
We do something similar to this, but are connecting up to an MVS server
that I wrote in Assembler.  Basically it has a main task that simply
listens on a specific port, and then hands the incoming request off to a
waiting subtask for service.  Each client contacts the main "listener"
task, drops the connection, and then waits for the server subtask to
contact back.

We do the same thing with a Windows version, just doing a "Listen"
command, and then going through the same process.  If this sounds like
what you are trying to do then e-mail me off-line and I will see if I
can't send you some code.  The client pieces all work using Workbench,
NetExpress, or MFE, as well as the Windows version of the Server task.
The MVS version of the server task is written in Assembler.

TL
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
