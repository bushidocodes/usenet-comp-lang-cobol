[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trapping esc, function and tab keys

_2 messages · 2 participants · 1997-03_

---

### Trapping esc, function and tab keys

- **From:** "cobal" <ua-author-12404358@usenetarchives.gap>
- **Date:** 1997-03-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33387461.1451@southeast.net>`

```

Hi

Anybody had experience with trapping extended keystrokes (esc, function
and tab, etc) using cobol '85 without using calls to another language??
What process did you use?
Thanks.
```

#### ↳ Re: Trapping esc, function and tab keys

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1997-03-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9afef00e7a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33387461.1451@southeast.net>`
- **References:** `<33387461.1451@southeast.net>`

```

On Tue, 25 Mar 1997 19:57:05 -0500, cobal wrote:

› Hi
› 
…[3 more quoted lines elided]…
› Thanks.

In RM/COBOL,MF/COBOL and ACUCOBOL for example.

....
01 FUNC-VALUE PIC 9(4) COMP-1.
88 ESC-KEY VALUE 27.
88 F1-KEY VALUE 1.
88 F2-KEY VALUE 2.
....

ACCEPT variable LINE .... ON EXCEPTION FUNC-VALUE
CONTINUE.

IF ESC-KEY PERFORM.....
IF F1-KEY PERFORM.....
IF F2-KEY PERFORM.....

And so on.

Best regards
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
