[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Quick ? about Fujitsu COBOL 85...

_3 messages · 3 participants · 1999-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Quick ? about Fujitsu COBOL 85...

- **From:** "Tom Montana" <tommontana@REMOVEME.earthlink.net>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79t5ch$g9o$1@birch.prod.itd.earthlink.net>`

```
Hey all...

I have a little problem...

I've been using version 3 of the Fujitsu COBOL 85 compiler and I can't seem
to convert display numeric values (-ZZZ,ZZZ.ZZ) to editable numeric values
(S999999V99). I've tried using different types of accepts...

ACCEPT ENTRY-FIELD WITH CONVERSION.
ACCEPT ENTRY-FIELD CONVERT.
ACCEPT ENTRY-FIELD.

Nothing seems to work. Meanwhile, I'll start reading the Fujitsu COBOL 85
standard book. I was just hoping someone out in the audience had the answer
off the top of their heads.

Thanks..

Tom.
```

#### ↳ Re: Quick ? about Fujitsu COBOL 85...

- **From:** "John Hicks (Remove \\"nospam\\" from address before replying)" <johnhicks@ibm.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CA508F.44042E4@ibm.net>`
- **References:** `<79t5ch$g9o$1@birch.prod.itd.earthlink.net>`

```
Tom--

I'm not familiar with Fujitsu and with the "with conversion" or
"convert" options, but if you're in a hurry, you can always do it the
old fashioned way: accept into an alphanumeric display field and then
parse the field, character by character, checking for signs, decimal
point, and digits, accumulating the result in a numeric field (which you
multiply by ten before adding each digit).

--John

Tom Montana wrote:
> 
> Hey all...
…[17 more quoted lines elided]…
> Tom.
```

##### ↳ ↳ Re: Quick ? about Fujitsu COBOL 85...

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7afmm5$c4c$1@news1.epix.net>`
- **References:** `<79t5ch$g9o$1@birch.prod.itd.earthlink.net> <36CA508F.44042E4@ibm.net>`

```
01 accept-in      pic s9(7)v99.
01 accept-out   pic zzz,zz9.99-.

accept accept-in.
move accept-in to accept-out.
display accept-out.

Display the output in the same position as the input,
and the user will not know the conversion was done.
Make sure the accept-out uses at least as many character
positions as the accept-in, or it may not over-write all the
original input.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
