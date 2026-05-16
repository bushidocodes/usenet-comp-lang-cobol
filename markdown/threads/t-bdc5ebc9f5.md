[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Squares in my output file???????????????

_4 messages · 4 participants · 2002-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Squares in my output file???????????????

- **From:** jfrick@sc.rr.com
- **Date:** 2002-02-27T02:18:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com>`

```
I wrote a program and finally got it to run but my output file ended
up with squares throughout it in between my headings and data. Why did
this happen? 

Jim
jfrick@sc.rr.com
```

#### ↳ Re: Squares in my output file???????????????

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-02-27T03:55:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-3NxqulkTiUMl@thishost>`
- **References:** `<75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com>`

```
On Wed, 27 Feb 2002 02:18:03 UTC, jfrick@sc.rr.com wrote:

> I wrote a program and finally got it to run but my output file ended
> up with squares throughout it in between my headings and data. Why did
…[4 more quoted lines elided]…
> 

A bug :-)

You did not initialize your working storage areas with spaces.
```

#### ↳ Re: Squares in my output file???????????????

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-02-27T00:55:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cv_e8.74591$JZ.9204335@news20.bellglobal.com>`
- **References:** `<75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com>`

```
The fields are initialized to nulls instead of spaces.  You are probably
setting up the title as so:
01 title.
    02 filler        picture x(4) value "word".
    02 filler        picture xx.
    02 filler        picture xx value "cc
The filler between the words is not initialized (make it space with a value
statement).

Donald

<jfrick@sc.rr.com> wrote in message
news:75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com...
> I wrote a program and finally got it to run but my output file ended
> up with squares throughout it in between my headings and data. Why did
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Squares in my output file???????????????

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-02-27T13:01:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sM4f8.4647$E11.783@nwrddc02.gnilink.net>`
- **References:** `<75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com>`

```
<jfrick@sc.rr.com> wrote in message
news:75go7ucq7k2ou9m447cgrv6dv3l2tbhqi0@4ax.com...
> I wrote a program and finally got it to run but my output file ended
> up with squares throughout it in between my headings and data. Why did
> this happen?

If you are trying to read your output in Microsoft Word(r), carriage returns
also appear as "squares." (This also happens with WordPad, but not with
NotePad).

If you want to check your output completely, view it with a hex viewer,
looking for CR, LF or CRLF at the end of lines in addition to embedded NULs
(x'00').

You can solve embedded nulls easily enough using INSPECT
CONVERTING|REPLACING just prior to writing, although MOVE'ing SPACE to the
output group item, INITIALIZE'ing the print line record, then MOVE'ing the
data would be more elegant and is the recommended method.

When I am going to create a "report file" which goes to disk, I generally
make the file SEQUENTIAL rather then LINE SEQUENTIAL and explicitly write
the end-of-line terminator desired.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
