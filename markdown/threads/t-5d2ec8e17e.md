[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling Cobol from C (Microfocus Cobol)

_3 messages · 3 participants · 1996-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Calling Cobol from C (Microfocus Cobol)

- **From:** "or..." <ua-author-95833@usenetarchives.gap>
- **Date:** 1996-02-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3117d247.6853744@199.60.229.3>`

```
I have a client who needs to know how to call a MicroFocus program
from within C. Are there examples out there explaining how this is
done? Thank you.
```

#### ↳ Re: Calling Cobol from C (Microfocus Cobol)

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1996-02-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d2ec8e17e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3117d247.6853744@199.60.229.3>`
- **References:** `<3117d247.6853744@199.60.229.3>`

```

In article <311··.@199··9.3>, or··.@min··c.ca (Greg Goss) writes:
› I have a client who needs to know how to call a MicroFocus program
› from within C. Are there examples out there explaining how this is
› done? Thank you.

It depends what OS and version of COBOL and C compilers you are using. For
example, on Unix it's seamless (looks just like you're calling another C
function), but with a 16-bit product on DOS, it will most probably depend on
the specifics of the C compiler you're using (call conventions and the like).

Can you give more information please ?

Cheers, Kev.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

#### ↳ Re: Calling Cobol from C (Microfocus Cobol)

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-02-06T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d2ec8e17e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3117d247.6853744@199.60.229.3>`
- **References:** `<3117d247.6853744@199.60.229.3>`

```
In article <311··.@199··9.3>, or··.@min··c.ca says...
›
› I have a client who needs to know how to call a MicroFocus program
› from within C. Are there examples out there explaining how this is
› done? Thank you.

Try http://www.mfltd.co.uk/~mw/cobol_c/cobol_c.html

Shaun C. Murray                               | s.··.@mfl··o.uk (work)
Micro Focus Ltd, UK. http://www.mfltd.co.uk   | s.··.@doo··o.uk (home)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
