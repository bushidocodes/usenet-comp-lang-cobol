[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Releasing MF Cobol DLL

_3 messages · 2 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Releasing MF Cobol DLL

- **From:** EdStevens1@csi.com (Ed Stevens)
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a7d459.4556482@news.eur.sprynet.com>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <359df7aa.34446254@news.comcen.com.au>`

```
It's not that we aren't allowed to stop the app, but we have to do it
during a scheduled, weekend 'maintenance window'  and have to send a
tech to each kiosk location to do it, so we can't just slip in a new
module whenever we feel like it.

On Sun, 05 Jul 1998 10:35:56 GMT, findit@end.of.message (Siegen)
wrote:

>Ed.Stevens@nmm.nissan-usa.com wrote:
>
…[69 more quoted lines elided]…
>---------------------

Ed Stevens/TN
```

#### ↳ Re: Releasing MF Cobol DLL

- **From:** findit@end.of.message (Siegen)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a9b7f9.630228@news.comcen.com.au>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <359df7aa.34446254@news.comcen.com.au> <35a7d459.4556482@news.eur.sprynet.com>`

```
EdStevens1@csi.com (Ed Stevens) wrote:

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
(rodsp@comxcen.com.au)
---------------------
```

##### ↳ ↳ Re: Releasing MF Cobol DLL

- **From:** EdStevens1@csi.com (Ed Stevens)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35aa9c62.29443771@news.eur.sprynet.com>`
- **References:** `<6jc7ig$qdm$1@nnrp1.dejanews.com> <359df7aa.34446254@news.comcen.com.au> <35a7d459.4556482@news.eur.sprynet.com> <35a9b7f9.630228@news.comcen.com.au>`

```
On Mon, 13 Jul 1998 07:32:12 GMT, findit@end.of.message (Siegen)
wrote:

>Apologies should my original response have seemed
>a little terse -- I was feeling somewhat grumpy
>that day.


Gee, I can't imagine *anyone* in this business *ever* being grumpy!
<VBG>
Ed Stevens/TN
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
