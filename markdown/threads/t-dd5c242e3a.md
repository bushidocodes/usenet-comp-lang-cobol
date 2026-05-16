[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hexadecimal literals

_3 messages · 3 participants · 2000-10_

---

### Hexadecimal literals

- **From:** Rosa Fischer <rosa.fischer@mch.sni.de>
- **Date:** 2000-10-20T07:11:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39EFD403.D01D7A0@mch.sni.de>`

```
Today I need some advice about hexadecimal literals. IBM and Merant
support hexadecimal literals and I need to know what are they used
for and what length is normally used - shorter than 30 bytes or longer
than 100? Does anybody use them in copy replacing or replace statements?
Thank you in advance

Sincerely
Rosa Fischer
```

#### ↳ Re: Hexadecimal literals

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-20T01:12:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sonin$tpr$1@slb3.atl.mindspring.net>`
- **References:** `<39EFD403.D01D7A0@mch.sni.de>`

```
There is no "general rule" that applies to all cases, but the MOST common
(usual) case for using hex literals is for "populating" (or comparing to) a
field that has characters in it that aren't in the "normal" print/screen
"displayable" set of characters (such as a X'00' which is used to interface
with those C programs that use "null-terminated strings")  Similarly X'0A'
is either a line feed or carriage control (I can never remember which) in
many systems.

The ONLY restriction on "length" is that the entire literal may not exceed
the "normal" length of an alphanumeric literal (when you divide by two).
Therefore X'00' counts as a "one-byte" alphanumeric literal.

In some systems it is QUITE common to see one and two byte hex-literals (to
fill in "attribute bytes" or similar not display characters) - but there are
also cases where you will see QUITE long ones (for example, you want to
"write" an EBCDIC string when running in an ASCII environment).

COPY/REPLACING is such "hornets" nest with  the "simplest" cases, that I
would not recommend adding hex-literals to the "stew".  However, they are
allowed where alphanumeric literals are allowed and if you want to make
source code maintenance a "challenge" - feel free to use them there <G>.

P.S.  Just noticing the ".de" in your email address, another semi-common
case for using them is when you want to use an "accented" or non-"basic
Latin" character in a report or screen - and the environment that you are
coding in/compiling in doesn't support that character.
```

##### ↳ ↳ Re: Hexadecimal literals

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DaXH5.17$ZX2.1444@iad-read.news.verio.net>`
- **References:** `<39EFD403.D01D7A0@mch.sni.de> <8sonin$tpr$1@slb3.atl.mindspring.net>`

```
In article <8sonin$tpr$1@slb3.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:

[snippage]

>Similarly X'0A'
>is either a line feed or carriage control (I can never remember which) in
>many systems.

I remember this as a kind of chant... CRLF 0D0A ('SEE-ar-EL-eff
ZERO-dee-ZERO-ay' (where 'ay' = long 'a' sound as in 'may' or 'hay'))

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
