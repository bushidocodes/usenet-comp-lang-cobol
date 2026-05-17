[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Report Layout - Widows and Orphans

_2 messages · 2 participants · 1996-01_

---

### Report Layout - Widows and Orphans

- **From:** "cswa..." <ua-author-15697567@usenetarchives.gap>
- **Date:** 1996-01-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d9o5b$fh5@ixnews2.ix.netcom.com>`

```
We have been given a challenge in a COBOL II class to produce a report
grouped on one field within another field. No problem! But,we want to
prevent a single line at the bottom or top of a page. Any suggestions?
Is this a place to use buffered input (haven't studied it but I have
seen something regarding it in another book).

Thanks for any replies


Chuck Swafford
csw··.@ix.··m.com
cbs··.@cbs··e.com
```

#### ↳ Re: Report Layout - Widows and Orphans

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-01-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58b8c96ccf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4d9o5b$fh5@ixnews2.ix.netcom.com>`
- **References:** `<4d9o5b$fh5@ixnews2.ix.netcom.com>`

```
csw··.@ix.··m.com (Chuck Swafford) wrote:

› We have been given a challenge in a COBOL II class to produce a report
› grouped on one field within another field. No problem! But,we want to
› prevent a single line at the bottom or top of a page. Any suggestions?
› Is this a place to use buffered input (haven't studied it but I have
› seen something regarding it in another book).

Not buffering, but logic. The rules you implement for print
determines the look of the report.

so that a perform loop may look like this:
....
write a-detail-line
if end-of-page perform ovflo.
this does not guarantee that there will be detail after this ovflo.

alternatve code is:
read-loop.
if end-of-page....
read ... at end...
break logic.....
write ....
this code would cause a title with nothing on it

this is closer:
write-a-detail section.
if end-of-page .....
write .....
this guarantees that a page is not empty..

there is soooooo many things to consider, end-of-page earlier on
breaks than on detail etc...
.now is the time...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
