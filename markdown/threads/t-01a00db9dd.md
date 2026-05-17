[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Giving filnames in cobol

_2 messages · 2 participants · 1996-12_

---

### Giving filnames in cobol

- **From:** "ari..." <ua-author-17071987@usenetarchives.gap>
- **Date:** 1996-12-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59lkc8$45n@pravda.tisip.no>`

```

Hi
We have a Micro-Focus cobol-written program in pc-environment. Our data-files
is often located in a pc-server. When we write our Select-assign verb, we
use a set-parameter, who tell the program where to look after the files.
This can be like: Select Data-File
assign to "Set-Param\File-name.txt"

We use this sentence when assigning to a text-file. Now, we have a customer
who want to generate a new text-file for every order our system create.
Today, our textfile consist of a lot of orders, but our customer want to
create a new text-file for every order. How should we create our Select-
assign verb ? We want to use the Set-Param, so we can direct the file
to the right server, but we want the filename to be a order-number

Any suggestions ?

Thanks in advance

Arild Andersen
Trondeheim, Norway
```

#### ↳ Re: Giving filnames in cobol

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01a00db9dd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<59lkc8$45n@pravda.tisip.no>`
- **References:** `<59lkc8$45n@pravda.tisip.no>`

```

ari··.@col··t.no (Arild Andersen) wrote:

› Hi
› We have a Micro-Focus cobol-written program in pc-environment. Our data-files
…[14 more quoted lines elided]…
› Thanks in advance

I do not know your variant of cobol. But, it may support :
ASSIGN TO VARYING data-name.
data-name in working storage to play with.
The word VARYING may not be needed.

JR


› Arild Andersen
› Trondeheim, Norway

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
