[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# translate from EBCDIC to ASCII

_6 messages · 5 participants · 2000-02_

---

### translate from EBCDIC to ASCII

- **From:** "Joe" <jleary@vr.state.ut.us>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88f1mb$hp0$1@coward.ks.cc.utah.edu>`

```
Hi all,

Anyone have a routine to translate standard text from mainframe (EBCDIC) to
PC (ASCII)?  I FTP a file to my PC and need to translate to ASCII,
preferably with Fujitsu COBOL.

TIA

Joe
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88f6c2$rui$1@nntp4.atl.mindspring.net>`
- **References:** `<88f1mb$hp0$1@coward.ks.cc.utah.edu>`

```
If all of the fields are either PIC X or PIC 9 (with no signs - or sign is
separate) then you should just be able to specify "EBCDIC" to "ASCII"
conversion when doing the download.

If, HOWEVER, you have any COMP, Binary, Packed-Decimal, or "included signs",
then you will need to write a simple program. This can be done by "moving"
you input to an output field converting from "internal" format to "external
format".  To do this, you should probably look at the CODE-SET clause.  The
Standard says that you can't use this with files that have computational
usages, but many implementors don't enforce this.
```

##### ↳ ↳ Re: translate from EBCDIC to ASCII

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000217081316.08112.00000562@nso-ce.aol.com>`
- **References:** `<88f6c2$rui$1@nntp4.atl.mindspring.net>`

```
In article <88f6c2$rui$1@nntp4.atl.mindspring.net>, "William M. Klein"
<wmklein@nospam.netcom.com> writes:

>
>If all of the fields are either PIC X or PIC 9 (with no signs - or sign is
>separate) then you should just be able to specify "EBCDIC" to "ASCII"
>conversion when doing the download.
>

I don't know about your setup, but when I FTP the default is to translate
from EBCDIC to ASCII.   If there are COMP, COMP-3 fields in the file
you MUST specify BINARY mode before issuing the GET.
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ABDEC9.AEBEC402@zip.com.au>`
- **References:** `<88f1mb$hp0$1@coward.ks.cc.utah.edu>`

```
Joe wrote:
> 
> Hi all,
…[3 more quoted lines elided]…
> to ASCII, preferably with Fujitsu COBOL.

C program forwarded to Joe,  available on request (exe and source)

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000217081317.08112.00000563@nso-ce.aol.com>`
- **References:** `<88f1mb$hp0$1@coward.ks.cc.utah.edu>`

```
In article <88f1mb$hp0$1@coward.ks.cc.utah.edu>, "Joe" <jleary@vr.state.ut.us>
writes:

>Anyone have a routine to translate standard text from mainframe (EBCDIC) to
>PC (ASCII)?  I FTP a file to my PC and need to translate to ASCII,
>preferably with Fujitsu COBOL.
>
>

If you have the Data Tools package that came with the Fujitsu COBOL CD,
you can supply a file layout/copylib to the Data Converter tool and it will
translate
the EBCDIC file to ASCII including all COMP and COMP-3 fields.
I have used this extensively to test my mainframe programs on the PC before
compiling them on the mainframe for production.
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1317fe99f30f3e8598986e@news.mersinet.co.uk>`
- **References:** `<88f1mb$hp0$1@coward.ks.cc.utah.edu>`

```
I noticed that Joe as jleary@vr.state.ut.us said...
> Hi all,
> 
> Anyone have a routine to translate standard text from mainframe (EBCDIC) to
> PC (ASCII)?  I FTP a file to my PC and need to translate to ASCII,
> preferably with Fujitsu COBOL.

When I ftp, the translation from EBCDIC to ASCII is just part of the 
process - binary transfer is a must.  I'll have a look on Monday if you 
really want but it's just a function of mainframe session window on the 
PC.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
