[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus report to NT printer

_4 messages · 2 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus report to NT printer

- **From:** britishvicar@yahoo.com (Karl O)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3641e0f4.166324421@news.enter.net>`

```
Help!!

I have a MF COBOL prog that writes to LPT1 and works fine. Now the
printer is redirected to a Windows NT shared printer. The OPEN gets a
status 37. If I TYPE a file to LPT1 it prints just fine....whats my
problem???

Thanks
Karl
```

#### ↳ Re: Microfocus report to NT printer

- **From:** britishvicar@yahoo.com (Karl O)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3641f0c5.170373624@news.enter.net>`
- **References:** `<3641e0f4.166324421@news.enter.net>`

```
Thanks anyway...I found the solution. Found an NT configuration that
could be set up.

Thanks

On Thu, 05 Nov 1998 17:33:57 GMT, britishvicar@yahoo.com (Karl O)
wrote:

>Help!!
>
…[6 more quoted lines elided]…
>Karl
```

##### ↳ ↳ Solution!!!

- **From:** britishvicar@yahoo.com (Karl O)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36432fa7.252007788@news.enter.net>`
- **References:** `<3641e0f4.166324421@news.enter.net> <3641f0c5.170373624@news.enter.net>`

```
The answer was to change the properties defined for the NT printer.
The is an option to "Print immediately (default) or to "Spool the
entire document before printing"
It appears that OPEN OUTPUT needing exclusive control of the printer
is in direct conflict with the default option.

Hope this helps...it worked for me

Cheers

Karl 

On Thu, 05 Nov 1998 18:39:36 GMT, britishvicar@yahoo.com (Karl O)
wrote:

>Thanks anyway...I found the solution. Found an NT configuration that
>could be set up.
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Microfocus report to NT printer

- **From:** jeff@jakfield.xu-netx.com (Jeff York)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36441115.3663477@news.u-net.com>`
- **References:** `<3641e0f4.166324421@news.enter.net> <3641f0c5.170373624@news.enter.net>`

```
britishvicar@yahoo.com (Karl O) wrote:

>Thanks anyway...I found the solution. Found an NT configuration that
>could be set up.

Out of interest,  what was it?

>
>Thanks
…[12 more quoted lines elided]…
>>Karl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
