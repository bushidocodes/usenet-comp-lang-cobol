[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MAKE file for COBOL

_4 messages · 3 participants · 2001-08_

---

### MAKE file for COBOL

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2001-08-06T13:24:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0108061224.6ef098a7@posting.google.com>`

```
While we can use MF NetExpress as a reasonable IDE and thus use its
dependency analysis etc. if we want to run the compilations in batch
mode we lose the dependencies and have to do a full re-compile. In
practice this isn;t a major problem because it doesn't take *that*
long, however, wouldn't it be nice if...

I haven't used MAKE etc. for some time but know that it is possible to
set up Make files to call the COBOL compiler subject to the
appropriate dependency rules and this is where the problem lies -
setting up all the dependency rules. I seem to recal that there is a
UNIX utility IMAKE (or similar) that will perform the dependency
analysis but it knows only(?) about C/C++ syntax. Surely there is some
utility that understands COBOL syntax and can create the Make
dependency rules automatically ??

(MF have said that they don't believe the NetEx project dependency
information can be readily accessed outside of the NetExpress IDE)

Any suggestions ?

graham
Olympic Computers
```

#### ↳ Re: MAKE file for COBOL

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-08-07T21:47:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slZb7.18662$t41.349936@newsread2.prod.itd.earthlink.net>`
- **References:** `<8a02b0a1.0108061224.6ef098a7@posting.google.com>`

```
Years ago I worked with Realia Cobol and it had a Make file generator that
would look at the Cobol programs and figure out the dependencies of copy,
call, etc. The generated make file could then be run batch. Very nice.
```

##### ↳ ↳ Re: MAKE file for COBOL

- **From:** "Charles Godwin" <charles@godwin.ca>
- **Date:** 2001-08-07T19:55:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mc%b7.31752$jA2.2212220@news20.bellglobal.com>`
- **References:** `<8a02b0a1.0108061224.6ef098a7@posting.google.com> <slZb7.18662$t41.349936@newsread2.prod.itd.earthlink.net>`

```
This is still part of the product although we don't emphasis it. It's part
of the PAN/LCM configuration Management software.

Charles Godwin
Development Manager - Realia Products
Computer Associates

"Robert M. Pritchett - RMP Consulting Partners LLC"
<Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Do
llars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Tho
usand-Dollars-To-RMPCP-For-Each-Message> wrote in message
news:slZb7.18662$t41.349936@newsread2.prod.itd.earthlink.net...
> Years ago I worked with Realia Cobol and it had a Make file generator that
> would look at the Cobol programs and figure out the dependencies of copy,
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MAKE file for COBOL

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2001-08-08T03:41:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0108080241.24df1a00@posting.google.com>`
- **References:** `<8a02b0a1.0108061224.6ef098a7@posting.google.com> <slZb7.18662$t41.349936@newsread2.prod.itd.earthlink.net> <mc%b7.31752$jA2.2212220@news20.bellglobal.com>`

```
"Charles Godwin" <charles@godwin.ca> wrote in message news:<mc%b7.31752$jA2.2212220@news20.bellglobal.com>...
> This is still part of the product although we don't emphasis it. It's part
> of the PAN/LCM configuration Management software.
> 

But you should, you really, really should !!

Interactive IDEs are all very well but real applications need batch
compilations, no, but seriously...

Being able to run impact analyses based on file changes is very
useful; without a usable dependency structure one has to resort to
various search tools and while these do work, because they don't know
the COBOL syntax, they can pick up a lot of noise (matches in comments
etc. or commented out code) and this means there is still a lot of
manual checking necessary. Using a stupid build within an IDE means
that you can recompile all affected modules readily but it may be that
had you known which ones were affected (e.g. some very critical
modules that you didn't want to change) or the full scale of the
changes (e.g. where it may mean a virtually complete system
replacement for existing users rather than a small scale update) you
would have adopted a different approach.

I'm rather surprised there aren't any smart programmable analysers
about; or perhaps its possible with utilities like awk, but I thought
that with COBOL being such a popular language someone must had
produced such a utility decades ago.

graham
Olympic Computers (UK)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
