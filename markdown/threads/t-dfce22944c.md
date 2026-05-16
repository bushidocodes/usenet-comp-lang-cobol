[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Implementors confused about NEXT SENTENCE

_1 message · 1 participant · 2003-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Implementors confused about NEXT SENTENCE

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-14T13:12:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2jf37$6at$1@slb1.atl.mindspring.net>`

```
As a follow-up on another thread, I did want to confirm that at least one
"early implementor" of the '85 Standard *did* mis-understand the difference
between CONTINUE and NEXT SENTENCE.

In its first (and it was - I believe THE first) '85 Standard compiler, Micro
Focus treated a "next sentence" as the same as a CONTINUE.  This was
"particularly" obvious - because they also had an extension where "Next
Sentence" was a valid imperative statement - allowed within the conditional
phrase of any verb.

HOWEVER, this "error" was corrected quite early (certainly before 1990).
Micro Focus did, in its usual "support ALL upward compatibility" manner,
provide an "OLDNEXTSENTENCE" directive to support those who "wanted" a "Next
Sentence" to work as a "CONTINUE".   This was not the default - and is
clearly marked as non-ANSI/ISO conforming.

I don't know if there were any other implementors that had the same problem
or not - but it did show that (contrary to what I said in one of my other
posts) that there was at least some room for "confusion" in the Standard -
even among those who know COBOL and "standard-ize" well.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
