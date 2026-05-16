[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TCP Client Sample Code with Winsock

_21 messages · 10 participants · 2002-09 → 2002-10_

---

### TCP Client Sample Code with Winsock

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-29T22:21:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com>`

```
Argh!  I started out to do something I thought was very simple, and it has turned into a bloody nightmare! 
From a COBOL program, I need to open up a socket, read a webpage, parse the information on the webpage, and construct a display from it. (Not an HTML display, a console based display.) 

Using NetExpress and Fujitsu-3, I have been able to open the doggon socket, but I cannot, for the life of me, seem to get the buffer to send the right size command to the remote web site. Either it will give no reply at all, or by upping the size of the buffer, I can cause a 414 error on the WebServer and get back a nice reply telling me the URI is too long. (At least I know the doggon thing works! :) 

This has to be from Windows I am afraid, so does anyone out there have sample code to do this, or 
even non-sample code they would be willing to share? 

The program opens a socket, sets the connection to port 80 of the remote web server (in this case 205.238.189.192) and issues a command. It then reads the socket until the return code from the receive call is 0. The point that seems to be driving me crazy is this: 


 000277        Send-Data SECTION.
 000278            call win32api "send" using
 000279                    by value SOCKET
 000280                    by reference SendBuf
 000281                    by value CmdSize
 000282                    by value 0  size 4
 000283                    returning WS-Return-Code
 000284            end-call

The CmdSize argument is currently set to the size of the command going out, with a X'0A0D0A0D' 
appended to it. In this particular case the command is: 

GET / HTTP1/.0

And the command size is set to 18.  

Help? 

Thanks 
-Paul
```

#### ↳ Re: TCP Client Sample Code with Winsock

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-09-29T18:51:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0209291751.67d06170@posting.google.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote

> From a COBOL program, I need to open up a socket, read a webpage, parse 
> the information on the webpage, and construct a display from it. (Not an 
> HTML display, a console based display.) 

I do that using Python.  Python has a nice HTML parser class that
makes it quite easy to fetch a page and extract the data.  Use a
WinExec to fire off the Python program and have it write the a results
text file that the Cobol can pick up the data from.
```

##### ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-30T02:16:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YtOl9.42137$121.1090863@twister.austin.rr.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <217e491a.0209291751.67d06170@posting.google.com>`

```
I did that with PERL, but the problem is the program needs to process pretty quickly; and that extra step adds a few seconds to each
display as well as introduces the problems of temporary files under Windows.
Thanks for the advice though. Hopefully someone else will have done this before and will be able to point
out what is going wrong.

-Paul


"Richard" <riplin@Azonic.co.nz> wrote in message news:217e491a.0209291751.67d06170@posting.google.com...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote
>
…[7 more quoted lines elided]…
> text file that the Cobol can pick up the data from.
```

#### ↳ Re: TCP Client Sample Code with Winsock

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-09-30T08:23:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0209300723.148271e9@posting.google.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com>`

```
Paul,

the expert in this is Thane Hubbell, but I haven't seen him here for a
while so I'll do my best <G>.

There are several things I note about your post:

1. Have you checked that the socket connection has defined port 80 and
that the "family" is AF_NET (this is a value of "2" for COBOL...)

2. The CmdSz parameter must be defined as little endian, not
binary...i.e. pic s9(5) comp-5. If I were you, I'd try simply coding
it as a literal 18. If this works, then you have established that the
problem is in your definition of the CmdSz parameter...

3. When it says the URI is too long this usually relates to the
information which follows a URL. For example, if you said:
"http://somewebsite/some.asp?ABC"
the "ABC" would constitute the Uniform Resource Indicators (URI). In
your case there are none and it then encounters x'0d0a0d0a'. While it
is correct that the HTTP header should end with these terminators,I am
not sure that you have sent enough information to get a proper
response. The usual process is to send the command, followed by other
information separated by x'0d0a', then terminated by double CR/LF.

Here's an example:

"GET / HTTP/1.1" & x'0d0a' & "Host: www.vbapi.com" & x'0d0a'& _
		"User-Agent: Winsock-Example-Program" & x'0d0a'& x0d0a

4. Try experimenting with BY VALUE and BY CONTENT on the parameters
that are not obviously strings (strings must ALWAYS be BY REFERENCE
when calling APIs from COBOL), as this is the most frequent cause of
error when coding API calls.

I don't know whether the above will solve your problem but you
certainly won't be any worse off...

Good Luck!

Pete.

PS This is a terrible and painful way to deal with sockets...
Nowadays, it makes sense to use a socket interfacing component (that
takes care of all the API interfacing for you)and simply invoke its
methods. Still, I accept we must all use the tools we have and this is
certainly ONE way to learn about socket programming... (even if it
wouldn't be my choice...<G>)

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:<A1Ll9.40149$8o3.981815@twister.austin.rr.com>...
> Argh!  I started out to do something I thought was very simple, and it 
> has turned into a bloody nightmare! 
…[43 more quoted lines elided]…
> --
```

##### ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-10-01T00:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6X5m9.77179$jG2.4196569@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <b3638c46.0209300723.148271e9@posting.google.com>`

```
    You could check this URL.


http://www.kimsoft.com/api-cobol/api-cobol.htm


    I don't know if he covers this API, but it is worth looking at.





"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:b3638c46.0209300723.148271e9@posting.google.com...
> Paul,
>
…[47 more quoted lines elided]…
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:<A1Ll9.40149$8o3.981815@twister.austin.rr.com>...
> > Argh!  I started out to do something I thought was very simple, and it
> > has turned into a bloody nightmare!
…[43 more quoted lines elided]…
> > --
```

##### ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Editor" <Editor@aboutlegacycoding.commm>
- **Date:** 2002-10-01T11:17:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d99bc8a$1_2@news.teranews.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <b3638c46.0209300723.148271e9@posting.google.com>`

```
Pete,

Thanks for reminding me about Thane.

Thane posted a library of COBOL TCP/IP routines that use WinSock in the FREE
download library of www.aboutleagacycoding.com  It's our third most popular
download.

You have to register to get access to the library, but longtime members of
this forum and About Legacy Coding can vouch for the fact that I NEVER spam
and I never sell or give my address list to anyone.  You can register
without subscribing, but if you subscribe you get just ONE e-mail every two
months notifying you of the new issue.

OH - and Pete has a really good article in this latest issue, just posted
today.
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-10-02T01:38:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y6sm9.51343$Fw2.1437911@twister.austin.rr.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <b3638c46.0209300723.148271e9@posting.google.com> <3d99bc8a$1_2@news.teranews.com>`

```
Thanks Buddy - that sounds exactly like what I need. :)
-Paul


"Editor" <Editor@aboutlegacycoding.commm> wrote in message news:3d99bc8a$1_2@news.teranews.com...
> Pete,
>
…[121 more quoted lines elided]…
>
```

#### ↳ Re: TCP Client Sample Code with Winsock

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-10-01T10:57:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0210010957.58a144f8@posting.google.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com>`

```
Paul - head to http://www.aboutlegacycoding.com and go to their
downloads section.  Get sockets.zip.  The dynamic example works with
NetExpress - and there is a Fujitsu example as well.


"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:<A1Ll9.40149$8o3.981815@twister.austin.rr.com>...
> Argh!  I started out to do something I thought was very simple, and it 
> has turned into a bloody nightmare! 
…[43 more quoted lines elided]…
> --
```

##### ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-10-02T01:49:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sgsm9.51345$Fw2.1440029@twister.austin.rr.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <bfdfc3e8.0210010957.58a144f8@posting.google.com>`

```
Yahoo! This *is* exactly what I needed. Thank you!!! 
Amazing how difficult it is to do anything with Windows.  

-Paul



"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message news:bfdfc3e8.0210010957.58a144f8@posting.google.com...
> Paul - head to http://www.aboutlegacycoding.com and go to their
> downloads section.  Get sockets.zip.  The dynamic example works with
…[49 more quoted lines elided]…
> > --
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** "Editor" <Editor@aboutlegacycoding.commm>
- **Date:** 2002-10-04T10:30:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d9da8ad$1_7@news.teranews.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <bfdfc3e8.0210010957.58a144f8@posting.google.com> <sgsm9.51345$Fw2.1440029@twister.austin.rr.com>`

```
I'm always amazed how little the download area of About Legacy Coding is
used.
COBOLers just don't seem to share code.

Go to any one of dozens of C++, VB or Web development Community sites and
you will find litterally thousands of code snippets, subroutines, utilities
and other helpful downloads.

Is it that our community is too technically fractured?  (i.e. platforms are
to numerous and different to make sharing code reasonable)
Or does COBOL, JCL, etc. simply not lend itself to the sharing of code?
Or is it that we all work for large corporations who frown on our sharing
even snippets of routines of what they view as Company owned code?
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2002-10-05T03:29:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021004232935.01003.00002494@mb-mq.aol.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com>`

```
In article <3d9da8ad$1_7@news.teranews.com>, "Editor"
<Editor@aboutlegacycoding.commm> writes:

>Or is it that we all work for large corporations who frown on our sharing
>even snippets of routines of what they view as Company owned code?

I believe that this might be a major part of the restriction on code sharing.
Most places regardless of size (speaking from limited corporate exposure 
of 6 prior employers of varying size) have proprietary language in their hiring

papers regarding ownership of all code developed by the employee (on or off
the job).
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-10-05T09:17:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D9EADDE.5A5C8FA2@worldnet.att.net>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com>`

```
Sff5ky wrote:
> 
> In article <3d9da8ad$1_7@news.teranews.com>, "Editor"
…[10 more quoted lines elided]…
> the job).

Indeed, every COBOL program in my shop has a copyright notice in the
Identification Division that looks something like this:

       SKIP1
      ****************************************************************
      *SECURITY. 'CONFIDENTIAL                                       *
      *          THIS ITEM CONTAINS INFORMATION AND PROCEDURES       *
      *          WHICH ARE PROPRIETARY TO XXXXXXXXXXXXXXXXXXX        *
      *          INCORPORATED, AND WHICH ARE CONFIDENTIAL.  IT IS    *
      *          PROVIDED WITH THE EXPRESS UNDERSTANDING THAT IT     *
      *          IS TO BE USED ONLY FOR THE BENEFIT OF XXXXXXXX      *
      *          XXXXXXXXXX, AND IS NOT TO BE USED, COPIED OR        *
      *          DISCLOSED FOR ANY OTHER PURPOSE.  ANY AUTHORIZED    *
      *          REPRODUCTION (IN WHOLE OR IN PART) OF THIS          *
      *          MATERIAL MUST BE MARKED WITH THIS LEGEND.'          *
      ****************************************************************

I'm not sure what the legal status would be of any COBOL program I
wrote for my PC at home, completely unrelated to my job.  Do I own
it?  Can I give it away?  I'm not sure.  Curiously enough, I am aware
of at least one instance where my company sold several COBOL source
programs to a competitor.  I doubt they removed the copyright notice.  

There is a similar problem with acquiring free COBOL source code.  If
we didn't write it and didn't pay for it, can we legally use it?  How
would TPTB know whether or not it was any good? 

Obviously, any code that contains a company's business rules can't
easily be shared.  Yet at the same time, my employer has no qualms
about bringing in contract programmers to work on a large project. 
They must learn something about our business, and they might end a
contract with us and take another at a competing company. 
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-06T22:52:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da0adb0_1@Usenet.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net>`

```
This is an interesting point, Arnold.

As a contractor (in the days when I wrote COBOL code for a living) it was
quite usual for each contract to contain a clause stating that all code
written by me on their site remained their intellectual and physical
property. I always crossed it out and explained that I could not sell them
the intellectual property rights to solutions I developed because I would
then be unable to use the same solution anywhere else. Consider something
like a table searching algorithm. You come up with a "smarter" one... you
can only write and use it once, and that would be for the people where you
were currently working. Nowadays, there are many standard algorithms for
doing things, but in the old days we wrote our own and it would have been
impossible not to re-use them. No Company I worked for ever refused to
employ me because I would not sign this clause. As long as they owned the
code I wrote it was fne. As long as I retained the intellectual property to
go and write it again somewhere else, I had no problem with it either. It
was sort of like..."Well, it's yours and you have ownership of it, but I own
it too..."

This has been challenged in Court (in the 1980s in the U.K.) and found to be
a "restrictive practice". A restrictive practice is something that revents a
person from making a living. Such clauses, although still in contracts to
this day, are not legally binding, (at least, my understanding is that they
are not in the U.K...I have no idea what the US position on this would be.).

I would strongly recommend contractors to delete this clause before signing
the contract. (Yes, I know you'll say "but then I won't get the job...".
Don't be such a baby! If everyone resisted unfair clauses like this, they'd
soon disappear from "standard" contracts... Besides, contracting is a two
way street; if you have what they want, they'll bend a little in order to
get it. If you explain the position, make it clear to them that they will
have full rights to whatever you write, but you retain IP, most people are
prepared to be fair. (If they're not, you're in for a rocky ride working for
them anyway...)).

I believe the reason COBOL code is not shared as much as other languages is
because there are few "complex" techniques in COBOL. And it is so verbose
that when you do get sample code it requires a lot of time to wade through
it.

Style in COBOL is a very touchy subject and many people don't want their
coding style exposed to the World for criticism by others; then there are
many COBOL programmers who will only see the style and miss the underlying
technique (especially if they disagree with the style...people turn off when
they see code they don't "like". As Richard Plinston has observed here, most
COBOL programmers don't "like" what is unfamiliar to them).

We have all seen the "Religious Wars" here on style... they can get very
fierce. Personally, I don't mind maintaining someone else's code whatever
style they use, provided the intent is clear and they don't have a
requirement for me to learn their personal "shorthand" (a la Foodman).
During my career I have seen good and bad COBOL and dealt with it. I can't
see the point of making a crusade out of it.

Some people LOVE to have code samples and need them to really understand
what is going on (Jimmy Gavan is an example of this...Jimmy loves to see and
post code samples.) Others are content with a description of a concept and a
few coding clues. I find it tiresome to go through screeds of code when the
concept could be described in a few lines. Neither approach is "wrong".
Everybody's different.

In the case of the TCP Client sample code for use with Winsock, Paul
Raulerson opted to use Thane's sample code. That makes sense, but only if
you are determined to do this at the lowest level, in COBOL. I solved the
same problem by using a component. Not because I COULDN'T get the COBOL to
work (and I posted Paul the details of where I believed his code was
lacking), but because COBOL is NOT the best tool for the job in talking to
Sockets.

(The Sockets API is documented extensively for VB, Java, and C++ and it
works perfectly. Use COBOL you must "translate" all the parameters and the
methods of invoking them; use a component and you don't care what language
it is written in, you just get/set the properties and invoke the Methods...
It is simple, straightforward, and portable. Hard coded COBOL to the API is
not.).

I have many thousands of lines of COBOL code which I would be prepared to
share, but I suspect it has little relevance in today's World. I am slowly
converting the valuable stuff (standard Date routines, input validations,
relational DB utilities...etc.) to Components and these I am NOT prepared to
give away <G>. (Well, maybe, under special circumstances...<G>)

Pete.

Arnold Trembley <arnold.trembley@worldnet.att.net> wrote in message
news:3D9EADDE.5A5C8FA2@worldnet.att.net...
> Sff5ky wrote:
> >
…[3 more quoted lines elided]…
> > >Or is it that we all work for large corporations who frown on our
sharing
> > >even snippets of routines of what they view as Company owned code?
> >
> > I believe that this might be a major part of the restriction on code
sharing.
> > Most places regardless of size (speaking from limited corporate exposure
> > of 6 prior employers of varying size) have proprietary language in their
hiring
> >
> > papers regarding ownership of all code developed by the employee (on or
off
> > the job).
>
…[34 more quoted lines elided]…
> http://arnold.trembley.home.att.net/



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-10-07T07:56:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0210070656.799bc2f6@posting.google.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com>`

```
Hello Pete, 

I have a slightly different way of handling this.  Your point is well
taken and valid but the client also wants protection, and deserves it,
for things that you do that really ARE HIS.  I have the following
exception clause in my standard contract (I am "VENDOR", client is
"Short Name").

VENDOR may reuse programs and source code that have been previously
developed.  Rights to such programs and source code are granted to
(Short Name) non-exclusively.  In addition, VENDOR may in the course
of development create additional programs, source code, routines
and/or methods that VENDOR may have reason to believe will be useful
in the future.  Any such development must be of a general nature and
not specific to the project being undertaken.  Such items will be
identified by VENDOR and (Short Name) will not be charged for the cost
of such development.

Additionally, such code previously developed may be utilized in the
course of development for this contract.  When such code is used,
rights to such programs and source code are granted to (Short Name)
non-exclusively.  (Short Name) will be charged a reasonable fee for
such code and it's incorporation.


"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3da0adb0_1@Usenet.com>...
> This is an interesting point, Arnold.
> 
…[145 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-07T22:14:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da1f8d7_3@Usenet.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com> <bfdfc3e8.0210070656.799bc2f6@posting.google.com>`

```
Hi Thane,

I like your approach and it sems fair to all concerned.

What do you say when they offer you a "standard contract" that isn't set up
on the basis you describe?

Have you ever had an


Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0210070656.799bc2f6@posting.google.com...
> Hello Pete,
>
…[23 more quoted lines elided]…
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3da0adb0_1@Usenet.com>...
> > This is an interesting point, Arnold.
> >
> > As a contractor (in the days when I wrote COBOL code for a living) it
was
> > quite usual for each contract to contain a clause stating that all code
> > written by me on their site remained their intellectual and physical
> > property. I always crossed it out and explained that I could not sell
them
> > the intellectual property rights to solutions I developed because I
would
> > then be unable to use the same solution anywhere else. Consider
something
> > like a table searching algorithm. You come up with a "smarter" one...
you
> > can only write and use it once, and that would be for the people where
you
> > were currently working. Nowadays, there are many standard algorithms for
> > doing things, but in the old days we wrote our own and it would have
been
> > impossible not to re-use them. No Company I worked for ever refused to
> > employ me because I would not sign this clause. As long as they owned
the
> > code I wrote it was fne. As long as I retained the intellectual property
to
> > go and write it again somewhere else, I had no problem with it either.
It
> > was sort of like..."Well, it's yours and you have ownership of it, but I
own
> > it too..."
> >
> > This has been challenged in Court (in the 1980s in the U.K.) and found
to be
> > a "restrictive practice". A restrictive practice is something that
revents a
> > person from making a living. Such clauses, although still in contracts
to
> > this day, are not legally binding, (at least, my understanding is that
they
> > are not in the U.K...I have no idea what the US position on this would
be.).
> >
> > I would strongly recommend contractors to delete this clause before
signing
> > the contract. (Yes, I know you'll say "but then I won't get the job...".
> > Don't be such a baby! If everyone resisted unfair clauses like this,
they'd
> > soon disappear from "standard" contracts... Besides, contracting is a
two
> > way street; if you have what they want, they'll bend a little in order
to
> > get it. If you explain the position, make it clear to them that they
will
> > have full rights to whatever you write, but you retain IP, most people
are
> > prepared to be fair. (If they're not, you're in for a rocky ride working
for
> > them anyway...)).
> >
> > I believe the reason COBOL code is not shared as much as other languages
is
> > because there are few "complex" techniques in COBOL. And it is so
verbose
> > that when you do get sample code it requires a lot of time to wade
through
> > it.
> >
> > Style in COBOL is a very touchy subject and many people don't want their
> > coding style exposed to the World for criticism by others; then there
are
> > many COBOL programmers who will only see the style and miss the
underlying
> > technique (especially if they disagree with the style...people turn off
when
> > they see code they don't "like". As Richard Plinston has observed here,
most
> > COBOL programmers don't "like" what is unfamiliar to them).
> >
> > We have all seen the "Religious Wars" here on style... they can get very
> > fierce. Personally, I don't mind maintaining someone else's code
whatever
> > style they use, provided the intent is clear and they don't have a
> > requirement for me to learn their personal "shorthand" (a la Foodman).
> > During my career I have seen good and bad COBOL and dealt with it. I
can't
> > see the point of making a crusade out of it.
> >
> > Some people LOVE to have code samples and need them to really understand
> > what is going on (Jimmy Gavan is an example of this...Jimmy loves to see
and
> > post code samples.) Others are content with a description of a concept
and a
> > few coding clues. I find it tiresome to go through screeds of code when
the
> > concept could be described in a few lines. Neither approach is "wrong".
> > Everybody's different.
> >
> > In the case of the TCP Client sample code for use with Winsock, Paul
> > Raulerson opted to use Thane's sample code. That makes sense, but only
if
> > you are determined to do this at the lowest level, in COBOL. I solved
the
> > same problem by using a component. Not because I COULDN'T get the COBOL
to
> > work (and I posted Paul the details of where I believed his code was
> > lacking), but because COBOL is NOT the best tool for the job in talking
to
> > Sockets.
> >
> > (The Sockets API is documented extensively for VB, Java, and C++ and it
> > works perfectly. Use COBOL you must "translate" all the parameters and
the
> > methods of invoking them; use a component and you don't care what
language
> > it is written in, you just get/set the properties and invoke the
Methods...
> > It is simple, straightforward, and portable. Hard coded COBOL to the API
is
> > not.).
> >
> > I have many thousands of lines of COBOL code which I would be prepared
to
> > share, but I suspect it has little relevance in today's World. I am
slowly
> > converting the valuable stuff (standard Date routines, input
validations,
> > relational DB utilities...etc.) to Components and these I am NOT
prepared to
> > give away <G>. (Well, maybe, under special circumstances...<G>)
> >
…[15 more quoted lines elided]…
> > > > Most places regardless of size (speaking from limited corporate
exposure
> > > > of 6 prior employers of varying size) have proprietary language in
their
> >  hiring
> > > >
> > > > papers regarding ownership of all code developed by the employee (on
or
> >  off
> > > > the job).
…[43 more quoted lines elided]…
> >                 http://www.usenet.com



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-07T22:45:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da1fd6a_8@Usenet.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com> <bfdfc3e8.0210070656.799bc2f6@posting.google.com>`

```
Hi Thane,

I like your approach and it sems fair to all concerned.

What do you say when they offer you a "standard contract" that isn't set up
on the basis you describe?

Have you ever had a Company or Agent refuse to accept your alternative?

I'd be interested to know what the variations on this are between the USA
and UK.

In my current job I have to sign contracts for my guys and deal with Agents.
There is a Law in the UK called IR35 that says if a contractor stays more
than 6 months he must be treated as a permanent employee. That means the
Company must pay holidays and withold tax at the standard rate (this is
pretty devastating for most contractors who prefer to deal directly with the
Internal Revenue as Self-Employed people and use every legal means possible
to avoid tax). Some of the contracts I have read recently have gone to
incredibly  imaginative lengths to avoid IR 35. They contain clauses that NO
Company would ever countenance, like the following...

1. The contractor can work from home or on site at his discretion. He may
also use his own equipment but the Company have the right to check it before
allowing connection to their Network.

2. The contractor is not subject to the discipline or control of the Company
but will behave in a Professional manner.

3. The Contractor is contracted to provide service for a specific piece of
work, irrespective of how long it takes.

(there are many more that made me smile)

All of this is designed to show that the Contractor is NOT a de facto
employee of the Company.

When I queried some of these clauses with the various Agents I was hastily
assured that these clauses would never be invoked but were intended purely
for avoiding IR35. The only reason I signed these contracts was because
there is a  clause which gives me (as the empowered representative of the
Corporation) the right to terminate the contract for any reason, and if any
unilateral attempt was ever made to invoke these rights, I would certainly
do so.

It is an interesting example, though, of how bright people will conspire to
get round a stupid law... It is a pity that they have to.

(BTW, I always allow them to retain IP rights to their code, as long as they
accept that we own the instance of it they write for us, and no further
claim on it will be considered <G>. When you are dealing with things that
may not be program code as is understood by COBOL, this whole area becomes
more "fuzzy". For example, If a guy writes an ACCESS macro or SQL Server
stored procedure, or processes some workflows with DTS, can he really
attempt to "copyright" it? What if someone else comes along with the same
requirement and creates the same solution (this COULD happen with COBOL
code, but it is far less likely that the solutions would be identical,
because of the many possibilities and styles of coding...with facilities
like SQL however, there is a much greater chance of accidental duplication.
There might only be ONE way to efficiently join 3 tables, and SQL is SQL; it
is not really subject to style...)

I think your idea of "non-exclusive rights" is a good and fair one. Will
give that some more thought...


Pete.


Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0210070656.799bc2f6@posting.google.com...
> Hello Pete,
>
…[23 more quoted lines elided]…
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3da0adb0_1@Usenet.com>...
> > This is an interesting point, Arnold.
> >
> > As a contractor (in the days when I wrote COBOL code for a living) it
was
> > quite usual for each contract to contain a clause stating that all code
> > written by me on their site remained their intellectual and physical
> > property. I always crossed it out and explained that I could not sell
them
> > the intellectual property rights to solutions I developed because I
would
> > then be unable to use the same solution anywhere else. Consider
something
> > like a table searching algorithm. You come up with a "smarter" one...
you
> > can only write and use it once, and that would be for the people where
you
> > were currently working. Nowadays, there are many standard algorithms for
> > doing things, but in the old days we wrote our own and it would have
been
> > impossible not to re-use them. No Company I worked for ever refused to
> > employ me because I would not sign this clause. As long as they owned
the
> > code I wrote it was fne. As long as I retained the intellectual property
to
> > go and write it again somewhere else, I had no problem with it either.
It
> > was sort of like..."Well, it's yours and you have ownership of it, but I
own
> > it too..."
> >
> > This has been challenged in Court (in the 1980s in the U.K.) and found
to be
> > a "restrictive practice". A restrictive practice is something that
revents a
> > person from making a living. Such clauses, although still in contracts
to
> > this day, are not legally binding, (at least, my understanding is that
they
> > are not in the U.K...I have no idea what the US position on this would
be.).
> >
> > I would strongly recommend contractors to delete this clause before
signing
> > the contract. (Yes, I know you'll say "but then I won't get the job...".
> > Don't be such a baby! If everyone resisted unfair clauses like this,
they'd
> > soon disappear from "standard" contracts... Besides, contracting is a
two
> > way street; if you have what they want, they'll bend a little in order
to
> > get it. If you explain the position, make it clear to them that they
will
> > have full rights to whatever you write, but you retain IP, most people
are
> > prepared to be fair. (If they're not, you're in for a rocky ride working
for
> > them anyway...)).
> >
> > I believe the reason COBOL code is not shared as much as other languages
is
> > because there are few "complex" techniques in COBOL. And it is so
verbose
> > that when you do get sample code it requires a lot of time to wade
through
> > it.
> >
> > Style in COBOL is a very touchy subject and many people don't want their
> > coding style exposed to the World for criticism by others; then there
are
> > many COBOL programmers who will only see the style and miss the
underlying
> > technique (especially if they disagree with the style...people turn off
when
> > they see code they don't "like". As Richard Plinston has observed here,
most
> > COBOL programmers don't "like" what is unfamiliar to them).
> >
> > We have all seen the "Religious Wars" here on style... they can get very
> > fierce. Personally, I don't mind maintaining someone else's code
whatever
> > style they use, provided the intent is clear and they don't have a
> > requirement for me to learn their personal "shorthand" (a la Foodman).
> > During my career I have seen good and bad COBOL and dealt with it. I
can't
> > see the point of making a crusade out of it.
> >
> > Some people LOVE to have code samples and need them to really understand
> > what is going on (Jimmy Gavan is an example of this...Jimmy loves to see
and
> > post code samples.) Others are content with a description of a concept
and a
> > few coding clues. I find it tiresome to go through screeds of code when
the
> > concept could be described in a few lines. Neither approach is "wrong".
> > Everybody's different.
> >
> > In the case of the TCP Client sample code for use with Winsock, Paul
> > Raulerson opted to use Thane's sample code. That makes sense, but only
if
> > you are determined to do this at the lowest level, in COBOL. I solved
the
> > same problem by using a component. Not because I COULDN'T get the COBOL
to
> > work (and I posted Paul the details of where I believed his code was
> > lacking), but because COBOL is NOT the best tool for the job in talking
to
> > Sockets.
> >
> > (The Sockets API is documented extensively for VB, Java, and C++ and it
> > works perfectly. Use COBOL you must "translate" all the parameters and
the
> > methods of invoking them; use a component and you don't care what
language
> > it is written in, you just get/set the properties and invoke the
Methods...
> > It is simple, straightforward, and portable. Hard coded COBOL to the API
is
> > not.).
> >
> > I have many thousands of lines of COBOL code which I would be prepared
to
> > share, but I suspect it has little relevance in today's World. I am
slowly
> > converting the valuable stuff (standard Date routines, input
validations,
> > relational DB utilities...etc.) to Components and these I am NOT
prepared to
> > give away <G>. (Well, maybe, under special circumstances...<G>)
> >
…[15 more quoted lines elided]…
> > > > Most places regardless of size (speaking from limited corporate
exposure
> > > > of 6 prior employers of varying size) have proprietary language in
their
> >  hiring
> > > >
> > > > papers regarding ownership of all code developed by the employee (on
or
> >  off
> > > > the job).
…[43 more quoted lines elided]…
> >                 http://www.usenet.com







 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Contract work - was Re: TCP Client Sample Code with Winsock

_(reply depth: 9)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-10-09T07:33:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0210090633.46240c33@posting.google.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com> <bfdfc3e8.0210070656.799bc2f6@posting.google.com> <3da1fd6a_8@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3da1fd6a_8@Usenet.com>...

> Hi Thane,
> 
…[8 more quoted lines elided]…
> and UK.

..Snip..

There's a ton of variation.  Some contractacts lean more toward
confidentiality than anything else.  Some are clearly written to avoid
hassles with the tax authorities.

I've never had anyone balk at my ammendment - they all realize that it
saves them time and money, which in the long run is to their benefit.

Presently I operate as an individual, but shortly I intend to
incorporate.  When that is done, the relationship is company to
company and all the questions about "are they an employee or not" go
away.

The IRS here has some simple rules:

1 - the company cannot provide the equipment or tools.
2 - the company cannot say when you work or exactly what you work on.

This is a paraphrase obviously.  Bottom line - it goes down to the
level of supervision.
```

###### ↳ ↳ ↳ Re: Contract work - was Re: TCP Client Sample Code with Winsock

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-10T00:14:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da4b7b0_4@Usenet.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com> <bfdfc3e8.0210070656.799bc2f6@posting.google.com> <3da1fd6a_8@Usenet.com> <bfdfc3e8.0210090633.46240c33@posting.google.com>`

```
Thanks for that, Thane.

Pete.

Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0210090633.46240c33@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3da1fd6a_8@Usenet.com>...
>
> > Hi Thane,
…[3 more quoted lines elided]…
> > What do you say when they offer you a "standard contract" that isn't set
up
> > on the basis you describe?
> >
> > Have you ever had a Company or Agent refuse to accept your alternative?
> >
> > I'd be interested to know what the variations on this are between the
USA
> > and UK.
>
…[20 more quoted lines elided]…
> level of supervision.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 7)_

- **From:** "Editor" <Editor@aboutlegacycoding.commm>
- **Date:** 2002-10-07T11:05:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da1a2a1$1_7@news.teranews.com>`
- **References:** `<3d9da8ad$1_7@news.teranews.com> <20021004232935.01003.00002494@mb-mq.aol.com> <3D9EADDE.5A5C8FA2@worldnet.att.net> <3da0adb0_1@Usenet.com>`

```
I think Pete is probably closer to the truth of why COBOL code isn't shared.
The copyright issues are all true, but they are also just as true for C++ or
VB code or even Java - all of which are shared in copious amounts dispite
all these restrictive contract clasues (which I agree are not enforceable).
I'm a web developer by trade and like Pete I've see and scratched out those
clauses too.

However, there doesn't seem to be the same restrictions on using shareware
code on a corporate web site, even a complex, business critical e-commerce
site.  I guess we just don't have the years of version control procedures,
submission to production procedures, QA procedures, etc.  There is more of a
"throw it up and see if it flys" mentality to web development.  I've run
several shops where installing good QA and release procedures required a
small war with the staff.

Paul's point is also well taken - very few people "hobby" code in COBOL.
The compilers (up until Tiny Cobol like compilers) were very expensive.  And
for many people, the enviornments they are comfortable with (Mainframe) just
don't fit in their den.  Most of the code that is shared among JScript, VB
Script or Java programmers is written 'off the clock' so to speak.

Well, It's there, so I'm not going to take the shareware library on About
Legacy Coding down just because it's rarely used.  It costs me nothing to
run and since nobody contributes much, it takes very little of my time.
Perhaps as more 'freeware' compilers come into maturity I'll see more
submissions.
```

###### ↳ ↳ ↳ Re: TCP Client Sample Code with Winsock

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-10-05T15:28:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KyDn9.96216$121.2093814@twister.austin.rr.com>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <bfdfc3e8.0210010957.58a144f8@posting.google.com> <sgsm9.51345$Fw2.1440029@twister.austin.rr.com> <3d9da8ad$1_7@news.teranews.com>`

```
I think it is more than only a very tiny "garage" industry in COBOL every developed, due to the steep entry price into COBOL
development. A history of COBOL compilers would make a very interesting article indeed, and would show that all the "professional"
compilers, with just a very few exceptions, have always been list priced over $3K. That used to be a huge chunk of money for an
individual, and is still far from being an insignificant amount even today.

Just try to get another $3K past *my* wife without at least a 51% probability of making a return off that investment. :)

-Paul

"Editor" <Editor@aboutlegacycoding.commm> wrote in message news:3d9da8ad$1_7@news.teranews.com...
> I'm always amazed how little the download area of About Legacy Coding is
> used.
…[83 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Code sharing was Re: TCP Client Sample Code with Winsock

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2002-10-07T20:00:16-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DA21200.BEEE8A8E@istar.ca>`
- **References:** `<A1Ll9.40149$8o3.981815@twister.austin.rr.com> <bfdfc3e8.0210010957.58a144f8@posting.google.com> <sgsm9.51345$Fw2.1440029@twister.austin.rr.com> <3d9da8ad$1_7@news.teranews.com>`

```
How much of the coding done in COBOL is generic across application
areas? 
I have shared various things I did in assembler plus some COBOL programs
that parsed IBM system accounting records for usage reports.  For the
rest of the COBOL work I have done, there wasn't that much reusability
even within the organization.  Ironically, COBOL is becoming more and
more usable for Systems Programming and Operating system type coding as
the need for it diminishes.  
Editor wrote:
> 
> I'm always amazed how little the download area of About Legacy Coding is
…[80 more quoted lines elided]…
> > > --
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
