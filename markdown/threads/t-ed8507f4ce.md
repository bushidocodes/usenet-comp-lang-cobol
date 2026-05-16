[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to trap B34 abends in COBOL OS390

_2 messages · 2 participants · 1999-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How to trap B34 abends in COBOL OS390

- **From:** "Jordaens Robert" <icare@wanadoo.be>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81om34$1kp8$1@buty.wanadoo.nl>`

```
Anyone that knows how to trap a B34 or any file exception in OS390 so that
the program can give its own message and finish normally ?

Thanks,
```

#### ↳ Re: How to trap B34 abends in COBOL OS390

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383FF170.FA010F88@nbnet.nb.ca>`
- **References:** `<81om34$1kp8$1@buty.wanadoo.nl>`

```
Add a status-code on the select statement (status-code is pic xx and is
aprogrammer-defined field in working-storage). Then check the
status-code after ALL i-o statements for the file(s).  Note that the IBM
abend is trapped and mapped to the COBOL defined status-code.  See the
manual for details.

Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca or
cmorris@fox.nstn.ca 

Jordaens Robert wrote:
> 
> Anyone that knows how to trap a B34 or any file exception in OS390 so that
> the program can give its own message and finish normally ?
> 
> Thanks,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
