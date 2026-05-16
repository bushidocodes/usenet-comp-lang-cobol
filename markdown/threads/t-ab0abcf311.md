[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Did Microsoft Just Patent The PDS?

_3 messages · 3 participants · 2003-07_

---

### Did Microsoft Just Patent The PDS?

- **From:** theodp@aol.com (theodp)
- **Date:** 2003-07-15T14:23:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7946e7b.0307151323.b01809c@posting.google.com>`

```
From the 'Summary Of The Invention' for U.S. patent no. 6,594,674,
'System and method for creating multiple files from a single source
file', which was issued today to Microsoft:

The invention overcomes the limitations of the prior art by allowing
applications and utilities to write several files to a disk as a
single file-write operation, yet, after conversion, to individually
access the several files.

--> Full Patent Available At

http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=/netahtml/srchnum.htm&r=1&f=G&l=50&s1=6,594,674.WKU.&OS=PN/6,594,674&RS=PN/6,594,674
```

#### ↳ Re: Did Microsoft Just Patent The PDS?

- **From:** Patrick Herring <ph@anweald.co.uk>
- **Date:** 2003-07-16T14:47:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F155778.479CBEEC@anweald.co.uk>`
- **References:** `<e7946e7b.0307151323.b01809c@posting.google.com>`

```
theodp wrote:
> 
> From the 'Summary Of The Invention' for U.S. patent no. 6,594,674,
…[6 more quoted lines elided]…
> access the several files.

zip file?
```

#### ↳ Re: Did Microsoft Just Patent The PDS?

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-17T11:55:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.198090d08cac885698968a@News.CIS.DFN.DE>`
- **References:** `<e7946e7b.0307151323.b01809c@posting.google.com>`

```
In article <e7946e7b.0307151323.b01809c@posting.google.com>, 
theodp@aol.com says...
<snip>
> The invention overcomes the limitations of the prior art by allowing
> applications and utilities to write several files to a disk as a
…[6 more quoted lines elided]…
> 
I guess the following sent to the PTO won't win me any friends 
at Micro$**t:

Dear Sirs:

I wish to challenge patent 6,594,674. I understand there is an 
informal way to do this.

I might bring to your attention that IBM (among others) 
specifically does this with the old PDS (Partitioned Data Set) 
file type (known as _PAM where PAM is Partitioned Access 
Method). IBM has also been doing this via PDS/E (based on the 
VSAM I/O principles used with their "MVS" operating system).

The "MVS" utility, IEBUPDTE has the ability to do what is 
claimed in the patent, as does IEBCOPY and the various versions 
of the Linkage Editor (now called Binder). 

Personally, I worked on such a file system for NASA in 1979 
using a Univac 1100/22 at the Goddard Space Flight Center while 
an employee of CSC. I designed the entire file system based on 
IBM's PDS methodolgy.

Lastly, Microsoft has their own software out there, that they 
market that builds something called DLLs. Those DLLs have within 
them executable code, of which each member is a file unto 
itself.

Regards,
Steve Thompson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
