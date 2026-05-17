[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting COMP Fields

_5 messages · 5 participants · 1998-04_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Converting COMP Fields

- **From:** "jason rummel" <ua-author-17074878@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`

```

I have a PIC 99999 COMP 3 field in need to convert back out to a decimal
number that is sent to me. Any ideas/help?

Please e-mail a response.
```

#### ↳ Re: Converting COMP Fields

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4cd4527fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`
- **References:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`

```

In <352··.@bel··t.net>, Jason Rummel writes:
› I have a PIC 99999 COMP 3 field in need to convert back out to a decimal
› number that is sent to me. Any ideas/help?
›
› Please e-mail a response.
›

You post here then you read here.

05 packed-decimal-field pic 99999 comp-3.
05 display-field pic 99999.

move packed-decimal-field to display-field.
```

#### ↳ Re: Converting COMP Fields

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4cd4527fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`
- **References:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`

```

In article <352··.@bel··t.net>,
Jason Rummel wrote:
› I have a PIC 99999 COMP 3 field in need to convert back out to a decimal
› number that is sent to me. Any ideas/help?
 
› I am not sure what you mean... please post some code?
 
› 
› Please e-mail a response.

Ask the group, read the group.

DD
```

#### ↳ Re: Converting COMP Fields

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4cd4527fb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`
- **References:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`

```

Jason Rummel wrote:
›
› I have a PIC 99999 COMP 3 field in need to convert back out to a decimal
› number that is sent to me. Any ideas/help?
›
› Please e-mail a response.

Noticed the Bellsouth Labs organization. Are you trying to get this
into a C data type? There are numerous ways to do what you want, what
is your ultimate goal? Why not just use the MOVE statement?
```

#### ↳ Re: Converting COMP Fields

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4cd4527fb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`
- **References:** `<3523BD3C.7F578376@bellsouth.bridge.bst.net>`

```

All of a sudden, Jason Rummel
wrote:

› I have a PIC 99999 COMP 3 field in need to convert back out to a decimal
› number that is sent to me. Any ideas/help?
›
Look up the MOVE command...


Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
