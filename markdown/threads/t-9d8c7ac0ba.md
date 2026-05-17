[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Secondary extents

_4 messages · 2 participants · 1998-05_

---

### Secondary extents

- **From:** "min..." <ua-author-793677@usenetarchives.gap>
- **Date:** 1998-05-23T08:09:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k6eaf$teq$1@nnrp1.dejanews.com>`

```

I ran into this IBM JCL phrase at my new job: UNIT=(SYSDA,5)
I don't remember ever using this 'number of units' previously. After RTFM
(albeit an old FM) it appears that secondary extent attempts are solely done
on the same physical device as the primary storage. All these years I was
under the impression that the attempts would occur over the realm of the
'group' of devices identified as 'SYSDA'.

I can't see any harm in the above - I'd assume there are always 5 disk drives
available for SYSDA. And I assume when there are 6 DD statements in a STEP
using this, it still only needs 5 available devices, not 30.

So - is it correct that secondaries only occur on the primary's device? Or
does that depend on a system installation choice or a version of some IBM
system software?
And can anyone see any harm in the above? It does potentially create a multi-
volume dataset, which may be a problem for ISPF edit.

Thanks
John


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Secondary extents

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1998-05-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9d8c7ac0ba-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6k6eaf$teq$1@nnrp1.dejanews.com>`
- **References:** `<6k6eaf$teq$1@nnrp1.dejanews.com>`

```

min··.@my-··s.com wrote:
› I ran into this IBM JCL phrase at my new job: UNIT=(SYSDA,5)
› I don't remember ever using this 'number of units' previously. After RTFM
…[16 more quoted lines elided]…
› John

UNIT=SYSDA (which is equivalent to UNIT=(SYSDA,1)) allows initial
primary allocation on any eligible SYSDA volume (unless SMS is
controlling allocation, in which case SMS uses its own volume selection
rules). If the dataset needs to expand beyond the primary allocation,
all secondaries must be allocated on the same volume as the primary up
to the max allowed nr of secondaries or limits of available space on the
volume, whichever limit is reached first. Initial volume allocation for
UNIT=(SYSDA,n) is identical, but as the file expands and the available
space or max secondaries on a volume is reached, if the total number of
volumes in use is less than "n" the file is allowed to allocate its next
extent on another SYSDA volume, and then allowed to allocate additional
secondary extents on that volume until its limits are reached, etc. For
a sequential dataset, UNIT=(SYSDA,5) could conceivably allow allocation
of 5*16 extents across 5 volumes (although depending on primary &
secondary space size and volume free space, you could get as little as 5
extents--one per volume).

DFHSM 2.5 is unable to migrate a multi-volume dataset, although this
capability is present by at least DFSMShsm 1.3. I think at least one of
the ISPF V4.1 editor or ISOGON SPIFFY editor is able to edit
multi-volume datasets provided they do not exceed the amount of virtual
storage available to your TSO session. If the dataset really needs to
be multi-volume because of its size, it is unlikely your installation
defaults will allow you a large enough Region size above the line to
edit it, as edit requires the entire dataset plus control info to be in
virtual storage.

You are correct in your assumptions about the effects of multiple
UNIT=(SYSDA,n) in the same step. Each allocation is considered
independently, so as long as adequate space is otherwise available, you
can get by with as few as "n" drives total.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

##### ↳ ↳ Re: Secondary extents

- **From:** "min..." <ua-author-793677@usenetarchives.gap>
- **Date:** 1998-05-28T21:28:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9d8c7ac0ba-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9d8c7ac0ba-p2@usenetarchives.gap>`
- **References:** `<6k6eaf$teq$1@nnrp1.dejanews.com> <gap-9d8c7ac0ba-p2@usenetarchives.gap>`

```

In article <6kculo$hus$1.··.@chi··k.net>,
"Joel C. Ewing" wrote:

he wrote a definitive explanation of (SYSDA,5)answering my questions

Joel - Thanks for the explanation. Somedays ya learns something everyday.

John

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Secondary extents

- **From:** "min..." <ua-author-793677@usenetarchives.gap>
- **Date:** 1998-05-26T21:09:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9d8c7ac0ba-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6k6eaf$teq$1@nnrp1.dejanews.com>`
- **References:** `<6k6eaf$teq$1@nnrp1.dejanews.com>`

```

In article ,
red··.@i··.net (Thane Hubbell) wrote:
› 
› On Sat, 23 May 1998 12:09:51, min··.@my-··s.com wrote:
…[15 more quoted lines elided]…
› tells the system to look at 'up to 5' SYSDA units for secondaries - without
the '5', a chance of a B37 is more likely because the system only looks on
the same unit as the primary. This is when defining new datasets, of course.
The RTFM seems to back up that explanation but it's an old FM.
Thanks
John

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
