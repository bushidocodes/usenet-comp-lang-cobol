[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 74 question

_3 messages · 3 participants · 1995-10_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Cobol 74 question

- **From:** "rtin..." <ua-author-9439303@usenetarchives.gap>
- **Date:** 1995-10-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44sgdm$dhf@guava.epix.net>`

```
I have a question for those that are sharp in
cobol 74.When formating a dl-header line
with the character '=' , what is the forumla
for getting this character to print the
same row but 80 columns wide? I am using
this character to seperate my other 3 dl-headers.

05 FILLER PIC X(80) VALUE '='.

This I know will only print 1. But there has to
be a better way then putting 80 = in a row.
I could do this in Pascal and C, but
I am learning Cobol 74.
Thanks,
Randy
```

#### ↳ Re: Cobol 74 question

- **From:** "mike giaquinto" <ua-author-13690527@usenetarchives.gap>
- **Date:** 1995-10-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5adde45e6b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<44sgdm$dhf@guava.epix.net>`
- **References:** `<44sgdm$dhf@guava.epix.net>`

```
rti··.@ep··x.net (Randy Tingley) wrote:
› I have a question for those that are sharp in 
› cobol 74.When formating a dl-header line 
…[13 more quoted lines elided]…
› 
Hi Randy,
Have you tried the ALL figurative constant?
05 FILLER PIC X(80) VALUE ALL '='.
This will fill the entire area with '======'.
It also works with multiple characters, i.e.,
05 FILLER PIC X(80) VALUE ALL 'ABCD'.
will repeat the string ABCD 20 times.

Mike Giaquinto
```

#### ↳ Re: Cobol 74 question

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1995-10-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5adde45e6b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<44sgdm$dhf@guava.epix.net>`
- **References:** `<44sgdm$dhf@guava.epix.net>`

```
r.··.@int··s.com (Richard Bergdahl) wrote:
››
›
…[3 more quoted lines elided]…
› with COBOL 74.

This _should_ work as it has been in every ANSI X3.23 standard
since at least COBOL 68. Some lesser implementations used to
limit the literal after the reserved word ALL to one character,
but multiple characters is by now almost universal.


Tom Morrison, T.M··.@li··t.com
Relativity (div. Liant Software)
512-719-7019  FAX:512-719-7070  WWW: http://www.liant.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
