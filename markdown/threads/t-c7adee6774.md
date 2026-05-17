[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Questions From a Beginner of COBOL

_4 messages · 4 participants · 1997-09 → 1997-10_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Questions From a Beginner of COBOL

- **From:** "calvin" <ua-author-104981@usenetarchives.gap>
- **Date:** 1997-09-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcc757$cb58ae00$0f02000a@calvin>`

```

Q1. The reserved words must be written in Capital Letters?
Q2. Variables for COBOL are case-sensitive?
Q3. If I am using RM-COBOL/85 complier, then I need following the ordinary
cobol format or not?
e.g. 7th column for indication, 8-11 is Region A, 12-72 is Region B?


From
Calvin
```

#### ↳ Re: Questions From a Beginner of COBOL

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1997-09-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7adee6774-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcc757$cb58ae00$0f02000a@calvin>`
- **References:** `<01bcc757$cb58ae00$0f02000a@calvin>`

```

Calvin wrote:
› 
› Q1. The reserved words must be written in Capital Letters?
 
› Not required in RM/COBOL-85.  RM/COBOL-85 is case-insensitive.
 
› Q2. Variables for COBOL are case-sensitive?
 
› Not in RM/COBOL-85.  RM/COBOL-85 is case-insensitive.
 
› Q3. If I am using RM-COBOL/85 complier, then I need following the
› ordinary
› cobol format or not?
›        e.g. 7th column for indication, 8-11 is Region A, 12-72 is
› Region B?

Yes.

For other COBOL implementations, check your language reference manual.
Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

#### ↳ Re: Questions From a Beginner of COBOL

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-09-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7adee6774-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bcc757$cb58ae00$0f02000a@calvin>`
- **References:** `<01bcc757$cb58ae00$0f02000a@calvin>`

```

Calvin wrote:
›
› Q1. The reserved words must be written in Capital Letters?

The use of capital letters depends on your platform, your compiler, and
what your instructor wants to see in order to get the best grade... can
you offer some specifics?

› Q2. Variables for COBOL are case-sensitive?
 
› Once again, depends on your platform and compiler... specifics?
 
› Q3. If I am using RM-COBOL/85 complier, then I need following the ordinary
› cobol format or not?
›        e.g. 7th column for indication, 8-11 is Region A, 12-72 is Region B?

Ahhhh, I will assume that you are using RM-COBOL/85... to the best of my
knowledge (my experience is in MicroFocus) nothing is case-sensitive but
you can perform a rather simple experiment along the lines of:

01 flda pic x value 'a'.
01 FLDA pic x value 'z'.
...
DISPLAY flda.
display FLDA.

and that should answer all questions about capitalization and
case-sensitivity.

DD
```

#### ↳ Re: Questions From a Beginner of COBOL

- **From:** "lawrence a.free" <ua-author-17072406@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7adee6774-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bcc757$cb58ae00$0f02000a@calvin>`
- **References:** `<01bcc757$cb58ae00$0f02000a@calvin>`

```

In article 01bcc757$cb58ae00$0f02000a@calvin,
"Calvin" said:
›
›
› Q1. The reserved words must be written in Capital Letters?

With COBOL/85, verbage does not need to be capitalized. Check your
manual for sure.

› Q2. Variables for COBOL are case-sensitive?
 
› Not sure, haven't tried it.
 
› Q3. If I am using RM-COBOL/85 complier, then I need following the
› ordinary
…[3 more quoted lines elided]…
› 

Here you are opening a potential can of worms. Most COBOL/85
compilers permit the free-form format, though generally require a
switch setting when you compile. In free-form, Column 1 is
indicator, 2-5 is Area A, 6 and beyond Area B, and no Area C.

The ANSI standard you mention above is still the standard notation.
The can of worms: portability. If you wish to maintain code
portability between platforms and dialects, you should stay within
the defined ANSI standard. Move beyond it and there is no guarantee
that what you write will work elsewhere.

›
› From
› Calvin


Lawrence A. Free
A.F.Software Services, Inc.
630-232-0790
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
