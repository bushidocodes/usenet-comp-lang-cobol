[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I need help with reading multiple records off one data file

_1 message · 1 participant · 2002-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: I need help with reading multiple records off one data file

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-08-10T03:41:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D54C3A0.40506@optonline.NOSPAM.net>`
- **References:** `<7d57a35f.0207280252.3bb96ddc@posting.google.com> <fcd09c56.0207281206.5f56a0ae@posting.google.com> <93dfc7c7.0208040513.2bab448f@posting.google.com> <jvyyrzubevmbagrfvasbezngvpnpbz.h0fma90.pminews@News.CIS.DFN.DE> <217e491a.0208061130.60692e91@posting.google.com>`

```
Richard wrote:
> "Willem Clements" <willem@horizontes-informatica.com> wrote > 
> 
…[15 more quoted lines elided]…
> operation but there is a valid duplicate alternate key.

I wouldn't test for only '00' after a READ. I'd define an 88 for use 
after READs which includes the '02' value, as well as any others which 
also represent valid READs with some special attribute.

If you don't like 88's, you can code an EVALUATE which treats '00' & 
'02' as valid READS, e.g.:

EVALUATE 
	file-status
WHEN 
		ZEROS
WHEN 
		'02'
WHEN 
		<any others>
	continue
WHEN 
		OTHER
	<handle the error here>
END-EVALUATE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
