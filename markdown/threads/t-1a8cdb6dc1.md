[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL on the Web....HELP!

_23 messages · 15 participants · 2001-10 → 2001-12_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### COBOL on the Web....HELP!

- **From:** KNeddy@home.com
- **Date:** 2001-10-30T01:43:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bde0281.647438122@NEWS>`

```
I want to write a script in COBOL that updates files.  I want to
create a web page on the internet, have the user fill out a form, and
then when the submit button is clicked, execute a script written in
COBOL.  Why COBOL you ask.  Simply because I don't know Java or Perl
but I do know how to code the heck out of COBOL.  What are the tools I
need to do this with?  Most likely my page and script will reside on a
Linux server.  I've been looking at Net Express but it doesn't say it
supports the Linux platform. Would ACUCOBOL be a better choice?

I'm a newbie to writing any kind of script for the web...I have a
basic knowledge of HTML.  What do I need to keep in mind as far as
selecting a server for my page and COBOL script.  Does the server have
to have any special software to run the COBOL script or can I compile
it on my pc and then simply move the executable out to a cgi-bin to be
able to execute?  

You can reply here or to my email: KNeddy@home.com

Thanks a lot,

KN.
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-29T21:55:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kyoD7.21543$az4.1247696@news20.bellglobal.com>`
- **References:** `<3bde0281.647438122@NEWS>`

```
I would like to do the same thing, but the biggest inpediment is that the
Cobol runtime must be installed on the server.  If you can find a server
that has or will install the runtime for the cobol of your choice, then
their are lots of choices from there on in ...

<KNeddy@home.com> wrote in message news:3bde0281.647438122@NEWS...
> I want to write a script in COBOL that updates files.  I want to
> create a web page on the internet, have the user fill out a form, and
…[18 more quoted lines elided]…
> KN.
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** KNeddy@home.com
- **Date:** 2001-10-30T05:04:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bde342c.660154832@NEWS>`
- **References:** `<3bde0281.647438122@NEWS> <kyoD7.21543$az4.1247696@news20.bellglobal.com>`

```
On Mon, 29 Oct 2001 21:55:40 -0500, "Donald Tees"
<donald_tees@sympatico.ca> wrote:

>I would like to do the same thing, but the biggest inpediment is that the
>Cobol runtime must be installed on the server.  If you can find a server
>that has or will install the runtime for the cobol of your choice, then
>their are lots of choices from there on in ...
>
Thanks for your reply.  

So what is so tough about getting a server to install the cobol
runtime of your choice?   Is it simply not cost effective for the
server to install it?
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-30T06:40:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_jwD7.8483$Fy2.1338904@news20.bellglobal.com>`
- **References:** `<3bde0281.647438122@NEWS> <kyoD7.21543$az4.1247696@news20.bellglobal.com> <3bde342c.660154832@NEWS>`

```
<KNeddy@home.com> wrote in message news:3bde342c.660154832@NEWS...
> On Mon, 29 Oct 2001 21:55:40 -0500, "Donald Tees"
> <donald_tees@sympatico.ca> wrote:
…[10 more quoted lines elided]…
> server to install it?

The biggies, like bell, will just look at you with a stupid look ... the
people that sell the service do not even know what country the actual server
is in. Trying to make them understand you cannot install it from your PC can
take a few days.  Once they get over that hurdle, they will start talking
about the funding for the consultants they will need for security, etc.,
etc., etc.   Think in terms of money that will fund a T1 line ...
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-30T07:00:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jxwD7.23240$az4.1494290@news20.bellglobal.com>`
- **References:** `<3bde0281.647438122@NEWS> <kyoD7.21543$az4.1247696@news20.bellglobal.com> <3bde342c.660154832@NEWS>`

```
<KNeddy@home.com> wrote in message news:3bde342c.660154832@NEWS...

> So what is so tough about getting a server to install the cobol
> runtime of your choice?   Is it simply not cost effective for the
> server to install it?

PS to that last.

While it is obviously not an impossible task to find a server with a variety
of Cobol installed on it, or to find a company in the web service business
that will install a Cobol run time,  it tends to be a huge expense compared
to the amount charged for a server that has Java on it.

If Cobol is going to become "easy" on the net, we need servers that Cobol
programmers can use for small test sites and personal sites.  That will
allow the ordinary programmer to play a bit, do some testing, and even
(heaven forbid) put some free cobol code out that the rest of us can learn
from. I would be quite delighted to write some free library routines that
could be plugged into a web site, and make the Cobol code public domain.

That said, there are likely people in this NG that have the resources to do
just that, and could probably make a buck off it.  So people, does anybody
have a "cobol ready" server that they are willing to rent web space on, at a
rate suitable for a personal web page?
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

_(reply depth: 4)_

- **From:** praul@isot.com (Paul Raulerson)
- **Date:** 2001-10-31T13:08:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40f8f32c.0110311308.496d394@posting.google.com>`
- **References:** `<3bde0281.647438122@NEWS> <kyoD7.21543$az4.1247696@news20.bellglobal.com> <3bde342c.660154832@NEWS> <jxwD7.23240$az4.1494290@news20.bellglobal.com>`

```
Well, yes, there are. (

I can easily setup a system with one or more COBOL compilers on it for 
web developers; would anyone be interested in paying $5/month to cover
expenses? (i.e. Backup tapes, support, etc.) I would not be interested in 
making a profit, but I don't particularly want to loose money. 


The issues that come to mind are: 

  (1) Availability - the server can be up 24/7 except for scheduled downtime. 

  (2) Security     - I would have to put the server behind a firewall,
                     which means that if you want a completely separate
                     space and virtual server to play with, you may need
                     to use a "non standard port." That really isn't a
                     problem for most developers I suppose. 

  (3) Bandwidth    - Not enough bandwith available to support high bandwidth 
                     deployed applications. Can support 100 - 150 developers.

  
  (4) Rules        - What kind of rules need to be set? If developer "A"
                      cracks into developer "B"'s space and steals his code,
                      whom is responsible? What would be acceptable? 

  (5) Resources available: 
          This is the toughie of course. I would suggest: 

             (A) Apache Webserver with SSL available
             (B) IBM COBOL (CGI)
             (C) IBM C or GCC?
             (D) Java? Perl? PHP? What? 
             (E) DB/2 
             (F) VSAM? 
     
If you guys want to discuss and/or work out what you want, I'll put a 
system up with whatever requirements I can afford to meet. ;) 

Yours,
-Paul

     
                 



"Donald Tees" <donald_tees@sympatico.ca> wrote in message news:<jxwD7.23240$az4.1494290@news20.bellglobal.com>...
> <KNeddy@home.com> wrote in message news:3bde342c.660154832@NEWS...
> 
…[21 more quoted lines elided]…
> rate suitable for a personal web page?
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-31T07:26:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDFA795.4EF65E3F@Azonic.co.nz>`
- **References:** `<3bde0281.647438122@NEWS> <kyoD7.21543$az4.1247696@news20.bellglobal.com>`

```
> <KNeddy@home.com> wrote in message news:3bde0281.647438122@NEWS...
> > I want to write a script in COBOL that updates files.  I want to
…[6 more quoted lines elided]…
> > supports the Linux platform. Would ACUCOBOL be a better choice?

Using standard CGI is relatively simple to get Cobol to do this.  Input
to the program is via environment variables (for a GET) and standard
input (for a POST). So the program needs to do some DISPLAY name UPON
ENVIRONMENT-NAME / ACCEPT value FROM ENVIRONMENT-VALUE and then a ACCEPT
FROM CONSOLE that will read the correct number of characters from
standard input.

To output the HTML it needs to DISPLAY UPON CONSOLE to standard output. 
I don't directly output HTML from the application module but build a
table of data and names and merge this into an an HTML template file
with a called module.  This gives flexability to the output without
having to rewrite.  

There are commercial modules that you can buy to do this, but it just
isn't very hard and the commercial stuff can be restricting on what it
works with.

> > I'm a newbie to writing any kind of script for the web...I have a
> > basic knowledge of HTML.  What do I need to keep in mind as far as
…[3 more quoted lines elided]…
> > able to execute?

You will need a run-time for each machine that the program runs on.  For
MF this is OCSD (?) Cobol 4.1 application server.  It is compatible with
NetExpress so it should be possible to write on one system and deploy to
the other.  With my CGI stuff I have it running with Windows/Xitami,
Linux/Apache, OS/2/Xitami and a Multiuser-DOS based system from 99% one
set of source (about 100 lines different for Windows).  Some differences
are also sorted out at run-time but these are very minor.

If the CGI system is to do updates to live files then you will need to
use the same brand of Cobol to ensure compatability of file structures. 
You will also need to worry about file sharing and locking if these run
on different platforms.  If you will work with extracts and later batch
updating then any Cobol (or even, say, Python, will do the job.

If you will have a high loading then CGI may not be enough.  With CGI
the program is loaded for each transaction and it must open files,
recover status information, process and close.  This does have a
significant overhead.  For high volume work you may need to have the
Cobol program resident with files open and have a mechanism for directly
interacting with the web server (there are several ways of doing this). 
Design the program so that it can be made to work either way.

For example have a flag in W-S '01  Program-Active     PIC X VALUE
"N".'.  When you sucessfully initialise the module and open the files
set this to "Y" and check whether you need to initialise (open the
files) on each entry.  If the program has been reloaded for CGI then the
W-S value will be "N" and the files need reopening, if the program is
resident then this will be "Y" for the 2nd message.

Use Cookies and/or hidden fields for holding a key to a status file for
each user, you will be getting messages at random from several users and
not necessarily in exactly the sequence you want, they can press a back
button and re-send a previous message.  If the message is, say, an order
line, then this can cause duplicated entries.  If he had originally sent
quantity 1 and later resent quantity 2 from the same form (recovered
from the cache) is this to be two lines or a correction of the first ? 
Using a hidden field in the form with a generated unique number will
allow you to determine whether it is a resend.  I ignore resends and
reply he has tried to do this, there is a proper procedure for amending
an order line or creating a new one.

When doing an order entry form I process each line one at a time (ie I
don't give them a form to fill in 20 products and quantities before
sending), in fact they can send after each field of the line so that
they can send just the product code and get details, product + order
qty, product + order qty + back order, etc until they set a 'complete'
check box for the line (or for the whole order).  This allows
interaction at the level the user determines.  There is nothing worse
then a completely 'blind' system that requires the whole form to be
filled out only to have it cleared for some trivial reason, nor is it
sensible to have every step an interaction because it can be slow.

Alternately look at SP/2 client-server.  This will run SP/2 screens over
the web, the same screens that can run locally under Linux (text mode
GUI) or Windows.
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2001-10-29T22:51:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0110292251.53ef1a6f@posting.google.com>`
- **References:** `<3bde0281.647438122@NEWS>`

```
KNeddy@home.com wrote in message news:<3bde0281.647438122@NEWS>...
> I want to write a script in COBOL that updates files.  I want to
> create a web page on the internet, have the user fill out a form, and
…[5 more quoted lines elided]…
> supports the Linux platform. Would ACUCOBOL be a better choice?

Did you try PERCobol from LegacyJ (www.legacyj.com)?
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** kneddy@home.com
- **Date:** 2001-10-30T07:09:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bde596d.4008691@NEWS>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com>`

```
On 29 Oct 2001 22:51:06 -0800, g.friedrich@fiuka.de (Friedrich) wrote:

>KNeddy@home.com wrote in message news:<3bde0281.647438122@NEWS>...
>> I want to write a script in COBOL that updates files.  I want to
…[8 more quoted lines elided]…
>Did you try PERCobol from LegacyJ (www.legacyj.com)?
 No, actually I just found out about that today....maybe that's the
answer I'm looking for. thanx
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-03T17:29:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE4297A.6BF29C6F@Azonic.co.nz>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com> <3bde596d.4008691@NEWS>`

```
kneddy@home.com wrote:
> I want to write a script in COBOL that updates files.  I want to
> create a web page on the internet, have the user fill out a form, and
> then when the submit button is clicked, execute a script written in
> COBOL.  Why COBOL you ask.  Simply because I don't know Java or Perl
> but I do know how to code the heck out of COBOL.  

You could try CobolScript.  It is mostly like Cobol, but is scripting
like Perl or Python, costs only $US 50.00 for the professional version,
has CGI interface (and ftp and EMail), can access SQL (but not ISAM
files), has Windows and Linux (and BSD and Sun) versions, and can build
standalone executables with no runtime cost (unless you are an ISP or
ASP provider).

see http://www.cobolscript.com
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** kneddy@home.com
- **Date:** 2001-10-30T14:16:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdeb38f.692771600@NEWS>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com>`

```

>
>Did you try PERCobol from LegacyJ (www.legacyj.com)?

Looking at that right now.  There seems to be a educational tool and
an enterprise tool. The price difference is astronomical. 
I'm guessing the enterprise tool allows you to code in a production
environment and that is why it's so expensive?  Can someone explain to
me in simple terms why the cost difference is so vast?  The cost of
these packages that I've looked at would seem to be killing cobol. No
wonder C programmers hate cobol so much.
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** "Ray" <sorry_cant trust_my_email_address@on_usenet.com>
- **Date:** 2001-11-09T04:57:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YmJG7.46216$zK1.11995906@typhoon.tampabay.rr.com>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com>`

```
http://www.ils-international.com/goldmine/webcobol.htm

"Friedrich" <g.friedrich@fiuka.de> wrote in message
news:bcfdd616.0110292251.53ef1a6f@posting.google.com...
> KNeddy@home.com wrote in message news:<3bde0281.647438122@NEWS>...
> > I want to write a script in COBOL that updates files.  I want to
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** "Donald Steier" <dsteier@csc.com>
- **Date:** 2001-11-26T15:02:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5yM7.84$kY4.2174@dfw-service2.ext.raytheon.com>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com> <YmJG7.46216$zK1.11995906@typhoon.tampabay.rr.com>`

```
Why can't you use MicroFocus COBOL and imbed the COBOL executables in your
HTML?
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

_(reply depth: 4)_

- **From:** "Acucorp News" <shaun_gough@hotmail.com>
- **Date:** 2001-11-26T15:59:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1451C740A890D411B65C00104B95B1C04A2755@ras.acucorp.com>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com> <YmJG7.46216$zK1.11995906@typhoon.tampabay.rr.com> <b5yM7.84$kY4.2174@dfw-service2.ext.raytheon.com>`

```
I am not sure if this is possible in other COBOLs, but Acucorp does have
some good Documentation and Examples in the standard Development System that
you can purchase, explaining exactly how you can have a HTML form to obtain
data and send it to COBOL for processing, as with any other COBOL
application.

Acucorp also has a Web Plugin, so that you can execute COBOL applications
directly from an Internet Browser, so depending on how you want the
application to look and feel, depends on which route you want to take.

Please take a look at the Acucorp Website, and do not hesitate to contact me
directly if you ahev any questions.
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

_(reply depth: 5)_

- **From:** Paul Barnett <paul.barnett@nospam.microfocus.com>
- **Date:** 2001-12-04T13:23:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0CCE67.EB158E7F@nospam.microfocus.com>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com> <YmJG7.46216$zK1.11995906@typhoon.tampabay.rr.com> <b5yM7.84$kY4.2174@dfw-service2.ext.raytheon.com> <1451C740A890D411B65C00104B95B1C04A2755@ras.acucorp.com>`

```
For the record, Net Express does not need a web plug-in.

Net Express should be able to do what you want and for Linux, you would need to
re-compile using Object Cobol Developer Suite.

Regards,
Paul


Acucorp News wrote:

> I am not sure if this is possible in other COBOLs, but Acucorp does have
> some good Documentation and Examples in the standard Development System that
…[65 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-06T01:15:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0EC74E.D6768E74@shaw.ca>`
- **References:** `<3bde0281.647438122@NEWS> <bcfdd616.0110292251.53ef1a6f@posting.google.com> <YmJG7.46216$zK1.11995906@typhoon.tampabay.rr.com> <b5yM7.84$kY4.2174@dfw-service2.ext.raytheon.com> <1451C740A890D411B65C00104B95B1C04A2755@ras.acucorp.com> <3C0CCE67.EB158E7F@nospam.microfocus.com>`

```


Paul Barnett wrote:

> For the record, Net Express does not need a web plug-in.
>
> Net Express should be able to do what you want and for Linux, you would need to
> re-compile using Object Cobol Developer Suite.
>

Simple and direct reply. Unfortunately last time I checked on the price for the
Linux compiler that you are talking about - $4,200 Canadian ! Plus of course the
GUI tool, (forgotten its name - is part of Linux).

Jimmy
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2001-10-30T14:45:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l2zD7.1970$F56.551478416@newssvr12.news.prodigy.com>`
- **References:** `<3bde0281.647438122@NEWS>`

```
KN,

Have you looked at RM/COBOL:

http://www.liant.com/products/cobolcgi/

Linux is a supported platform.

-Rob

KNeddy@home.com wrote in message <3bde0281.647438122@NEWS>...
>I want to write a script in COBOL that updates files.  I want to
>create a web page on the internet, have the user fill out a form, and
…[18 more quoted lines elided]…
>KN.
```

##### ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-10-30T11:23:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nsAD7.93$DM.165361@newsrump.sjc.telocity.net>`
- **References:** `<3bde0281.647438122@NEWS> <l2zD7.1970$F56.551478416@newssvr12.news.prodigy.com>`

```
If what you need to do isn't that difficult, just 'buck up' and learn Java.
You can probably learn what you need within two weeks and its guaranteed
that
the server will support Java.

Check these links:
http://www.michael-thomas.com/java/javahotsites.htm
http://www.apl.jhu.edu/~hall/java/
http://ariel.minilab.bdeb.qc.ca/docs/java/secrets_examples/


"Robert Heady" <r.heady@liant.com> wrote in message
news:l2zD7.1970$F56.551478416@newssvr12.news.prodigy.com...
> KN,
>
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-30T17:36:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IyBD7.6080$xS6.7319@www.newsranger.com>`
- **References:** `<3bde0281.647438122@NEWS> <l2zD7.1970$F56.551478416@newssvr12.news.prodigy.com> <nsAD7.93$DM.165361@newsrump.sjc.telocity.net>`

```
No it is not guarenteed.  One site I maintain is hosted on FreeBSD with Java
prohibited - you must use Perl or Pyton or C for scripting.

In article <nsAD7.93$DM.165361@newsrump.sjc.telocity.net>, James says...
>
>If what you need to do isn't that difficult, just 'buck up' and learn Java.
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL on the Web....HELP!

- **From:** kneddy@home.com
- **Date:** 2001-10-31T13:25:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdffac5.776549910@NEWS>`
- **References:** `<3bde0281.647438122@NEWS> <l2zD7.1970$F56.551478416@newssvr12.news.prodigy.com> <nsAD7.93$DM.165361@newsrump.sjc.telocity.net>`

```
On Tue, 30 Oct 2001 11:23:22 -0500, "James" <mangogrower@telocity.com>
wrote:

>If what you need to do isn't that difficult, just 'buck up' and learn Java.
>You can probably learn what you need within two weeks and its guaranteed
…[7 more quoted lines elided]…
>

I'm taking a Java course at the college (starting in January).
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-31T13:03:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdf4294_4@news.newsgroups.com>`
- **References:** `<3bde0281.647438122@NEWS>`

```
I have COBOL CGI code running for form input, as you describe, but I don't
update COBOL files; I use ODBC and SQL to update a server based RDB from my
COBOL CGI code. (In my case it is ACCESS as the server is a Windows
platform). I use Fujitsu COBOL 97 with a third party interface for Windows,
to implement the CGI code.

Don Tees raised some excellent points on the "objection" to using COBOL; a
COBOL RTS must be installed and most public ISPs are just not interested. I
hit the same wall Don has described when I first started doing this around 2
years ago.

The way I got round this was as follows:

1. Installed Personal Web Server on my development machine (It is free with
Win 98 and you'll find it in the "ADDons" directory of your Win 98 CD.)

2. Developed my application and tested it. PWS is an excellent tool to
facilitate this.

3. As my application needs ACCESS, the target server would be Windows based
anyway. (I don't know if it is now possible to run ACCESS on non-Windows
platforms, but I believe it wasn't when I first started doing this.) The
reason I mention this is because Fujitsu provide an ASAPI interface with
Version 5 COBOL and this allows multithreading on the Windows server, and
thereby overcomes most of the CGI overheads that were described elsewhere in
this thread. I am currently considering revising my application to use
ASAPI. The downside is that I am then tied to only windows platforms. (Mind
you, it doesn't stop the VB guys...<G>).

I have never tried running the same CGI code on a UNIX type server. In
theory, I would need to use the third party interface differently and simply
recompile.

Now, after reading Richard Plinston's post to this same thread, I would say
that Richard's solution is infinitely better. I know he is not enamoured of
Windows (or anything MicroSoft <G>) from his previous posts here, and I
believe that his solution is a very good one. It certainly covers more
platforms.

However, to get you started, and assuming you don't have "control" over the
server (which is what prompted Don's point) the CGI with PWS route is very
viable. I liked Richard's idea of avoiding the third party interface by
doing his own ACCEPT/DISPLAY directly to the appropriate ports, but this
would require detailed knowledge of the differences between Win CGI and
"other" CGI and, personally, I have neither the time nor inclination to get
into it. The interface is great; I just call it when I want to write HTML.
It came free with Fujitsu 4.2 but they have dropped it now.

I would echo Don's call for anyone with a COBOL oriented server to make
themselves known...<G> It's a bit ironic that I considered setting up just
such a server a few weeks ago, but I am still too mobile to make it viable
and I would've needed someone here who could re-boot it when necessary...<G>

Someone else in this thread suggested  "Learn Java" I would endorse that
(for your own personal development, if for nothing else <G>), and I do use
Java servlets as well as COBOL CGI.  There are not the same downsides of
requiring a COBOL RTS, but you still have to have a "Java friendly" ISP as
there are Java policy requirements for running the servlet.

Finally, we should be aware that the forthcoming .NET will remove the
requirement for a COBOL RTS. Intermediate code should be acceptable to the
server irrespective of what source language it was generated by... Hopefully
this will simplify the whole business. Fujitsu NetCOBOL will not require
specific connection to the CGI as far as I understand it, maybe it is
implicit... I don't know, as I haven't really examined NetCOBOL yet. (I plan
to do so after it is released). NetCOBOL will require OO knowledge as it is
based on OO COBOL.

Again, using NetCOBOL will require a Windows based server.

Many people will not be keen on this, and Richard's solution is therefore an
attractive one.

Pete.

<KNeddy@home.com> wrote in message news:3bde0281.647438122@NEWS...
> I want to write a script in COBOL that updates files.  I want to
> create a web page on the internet, have the user fill out a form, and
…[18 more quoted lines elided]…
> KN.



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2001-10-31T01:55:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GSID7.158$2k1.70120@monger.newsread.com>`
- **References:** `<3bde0281.647438122@NEWS>`

```
Acucobol supports Linux and has some built-in extensions for doing CGI.  I
normally compile Acucobol to their p-code (you would need a runtime on the
web server for that), but later versions of the compiler have options for
generating native binaries on some platforms.

You could also look at http://tinycobol.org/ for a free Cobol that you could
play around with.  It's not a full Cobol85 compiler, but might have enough
features for you to do the web side of things.

<KNeddy@home.com> wrote in message news:3bde0281.647438122@NEWS...
> I want to write a script in COBOL that updates files.  I want to
> create a web page on the internet, have the user fill out a form, and
…[18 more quoted lines elided]…
> KN.
```

#### ↳ Re: COBOL on the Web....HELP!

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2001-10-31T15:54:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3be01d87.8790843@news.epix.net>`
- **References:** `<3bde0281.647438122@NEWS>`

```
KNeddy@home.com wrote:

>I want to write a script in COBOL that updates files.  I want to
>create a web page on the internet, have the user fill out a form, and
…[5 more quoted lines elided]…
>supports the Linux platform. Would ACUCOBOL be a better choice?

KN:

The Flexus Web Client works with either Micro Focus NetExpress or
Acucobol.  In addition, it works mbp Visual COBOL, RM COBOL, Fujitsu
COBOL, IBM Visual Age COBOL and CA-Realia COBOL.

You don't need to learn how to write any scripts or embed HTML into
your program.  We also support Linux servers in addition to Windows
servers with Web Client.

If you would like more details, we should discuss them via private
e-mail so as to avoid commercial product discussions in the newsgroup.
My e-mail address is rtwolfe@flexus.com.

>I'm a newbie to writing any kind of script for the web...I have a
>basic knowledge of HTML.  What do I need to keep in mind as far as
…[3 more quoted lines elided]…
>able to execute?  

Web Client generates HTML for you and you don't have to know how to
write CGI or Perl.

>You can reply here or to my email: KNeddy@home.com
>
>Thanks a lot,
>
>KN.


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
