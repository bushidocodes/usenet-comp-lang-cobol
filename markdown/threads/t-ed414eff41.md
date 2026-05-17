[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DOS program converted to NetExpress printing question

_2 messages · 2 participants · 1998-02_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### DOS program converted to NetExpress printing question

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980218015000.UAA28058@ladder02.news.aol.com>`

```

Hi,

I am in the process of converting my DOS Work Bench 3.2.xx program to
NetExpress 2.0. My program prints to a number of different serial printers.
The way i would accomplish this under DOS was to redirect the printer port to
the serial port with the DOS mode command. In my COBOL program i would then
send the output to the printer port and let DOS do the work of moving it over
to the serial port.

The serial printers that i work with do not come with Win95 drivers.

Any ideas for what would be the best way to handle this under Win95.

Thanks in advance for any ideas,

Bob Hennessey
```

#### ↳ Re: DOS program converted to NetExpress printing question

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed414eff41-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980218015000.UAA28058@ladder02.news.aol.com>`
- **References:** `<19980218015000.UAA28058@ladder02.news.aol.com>`

```

On 18 Feb 1998 01:50:05 GMT, bob··.@a··.com (Bob7536) wrote:

› Hi,
› 
…[11 more quoted lines elided]…
› Thanks in advance for any ideas,

Set up a the GENERIC TEXT PRINTER Driver. Attach it to COM1. There
are some other things you might have to do. Send your print to PRN,
make the generic text printer the default printer. Set the form size
to very large and very wide. Mark the settings continous form. See
if that will fix you up!?!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
