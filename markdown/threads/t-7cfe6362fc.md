[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need to access data in AcuCobol Isam Files

_5 messages · 5 participants · 2000-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Need to access data in AcuCobol Isam Files

- **From:** Adam Williams <adam@lnx01688.morrison.iserv.net>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%hkE5.56435$sB2.1123113@news-east.usenetserver.com>`

```
I have a large application written in PHP running on a
RedHat Linux/Apache web server.  Up till this point I
have used an Informix database (either through PHP's
native Informix support or UnixODBC).  

Now I need to access data residing in AcuCOBOL ISAM
(or are they called Vision files?) running on an
IBM RS/6000 AIX 4.2.1.  AcuCOBOL does support data
access from Win32 ODBC drivers, but I need to acces
this data from my web server.  The version of
AcuCOBOL is:

ACUCOBOL-GT version 4.0.0
Vision version 4 file system

I've inquired at both Informix (Data Blades) and
AcuCOBOL and neither has been able to offer any
solutions. 

And pointers would be greatly appreciated
```

#### ↳ Re: Need to access data in AcuCobol Isam Files

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e1e2ea.744294856@207.126.101.100>`
- **References:** `<%hkE5.56435$sB2.1123113@news-east.usenetserver.com>`

```
Write a COBOL CGI program to service the data to the web server?

On Mon, 09 Oct 2000 14:06:51 GMT, Adam Williams
<adam@lnx01688.morrison.iserv.net> wrote:

>I have a large application written in PHP running on a
>RedHat Linux/Apache web server.  Up till this point I
…[17 more quoted lines elided]…
>And pointers would be greatly appreciated

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Need to access data in AcuCobol Isam Files

- **From:** Vadim Maslov <vadim-cbl@siber.com>
- **Date:** 2000-10-14T05:27:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E7EF48.B641E978@siber.com>`
- **References:** `<%hkE5.56435$sB2.1123113@news-east.usenetserver.com>`

```
Looks like we have an answer.

Siber Systems has a C++ library that can read 
AcuCobol data files and turn the records 
into sets of fields that C++ can understand.

We can license the library to you in source or binary format.

For more details see http://www.siber.com/sct/datafile/

Regards,
Vadim Maslov


Adam Williams wrote:
> 
> I have a large application written in PHP running on a
…[18 more quoted lines elided]…
> And pointers would be greatly appreciated
```

##### ↳ ↳ Re: Need to access data in AcuCobol Isam Files

- **From:** "Ray Smith" <smithr@ix.net.au>
- **Date:** 2000-10-15T09:07:46+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OP4G5.349$bq1.801@news.syd.ip.net.au>`
- **References:** `<%hkE5.56435$sB2.1123113@news-east.usenetserver.com> <39E7EF48.B641E978@siber.com>`

```
> Adam Williams wrote:
> >
…[19 more quoted lines elided]…
> > And pointers would be greatly appreciated

I find it a little surprising AcuCorp couldn't help you.
Acu's Vision files are created and accessed by a C routine
which is linked into their cobol runtime.
We use a call to "I$IO" (which is the C routine) to access Vision
files without use of the standard Cobol commands.

What Acu must be saying then is that they won't allow their C
routine to be linked into / or used by any other program.

It is probably worth asking Acu again but specifically ask if you
can use their I$IO routines from a different language (PHP).

Sometimes the person you ask the question to doesn't
have all the answers!

"I" thought it would have just been a licensing issue.

Regards,

Ray Smith
```

###### ↳ ↳ ↳ Re: Need to access data in AcuCobol Isam Files

- **From:** "Cheesle" <cheesle@NoSpamPlease.online.no>
- **Date:** 2000-10-18T03:22:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DH8H5.2909$_o5.13792@typhoon.san.rr.com>`
- **References:** `<%hkE5.56435$sB2.1123113@news-east.usenetserver.com> <39E7EF48.B641E978@siber.com> <OP4G5.349$bq1.801@news.syd.ip.net.au>`

```
"Ray Smith" <smithr@ix.net.au> wrote in message
news:OP4G5.349$bq1.801@news.syd.ip.net.au...
> It is probably worth asking Acu again but specifically ask if you
> can use their I$IO routines from a different language (PHP).

You are correct about this assumption. Provided that PHP is a language
capable of using a C library, and that this person has an agreement with
Acucorp this should be a doable task.

Gisle Forseth

I work for Acucorp, however, my opinions expressed in contributions to this
news group is my own and does in no way express opinions on behalf of the
company.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
