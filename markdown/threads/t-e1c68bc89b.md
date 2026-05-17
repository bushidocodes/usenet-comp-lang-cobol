[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 85 print error codes

_3 messages · 3 participants · 1998-05_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL 85 print error codes

- **From:** "c.dewar" <ua-author-16820789@usenetarchives.gap>
- **Date:** 1998-05-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<354C2B1D.C50@virgin.net>`

```

Hi there,

I am new to COBOL programming, and I've brick walled trying to find out
how to check if a printer is on line. I suspect WS_STATUS is used, but
cannot find the error code to use with it. Please help if you can I'm
desperate.

Many thanks

Anne Dewar
```

#### ↳ Re: COBOL 85 print error codes

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1c68bc89b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<354C2B1D.C50@virgin.net>`
- **References:** `<354C2B1D.C50@virgin.net>`

```

Why not just open the file in output, with the printer turned offline,
and display the error code on the screen? After you have read
it, then you will know what it is. Why ask other people to look
for you?
```

#### ↳ Re: COBOL 85 print error codes

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-05-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1c68bc89b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<354C2B1D.C50@virgin.net>`
- **References:** `<354C2B1D.C50@virgin.net>`

```

In message <<354··.@vir··n.net>> "c.dewar" writes:
› 
› I am new to COBOL programming, and I've brick walled trying to find out
› how to check if a printer is on line.  I suspect WS_STATUS is used, but
› cannot find the error code to use with it. Please help if you can I'm
› desperate. 

Should we have to guess your environment ?

In many cases there is system software (spooler) that gets
between program and printer, even Windows Print Manager does
this, or the printer is not accessible because it is over
the network and on-line status cannot be determined.

To cover all possible situations would require large amounts
of code.

But what have you tried ? Write to the printer and check
the file status. Most likely to program will simply wait,
but I do get a 9/027 in my environment when printer is
in use by another user.

Some compilers have specific extensions to deal with
printers in some environments, such as MF's PC_WIN_PRINT...
functions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
