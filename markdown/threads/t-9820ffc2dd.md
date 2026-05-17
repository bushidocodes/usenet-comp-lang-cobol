[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with Report Section

_4 messages · 3 participants · 1996-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Problem with Report Section

- **From:** "tony saywell" <ua-author-13937182@usenetarchives.gap>
- **Date:** 1996-04-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<316DA51E.4CD@iconz.co.nz>`

```
I am trying to use the Cobol Report Section for the first time.

The problem that I have got is when I say 'GENERATE R1-SPR-DETAILS' my
program goes into an endless loop. If I ctrl-C and look in the print file it
has the Heading printed over and over again.

The report I am trying to generate is a very simple one ( a Despatch Note
) that has 1 to 4 detail lines, with no control breaks.

I am trying to set this up using the cobol manual, except the manual doesn't
show any examples.

If anyone can send me some example code or knows where the problem may be
could they please e-mail me.

Regards,

Tony Saywell to··.@ico··o.nz
Analyst/Programmer
Auckland, New Zealand
```

#### ↳ Re: Problem with Report Section

- **From:** "jsa" <ua-author-2098004@usenetarchives.gap>
- **Date:** 1996-04-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9820ffc2dd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<316DA51E.4CD@iconz.co.nz>`
- **References:** `<316DA51E.4CD@iconz.co.nz>`

```
Tony Saywell wrote:
› > I am trying to use the Cobol Report Section for the first time.
>
…[17 more quoted lines elided]…
> Auckland, New Zealand

Tony, this sort of thing can happen if you use a LINE IS clause on
a detail that is higher on the page than the heading.  System trys
to print detail, but since line specified is gone by on this page
it ejects a page.  Then Header routine kicks in and header is
printed.  Lo-and Behold, it is now further down the page than the
detail is specified to appear.  Time to page eject.... You get the
picture.  Use Line Plus instead of Line Is..

Without knowing more specifics, this is the best I can do.


__________________________________________
John Andersen                             |
Juneau Alaska                             |
__________________________________________|
```

#### ↳ Re: Problem with Report Section

- **From:** "wbla..." <ua-author-620238@usenetarchives.gap>
- **Date:** 1996-04-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9820ffc2dd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<316DA51E.4CD@iconz.co.nz>`
- **References:** `<316DA51E.4CD@iconz.co.nz>`

```
On Fri, 12 Apr 1996 12:25:36, mor··.@lin··c.nz (Morris, Peter)
wrote:

› In article <316··.@ico··o.nz> Tony Saywell  writes:
›› I am trying to use the Cobol Report Section for the first time. 
…[8 more quoted lines elided]…
› Cobol II for the IBM. Shame really as it's amazingly amazing to use.

I had to hijack this, as I missed the original post ...

Check the specification of your page size (I believe it's LINAGE, but
I could be wrong, as it's been quite a while). The GENERATE statement
will automatically create a new header line every time its line count
exceeds the page line limit ... if that limit is zero, that puppy will
loop forever ...



Regards,
Bill
```

#### ↳ Re: Problem with Report Section

- **From:** "wbla..." <ua-author-620238@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9820ffc2dd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<316DA51E.4CD@iconz.co.nz>`
- **References:** `<316DA51E.4CD@iconz.co.nz>`

```
On Thu, 11 Apr 1996 17:34:38 -0700, Tony Saywell
wrote:

› I am trying to use the Cobol Report Section for the first time. 
› 
…[11 more quoted lines elided]…
› could they please e-mail me.

Tony ...

I doubt examples will help that much ... why not just tell us what
platform you're running on, and post the RD and relevant portions
of the procedure division, and let the rest of us see what we can
find?


Regards,
Bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
