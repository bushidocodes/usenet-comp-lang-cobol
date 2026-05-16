[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMREG & COBOL 74

_2 messages · 2 participants · 1999-08_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### RE: COMREG & COBOL 74

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90491CB93918D21189BD00805FBE300B014E30F6@voyager.okc.disa.mil>`

```
What is *fatal*?  I just can't remember which COBOL's allow which verbs, but
I didn't think that address setting was allowed in '74....

Which means that you would need corresponding full word registers in
linkage...

Which would mean that you should be able to move a zero to the appropriate
full word...

-----Original Message-----

snip

but the following statements/instructions are fatal in '74:

    03    POINT-COMREG        USAGE POINTER.

    SET ADDRESS OF PAGE-ZERO TO NULL

    SET ADDRESS OF COMREG TO POINT-COMREG

Is it possible to access COMREG in COBOL 74?  How?

snip


 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

#### ↳ Re: COMREG & COBOL 74

- **From:** "Tim Mueller" <tmiller16@yahoo.com>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37af0bca@news2.one.net>`
- **References:** `<90491CB93918D21189BD00805FBE300B014E30F6@voyager.okc.disa.mil>`

```

Thompson, William <wthompson@okc.disa.mil> wrote in message
news:90491CB93918D21189BD00805FBE300B014E30F6@voyager.okc.disa.mil...
> What is *fatal*?  I just can't remember which COBOL's allow which verbs,
but
> I didn't think that address setting was allowed in '74....

Exactly.  The SET verb is supported in '74, but not the ADDRESS OF option,
which gives the addressability.  I know now (thanks, everyone) that the only
way to access the COMREG in '74 is with an Assembler subroutine.

By 'fatal', I just meant that it would not compile.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
