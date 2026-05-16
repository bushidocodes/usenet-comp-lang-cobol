[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linking an icon and an exe-file.

_2 messages · 2 participants · 2000-01_

---

### Linking an icon and an exe-file.

- **From:** "tommy" <tommynilsen@yahoo.com>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86np6s$ppn$1@nntp.newmedia.no>`

```

Hi.

Can somone tell me how to link an icon and an exe-file ??

Tommy Nilsen
```

#### ↳ Re: Linking an icon and an exe-file.

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86p6gi$24g$1@hyperion.mfltd.co.uk>`
- **References:** `<86np6s$ppn$1@nntp.newmedia.no>`

```
Tommy,

You can't link an icon resource to an EXE as you could with the 16-bit
linkers. On 32-bit the icon has to be compiled into a resource using the
resource compiler (RC.EXE) and the .RES file produced passed to the linker
when the EXE is created.

So, your .RC would look something like

iconname ICON my.ico

Then run RC /R my.rc

That generates the .RES which you can add to the command line passed to the
linker, or if using CBLLINK (as I know you are using Micro Focus product),
just add the .RES to its command line.

Hope this helps.

tommy wrote in message <86np6s$ppn$1@nntp.newmedia.no>...
>
>Hi.
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
