[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CA Realia II VS MicroFocus COBOL?

_4 messages · 3 participants · 1995-04 → 1995-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### CA Realia II VS MicroFocus COBOL?

- **From:** "qyq..." <ua-author-1933572@usenetarchives.gap>
- **Date:** 1995-04-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3npjgn$14mk@usenetw1.news.prodigy.com>`

```
I was recently involved in evaluating CA & MF COBOL at my MVS shop. My
impressions are that while MF is more powerful, CA is much easier to use.
Major problem areas in both products appear to be with file transfer (We
use LOTS of packed data); source code control (the library security is
easy to bypass); and IMS "emulation" on the PC.
Has anyone else tried both products? Your thoughts will be appreciated!

regards,
J.P.
```

#### ↳ Re: CA Realia II VS MicroFocus COBOL?

- **From:** "krl..." <ua-author-8472398@usenetarchives.gap>
- **Date:** 1995-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cebe1be1a5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3npjgn$14mk@usenetw1.news.prodigy.com>`
- **References:** `<3npjgn$14mk@usenetw1.news.prodigy.com>`

```
I just started evaluating MF-Cobol today and I will be evaluating CA-
Realia very soon. I am also very interested in any comments. By the way
I have the thankless task of migrating a fairly large PC application
written in RM-Cobol/74 to whichever of the above I choose. Anyone done
THAT. I'd appreciate any tips along those lines too. Thanks in advance!
```

##### ↳ ↳ Re: CA Realia II VS MicroFocus COBOL?

- **From:** "qyq..." <ua-author-1933572@usenetarchives.gap>
- **Date:** 1995-04-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cebe1be1a5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cebe1be1a5-p2@usenetarchives.gap>`
- **References:** `<3npjgn$14mk@usenetw1.news.prodigy.com> <gap-cebe1be1a5-p2@usenetarchives.gap>`

```
KRL··.@pro··y.com (Joseph Giachero) wrote:
›
› I just started evaluating MF-Cobol today and I will be evaluating CA-
› Realia very soon. I am also very interested in any comments.

Ah, innocence! During my own evaluation of CA & MF, I had planned to
spend 30 days on each product. It took over 30 days just to get MF
installed and tuned, so that I didn't get a General Protection Fault
every 5 minutes! My evaluation lasted almost 4 months! However, I
admit that I am a mainframe guy, and not a PC guru. But if you want to
get up and running quickly, I would strongly suggest the CA product. I
had it installed and working well in only 2 days.
Some collateral issues:
1. Carefully read the products' licensing agreements regarding the
shipping of finished executable code to end users, and the licensing of
the repective run time systems.
2. If you are a LAN user, check out CA's site license, which can
save a bundle of money. MF required a separate copy to be purchased for
each PC (although this may have changed since my evaluation).
3. If you plan to download mainframe development onto the PC level,
be aware of the headaches involved when using EBCDIC data on the PC.
It's either this, or attempt to translate to/from ASCII. Sure, it is
easy to translate, unless you work with a lot of COMP/COMP-3 data.
4. Regarding source code and file transfer to/from mainframe. MF
uses whichever transfer utility your emulation supports, while CA
provides its own mainframe software. It doesn't come in the product
package! You have to request it from CA.


-
JPG QYQ··.@pro··y.com
```

#### ↳ Re: CA Realia II VS MicroFocus COBOL?

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cebe1be1a5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3npjgn$14mk@usenetw1.news.prodigy.com>`
- **References:** `<3npjgn$14mk@usenetw1.news.prodigy.com>`

```

JG> I just started evaluating MF-Cobol today and I will be evaluating
JG> CA-Realia very soon. I am also very interested in any comments.

Please let us all know as your study progresses.
---
* SLMR 2.1a * Windows: The CP/M of the future!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
