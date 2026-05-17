[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fuji COBOL vs Realia COBOL for PC's

_2 messages · 2 participants · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fuji COBOL vs Realia COBOL for PC's

- **From:** "me" <ua-author-10431@usenetarchives.gap>
- **Date:** 1998-06-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l9eri$p86$1@utnetw.utoledo.edu>`

```

Pardon the stupidity on my part but I'm having difficulty understanding the
use of the FunctionKeys (F1-F12) with Fuji COBOL. My experience with Realia
and their CALL-DOS-KEYBOARD subroutines, and other DOS subroutines, made the
programming to easy. Now, with Fuji I'm just not getting it.

Any suggestions or input? I've read every damn manual Fuji sent with the CD
but can't find info on Function Keys and using their resultants to control a
program. I've dl'd some little prog called KEYTEST from the Fuji Web but
still am hitting a wall.

ThanX..
```

#### ↳ Re: Fuji COBOL vs Realia COBOL for PC's

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-06-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bec93fdf7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6l9eri$p86$1@utnetw.utoledo.edu>`
- **References:** `<6l9eri$p86$1@utnetw.utoledo.edu>`

```

The KEYTEST program demonstrates testing if a function key has been pressed
during a standard ACCEPT statement. If you want to scan the keyboard and do
not want to use an ACCEPT statement, then Fujitsu COBOL V4 offers a
CBL_Routine to scan the keyboard.

For more information on Fujitsu COBOL V4 see: http://www.adtools.com/4/

For more information on Upgrading to Fujitsu COBOL V4 see:
http://www.adtools.com/order/faxform.htm

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


ME wrote in message <6l9eri$p86$1.··.@utn··o.edu>...
› Pardon the stupidity on my part but I'm having difficulty understanding the
› use of the FunctionKeys (F1-F12) with Fuji COBOL.  My experience with
…[16 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
