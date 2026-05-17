[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HLLAPI And MF Cobol.

_2 messages · 2 participants · 1995-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### HLLAPI And MF Cobol.

- **From:** "mark walsham" <ua-author-15609224@usenetarchives.gap>
- **Date:** 1995-09-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<811453163snz@dudeman.demon.co.uk>`

```
Hi,

I've just come across a need to communicate with a 3270 Comms
program from a Cobol program. Has anyone used the HLLAPI
support in MF Cobol or knows how it works.

I have an idea that it is included in the Full Workbench but
not in Proco. I basically want to initiate a logon, then do
a file transfer to the VM/ESA host and then log off.

Does this sound feasible?

Hang Loose,

Mark.
------------------------------------------------------------
FROM:- Ma··.@dud··o.uk [London, United Kingdom, 95]

     In The Quiet Of The Night Let Our Candle Always Burn
     Let Us Never Lose The Lessons We Have Learned.
------------------------------------------------------------
```

#### ↳ Re: HLLAPI And MF Cobol.

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1995-09-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1cefa4819b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<811453163snz@dudeman.demon.co.uk>`
- **References:** `<811453163snz@dudeman.demon.co.uk>`

```
HLLAPI is available in almost all 3270 emulators, even from 5 years ago.

They all are slightly different, especially depending on your linkup to
the mainframe.

One just needs to coordinate the CALL and data formats between your 3270
emulator and the COBOL program. No additional M/F stuff should be
required.

You essentially link up the API portion of the emulator as subroutines to
the COBOL program, make the calls and have fun.

Usual biggest challange - avoiding loops beating on the 3270 enter key
when something unexpected happens.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
