[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT DATA FROM STD IN

_3 messages · 3 participants · 1996-07 → 1996-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### ACCEPT DATA FROM STD IN

- **From:** "alessandro battaglia" <ua-author-17086138@usenetarchives.gap>
- **Date:** 1996-07-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4tcgpm$ohg@serra.unipi.it>`

```

I'm an old Cobol programmer and i would like to write httpd cgi with it.
Well i don't remeber if is possible to accept data from shell. I have
written cobol program and i've used it in "cgi mode". It work very fine.
It assune httpd how std out.
Please help me with any advice, many thanks in advance.
Post your replies to this e-mail address also: ja··.@inp··i.it

Alessandro Battaglia
```

#### ↳ Re: ACCEPT DATA FROM STD IN

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1996-07-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b217a6dbb4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4tcgpm$ohg@serra.unipi.it>`
- **References:** `<4tcgpm$ohg@serra.unipi.it>`

```

Alessandro Battaglia wrote:
› 
› I'm an old Cobol programmer and i would like to write httpd cgi with it.
…[6 more quoted lines elided]…
›        Alessandro Battaglia

There is no ANSI standard way of doing it, but if your compiler supports
the X/Open COBOL spec then you can use the X/Open Mnemonic names
ARGUMENT-NUMBER and ARGUMENT-VALUE with Accept/Display to get command
line arguments and ENVIRONMENT-NAME and ENVIRONMENT-VALUE for getting
environment variables. If you have a Micro Focus compiler, you can
also read the command line using the special filename :CI:. Here's a
fragment I found:


Parse-stdio section.
move ":CI:" to input-file-name
open input input-file
read input-file
* Get the length of the data stream
display "CONTENT_LENGTH" upon environment-name
accept inputLenX from Environment-value
if inputlenX not numeric
move 128 to inputlen9
...



Martyn      (m.··.@mfl··o.uk)
Phone: +44 (0)1635 565 358, fax +44 (0)1635 565 567
```

#### ↳ Re: ACCEPT DATA FROM STD IN

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-08-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b217a6dbb4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4tcgpm$ohg@serra.unipi.it>`
- **References:** `<4tcgpm$ohg@serra.unipi.it>`

```

Alessandro Battaglia wrote:
: . . . i don't remeber if is possible to accept data from shell.

Command line arguments are also useful for passing query data:
01 ARGUMENT-STRING PIC X(120). ... for example;

ACCEPT ARGUMENT-STRING FROM COMMAND-LINE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
