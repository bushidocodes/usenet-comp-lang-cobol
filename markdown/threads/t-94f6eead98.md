[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Difference between REM and MOD

_7 messages · 3 participants · 1999-02_

---

### Re: Difference between REM and MOD

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqGu2.3627$Xl5.4985628@news1.mia>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com>`

```
jasonc@collegeestrie.com wrote:
>Would someone please explain to me the difference between MOD and REM.

MOD(argument-1, argument-2) returns the integer value defined by the
modulo arithmetic function (argument-1 modulo argument-2).  For positive
arguments, it is equivalent to REM (remainder).  But unless you are math-
aware, you may not get the result for negative arguments that you expect.
The ANSI Intrinsic Functions documentation gives this table:

  FUNCTION MOD(argument-1, argument-2)

  Argument-1    Argument-2    Return
     11             5            1
    -11             5            4
     11            -5           -4
    -11            -5           -1

REM(argument-1, argument-2) returns the integer value which is the
remainder after dividing argument-1 (dividend) by argument-2 (divisor).
The arguments in the above table would give the following results when
used with FUNCTION REM:

  FUNCTION REM(argument-1, argument-2)

  Argument-1    Argument-2    Return
     11             5            1
    -11             5           -1
     11            -5            1
    -11            -5           -1

Since FUNCTION REM returns the 'remainder' after integer division,
FUNCTION REM has the sign of the dividend (argument-1).
```

#### ↳ Re: Difference between REM and MOD

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36BB3934.A92F14E7@NOSPAMhome.com>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia>`

```
What types of COBOL (business) needs might I want to use MOD instead of
REM?
```

##### ↳ ↳ Re: Difference between REM and MOD

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u8Iu2.3721$Xl5.5045069@news1.mia>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia> <36BB3934.A92F14E7@NOSPAMhome.com>`

```
Howard Brazee wrote:
>What types of COBOL (business) needs might I want to use MOD instead of
>REM?

Possibly some statistics calculations, but that's about all I can think
of, off the top of my head.
```

##### ↳ ↳ Re: Difference between REM and MOD

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36be134a.8756802@netnews>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia> <36BB3934.A92F14E7@NOSPAMhome.com>`

```
'Twas Fri, 05 Feb 1999 11:32:20 -0700, when Howard Brazee
<brazee@NOSPAMhome.com> illuminated comp.lang.cobol thusly:

>What types of COBOL (business) needs might I want to use MOD instead of
>REM?

Most uses of MOD and REM are with positive arguments, and in such uses the
functions are identical.  Because of my math background I prefer MOD.
```

###### ↳ ↳ ↳ Re: Difference between REM and MOD

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36BEF8B0.6B0200C1@NOSPAMhome.com>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia> <36BB3934.A92F14E7@NOSPAMhome.com> <36be134a.8756802@netnews>`

```
Randall Bart wrote:
> 
> 'Twas Fri, 05 Feb 1999 11:32:20 -0700, when Howard Brazee
…[6 more quoted lines elided]…
> functions are identical.  Because of my math background I prefer MOD.

Where they are identical, I still prefer using the function which has
the correct INTENT.  If I extend my logic to where they are not
identical, I want to be using the correct word with the correct mindset.
```

###### ↳ ↳ ↳ Re: Difference between REM and MOD

_(reply depth: 4)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36bf6ade.42835568@netnews>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia> <36BB3934.A92F14E7@NOSPAMhome.com> <36be134a.8756802@netnews> <36BEF8B0.6B0200C1@NOSPAMhome.com>`

```
'Twas Mon, 08 Feb 1999 07:46:08 -0700, when Howard Brazee
<brazee@NOSPAMhome.com> illuminated comp.lang.cobol thusly:

>Randall Bart wrote:

>> Most uses of MOD and REM are with positive arguments, and in such uses the
>> functions are identical.  Because of my math background I prefer MOD.
…[3 more quoted lines elided]…
>identical, I want to be using the correct word with the correct mindset.

Okay.  If you are splitting seconds into hours, minutes, and seconds, or
splitting inches into feet and inches, the correct intent is found in the
function REM.  If you are doing a check digit or encryption calculation
the correct intent is found in the function MOD.
```

###### ↳ ↳ ↳ Re: Difference between REM and MOD

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C0421F.D0C32AD@NOSPAMhome.com>`
- **References:** `<79f0pn$rl4$1@nnrp1.dejanews.com> <hqGu2.3627$Xl5.4985628@news1.mia> <36BB3934.A92F14E7@NOSPAMhome.com> <36be134a.8756802@netnews> <36BEF8B0.6B0200C1@NOSPAMhome.com> <36bf6ade.42835568@netnews>`

```
> >> Most uses of MOD and REM are with positive arguments, and in such uses the
> >> functions are identical.  Because of my math background I prefer MOD.
…[8 more quoted lines elided]…
> the correct intent is found in the function MOD.

Thank-you.  I shall remember that.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
