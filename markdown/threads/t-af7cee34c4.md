[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please ( change the name of Wrun32.exe )

_1 message · 1 participant · 1999-09_

---

### Re: Please ( change the name of Wrun32.exe )

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7so8n4$ajr$1@news.cerf.net>`
- **References:** `<7skq84$f0t$1@talia.mad.ttd.net>`

```
Oscar Jofre wrote in message <7skq84$f0t$1@talia.mad.ttd.net>...
>I'm working with AcuCobol.
>
>Can I change the name of the Wrun32.exe ( in the Process Administration )
in
>Windows Nt with the name of the program ??
>
>So when I run \:> wrun32 prog1, I'd like to see running prog1.exe not
>wrun32.exe. I add funcitions with c++ in AcuCobol.

Yes you can rename wrun32.exe, just remember to rename the license file too
(not the extension!)

However, if the purpose is to specify a window title, you may do that inside
your cobol app:

    DISPLAY WINDOW TITLE "My title"

Or you may put it in your configuration file:

    window-title    My title

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
