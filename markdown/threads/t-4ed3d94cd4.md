[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WinAPI

_4 messages · 4 participants · 1997-08_

---

### WinAPI

- **From:** "trig..." <ua-author-986361@usenetarchives.gap>
- **Date:** 1997-08-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970811212600.RAA17664@ladder02.news.aol.com>`

```

How come when I go to run a Cobol program that calls the windows api
(example below) I get an error that says called program not found in
drive/directory??

Using MF cobol 2.0 and on a win 95 machine. Any suggestions?
CALL WinAPI "WINEXEC"
USING BY REFERENCE LS-Shell-Command-Line
BY VALUE LS-Shell-Window-State
RETURNING LS-Shell-Return-Code
END-CALL.

Tom Wright

tomwright1 AT juno.com
```

#### ↳ Re: WinAPI

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1997-08-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed3d94cd4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970811212600.RAA17664@ladder02.news.aol.com>`
- **References:** `<19970811212600.RAA17664@ladder02.news.aol.com>`

```

TRight785 wrote:
› 
› How come when I go to run a Cobol program that calls the windows api
…[12 more quoted lines elided]…
› tomwright1 AT juno.com

As Kev says, the case is wrong, so try "WinExec" but as the ANSI COBOL
default is case insensitivity in a call, I think you need to set the
CASE directive as in " $set case".



Martyn.

To reply, remove the two "unspam." from the address.
```

#### ↳ Re: WinAPI

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-08-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed3d94cd4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19970811212600.RAA17664@ladder02.news.aol.com>`
- **References:** `<19970811212600.RAA17664@ladder02.news.aol.com>`

```

TRight785 wrote:
› 
› How come when I go to run a Cobol program that calls the windows api
…[8 more quoted lines elided]…
› END-CALL.

Hi Tom.

The problem is probably case-sensitivity - try calling "WinExec".
This is a caveat of the dynamically bound environment - when you call
a function the COBOL RTS must bind to it. That means looking it up in
the DLLs, and the Windows function which looks it up is case sensitive.
Once you've called it once, the COBOL RTS will cache the reference and
will allow case-insensitive calls to it. Probably best to make all
WinAPI calls the correct case, though, as a slight change in processing
logic could cause a case-insensitive CALL to be executed first.

OTOH, if that isn't the problem, give some more clues as to how you
are linking (or are you using .int/.gnt etc).

Cheers,
Kev.
```

#### ↳ Re: WinAPI

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-08-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ed3d94cd4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19970811212600.RAA17664@ladder02.news.aol.com>`
- **References:** `<19970811212600.RAA17664@ladder02.news.aol.com>`

```

In message <<199··.@lad··l.com>> tri··.@a··.com writes:
› (example below) I get an error that says called program not found in
› drive/directory??
…[10 more quoted lines elided]…
› tomwright1 AT juno.com

MF Cobol version 2.0 does not support writing Windows programs,
However this may be something else, such as Personal Cobol ?
Windows support was added in 2.4 (AFAIK).

If this is a version that does support Windows development then
the call convention should be static (ie WinAPI should be 11
or use leading __ as in CALL WINAPI "__WinExec" ...).

You will also need to link in Win.Lib or equivalent.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
