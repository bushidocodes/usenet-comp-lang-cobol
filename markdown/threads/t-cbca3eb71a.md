[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Getting rid of trailing spaces

_1 message · 1 participant · 1999-09_

---

### RE: Getting rid of trailing spaces

- **From:** Peter van Zeeland <peter.van.zeeland@cmg.nl>
- **Date:** 1999-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6DE2D20B5851D2119BB300A0C9DAF698498E1F@NL-AMB-MAIL01>`

```
Pardon me for intruding, but this approach requires previous knowlegde of
both number of fields and maximum field size, and thereby making the program
single-purpose. Furthermore, the inspect and string/unstring statements are
overkill.

For the task at hand, I would take another approach.

read the input record back to front on a character by character basis using
reference modification, 
skipping the trailing spaces, and the spaces after (=before) ending quotes,
moving all other characters
to a ws-field. Then write the output record from the ws-field backward
again.

This would require only two perform varying... loops and require no
knowledge of the fields and their
contents. Only the maximum record size. And the program becomes
multi-purpose.

For a real nice job, I would make the output file a byte-stream to eliminate
trailing spaces at record level in the outfile.

Would you agree ?


> -----Original Message-----
> From:	peter dashwood [SMTP:dashwood@freewebaccess.co.uk]
…[199 more quoted lines elided]…
>  http://www.deja.com/thread/%3C37cf3155%40eeyore.callnetuk.com%3E


 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
