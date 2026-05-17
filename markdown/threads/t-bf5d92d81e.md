[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus COBOL refresh key

_3 messages · 3 participants · 1996-05 → 1996-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus COBOL refresh key

- **From:** "sria..." <ua-author-17087282@usenetarchives.gap>
- **Date:** 1996-05-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00001a84+000012c3@msn.com>`

```

This is a generic question concerning Micro Focus COBOL under Unix.
Is there any way to set up a key combination to have COBOL
automatically re-paint the screen? We are using an operating-system
hotkey facility to toggle between a COBOL application and an email
system, and need to repaint the screen on returning to COBOL.

I know that MF COBOL keeps a memory-mapped screen, so it should be
possible. Their documentation refers to a refresh key being the
"slash" "pipe" key combination, but it only seems to work with their
own tools like Toolbox or Animator, not user-applications. The
problem is that if COBOL is ACCEPTing say a PIC X(10) field, any
keystrokes we use are simply taken as a field entry.

Any ideas?

Thanks in advance.
```

#### ↳ Re: Micro Focus COBOL refresh key

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-06-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf5d92d81e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<00001a84+000012c3@msn.com>`
- **References:** `<00001a84+000012c3@msn.com>`

```



sri··.@m··.com (Andrew Torry) wrote:
› This is a generic question concerning Micro Focus COBOL under Unix. 
› Is there any way to set up a key combination to have COBOL 
› automatically re-paint the screen? We are using an operating-system 
› hotkey facility to toggle between a COBOL application and an email 
› system, and need to repaint the screen on returning to COBOL.

Hi. I'll look into the "/|" combination for you. In the meantime, try
using the OS support for suspending foreground processes. If you type
"stty susp ^Z" (or maybe it's already defined), then hitting the ctrl-Z
key during the accept will pop the COBOL RTS into the background and
you can run your mail system or whatever. When you want to resume the
COBOL program simply type "fg" in the shell and the RTS will come back.
It's aware that this has happened, so will automatically refresh the
screen for you.

Cheers, Kev.
```

#### ↳ Re: Micro Focus COBOL refresh key

- **From:** "ni..." <ua-author-17086511@usenetarchives.gap>
- **Date:** 1996-06-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf5d92d81e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<00001a84+000012c3@msn.com>`
- **References:** `<00001a84+000012c3@msn.com>`

```

sri··.@m··.com (Andrew Torry) wrote:

› to have COBOL
› automatically re-paint the screen?

I asked them aboutthis some years ago & the only answer at the time
was to check for a faction key or similar using a crt-status is within
special-names. If for example F10 is hit then code to redraw the
screen is run.

I now use V4.0 with generic attributes so I make a call to my own
routine to repaint. This works in full colour as well.

e.g.
call "store-screen".
string "e-mail_prog" x"00" delimited by size into communication-line.
call "system" using commincation-line.
call "restore-screen".


This works a treat.
Nick.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
