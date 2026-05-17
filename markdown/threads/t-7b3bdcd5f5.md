[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using HP laserjet 5 with COBOL

_7 messages · 7 participants · 1997-08_

---

### Using HP laserjet 5 with COBOL

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1997-08-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33F1DD60.417@best.com>`

```

Hello:
Has anyone attached an HP laser to an IBM Mainframe? I am a COBOL
Programmer that has to replace a vintage Xerox 3700 with an HP Laserjet
5Si Mx. Any ideas on SNA/to ethernet conversion cards? I'm going
to have to send an escape sequence to the printer to print barcodes.
I'm hopeing to use forms saved on the printers hard disk. Any
suggestions about form drawing software that generates PCL or
Postscript?

Thanks a million!
Chris Mason
h.c··.@lm··o.com
and
hcm··.@be··t.com
```

#### ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33F1DD60.417@best.com>`
- **References:** `<33F1DD60.417@best.com>`

```

Chris Mason wrote:
› 
› Hello:
…[12 more quoted lines elided]…
› hcm··.@be··t.com
You have a couple options:

(1) Get an external 'protocol converter'. This is a little box typically
with a (3270) coax connector on one side and an RS-232 connector on the
other, from I-O Data or Intermate. If you're sending barcodes from the
host via AFP, you'll need one that supports AFP. But if you were using a
Xerox printer, you might be calling up fonts internal to the printer
through control codes. In this case, there are protocol converters that
do the bar-coding as well, but you may have to modify your data stream.
Call the guy you got the HP 5si from or maybe Anixter (Black Box is
over-priced). It'll probably run you around $1,000-$1,200.

(2) Same as above, but you can get a protocol converter card that slips
into one of the 5si's MIO slots (We have a Lexmark Optra N model 240
which is a first cousin to the 5si setup exactly this way).

(3) If your printer is LAN attached, you can buy software to route the
print jobs over the LAN, like Novell Hostprint or one of BARR systems'
products. However, you might lose a little control going this route
because your host operators might not be able to accurately monitor the
print jobs from their consoles. The 5si *does* support multiple
concurrent interfaces, though, so it can service print jobs from your
LAN via, say, Ethernet, and your host via a protocol converter (card)
seamlessly.

Hope this helps :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "colin campbell" <ua-author-181794@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33F1DD60.417@best.com>`
- **References:** `<33F1DD60.417@best.com>`

```

Chris Mason wrote:
› 
› Hello:
…[12 more quoted lines elided]…
› hcm··.@be··t.com

Chris,
Our shop uses a product named VPS, from Levi, Ray, and Shoup (Web
address http://www.lrs.com, phone (217) 793-3800). I wonder if the last
four digits of the number constitute a clue to their business?

Anyway, as well as I understand it, VPS takes output from the MVS sysout
queues, translates it to the appropriate HP LaserJet commands, and ships
it via several network protocols to the designated printer.

We moved locations, and the management wanted to dump the last IBM 38nn
printers, so they decided to use this product set. I was skeptical, but
I have printed output which uses simple line printing like compiles, and
complex page printing (pagedefs, formdefs, and GDDM graphics). I guess
I'm a believer. It's hard to tell from your note if maybe you're a
small shop, and I don't know the costs, so you'll have to check the VPS
product for applicability to your situation.
Colin Campbell
(my opinions only)
```

#### ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-08-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33F1DD60.417@best.com>`
- **References:** `<33F1DD60.417@best.com>`

```

There are any number of conversion products available. Axis
Communications, Black Box, and a few dozen (at least) other companies make
and sell them. Just about any LAN/Communications distributor will have a
section in their catalog for Twinax to HP, Coax (3270) to HP, etc.

Alternatively, if you have TCP/IP for MVS on your mainframe, and are hooked
to something (Token-Ring, etc.) with a route to your LAN, you should be
able to spool out to the LPR mode on the HP. There are various software
products to run on the MVS side to manage this, which will convert AFP
formats to PCL for you on the fly.

If you want to go direct channel attach, you probably have a real problem.
There was a product we used years ago that would attach to a channel (bus
and tag) on one side, and a centronics port on the other, but I have no
idea who made it, or whether it is still available.

On the Postscript side, Script/VS will output postscript. It is also
possible to write a Postscript program to interpret other print command
sets (a good example is the Daisyprint routine bundled into many products,
like Paradox 4.x). I have run Script/VS output to a 5si with excellent
results. Alternatively (if you haven't already bought the printer), look
at the Lexmark line. They include PPDS, along with Postscript and PCL, in
many of their 40x9 series, which you can run direct from AFP.

Chris Mason wrote in article <33F··.@be··t.com>...
› Hello:
› Has anyone attached an HP laser to an IBM Mainframe?  I am a COBOL
…[12 more quoted lines elided]…
›
```

#### ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "rber..." <ua-author-17072445@usenetarchives.gap>
- **Date:** 1997-08-15T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<33F1DD60.417@best.com>`
- **References:** `<33F1DD60.417@best.com>`

```

Chris Mason wrote:

› Hello:
› Has anyone attached an HP laser to an IBM Mainframe?  I am a COBOL
…[6 more quoted lines elided]…
› 
You can attach your printer on a micro with a 3270 emulation and send
to this printer all data (with escape sequence).
If you can alter your program (source), is very simple to add escape
sequence "HardCode" but if your escape sequence are in an external
file you can change your printer with no alter your program (only
update escape sequen in file).

BYE RBL
*****************************************
* Raymond BERTHOU *
* E-Mail mailto:rbe··.@pra··e.fr *
* Url: http://www.pratique.fr/â€¾rberthou *
* ou http://www.mygale.org/06/rbl *
*****************************************
```

##### ↳ ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "msl..." <ua-author-10897826@usenetarchives.gap>
- **Date:** 1997-08-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b3bdcd5f5-p5@usenetarchives.gap>`
- **References:** `<33F1DD60.417@best.com> <gap-7b3bdcd5f5-p5@usenetarchives.gap>`

```

Raymond BERTHOU (rbe··.@pra··e.fr) wrote:
:>You can attach your printer on a micro with a 3270 emulation and send
:>to this printer all data (with escape sequence).
:>If you can alter your program (source), is very simple to add escape
:>sequence "HardCode" but if your escape sequence are in an external
:>file you can change your printer with no alter your program (only
:>update escape sequen in file).


This is true in principle but may be hard in practice, since many
communication products erase low value hex characters.

Things to look out for:
1. Emulation translation tables
2. TP monitor quirks (IMS for example erase small values, and put X'00'
instead)
3. VTAM/controller/gw configuartion

But if you work direclty with VTAM support (like using VPS [heard of
VPS/PCL btw?? seems like what you need]), you should be fine.

Otherwise this may not be all that trivial.

Good luck.

Will be happy to hear how you succeed.
```

###### ↳ ↳ ↳ Re: Using HP laserjet 5 with COBOL

- **From:** "mslamm" <ua-author-10667488@usenetarchives.gap>
- **Date:** 1997-08-21T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b3bdcd5f5-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b3bdcd5f5-p6@usenetarchives.gap>`
- **References:** `<33F1DD60.417@best.com> <gap-7b3bdcd5f5-p5@usenetarchives.gap> <gap-7b3bdcd5f5-p6@usenetarchives.gap>`

```

››
›› But if you work direclty with VTAM support (like using VPS [heard of
›› VPS/PCL btw?? seems like what you need]), you should be fine.
› What is VPS ?


VPS == VTAM Printer Support is a product that allows you to print
direclty to VTAM printers (they act like external writers, in your JCL).
The product is a leader in this category.

VPS/PCL is the support for PCL (that is HP) laser printers.

Ehud

Ehud Lamm msl··m@plu··c.il
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
