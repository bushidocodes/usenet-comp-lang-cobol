[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/COBOL, VB5 and VanGui problem

_6 messages · 4 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM/COBOL, VB5 and VanGui problem

- **From:** "greg" <ua-author-13260@usenetarchives.gap>
- **Date:** 1998-07-29T15:04:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35BF7216.9E09F763@mrfax.com>`

```
I'm a novice at VB5 and VanGui, so I'm probably overlooking something
elementary, but I can't get my VB5 interface to open a second
communicator. On my initial form, communicator_1 successfully opens a
connection with COBOLapplication_1, which successfully communicates to
element_1. On my second form, I try to communicate with a second COBOL
application. However, the VB5 program freezes after executing the
statement "Communicator_2.Open = True". The COBOL application runs OK,
but the VB5 program hangs.

Any hints, even those prefaced with "Ya moron", are greatly appreciated.

-greg
```

#### ↳ Re: RM/COBOL, VB5 and VanGui problem

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e66f525cde-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35BF7216.9E09F763@mrfax.com>`
- **References:** `<35BF7216.9E09F763@mrfax.com>`

```
› Any hints, even those prefaced with "Ya moron", are greatly appreciated.

I am guessing here, but might it be a single site licence? I have rejected
using two different Cobols lately after I discovered that opening x windows
required x site licences. The number of machines was irrelevant, as was
the number of users. What was being counted was the number of times
the runtime was being used. Makes a mockery of the "multi-tasking" adverts.
```

#### ↳ Re: RM/COBOL, VB5 and VanGui problem

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-07-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e66f525cde-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35BF7216.9E09F763@mrfax.com>`
- **References:** `<35BF7216.9E09F763@mrfax.com>`

```
On Wed, 29 Jul 1998 19:04:04 GMT, greg wrote:

› I'm a novice at VB5 and VanGui, so I'm probably overlooking something
› elementary, but I can't get my VB5 interface to open a second
…[9 more quoted lines elided]…
› -greg
I am not quite sure about this so I not going to suggest anything.
Have you spoken with Liant supprot about this.??
You can speak with them (www.liant.com) (or with you reseller) or with
Softis (www.softis.is) this one is the manufacturer of VANGUI.
Normally there should be only one "Comunicator.Open". All the other
calls should be related with the "Comunicator.Action", This is what I
think. I may be wrong.

Best regards

FF
```

##### ↳ ↳ Re: RM/COBOL, VB5 and VanGui problem

- **From:** "greg" <ua-author-13260@usenetarchives.gap>
- **Date:** 1998-07-30T16:08:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e66f525cde-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e66f525cde-p3@usenetarchives.gap>`
- **References:** `<35BF7216.9E09F763@mrfax.com> <gap-e66f525cde-p3@usenetarchives.gap>`

```
Frederico Fonseca wrote:

› Normally there should be only one "Comunicator.Open". All the other
› calls should be related with the "Comunicator.Action", This is what I
› think. I may be wrong.
›
›

You are right. Thanks.

The documentation I have does not mention this little fact. In fact, it
implies that any number of communicators can be open at the same time.
The truth is, you can define any number of communicators, but only one
can be open at any given time. If a second communicator is opened
without closing the first, the VB program hangs.

This means you can't run a COBOL routine in background using VanGui. To
run COBOL in background, you have to initiate the run using a system
call, and pass data back to the VB module by writing it to a disc file.
The VB module must periodically check the file's time stamp to detect
when the COBOL routine has finished. That's exactly the kind of kluge I
was hoping to avoid with VanGui.

--greg
```

###### ↳ ↳ ↳ Re: RM/COBOL, VB5 and VanGui problem

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e66f525cde-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e66f525cde-p4@usenetarchives.gap>`
- **References:** `<35BF7216.9E09F763@mrfax.com> <gap-e66f525cde-p3@usenetarchives.gap> <gap-e66f525cde-p4@usenetarchives.gap>`

```
On Thu, 30 Jul 1998 20:08:01 GMT, greg wrote:

› Frederico Fonseca wrote:
› 
…[3 more quoted lines elided]…
› .....
 
› This means you can't run a COBOL routine in background using VanGui. To
› run COBOL in background, you have to initiate the run using a system
…[5 more quoted lines elided]…
› --greg
Try and pose this problem to www.softis.is. Maybe they can help you
with this. Maybe there is a turn around.

Best

Frederico Fonseca
```

###### ↳ ↳ ↳ Re: RM/COBOL, VB5 and VanGui problem

- **From:** "albert ratzlaff" <ua-author-6589172@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e66f525cde-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e66f525cde-p4@usenetarchives.gap>`
- **References:** `<35BF7216.9E09F763@mrfax.com> <gap-e66f525cde-p3@usenetarchives.gap> <gap-e66f525cde-p4@usenetarchives.gap>`

```
Hi Greg,

I've got a little C program that acts as a Unix-based server and
activates RM/COBOL programs under instructions from a Windows-based
client thru WinSock (tested with Delphi). Seems to work, though you have
to tweak the server sub.c (runcobol) file a bit. If you're interested I
can send it via email.

Regards
Albert Ratzlaff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
