[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT x FROM DATE issue

_4 messages · 4 participants · 1997-01 → 1998-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Date and calendar processing`](../topics.md#dates)

---

### ACCEPT x FROM DATE issue

- **From:** "ph..." <ua-author-17072630@usenetarchives.gap>
- **Date:** 1997-01-14T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1997Jan15.171737.14661@RedBrick.COM>`

```

Anyone have a good workaround for the fact that the ACCEPT identifier FROM
DATE command gives only two digits for the year? I'm coding some routines to
timestamp output files and would feel sort of stupid if they "expire" in three
years.

What are Y2K programmers doing to get around this?

- Paul
```

#### ↳ Re: ACCEPT x FROM DATE issue

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-01-14T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb02018fbb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan15.171737.14661@RedBrick.COM>`
- **References:** `<1997Jan15.171737.14661@RedBrick.COM>`

```

Paul Horn wrote:
› 
› Anyone have a good workaround for the fact that the ACCEPT identifier FROM
…[6 more quoted lines elided]…
›  - Paul

There are several ways around this:

1. As Sallie Kudra mentioned, if your compiler supports intrinsic functions
then use the appropriate one. You might want to investigate upgrading
your COBOL compiler if necessary. If you can't do that in a reasonable
time frame, see below. Also, if you are using the IBM COBOL II compiler
there is an APAR to give you an assembler subprogram which returns the
full date.

2. If #1 above is not possible, you could write a C or assembler subprogram
to obtain the date with 4-digit year from the operating system. Does
your operating system support 4-digit years? Some don't.

3. Ignore the whole thing, store the date with 2-digit year, and let the
somebody else figure it out. This could be a cost-effective solution if
the date is only printed and never compared to another date, used to
compute day-of-week, et cetera.

4. Add a little "date-windowing" logic to your program to build the date
with the century. If you're always writing current-date, just
add something like this to the program:
IF CURRENT-YY > 95
MOVE '19' TO CURRENT-CENTURY
ELSE
MOVE '20' TO CURRENT-CENTURY
END-IF
This buys you a lot of time, and it's easy to do. It will probably more
than cover the useful life of your program. Of course, it's no
fun to replicate it in 1000 programs, and could lead to a maintenance
nightmare when you get your #1 solution.

5. If your systems will be doing a lot of date windowing, like #4 above,
you might consider writing a standard subprogram to convert YY to CCYY
using a standard cutoff year. It could also be helpful interpreting
dates in existing files. Of course you have to know how wide your date
horizon is.

Good Luck!

Arnold Trembley
Software Engineer I (and working on a Year 2000 project)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: ACCEPT x FROM DATE issue

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1997-01-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb02018fbb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan15.171737.14661@RedBrick.COM>`
- **References:** `<1997Jan15.171737.14661@RedBrick.COM>`

```

In a sudden flurry of activity, ph··.@lin··e.com (Paul Horn) wrote:
› Anyone have a good workaround for the fact that the ACCEPT identifier FROM 
› DATE command gives only two digits for the year? I'm coding some routines to 
…[4 more quoted lines elided]…
› 

It really depends on how long you plan to use the file. Probably the
easiest way is to pick a number (say 80) and compare the returned 2
digit year against it, assuming that anything over 80 is in the 1900's
and place the '19' in front of it while anything under 80 is in the
2000's, placing the '20' in front of it.

Dave

The opinions expressed in this post are purely my own.
You may e-mail replies to: ren··.@d··.com
```

#### ↳ Re: ACCEPT x FROM DATE issue

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-11-02T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb02018fbb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan15.171737.14661@RedBrick.COM>`
- **References:** `<1997Jan15.171737.14661@RedBrick.COM>`

```
The latest Micro Focus products (3.4, 4.0 and NetExpress) support the new
ACCEPT x FROM DATE syntax which will return a four digit year. The
syntax is as follows:

...
ACCEPT x FROM DATE YYYYMMDD.
...

Where x is a PIC X(8) or equivalent.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

sallie j kudra wrote in message ...
› ph··.@lin··e.com (Paul Horn) writes:
› 
…[32 more quoted lines elided]…
› ===========================================================================
=====
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
