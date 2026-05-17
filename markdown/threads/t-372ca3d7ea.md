[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Segmentation; thanks

_4 messages · 4 participants · 1998-01_

---

### Segmentation; thanks

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1998-01-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34AFF393.6398@swbell.net>`

```

A couple of weeks ago I started a thread about ALTER in the presence
of segmentation. Thanks to everyone who responded, for contributing
to my education.

I added a page to my web site to summarize my understanding of
segmentation:

http://home.swbell.net/mck9/cobol/style/segment.html

If I still don't have it right, I hope someone will correct me.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

#### ↳ Re: Segmentation; thanks

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-01-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-372ca3d7ea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34AFF393.6398@swbell.net>`
- **References:** `<34AFF393.6398@swbell.net>`

```

On Sun, 04 Jan 1998 14:39:47 -0600, "Michael C. Kasten"
wrote:

› A couple of weeks ago I started a thread about ALTER in the presence
› of segmentation.  Thanks to everyone who responded, for contributing 
…[10 more quoted lines elided]…
› http://home.swbell.net/mck9/cobol/cobol.html

I like your website, Michael, but -- in my opinion -- at least for
mainframes -- segmentation died in mid 70's when virtual memory became
widely available. I recall teaching it in 72-74 time frame. Also
taught class in LinkageEditor overlays and Linkage regions. It was a
useful technique when memory was tight. Nicely written, though. I'm
pleased to see much of this documented now. thanks,

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: Segmentation; thanks

- **From:** "ed milne." <ua-author-6589438@usenetarchives.gap>
- **Date:** 1998-01-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-372ca3d7ea-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34AFF393.6398@swbell.net>`
- **References:** `<34AFF393.6398@swbell.net>`

```

"These days, most big machines use virtual memory пїЅ"

ItпїЅs the operating system rather than the computer that provide virtual
memory. A PC running Windows has virtual memory. The same machine running
straight DOS does not.

Its just not big machines that have virtual memory since operating systems
like Windows and Linux have that feature. Of course, the PCs that run these
operating systems are much more powerful than the mainframes that required
segmented application programs. The idea of a "big" machine is very time
dependant.

› A couple of weeks ago I started a thread about ALTER in the presence
› of segmentation.  Thanks to everyone who responded, for contributing
…[7 more quoted lines elided]…
› If I still don't have it right, I hope someone will correct me.
```

##### ↳ ↳ Re: Segmentation; thanks

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1998-01-08T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-372ca3d7ea-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-372ca3d7ea-p3@usenetarchives.gap>`
- **References:** `<34AFF393.6398@swbell.net> <gap-372ca3d7ea-p3@usenetarchives.gap>`

```

Ed Milne. wrote:
› 
› "These days, most big machines use virtual memory  …"
…[10 more quoted lines elided]…
› 
Swapping is not the same as virtual memory. The concept of virtual
memory allows an application (or system) program to reference a linear
virtual addressing space which is mapped by the hardware and operating
system onto real memory and external storage in a manner that is
transparent (except for performance) to the running program. There are
some places in the guts of the operating system that has to be aware of
real memory (in order to manage it), but application code would just be
aware of virtual memory. This requires at a minimum some hardware
assistance to either handle the mapping of a virtual address to the
correct real address before performing the memory reference or to
produce an interrupt to the operating system to fetch the required
"page" from external storage if it is not already in memory, plus
priviledged or supervisory mode hardware instructions accessible only to
the operating system for the control of real memory. If the
architecture of the computer hardware doesn't provide this capability,
there is no practical way to kludge true virtual memory support via the
operating system. The "big" machines have much more than this minimal
support in order to reduce the overhead of virtual memory management.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
