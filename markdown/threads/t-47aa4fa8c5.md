[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WinAPI on NT 4.0 with MF

_2 messages · 2 participants · 1998-05 → 1998-06_

---

### WinAPI on NT 4.0 with MF

- **From:** "frank pohlmann" <ua-author-11050768@usenetarchives.gap>
- **Date:** 1998-05-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<356FFDB3.6ACB42D@baeurer.de>`

```

I want to make API-calls from Micro Focus Cobol 4.0.32 on WinNT 4.0
workstation.
I use the sample programm winhello.cbl. I take care of the right
call-convention and everything mentioned in the sample programm.
But when I run the programm, I get error 173 (called program not found)
on "call winapi "FindWindow" (and every other call, too).
The documentation says "just run the program". I think something is
missing. Perhaps a directory in PATH, COBLIB or COBDIR?
Is there anybody who can give me a hint?

Frank
____________________________________________________________________
Frank Pohlmann
BÃ¤urer Unternehmensberatung und  Software GmbH
Eckendorfer Str. 2 - 4
33609 Bielefeld
Tel.: 0521/96652-0       Fax: 0521/96652-99
E-Mail: Fra··.@bae··r.de
____________________________________________________________________
```

#### ↳ Re: WinAPI on NT 4.0 with MF

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-06-01T10:10:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-47aa4fa8c5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<356FFDB3.6ACB42D@baeurer.de>`
- **References:** `<356FFDB3.6ACB42D@baeurer.de>`

```

In article <356··.@bae··r.de>,
Fra··.@bae··r.de wrote:
› 
› I want to make API-calls from Micro Focus Cobol 4.0.32 on WinNT 4.0
…[20 more quoted lines elided]…
› 
You might verify that you are using the case directive and also check each
call to make sure that the case of the call and that the calling parms are
correct. If any of this is wrong you could get and error.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
