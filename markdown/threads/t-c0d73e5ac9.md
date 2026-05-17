[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol w/NT and HLLAPI

_2 messages · 2 participants · 1996-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol w/NT and HLLAPI

- **From:** "paul denno" <ua-author-3236725@usenetarchives.gap>
- **Date:** 1996-03-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3159C271.4FB1@ix.netcom.com>`

```
I am looking to convert an existing MicroFocus COBOL application to
Windows NT. Has anyone done this with an app that uses HLLAPI calls to a
3270 session? Did you use the language interface modules (coblim's) that
come with MF COBOL ? What 3270 emulator did you use ?
Any help would be greatly appreciated.
Thanks,
Paul
```

#### ↳ Re: MF Cobol w/NT and HLLAPI

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-03-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0d73e5ac9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3159C271.4FB1@ix.netcom.com>`
- **References:** `<3159C271.4FB1@ix.netcom.com>`

```
In article <315··.@ix.··m.com>, pde··.@ix.··m.com says...
›
› I am looking to convert an existing MicroFocus COBOL application to
› Windows NT. Has anyone done this with an app that uses HLLAPI calls to a
› 3270 session?

Hmm. I'm the developer working on MFXFER - The mainframe file transfer tool
so I suspect I 've done this before. ;-)

› Did you use the language interface modules (coblim's) that come with MF COBOL
› ?

..and I look after those too. They are used extensively throughout MFXFER. It
does not call HLLAPI functions directly.

› What 3270 emulator did you use ?

This is a very good question as true 32bit NT 3270 emulators are thin on the
ground at the moment. This is improving rapidly due largely to Windows 95.

The major problem is that the emulator companies are just now getting their
heads around 32bit. Attachmates Extra for NT product for instance doesn't
support 32bit HLLAPI correctly. The interface library is 16bit. This made it
impossible to create a LIM module for our 32bit NT product

I've been told by Attachmate that Personal Client V6 is fully 32bit and I
received a copy yesterday so that may be supported soon. As yet I haven't had
a chance to play with it.

If you're using our 16bit product still ie. v3.2, supported Windows 3270
emulators are much easier to find. You shouldn't have much of a problem with
those via the appropriate LIM's.

› Any help would be greatly appreciated.
› Thanks,
› Paul

Let me know how you get on with NT and 3270 emulators. If you need any
specific help, email me.

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
