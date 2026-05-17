[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling VB progs from MF Cobol....

_5 messages · 4 participants · 1996-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Calling VB progs from MF Cobol....

- **From:** "de..." <ua-author-17086476@usenetarchives.gap>
- **Date:** 1996-08-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<321CD647.1B45@epix.net>`

```

Is there any way to call a Visual Basic .exe file from MF Cobol v3.2?
(or any Windows application, for that matter???)
```

#### ↳ Re: Calling VB progs from MF Cobol....

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-08-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-552f9fc4da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<321CD647.1B45@epix.net>`
- **References:** `<321CD647.1B45@epix.net>`

```

In message <<321··.@ep··x.net>> DE··.@ep··x.net writes:

Is there any way to call a Visual Basic .exe file from MF Cobol v3.2?
(or any Windows application, for that matter???)

No. But you can do it the other way round with VB calling a Cobol
DLL (Dynamic Load Library).

I don't think that you can build a DLL in VB and that would be
required to make it callable. You can, however, execute any .EXE
(ie start it up) using the appropriate .API WinExec().
```

##### ↳ ↳ Re: Calling VB progs from MF Cobol....

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1996-08-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-552f9fc4da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-552f9fc4da-p2@usenetarchives.gap>`
- **References:** `<321CD647.1B45@epix.net> <gap-552f9fc4da-p2@usenetarchives.gap>`

```

Richard Plinston wrote:
› 
› In message <<321··.@ep··x.net>> DE··.@ep··x.net writes:
…[9 more quoted lines elided]…
› (ie start it up) using the appropriate .API WinExec().
Actually there is a product from Simply Solutions called Visual DLL that
will turn VB programs into DLL's. I haven't used the product, but came
across the the ad in the VB programmers journal. The ad was being run
by VBextras at 1-800-788-4794, http://www.vbxtras.com.
-Dan Maltes
```

#### ↳ Re: Calling VB progs from MF Cobol....

- **From:** "john power" <ua-author-515717@usenetarchives.gap>
- **Date:** 1996-08-25T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-552f9fc4da-p4@usenetarchives.gap>`
- **In-Reply-To:** `<321CD647.1B45@epix.net>`
- **References:** `<321CD647.1B45@epix.net>`

```

I'am in the same boat as yourself if you do get an answer to your solution
could you please e-mail your answers.

Regards ...Jon
```

##### ↳ ↳ Re: Calling VB progs from MF Cobol....

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1996-08-31T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-552f9fc4da-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-552f9fc4da-p4@usenetarchives.gap>`
- **References:** `<321CD647.1B45@epix.net> <gap-552f9fc4da-p4@usenetarchives.gap>`

```

John Power wrote:
›
› I'am in the same boat as yourself if you do get an answer to your solution
› could you please e-mail your answers.
›
› Regards ...Jon
Visual DLL from Simply Solutions should do the trick for you. It
creates Windows standard DLL's from VB3 and VB4 code. Product info at
http://www.vbxtras.com/products/VisualDLL/visauldll.htm
and can be purchased online from VBextras at http://www.vbxtras.com
By the way, I am in no way affiliated with Simply Solutions or VBextras
and I have never used the Visual DLL product. I'm just passing along
info I came across that might help you.
Keep surfin'
Dan Maltes
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
