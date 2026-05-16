[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# how to convert packed COBOL data?

_8 messages · 6 participants · 2000-06_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Help requests and how-to`](../topics.md#help)

---

### how to convert packed COBOL data?

- **From:** "Heini" <no.spam@online.de>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8il589$9q0$1@news.online.de>`

```
I'm receiving packed COBOL data - integers (P), single precisions or
currencies (P), dates (D) - in a file and must read out these values using
Visual Basic.
Checking the file under DOS I found they contain ascii chars < 20H. Where
can I
found some information to convert these byte fields into text fields?

Heini
```

#### ↳ Re: how to convert packed COBOL data?

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394e6ba0.11284135@news.transport.com>`
- **References:** `<8il589$9q0$1@news.online.de>`

```
I think there are tool kits for this, and several people can probably
provide you with home-grown solutions.

However, in my opinion the BEST solution is to modify the program that
builds this data for you to re-format it into non-packed.   The reason
I say this is because if the data is going through an EBCDIC to ASCII
conversion, it is possible for valid EBCDIC packed numbers to cause
things to go bonkers during the conversion to ASCII.

As a rule, we NEVER process packed data in ASCII here....

Pete


On Mon, 19 Jun 2000 14:53:21 +0200, "Heini" <no.spam@online.de> wrote:

>I'm receiving packed COBOL data - integers (P), single precisions or
>currencies (P), dates (D) - in a file and must read out these values using
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: how to convert packed COBOL data?

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394ED928.3A5F@NOSPAMguysoftware.com>`
- **References:** `<8il589$9q0$1@news.online.de> <394e6ba0.11284135@news.transport.com>`

```
Parser/Converters like ParseRat (http://www.guysoftware.com/parserat.htm) can convert 
files like that.  They can also make allowances for files which started off as EBCDIC 
and got garbled by the default character conversions to ASCII when moving from the 
mainframe to the PC.


Pete Wirfs wrote:
> 
> I think there are tool kits for this, and several people can probably
…[23 more quoted lines elided]…
> >
```

#### ↳ Re: how to convert packed COBOL data?

- **From:** Alexander Meins <alex@nikocity.de>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394E6D20.22CDB01D@nikocity.de>`
- **References:** `<8il589$9q0$1@news.online.de>`

```
A usual format for numeric values in COBOL is PACKED.
The number +123456 would be Hex '0123456F'. Where F is
the sign (positive). C is also positive, D is negative.

Alex

Heini wrote:
> 
> I'm receiving packed COBOL data - integers (P), single precisions or
…[6 more quoted lines elided]…
> Heini
```

##### ↳ ↳ Re: how to convert packed COBOL data?

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394eb188.29180479@news.transport.com>`
- **References:** `<8il589$9q0$1@news.online.de> <394E6D20.22CDB01D@nikocity.de>`

```
But it does *NOT* look like '0123456F' if it has been converted to
ASCII.  (And Visual Basic is usually running with ASCII data.)

Pete


On Mon, 19 Jun 2000 20:57:36 +0200, Alexander Meins <alex@nikocity.de>
wrote:

>A usual format for numeric values in COBOL is PACKED.
>The number +123456 would be Hex '0123456F'. Where F is
…[18 more quoted lines elided]…
>http://www.gohip.com/free_video/
```

###### ↳ ↳ ↳ Re: how to convert packed COBOL data?

- **From:** Alexander Meins <alex@nikocity.de>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395666FD.9ED5019B@nikocity.de>`
- **References:** `<8il589$9q0$1@news.online.de> <394E6D20.22CDB01D@nikocity.de> <394eb188.29180479@news.transport.com>`

```
How do you convert a EBCDI code of X'0123456F' to ASCII then??

A.

Pete Wirfs wrote:
> 
> But it does *NOT* look like '0123456F' if it has been converted to
…[27 more quoted lines elided]…
> >http://www.gohip.com/free_video/
```

#### ↳ Re: how to convert packed COBOL data?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uo445.117$az.54490@dfiatx1-snr1.gtei.net>`
- **References:** `<8il589$9q0$1@news.online.de>`

```
1. Read and/or download:
http://www.flexus.com/ebd2asc.html

This explains the difference between IEEE and COBOL datatypes, and also
deals with EBCDIC/ASCII conversions: A brilliant treatise by a talented
programmer and writer. (Me). (It's not visually too appealing, but I'm not
an artist type at all).

2. Conversion, huh? It just so happens that I am looking for a VB-programmer
type to use my FREE (*) 32-bit DLL which converts COBOL to IEEE data, as
well as doing EBCDIC to ASCII conversions.

I have a complete kit with PowerBASIC souce code, test files, executables,
etc which you can use to convert COBOL data to somehting VB can read. Write
directly to me with a reply e-mail-address.

(*) Free - almost: I INSIST that you "pay" for your use of this product by
doing me the courtesy of letting me know how it worked out, what was
unclear/wrong/missing from the documentation, etc. So far for the
twenty-seven kits I have sent I have received only, "well, I haven't gotten
around to it yet..." and often that's been because I sent a followup.
(Except for one guy, who did comment as requested).
```

##### ↳ ↳ Re: how to convert packed COBOL data?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3951070A.A2488A1@home.com>`
- **References:** `<8il589$9q0$1@news.online.de> <Uo445.117$az.54490@dfiatx1-snr1.gtei.net>`

```


Michael Mattias wrote:
> 
> 1. Read and/or download:
…[4 more quoted lines elided]…
> programmer and writer. (Me). (It's not visually too appealing,

OOohhhh !

> but I'm not an artist type at all).

Now there's a refutation of the famous quote, from the author, no less
<G>

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
