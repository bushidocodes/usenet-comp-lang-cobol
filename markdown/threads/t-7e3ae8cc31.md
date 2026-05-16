[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Resources for Microsoft COBOL?

_14 messages · 12 participants · 2002-10 → 2003-01_

---

### Resources for Microsoft COBOL?

- **From:** "iinetnews" <david@somewh.ere>
- **Date:** 2002-10-07T07:24:00+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
I have dusted off my venerable Microsoft COBOL.
Is there any support for this anywhere?

Although DOS-based it can do system calls so I am
wondering if I can use it to communicate using tcp/ip.
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-10-06T22:56:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-pP6mozORV7TX@h24-82-204-17.wp.shawcable.net>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
On Sun, 6 Oct 2002 22:24:00 UTC, "iinetnews" <david@somewh.ere> wrote:

> I have dusted off my venerable Microsoft COBOL.
> Is there any support for this anywhere?
…[4 more quoted lines elided]…
> 

You won't have much luck doing Windows API calls unless you can get 
the 16 bit Windows development kit.
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-10-06T22:45:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0210062145.3bd4e4e0@posting.google.com>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
"iinetnews" <david@somewh.ere> wrote

> I have dusted off my venerable Microsoft COBOL.
> Is there any support for this anywhere?

Not for several years.
 
> Although DOS-based it can do system calls so I am

That depends on version, which you didn't specify.  MS Cobol 4.5 does
DOS, OS/2 1.x and Windows 3.1x.  MS Cobol 5.0 dropped OS/2.

> wondering if I can use it to communicate using tcp/ip.

What did you want to do ?  MS Cobol 4.5 and 5.0 can do CGI Web serving
on Windows and OS/2, for example with Xitami Web Server
(www.xitami.com).
There are even Web Servers that can run DOS programs as CGI scripts.
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-10-07T12:40:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DA18248.10000@nycap.rr.com>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
If I remember correctly Microsoft COBOL was really MicroFocus COBOL 
marketed by Microsoft.  (I have a DOS version too, but I think some of 
my 5-1/4 floppies have had some bytes drop off and are now unusable. 
Besides, I don't have a 5-1/4 floppy drive on my PC (just 3-1/2 and CD).

As far as support, well... you could try the MicroFocus site or check 
out some of the "discontinued & discounted" book bins at places like 
Barns & Nobel for books covering Micro Focus Cobol for DOS.

Other than that, you'll just have to brute force try it.

iinetnews wrote:
> I have dusted off my venerable Microsoft COBOL.
> Is there any support for this anywhere?
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2002-10-08T10:54:06+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<anu320$gl5$1@usenet.otenet.gr>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
Keep in mind that this is a 16bit software.

I'm not sure if it will do for TCP/IP programming under todays 32bit
Windows.

regards

Panos

"iinetnews" <david@somewh.ere> wrote in message
news:3da0b339$0$9156$5a62ac22@freenews.iinet.net.au...
> I have dusted off my venerable Microsoft COBOL.
> Is there any support for this anywhere?
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** Brian Walker <walkerbj@optus(remove)net.com.au>
- **Date:** 2002-10-10T11:25:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns92A3DA3E83A28walkerbjoptusnetcoma@210.49.20.254>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```
"iinetnews" <david@somewh.ere> wrote in news:3da0b339$0$9156$5a62ac22
@freenews.iinet.net.au:

> I have dusted off my venerable Microsoft COBOL.
> Is there any support for this anywhere?
…[4 more quoted lines elided]…
> 

I have the manuals for version 3, but I tossed the software many years ago. 
If you have specific queries I am happy to try and find answers in the 
books. By the way it is Micro focus rebadged as Microsoft. The manauls are 
really very good, which was why I checked if it was really Microsoft or 
not.
Cheers.
```

#### ↳ Re: Resources for Microsoft COBOL?

- **From:** mcldev <member@dbforums.com>
- **Date:** 2002-12-27T05:04:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2320431.1040965490@dbforums.com>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au>`

```

Speak of blowing the dust off, well I dug up an old floppy or two and
managed to install MS Cobol 3.00A and to my delight it still works.
However certain verbs are not fully implemented, like INSPECT for
example.  So I humbly ask all gurus where in the heck can I get a patch
to this outdated sucker?

Thanks Mike
```

##### ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-27T14:30:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PtZO9.3509$qU5.2701070@newssrv26.news.prodigy.com>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com>`

```
"mcldev" <member@dbforums.com> wrote in message
news:2320431.1040965490@dbforums.com...
>
> Speak of blowing the dust off, well I dug up an old floppy or two and
…[3 more quoted lines elided]…
> to this outdated sucker?

If you can handle the "no" or even a "you have got to be kidding" you can
contact the publisher:

Microsoft Corporation
One Microsoft Way
Redmond WA 98052-6399
Sales Info: 1-800-426-9400

Microsoft must have been out of the COBOL business for ten years; and even
at that, I believe "Microsoft" COBOL was a private-labelled Microfocus
product.

If you have your heart set on PC COBOL better you should start looking at
current offerings. (Or figure out how to get the job done with the more
limited version of INSPECT).
```

###### ↳ ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** "Vince Coen" <Vince_Coen@f609.n257.z2.fidonet.org>
- **Date:** 2002-12-27T23:26:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1041031244@f609.n257.z2.fidonet.ftn>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com> <PtZO9.3509$qU5.2701070@newssrv26.news.prodigy.com>`

```
Hello Michael!

27 Dec 02 14:30, Michael Mattias wrote to All:

 >> Speak of blowing the dust off, well I dug up an old floppy or two
 >> and managed to install MS Cobol 3.00A and to my delight it still
 >> works. However certain verbs are not fully implemented, like INSPECT
 >> for example.  So I humbly ask all gurus where in the heck can I get
 >> a patch to this outdated sucker?

 MM> Microsoft must have been out of the COBOL business for ten years; and
 MM> even at that, I believe "Microsoft" COBOL was a private-labelled
 MM> Microfocus product.

Only from version 4.5. Previous version was either MS or another vendor and 
bought in to MS. I still have version 4.5 around as well as MF v3.1.



Vince
```

##### ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-28T11:08:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E0D863D.9CDB8E60@Azonic.co.nz>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com>`

```
mcldev wrote:
> 
> Speak of blowing the dust off, well I dug up an old floppy or two and
…[3 more quoted lines elided]…
> to this outdated sucker?

The 'patches' were called MS Cobol versions 4.0, 4.5 and 5.0.  These
have not been available for quite some time.
```

###### ↳ ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-28T18:51:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021228135136.13293.00000363@mb-fr.aol.com>`
- **References:** `<3E0D863D.9CDB8E60@Azonic.co.nz>`

```
I still have version 1.12 of microsoft cobol. but would prefer to have a more
up to date copy than that !  
  RonGlaz6@aol.com
in Los Angeles
```

##### ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2002-12-29T12:49:24
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aumr0k$27d$1@newsg4.svr.pol.co.uk>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com>`

```
Post a request to the ng :

    alt.binaries.warez.ibm-pc.old

"mcldev" <member@dbforums.com> wrote in message
news:2320431.1040965490@dbforums.com...
>
> Speak of blowing the dust off, well I dug up an old floppy or two and
…[8 more quoted lines elided]…
> Posted via http://dbforums.com
```

###### ↳ ↳ ↳ Re: Resources for Microsoft COBOL?

- **From:** robin lee <robinlee@rr.com>
- **Date:** 2003-01-03T04:04:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E150A2A.5B5C294F@rr.com>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com> <aumr0k$27d$1@newsg4.svr.pol.co.uk>`

```
 
> "mcldev" <member@dbforums.com> wrote in message
> news:2320431.1040965490@dbforums.com...
…[6 more quoted lines elided]…
> >

  MS Cobol v3.0 does indeed support the INSPECT verb.  It is a full
implementation of the Cobol 85 standard.

  I still use a number of utilities which I had created with this
compiler. They work so well that it hasn't been worth the effort to
convert them to any newer product.

  Versions 3 thru 5 were customized versions of the Microfocus product,
but there was no correlation between the MS and MF version numbers.
```

###### ↳ ↳ ↳ Re: Resources for Microsoft COBOL?

_(reply depth: 4)_

- **From:** "zfty" <ss@ss.org>
- **Date:** 2003-01-04T21:05:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e17302f.0@news1.mweb.co.za>`
- **References:** `<3da0b339$0$9156$5a62ac22@freenews.iinet.net.au> <2320431.1040965490@dbforums.com> <aumr0k$27d$1@newsg4.svr.pol.co.uk> <3E150A2A.5B5C294F@rr.com>`

```
try using EXAMINE ?

"robin lee" <robinlee@rr.com> wrote in message
news:3E150A2A.5B5C294F@rr.com...
>
> > "mcldev" <member@dbforums.com> wrote in message
…[5 more quoted lines elided]…
> > > example.  So I humbly ask all gurus where in the heck can I get a
patch
> > > to this outdated sucker?
> > >
…[9 more quoted lines elided]…
> but there was no correlation between the MS and MF version numbers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
