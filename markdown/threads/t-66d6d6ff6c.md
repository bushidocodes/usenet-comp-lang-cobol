[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# REMARKS paragraph

_5 messages · 3 participants · 2013-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### REMARKS paragraph

- **From:** "charles.leviton" <ua-author-14486870@usenetarchives.gap>
- **Date:** 2013-10-10T14:36:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com>`

```
An earlier post on this forum said
"The INSTALLATION, AUTHOR, etc paragraphs are "OBSOLETE" in the '85 Standard and
removed from the '02 Standard. Therefore, this technique will NOT work in a
"strictly" conforming '02 Standard compiler (of which there aren't any - that I
know of). Using the asterisk in column 7 really IS the best way to make a
comment in "fixed form reference format". (With free form reference format,
start a comment line with "*>" in any old column)"

I understand that Ent Cobol 5.1 (for IBM Mainframes) conforms to the 2002 standard. Does this mean that REMARKS para will cause a compile error. We are a Cobol 4.1 shop and I am able to successfully compile an old program that has a REMARKS paragraph.

Thanks!
```

#### ↳ Re: REMARKS paragraph

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-10T15:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66d6d6ff6c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com>`
- **References:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com>`

```
On Thursday, October 10, 2013 2:36:51 PM UTC-4, cha··.@gm··l.com wrote:
› An earlier post on this forum said
› "The INSTALLATION, AUTHOR, etc paragraphs are "OBSOLETE" in the '85 Standard
…[10 more quoted lines elided]…
› program that has a REMARKS paragraph.

See the Enterprise COBOL for z/OS Migration Guide Version 5 Release 1,
page 55, at
< http://pic.dhe.ibm.com/infocenter/ratdevz/v9r0/topic/com.ibm.ent.cbl.zos.doc/migrate/igy5mg10.pdf >
----
REMARKS paragraph

OS/VS COBOL accepted the REMARKS paragraph.

Enterprise COBOL does not accept the REMARKS paragraph. As a replacement,
use comment lines beginning with an * in column 7 or use the floating
comment indicator *>.
----
›
› Thanks!

You are welcome.
```

##### ↳ ↳ Re: REMARKS paragraph

- **From:** "charles.leviton" <ua-author-14486870@usenetarchives.gap>
- **Date:** 2013-10-10T16:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66d6d6ff6c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-66d6d6ff6c-p2@usenetarchives.gap>`
- **References:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com> <gap-66d6d6ff6c-p2@usenetarchives.gap>`

```
On Thursday, October 10, 2013 3:03:36 PM UTC-4, Rick Smith wrote:
› On Thursday, October 10, 2013 2:36:51 PM UTC-4, cha··.@gm··l.com wrote:
› 
…[58 more quoted lines elided]…
› You are welcome.

Hi,
Thanks, I had seen that same sentence in the info center for Ent Cobol 4.2 as well. But as I have discovered the 4.2 compiler has no problem with the Remarks paragraph.
I mean either way it's no big deal, if Ent Cobol 5.1 behaves differently at compile time then if this program has ever to be recompiled it will fail and we just have to put * in the 7th column for all those lines, that's all.
Regards
```

##### ↳ ↳ Re: REMARKS paragraph

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2013-10-11T04:20:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66d6d6ff6c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-66d6d6ff6c-p2@usenetarchives.gap>`
- **References:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com> <gap-66d6d6ff6c-p2@usenetarchives.gap>`

```
On 10/10/2013 2:03 PM, Rick Smith wrote:
› On Thursday, October 10, 2013 2:36:51 PM UTC-4, cha··.@gm··l.com wrote:
›› An earlier post on this forum said
…[16 more quoted lines elided]…
› ----
 
› Thanks for the link to the Migration guide!
 
 
› REMARKS paragraph
› 
…[10 more quoted lines elided]…
› 

There was a big debate recently in bit.listserv.ibm-main because IBM
Enterprise COBOL 5.1 does not support the older linkage editor and COBOL
programs must be stored in PDSE's (PDS for COBOL executable programs is
not allowed for 5.1). This is potentially a huge problem for a number
of IBM Mainframe shops that have avoided using PDSE libraries.


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: REMARKS paragraph

- **From:** "charles.leviton" <ua-author-14486870@usenetarchives.gap>
- **Date:** 2013-10-11T08:12:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66d6d6ff6c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-66d6d6ff6c-p4@usenetarchives.gap>`
- **References:** `<2352f3e6-03a0-41b6-99c6-101e73e15957@googlegroups.com> <gap-66d6d6ff6c-p2@usenetarchives.gap> <gap-66d6d6ff6c-p4@usenetarchives.gap>`

```
On Friday, October 11, 2013 4:20:23 AM UTC-4, Arnold Trembley wrote:
› On 10/10/2013 2:03 PM, Rick Smith wrote:
› 
…[90 more quoted lines elided]…
› http://www.arnoldtrembley.com/

Yeah, our hand was forced on the PDSE issue by Cool:Gen upgrade.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
