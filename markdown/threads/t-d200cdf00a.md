[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# XML and the New COBOL

_7 messages · 3 participants · 2005-09_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### XML and the New COBOL

- **From:** "knorth" <ken_north@compuserve.com>
- **Date:** 2005-09-12T22:31:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com>`

```
The SQL 2003 standard added functions for working with XML data.
The next COBOL standard is also adding XML support.

Barry Tauber explains in this article.

"XML and the New COBOL"
http://www.webservicessummit.com/Trends/COBOL_XML.htm
```

#### ↳ Re: XML and the New COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-13T18:24:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UPEVe.48052$yd.20724@fe11.news.easynews.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com>`

```
Just to clarify (and I am CC'ing Barry on this), when the article writes,

"The XML changes to the COBOL standard will be released as a Technical Report 
(TR). The TR will be published by the end of 2005 or middle 2006 and it will be 
based on features in the 2002 standard. When it is rolled into the 2008 
standard, the TR will go away. Anyone with an interest in XML and COBOL can view 
and comment (to me or the committee) on the current (23 Aug 2005) working draft 
."

There are a few of (semi?)reasonable assumptions in this paragraph.  (Barry may 
or may not have worded it this way, but there are certainly problems with how it 
shows up).

1) When/If the TR is published, it will be an ISO TR (Technical Report) and NOT 
an ANSI (or INCITS) TR. Therefore, it is WG4 (and not INCITS J4 TC) that is 
responsible for the "development" of the report.  (Although J4 *is* doing the 
technical drafting of it).

2) There was a version of the draft ISO TR that went to "ballot" and which 
received some "technical" and substantive comments.  Therefore, there is 
(currently) no guarantee that this TR will EVER be approved as an ISO TR.  As I 
am watching the work on it, I think I (and others) will have a much better idea 
AFTER the WG4 meeting in October 2005 as to whether or not this will be an 
approved TR in 2005, 2006, or EVER.

3) There is currently *NO* ISO WG4 (working-group 4) "direction" to include this 
TR (if approved) within the 2008 (or 2009) next revision of the ISO COBOL 
Standard. However, I believe that the US (and possibly some other countries) are 
requesting/suggesting this.

  ***

Having said the above, my best GUESS is that this will become an approved ISO TR 
*late* in 2006 and that *IF* there is minimal objection to it at the 
international level, that it will be incorporated into the next ISO COBOL 
revision.

HOWEVER, it is worth mentioning
 A) the approach in the draft TR is QUITE different from (at least one) current 
COBOL implementation (that available in IBM's COBOL compilers)
 B) At least one country (Germany) is "on record" as questioning whether this 
belongs in the COBOL Standard at all
 C) There are currently (as far as I know) *ZERO* "full implementations" of the 
ISO 2002 COBOL Standard, so what difference it will (or will not) make if this 
gets into a 2008 or 2009 Standard is certainly an "open question".
```

##### ↳ ↳ Re: XML and the New COBOL

- **From:** "knorth" <ken_north@compuserve.com>
- **Date:** 2005-09-13T14:23:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126646594.927399.260970@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<UPEVe.48052$yd.20724@fe11.news.easynews.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com> <UPEVe.48052$yd.20724@fe11.news.easynews.com>`

```
William M. Klein wrote:
>>When/If the TR is published, it will be an ISO TR (Technical Report) and NOT
an ANSI (or INCITS) TR.

That runs counter to the ISO fast track process.

If a standard passes through INCITS to ANSI, ANSI can submit it as a
fast track candidate to ISO. ANSI did it with Forth and SQLJ. ECMA did
it with C# and CLI.


Are you aware of some change to the fast track process?
```

###### ↳ ↳ ↳ Re: XML and the New COBOL

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-13T14:27:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg7g5b$15cm$1@si05.rsvl.unisys.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com> <UPEVe.48052$yd.20724@fe11.news.easynews.com> <1126646594.927399.260970@f14g2000cwb.googlegroups.com>`

```
In this case the TR is starting out as an *ISO/IEC* TR, not an ANSI TR.  If
approved as such it will be adopted by ANSI by virtue of its approval by
ISO/IEC.  That standards adopted by international consensus are, unless
specific action is taken otherwise, adopted as US standards as well (as I
recall the matter) is indeed a change to the process since the '85 standard
and its amendments.  The XML TR isn't the "fast track" adoption of an ANSI
standard, as I understand matters.    INCITS/J4 is the "subcontractor"
preparing an *ISO/IEC* document.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: XML and the New COBOL

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-13T21:33:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mAHVe.5016$1z2.2845@fe10.news.easynews.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com> <UPEVe.48052$yd.20724@fe11.news.easynews.com> <1126646594.927399.260970@f14g2000cwb.googlegroups.com> <dg7g5b$15cm$1@si05.rsvl.unisys.com>`

```
Chuck,
   Are you certain of this?  I *know* you are correct for STANDARDS, but I 
thought there were different rules for TRs (which are EXPLICITLY *not* 
Standards - for either ISO or ANSI).

P.S.  For those who don't know, Chuck either is or soon will be the new 
"convenor" for WG4, so I do consider him the "authority" on this, so if he says 
it will be an ANSI TR, I certainly "stand corrected".
```

###### ↳ ↳ ↳ Re: XML and the New COBOL

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-13T15:25:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg7jhh$17dm$1@si05.rsvl.unisys.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com> <UPEVe.48052$yd.20724@fe11.news.easynews.com> <1126646594.927399.260970@f14g2000cwb.googlegroups.com> <dg7g5b$15cm$1@si05.rsvl.unisys.com> <mAHVe.5016$1z2.2845@fe10.news.easynews.com>`

```
The distinction between an adopted ISO/IEC TR and an adopted ISO/IEC
standard may well be important here, Bill, as you point out.

However, I took the intent of the National Technology Transfer and
Advancement Act of 1995 to be inclusive of both approved TR's and approved
standards, on the basis that the TR was arrived at as a matter of
international consensus, which seems to be the key point in that act.

    -Chuck Stevens

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:mAHVe.5016$1z2.2845@fe10.news.easynews.com...
> Chuck,
>    Are you certain of this?  I *know* you are correct for STANDARDS, but I
…[4 more quoted lines elided]…
> "convenor" for WG4, so I do consider him the "authority" on this, so if he
says
> it will be an ANSI TR, I certainly "stand corrected".
>
…[5 more quoted lines elided]…
> > In this case the TR is starting out as an *ISO/IEC* TR, not an ANSI TR.
If
> > approved as such it will be adopted by ANSI by virtue of its approval by
> > ISO/IEC.  That standards adopted by international consensus are, unless
> > specific action is taken otherwise, adopted as US standards as well (as
I
> > recall the matter) is indeed a change to the process since the '85
standard
> > and its amendments.  The XML TR isn't the "fast track" adoption of an
ANSI
> > standard, as I understand matters.    INCITS/J4 is the "subcontractor"
> > preparing an *ISO/IEC* document.
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: XML and the New COBOL

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-13T23:32:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kJVe.43332$e95.31805@fe08.news.easynews.com>`
- **References:** `<1126589518.796207.177850@z14g2000cwz.googlegroups.com> <UPEVe.48052$yd.20724@fe11.news.easynews.com> <1126646594.927399.260970@f14g2000cwb.googlegroups.com> <dg7g5b$15cm$1@si05.rsvl.unisys.com> <mAHVe.5016$1z2.2845@fe10.news.easynews.com> <dg7jhh$17dm$1@si05.rsvl.unisys.com>`

```
For those who don't know how "pedantic" I am (that is they aren't regular 
participants in comp.lang.cobol <G>), I have just done a little research (given 
Chuck's pointer).

I am now even less certain that I was before <G> . According to:
  http://www.nal.usda.gov/ttic/faq/pl104113.htm

"(1) IN GENERAL- Except as provided in paragraph (3) of this subsection, all 
Federal agencies and departments shall use technical standards that are 
developed or adopted by voluntary consensus standards bodies, using such 
technical standards as a means to carry out policy objectives or activities 
determined by the agencies and departments.

 <snip>

(3) EXCEPTION- If compliance with paragraph (1) of this subsection is 
inconsistent with applicable law or otherwise impractical, a Federal agency or 
department may elect to use technical standards that are not developed or 
adopted by voluntary consensus standards bodies if the head of each such agency 
or department transmits to the Office of Management and Budget an explanation of 
the reasons for using such standards. Each year, beginning with fiscal year 
1997, the Office of Management and Budget shall transmit to Congress and its 
committees a report summarizing all explanations received in the preceding year 
under this paragraph.

(4) DEFINITION OF TECHNICAL STANDARDS- As used in this subsection, the term 
`technical standards' means performance-based or design-specific technical 
specifications and related management systems practices."

   ***

However, according to:
   http://www.cobolportal.com/j4/files/05-0212.doc

"Technical Reports are drafted in accordance with the rules given in the ISO/IEC 
Directives, Part 2."

and

"This Technical Report specifies the syntax and semantics for XML support in 
COBOL.  The purpose of this Technical Report is to promote a high degree of 
portability in implementations, even though some elements are subject to trial 
before completion of a final design suitable for standardization."

  ***

While according to:
  http://isotc.iso.org/livelink/livelink.exe/4230518/ISO_IEC_Directives__Part_2__Rules_for_the_structure_and_drafting_of_International_Standards__2004__5th_edition__Word_format_.doc?func=doc.Fetch&nodeid=4230518

"NOTE 4     Prior to mid-1999, Technical Specifications were designated as 
Technical Reports of type 1 or 2.

3.5
Technical Report
TR
document published by ISO or IEC containing collected data of a different kind 
from that normally published as an International Standard or Technical 
Specification

NOTE 1     Such data may include, for example, data obtained from a survey 
carried out among the national bodies, data on work in other international 
organizations or data on the "state of the art" in relation to standards of 
national bodies on a particular subject."

  ***

and according to (from the draft of the only ISO TR so-far approved for COBOL)
  http://www.cobolportal.com/j4/files/03-0046.doc

"This draft Technical Report specifies a feature for finalizing objects in 
COBOL.  The feature is considered to be immature and not ready for 
standardization.  The decision was made to publish the specification in a Type 2 
Technical Report so that implementations can be undertaken on an experimental 
basis.  The experience gained is expected to result in an improved specification 
that can progress to standardization."

    ***

Bottom-Line,
  When/If the there is an approved ISO/IEC Technical Report for COBOL native 
support of XML, the impact of this "approval" for the US is whatever it is (and 
probably of ZERO interest to anyone but me <G>)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
