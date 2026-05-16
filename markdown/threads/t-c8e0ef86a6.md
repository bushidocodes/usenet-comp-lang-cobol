[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT - See you Saturday

_5 messages · 4 participants · 2003-05_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT - See you Saturday

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-21T05:38:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ECB5743.9000209@Knology.net>`

```
I'll be back here Saturday - so, if you wonder why I haven't responded, 
that's why...  The government is sending me to the land of the hanging 
chads...  :)
```

#### ↳ Re: OT - See you Saturday

- **From:** docdwarf@panix.com
- **Date:** 2003-05-21T10:51:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bag3oq$p3q$1@panix1.panix.com>`
- **References:** `<3ECB5743.9000209@Knology.net>`

```
In article <3ECB5743.9000209@Knology.net>,
LX-i  <DanielJSNOSPAM@Knology.net> wrote:
>I'll be back here Saturday - so, if you wonder why I haven't responded, 
>that's why...  The government is sending me to the land of the hanging 
>chads...  :)

The Nation's Low-Sodium Section?  Take care, stay well and go in good 
health, old boy.

DD
```

##### ↳ ↳ Re: OT - See you Saturday

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-24T21:09:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED025D3.1010504@Knology.net>`
- **References:** `<3ECB5743.9000209@Knology.net> <bag3oq$p3q$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3ECB5743.9000209@Knology.net>,
> LX-i  <DanielJSNOSPAM@Knology.net> wrote:
…[7 more quoted lines elided]…
> health, old boy.

Thanks - I did...  :)  Which was nice, because the last trip we had to 
the good ol' F-L-of-A was not good, and we -all- were not in good health.

And, to beat all, not only did I have fun after work on the beach, I 
actually fixed everything that needed fixing...  Your tax money was 
well-spent on that TDY.  (Although, as King, you probably don't actually 
pay taxes...)

Now, can I go on a rant about how, using 36-bit words, Pic 9(02) Binary 
and Pic 1(09) will both hold the value 102, but not in the Value clause? 
  (No, that wasn't one of the problems, but it was a bonus find...)  :) 
  And, by the same token, Pic 9(05) Binary and Pic 1(18) both describe 
the same size (half-word), but only one of these definitions will take 
the number 100001 nicely...
```

###### ↳ ↳ ↳ Re: OT - See you Saturday

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-27T07:54:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bavu7r$vqs$1@si05.rsvl.unisys.com>`
- **References:** `<3ECB5743.9000209@Knology.net> <bag3oq$p3q$1@panix1.panix.com> <3ED025D3.1010504@Knology.net>`

```

"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
news:3ED025D3.1010504@Knology.net...

>   And, by the same token, Pic 9(05) Binary and Pic 1(18) both describe
> the same size (half-word), but only one of these definitions will take
> the number 100001 nicely...

That's not a surprise, presuming a COBOL compiler compliant with ANSI
X3.23-1985 or later.  USAGE BINARY is a standards-specified USAGE, and the
implementation is obligated to provide code to apply the odometer effect.

That's one of the areas the MCP/AS world had to deal with in migration from
COBOL74 to COBOL85, as that system's '74 implementation had USAGE BINARY as
a Unisys extension (and a very commonly used one, at that), and the odometer
effect *didn't* apply there (well, unless the item so declared was an
elementary 01-level item, as distinct from a 77-level item or an item within
a record), whereas it is required to apply unconditionally in '85.

We added the Unisys extension syntax USAGE BINARY EXTENDED and USAGE BINARY
TRUNCATED to both compilers to allow programmers the ability to specify
exactly what they wanted in a manner that would be applicable to either
dialect.

    -Chuck Stevens
```

#### ↳ Re: OT - See you Saturday

- **From:** "Johan den Boer" <me@knoware.nl>
- **Date:** 2003-05-21T20:11:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vcngaa74cocfe9@corp.supernews.com>`
- **References:** `<3ECB5743.9000209@Knology.net>`

```
Hi

Hope you hang high


"LX-i" <DanielJSNOSPAM@Knology.net> schreef in bericht
news:3ECB5743.9000209@Knology.net...
> I'll be back here Saturday - so, if you wonder why I haven't responded,
> that's why...  The government is sending me to the land of the hanging
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
