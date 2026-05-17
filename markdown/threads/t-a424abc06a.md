[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Qs: representation of sign in zoned decimal

_3 messages · 3 participants · 1996-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Qs: representation of sign in zoned decimal

- **From:** "sam kendall" <ua-author-13876197@usenetarchives.gap>
- **Date:** 1996-12-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32B0547B.742B@cybercom.net>`

```

My VS COBOL II manual shows the representation of non-separate sign in
zoned decimal as follows: the upper nybble (4 bits) value hex C means +,
and hex D means -. (Or maybe the other way around; I don't have the
manual handy at the moment.) Yet I've been given a table showing that
*any* upper nibble value is legal to indicate a sign in zoned decimal.

So my questions are: is it true that any upper nybble value is legal to
indicate a sign in zoned decimal data (e.g., PIC S99 DISPLAY)?
If so, do COBOL implementations ever write values other than hex C and
D?
How common are values other than hex C and D?
What generates those other values if COBOL implementations don't?
What about unsigned zoned decimal (e.g., PIC 99 DISPLAY) -- are upper
nybble values simply ignored when COBOL reads such data, or what?
```

#### ↳ Re: Qs: representation of sign in zoned decimal

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1996-12-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a424abc06a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32B0547B.742B@cybercom.net>`
- **References:** `<32B0547B.742B@cybercom.net>`

```

Sam Kendall wrote:
› 
› My VS COBOL II manual shows the representation of non-separate sign in
…[16 more quoted lines elided]…
› Kendall Consulting

Ken,

Here is what I know about VS Cobol II, hope it helps....

there is a compiler option called NUMPROC(PFD) that will cause the
compiler to assume that the signs in your program are one of the
"prefered" signs:

signed positive or 0 - X'C'
signed negative - X'D'
unsigned or alphas - X'F'

If you use NUMPROC(NOPFD), there are six valid signs:

Positive - X'C', X'A', X'E', and X'F'
Negative - X'D' and X'B'

>From what I gather, the compiler uses whatever sign it is given to
process data even if the sign is incompatible with the data definition.
The prefered sign is generated only where necessary (such as moving a
signed element to an unsigned or alpha element per IBM). Object code
size will increase with NUMPROC(NOPFD). NUMPROC(PFD) is a performance
option that can be used to bypass invalid sign processing (you have to
be sure your data conforms to the above. IBM also recommends using
initialize instead of group moves to clear out data items). These are
the only valid signs I know of, if someone knows of more, please let Ken
and I know!!!

Steve
***************************************************************************
          "Thought by many to be endangered, the lesser spotted
                     COBOL programmer makes a comeback". 

email: prg··.@ep··x.net
url  : http://www.epix.net/~prgsdw
***************************************************************************
```

#### ↳ Re: Qs: representation of sign in zoned decimal

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1996-12-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a424abc06a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32B0547B.742B@cybercom.net>`
- **References:** `<32B0547B.742B@cybercom.net>`

```

Sam Kendall wrote:
› 
› My VS COBOL II manual shows the representation of non-separate sign in
…[16 more quoted lines elided]…
› Kendall Consulting

According to Harvey Bookman's "COBOL II", when you install your VS COBOL II
compiler you can choose between the NUMCLS(PRIM) or NUMCLS(ALT) options. If
you install your compiler with the NUMCLS(ALT) option, then COBOL will
interpret nybbles of A, B, and E as valid signs0 in addition to the normal C
(positive), D (negative), and F (unsigned). You can only change this
behavior when you install the compiler.

I am not sure how A, B, and E map to positive, negative, and unsigned. You
might want to run some tests to see what happens with your installation.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
