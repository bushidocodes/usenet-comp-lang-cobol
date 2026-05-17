[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PIC-9 COMP format?

_3 messages · 3 participants · 1997-05_

---

### PIC-9 COMP format?

- **From:** "todd radel" <ua-author-467674@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<338C3D67.545A@voicenet.com>`

```

I'm not a COBOL programmer, but I once shook hands with one. :-)

I need to convert a download file from a mainframe into ASCII. I have a
COBOL copybook which gives me the record format. My only problem is with
the compressed PIC-9 fields; I don't know how to decode them. (I did it
successfully several years ago, but I can't find the code I wrote back
then.)

I have fields like: PIC 9(06) COMP.
PIC S9(07)V99 COMP.

Can someone give me a pointer?

Please email, as I don't normally read this newsgroup.

TIA,
Todd Radel
```

#### ↳ Re: PIC-9 COMP format?

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff7fba4c21-p2@usenetarchives.gap>`
- **In-Reply-To:** `<338C3D67.545A@voicenet.com>`
- **References:** `<338C3D67.545A@voicenet.com>`

```

Todd Radel (ra··.@voi··t.com) wrote:
: I'm not a COBOL programmer, but I once shook hands with one. :-)
: I need to convert a download file from a mainframe into ASCII. I have a
: COBOL copybook which gives me the record format. My only problem is with
: the compressed PIC-9 fields; I don't know how to decode them. (I did it
: successfully several years ago, but I can't find the code I wrote back
: then.)
: I have fields like: PIC 9(06) COMP.
: PIC S9(07)V99 COMP.
: Can someone give me a pointer?
(snip)
-------------------------

If you are referring to an IBM mainframe, then the COMP is plain old
binary data (COMP-3 is a different animal).

The size of the item depends on the number of digits (including decimals)
in the PIC.

If the nbr/digits is 1 thru 4, then the item is 2 bytes binary.
If the nbr/digits is 5 thru 9, then the item is 4 bytes binary.
If the nbr/digits is 10 thru 18, then the item is 8 bytes binary.

In your examples, PIC 9(06) results in 4 bytes binary, and PIC
S9(07)V99 also results in 4 bytes binary.
```

#### ↳ Re: PIC-9 COMP format?

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff7fba4c21-p3@usenetarchives.gap>`
- **In-Reply-To:** `<338C3D67.545A@voicenet.com>`
- **References:** `<338C3D67.545A@voicenet.com>`

```

Comp fields do not need to be converted... The are in binary format. DO
NOT EBCDIC TO ASCII convert them. They are fine. Comp-3 is another
story...
Todd Radel wrote in article <338··.@voi··t.com>...
› I'm not a COBOL programmer, but I once shook hands with one.  :-)
› 
…[15 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
