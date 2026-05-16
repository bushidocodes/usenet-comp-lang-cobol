[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Netexpress/Dialog System

_5 messages · 2 participants · 2003-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Netexpress/Dialog System

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-06T12:28:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2490636.1044534514@dbforums.com>`

```

how to maintain a window(GUI) in first same plan that other applications
are open? I saw that with the browse Opera.

Marcos A.S.
Brasil
```

#### ↳ Re: Microfocus Netexpress/Dialog System

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-06T09:49:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2zu0a.5148$CF1.920621@news20.bellglobal.com>`
- **References:** `<2490636.1044534514@dbforums.com>`

```
Are you talking about always on top?

Calin, TORONTO


"mfcobol2002" <marcos_as@terra.com.br> wrote in message
news:2490636.1044534514@dbforums.com...
>
> how to maintain a window(GUI) in first same plan that other applications
…[6 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Microfocus Netexpress/Dialog System

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-06T17:29:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2492064.1044552591@dbforums.com>`
- **References:** `<2490636.1044534514@dbforums.com>`

```

yes, on top..ever

marcos A.S
Brasil
```

##### ↳ ↳ Re: Microfocus Netexpress/Dialog System

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-06T15:33:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Bz0a.3793$qQ.1003363@news20.bellglobal.com>`
- **References:** `<2490636.1044534514@dbforums.com> <2492064.1044552591@dbforums.com>`

```
Two choices:
    - use WS_EX_TOPMOST extended style when creating the window;
    - use the SetWindowPos api with the HWND_TOPMOST after the window
creation;

With NetExpress there is a method in the AbstractWindow class called
"topMost" that makes the call for you, all you need is an object reference
to your window.

Good luck,
Calin, TORONTO


"mfcobol2002" <marcos_as@terra.com.br> wrote in message
news:2492064.1044552591@dbforums.com...
>
> yes, on top..ever
…[5 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Microfocus Netexpress/Dialog System

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-07T11:21:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2496182.1044616868@dbforums.com>`
- **References:** `<2490636.1044534514@dbforums.com>`

```

thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
