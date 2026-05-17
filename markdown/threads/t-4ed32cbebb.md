[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II Conversion Help?

_6 messages · 6 participants · 1998-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL II Conversion Help?

- **From:** "dennis m. matsudaira" <ua-author-14704862@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`

```

Does anyone have or know where to download a checklist to assist in the
manual conversion of OS/VS COBOL (maybe some ANSI '74, too) to COBOL II?
One of our clients is in a bind to get 1 million lines of code converted
and turned to us for help. Problem is that we've never done a code
dialect conversion before and aren't sure what to look for. We have the
IBM documentation on that outlines the differences, but more and better
information would be VERY helpful.

Thanks for any help!!!
Dennis
```

#### ↳ Re: COBOL II Conversion Help?

- **From:** "mickey ben-tovim" <ua-author-17074116@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed32cbebb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`
- **References:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`

```

Dennis M. Matsudaira wrote:
› 
› Does anyone have or know where to download a checklist to assist in the
…[8 more quoted lines elided]…
› Dennis

IBM has a tool to do just this. It will even remove the OS Report Writer
and convert it into native Cobol/2. It works very well. I know. I wrote
it in Germany in 1987.

mickey
```

##### ↳ ↳ Re: COBOL II Conversion Help?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed32cbebb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4ed32cbebb-p2@usenetarchives.gap>`
- **References:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net> <gap-4ed32cbebb-p2@usenetarchives.gap>`

```

Just to comment on Report Writer.

The CCCA also has an option to KEEP report writer in. As IBM does support
Report Writer (via an add-on product) with all the newer COBOLs and as
Report Writer will be a required (and enhanced) part of the next COBOL
Standard, I would certainly recommend going with the "keep" option -
assuming your shop already knows and uses Report Writer.
```

#### ↳ Re: COBOL II Conversion Help?

- **From:** "the man in spectacles" <ua-author-8441646@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed32cbebb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`
- **References:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`

```

Dennis, there is an appendix in Stern and Stern that lists the features of
COBOL 85, otherwise known as COBOL II. However COBOL II is not the latest
version of COBOL, so I would make sure your client is aware of this. There
is also a question over how much longer IBM will support COBOL II and this
leads into the Year 2000 compliance issue.
I would also make sure of their exact requirements, since many COBOL I
programs can be recompiled without problem with the COBOL II compiler.
(e.g. do you really need to change all those IF THEN ELSE IF statements to
EVALUATE?).
Two things to watch out for, that will compile but may cause a logic change
between COBOL I and II.
PERFORM VARYING X FROM Y BY 1 ... AFTER ...
IF A = B AND NOT LESS THAN C OR D

A compiler and run time migration guide for COBOL for MVS, which could be
what you really want can be found at

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYMG200/CCONT
ENTS
                                         Regards
                              The Man in Spectacles

Please remove -nematode- from the email address before replying

Solicitations to me must be pre-approved in writing by me after solicitor 
pays $1000 US per incident.  Solicitations sent to me are proof that you 
accept this notice and will send a certified check forthwith.
```

#### ↳ Re: COBOL II Conversion Help?

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed32cbebb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`
- **References:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`

```

Siber Systems has an automated converter for IBM OS/VS COBOL. For more
information see: www.siber.com

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com



Dennis M. Matsudaira wrote in message
<6hgt7v$d.··.@bgt··t.net>...
› Does anyone have or know where to download a checklist to assist in the
› manual conversion of OS/VS COBOL (maybe some ANSI '74, too) to COBOL II?
…[8 more quoted lines elided]…
›
```

#### ↳ Re: COBOL II Conversion Help?

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed32cbebb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`
- **References:** `<6hgt7v$dk3@bgtnsc02.worldnet.att.net>`

```

Get MHTRAN. It does a fairly good job of code conversion. I'm using
it at the moment.

On Mon, 20 Apr 1998 18:38:22 -0700, "Dennis M. Matsudaira"
wrote:

› Does anyone have or know where to download a checklist to assist in the
› manual conversion of OS/VS COBOL (maybe some ANSI '74, too) to COBOL II?
…[7 more quoted lines elided]…
› Dennis
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
