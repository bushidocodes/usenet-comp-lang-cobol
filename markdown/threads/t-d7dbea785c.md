[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# can cobol handle the handle?

_16 messages · 9 participants · 2004-01_

---

### can cobol handle the handle?

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-01-05T08:01:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0401050801.418ca226@posting.google.com>`

```
Hello everyone,

when we use the cobol command 'open i-o indexed-file', is there a way
that I can get or obtain the file handle from the cobol runtime system?
I need to use some win32 api functions and I must provide the file handle
on entry as a call parameter. I am using Net Express 3.1 with windows 2000.

thanks a lot for your kind help, Kellie.
```

#### ↳ Re: can cobol handle the handle?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-01-05T18:03:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com>`

```
"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0401050801.418ca226@posting.google.com...

> when we use the cobol command 'open i-o indexed-file', is there a way
> that I can get or obtain the file handle from the cobol runtime system?
> I need to use some win32 api functions and I must provide the file handle
> on entry as a call parameter. I am using Net Express 3.1 with windows
2000.

I do not have the answer, but...

There is more than one system handle here, one for the data file and one for
the index file.

Maybe you should just "COBOL-OPEN"  indexed-file SHARED, and simultaneously
open the two files (the data file AND the index file!) with CreateFile (also
shared) and you'll get valid system handle(s) to the same physical file(s).

I just can't see how the system file handle(s) obtained by NetExpress under
these conditions is(are) anything but pretty useless. (Sorry, I cannot
imagine what API call you could be trying to use here... Oh, wait a
minute... one of the NetApi's so you can find "who" has the file open? Well,
the above suggestion handles that, too. If that's a bad guess on my part,
can you describe your challenge in application terms?).
```

##### ↳ ↳ Re: can cobol handle the handle?

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-01-05T15:24:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0401051524.6d11c4cd@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<RFhKb.20986

Michael wrote:
can you describe your challenge in application terms?.

Kellie wrote:
I am trying to use the following win32 api function:

1). call "GetFileSizeEx" (get file size in bytes)
2). call "GetFileInformationByHandle" (have two copies of the same
          file on the hard drive, so we check for duplicates or not).
3). call "GetFileType" (check for disk file)

regards, kellie.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-01-05T23:58:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com>`

```
"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0401051524.6d11c4cd@posting.google.com...
> "Michael Mattias" <michael.mattias@gte.net> wrote in message
news:<RFhKb.20986
>
> Michael wrote:
…[5 more quoted lines elided]…
> 1). call "GetFileSizeEx" (get file size in bytes)

Use FindFirstFile against indexed-file. That will return a 64-bit size in
the WIN32_FIND_DATA structure.  (Not that that is going to be meaningful,
read on).

> 2). call "GetFileInformationByHandle" (have two copies of the same
>           file on the hard drive, so we check for duplicates or not).

???  Indexed-file in your program should have the name of your file, but if
you are talking about problems with "paths" you can take a look at the
GetFullPathName API. That will get you the fully-qualified name from a
relative name.  GetFileInformationByHandle would get the filesize,
attributes etc , too, but you can get the same info from FindFirstFile in
the WIN32_FIND_DATA structure.

If you want to conduct a search for a file, see the SearchPath API function.

> 3). call "GetFileType" (check for disk file)

Why call it? In this case, it will always return FILE_TYPE_DISK. Well, on
further review, I guess it could be a FILE_TYPE_PIPE because....

...in any event, the COBOL "OPEN I-O indexed-file"  may refer to ONE or TWO
(or more, I guess) physical files, and how you get to the individual
physical names from the COBOL 'OPEN'  verb is implementor-defined.

I.e., you might specifiy
indexed-file      PIC X(260) VALUE IS "myfile".

.. and the compiler will go looking for "myfile.IDX", which contains the
name of a separate datafile "myfile.dat".. or maybe vice-versa.

Bottom line...
To get the file size of a file for which you know the name, use
FindFirstFile
To determine the fully qualified name of a file for which you only have a
relative path name, use GetFullPathName
To search for a file along either the default or a custom path list, use
SearchPath

For professional assistance re using the WIndows API (with COBOL or 'all by
itself') ...
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 4)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2004-01-06T01:30:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com>`

```

Michael Mattias <michael.mattias@gte.net> wrote in message news:1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com...
>
> For professional assistance re using the WIndows API (with COBOL or 'all by
…[5 more quoted lines elided]…
> mmattias@talsystems.com

What do you think about Microsoft's plan to replace
the Win 32 API ?
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-06T11:13:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81f64069d13ced4cb906b49f0de42467@news.teranews.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com> <JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote:
>
> What do you think about Microsoft's plan to replace the Win 32 API?

I don't like Steve Jobs, he is a serious jerk. But Jobs said one thing that
struck me with astounding clarity. (paraphrase) "It is not in Microsoft's
interests to make programming easier. What do they care if it costs one
or two million dollars more for the next release of Office? But it matters
to all the smaller developers with whom they compete." When you sell
10+ million copies of a several hundred dollar product, a $.10 higher
development cost per item is negligible. Also, Microsoft makes lots of
money from selling training and manuals. Microsoft isn't happy just
adding new features, they want to make you relearn stuff you already
know. Notice that in every release of Microsoft Office, for example,
they change the way you execute some common commands. Not to make
it better, just different. Every time they make a major change in the API
or user interface it is a windfall for them, though a pain in the neck for
everybody else. People buy more training and manuals, and are
prompted to upgrade their obsolete software, that still works perfectly,
just to get the new gee-whiz stuff.

This shouldn't be surprising, the auto manufacturers have done this for
decades.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-01-06T10:48:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KbudnR0j7d5fe2eiRVn-tw@giganews.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com> <JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net> <81f64069d13ced4cb906b49f0de42467@news.teranews.com>`

```
Judson McClendon wrote:
>
> This shouldn't be surprising, the auto manufacturers have done this
> for decades.

This is the problem for monopolies and near-monopolies. Their biggest
competitor is their own company.

In the case of software, autos, or other durable goods, the company has to
offer a better, or perceived better, product else their revenue stream just
damn STOPS.

Innovate or die is the motto.

This is obviously not the case with consumables - those companies use other
tactics. For example, Rockefeller managed to drop the price of kerosene from
$3.00/gallon to less than five cents within three years. In so doing, he
dramatically increased his customer base (and destroyed the whale-oil
business).
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-06T16:47:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401061647.582abc4c@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com> <JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net> <81f64069d13ced4cb906b49f0de42467@news.teranews.com> <KbudnR0j7d5fe2eiRVn-tw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> This is obviously not the case with consumables - those companies use other
> tactics. For example, Rockefeller managed to drop the price of kerosene from
> $3.00/gallon to less than five cents within three years. In so doing, he
> dramatically increased his customer base (and destroyed the whale-oil
> business).

First of all your figures are wrong:

"""Standard Oil began in 1870, when kerosene cost 30 cents a gallon.
By 1897, Rockefeller's scientists and managers had driven the price to
under 6 cents per gallon, ..."""

But this wasn't just because he was a good guy and wanted to help
consumers:

""" ... and many of his less-efficient competitors were out of
business -including companies whose inferior grades of kerosene were
prone to explosion and whose dangerous wares had depressed the demand
for the product."""

It was also to drive the competitors out of the market - those making
kerosene, not just whale oil. Not only would that low price drive
existing manufacturers out, but it acted as a barrier from anyone else
entering the market.  Standard Oil could make a profit at that price
because they had large volumes and a captive distribution network, but
also kerosene is a byproduct of petrol production which was increasing
at about 40% a year and so the total kerosene market had to be
increased otherwise it would be a waste product.

The 1870s was also a highly deflationary time when prices for
everything fell.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-07T14:28:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bth522$dhr$1@peabody.colorado.edu>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com> <JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net> <81f64069d13ced4cb906b49f0de42467@news.teranews.com> <KbudnR0j7d5fe2eiRVn-tw@giganews.com>`

```

On  6-Jan-2004, "JerryMouse" <nospam@bisusa.com> wrote:

> This is obviously not the case with consumables - those companies use other
> tactics. For example, Rockefeller managed to drop the price of kerosene from
> $3.00/gallon to less than five cents within three years. In so doing, he
> dramatically increased his customer base (and destroyed the whale-oil
> business).

And for these evils, the feds broke up his company - unlike the other examples
in this thread.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-01-06T14:12:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BnzKb.21418$P%1.20588761@newssvr28.news.prodigy.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com> <1TmKb.21124$P%1.20308181@newssvr28.news.prodigy.com> <JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message
news:JcoKb.284762$Ec1.9812117@bgtnsc05-news.ops.worldnet.att.net...
>
>
> What do you think about Microsoft's plan to replace
> the Win 32 API ?

Apparently not much, since no such article/message/announcement has caught
my eye, and I'm pretty likely to have  followed up on that sort of thing.

Besides, there are more than enough machines out there that I will have
business until it's time for me to start cashing the Social Security checks.
Were I twenty years younger, I might be concerned, but as things stand I'm
not losing any sleep.

MCM
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-05T20:10:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OYnKb.4586$k_.552331@news20.bellglobal.com>`
- **In-Reply-To:** `<41758a6b.0401051524.6d11c4cd@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <RFhKb.20986$P%1.20199178@newssvr28.news.prodigy.com> <41758a6b.0401051524.6d11c4cd@posting.google.com>`

```
KELLIE FITTON wrote:
> "Michael Mattias" <michael.mattias@gte.net> wrote in message news:<RFhKb.20986
> 
…[11 more quoted lines elided]…
> regards, kellie.

If you are using MS or Fujutsu, there is a subrourine library that 
returns those values for you.  Look for the CBL_(other stuff) routines 
in the software installation areas.  I expect all the other PC Cobols 
have similar libraries. Under MF, you can find it in the help files. 
With Fujitsu, you will have to search the PDF manuals.

There are lots of other primitives in those libraries, as well.  They 
are worth exploring.

Donald
```

#### ↳ Re: can cobol handle the handle?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-05T10:31:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401051031.7a0142d0@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com>`

```
KELLIEFITTON@YAHOO.COM (KELLIE FITTON) wrote

> when we use the cobol command 'open i-o indexed-file', is there a way
> that I can get or obtain the file handle from the cobol runtime system?
> I need to use some win32 api functions and I must provide the file handle
> on entry as a call parameter. I am using Net Express 3.1 with windows 2000.

It is unlikely taht there is anything useful that you could do on an
indexed file using Win32 API functions that require a file handle.

Which particular functions were you intending to use and what did you
hope to achieve.
```

##### ↳ ↳ Re: can cobol handle the handle?

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-01-05T15:26:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0401051526.64505179@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <217e491a.0401051031.7a0142d0@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0401051031.7a0142d0@posting.google.com>...

riplin wrote:
Which particular functions were you intending to use and what did you
hope to achieve.

Kellie wrote:
I am trying to use the following win32 api function:

1). call "GetFileSizeEx" (get file size in bytes)
2). call "GetFileInformationByHandle" (have two copies of the same
          file on the hard drive, so we check for duplicates or not).
3). call "GetFileType" (check for disk file)

regards, kellie.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-05T18:56:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401051856.7eb2ce38@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <217e491a.0401051031.7a0142d0@posting.google.com> <41758a6b.0401051526.64505179@posting.google.com>`

```
In this case - obtain your file handle not by using a COBOL Open, but
instead by usng CreateFile or CreateFileEx API's.  CreateFile is a
misleading name because it is also used to open and not create an
existing data file - but it's the API you want.


KELLIEFITTON@YAHOO.COM (KELLIE FITTON) wrote in message news:<41758a6b.0401051526.64505179@posting.google.com>...
> riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0401051031.7a0142d0@posting.google.com>...
> 
…[12 more quoted lines elided]…
> regards, kellie.
```

###### ↳ ↳ ↳ Re: can cobol handle the handle?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-05T19:24:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401051924.2f9529c8@posting.google.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com> <217e491a.0401051031.7a0142d0@posting.google.com> <41758a6b.0401051526.64505179@posting.google.com>`

```
KELLIEFITTON@YAHOO.COM (KELLIE FITTON) wrote 

> riplin wrote:
> Which particular functions were you intending to use and what did you
…[5 more quoted lines elided]…
> 1). call "GetFileSizeEx" (get file size in bytes)

You don't need to use a file handle to get the file size, it can be
done using the name.  For example run a command 'DIR name >dirlist'
and this file contains the file size.

> 2). call "GetFileInformationByHandle" (have two copies of the same
>           file on the hard drive, so we check for duplicates or not).

'Two copies' must be different names or be in different directories. 
If there are two files that you have opened and you could obtain the
handles then what would the 'file information' tell you that will
determine that they are or are not duplicates.

Even if they are the same size and date/time this does not mean they
are identical.  Only reading all the records will tell you that.

> 3). call "GetFileType" (check for disk file)
 
As distinct from what ?

Are any of these of any practical use or are you just playing ?

Why not use a WinAPI function to open the file and get a file handle
that way ?
```

#### ↳ Re: can cobol handle the handle?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-01-06T10:49:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k9mdnVvMt_WGemei4p2dnA@giganews.com>`
- **References:** `<41758a6b.0401050801.418ca226@posting.google.com>`

```
KELLIE FITTON wrote:
> Hello everyone,
>
…[7 more quoted lines elided]…
> thanks a lot for your kind help, Kellie.

With COBOL, you don't need no stinkin' file handle.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
