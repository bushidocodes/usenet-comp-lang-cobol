[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Easytrieve alternative

_4 messages · 4 participants · 2001-02_

---

### Easytrieve alternative

- **From:** John Matheson <john_matheson@acpe.state.ak.us>
- **Date:** 2001-02-21T15:28:08-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A945D17.26E54BED@acpe.state.ak.us>`

```
Can anyone recommend an alternative to CA-Easytrieve as a report writer
on an RS-6000 using COBOL and VSAM files? I have to make a procurement
for our mainframe guys that are used to using Easytrieve on our S390. CA
wants over $30,000 for the privilege of using their product on a little
2 user RISC development box. Sorry if this the wrong forum but I know
nothing about UNIX and I see some Easytrieve folks pass through here
from time to time.
Thanks
john_matheson@acpe.state.ak.us
```

#### ↳ Re: Easytrieve alternative

- **From:** Jeff Baynard <jeffbaynard@home.com>
- **Date:** 2001-02-22T02:14:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6B9E052.7A7%jeffbaynard@home.com>`
- **References:** `<3A945D17.26E54BED@acpe.state.ak.us>`

```
Dunno about the AIX environment, but on OS390 we also have a product called
QuikJob.  It is basically the same as Easytrieve (or is that Vision:Report
or something), but I don't know if it is available for AIX.  Have you ever
thought about using Perl?

Jeff

> From: John Matheson <john_matheson@acpe.state.ak.us>
> Organization: Posted via Supernews, http://www.supernews.com
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Easytrieve alternative

- **From:** "Rufio" <davecawdell@home.com>
- **Date:** 2001-02-22T04:02:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lb0l6.23$Qd4.20225@news1.rdc1.az.home.com>`
- **References:** `<3A945D17.26E54BED@acpe.state.ak.us>`

```
SAS?

"John Matheson" <john_matheson@acpe.state.ak.us> wrote in message
news:3A945D17.26E54BED@acpe.state.ak.us...
> Can anyone recommend an alternative to CA-Easytrieve as a report writer
> on an RS-6000 using COBOL and VSAM files? I have to make a procurement
…[8 more quoted lines elided]…
>
```

#### ↳ [OT] Re: Easytrieve alternative

- **From:** "Anthony Borla" <ajborla@bigpond.com>
- **Date:** 2001-02-22T16:30:14+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ci1l6.713$v5.2736@newsfeeds.bigpond.com>`
- **References:** `<3A945D17.26E54BED@acpe.state.ak.us>`

```
"John Matheson" <john_matheson@acpe.state.ak.us> wrote in message
news:3A945D17.26E54BED@acpe.state.ak.us...
> Can anyone recommend an alternative to CA-Easytrieve as a report writer
> on an RS-6000 using COBOL and VSAM files? I have to make a procurement
…[8 more quoted lines elided]…
>

The standard *NIX utility for file manipulation, which means that it can
also act as a 'report writer' is 'awk'. It is part of any standard *NIX
installation, no additional cost or license fees applicable; I would assume
AIX would also offer it on these terms.

The 'awk' utility is *very* easy to use. It even bears a slight similarity
to Easytrieve in that it automatically loops on each record of the input
file. A typical 'awk' program has the form:

    /* Startup */
    BEGIN {
    ...
    }

    /* Main loop */
    {
    ...
    }

    /* Cleanup */
    END {
    ...
    }

While 'awk' is designed to work primarily with 'delimited' files, it is
able, through its 'substr' function, to read fixed-length record files as
well. I often use it for prototyping, that is, to code preliminary versions
of reports that will later be coded up in COBOL.

Finally, while 'awk' offers may features, it is, as are many such utilites,
quite resource hungry. However this is often a small price to pay for
getting a job done quickly.

I hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
