[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Releasing MF Cobol DLL

_6 messages · 4 participants · 1998-05 → 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Releasing MF Cobol DLL

- **From:** "ed.s..." <ua-author-13502311@usenetarchives.gap>
- **Date:** 1998-05-13T09:35:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jc7ig$qdm$1@nnrp1.dejanews.com>`

```

Subject: Releasing MF Cobol DLL I have written a DLL in Micro Focus Cobol
(32-bit, running under NT) which is called by a PowerBuilder application. We
have a change management problem in that the application runs a walkup,
self-service kiosk which management is loath to bring down. When we have to
put in a new version of the DLL, the app still has a lock on it. My take is
that (regardless of language) it is always the calling program's
responsibility to release any called programs, but asked to look into the
possibility of having the Cobol DLL 'self cancel' when it returns to the
caller. Does anyone have any knowledge of how this might be done, or a good
summation of why it can't be done? TIA. Ed Stevens

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Releasing MF Cobol DLL

- **From:** "kenmu..." <ua-author-17072514@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0fd06d4b3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6jc7ig$qdm$1@nnrp1.dejanews.com>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com>`

```

› Subject: Releasing MF Cobol
› DLL
…[32 more quoted lines elided]…
› 

Have you tried the "Cancel" statement...if that does not work, try
"FreeLibrary" api...

Ken Mullins
Atlanta, GA
```

#### ↳ Re: Releasing MF Cobol DLL

- **From:** "edste..." <ua-author-8362724@usenetarchives.gap>
- **Date:** 1998-07-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0fd06d4b3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6jc7ig$qdm$1@nnrp1.dejanews.com>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com>`

```
It's not that we aren't allowed to stop the app, but we have to do it
during a scheduled, weekend 'maintenance window' and have to send a
tech to each kiosk location to do it, so we can't just slip in a new
module whenever we feel like it.

On Sun, 05 Jul 1998 10:35:56 GMT, fin··t@end··f.message (Siegen)
wrote:

› Ed.··.@nmm··a.com wrote:
› 
…[69 more quoted lines elided]…
› ---------------------

Ed Stevens/TN
```

##### ↳ ↳ Re: Releasing MF Cobol DLL

- **From:** "findit" <ua-author-874518@usenetarchives.gap>
- **Date:** 1998-07-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0fd06d4b3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0fd06d4b3-p3@usenetarchives.gap>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <gap-b0fd06d4b3-p3@usenetarchives.gap>`

```
EdS··.@c··.com (Ed Stevens) wrote:

:> It's not that we aren't allowed to stop the app, but we have to
:> do it during a scheduled, weekend 'maintenance window' and
:> have to send a tech to each kiosk location to do it, so
:> we can't just slip in a new module whenever we feel like it.
Understood, but your original post said you had a
problem upgrading because management didn't like
the idea of having to shut down the application.

However, seeings you can shut down the application
during a scheduled weekend maintenance then that
is the time to do the upgrade. The application, if
running, will cause a "lock" to be held on any
DLLs it may be using --- whether they are yours or
the operating system's. That is what you noticed
and which prompted your original post.

I think that is your best option.

Apologies should my original response have seemed
a little terse -- I was feeling somewhat grumpy
that day.

Cheers,

[snip]


-- Siegen
----------------------
Please remove the letter "x" from my email address, should you wish
to email me.
(ro··.@com··m.au)
---------------------
```

###### ↳ ↳ ↳ Re: Releasing MF Cobol DLL

- **From:** "edste..." <ua-author-8362724@usenetarchives.gap>
- **Date:** 1998-07-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0fd06d4b3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0fd06d4b3-p4@usenetarchives.gap>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <gap-b0fd06d4b3-p3@usenetarchives.gap> <gap-b0fd06d4b3-p4@usenetarchives.gap>`

```
On Mon, 13 Jul 1998 07:32:12 GMT, fin··t@end··f.message (Siegen)
wrote:

› Apologies should my original response have seemed
› a little terse -- I was feeling somewhat grumpy
› that day.


Gee, I can't imagine *anyone* in this business *ever* being grumpy!

Ed Stevens/TN
```

###### ↳ ↳ ↳ Re: Releasing MF Cobol DLL

_(reply depth: 4)_

- **From:** "findit" <ua-author-874518@usenetarchives.gap>
- **Date:** 1998-07-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0fd06d4b3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0fd06d4b3-p5@usenetarchives.gap>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <gap-b0fd06d4b3-p3@usenetarchives.gap> <gap-b0fd06d4b3-p4@usenetarchives.gap> <gap-b0fd06d4b3-p5@usenetarchives.gap>`

```
EdS··.@c··.com (Ed Stevens) wrote:

:> On Mon, 13 Jul 1998 07:32:12 GMT, fin··t@end··f.message (Siegen)
:> wrote:

:> >Apologies should my original response have seemed
:> >a little terse -- I was feeling somewhat grumpy
:> >that day.

:>
:> Gee, I can't imagine *anyone* in this business *ever* being grumpy!
:>
Yes, it is difficult to imagine isn't it ;)

Cheers and goodluck etc.

Rod.

:> Ed Stevens/TN

-- Siegen
----------------------
Please remove the letter "x" from my email address, should you wish
to email me.
(ro··.@com··m.au)
---------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
