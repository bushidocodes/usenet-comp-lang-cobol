[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I show decimal pt. values??

_3 messages · 3 participants · 1998-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How do I show decimal pt. values??

- **From:** "anonymous" <ua-author-4@usenetarchives.gap>
- **Date:** 1998-03-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dt84v$fu9@bgtnsc03.worldnet.att.net>`

```

I'm very much a rookie at COBOL so I apologize if the following question is
offensively stupid:

How do I make my decimal point values appear? In my program (I'm using
COBOL II) my pic clauses are set up as pic $$,$$9.99. yet when I perform a
calculation with other fields (which have similar pic clauses including the
two decimal points) I always get two zeros after the decimal point instead
of actual numbers.

Any help will be greatly appreciated
```

#### ↳ Re: How do I show decimal pt. values??

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db5ed2d01b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6dt84v$fu9@bgtnsc03.worldnet.att.net>`
- **References:** `<6dt84v$fu9@bgtnsc03.worldnet.att.net>`

```

Anonymous wrote in message <6dt84v$f.··.@bgt··t.net>...
› I'm very much a rookie at COBOL so I apologize if the following question is
› offensively stupid:
…[9 more quoted lines elided]…
› 
You normally do arithmetic on numeric fields and then move the results to a
numeric-edited field for "display". However, working with numeric-edited
fields should NOT result in loss of significant digits. Can you post a
sample with just the fields' definitions and the arithmetic statement?
There may be something else that you are missing that is causing the
"truncation".
```

#### ↳ Re: How do I show decimal pt. values??

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-03-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db5ed2d01b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6dt84v$fu9@bgtnsc03.worldnet.att.net>`
- **References:** `<6dt84v$fu9@bgtnsc03.worldnet.att.net>`

```

Anonymous wrote:
› 
› How do I make my decimal point values appear?  In my program (I'm using
…[3 more quoted lines elided]…
› of actual numbers.

In your calculation fields, the decimal point needs to be defined with
the PICTURE character V, eg, the field that you're moving to PIC
$$,$$9.99 should have a PIC 9999V99

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-310-542-6013                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ The puzzle too hard for human beings:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
