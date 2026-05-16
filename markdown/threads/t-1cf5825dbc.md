[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBO to Java translation

_5 messages · 5 participants · 2001-06_

---

### COBO to Java translation

- **From:** Howard Wong <hwong@ican.net>
- **Date:** 2001-06-26T23:11:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B394ED8.EEBA7F03@ican.net>`

```
Hi All,

I'm working on a project that is looking into extracting some
functionality of any existing COBOL application and making it into a
stand-alone application. It will be enhanced and used to serve the needs
of other similar applications that the organization has.

The application is now on an MVS/IMS/IBM VS COBOL II platform. We are
contemplating on how best we can deploy this new application, because it
is part of an initiative to migrate our mainframe UI to browser-based
UI.

One way is to build this new app on the same host platform, and then
construct the JSP/HTML GUI to talk to the new app via MQ.

The other way is to build the new app in Java and put it on the Web
server, and it will in turn interface with the host applications via MQ.
There are two approaches that we are considering: one is to redesign and
write the application in Java, and two is to translate the COBOL code to
Java.

I'm conducting research into all of the above approaches. What I need
help with is the translation of COBOL to Java. By this I mean something
like going through the COBOL code line by line and replace that with
equivalent Java statements or new classes/methods. This is of course a
very simplistic view. There are things that will likely to provide
serious challenges, such as REDEFINE, FILLER, GOTO (I mean the really
bad ones), CORRESPONDING phrases, etc.

I have searched in Google with the phrase "cobol to java translation"
and got a bunch of company web sites promoting their own wares, plus an
odd review or two. What I am looking for is some real-life experience on
this subject. Has anyone attempted translating COBOL to Java? Did you
use any automation tool? How difficult was that (automated or
otherwise)? What were the "gotchas"?

As for those tools out there that can automate the job, has anyone used
any of them? If so, how effective were they? Was the generated Java code
tight and tidy (i.e. easy to maintain)?

One request: please forward you postings to my email address
"hhjwong@netscape.net" as well. I appologise for the inconvenience but I
can no longer get to any of my usual news servers at work, which I have
found out is due to firewall rule changes. I have been told that there
are no approved news servers that I can use. I'm posting this from home,
but I would like to get any repsonse ASAP, and I can get to my netscape
account at work. Besides, I really rather not bring any work home. ;-)

Many thanks in advance.

Regards,
Howard Wong
hhjwong@netscape.net
```

#### ↳ Re: COBO to Java translation

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T03:41:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B39559B.28EA568@home.com>`
- **References:** `<3B394ED8.EEBA7F03@ican.net>`

```


Howard Wong wrote:

> Hi All,
>
…[4 more quoted lines elided]…
> Howard,

I'm in no position to answer your specific questions but would offer a word
of caution as regards OO. (And I'm assuming you are already comfortable with
Java ?).

It is possible for me to do a 'quick and dirty' job in COBOL 'translating'
from non-OO to OO COBOL, but it is quick and dirty and means substituting
method-names for paragraphs. Such an approach doesn't acknowledge any
hierarchy or inheritance, plus the whole can be 'translated' without even
using object references.

I have no idea what the tools you have referred to are capable of doing -
but it seems to me, to take advantage of COBOL to Java - you will be faced
with a lot of chopping around of COBOL source code to dove tail into Java.
For most effective use of COBOL to Java, it seems to me you are faced with a
a systems re-write as a minimum, and then - do you fall into the trap of a
system re-design - but possibly you consider this latter to be an
'advantage' ?

Jimmy, Calgary AB
```

#### ↳ Re: COBO to Java translation

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-06-27T15:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hcu7k$g61$1@news.netmar.com>`
- **References:** `<3B394ED8.EEBA7F03@ican.net>`

```
In article <3B394ED8.EEBA7F03@ican.net>, Howard Wong  <hwong@ican.net>
writes:
>Hi All,
>
…[33 more quoted lines elided]…
>
You may want to check out the website at newsone.net they have html access to
the newsgroups.  

COBOL doesn't lend itself well to converting to OO from a non-OO platform. 
You may want to look for some tools that can look for perform statements or
make lists of the paragraphs (blocks of reusable code)  Often the GO TO
statements represent all of the key logic points and there seem to be no
blocks of reusable code.  But even a GO TO has to have a Label.  You are not
going to find many products that can take into account all of the redefines
and the occurs in a nice neet way.  Ive seen some Payroll files with occurs
inside of occurs that would drive a database conversion nuts.  Wait till you
find a file with 9 differrent record types, each with their own occurs for a 
600 character record!  Then there are the fields that hold different data at
different times in the processing stages.

You should just hire an experienced COBOL programmer as a consultant.  Often
these older programs are very old and they are not rewritten because the
orgranization did not want to spend the time or money to reengineer them. The
top-down approach works; it is just different.  

The use of Corresponding is a matter of taste and style.  If you use it that
means 2 things have to correspond.  That has always seemed to mean that much
more could go wrong when you have to change an existing program.  Many
programmers stay away from using corresponding.  

Varying is a fun one too.  It is often used to do things in a loop with a
counter, like a for loop.

You could just write CICS programs and use a screen scraper.

Have Fun.

>As for those tools out there that can automate the job, has anyone used
>any of them? If so, how effective were they? Was the generated Java code
…[16 more quoted lines elided]…
>


 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

#### ↳ Re: COBO to Java translation

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-27T10:05:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106270905.a875118@posting.google.com>`
- **References:** `<3B394ED8.EEBA7F03@ican.net>`

```
Howard,

There's really no point to doing this.

One thing you can do is interface directly to the mainframe using
Sockets, or ECI (if CICS) and just use the application from the web
server.

If it must exist as a "bean" various COBOL vendors have tools that
will take the code and compile it - with the source remaining in COBOL
- into a Java Bean.

Alternately you can use the .NET Compiler from Fujitsu (free beta
download at adtools.com) to create a web service from the code.

The language it is written in is becoming largely irrelevant - what
matters is the connection to the web server (whatever it is) and the
security of the transaction.

Howard Wong <hwong@ican.net> wrote in message news:<3B394ED8.EEBA7F03@ican.net>...
> Hi All,
> 
…[50 more quoted lines elided]…
> hhjwong@netscape.net
```

#### ↳ Re: COBO to Java translation

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2001-06-29T18:42:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3d17b7$1_1@feed1.realtime.net>`
- **References:** `<3B394ED8.EEBA7F03@ican.net>`

```
Others have remarked already on whether this is a good idea or not.
My initial reaction generally matches others.

However, Howard's organization may have good reasons to do this,
even if it is complicated or difficult.   One good reason is that
the business rules already encoded, while not priceless,
are enormously valuable, and automated conversion
might translate these reliably.   Hand-conversion likely won't.

I was under the impression that there was a COBOL-to-Java translator
out there, if you didn't mind the unreadability of the result.
No further comment.

If you want to do a custom translation, the DMS Software Reengineering
Toolkit
might be the way to go.  It offers generalized compiler technology
that can parse langauges, carry out arbitrary analyses and/or
transformations,
and then prettyprint the result.    DMS is already capable of
parsing/transforming/prettyprinting
both COBOL and Java, and can handle both at the same moment.

What is left is decide which part of the COBOL to extract, and
to write transforms that map between the languages.
This isn't easy (although having DMS take care of all that other
stuff means you can concentrate on just this).

See http://www.semdesigns.com/Products/DMS/DMSToolkit.html.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
