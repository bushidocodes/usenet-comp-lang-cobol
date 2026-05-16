[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Cobol Error- Exception in page error

_2 messages · 2 participants · 2005-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Cobol Error- Exception in page error

- **From:** "mvalecruz5@mcyber.com" <mvalecruz5@mcyber.com>
- **Date:** 2005-05-03T11:57:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1115146666.852298.45540@g14g2000cwa.googlegroups.com>`

```
Our product is written in Netcobol for Windows 7.0. User is running
programs stored on a Window 2000 server. End User is going thru Citrix
server to access program and files. The "exception in page error"s are
random happing on any program at any time. We first thought it was
Windows Client Access License causing the problem. Hardware people have
since bump up CAL licenses by 100.
The error only occur in the Citrix sessions and not to the workstation
directly on the network.

Any comment you may have please...

Michael ValeCruz
Atlanta, GA
```

#### ↳ Re: Fujitsu Cobol Error- Exception in page error

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-05-04T12:33:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dqjjqF6r394dU1@individual.net>`
- **References:** `<1115146666.852298.45540@g14g2000cwa.googlegroups.com>`

```

<mvalecruz5@mcyber.com> wrote in message
news:1115146666.852298.45540@g14g2000cwa.googlegroups.com...
> Our product is written in Netcobol for Windows 7.0. User is running
> programs stored on a Window 2000 server. End User is going thru Citrix
…[8 more quoted lines elided]…
>

The MySQL open source people have exactly the same problem with their
product running on windows 2000 server. Intermittent error messages and
locking problems that are very hard to duplicate.

They combed the C libraries to try and find the problem, so far without
success (at least that was the last I heard, about a week ago).

The Fujitsu RTS may be suffering from a similar problem.

It is pretty upsetting when code runs correctly in most environments, then
is deployed to one where problems arise... ;-)

I'd pass this one to Fujitsu as soon as you can. It is likely the people in
Japan will want to look at it.

Good luck.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
