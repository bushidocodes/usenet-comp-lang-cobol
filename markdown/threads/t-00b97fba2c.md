[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 8 bit C boolean in MF Cobol 4.038

_2 messages · 2 participants · 1999-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### 8 bit C boolean in MF Cobol 4.038

- **From:** Alan Dreyer <chieflilal@triton.net>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385BF23D.AA37D012@triton.net>`

```
I writing a program in Cobol that does calls to the Win API.  I need to
know how to define the equivalent of a C 8 bit boolean value in MF Cobol
4.038.  Any assistance would be greatly appreciated.

Thanks.
Al Dreyer
```

#### ↳ Re: 8 bit C boolean in MF Cobol 4.038

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MFe84.874$ra.23803@dfiatx1-snr1.gtei.net>`
- **References:** `<385BF23D.AA37D012@triton.net>`

```
Well, I'm not a C/C++ guy, but an eight-bit value should be a PIC X(01). (If
you use COMP-X you can get numeric values in it pretty easily).

But...

Which Win32 API call uses an 8-bit value? Even within structures I think
most everything is aligned at least 16 bits.

If you post the name(s) of the Win32API functions you are contemplating,
perhaps someone will have specific COBOL code you  can adapt.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
