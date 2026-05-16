[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS DOCUMENT CREATE storage?

_14 messages · 8 participants · 2006-03 → 2006-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS DOCUMENT CREATE storage?

- **From:** "Steamroller" <walkertigers@gmail.com>
- **Date:** 2006-03-28T08:55:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com>`

```
Hi.  The question is, where does CICS allocate storage for the EXEC
CICS DOCUMENT commands?  Is it above or below the line?
The environment is Z/OS, CICS TS 2.3, Cobol CICS program with an
HTML/JavaScript front end (uses CWS).

We are seeing 2-3 (or more) times as much storage allocated below the
line for all "web-aware" cobol programs versus other programs using BMS
and we are trying to pinpoint the reason why.

Thanks
```

#### ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** Joseph Katnic <usrr@post.no.mail>
- **Date:** 2006-03-29T19:57:22+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<290320061957221576%usrr@post.no.mail>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com>`

```
In article <1143564941.574464.155400@i40g2000cwc.googlegroups.com>,
Steamroller <walkertigers@gmail.com> wrote:

> Hi.  The question is, where does CICS allocate storage for the EXEC
> CICS DOCUMENT commands?  Is it above or below the line?
…[8 more quoted lines elided]…
> 
Of course, your COBOL programs are linkedited (Bound) with AMODE=31?

Joe.
```

##### ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2006-03-29T09:12:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1p1l22pg3s14007gqt4fk0k58812kqst4j@4ax.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <290320061957221576%usrr@post.no.mail>`

```
On Wed, 29 Mar 2006 19:57:22 +0800, Joseph Katnic <usrr@post.no.mail>
wrote:

>In article <1143564941.574464.155400@i40g2000cwc.googlegroups.com>,
>Steamroller <walkertigers@gmail.com> wrote:
…[12 more quoted lines elided]…
>Of course, your COBOL programs are linkedited (Bound) with AMODE=31?
I would guess that they are based on the phrasing of the request.  A
more subtle thing might be that DATA24 is specified as a compile
option or that the EXEC DOCUMENT COMMAND generates this code.  It
looks like a trip into arcanity.
>
>Joe.
```

#### ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** Joe Zitzelberger <zberger@knology.net>
- **Date:** 2006-03-29T08:44:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zberger-85FF77.08441929032006@ispnews.usenetserver.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com>`

```
In article <1143564941.574464.155400@i40g2000cwc.googlegroups.com>,
 "Steamroller" <walkertigers@gmail.com> wrote:

> Hi.  The question is, where does CICS allocate storage for the EXEC
> CICS DOCUMENT commands?  Is it above or below the line?
…[7 more quoted lines elided]…
> Thanks

Check your transaction options.  I suspect you have them set to BELow 
instead of ANY.
```

##### ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "Steamroller" <walkertigers@gmail.com>
- **Date:** 2006-03-29T06:27:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143642443.598156.64320@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<zberger-85FF77.08441929032006@ispnews.usenetserver.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com>`

```
I have checked all of these things from the application and
compile/link edit side and it appears that everything is 31 (amode(31),
data(31), etc) nothing below the line, or set to 24.  I'll double check
with the systems guys to make sure the transaction options are set to
ANY but I'm positive they have been.
I didn't see any options on the document create to specify 24 or any or
anything like that.  I agree this is one of those things that will
drive you nuts.

Thanks for the help so far, anyone else have any ideas?
```

###### ↳ ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-29T21:34:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3DWf.247117$Mh4.212464@fe02.news.easynews.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com> <1143642443.598156.64320@g10g2000cwb.googlegroups.com>`

```
I do NOT know if this is the answer or not, but if you look at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfht3b02/APPENDIX1.6.5.1


It distinguishes between CDSAand ECDSA.   When you look at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfht3b02/APPENDIX1.6.5.1.1

It mentions (for CDSA - which would be "below the line")

    "DHPDPOOL  -  contains DCBs for partitioned data sets used by document 
handler domain"

P.S. I have asked some of my "IBM sources" to see if they have any better 
answers to the original question.  So far, they are still "researching" the 
question.
```

##### ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-03-30T06:41:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<zberger-85FF77.08441929032006@ispnews.usenetserver.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com>`

```


Joe Zitzelberger wrote:
> In article <1143564941.574464.155400@i40g2000cwc.googlegroups.com>,
>  "Steamroller" <walkertigers@gmail.com> wrote:
…[15 more quoted lines elided]…
> instead of ANY.

Not all CICS applications programmers have access to CEDA to maintain 
CSD table entries.  I believe the parameter in the TRANSACTION ID 
entry (formerly know as the PCT entry) is named DATALOCATION.  Since 
the PCT/Transaction entry only identifies the first program to be 
executed in the CICS transaction, and that program could EXEC CICS 
LINK or XCTL to another program, it's quite possible that another 
program could be executed that is not AMODE31.  Therefore there might 
be a need to force a transaction to use only AMODE24 data areas.

It might take a system programmer to change the DATALOCATION parameter 
for the transction.

If you know the transaction ID, you can try to inquire on this by 
typing the following command on a blank screen in CICS:

CEDC EXPAND GROUP(*) TRANS(XXXX)

The CEDC transaction only allows you to view CSD table entries.  The 
CEDB transaction allows you to view or modify CSD entries.  The CEDA 
transaction allows you to view, modify, or install CSD entries.

And for the old-timers who have been away from CICS for a while, the 
CSD file replaces virtually all of the configuration tables that had 
to be assembled to configure CICS -- PCT (transactions), PPT 
(programs), FCT (files), TCT (Terminals), et cetera.  CSD entries are 
stored in GROUPS, and each CICS region has a LIST of GROUPS that 
comprise its configuration.

I hope that helps.
```

###### ↳ ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-30T21:18:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<491m3aFmc3o4U1@individual.net>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com> <t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net...
>
<snipped>>
> And for the old-timers who have been away from CICS for a while, the CSD 
> file replaces virtually all of the configuration tables that had to be 
…[3 more quoted lines elided]…
>

Thanks Arnold. This old timer found that interesting and helpful :-) So what 
does CSD stand for :-)?

Pete.
```

###### ↳ ↳ ↳ Re: CICS DOCUMENT CREATE storage?

_(reply depth: 4)_

- **From:** Joe Zitzelberger <zberger@knology.net>
- **Date:** 2006-03-30T08:28:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zberger-7529A2.08282430032006@ispnews.usenetserver.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com> <t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net> <491m3aFmc3o4U1@individual.net>`

```
In article <491m3aFmc3o4U1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> "Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
> news:t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net...
…[12 more quoted lines elided]…
> Pete.

Common System Defs -- or something like that...
```

###### ↳ ↳ ↳ Re: CICS DOCUMENT CREATE storage?

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-04-01T08:12:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MBqXf.48759$bn3.14974@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<491m3aFmc3o4U1@individual.net>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com> <t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net> <491m3aFmc3o4U1@individual.net>`

```


Pete Dashwood wrote:
> "Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
> news:t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net...
…[14 more quoted lines elided]…
> Pete.

Found by googling for "cics csd file", on an ibm web site:

*** begin quote ***

CSD file management
The CICSï¿½ system definition (CSD) file is a VSAM data set containing a
resource definition record for every resource defined to CICS by means 
of CEDA or DFHCSDUP. It can be defined as recoverable, so that changes 
made  by CEDA or CEDB that were incomplete when an abend occurred, are 
backed out.

*** end quote ***

DFHCSDUP is a batch program that can process CEDA commands.  It is 
often used to generate reports from the CSD file.  But it can also be 
used in a production batch job to apply CSD updates.  That can be 
useful for audit purposes.
```

###### ↳ ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "Steamroller" <walkertigers@gmail.com>
- **Date:** 2006-03-30T06:54:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143730460.462386.111240@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <zberger-85FF77.08441929032006@ispnews.usenetserver.com> <t4LWf.42385$bn3.21269@bgtnsc04-news.ops.worldnet.att.net>`

```
that would be a helpful transaction, unfortunately, I'm not authorized
for CEDC.  such is the life of a contractor.
```

#### ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2006-03-29T16:11:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20060329.16113068@rechner12.lerch.xl>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com>`

```


?? Ursprüngliche Nachricht

Am 28.03.06, 16:55:41, schrieb "Steamroller" <walkertigers@gmail.com> 
zum Thema CICS DOCUMENT CREATE storage?:


> Hi.  The question is, where does CICS allocate storage for the EXEC
> CICS DOCUMENT commands?  Is it above or below the line?
> The environment is Z/OS, CICS TS 2.3, Cobol CICS program with an
> HTML/JavaScript front end (uses CWS).

> We are seeing 2-3 (or more) times as much storage allocated below the
> line for all "web-aware" cobol programs versus other programs using 
BMS
> and we are trying to pinpoint the reason why.

Do you run in SOS below 16MB then you can:

Have you take a look on your config-file CEE%OPT with heap below
	You can reduce the below-heap to 4080 (one page minus beginning and 
endig SAA)
Have you linked all BMS-maps AMODE=31,RMODE=ANY
	You can ignore the IEWL message, i do it since CICS TS 2.1
Do you have any programms AMODE=24 who invoked with EXEC CICS LINK
	The COMMAREA is copied from high storage to low Storage and back

that are some reasons, but there can be more worth activity.

Einen schoenen Tag
Andreas Lerch
```

#### ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-04-07T05:37:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wUmZf.30306$Y53.21624@fe07.news.easynews.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com>`

```
From my "usually reliable sources" (at IBM),

"Hi Bill,

The developer for this area has passed on some information that might be useful 
for you. A customer raised a service request recently about this. As a result of 
this there was an APAR PK17576 CICS GOES SOS IN ECDSA WHEN CREATING LARGE WEB 
DOCUMENTS.

The APAR explains what's happening - multiple copies of the document are being 
held:

[For sending a CICS document using CICS Web support] there will ... be 5 large 
storage users.
2 copies in document handler using DHDDB storage, 1 copy in TS using TSMAIN, 1 
copy in a temporary buffer in WBGENRAL, and 1 buffer to hold the completed HTTP 
response.
.
The HTTP response is in user key storage because the server program runs in user 
key. This will be the storage increase seen in EUDSA. The other 4 areas will all 
be in ECDSA.

The APAR reduces the copies of the document that are held. Unfortunately I see 
the only doc update requested was for the Data Areas manuals! I've made a note 
to improve the documentation about this.

Hope that helps,"
```

##### ↳ ↳ Re: CICS DOCUMENT CREATE storage?

- **From:** "Steamroller" <walkertigers@gmail.com>
- **Date:** 2006-04-07T10:25:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144430710.544595.253360@z34g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<wUmZf.30306$Y53.21624@fe07.news.easynews.com>`
- **References:** `<1143564941.574464.155400@i40g2000cwc.googlegroups.com> <wUmZf.30306$Y53.21624@fe07.news.easynews.com>`

```
very nice... thanks for the info!!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
