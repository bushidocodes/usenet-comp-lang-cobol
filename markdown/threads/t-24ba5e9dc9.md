[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Numeric format problem

_5 messages · 5 participants · 1998-01_

---

### Numeric format problem

- **From:** "asdf" <ua-author-14688682@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a3em7$fe6$1@mark.ucdavis.edu>`

```


I have a data file from a remote mainframe with numbers in an unknown format.
Suspect it was COBOL-generated. Have been able to decode some specific values
by cross-referencing with another file that has numbers in ASCII, but only
some of the numeric fields can be dealt with that way.

It is plain from the numbers I can see that the rightmost byte carries
only one digit (the least significant). I expected something in that byte for
the sign (I did COBOL about 15 years ago), but can't figure what the pattern
is. This is how that least-significant byte is encoded:

value - hex - binary
0 - 0C - 00001100
1 - 1C - 00011100
2 - 1A - 00011010
3 - 14 - 00010100
4 - 3C - 00111100
5 - 2A - 00101010
6 - 25 - 00100101
7 - 40 - 01000000
8 - F3 - 11110011
9 - CE - 11001110

So for example, if in the right byte there is a hex '25', I know that the
least significant digit is 6.

The other bytes are also a mystery to me - more so than the least significant
- but maybe this is enough of a clue that someone will recognize it?

Just for further obfuscation, here's a sample of decoded two-byte numbers:

value - hex - binary
150 - 0A 0C - 00001010 00001100
103 - 10 14 - 00010000 00010100
203 - 1A 14 - 00011010 00010100
403 - 20 14 - 00100000 00010100

Anyone have any clues as to what this is?
Thanks,

Dan Quickert
dequickert at ucdavis dot edu
```

#### ↳ Re: Numeric format problem

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24ba5e9dc9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6a3em7$fe6$1@mark.ucdavis.edu>`
- **References:** `<6a3em7$fe6$1@mark.ucdavis.edu>`

```

In article <6a3em7$fe6$1.··.@mar··s.edu>,
as··f@as··f.asd (asdf) wrote:
› 
› I have a data file from a remote mainframe with numbers in an unknown
› format.  Suspect it was COBOL-generated.  Have been able to decode some
› specific values by cross-referencing with another file that has numbers
› in ASCII, but only some of the numeric fields can be dealt with that way.

If you have an EBCDIC file from a mainframe and translate it to ASCII,
all of the character fields will be translated in a sensible way.
However, binary fields and packed-decimal fields are not character
fields.

For example, +403 in packed-decimal is X'403C'. If you do not know this
is packed decimal and translate it as character, the first byte will be
treated as an EBCDIC SP, X'40', and translated into an ASCII SP, X'20'.
The second byte will be treated as an EBCDIC DC4, X'3C', and translated
into an ASCII DC4, X'14'. The result is ASCII X'2014', which bears no
obvious relation to EBCDIC X'403C'.

Working backward from ASCII X'6B40', treat the first byte as an ASCII
"k", X'6B', and translate it into an EBCDIC "k", X'92'. Treat the second
byte as an ASCII "@", X'40' and translate it into an EBCDIC "@", X'7C'
The result is EBCDIC X'927C', or +927.

Unfortunately, there are several pitfalls. EBCDIC has twice as many
characters as ASCII, and there is no universal standard translation
table. You would have to have the exact table used, because there are
discrepancies between manufacturers, especially in the first quadrant.
For example, the DEC table I consulted differs from your posted data in
several places. Worst of all, not every manufacturer has taken the
trouble to insure that his translation is reversible!

For these reasons, unless you have a mainframe file that is all character
or can rely on a known reversible table that will not change, you are
better off reading mainframe data in EBCDIC and translating it within the
program, where you know which fields are character and which fields are
not.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: Numeric format problem

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24ba5e9dc9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6a3em7$fe6$1@mark.ucdavis.edu>`
- **References:** `<6a3em7$fe6$1@mark.ucdavis.edu>`

```

All of a sudden, as··f@as··f.asd (asdf) wrote:

› 
› I have a data file from a remote mainframe with numbers in an unknown format. 
…[39 more quoted lines elided]…
› dequickert at ucdavis dot edu

Got me. Doesn't look like any numeric format I've ever encountered in
COBOL or Assembler. I do find it interesting to note that the '0A 0C'
above is the ASCII carriage return, line feed (or vice versa), and the
'20' is an ASCII space. Is it possible that you're looking at ASCII
data here?
Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

##### ↳ ↳ Re: Numeric format problem

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24ba5e9dc9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24ba5e9dc9-p3@usenetarchives.gap>`
- **References:** `<6a3em7$fe6$1@mark.ucdavis.edu> <gap-24ba5e9dc9-p3@usenetarchives.gap>`

```

I don't recognize it either. Does anyone know the binary encoding scheme
for floating point (IBM MVS COMP-1 and COMP-2)? I don't think that this is
what you are seeing, but I also wouldn't recognize floating point in hex -
if it came up and bit me.

Renegade wrote in message <34c··.@new··x.com>...
› All of a sudden, as··f@as··f.asd (asdf) wrote:
› 
…[57 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Numeric format problem

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-24ba5e9dc9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-24ba5e9dc9-p3@usenetarchives.gap>`
- **References:** `<6a3em7$fe6$1@mark.ucdavis.edu> <gap-24ba5e9dc9-p3@usenetarchives.gap>`

```

Renegade wrote:
› 
› All of a sudden, as··f@as··f.asd (asdf) wrote:
…[20 more quoted lines elided]…
› 
Hmmm, x'0a0c'? On an IBM mainframe the x'0a' is a supervisor call (SVC)
instruction, e.g., in MVS SVC 10 is a GETMAIN & SVC 6 is either a LINK
or a LOAD, etc. This bit would be an "SVC 12". 'Don't know which flavour
of SVC this might be in either MVS or VSE.

Bill Lynch

› You may e-mail replies to: renegade at (@) dwx dot (.) com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
