[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Programming St���������������

_2 messages · 2 participants · 1995-02_

---

### COBOL Programming St���������������

- **From:** "colin..." <ua-author-5711152@usenetarchives.gap>
- **Date:** 1995-02-09T17:06:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8A3356A.09D2000521.uuout@almac.co.uk>`

```
JW> Nonetheless, old habits die hard and I still bring in contractors wh
JW> insert these "handles" into the code they write for me.

Well answered, Jerry. I could be one of those old contractors and agree
wholeheartedly with your answer. However, there are still times when
ABEND-AID fails and you have to take old-fashioned dumps and those
"handles" are invaluable even if only for checking that you can still do
hexadecimal arithmetic! I'm working in such an environment now :-(

Not so long ago, I even reconstructed a lost COBOL source program from a
dump, much to the astonishment of the rest of the department.

While I'm writing, I may as well tell you of some more oldstagers tricks.
On file headers, always try to fill otherwise unused parts of the header
record with some meaningful data about the file - especially if you
can't get it from the operating system; try to use USAGE DISPLAY numbers
on files to make them easy for *YOU* to read if you have to (remember
that you are the most expensive peripheral, the users are the slowest);
and when you're writing code the rule is KISS - you'll be glad of it
later :-)
---
* RM 1.3 00712 * If thine enemy offend thee, give his child a drum.
```

#### ↳ Re: COBOL Programming St���������������

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-02-12T10:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fad8e6beb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<8A3356A.09D2000521.uuout@almac.co.uk>`
- **References:** `<8A3356A.09D2000521.uuout@almac.co.uk>`

```
On Thu, 09 Feb 95 23:06:00 +0100, COLIN SMITH (col··.@alm··o.uk) wrote:

› Not so long ago, I even reconstructed a lost COBOL source program from a
› dump, much to the astonishment of the rest of the department.

Did I read this right? You reconstructed a COBOL program out of thin
air and machine code? Please share your technique with the rest of
us.

//---------------------------------------------------------------
// Joseph I. Tsatskin   jts··.@pri··t.com
//                      jts··.@azt··u.edu
//                      jts··.@bcf··l.us
//---------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
