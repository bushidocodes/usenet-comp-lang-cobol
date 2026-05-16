[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL-9X Standard?

_2 messages · 2 participants · 1999-01_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL-9X Standard?

- **From:** cpcohen@inforamp.net (Charles P. Cohen)
- **Date:** 1999-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368e56c7.8979011@news.istar.ca>`

```
I'll be teaching two COBOL courses in the spring, and I've been
out-of-touch with the development of the language since the early
1990's.  

Can someone describe (or point to) the additions expected in the
COBOL-9X standard?

Or will it be the COBOL-20XX standard?

Thanks.
```

#### ↳ Re: COBOL-9X Standard?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76omku$sko@sjx-ixn3.ix.netcom.com>`
- **References:** `<368e56c7.8979011@news.istar.ca>`

```
COBOL 2000 (semi-officially) - more likely 2002 at the earliest (IMHO).
There are lots of "summary documents" available.

If you haven't been working with COBOL since the early 90's, certainly the
many flavors (already existing) of OO COBOL are the biggest changes.  Also,
(as extensions in various implementations - I assume you already know about
the Standard Intrinsic Functions)
   - Recursive programming
   - DBCS/MOCS or National Character handling
   - user defined functions
   - returned values (and CALL BY VALUE)
   - many other "tweaks" to allow calls to/from C, C++, and use of various
APIs
   - screen handling (character and/or GUI)
   - pointers (procedure and data)

   and lots more (what platform are you targeting and/or what compiler? -
this might help us give you a list of "what's new")

Charles P. Cohen wrote in message <368e56c7.8979011@news.istar.ca>...
>I'll be teaching two COBOL courses in the spring, and I've been
>out-of-touch with the development of the language since the early
…[7 more quoted lines elided]…
>Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
