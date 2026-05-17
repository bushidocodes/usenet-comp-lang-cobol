[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wang's COBOL85 Funkiness

_2 messages · 2 participants · 1995-01_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Wang's COBOL85 Funkiness

- **From:** "rsid..." <ua-author-17088230@usenetarchives.gap>
- **Date:** 1995-01-17T14:36:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-Msu-kByRAGY@usenetarchives.gap>`

```
I came across a problem with release 3.00.00 of Wang's COBOL85 complier. The
complier will take a simple addition compute statement and produce the wrong
answer. Consider the following statement:

COMPUTE [identifier-1] = [identifier-2] + [identifier-3] +
[identifier-4].

The statement will take the first non-zero identifier and stop. I've checked
this switching values around in the compute statement getting different
results based on where the non-zero identifier is located. Just for grins, I
enclosed the addition in parentheses and added a multiply by 1, and the
calculation worked just fine.

Has anybody got any idea what's going on here, or has had the same problem?
```

#### ↳ Re: Wang's COBOL85 Funkiness

- **From:** "dbr..." <ua-author-535048@usenetarchives.gap>
- **Date:** 1995-01-20T01:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-60bdce7ee1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-Msu-kByRAGY@usenetarchives.gap>`
- **References:** `<ua-fallback-Msu-kByRAGY@usenetarchives.gap>`

```
rsi··.@euc··d.com (Rodney Sidener) writes:

› I came across a problem with release 3.00.00 of Wang's COBOL85 complier.  The 
› complier will take a simple addition compute statement and produce the wrong 
› answer.  Consider the following statement:
 
› [ snip ]
 
› Has anybody got any idea what's going on here, or has had the same problem?

You have violated one of the basic tenents of computing...

never install a product who's version number ends in zero.



Nice to know there's another Wanger out there.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
