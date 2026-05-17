[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Persistency

_4 messages · 3 participants · 1998-04_

---

### Persistency

- **From:** "ralf laemmel" <ua-author-13874780@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3534F31C.2519@informatik.uni-rostock.de>`

```

Hi all.

I try understand the state of the affairs
concerning PERSISTENCY in COBOL.

Raymond Obin's book OO COBOL for COBOL programmers,
for example, proposes a system-object supporting persistency
based assigning names to persistent objects.
However, looking into the committee draft
this issue is not addressed at all. So what is
the expected or de-facto standard for persistency?

Many thanks,
Ralf
```

#### ↳ Re: Persistency

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e05fec50-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3534F31C.2519@informatik.uni-rostock.de>`
- **References:** `<3534F31C.2519@informatik.uni-rostock.de>`

```

The following is the reply that I received from the Chair of J4,

"J4 and its OO ad hoc considered including persistence in the next COBOL
standard by means of a system-object that assigned names to objects to make
them persistent. After further consideration, it was decided that the
technology in this area was not mature. Persistence of objects, like other
data in COBOL, is gained through the use of files and databases.

Don Schricker
Chair, COBOL technical committee J4"



Ralf Laemmel wrote in message <353··.@inf··k.de>...
› Hi all.
› 
…[11 more quoted lines elided]…
› Ralf
```

##### ↳ ↳ Re: Persistency

- **From:** "ralf laemmel" <ua-author-13874780@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e05fec50-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0e05fec50-p2@usenetarchives.gap>`
- **References:** `<3534F31C.2519@informatik.uni-rostock.de> <gap-f0e05fec50-p2@usenetarchives.gap>`

```

› Persistence of objects, like other
› data in COBOL, is gained through the use of files and databases.
› 
› Don Schricker
› Chair, COBOL technical committee J4"

Thanks.
So what is about the vendors? Do they agree to that view.
Or is it likely that a modern OO COBOL environment provides
special support for persistency (e.g. in the sense of a system
object assigning names to objects). I understand your attitude
why the standardization committee does not want to fix that issue.

However, (IMO) without support for persistency deep in the
language or environment resp.,
we cannot speak about persistnt
objects in the strong sense. It must be irrelevant for a programmer
if an object is in the memory or in an object store on the disk.
It is a real burden for the programmer to code that object data
is stored in files and reloaded during the next run.

More critically, persistency gained through files and databases
seems to be VERY limited: For example, if I have a class CUSTOMER,
I really want to use object references to CUSTOMER objects anywhere
in my application. How can I do that without support for persistent
objects? Besides the fact that all the customer objects will not fit
into the memory, I had to RECREATE all the objects for every run.
Moreover, it is not straightforward how to present object references
in files or databases?

I appreciate your comments.

Ralf Laemmel
```

##### ↳ ↳ Re: Persistency

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-04-16T17:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e05fec50-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0e05fec50-p2@usenetarchives.gap>`
- **References:** `<3534F31C.2519@informatik.uni-rostock.de> <gap-f0e05fec50-p2@usenetarchives.gap>`

```

In article <6h5cja$j.··.@dfw··m.com>,
"William M. Klein" wrote:
› 
› The following is the reply that I received from the Chair of J4,
…[26 more quoted lines elided]…
› The OO workbench product for MicroFocus COBOL already supports persistence
from one run to the next. I have not used it but it is documented. There is
also an early release File Dictionary class that would support the same thing
... so there is a work around today.


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
