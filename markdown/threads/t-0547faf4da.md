[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Day of week date routine

_4 messages · 4 participants · 1995-11_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Day of week date routine

- **From:** "gkam..." <ua-author-2961498@usenetarchives.gap>
- **Date:** 1995-11-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47s276$3ni@ixnews3.ix.netcom.com>`

```
I am looking for logic that will return a numeric day of week
indicator when a gregorian (mmddyy) date is fed into it.

Thanks in advance for any help.

George K.
```

#### ↳ Re: Day of week date routine

- **From:** "eha..." <ua-author-933943@usenetarchives.gap>
- **Date:** 1995-11-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0547faf4da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<47s276$3ni@ixnews3.ix.netcom.com>`
- **References:** `<47s276$3ni@ixnews3.ix.netcom.com>`

```
In article <47s276$3.··.@ixn··m.com>,
GKA··.@IX.··M.COM (George K.) wrote:
› I am looking for logic that will return a numeric day of week
› indicator when a gregorian (mmddyy) date is fed into it.
›
› Thanks in advance for any help.

I wrote a routine to do this a long time ago. I remember using a 'base date'
then calculating the number of days between the dates. Divide that by 7 and
get the remainder. That will tell you what the day is.
```

#### ↳ Re: Day of week date routine

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-11-09T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0547faf4da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<47s276$3ni@ixnews3.ix.netcom.com>`
- **References:** `<47s276$3ni@ixnews3.ix.netcom.com>`

```
In article <47s276$3.··.@ixn··m.com> George K.,
GKA··.@IX.··M.COM writes:
› I am looking for logic that will return a numeric day of week
› indicator when a gregorian (mmddyy) date is fed into it.  
…[4 more quoted lines elided]…
› 
I assume you are using an up-to-date compiler. If so, format the
date as yyyymmdd, and do the following:

FUNCTION MOD (FUNCTION INTEGER-OF-DATE (your-date)) 7)

The result is 1 for Monday, through 6 for Saturday, and 0 for
Sunday.
Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

#### ↳ Re: Day of week date routine

- **From:** "john andersen" <ua-author-843256@usenetarchives.gap>
- **Date:** 1995-11-10T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0547faf4da-p4@usenetarchives.gap>`
- **In-Reply-To:** `<47s276$3ni@ixnews3.ix.netcom.com>`
- **References:** `<47s276$3ni@ixnews3.ix.netcom.com>`

```
GKA··.@IX.··M.COM (George K.) wrote:
› I am looking for logic that will return a numeric day of week
› indicator when a gregorian (mmddyy) date is fed into it.  
…[4 more quoted lines elided]…
› 

This routine is included here:
http://www.alaska.net/~norcom/dates.html

Comes with source code.
------------------------------------------------------
John Andersen
Juneau, Alaska
and··.@ala··a.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
