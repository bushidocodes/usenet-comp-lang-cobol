[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and message IWZ200S with file status 96

_7 messages · 6 participants · 2006-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### COBOL and message IWZ200S with file status 96

- **From:** "rolf_cologne" <rolf-peter_kollbach@msg-systems.com>
- **Date:** 2006-08-22T05:27:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`

```
Hi!

I'm receiving a message IWZ200Z with file status 96 - and I cannot find a
description of this file status.

Can anybody help me? 

Thanks 
Rolf
```

#### ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** docdwarf@panix.com ()
- **Date:** 2006-08-22T09:42:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ecejho$oj1$1@reader2.panix.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`

```
In article <0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>,
rolf_cologne <rolf-peter_kollbach@msg-systems.com> wrote:
>Hi!
>
>I'm receiving a message IWZ200Z with file status 96 - and I cannot find a
>description of this file status.

Platform/compiler?

DD
```

##### ↳ ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** "rolf_cologne" <rolf.kollbach@gmx.de>
- **Date:** 2006-08-22T07:49:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42d70950a331579180cdea8da1c06eff@localhost.talkaboutprogramming.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com> <ecejho$oj1$1@reader2.panix.com>`

```
The platform is AIX with the IBM COBOL compiler.

Regards,
Rolf
```

###### ↳ ↳ ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** docdwarf@panix.com ()
- **Date:** 2006-08-22T12:13:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ecesd0$1b6$1@reader2.panix.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com> <ecejho$oj1$1@reader2.panix.com> <42d70950a331579180cdea8da1c06eff@localhost.talkaboutprogramming.com>`

```
In article <42d70950a331579180cdea8da1c06eff@localhost.talkaboutprogramming.com>,
rolf_cologne <rolf.kollbach@gmx.de> wrote:
>The platform is AIX with the IBM COBOL compiler.

Well, I can't offer much help there; I use an IBM COBOL compiler but it is 
on a mainframe.  According to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/IGY3LR10/CCONTENTS?DT=20020920180651> 
a file status of '96' is:

-begin quoted text:

For VSAM file: An OPEN statement with the OUTPUT phrase was attempted, or 
an OPEN statement with the I-O or EXTEND phrase was attempted for an 
optional file, but no DD statement was specified for the file.

For QSAM file: An OPEN statement with the OUTPUT phrase was attempted, or 
an OPEN statement with the I-O or EXTEND phrase was attempted for an 
optional file, but no DD statement was specified for the file and the 
CBLQDA(OFF) run-time option was specified.

--end quoted text

... but I don't know how much help that is going to be.  Has someone been 
moving around your files so that they no longer match up with what is in 
their SELECTs?

DD
```

#### ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** ozzy.kopec@gmail.com
- **Date:** 2006-08-22T05:53:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1156251216.649492.55700@h48g2000cwc.googlegroups.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`

```
rolf_cologne wrote:
> Hi!
>
…[4 more quoted lines elided]…
>
Sorry no idea, here's an old (short) thread that may apply to your
problem: http://tinyurl.com/lz3re
```

#### ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-08-22T14:42:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CJEGg.621760$C62.590559@fe12.news.easynews.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`

```
If you go to:

 http://publib.boulder.ibm.com/infocenter/comphelp/v7v91/topic/com.ibm.aix.cbl.doc/rlpdscpf.htm#statkeyyou will see that with IBM COBOL for AIX, FS=96 means "File system not available"--Bill Klein wmklein <at> ix.netcom.com"rolf_cologne" <rolf-peter_kollbach@msg-systems.com> wrote in messagenews:0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com...> Hi!>> I'm receiving a message IWZ200Z with file status 96 - and I cannot find a> description of this file status.>> Can anybody help me?>> Thanks> Rolf>
```

#### ↳ Re: COBOL and message IWZ200S with file status 96

- **From:** "Pizzo" <pl.piz@alice.it>
- **Date:** 2006-08-27T19:49:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1156733381.038696.275910@74g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`
- **References:** `<0c4c460b9fec524ca066d44971dcf48e@localhost.talkaboutprogramming.com>`

```

rolf_cologne wrote:
> Hi!
>
> I'm receiving a message IWZ200Z with file status 96 - and I cannot find a
> description of this file status.
> ----------- cut -----------------


Try to see here --> http://www.simotime.com/vsmfsk01.htm


Bye all !!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
