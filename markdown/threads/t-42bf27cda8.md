[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol under SCO Unix with Fileshare

_2 messages · 2 participants · 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol under SCO Unix with Fileshare

- **From:** grwallace@taynet.co.uk ()
- **Date:** 1998-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v3eie$lh5$1@phys-ma.sol.co.uk>`

```
We are trying to get a medium-sized application (up to 50 users) to
run under Fileshare on a SCO Unix platform.

When about 30 users log in we get errors and the whole system falls
over.

We pay MF maintenance and, in general, we find that their products
work.

We would be pleased to here from anyone out there who may have a
similar system, and who may have something to say on ths subject

regards,

Gordon Wallace

grwallace@taynet.co.uk
```

#### ↳ Re: MF Cobol under SCO Unix with Fileshare

- **From:** nick@asheath.demon.co.uk (Nick & Carol Lucas-White)
- **Date:** 1998-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36162c5a.2365197@news.demon.co.uk>`
- **References:** `<6v3eie$lh5$1@phys-ma.sol.co.uk>`

```
On Sat, 03 Oct 1998 04:53:25 GMT, grwallace@taynet.co.uk () wrote:

>We are trying to get a medium-sized application (up to 50 users) to
>run under Fileshare on a SCO Unix platform.
…[9 more quoted lines elided]…
>

You don't say what sort of errors, are they cobol error messages, SCO
messages or what ?

I had a problem with the Unix conecting to the 'net everytime it fired
up the MF CCI but I traced this to a Morningstar PPP filter file
needing the entry MFCOB PASS in it so that it did not have to identify
the service being used with the Domain name server. Apart from that
I've not experienced any other problems. Are all the users logging in
with the same login/password as this may cause additional problems.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
