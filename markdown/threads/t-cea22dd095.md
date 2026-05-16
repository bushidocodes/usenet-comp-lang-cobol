[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Routine

_1 message · 1 participant · 1998-09_

---

### Re: Right Justify Routine

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F44C18.CA741D18@IMN.nl>`
- **References:** `<Jl0PnHJ5PvPd-pn2-XiTbHJiS5z0r@Dwight_Miller.iix.com> <35F1557A.54E0@bellsouth.net> <6sreg7$4v2$1@news02.btx.dtag.de>`

```
Andreas Strzoda wrote:

> Kitty Carr schrieb:
>
> > What does (counter:1) mean?  (I mean specifically the colon.)  And
> > function reverse?  I've done my homework!

8<

> Hello Kitty,
>
…[5 more quoted lines elided]…
> then DISPLAY STR(2:2) will show "AL" and DISPLAY (1:) will show "H"

No, no! A little differnt! Display str(1:) will show "HALLO". leaving
the
number of chars out means "all the rest". F.e. display str (3:) is the
same as display str (3:4) and both show "LLO".

> Function is new too, that are the INSTRINSIC-Functions,
> getting arguments and returning something:
…[3 more quoted lines elided]…
> for the functions supported by your compiler.

All functions were once new, being added to the '85 standard in 1989.
Some
shops still use COBOL '85 without this '89 extension. But functions are
yet more than 8 years long in existance.New is relative.

>
>
> regards
> AS

BW from
The Teaching Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
