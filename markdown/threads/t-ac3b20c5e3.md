[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Refresh window created by Dialog System 3.0 with WIN32-API.

_4 messages · 4 participants · 1998-03_

---

### Refresh window created by Dialog System 3.0 with WIN32-API.

- **From:** "tommy" <ua-author-13561@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fb19i$pbp$1@o.online.no>`

```

I need to refresh a window using WIN32-API calls from Cobol .
The window is created using Dialog System 3.0 from MicroFocus.

Because this makes things a lot easier,
I don't want to return to DialogSystem and do the refresh there.

Anyone know of wich API-calls to use ??


Tommy
tommynilsen@"nospam".yahoo.com
```

#### ↳ Re: Refresh window created by Dialog System 3.0 with WIN32-API.

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac3b20c5e3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6fb19i$pbp$1@o.online.no>`
- **References:** `<6fb19i$pbp$1@o.online.no>`

```

Hi Tommy,

Why do you not want to do the refresh with Dialog ?


Bob
```

#### ↳ Re: Refresh window created by Dialog System 3.0 with WIN32-API.

- **From:** "gco..." <ua-author-17074589@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac3b20c5e3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6fb19i$pbp$1@o.online.no>`
- **References:** `<6fb19i$pbp$1@o.online.no>`

```

tommy ("tommynilsen"@\"nospam\".yahoo.com) wrote:
: I need to refresh a window using WIN32-API calls from Cobol .
: The window is created using Dialog System 3.0 from MicroFocus.

: Because this makes things a lot easier,
: I don't want to return to DialogSystem and do the refresh there.

: Anyone know of wich API-calls to use ??


What exactly do you mean by "refresh"? Can you give me
an explanation of what you are doing to require the
refresh in the first place?

For quickest response, you may want to contact me by e-mail.

Cheers!
Greg
```

##### ↳ ↳ Re: Refresh window created by Dialog System 3.0 with WIN32-API.

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac3b20c5e3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac3b20c5e3-p3@usenetarchives.gap>`
- **References:** `<6fb19i$pbp$1@o.online.no> <gap-ac3b20c5e3-p3@usenetarchives.gap>`

```

Tommy,

It sounds like you are using 32 bit Dialog. You may want to look at the
Dialog vocabulary feature. This allows you to place Dialog commands
within your COBOL source. See the demos in the DS\DEMO\GUI\VOC*.*.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus UK.

gcondon wrote in message <6fca2m$l.··.@lot··i.com>...
› tommy ("tommynilsen"@\"nospam\".yahoo.com) wrote:
› : I need to refresh a window using WIN32-API calls from Cobol .
…[15 more quoted lines elided]…
› Greg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
