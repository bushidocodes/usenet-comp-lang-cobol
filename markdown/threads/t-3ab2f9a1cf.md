[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# xml generate error

_2 messages · 2 participants · 2006-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### xml generate error

- **From:** "shabi" <shabinaz@gmail.com>
- **Date:** 2006-02-15T00:30:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139992211.180474.249570@g47g2000cwa.googlegroups.com>`

```
In COBOL, I am generating an XML from a COBOL copybook by the use of
the 'XML GENERATE' statement. I find the following problem when I use
special characters.
When I have a special character say, & in a field in the second
potition, the XML generated looks fine and has covnerted & to the
correct escape sequence in the output XML. But when I have the '&' as
the first character of a field, the XML generated is junk.
Anyone any ideas how I could solve this. This is a critical issue in my
Project and any comments would be really helpful.
```

#### ↳ Re: xml generate error

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-15T21:12:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VOMIf.59393$Ak4.14310@fe09.news.easynews.com>`
- **References:** `<1139992211.180474.249570@g47g2000cwa.googlegroups.com>`

```
Did you see/read

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr30/6.2.41.2.1

"Any remaining instances of the five characters & (ampersand), ' (apostrophe), > 
(greater-than sign), < (less-than sign), and " (quotation mark) are converted 
into the equivalent XML references '&amp;', '&apos;', '&gt;', '&lt;', and 
'&quot;', respectively. "

If you are using IBM Enterprise COBOL V3.4 and the compiler is NOT working this 
way, then you should report it to IBM support.  (You don't tell us what compiler 
you are using, so this was just a GUESS given the references to XML and 
GENERATE)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
