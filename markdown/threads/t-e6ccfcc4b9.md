[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/390 TCP Examples?

_17 messages · 5 participants · 2002-08 → 2002-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### OS/390 TCP Examples?

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-31T14:33:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<As4c9.380199$q53.12570481@twister.austin.rr.com>`

```
Would someone point me to some examples of how to call TCP/IP services from a COBOL program please? 
The best of all worlds would be one routine I can call from both batch and CICS. I did a bit of a web search and found some discussion, and I realize that there are samples somewhere in the TCPIP.* datasets, but they all look like they are for REXX or USS. (Or do you have to use USS services?) 

Thanks
-Paul
```

#### ↳ Re: OS/390 TCP Examples?

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-31T14:42:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8B4c9.380200$q53.12572597@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com>`

```
P.S. - I should have mentioned that what I need to do is open a socket, drag down a web page, and parse some information out of it. Trivial indeed to do from say, Perl under AIX. Example included below for example, grabs a stock quote from the NYSE and displays it in an HTML table. 

-Paul


#!/usr/bin/perl
#
use strict;
use IO::Socket;
my $host = shift  || 'www.nyse.com';
my $port = shift  || 80;
my $sock = IO::Socket::INET -> new(
                Proto      => 'tcp',
                PeerAddr   => $host,
                PeerPort   => $port);

my $printFlag = 'N';

$sock;
##
## Now emit the string to the web server
##
  print $sock "GET /cgi-bin/ny_quote?sym=cia&links=%23\n";

##
## Then read/parse the response
##
  $printFlag = 'N';

  print "<table><tr><td width=30></td><td>";
  while ( $_ = <$sock> ) {


        if (/^<\/FORM/) {
           $_ = <$sock>;
           $printFlag = 'Y';
           }



        if ($printFlag EQ 'Y'){
          print "$_";
          }

       }
  #
  print "</TD></TR></Table>";
  close $sock;





  "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:As4c9.380199$q53.12570481@twister.austin.rr.com...
  Would someone point me to some examples of how to call TCP/IP services from a COBOL program please? 
  The best of all worlds would be one routine I can call from both batch and CICS. I did a bit of a web search and found some discussion, and I realize that there are samples somewhere in the TCPIP.* datasets, but they all look like they are for REXX or USS. (Or do you have to use USS services?) 

  Thanks
  -Paul
```

##### ↳ ↳ Re: OS/390 TCP Examples?

- **From:** "Jay S. Siegel" <ka2csh@nospam.nowhere>
- **Date:** 2002-09-04T20:05:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s3.I3.ML2OEjQaL0s4RfEv4.NR@nospam.nowhere>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <8B4c9.380200$q53.12572597@twister.austin.rr.com>`

```
"PR" == "Paul Raulerson" writes:

PR> 
PR> P.S. - I should have mentioned that what I need to do is open a socket,
PR> drag down a web page, and parse some information out of it. Trivial
PR> indeed to do from say, Perl under AIX. Example included below for
PR> example, grabs a stock quote from the NYSE and displays it in an HTML
PR> table. 

    I checked out the REBOL language web site:

    http://www.rebol.com

    and they, unfortunately, don't have REBOL/Core for the IBM mainframes.
    It looks like a version for an OS/400 is planned, though.

    For those of you out there that have similar needs, but are operating on
    other platforms, you might want to consider using REBOL/Core.  It handles
    internet requirements elegantly and simply, and REBOL/Core is a free
    download at:

    http://www.rebol.com/platforms.html

    There are a bunch of scripts on the REBOL site, too.  I use REBOL on my
    Amiga here.
```

#### ↳ Re: OS/390 TCP Examples?

- **From:** "David Robinson" <david@nighttime.demon.invalid>
- **Date:** 2002-08-31T15:06:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wX4c9.4999$NR3.30259437@news-text.cableinet.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:As4c9.380199$q53.12570481@twister.austin.rr.com...
<Snipped HTML post>

Hey hotshot, if you've been posting to Usenet for 17 years or more, why are
you posting in HTML? And I know for a fact that people weren't posting in
HTML 17 years ago. :)
```

##### ↳ ↳ re: OT Top Posting

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-31T16:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kK5c9.380350$q53.12585159@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net>`

```
Mostly because anyone who does not want to see HTML can have their newsreader strip it automagicially.
With the bandwidth available today and with the benefits of being able to use nice text formatting, why not?
<grin> Besides which, it is trivial to strip out and almost all current newsreaders can do so.
-Paul

P.S. Hotshot yourself - how come you didn't re-subject your post with an off topic alert?
<grin>





"David Robinson" <david@nighttime.demon.invalid> wrote in message news:wX4c9.4999$NR3.30259437@news-text.cableinet.net...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
> news:As4c9.380199$q53.12570481@twister.austin.rr.com...
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

- **From:** "David Robinson" <david@nighttime.demon.invalid>
- **Date:** 2002-08-31T16:19:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<306c9.5083$K_3.30572589@news-text.cableinet.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:kK5c9.380350$q53.12585159@twister.austin.rr.com...
> "David Robinson" <david@nighttime.demon.invalid> wrote in message
news:wX4c9.4999$NR3.30259437@news-text.cableinet.net...
> > "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
> > news:As4c9.380199$q53.12570481@twister.austin.rr.com...
> > <Snipped HTML post>
> >
> > Hey hotshot, if you've been posting to Usenet for 17 years or more, why
are
> > you posting in HTML? And I know for a fact that people weren't posting
in
> > HTML 17 years ago. :)
> >
> Mostly because anyone who does not want to see HTML can have their
newsreader strip it automagicially.

Not all newsreaders strip HTML formatting including a few current ones I
could name.

> With the bandwidth available today and with the benefits of being able to
use nice text formatting, why not?

Because the content of the post is what is important not a load of flashy
HTML tags. And not everyone enjoys the beauty of fast, cheap bandwidth
globally. This may come as a shock to you in the good ol' US of A but in
some countries people have to pay for telephone calls to their ISPs and are
still using analogue modems.

Bandwidth is a finite resource. I often wonder how much faster the Internet
would flow without Usenet spam, spam cancels for such, properly quoted and
trimmed replies and no HTML postings which can be a 1/3 to 2/3 larger than
the equivalent plain text version.

HTML is bad because nasties can be hidden in it. There's that infinite loop
piece of JavaScript for a start, hit a few newsgroups I frequent recently.

> <grin> Besides which, it is trivial to strip out and almost all current
newsreaders can do so.

See above.

> P.S. Hotshot yourself - how come you didn't re-subject your post with an
off topic alert?

Changed now.
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-31T16:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yg6c9.380403$q53.12591205@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net>`

```

"David Robinson" <david@nighttime.demon.invalid> wrote in message news:306c9.5083$K_3.30572589@news-text.cableinet.net...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
> news:kK5c9.380350$q53.12585159@twister.austin.rr.com...
…[17 more quoted lines elided]…
>

And where might they be? They are not common under Windows, Macintosh, or Linux, since even the venerable and ancient "rn"
newsreader can do that these days...

> > With the bandwidth available today and with the benefits of being able to
> use nice text formatting, why not?
…[6 more quoted lines elided]…
>

The formatting of content was developed in historical times to enhance the infomation
densitiy. Note that even the serifs on a the letters in typical times font are there for a reason,
and they do very much increase the readabilty of the text.

There is as much, and probably more reason *to* format text than to not format it.


> Bandwidth is a finite resource. I often wonder how much faster the Internet
> would flow without Usenet spam, spam cancels for such, properly quoted and
> trimmed replies and no HTML postings which can be a 1/3 to 2/3 larger than
> the equivalent plain text version.
>

Not much faster. It would be a LOT more available however, without SPAM.

> HTML is bad because nasties can be hidden in it. There's that infinite loop
> piece of JavaScript for a start, hit a few newsgroups I frequent recently.
>

There are always bad guys. That is not enough reason (IMNSHO) to give up something that
adds tremendous value to a communications medium.You are welcome to disagree of course,
but I think you might find some flaws in your reasoning if you look a little closer.

> > <grin> Besides which, it is trivial to strip out and almost all current
> newsreaders can do so.
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 5)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-09-01T04:51:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com>`

```
Paul Raulerson wrote:
> "David Robinson" <david@nighttime.demon.invalid> wrote in message news:306c9.5083$K_3.30572589@news-text.cableinet.net...
> 
…[32 more quoted lines elided]…
> newsreader can do that these days...

Netscape & Mozilla (same code base, of course) are 2 I've used.
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-01T14:34:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kzpc9.384278$q53.12761564@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net>`

```
UH Liam - While that may be  technically correct, I am not sure it is applicable. You can of course, write a pre-filter for Netscape
(or simply recompile the mozilla code) to strip out HTML, but there is no benefit gained by doing so. They display plain text as
well as HTML documents.




"Liam Devlin" <LiamD@optonline.NOSPAM.net> wrote in message news:Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net...
> Paul Raulerson wrote:
> > "David Robinson" <david@nighttime.demon.invalid> wrote in message news:306c9.5083$K_3.30572589@news-text.cableinet.net...
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 7)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-09-02T01:32:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mJCc9.19403$NV6.559313@news4.srv.hcvlny.cv.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net> <Kzpc9.384278$q53.12761564@twister.austin.rr.com>`

```
Paul Raulerson wrote:
> UH Liam - While that may be  technically correct, I am not sure it is applicable. You can of course, write a pre-filter for Netscape
> (or simply recompile the mozilla code) to strip out HTML, but there is no benefit gained by doing so. They display plain text as
> well as HTML documents.

Serious question, how would I go about creating such a pre-filter? Which 
language would I want to use to create it? I ask because I get tons of 
spam and have been wondering if I could write something like this to 
scan headers & toss a whole lot of what comes in, e.g., anything from 
Taiwan.
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 8)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-02T13:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MhJc9.388787$q53.12919011@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net> <Kzpc9.384278$q53.12761564@twister.austin.rr.com> <mJCc9.19403$NV6.559313@news4.srv.hcvlny.cv.net>`

```
The source for mozilla is in C, so C would be the best choice, but you can use any language that uses
C calling conventions (even COBOL) and link it in to the executable. (Or you can use a DLL or
shared library, but why do things the hard way?)  To code the EXIT (add the function call) in the mozilla code you have to use C of
course.

-Paul


"Liam Devlin" <LiamD@optonline.NOSPAM.net> wrote in message news:mJCc9.19403$NV6.559313@news4.srv.hcvlny.cv.net...
> Paul Raulerson wrote:
> > UH Liam - While that may be  technically correct, I am not sure it is applicable. You can of course, write a pre-filter for
Netscape
> > (or simply recompile the mozilla code) to strip out HTML, but there is no benefit gained by doing so. They display plain text as
> > well as HTML documents.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 9)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-09-02T20:46:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GDTc9.31862$NV6.1041462@news4.srv.hcvlny.cv.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Vxkc9.1140$NV6.5460@news4.srv.hcvlny.cv.net> <Kzpc9.384278$q53.12761564@twister.austin.rr.com> <mJCc9.19403$NV6.559313@news4.srv.hcvlny.cv.net> <MhJc9.388787$q53.12919011@twister.austin.rr.com>`

```
Paul Raulerson wrote:
> The source for mozilla is in C, so C would be the best choice, but you can use any language that uses
> C calling conventions (even COBOL) and link it in to the executable. (Or you can use a DLL or
> shared library, but why do things the hard way?)  To code the EXIT (add the function call) in the mozilla code you have to use C of
> course.

Thanks, Paul.
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 5)_

- **From:** "David Robinson" <david@nighttime.demon.invalid>
- **Date:** 2002-09-01T13:01:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Scoc9.6086$%r.36590750@news-text.cableinet.net>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:Yg6c9.380403$q53.12591205@twister.austin.rr.com...
>
> "David Robinson" <david@nighttime.demon.invalid> wrote in message
news:306c9.5083$K_3.30572589@news-text.cableinet.net...
> > HTML is bad because nasties can be hidden in it. There's that infinite
loop
> > piece of JavaScript for a start, hit a few newsgroups I frequent
recently.
> >
>
> There are always bad guys. That is not enough reason (IMNSHO) to give up
something that
> adds tremendous value to a communications medium.You are welcome to
disagree of course,
> but I think you might find some flaws in your reasoning if you look a
little closer.
>

I'm sorry, but the flaws are in your reasoning. You are assuming that
everyone is using a newsreader that it capable of handling HTML or stripping
the HTML tags from posts. The only assumption you can make without fear of
contradiction is that any RFC-compliant newsreader is capable of displaying
7-bit clean ASCII text without any form of mark-up language included. Note
that this also holds true for e-mail clients.

The other aspect of HTML posts about introducing unnecessary bloat not only
affects bandwidth but also the storage of posts on ISPs' news servers. The
current cost of IDE hard drives is irrelevant to the costs paid by ISPs,
they tend to use SCSI hard drives in RAID configurations. They're a bit
funny like that, liking redundancy and reliability in their systems. :) So
we have more storage space required, more bytes being transferred and
therefore more load on the servers. Hmmm, this all has to be paid for
somehow.

However, so long as it's convenient to you, hang the inconvenience to
others, eh? :)
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-01T14:55:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dTpc9.384454$q53.12763807@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Scoc9.6086$%r.36590750@news-text.cableinet.net>`

```
Well, perhaps - MR/ICE on OS/2 has to call a browser to deal with HTML encoded messages, if you don't tell it to strip out the HTML. 

But again, I contend that my reasoning is correct; the very small percentage of readers that *may* not be able to strip out HTML are either capable of being recompiled to do so, or else have front end systems (i.e. filters) that can do so. I can read posting using ISPF, and to that it even requires that the text be translated
to EBCDIC, as well as strip out HTML.  UNIX text only systems can do the same very easily with multiple tools, including emacs, vi(vim), rn, slrn, trn, and others. 

And as for bloat - I believe your reasoning is flawed there; you content that HTML adds 'bloat" while I contend it adds information content.  As I mentioned earlier, there are very good reasons that different typefaces and justification schemes were developed and HTML allows even the most trivial message to be formatted in such a way to increase the information density and the readability. 

For example, without enhanced encoding it would quite difficult indeed to insert a theta into this discussion:
θ   - since it is a non English character and defined in Unicode. However, by sending this message in HTML format, the theta above is correctly displayed. Unless of course, you strip it out and then you have go through a lot of effort. 



Yes, in the COBOL group, this is perhaps not that important. But even here, try putting a simple equation in that we all use:   I could code it  as 



FV = PV ( 1 + i ) ^n, 



but it sure looks better and it will be interpreted far more quickly if I code it as:

 

PV = FV(1 + i)n



Last point, if you meant "bloat" as "increase in network traffic", for legitimate uses that is not even a statistical blip. For use by spammers (i.e. Sex this and Gamble that and You Won This Free scam) you are 101% correct. The masses of garbage they spew out is nothing but stolen bandwidth from everyone else. But that has little or nothing to do with the you or I using or being able to use it. 

-Paul


"David Robinson" <david@nighttime.demon.invalid> wrote in message news:Scoc9.6086$%r.36590750@news-text.cableinet.net...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
> news:Yg6c9.380403$q53.12591205@twister.austin.rr.com...
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-09-01T18:46:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tftc9.344227$2p2.14532946@bin4.nnrp.aus1.giganews.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Scoc9.6086$%r.36590750@news-text.cableinet.net> <dTpc9.384454$q53.12763807@twister.austin.rr.com>`

```

Except your 14K post added not one iota of information, even though your
post was three times the size of the average post to this newsgroup.

No, HTML newsgroup posts are inappropriate, impolite, and just plain wrong.

If you insist on flames and what-not, I suggest you put your creation on a
web page and supply a link.
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 8)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-01T23:05:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q2xc9.181275$Yd.8062463@twister.austin.rr.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net> <Yg6c9.380403$q53.12591205@twister.austin.rr.com> <Scoc9.6086$%r.36590750@news-text.cableinet.net> <dTpc9.384454$q53.12763807@twister.austin.rr.com> <Tftc9.344227$2p2.14532946@bin4.nnrp.aus1.giganews.com>`

```
The only thing in the post was an equation, so if you saw one with 'flames' and such,
it was not from me. And most of the post was a quote of course.

-Paul

"JerryMouse" <nospam@bisusa.com> wrote in message news:Tftc9.344227$2p2.14532946@bin4.nnrp.aus1.giganews.com...
>
> Except your 14K post added not one iota of information, even though your
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT HTML posting

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-09-01T18:40:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ratc9.77442$On.3736436@bin3.nnrp.aus1.giganews.com>`
- **References:** `<As4c9.380199$q53.12570481@twister.austin.rr.com> <wX4c9.4999$NR3.30259437@news-text.cableinet.net> <kK5c9.380350$q53.12585159@twister.austin.rr.com> <306c9.5083$K_3.30572589@news-text.cableinet.net>`

```

"David Robinson" <david@nighttime.demon.invalid>
>
> Bandwidth is a finite resource. I often wonder how much faster the
Internet
> would flow without Usenet spam, spam cancels for such, properly quoted and
> trimmed replies and no HTML postings which can be a 1/3 to 2/3 larger than
> the equivalent plain text version.

When using the word "bandwidth" in a newsgroup post, please abbreviate it as
'bndwdth' thereby saving precious bndwdth.

Thnks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
