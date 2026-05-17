[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol for MS-DOS

_2 messages · 2 participants · 1996-11_

---

### Cobol for MS-DOS

- **From:** "jeremy rinderknecht" <ua-author-1876917@usenetarchives.gap>
- **Date:** 1996-11-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3299D11E.1E42@bbs.cedarnet.com>`

```

Greetings:
I am writing a payroll program, and instead of using display
statements to paint a screen, I have built several panels in "Thedraw" an
ansi/ascii screen design program. In order to save these screens in
color, I have to save them as executible .COM files. Is there a way to
call a program like this from cobol? Currently I have the following call
statement:
Call 'timecrd0.com'.
The source compiles fine, but when I attempt to link it, the linker comes
back with the following :
Unresolved externals: (timecrd0.com)

Is there anyway I can get around this annoying error?
Thank you.
JR.
```

#### ↳ Re: Cobol for MS-DOS

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-11-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7ad6ee9ce-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3299D11E.1E42@bbs.cedarnet.com>`
- **References:** `<3299D11E.1E42@bbs.cedarnet.com>`

```

Jeremy Rinderknecht wrote:

› Greetings:
› I am writing a payroll program, and instead of using display 
…[4 more quoted lines elided]…
› statement:

Basically you want these screens to show? If you're running on a DOS
environment, and have ANSI.SYS, just save the files as .ANS and import
them into your cobol program (cut/paste), each segment of the file
being in an X field. Otherwise, the only other solution I can think
of for you is to write an object that reads in the codes, interprets
them, and changes color (does PC Cobol have something like that as an
extension? If not, you can always write it in assembler -- there's
enough resources out there for it).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
