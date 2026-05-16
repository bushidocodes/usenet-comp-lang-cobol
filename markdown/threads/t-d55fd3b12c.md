[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Stumper Question for me: simple question for this group -exponential and logs

_6 messages · 6 participants · 1999-05_

---

### Stumper Question for me: simple question for this group -exponential and logs

- **From:** Ryan Coffey <rcoffey@jps.net>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374BA772.603E72EB@jps.net>`

```

I was wondering if you could help me w/ the syntax of a COBOL program
that would do exp. like below.  My goal would be to have it read a value

for variable x and b and give me U.  I took Fortran 77 a couple years
ago and today my dad asked me if I knew cobol.  I said I would try.  I
managed to screw around on the school's Unix accont, but I can't get it
to work.  I was wondering if you could help me out.

Ryan



  b^u=x

or Log termination U=log to the base b (x)

I want to know if I know x and b, how to I find U.
```

#### ↳ Re: Stumper Question for me: simple question for this group -exponential and logs

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374be2f2@news3.us.ibm.net>`
- **References:** `<374BA772.603E72EB@jps.net>`

```
MATHPK in ETKPAK at http://etk.com/downloads
give you logarithms in Cobol.

Ryan Coffey <rcoffey@jps.net> wrote in message
news:374BA772.603E72EB@jps.net...
>
> I was wondering if you could help me w/ the syntax of a COBOL program
…[16 more quoted lines elided]…
>
```

#### ↳ Re: Stumper Question for me: simple question for this group -exponential and logs

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374be752.642625936@news1.ibm.net>`
- **References:** `<374BA772.603E72EB@jps.net>`

```
On Wed, 26 May 1999 00:49:06 -0700, Ryan Coffey <rcoffey@jps.net>
wrote:


>
>
…[5 more quoted lines elided]…
>I want to know if I know x and b, how to I find U.

For Log, try "Function Log" or "Function Log10" to find the natural
log of a number.
```

##### ↳ ↳ Re: Stumper Question for me: simple question for this group -expo nential and logs

- **From:** Tom O' Toole <Tom.Otoole@policymaster.co.uk>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BA5679A31104D311A55D0000E218F7420C5974@MAROON>`
- **References:** `<374BA772.603E72EB@jps.net> <374be752.642625936@news1.ibm.net>`

```
>>
>>
…[5 more quoted lines elided]…
>>I want to know if I know x and b, how to I find U.

>For Log, try "Function Log" or "Function Log10" to find the natural
>log of a number.

And then use log (x) / log (b) to find U.  Or log10 (x) / log10 (b).
Just be consistent.
```

#### ↳ Re: Stumper Question for me: simple question for this group -exponential and logs

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72T23.1824$v%.372@news3.mia>`
- **References:** `<374BA772.603E72EB@jps.net>`

```
Ryan Coffey wrote:
>
>  b^u=x
>
>I want to know if I know x and b, how to I find U.

  b^u = x
  ln(b^u) = ln(x)
  u*ln(b) = ln(x)
  u = ln(b)/ln(x)

           COMPUTE U = FUNCTION LOG(B) / FUNCTION LOG(X).

Make sure both B and X > 0 and X <> 1!
```

#### ↳ Re: Stumper Question for me: simple question for this group -exponential and logs

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lL433.4321$v%.746@news3.mia>`
- **References:** `<374BA772.603E72EB@jps.net>`

```
Try :  answer-wanted = base**exponent.

Ryan Coffey wrote in message <374BA772.603E72EB@jps.net>...
>
>I was wondering if you could help me w/ the syntax of a COBOL program
…[16 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
