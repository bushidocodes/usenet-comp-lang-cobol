[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu COBOL

_4 messages · 3 participants · 1997-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu COBOL

- **From:** "robert s. robbins" <ua-author-17071337@usenetarchives.gap>
- **Date:** 1997-09-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34161F2F.5450@SunLink.net>`

```


Hello World,
I'm just getting started with Fujitsu COBOL 3.0. I managed to
successfully compile and execute a program from one of my old COBOL
books. I was wondering if it is possible to get screen output and maybe
prompt for user input? I don't think my old COBOL textbooks will cover
this because they only describe early versions of the language. Thanks
for your help!

Robert Robbins
rro··.@sun··k.net
```

#### ↳ Re: Fujitsu COBOL

- **From:** "graham ball" <ua-author-12745681@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aac44c93b1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34161F2F.5450@SunLink.net>`
- **References:** `<34161F2F.5450@SunLink.net>`

```

Yes, I've just started playing with Fujitsu and it does support display and
accept - see sample1 program, which BTW I couldn't get to link, because
there was no entry point/statement ??
Still got to investigate that !!

xrb··n@acc··x.netx wrote in article
...
```

##### ↳ ↳ Re: Fujitsu COBOL

- **From:** "robert s. robbins" <ua-author-17071337@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aac44c93b1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aac44c93b1-p2@usenetarchives.gap>`
- **References:** `<34161F2F.5450@SunLink.net> <gap-aac44c93b1-p2@usenetarchives.gap>`

```

Graham Ball wrote:
› 
› Yes, I've just started playing with Fujitsu and it does support display and
…[5 more quoted lines elided]…
› ...

Graham,
No entry point? I think I ran into that problem. You simply
failed to specify that SAMPLE1 program was a MAIN program. There is a
COMPILER OPTION button and a field
that you type MAIN into but I have to look over that again. You'll see a
fancy count-
down when the program is compiling.
Robert Robbins
```

#### ↳ Re: Fujitsu COBOL

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aac44c93b1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34161F2F.5450@SunLink.net>`
- **References:** `<34161F2F.5450@SunLink.net>`

```

Fujitsu COBOL fully support advanced screen handling.

Simple Console ACCEPT/DISPLAY
See: SAMPLE1 & SAMPLE2 including with Fujitsu COBOL

Full Screen ACCEPT/DISPLAY
See: SAMPLE8 included with Fujitsu COBOL

Field by Field ACCEPT/DISPLAY --
See: COPYFILE from http://www.adtools.com/support/samples.htm

Function Key Handling
See: KEYTEST from http://www.adtools.com/support/samples.htm

Fujitsu Software Corporation
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com


xrb··n@acc··x.netx wrote in article
...
› 
› On Wed, 10 Sep 1997, Robert S. Robbins wrote:
…[45 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
