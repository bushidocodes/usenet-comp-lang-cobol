[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with reading of negative numbers in data file

_2 messages · 2 participants · 2000-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with reading of negative numbers in data file

- **From:** "David Cole" <david-rc@worldnet.att.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7JTG4.15276$TM.922755@bgtnsc06-news.ops.worldnet.att.net>`

```
If you can help on this I sure would appreciate a quick reply.  Using
MicroFocus COCOL.  Data files built with Notepad as line sequential.
Balance fields have some negative values, and these data fields were keyed
using an alphabetic letter in the last digit position as an embedded sign
per ASCII standards.  Have done this for years on AS400 (with EBCDIC of
course) without problem.  Can't get the programs to run past the first
negative data item.  Compiles are fine.

I have added the clause 'sign is trailing' to the signed pic clauses of the
fields.  I did not add this on first attempts, but gave it a try when runs
aborted.  At run time, the program reads the record, but gives an 163 error
illegal character in numeric field message.

My MicroFocus literature is no help, and I have consulted a dozen COBOL
texts.  All discuss using signed picture clauses, but do no dwell on
negative value storage with microcomputer COBOL.  This is our first full
session teaching COBOL on microcomputers, as the AS/400 died recently, and
the class must go on.  I don't ever recall having this problem in past
seasons, but maybe the programs just did not happen to have negative values
when we briefly used the microcomputers.

I thank you in advance if you can shed some light on this - somehow I am
just not getting the problem solved.
```

#### ↳ Re: Help with reading of negative numbers in data file

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EC0BC6.A92103F9@home.com>`
- **References:** `<7JTG4.15276$TM.922755@bgtnsc06-news.ops.worldnet.att.net>`

```


David Cole wrote:
> 
> If you can help on this I sure would appreciate a quick reply.  Using
> MicroFocus COCOL.  Data files built with Notepad as line sequential.
> Balance fields have some negative values, and these data fields were keyed

David,

To stop all the guessing that will go on for sure, can you post some
source and sample data-file ? Then somebody in NG can zero-in on
specifics.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
