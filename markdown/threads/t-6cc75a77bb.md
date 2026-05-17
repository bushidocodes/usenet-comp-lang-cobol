[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Day/month/Year

_4 messages · 4 participants · 1998-01_

---

### Day/month/Year

- **From:** "janne vihervuori" <ua-author-17074257@usenetarchives.gap>
- **Date:** 1998-01-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34B22B7E.FF447BC6@myy.helia.fi>`

```

Would someone please help me with this one:

How can I get the current Date from the OS to
my Cobol-program?


Thanks,

Janne
```

#### ↳ Re: Day/month/Year

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc75a77bb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34B22B7E.FF447BC6@myy.helia.fi>`
- **References:** `<34B22B7E.FF447BC6@myy.helia.fi>`

```

In article <34B··.@myy··a.fi>, Janne Vihervuori
writes:

› How can I get the current Date from the OS to
› my Cobol-program?

This sounds suspiciously like a homework assignment.

Check your COBOL manuals for:

MOVE CURRENT-DATE TO 8-char-field.

ACCEPT field FROM DATE.

MOVE FUNCTION CURRENT-DATE TO 23-char-field.

(That might be 23 or 27; my references are at work. Not all compilers have
intrinsic functions so FUNCTION CURRENT-DATE might not be available in your
compiler. I know it is there in COBOL for MVS and VM, and in COBOL for VSE.)

If this is a CICS program, you shouldn't do any of the above, but instead
either use EIBDATE or use EXEC CICS ASKTIME followed by EXEC CICS FORMATTIME.
(FORMATTIME can format both the date and time in the same EXEC CICS.)
```

##### ↳ ↳ Re: Day/month/Year

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc75a77bb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6cc75a77bb-p2@usenetarchives.gap>`
- **References:** `<34B22B7E.FF447BC6@myy.helia.fi> <gap-6cc75a77bb-p2@usenetarchives.gap>`

```

› This sounds suspiciously like a homework assignment.
› 
…[7 more quoted lines elided]…
› 

If I just want the current date I generally say:
MOVE FUNCTION CURRENT-DATE (1:8) TO 8-char-field.

Note of course that CURRENT-DATE and FUNCTION CURRENT-DATE
are not the same format at all.
```

#### ↳ Re: Day/month/Year

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc75a77bb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34B22B7E.FF447BC6@myy.helia.fi>`
- **References:** `<34B22B7E.FF447BC6@myy.helia.fi>`

```

Boy is this one a "who is doing your homework question"!

The answer (in a semi-hint form) is to look at
A) the ACCEPT verb
B) the CURRENT-DATE intrinsic function

Janne Vihervuori wrote in message <34B··.@myy··a.fi>...
› Would someone please help me with this one:
› 
…[7 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
