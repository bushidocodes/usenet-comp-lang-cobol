[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Qualifying names

_4 messages · 4 participants · 2018-09 → 2018-10_

---

### Qualifying names

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T14:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`

```
When should one qualify names in cobol: Every time, or when there's a conflict?

Do you write

first-name of very-long-name-of-some-structure

or

first-name

?

Up to now, I tried to qualify names all the time, but this hurts readability, and anyway, the compiler will let me know if there's some conflict. What's a good practice?

Thanks,

Mayer
```

#### ↳ Re: Qualifying names

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:54:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af7b2fc6eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`
- **References:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`

```
On Monday, October 1, 2018 at 7:13:12 AM UTC+13, Mayer Goldberg wrote:
› When should one qualify names in cobol: Every time, or when there's a conflict?
› 
…[11 more quoted lines elided]…
› 

Only qualify if it is essential to do so.

Otherwise it is just clutter.

The only reason to have data names duplicated in different structures is to cater for MOVE CORRESPONDING and no one does that (in my experience) except in specific cases such as one-off file conversions.
```

#### ↳ Re: Qualifying names

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-30T19:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af7b2fc6eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`
- **References:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`

```
In article ,
Mayer Goldberg wrote:

[snip]

› What's a good practice?

The one that gets your code through Prod Review.

DD
```

#### ↳ Re: Qualifying names

- **From:** "kerry.liles" <ua-author-7511031@usenetarchives.gap>
- **Date:** 2018-10-01T10:19:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af7b2fc6eb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`
- **References:** `<a9b57dc9-64f0-401c-bbe7-0d6c91938b28@googlegroups.com>`

```
On 9/30/2018 2:13 PM, Mayer Goldberg wrote:
› When should one qualify names in cobol: Every time, or when there's a conflict?
› 
…[15 more quoted lines elided]…
› 

I would recommend only using qualification if required by the compiler
(in other words for data names that appear with the same name in more
than one structure). As another reply indicated, this is often
encountered to support MOVE CORRESPONDING - another one of those COBOL
constructs invented only to cause arguments among practitioners... :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
