[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reporting defects in the ANSI/ISO COBOL Standards

_3 messages · 2 participants · 2003-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Migration and conversion`](../topics.md#migration)

---

### Reporting defects in the ANSI/ISO COBOL Standards

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-19T13:31:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5agiq$4f7$1@slb1.atl.mindspring.net>`

```
As a follow-up on another thread, I thought that I would give some GUIDANCE
on submitting "defect reports" on ANSI/ISO COBOL Standards. Just as this is
an unmoderated newsgroup, readers of this note may do as they please with
its recommendations/information.

1) Although I have seen nothing to indicate that the '85 Standard (with its
approved 2 amendments) has been withdrawn as either an ANSI or an ISO COBOL
Standard, I *strongly* recommend against submitting defect reports against
it - unless the same defect exists in the 2002 Standard.  It is *highly*
unlikely that either J4 (ANSI-ish group) or WG4 (ISO-ish group) will do much
more than reply that this (older) Standard is no longer being "updated".

2) For those outside the US, it is possible for you to submit your defect
reports to *EITHER* your national Standards body or to ANSI/J4.  There are
PROs and CONs of each approach. I won't go into them here, but if you have
questions about them, please email me privately.  (Check the archives of CLC
on how to find out how to contact your "national standards body".)  It is
true that J4 will do the actual "grunt work" on any defect report no matter
WHERE it comes from, but it is also true that WG4 will review (and
approve/modify) it before it becomes final - even if it comes from within
the US.

3) The "easiest" (IMHO) way to submit a defect report to J4 is to send it
(by email) to the J4 chair at:
   Don.Schricker <at> microfocus.com
It is valid, however, to send it directly to ANSI indicating for which
Standard you are submitting the defect report.  See:
  http://www.ansi.org/
for contact information for them.

4) "Defect reports" are *not* intended as a way to submit
   "Wouldn't it have been better if ..."
        or
   "Why didn't you use this approach ..."
        or
   "Please expand the Standard to include ..."
        or
   "Vendor XYZ does it this way, why didn't you make the standard say ..."
comments.

 Defect reports are for reporting DEFECTS in what the Standard actually
says. This may include "omissions" where there is something "critical" left
out of the specification that makes it ambiguous or unclear what the
Standard requires. It also, DEFINITELY includes cases where two or more
separate parts of the Standard conflict with each other.  For examples of
what defects have already been reported and BEGUN their processing for the
2002 Standard, see:
   http://www.cobolstandard.info/defect.htm

You will notice that NONE of these documents is marked "DF" meaning that
they have reached final approval status.  However, these documents do show
the type of "problem" reported and how J4 drafts *tentative* responses.

If you are interested in *final* defect and interpretation (an "entirely
different kettle of fish") documents for the 85/89/91 ANSI Standard, you can
go to (long URL - combine to get to correct page):

http://global.ihs.com/doc_detail.cfm?currency_code=USD&customer_id=212547254
C0A&shopping_cart_id=2725385B2E4B202041594020240A&country_code=US&lang_code=
ENGL&item_s_key=00267482&item_key_date=020417&input_doc_number=&input_doc_ti
tle=cobol

and order (for $28 (USD)) a copy of CIB-28.  Members of J4 or WG4 *might* be
able to provide you with a "soft" copy of the document depending upon their
interpretation of the "Acknowledgement" versus "Copyright" requirements.

5)  The important information to include in a Defect Report are:
 -   Your name and contact information (company/organization affiliation is
OPTIONAL)
 -  Which version of the Standard you are reporting a problem with
 - Specific pages/sections (title and number) within the Standard where the
problems "appear"
 -  *EXACTLY* what the defect is that you are reporting

        and OPTIONALLY

   what solution (fix) you would suggest

6) I cannot give you ANY estimate on when you should expect a tentative or
final response to your report.  I will say, however, that it is HIGHLY
likely that J4 will at least begin processing your report within the next 2
meetings after they receive it (no guarantee, just likely).  If you wish to
"follow" their processes, you should contact the J4 chair for information on
seeing working documents related to your report (or on when/where meetings
are if you wish to attend).

        ***

Hopefully, any others who have participated in or are currently
participating in the standardization process will correct me, if I have
misspoken above - or add to this if I missed something.
```

#### ↳ Re: Reporting defects in the ANSI/ISO COBOL Standards

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-19T13:52:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5ahqq$sju$1@slb6.atl.mindspring.net>`
- **References:** `<b5agiq$4f7$1@slb1.atl.mindspring.net>`

```
(Speaking to myself <G>)

In addition to what I say below, you do NOT need to use "defect reports" to
let J4/WG4 know about strictly editorial issues (misspelling, punctuation,
font problems, etc).  Send them to the J4 chair directly.  If he disagrees
with your evaluation - or thinks it is NOT editorial, he may suggest that
you DO submit it as a "defect report" - but there is no need to start that
way.
```

#### ↳ Re: Reporting defects in the ANSI/ISO COBOL Standards

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-20T21:14:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303202114.4d71ce6f@posting.google.com>`
- **References:** `<b5agiq$4f7$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<b5agiq$4f7$1@slb1.atl.mindspring.net>...
> 
> Hopefully, any others who have participated in or are currently
> participating in the standardization process will correct me, if I have
> misspoken above - or add to this if I missed something.

The only thing I will add is that some Reports are at DF Status
currently --- and I will be (As the maintainer of the site) be adding
more in the next week or two.

http://www.cobolstandard.info/defect.htm

I will also be posting a suggested defect reporting form.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
