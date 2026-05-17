[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Opencobol (Gnucobol) error

_4 messages · 2 participants · 2016-05_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### Opencobol (Gnucobol) error

- **From:** "lrz1035" <ua-author-14501793@usenetarchives.gap>
- **Date:** 2016-05-25T08:54:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ni479p$1o8m$1@rsli.inka.de>`

```
I tried to build a self-written cobol program on a recent openbsd box.
cobc -x apa0xx.cob gives errors:

---------------------------------- cut --------------------------------

/usr/local/lib/libcob.so.3.0: warning: vsprintf() is often misused,
please use vsnprintf()
/usr/local/lib/libcob.so.3.0: warning: strcpy() is almost always
misused, please use strlcpy()
/usr/local/lib/libcob.so.3.0: warning: sprintf() is often misused,
please use snprintf()
/usr/local/lib/libcob.so.3.0: warning: strcat() is almost always
misused, please use strlcat()
/tmp/cob9886_0.o(.text+0x5ad): In function PA0XX_':
: undefined reference to ob_display'
/tmp/cob9886_0.o(.text+0x5ee): In function PA0XX_':
: undefined reference to ob_display'
/tmp/cob9886_0.o(.text+0x62f): In function PA0XX_':
: undefined reference to ob_display'
/tmp/cob9886_0.o(.text+0x156f): In function PA0XX_':
: undefined reference to ob_get_environment'
collect2: ld returned 1 exit status

---------------------------------- cut --------------------------------

On an older freebsd box, the same source compiles without any error.
Any idea what might be wrong on the openbsd box?

V*
```

#### ↳ Re: Opencobol (Gnucobol) error

- **From:** "lrz1035" <ua-author-14501793@usenetarchives.gap>
- **Date:** 2016-05-26T06:11:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e98efb74ee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ni479p$1o8m$1@rsli.inka.de>`
- **References:** `<ni479p$1o8m$1@rsli.inka.de>`

```
Volker Englisch schrieb am 25.05.2016:
› /usr/local/lib/libcob.so.3.0: warning: strcat() is almost always
› misused, please use strlcat()

Solved. It was a problem on just one openbsd box. A clean new setup
made the errors pass away ;-)

V*
```

##### ↳ ↳ Re: Opencobol (Gnucobol) error

- **From:** "luuk" <ua-author-557437@usenetarchives.gap>
- **Date:** 2016-05-27T16:32:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e98efb74ee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e98efb74ee-p2@usenetarchives.gap>`
- **References:** `<ni479p$1o8m$1@rsli.inka.de> <gap-e98efb74ee-p2@usenetarchives.gap>`

```
On 26-05-16 12:11, Volker Englisch wrote:
› Volker Englisch schrieb am 25.05.2016:
›› /usr/local/lib/libcob.so.3.0: warning: strcat() is almost always
…[6 more quoted lines elided]…
› 

This looks like a Microsoft sollution....

;)
```

###### ↳ ↳ ↳ Re: Opencobol (Gnucobol) error

- **From:** "lrz1035" <ua-author-14501793@usenetarchives.gap>
- **Date:** 2016-05-28T12:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e98efb74ee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e98efb74ee-p3@usenetarchives.gap>`
- **References:** `<ni479p$1o8m$1@rsli.inka.de> <gap-e98efb74ee-p2@usenetarchives.gap> <gap-e98efb74ee-p3@usenetarchives.gap>`

```
Luuk schrieb am 27.05.2016:
› On 26-05-16 12:11, Volker Englisch wrote:
›› Volker Englisch schrieb am 25.05.2016:
…[6 more quoted lines elided]…
› This looks like a Microsoft sollution....

Yes, I know... But, for I had to install opencobol on more than one
machine, I saw that there were no such problems on machine no. 2. So I
took the most easy approach ;-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
