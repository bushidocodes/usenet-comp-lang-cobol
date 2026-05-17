[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL layout based data editor?

_4 messages · 4 participants · 1998-05_

---

### COBOL layout based data editor?

- **From:** "michael holzer" <ua-author-14608156@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<355FECE3.7F1A@hp.com>`

```

Hi,

I'm looking for a layout based data editor that
can also handle redefinitions (unlike Fujitsu DataEdit).

Please email answers directly.

Regards

Michael Holzer

-------------------

example:

01 record.

05 rec-id pic x(6).
05 rec-data pic x(100).

01 data-layout-1.
* rec-id ='000001'
05 rec-id pic x(6).
05 data-1 pic x(20).
05 filler pic x(80).
01 data-layout-2.
* rec-id ='000002'
05 rec-id pic x(6).
05 data-2 pic s9(9) binary.
05 filler pic x(86).
```

#### ↳ Re: COBOL layout based data editor?

- **From:** "robert moriarty" <ua-author-17074153@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66daadc3ae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<355FECE3.7F1A@hp.com>`
- **References:** `<355FECE3.7F1A@hp.com>`

```

I used to use a product called DATA EXPERT under TSO that can handle
multiple record layouts from COBOL definitions for file browsing and
editing

Michael Holzer wrote:
Hi,

I'm looking for a layout based data editor that
can also handle redefinitions (unlike Fujitsu DataEdit).

Please email answers directly.

Regards

Michael Holzer

-------------------

example:

01 record.

05 rec-id pic x(6).
05 rec-data pic x(100).

01 data-layout-1.
* rec-id ='000001'
05 rec-id pic x(6).
05 data-1 pic x(20).
05 filler pic x(80).
01 data-layout-2.
* rec-id ='000002'
05 rec-id pic x(6).
05 data-2 pic s9(9) binary.
05 filler pic x(86).
```

##### ↳ ↳ Re: COBOL layout based data editor?

- **From:** "art perry" <ua-author-6589755@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66daadc3ae-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-66daadc3ae-p2@usenetarchives.gap>`
- **References:** `<355FECE3.7F1A@hp.com> <gap-66daadc3ae-p2@usenetarchives.gap>`

```

Robert Moriarty wrote in message <356··.@m··.com>...
› I used to use a product called DATA EXPERT under TSO that can handle
› multiple record layouts from COBOL definitions for file browsing and
› editing


I know you can edit data using FileAid, but I don't know how it handles
redefinitions.

-Art
```

###### ↳ ↳ ↳ Re: COBOL layout based data editor?

- **From:** "bobh" <ua-author-514237@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-66daadc3ae-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-66daadc3ae-p3@usenetarchives.gap>`
- **References:** `<355FECE3.7F1A@hp.com> <gap-66daadc3ae-p2@usenetarchives.gap> <gap-66daadc3ae-p3@usenetarchives.gap>`

```

Art Perry wrote:
› 
› Robert Moriarty wrote in message <356··.@m··.com>...
…[7 more quoted lines elided]…
› -Art
You can tell FileAid what field to use as the 'record type' and
what value equates for which format. As you Browse the data it
will 'test' and use the appropriate record format .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
