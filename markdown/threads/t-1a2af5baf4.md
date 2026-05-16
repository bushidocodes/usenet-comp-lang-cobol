[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dates in the Data Division (one compiler's extension)

_2 messages · 2 participants · 2004-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Dates in the Data Division (one compiler's extension)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-06T01:55:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ByBQc.10236$cK.4758@newsread2.news.pas.earthlink.net>`

```
As a follow-on to another thread, for those who might (or might NOT) like
extending the data division to support "date fields" and formats, you might want
to look at IBM's "DATE FORMAT" clause (from their "Millennium Language
Extensions").

See (for example),
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR20/5.3.6

and
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/7.2.2.3.1

   ***

Having pointed this out, it my impression (totally from UNSUBSTANTIATED reports)
that this is a VERY little used IBM feature/extension - and turned out to be a
"non-solution" to the Y2K problem (much less ongoing date formatting).

To see the "medium-commonly used" feature that IBM provides (in a programming
language independent fashion) for date formatting (and information), see the LE
callable services information at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3140/3.5.22

and

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3140/B.0

and

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2140/3.9.6.5.2
```

#### ↳ Re: Dates in the Data Division (one compiler's extension)

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-06T13:08:29-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf0agj$hg7$1@news.eusc.inter.net>`
- **In-Reply-To:** `<ByBQc.10236$cK.4758@newsread2.news.pas.earthlink.net>`
- **References:** `<ByBQc.10236$cK.4758@newsread2.news.pas.earthlink.net>`

```
William M. Klein wrote:

> As a follow-on to another thread, for those who might (or might NOT) like
> extending the data division to support "date fields" and formats, you might want
…[14 more quoted lines elided]…
> 
I would like to have used the Millennium Language Extensions.  They 
would have made the upgrade much easier at the shop where I was. 
However, we had to have the critical systems Y2K ready before the 
extensions were available.  It's like the screen section for the IBM 
mainframe.  Having it in 1985 or before and supported for CICS and 
TSO/ISPF would have been a great productivity enhancement.  In 2004, it 
would probably see little use even if IBM implemented it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
