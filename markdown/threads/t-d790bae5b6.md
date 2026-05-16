[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Digital Vax Cobol

_1 message · 1 participant · 2003-12_

---

### Re: Digital Vax Cobol

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-11T09:11:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tZ_Bb.6330$aF2.828001@news20.bellglobal.com>`
- **In-Reply-To:** `<br9nld$qq3$1@rrz.allgaeu.org>`
- **References:** `<br9nld$qq3$1@rrz.allgaeu.org>`

```
Volker Englisch wrote:
> Hi!
> 
…[74 more quoted lines elided]…
> Volker

The most likely problem (and I do not have a Vax to check on) is that 
the XX field is actually "space,5" or "5,space".  Neither of those *is* 
numeric.  Why do you want to accept the two characters as alphanumeric?
With the numeric definition, it will always have to be 05 or 50, and 
definitely not equal.

If you accept the number as a numeric field, it should work just fine.

If you accept the number as an alphanumeric string, then you will have 
to edit it, or the operator will have to enter "05". I expect that if 
you do answer "05" to the alphanumeric accept, then the test will work 
exactly like you expect.

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
