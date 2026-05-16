[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Mainframe to IBM Unix Cobol conversion?

_3 messages · 3 participants · 1999-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM Mainframe to IBM Unix Cobol conversion?

- **From:** "Al Ni���o" <please_reply@newsgroup.com>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fl1qu$7g2@sjx-ixn4.ix.netcom.com>`

```
Hi all, I asked this question earlier and didn't really give enough info. on
source and target machines/OS's

I want to know if it's easy to do a Cobol conversion between these two
environments and what would be involved, what tools/services are available,
etc.  Ideally the source code would be taken from the Mainframe, recompiled
on the Unix box and then everything would work perfectly (!)  I doubt if its
that simple.

On the mainframe :

The Cobol version is IBM VS Cobol II Release 4.0

The operating system version is MVS/ESA Version 5 Release 2.2

The version of UNIX on the IBM box is Version M-11/16/88f

Cobol to be used, based on your advice.

Any thoughts/ideas?

Thanks in anticipation!
```

#### ↳ Re: IBM Mainframe to IBM Unix Cobol conversion?

- **From:** "Calle" <markus.carl@fen.baynet.de>
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fljhp$a4g$1@freenet-b.fen.baynet.de>`
- **References:** `<7fl1qu$7g2@sjx-ixn4.ix.netcom.com>`

```
Hi,
we got the right tool for you. It���s called ICS-CASE and it���s a development
tool for portable COBOL code. It also contains modules for migration and
conversion for nearly EVERY (!) platform.
For further information mail to ics-khatib@fen.baynet.de

Hope to hear from you,

Calle
```

#### ↳ Re: IBM Mainframe to IBM Unix Cobol conversion?

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37211538.E943AEF0@siber.com>`
- **References:** `<7fl1qu$7g2@sjx-ixn4.ix.netcom.com>`

```
Al Niï¿½o wrote:
> 
> Hi all, I asked this question earlier and didn't really give enough info. on
…[6 more quoted lines elided]…
> that simple.

You can use our tool called IBM2FSC.
It would convert IBM COBOL dialects
OSVS, VSII and likely SAA to Fujitsu Cobol.
Please check it out at http://www.siber.com/sct/convs/

If you want to play with conversions
and create your own converter, based
on a set of transformations that we sell,
then you can use CobolTransformer
which is a general toolkit for building
Cobol converters and analyzers.
http://www.siber.com/sct/

Best regards,
Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
