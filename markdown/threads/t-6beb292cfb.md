[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobtest => Debug question

_3 messages · 2 participants · 1997-12_

---

### Cobtest => Debug question

- **From:** "bikr..." <ua-author-1169560@usenetarchives.gap>
- **Date:** 1997-12-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19971204201000.PAA18455@ladder01.news.aol.com>`

```

We recently converted to COBOL for MVS and one of our programmers ran into a
wall trying to figure out how to use AT OCCURRENCE in DEBUG instead of WHEN
name(condition) in Cobtest. No matter what we try, we can't get it to work.
I've looked for examples in the manuals, but all IBM says is:

There are no COBOL condition constants. Instead, an Language
Environment symbolic feedback code must be used, for example, CEE347.

(What the heck does that mean? When is IBM going to learn to write in
English?)

Can anyone help?

Karen
```

#### ↳ Re: Cobtest => Debug question

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-12-14T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6beb292cfb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19971204201000.PAA18455@ladder01.news.aol.com>`
- **References:** `<19971204201000.PAA18455@ladder01.news.aol.com>`

```

Post an example of what you are trying to debug. Tried private email to your
account, but shows you are refusing e-mail
Rex Widmer
Builder of software archeology tools and other strange programs to help survive
in a legacy based world.
```

#### ↳ Re: Cobtest => Debug question

- **From:** "bikr..." <ua-author-1169560@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6beb292cfb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19971204201000.PAA18455@ladder01.news.aol.com>`
- **References:** `<19971204201000.PAA18455@ladder01.news.aol.com>`

```

› We recently converted to COBOL for MVS and one of our > programmers ran into
› a wall trying to figure out how to use AT
› OCCURRENCE in DEBUG instead of WHEN name (condition) in > Cobtest. No matter
what we try, we can't get it to work.

Sample of DEBUG problem:

WORKING STORAGE SECTION.
:
:
04 EDITED-AWARD REDEFINES NEW-AWARD.
05 EA-AREA-1 PIC X.
05 EA-AREA-2.
10 FIELD1 PIC 9.
10 FIELD2 PIC 9.
:
:
10 FIELD8 PIC 999.

When the programmer tries to use the AT command to examine the contents of
FIELD8 whenever it changes, the message INVALID QUALIFIER IN A QUALIFIED
REFERENCE is displayed.

Additional unrelated problems:
- He is unable to set breakpoints using the 'AT * IF...'
- When he encounters a 'CEE3204S - THE SYSTEM DETECTED A
PROTECTION EXCEPTION. THE TRACEBACK INFORMATION
COULD NOT BE DETERMINED.' condition, it locks up his TSO
session in an online dump which can only be stopped by having the
computer operator cancel his session.

Thanks for any help you can provide.

Karen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
