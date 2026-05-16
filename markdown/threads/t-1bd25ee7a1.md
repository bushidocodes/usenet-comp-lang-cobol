[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL integration with TCP/IP and/or Java (long)

_20 messages · 9 participants · 2003-07_

---

### COBOL integration with TCP/IP and/or Java (long)

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-07-22T11:58:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>`

```
Greetings,

I am a complete COBOL novice, so please be patient.  I learned a small 
amount of COBOL in high school computer science, but have had little 
opportunity to explore it any further.  I'll admit to a certain 
chauvinism regarding the language.  After a few days reviewing the COBOL 
world, I now see the error of my ways.  It looks like COBOL is still a 
vibrant part of true enterprise computing.

Anyway, because of a small amount of OS/390 experience I have, I'm 
suddenly in charge of figuring out how to hook up a client-server Java 
API to a third-party app that runs on the 390.  This third-party tool 
has a public event and API mechanism we intend to hook into as part of 
the integration.  These events are intended to be accessed via 390 
assembler or COBOL.

We chose COBOL, so I needed to do a crash-course in COBOL, and figure 
out how to make sense of this public API.  I have all the API docs, as 
well as the relevant IBM PDFs describing the language.

Anyway, I'm not intending on this newsgroup to do my work for me.  I've 
mapped out a pretty high-level view of how we intend to get the COBOL 
information into a Java "adapter" that speaks to our own Java API.

I was hoping to treat the stuff we get out of the COBOL side as fixed 
strings, and send them to the Java adapter in some manner.  The problem 
is that I'm not entirely sure how to go about this.  I understand that I 
can invoke Java methods from IBM's 390 COBOL, but I was hoping to be 
able to just send the strings via TCP/IP to the adapter, which then does 
not have to run in a local JVM.  The adapter may have to, as part of the 
event model, call back to the COBOL API to complete it's work.

I just don't know how or if COBOL can speak TCP/IP.  Heck, I'm not sure 
how to get it to talk to a file at this point (I've played around with 
the Fujitsu COBOL compiler on Win32, and can at least get a "Hello 
World" working).  My assumption is that COBOL completely abstracts i/o 
and depends on the underlying environment for resources of this kind, 
but I'm unsure how that mechanism works.  I'm further assuming I have to 
do this in the DATA DIVISION.

Is this the wrong approach?  Can I depend on TCP/IP services at some 
level?  Is JNI more appropiate for this use?  I don't really need tight 
intercommunication between the COBOL and Java adapter -- I'm hoping to 
create one big COBOL program that just grabs the strings I need and 
fires them off to the Java adapter, which will do the rest.

I notice that IBM COBOL supports JNDI, but I _really_ don't want to use 
EJBs or ORB.  The idea is to make this initial adapter part cheap and 
fast -- it doesn't have to be smart at all, as our own API has all the 
intelligence.

I'm continuing to work through a book I found ("Fundamentals of 
Structured COBOL Programming") and reviewing the terse IBM docs.  As 
I've said, I'm a complete COBOL novice, so please be kind if my 
assumptions are off base.  Any ideas or suggestions appreciated.

-- cm
```

#### ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-22T17:17:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>`

```
clvrmnky<clvrmnky@coldmail.com.invalid> 07/22/03 09:58AM >>>
>Greetings,
>
…[52 more quoted lines elided]…
>assumptions are off base.  Any ideas or suggestions appreciated.

While COBOL as a language in and of itself does not support TCP/IP, neither
does C.  Both use calls to the appropriate TCP/IP API.  What I'm getting at
is, yes, you can do TCP/IP programming with COBOL.  I have done so myself,
to great success.

Anyway, in the MVS world you would want to use what are called EZASOKET
calls.  The EZASOKET calls are fairly similar to the standard BSD/C TCP/IP
calls (socket, bind, connect, send, receive, close, etc.)  A good manual for
this is the IP Application Programming Interface Guide.  Try:
http://publibz.boulder.ibm.com/epubs/pdf/f1af2031.pdf.  There's probably
more recent versions out there, but I don't feel like looking at the moment!
 :-)

Anyway, one big question I have is will the COBOL application on the
mainframe be a batch program or a CICS program?  I hope it's CICS, because
it seems to me that doing it under batch would require some sort of
multi-threading, and I don't know that COBOL supports that.

Well, actually, maybe not.  Is the OS/390 COBOL program going to be the
client or the server?  If the client, it should be fairly easy whether it's
CICS or batch.  Just have the COBOL program create a socket and do a connect
to the server; then send the request, receive the response and close the
socket.  Of course you'd need to agree on a 'message format'.  Meaning, are
the messages to be in EBCDIC or ASCII?  (Probably the latter... you can use
some subroutines from the above manual to do the conversion).  Are you
always going to send messages of the same size?  If not, you need to agree
on how you determine the end of the message.  Myself, I prefer a 'message
header' which gives the length of the message.  You can also use some sort
of delimiter (CR/LF/NL/NUL whatever...).

Anyway, hope this has helped a bit.  Feel free to ask more questions. 
Basically, if you are able to do Java to Java calls using the regular Socket
and ServerSocket classes, then using COBOL EZASOKET calls should be at least
somewhat similar.  In fact, since Java is your main language you may want to
write a simple Java client to connect to your Java server and simulate what
a "COBOL to Java" session would do.  This way you could make sure that your
Java server (I'm assuming that the Java application will be the server) is
working.  Then you can code the COBOL client to interact with a Java server
that you know is working.

Oh, as for file access, yes COBOL has 'built in' access to several file
types (sequential, indexed, etc.).  See FILE-CONTROL and FILE SECTION in
your manuals.  (Well, manuals won't really teach you COBOL, but anyway...)


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

##### ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-07-23T04:54:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ByoTa.1798$BB6.56442@twister.tampabay.rr.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de>`

```
> Anyway, one big question I have is will the COBOL application on the
> mainframe be a batch program or a CICS program?  I hope it's CICS, because
> it seems to me that doing it under batch would require some sort of
> multi-threading, and I don't know that COBOL supports that.

IBM Enterprise COBOL does support running in threads under USS.  I don't
believe COBOL is multithreaded itself but will not have a problem running in
a C or JAVA process ..there is a new THREAD compile option and certain
criteria that must be met such as being reentrant with attention paid to
working versus local storage (obviously).

JCE
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-23T09:33:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfm9t0$g0039$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <ByoTa.1798$BB6.56442@twister.tampabay.rr.com>`

```
jce<defaultuser@hotmail.com> 07/22/03 10:54PM >>>
>> Anyway, one big question I have is will the COBOL application on the
>> mainframe be a batch program or a CICS program?  I hope it's CICS,
because
>> it seems to me that doing it under batch would require some sort of
>> multi-threading, and I don't know that COBOL supports that.
>
>IBM Enterprise COBOL does support running in threads under USS.  I don't
>believe COBOL is multithreaded itself but will not have a problem running
in
>a C or JAVA process ..there is a new THREAD compile option and certain
>criteria that must be met such as being reentrant with attention paid to
>working versus local storage (obviously).

I thought something like that might be the case.  We are a VSE shop so
that's not available.  I don't think there's any such thing as a thread
under VSE.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

##### ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-07-23T13:29:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>`
- **In-Reply-To:** `<bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick wrote:

[...]
> Anyway, one big question I have is will the COBOL application on the
> mainframe be a batch program or a CICS program?  I hope it's CICS, because
> it seems to me that doing it under batch would require some sort of
> multi-threading, and I don't know that COBOL supports that.
>
This is the part I'm unclear on.  I don't know (yet) if the third-party 
app runs under CICS or JCL (if that is the correct reference).  I'm 
hoping to find this out tomorrow.  I've read about CICS, but I'm unclear 
on what it _actually_ is, other than it seems to offer sockets.  More 
homework required.

> Well, actually, maybe not.  Is the OS/390 COBOL program going to be the
> client or the server?  If the client, it should be fairly easy whether it's
…[9 more quoted lines elided]…
>
The third-party app is a server, which needs to communicate with our 
server.  We will utilize an event model and public API available to us 
to facilitate a specific set of actions and shared data.

As far as details go, I'm hoping to just use fixed-length strings as 
they come out of the app, and send those verbatim to the Java side.  Any 
charset conversion (if needed) will happen in the Java adapter.

Thanks for the pointers.

-- cm
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-23T22:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c35165$c7169ac0$0593f243@chottel>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>`

```
You might want to use www.google.com to search newsgroup
bit.listserv.ibm-main wher I have seen posts on COBOL and TCP/IP.

clvrmnky <clvrmnky@coldmail.com.invalid> wrote in article
<1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>...
> Frank Swarbrick wrote:
> 
> [...]
> > Anyway, one big question I have is will the COBOL application on the
> > mainframe be a batch program or a CICS program?  I hope it's CICS,
because
> > it seems to me that doing it under batch would require some sort of
> > multi-threading, and I don't know that COBOL supports that.
…[8 more quoted lines elided]…
> > client or the server?  If the client, it should be fairly easy whether
it's
> > CICS or batch.  Just have the COBOL program create a socket and do a
connect
> > to the server; then send the request, receive the response and close
the
> > socket.  Of course you'd need to agree on a 'message format'.  Meaning,
are
> > the messages to be in EBCDIC or ASCII?  (Probably the latter... you can
use
> > some subroutines from the above manual to do the conversion).  Are you
> > always going to send messages of the same size?  If not, you need to
agree
> > on how you determine the end of the message.  Myself, I prefer a
'message
> > header' which gives the length of the message.  You can also use some
sort
> > of delimiter (CR/LF/NL/NUL whatever...).
> >
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-24T01:48:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-5A6B82.01481524072003@corp.supernews.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>`

```
In article <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>,
 clvrmnky <clvrmnky@coldmail.com.invalid> wrote:

> Frank Swarbrick wrote:
> 
…[10 more quoted lines elided]…
> homework required.

CICS fits the same problem space as the http server does on little 
computers.  It is a transaction server that is tuned to satisfy many 
small, concurrent, requests from various sources.

It manages all machine resources used within said problem space, to 
include threads, files and database connections, for maximum throughput.
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-24T13:16:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca>`

```

"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:1CzTa.45388$PD3.4483594@nnrp1.uunet.ca...
| Frank Swarbrick wrote:
|
| [...]
| > Anyway, one big question I have is will the COBOL application on the
| > mainframe be a batch program or a CICS program?  I hope it's CICS,
because
| > it seems to me that doing it under batch would require some sort of
| > multi-threading, and I don't know that COBOL supports that.
…[5 more quoted lines elided]…
| homework required.

CICS has a TCP/IP listener to receive incoming messages.
You might want to start your homework there.
It's been a couple of years since I looked at the CICS TCP/IP manuals.
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 4)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-24T09:42:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfoup9$hajf9$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley<dennis.harleyNoSpam@worldnet.att.net> 07/24/03 07:16AM >>>
>
>"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
…[18 more quoted lines elided]…
>It's been a couple of years since I looked at the CICS TCP/IP manuals.

From what I can tell from the original description of the situation the
mainframe COBOL application will act as a client, not a server, and thus the
CICS listener would not fit in to the equation.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 5)_

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-07-24T14:29:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BAVTa.45747$PD3.4488810@nnrp1.uunet.ca>`
- **In-Reply-To:** `<bfoup9$hajf9$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick wrote:

> Harley<dennis.harleyNoSpam@worldnet.att.net> 07/24/03 07:16AM >>>
[...]
>>CICS has a TCP/IP listener to receive incoming messages.
>>You might want to start your homework there.
…[6 more quoted lines elided]…
> 
Well, I've determined that we have TCP/IP libraries available to us on 
the target system, and I now have Redbook details on using the 
Communication Server extended sockets.

Our COBOL is going to be driven by, and will run in the environment of, 
the third-party tool we are integrating with.  It will take care of 
loading and invoking my COBOL programs for us.  This will allow us to 
open up a socket to a Java listener on demand and pass a string to the 
Java part, which will do the necessary magic to talk to our API.

This is really a server-to-server integration, but our server is 
essentially slaved to the 390 application.  I've got an example COBOL 
app that simulates being called from the event, and writes it's data out 
to a file (well, the display right now, as I may not be able to count on 
a "file" as I'm used to talking about it).

Lots of work to do yet, and I'm still fuzzy on "levels" and how I need 
to use them to describe my various file bits, but I'm learning.

Thanks to the group for all your help.  I have to put my head down now 
and hack up a prototype.

-- cm
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 6)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-24T17:27:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfpq0k$ggsn1$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de> <BAVTa.45747$PD3.4488810@nnrp1.uunet.ca>`

```
clvrmnky<clvrmnky@coldmail.com.invalid> 07/24/03 12:29PM >>>>Frank Swarbrick
wrote:
>
>> Harley<dennis.harleyNoSpam@worldnet.att.net> 07/24/03 07:16AM >>>
…[7 more quoted lines elided]…
>> mainframe COBOL application will act as a client, not a server, and thus
the
>> CICS listener would not fit in to the equation.
>> 
…[20 more quoted lines elided]…
>and hack up a prototype.

Well, it's server to server in that both applications are servers.  But in
your specific case, one of the servers must act as a client.  Speaking
strictly within the TCP/IP paradigm, two server processes cannot talk to
each other.  This is because a TCP/IP server process by definition waits
passively for connections, while clients actively attempt to establish a
connection (to a server).  There is nothing to say that a process cannot be
both a client and a server (I have such a process).

To give a specific example, we have an internet banking server.  When this
server needs information from the mainframe it functions as a client and
establishes a connection to a server process running on the mainframe.  It
then sends a request and gets a response.  This doesn't make the internet
banking server any less of a server.  It just also makes it a client as
well.

As for your logic, you probably can think of it in terms of writing to a
file.  In the file situation the COBOL program would do the following:

OPEN the file
WRITE the record to the file
CLOSE the file

Your socket stuff will be pretty much the same:

Create a SOCKET
CONNECT the socket to a server
(these first two are basically your OPEN step)
SEND the record on the socket
CLOSE the socket




--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 6)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-26T05:42:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307260442.175a1df0@posting.google.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de> <BAVTa.45747$PD3.4488810@nnrp1.uunet.ca>`

```
Email me privately at thane at softwaresimple.com if you are
interested in making a deal on some COBOL IP Socket code that uses
EZASOCKET calls and works quite well under OS/390.

clvrmnky <clvrmnky@coldmail.com.invalid> wrote in message news:<BAVTa.45747$PD3.4488810@nnrp1.uunet.ca>...
> Frank Swarbrick wrote:
> 
…[33 more quoted lines elided]…
> -- cm
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-29T12:24:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ItVa.75565$3o3.5164924@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bfoup9$hajf9$1@ID-184804.news.uni-berlin.de...
| Harley<dennis.harleyNoSpam@worldnet.att.net> 07/24/03 07:16AM >>>
| >
…[13 more quoted lines elided]…
| >| hoping to find this out tomorrow.  I've read about CICS, but I'm
unclear
| >| on what it _actually_ is, other than it seems to offer sockets.  More
| >| homework required.
…[6 more quoted lines elided]…
| mainframe COBOL application will act as a client, not a server, and thus
the
| CICS listener would not fit in to the equation.

Yes, it would.
Messages go between the client & server.
The client starts the conversation.
The server replies.
Guess what handles the reply message coming from the server.

AND I said the CICS Listener is a good place to start research.
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 6)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-29T12:24:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg6e59$lm5uh$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de> <7ItVa.75565$3o3.5164924@bgtnsc05-news.ops.worldnet.att.net>`

```
Harley<dennis.harleyNoSpam@worldnet.att.net> 07/29/03 06:24AM >>>
>
>"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
…[8 more quoted lines elided]…
>| >| > Anyway, one big question I have is will the COBOL application on
the
>| >| > mainframe be a batch program or a CICS program?  I hope it's CICS,
>| >because
…[3 more quoted lines elided]…
>| >| This is the part I'm unclear on.  I don't know (yet) if the
third-party
>| >| app runs under CICS or JCL (if that is the correct reference).  I'm
>| >| hoping to find this out tomorrow.  I've read about CICS, but I'm
…[17 more quoted lines elided]…
>Guess what handles the reply message coming from the server.

Umm, the CICS client task that started the conversation.  Not the CICS
Listener.  We may be getting our terminology mixed up.  As far as I know,
all the CICS Listener does is waits for connections *from* clients and then
STARTs a new CICS task to handle the actual conversation.  Well, I guess it
does 'listen' for an initial message so it knows which CICS task to START.

If a CICS task is a TCP/IP client then it would do the connect, sends,
receives, and close all within the same task.  The CICS Listener would not
be involved.

>AND I said the CICS Listener is a good place to start research.

Perhaps, but I think in this case it would just be confusing.  You state in
your original message "CICS has a TCP/IP listener to receive incoming
messages".  It might be better to say "CICS has a TCP/IP listener to receive
incoming requests".  An incoming would consist, in this case, of both the
initial connection request and the initial request message.  

It is quite possible for the task started by the listener to consist of many
messages flowing in both directions.  In other words, a client could connect
to the CICS listener and then send "ABCD".  The CICS listener would start
tran ABCD.  ABCD might then send something like "OK" and then do a receive,
waiting for the client to send some more data.  The client might send
"2929292" and the CICS task (not the listener but tran ABCD) would receive
it and maybe send back the current balanace of 2929292.  The client, if it
had another account it wanted the balance on, would send another account
number.  This could go back and forth for many accounts.  Finally the client
would determine it's done and might send "DONE" instead of an account
number.  The server might then send "OK BYE" and close the connection.  Then
the client would receive this and close its side of the connection.

Yes, I've gone beyond the original issue.  I just wanted to clarify
(hopefully!) what the CICS Listener does and does not do.  The Listener is
only involved in the original connection establishment and receipt of the
first 'request'.  After that it is not involved in the remainder of the
conversation.  And it is not at all involved when a CICS task behaves as the
TCP/IP client. 

This is my understanding from what I've read in the documentation.  Of
course you may have an example that proves me wrong.  I'd like to hear it,
if that's the case.





--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-29T19:18:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pMzVa.75942$3o3.5193598@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <bfkgmm$f0abh$1@ID-184804.news.uni-berlin.de> <1CzTa.45388$PD3.4483594@nnrp1.uunet.ca> <4%QTa.70534$0v4.4710245@bgtnsc04-news.ops.worldnet.att.net> <bfoup9$hajf9$1@ID-184804.news.uni-berlin.de> <7ItVa.75565$3o3.5164924@bgtnsc05-news.ops.worldnet.att.net> <bg6e59$lm5uh$1@ID-184804.news.uni-berlin.de>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bg6e59$lm5uh$1@ID-184804.news.uni-berlin.de...
| Harley<dennis.harleyNoSpam@worldnet.att.net> 07/29/03 06:24AM >>>
| >
…[13 more quoted lines elided]…
| >| >| > it seems to me that doing it under batch would require some sort
of
| >| >| > multi-threading, and I don't know that COBOL supports that.
| >| >| >
…[5 more quoted lines elided]…
| >| >| on what it _actually_ is, other than it seems to offer sockets.
More
| >| >| homework required.
| >| >
…[5 more quoted lines elided]…
| >| mainframe COBOL application will act as a client, not a server, and
thus
| >the
| >| CICS listener would not fit in to the equation.
…[9 more quoted lines elided]…
| all the CICS Listener does is waits for connections *from* clients and
then
| STARTs a new CICS task to handle the actual conversation.  Well, I guess
it
| does 'listen' for an initial message so it knows which CICS task to START.

As I said, the Listener is the place to start your research.

http://www-1.ibm.com/servers/eserver/zseries/os/vse/pdf3/tcp15/iestce30.pdf

Check out Page 416.
The Client CICS TCP/IP Application
It's in Chapter 17.CICS Listener Programming Considerations

END OF MY COMMENTS.

|
| If a CICS task is a TCP/IP client then it would do the connect, sends,
…[5 more quoted lines elided]…
| Perhaps, but I think in this case it would just be confusing.  You state
in
| your original message "CICS has a TCP/IP listener to receive incoming
| messages".  It might be better to say "CICS has a TCP/IP listener to
receive
| incoming requests".  An incoming would consist, in this case, of both the
| initial connection request and the initial request message.
|
| It is quite possible for the task started by the listener to consist of
many
| messages flowing in both directions.  In other words, a client could
connect
| to the CICS listener and then send "ABCD".  The CICS listener would start
| tran ABCD.  ABCD might then send something like "OK" and then do a
receive,
| waiting for the client to send some more data.  The client might send
| "2929292" and the CICS task (not the listener but tran ABCD) would receive
| it and maybe send back the current balanace of 2929292.  The client, if it
| had another account it wanted the balance on, would send another account
| number.  This could go back and forth for many accounts.  Finally the
client
| would determine it's done and might send "DONE" instead of an account
| number.  The server might then send "OK BYE" and close the connection.
Then
| the client would receive this and close its side of the connection.
|
…[4 more quoted lines elided]…
| conversation.  And it is not at all involved when a CICS task behaves as
the
| TCP/IP client.
|
…[11 more quoted lines elided]…
| FirstBank Data Corporation
```

#### ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-07-23T05:42:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lfpTa.2174$BB6.59324@twister.tampabay.rr.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>`

```
> world, I now see the error of my ways.  It looks like COBOL is still a
> vibrant part of true enterprise computing.
Woo hoo....

> We chose COBOL
Why? Isn't assembler that much easier ;-)

> I was hoping to treat the stuff we get out of the COBOL side as fixed
> strings, and send them to the Java adapter in some manner.  The problem
…[4 more quoted lines elided]…
> event model, call back to the COBOL API to complete it's work.
You can write a cobol program that is called from Java
You can write a cobol program that calls Java.
This would require Enterprise Cobol and writing OO Cobol to run under USS.
There is also limited XML support which might be appropriate here depending
on what you are doing...it might not.

The new COBOL reference is here (type in COBOL in the search ....bookmark
this page):
http://publibz.boulder.ibm.com/cgi-bin/bookmgr/LIBRARY

If you have a nice middleware like MQ Series then you could use that as a
message transport which would give you a nice easy way to get disparate
systems to communicate without the hassle of TCPIP.

> I'm continuing to work through a book I found ("Fundamentals of
> Structured COBOL Programming") and reviewing the terse IBM docs.
The COBOL Application guide has a lot of detail I thought.
You could try looking at redbooks.  Most of these focus on Websphere
products but may help a little.

> Any ideas or suggestions appreciated.
Having rethought this I am confused by your overall architecture...what's
the client and what's the server...are you calling the S390 program
remotely? Who initiates what?

If you are trying to get information out of the cobol program from the Java
API on a remote system - you could look at the Redbook called Websphere
Version 5 Web Services Handbook for ideas of how to access legacy data (even
with its Websphere slant)

JCE
```

##### ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-07-23T13:21:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OuzTa.45376$PD3.4483628@nnrp1.uunet.ca>`
- **In-Reply-To:** `<lfpTa.2174$BB6.59324@twister.tampabay.rr.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <lfpTa.2174$BB6.59324@twister.tampabay.rr.com>`

```
jce wrote:

[...]
>>Any ideas or suggestions appreciated.
> 
…[3 more quoted lines elided]…
> 

Well, the client-server stuff is pretty remote from what I'm doing.

We have a third-party app that runs on the 390 which has an event model. 
  When something of interest happens in the app, it has the facility to 
run external COBOL or 390 assembler routines.

The plan is to make pretty simple (read: stupid) COBOL routines that 
simply take the data available to it (lots of hand-waving here) from the 
third-party app (when run via the event model), and send that to a Java 
adapter, which will properly speak with our Java API.  The Java adapter 
does all the real work.  Our API talks with our server app, and can act 
as a "proxy" client in the absence of our true client (this facilitates 
server-server integration, which is all that is required in this case).

I'm not sure about the other way: the third-party app has a public API 
that is probably also accessed via COBOL, but I haven't gone down that 
path, yet.

I'm trying to stay away from JNI and/or EJBs; mostly to keep things 
simple and fast.  We also do not want to depend on a JVM on the 390 
side.  This approach also makes it dead easy to setup a test harness 
without having the third-party app or the COBOL pieces present, as we 
can just feed strings into the Java adapter that correspond to the 
application events.  To be perfectly honest, COBOL is a minimal part of 
what we need to do, but it is required.  We are trying to minimize the 
COBOL we have to develop and maintain, as we are not a very COBOL smart 
shop.

Hope this clarifies what I'm trying to do.  The pointers in all the 
replies have given me a lot to chew on.  The next step is finding out 
the environment (if that is the correct word) the third-part app runs 
in.  I understand that "CICS" provides socker communication, but I'm 
unsure how CICS fits in to our situation, or if it is even present.

-- jdv
```

###### ↳ ↳ ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-23T12:30:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfmk8t$gcues$1@ID-184804.news.uni-berlin.de>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca> <lfpTa.2174$BB6.59324@twister.tampabay.rr.com> <OuzTa.45376$PD3.4483628@nnrp1.uunet.ca>`

```
clvrmnky<clvrmnky@coldmail.com.invalid> 07/23/03 11:21AM >>>
>jce wrote:
>
…[3 more quoted lines elided]…
>> Having rethought this I am confused by your overall
architecture...what's
>> the client and what's the server...are you calling the S390 program
>> remotely? Who initiates what?
…[34 more quoted lines elided]…
>unsure how CICS fits in to our situation, or if it is even present.

CICS does not provide socket communication in and of itself.  The socket API
can be used within CICS applications.  The socket API also can be used with
regular batch applications.

It sounds to me like you would want to third party app to function as a
client.  When an event occurs your 'external routine' would connect to your
Java adapter, send the data, perhaps wait for some sort of acknowledgement
from the Java adapter (or perhaps not), close the socket and return.

Your Java adapter (I don't even know what that means, honestly) would have
to be related to some sort of server application.  The server would wait for
a connection from your 390 client.  When one is received it would receive
the incoming message, do whatever it needs to do, close the socket and
return.

I don't think it makes much difference if your 390 application runs under
CICS or not.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

#### ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2003-07-23T00:18:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0307222318.124e7931@posting.google.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>`

```
Did you try PERCobol von legacyJ ( www.legacyj.com ) ?

clvrmnky <clvrmnky@coldmail.com.invalid> wrote in message news:<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>...
> Greetings,
> 
…[5 more quoted lines elided]…
> vibrant part of true enterprise computing.
```

#### ↳ Re: COBOL integration with TCP/IP and/or Java (long)

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-23T08:28:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3141990.1058948920@dbforums.com>`
- **References:** `<3bdTa.44959$PD3.4478855@nnrp1.uunet.ca>`

```

I'm not sure if this is helpful or not, bur Fujitsu have customers who
use the IBM Transaction Gateway to Access CICS on the mainframe via
TCP/IP from PC Client machines. Here's a link:

http://www-3.ibm.com/software/htp/cics/ctg/

I do believe however, that they use a version 3 product for this and the
product link above is for a version 5 product.

There are also .NET classes that will allow you easily to use TCP/IP
from a COBOL program if you have Fujitsu's .NET Compiler...

Good Luck,
-Howard
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
