[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Any way to access MF Indexed files on Unix from Windows?

_7 messages · 6 participants · 1998-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Any way to access MF Indexed files on Unix from Windows?

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<352c326f.1830517@news.wwa.com>`

```

Hello,

Our shop uses Microfocus 3.0 on SCO Unix 5. We would like to do
windows programming and access the indexed files on unix from Windows.
I saw once a VBX that could do this, but I forgot what it was.

Also, if you are doing something similar, what are the file and record
locking issues invloved?

We currently use TCP/IP to run the Unix apps from Windows using
terminal emulation, but it would be nice to write some pure windows
apps that just access the data that resides on Unix.

Thanks for any help,

Paul
```

#### ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<352c326f.1830517@news.wwa.com>`
- **References:** `<352c326f.1830517@news.wwa.com>`

```

Paul DuBois wrote:
› 
› Hello,
…[14 more quoted lines elided]…
› Paul

Try ODBC drivers for COBOL - www.transoft.com

Their U/SQL product should do the job for you !!!

Mike.
```

#### ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<352c326f.1830517@news.wwa.com>`
- **References:** `<352c326f.1830517@news.wwa.com>`

```

Paul:

Paul DuBois wrote:
›
› Hello,
›
› Our shop uses Microfocus 3.0 on SCO Unix 5. We would like to do
› windows programming and access the indexed files on unix from Windows.

You have already been informed by the folks from Micro Focus, who used
to sell a private-label version of Transoft, about the Transoft
solution. Please also consider Liant's offering, Relational DataBridge,
which provides standard ODBC SQL access to your UNIX based indexed
files. The following URL takes you directly to information:
http://www.liant.com/products/retooling/databridge/index.html (By the
way, our www2.liant.com server, upon which the demo resides, is having
some hardware problems. If the demo doesn't work, try again later. As
they say in broadcasting, "We are working to correct the problem...")

› I saw once a VBX that could do this, but I forgot what it was.

I have not seen the VBX solution promoted in this newsgroup for quite
some time; it was available from a German company. The weakness of this
approach is the requirement to do something about COBOL data types, of
which standard Windows programming tools know little. The VBX might
have provided some support in doing this -- I don't remember. Most
tools are ODBC compliant, however, due to the wide availability of ODBC
drivers for various data sources.

›
› Also, if you are doing something similar, what are the file and record
› locking issues invloved?

Relational DataBridge uses the Micro Focus file handler. Since routine
data access is read-only, file and record locking are nonissues. For
SQL UPDATE operations, Relational DataBridge uses optimistic
concurrency.

›
› We currently use TCP/IP to run the Unix apps from Windows using
› terminal emulation, but it would be nice to write some pure windows
› apps that just access the data that resides on Unix.

You are literally only a couple of hours (including installation) away
from such access when the Relational DataBridge box is delivered to your
office. It really is that easy, since you already have the TCP/IP
connections in place.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

##### ↳ ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d6a2d200cf-p3@usenetarchives.gap>`
- **References:** `<352c326f.1830517@news.wwa.com> <gap-d6a2d200cf-p3@usenetarchives.gap>`

```

Tom Morrison wrote:

› Large Snip<

Just want to say thanks to Tom and everyone else for their help. I
will probably go with one of the ODBC solutions, as our user would
like to use Windows spreadsheet programs and such to look at the Unix
Indexed files. Right now we are doing an export to ASCII in unix,
transfering the file to the PC, then using an import into the
spreadsheet.

Once I find a good product, I will also be doing some windows
programming to access the files dynamically. Who knows, maybee I will
eventually end up re-writing all the Unix CoBol in windows, but I
doubt it. Some things just don't need a Window's interface.

Thanks again,

Paul
```

###### ↳ ↳ ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d6a2d200cf-p4@usenetarchives.gap>`
- **References:** `<352c326f.1830517@news.wwa.com> <gap-d6a2d200cf-p3@usenetarchives.gap> <gap-d6a2d200cf-p4@usenetarchives.gap>`

```

Paul DuBois wrote:
› 
› Tom Morrison  wrote:
…[17 more quoted lines elided]…
› Paul

You should make sure to re-write then in COBOL under Windows. That'll
make it much easier.
```

#### ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<352c326f.1830517@news.wwa.com>`
- **References:** `<352c326f.1830517@news.wwa.com>`

```

Paul,

I believe a company called Transoft sell a product called u/SQL which
provides an ODBC interface to COBOL files on UNIX.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus UK.

Paul DuBois wrote in message <352··.@new··a.com>...
› Hello,
› 
…[13 more quoted lines elided]…
› Paul
```

##### ↳ ↳ Re: Any way to access MF Indexed files on Unix from Windows?

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6a2d200cf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d6a2d200cf-p6@usenetarchives.gap>`
- **References:** `<352c326f.1830517@news.wwa.com> <gap-d6a2d200cf-p6@usenetarchives.gap>`

```

In article <6gddeb$i.··.@hyp··o.uk>, p.··.@mfl··o.uk says...
›
› Paul,
›
› I believe a company called Transoft sell a product called u/SQL which
› provides an ODBC interface to COBOL files on UNIX.

Paul made no mention of databases in his original post so I find this
reccomendation odd. If he's just using standard COBOL indexed files, u/SQL or
some other ODBC database bridge isn't going to help. Going SQL/ODBC will
probably slow the application down although that really depends on the design.

Paul, Try looking at Fileshare/2 and CCI which are Micro Focus products
available on Windows and UNIX. I've done the exact same thing myself using
TCP/IP but to another Windows box (NT Server to be exact). I actually use a
predecessor to Fileshare/2 called Pedro but the technology is more or less the
same. Common ancestory for the two. CCI is used as the abstract transport
layer. I've also done a virtual interface that sits on top to allow
Fileshare/2 access to SQL databases but that's another matter.

You could also use the CCI interface for more than file transfers.

Shaun

› Paul DuBois wrote in message <352··.@new··a.com>...
›› Hello,
…[16 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
