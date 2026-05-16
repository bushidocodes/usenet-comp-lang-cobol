[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Have anyone a sample with "GetLogicalDriveStrings"

_1 message · 1 participant · 2008-05_

---

### Re: Have anyone a sample with "GetLogicalDriveStrings"

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-05-14T08:11:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5fef9e8-d46f-4762-976b-9eb7286632e1@m45g2000hsb.googlegroups.com>`
- **References:** `<9ba01cb1-10ac-4bee-9fd7-dae80e06d93b@r66g2000hsg.googlegroups.com>`

```
On May 14, 2:34 am, Bernd.Rie...@riemke-it.de wrote:
> Hi,
> I need a cobol api sample for the "GetLogicalDriveStrings"
…[15 more quoted lines elided]…
> I use the MF Net Express as a compiler...



Hi,

Try some thing like this:

	environment division.
	configuration section.

		special-names.
			call-convention 74 is winapi.


	working-storage section.

	01  ld-string-size		pic  9(9)   comp-5 value 512.
	01  ld-string		pic  x(512) value spaces.
	01  re-code		pic s9(9)   comp-5 value 0.


	procedure division winapi.
	100-main-section.

	call  winapi  "GetLogicalDriveStringsA" using
		by value  	ld-string-size
		by reference	ld-string
	          returning	re-code
	end-call.

Kellie.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
