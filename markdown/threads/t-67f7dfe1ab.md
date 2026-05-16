[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing from a CICS program

_2 messages · 2 participants · 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Printing from a CICS program

- **From:** timothyp@tampabay.rr.com (Timothy P)
- **Date:** 2002-11-06T12:37:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ef5c91a.0211061237.7d633e12@posting.google.com>`

```
I am trying to modify an existing CICS program.
The program currently prints a tax receipt in SIMPLEX mode (Prints on
one side). I have a client with a new duplex printer (Kyocera/Mita
FS-3800). I determined what the native command is I have to send the
printer to print in DUPLEX mode (Prints on both sides).

Where in the CICS program do I pass the native command?

Any help would be appreciated

Thanks,
Tim
```

#### ↳ Re: Printing from a CICS program

- **From:** "David P. Bretz" <davidbretz@earthlink.net>
- **Date:** 2002-11-16T22:22:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DD6C471.9F2D7D55@earthlink.net>`
- **References:** `<2ef5c91a.0211061237.7d633e12@posting.google.com>`

```
it's been my experience when sending commands to a printer from CICS that
you place the commands at the beginning of the information you're
printing.

Dave

Timothy P wrote:

> I am trying to modify an existing CICS program.
> The program currently prints a tax receipt in SIMPLEX mode (Prints on
…[9 more quoted lines elided]…
> Tim
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
