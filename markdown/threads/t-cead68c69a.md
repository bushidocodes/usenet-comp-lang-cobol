[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What's a Boundary Error?

_2 messages · 1 participant · 1996-08_

---

### What's a Boundary Error?

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-08-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4v2v9v$s2c@nnrp1.news.primenet.com>`

```

My co-worker created an indexed file, then tried to read it with another
program. Same FD, same key. The program can't read the file. When
stepping through the program with Animator, he got a Status 44 on the OPEN
INPUT for this file -- 44 translates to "Boundary Error."

We can't identify anything he's done outside our normal routine, so at
this point he's trying various "voodoo" changes to the program to see if
he can appease the Spirits of Runtime.....

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

#### ↳ Re: What's a Boundary Error?

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-08-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cead68c69a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4v2v9v$s2c@nnrp1.news.primenet.com>`
- **References:** `<4v2v9v$s2c@nnrp1.news.primenet.com>`

```

On Friday I wrote:
: My co-worker created an indexed file, then tried to read it with another
: program. Same FD, same key. The program can't read the file. When
: stepping through the program with Animator, he got a Status 44 on the OPEN
: INPUT for this file -- 44 translates to "Boundary Error."

Well, he opened the file I-O instead of just INPUT, and the problem went
away. But we still don't know what a "Code 44 -- Boundary Error" might
be, or why the Micro Focus Runtime doesn't want him to open this file in
read-only mode!

Can anyone comment on this?

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
