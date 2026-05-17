[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling winapi under MF cobol 3.2

_2 messages · 2 participants · 1997-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Calling winapi under MF cobol 3.2

- **From:** "holger kurze" <ua-author-17073321@usenetarchives.gap>
- **Date:** 1997-12-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd05b7$2ba9e330$0b1fa8c0@calvin1>`

```

Hey folks,

does anyone know how to call the Windows printer dialog from
an cobol text based program.
It魹ｽs not a Windows application, its a DOS application running on
Windows in a dos box.
In acucobol it works with " call win$printer" etc. but I think MF
don魹ｽt knows that call.
I魹ｽm using MF Toolset 3.2 any suggestions?

Thanks in advance Holger :-)
```

#### ↳ Re: Calling winapi under MF cobol 3.2

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1997-12-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1c8a5ddb27-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd05b7$2ba9e330$0b1fa8c0@calvin1>`
- **References:** `<01bd05b7$2ba9e330$0b1fa8c0@calvin1>`

```

You don't say if it is windows 31 or 95/NT so I will assume 95/NT.

I needed to do a similar thing under MF COBOL V4. something for NT. I
ended up writing a small C program that invoked the dialog box and then
calling that from the COBOL program. I would suspect you could do the
same thing with VB. I know this is not the COBOL answer you were looking
for but I found this to be pretty easy.. and It made the printer dialog
easily available from other apps...

I don't know what you are planning on printing, but printing is no
longer as easy as redirecting text to a port, though it could be...

I needed to dump a GUI screen image and had to deal with setting up
device contexts and handling palettes, etc... It was quite a learning
experience. If you have the Microsoft C product available there is a
sample program that covers these topics.

Good Luck And Happy Holidays!!!

Holger Kurze wrote:

› Hey folks,
› 
…[9 more quoted lines elided]…
› 



This bit of nonsense brought to you by the annoying spammers who like to
troll the news groups for new people to annoy. Protect yourself and
obfuscate your email address.

Return address is John underscore Saxton at ML dot com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
