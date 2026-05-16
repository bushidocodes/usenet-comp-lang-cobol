[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question-WYSIWYG and RMCobol on SCO

_8 messages · 7 participants · 2004-05 → 2004-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Question-WYSIWYG and RMCobol on SCO

- **From:** sbelt@dpcsystems.com
- **Date:** 2004-05-24T08:27:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
The company I work for has used RMCobol and SCO Unix for the last 15+
years.  Now they want to put a graphical front end on our package.
They want to keep running the SCO and use the cobol data files as they
are.

We are looking into methods of putting the graphical front end on SCO
or putting it on Windows and having to communicate in real time to the
SCO server and the cobol data files.

We have looked at VB, Liant's Cobol WOW, Flexis and Connx Solutions.

Has anyone successfully done this?  If you've tried and failed, are in
the process of trying or have successfully done this, would you mind
sharing any thoughts you might have, suggestions or products.

Really appreciate anything you can tell us.
```

#### ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-05-24T18:29:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<plb4b0hjfaf8gr5atflafotnhnm5tl6hvu@4ax.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
On Mon, 24 May 2004 08:27:15 -0500, sbelt@dpcsystems.com wrote:

>The company I work for has used RMCobol and SCO Unix for the last 15+
>years.  Now they want to put a graphical front end on our package.
…[13 more quoted lines elided]…
>Really appreciate anything you can tell us.

The answer to this will really depend on how you have your apps
developed so far.

If for example you are using RM/PANELS, then using COBOL-WOW or
changing to SP2 (Flexus) is probably the easiest. Both will allow you
to have your runtime/files/programs on the Unix machine, and work as a
thin-client over TCP/IP.

If you don't have any screen manager so far, it MAY be easy to move to
SP2, but only by looking at your code would be possible to determine
the work involved.

Another option is to use VB, Delphi or other Gui tool, and combine it
with Relativity, both client and server.

All of the above work fine, and there are loads of customers using any
of them, sometimes more than one.

Not sure if Connx will will work with RM/COBOL files. Probably not.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-05-24T18:03:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Oqsc.577385$Ig.364310@pd7tw2no>`
- **In-Reply-To:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
sbelt@dpcsystems.com wrote:

>The company I work for has used RMCobol and SCO Unix for the last 15+
>years.  Now they want to put a graphical front end on our package.
…[16 more quoted lines elided]…
>
I don't use the products and would hesitate about Unix, but  for a quick 
painless way from COBOL to GUI-ing, you will see a lot of 'Thumbs Up" 
endorsements for using Flexus. Another one is Norcomm Screen-IO. Check 
their sites, Bob or Kevin respectively will be only too happy to cover 
queries.

Actual users of the products can comment, but I'm of the inclination 
that if your screen handling is done by CALLing screen programs - life 
will be a lot easier.

Some people here using SP2 -

Thane Hubbell - with Fujitsu procedural , (and probably other compilers)
Donald Tees - using OO in both Fujitsu and Net Express
Bob Hennessey - Procedural Net Express (opted for SP2 after he had taken 
a training course for N/E's Dialog System)

There are other developers, but those are the ones that immediately come 
to mind.

Jimmy, Calgary AB
```

#### ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-24T12:47:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405241147.6d9bd4a8@posting.google.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
sbelt@dpcsystems.com wrote 

> The company I work for has used RMCobol and SCO Unix for the last 15+
> years.  Now they want to put a graphical front end on our package.

> They want to keep running the SCO and use the cobol data files as they
> are.

I am shocked.  Have they read no tech news in the last year or so ? 
(see Groklaw.net).  SCO has been taken over by corporate raiders
without two clues to rub together, have scaled down development and
support and, with MS involment in funding, will be relying on suing
everyone in sight for revenue.  They have started suing their
customers.
 
> We are looking into methods of putting the graphical front end on SCO
> or putting it on Windows and having to communicate in real time to the
> SCO server and the cobol data files.
> 
> We have looked at VB, Liant's Cobol WOW, Flexis and Connx Solutions.

Flexus SP/2 I use.  I do it in text mode and this will run on the
console, on xterm, or using putty or Token2 running on Windows
machines over LAN or internet or on old 486s running Pocket Linux. 
The same code and screens will run using the Flexus thin client with a
graphics GUI on Windows.
```

#### ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-24T23:38:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40b278d9.176214182@news.optonline.net>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
sbelt@dpcsystems.com wrote:

>The company I work for has used RMCobol and SCO Unix for the last 15+
>years.  Now they want to put a graphical front end on our package.
…[11 more quoted lines elided]…
>sharing any thoughts you might have, suggestions or products.

Millions of installations have done this. It's called Client-Server.  They
usually do it with a database on the server, not Cobol-style files.

In addition to Cobol on the server and a GUI product on the client (or perhaps
on the server as well), you need a communication product to pass data between
them AND to start Cobol programs on the server. Such products are usually called
Middleware. 

VB, by itself, does not provide either. If you data were in a database, you
could use ODBC to access it, thereby eliminating the need for middleware. 
Since it's not, you'd have to cobble a home-grown solution using RPC (remote
procedure call) to start the Cobol programs and do fairly primative
communication. This is do-able, and many companies have gone that way.

Cobol-Wow is similar. With the addition of Cobol-RPC, they've provided an
off-the-shelf solution to RPC. There are three problems with Liant: RPC is
primative, Liant's programs run slowly because they're interpreted, I wouldn't
want to bet my job on the survival of Liant. It's a small company with limited
resources. 

Connx requires you to copy all the Cobol data into a database. The Cobol files
would not be continuously updated. They'd see the updates when you do a batch
synchronization. I don't like their approach.

I'd lean toward Flexus. SP2 is a very well-done GUI for Cobol. Judging from its
quality, I'd expect Thin Client to be as good. I have no experience with Thin
Client, so my expectation is pure hope.

Thin Client does screen paints on the server side and ships images to the
desktop. As with Microsoft Terminal Server and Citrix,  that greatly simplifies
version upgrades.
```

##### ↳ ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-05-25T08:14:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nr5b0p38bdvrocapl4rf73bof6le5oe9t@4ax.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com> <40b278d9.176214182@news.optonline.net>`

```
On Mon, 24 May 2004 23:38:12 GMT, robert.deletethis@wagner.net (Robert
Wagner) wrote:

>sbelt@dpcsystems.com wrote:
>
…[24 more quoted lines elided]…
>could use ODBC to access it, thereby eliminating the need for middleware. 
The fact that th data is not on a Database does not matter, as it is
possible to use Relativity for the same purpose.

>Since it's not, you'd have to cobble a home-grown solution using RPC (remote
>procedure call) to start the Cobol programs and do fairly primative
>communication. This is do-able, and many companies have gone that way.
No need for this. As mentioned before both SP2 and COBOL-WOW will do
this with their thin client.
As another alternative it is possible to use VanGui, which is an
interface between VB and RM/COBOL. More work involved than using the
first two, hence my lack of mention before.

>
>Cobol-Wow is similar. With the addition of Cobol-RPC, they've provided an
…[3 more quoted lines elided]…
>resources.
Not really. If Liant was to close it would probably have done so a
long time ago. As for being slow, it has the same basic speed as
others on Unix environments. Also bear in mind that in many shops and
software houses those using MicroFocus will keep using .int or .gnt
files so they can port them easly to other OS's. Not doing so would
imply buying more than one compiler, one for each OS used.

>
>Connx requires you to copy all the Cobol data into a database. The Cobol files
>would not be continuously updated. They'd see the updates when you do a batch
>synchronization. I don't like their approach.
The fact that Connx required the files on the DB does not mean that
they could not be so. IF this was the real requirement (e.g. use a DB)
then using COBOL ACCESS + from www.rldt.fr would easly bypass that
problem, most of times without any changes to the file layout. Using
this product all the COBOL file access is indeed done on the DB of
choice.
>
>I'd lean toward Flexus. SP2 is a very well-done GUI for Cobol. Judging from its
…[5 more quoted lines elided]…
>version upgrades. 
Humm... Maybe Bob/Thane/Tom can clear us if this is how it happens. I
am under the impression that the PAINTING is done on the Client side,
not the server, although the information processing is on the Server
side, and that only the "text" that is to be displayed on the "form"
is sent to the client.






Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-05-25T14:22:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2FIsc.280$2S6.154@newssvr23.news.prodigy.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>`

```
<sbelt@dpcsystems.com> wrote in message
news:<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com>...

> The company I work for has used RMCobol and SCO Unix for the last 15+
> years. Now they want to put a graphical front end on our package.
> They want to keep running the SCO and use the cobol data files as they
> are.

One definition of 'graphical front end' that seems to interest a large
number of our customers is 'browser'. Do you consider 'browser' to be a
'graphical front end'?

One principal benefit of adopting the browser paradigm is that computer
users have come to expect different behavior from applications presented in
a browser than they have from GUI-based applications displayed on the same
display device at the same time. The browser paradigm (i.e. HTML forms) is a
better fit for most COBOL legacy applications.

> We have looked at VB, Liant's Cobol WOW, Flexis and Connx Solutions.

The tool of choice for browser-enabling, or for converting to web services
(which would allow a range of client tools), would be Liant's recently
released Xcentrisity (TM) Business Information Server (BIS).

http://www.liant.com/news/releases/20040405_bis.php3

Contact Liant sales for further information about BIS. Liant is holding
monthly seminars and workshops to introduce customers to this exciting new
technology, now available for Windows IIS and Apache/Linux (a SCO port
probably would be negotiable, but might not be the best approach, depending
on the applications needs).

> Has anyone successfully done this?

Yes.

> If you've tried and failed, are in
> the process of trying or have successfully done this, would you mind
> sharing any thoughts you might have, suggestions or products.

One thing that is common to almost any approach is: you must be prepared to
separate your business logic from the presentation logic. COBOL in general
has always had the ability to tightly intermix business logic and
presentation logic, with the result that most applications have
moderate-to-very-tight coupling between the two. Additionally, the
presentation logic has always been the most proprietary (e.g. COBOL vendor
specific) area of COBOL. BIS provides a mechanism that promotes the
necessary separation but, in a very real way, is far less proprietary than
the original program or any of the competitive approaches.

Best regards,

Tom Morrison

Liant Software Corporation
```

##### ↳ ↳ Re: Question-WYSIWYG and RMCobol on SCO

- **From:** "rearl306" <rearl306@nospam.hotmail.com>
- **Date:** 2004-06-14T21:31:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cc8542de769eea0e4277eb9337840494@localhost.talkaboutprogramming.com>`
- **References:** `<vgs3b0t30l7t9r91e2mi9r702qmn9jlck1@4ax.com> <2FIsc.280$2S6.154@newssvr23.news.prodigy.com>`

```
Another possibility might be to look at using InstantGUI from Liant.  See
http://www.liant.com/instantGUI for more info.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
