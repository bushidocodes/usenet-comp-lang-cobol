[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Syntax Question (arrays)

_4 messages · 4 participants · 2001-01 → 2001-02_

---

### Syntax Question (arrays)

- **From:** "Don" <mengd@home.com>
- **Date:** 2001-01-31T20:21:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a78b93b_2@spamkiller.newsfeeds.com>`

```
If I have an array of 50 elements in COBOL, the first element is accessed as
ARRAY(1) and the 50th element is ARRAY(50).  Can I change the subscripting
so the first element of the array starts at subscript 8200, and the 50th
element is ARRAY(8249)?  I could do it in PLI.  Is there a way to do it in
IBM mainframe COBOL 370?
```

#### ↳ Re: Syntax Question (arrays)

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2001-01-31T19:35:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95aeb0$gk1oi$1@ID-39920.news.dfncis.de>`
- **References:** `<3a78b93b_2@spamkiller.newsfeeds.com>`

```

Don <mengd@home.com> wrote in message
news:3a78b93b_2@spamkiller.newsfeeds.com...
> If I have an array of 50 elements in COBOL, the first element is accessed
as
> ARRAY(1) and the 50th element is ARRAY(50).  Can I change the subscripting
> so the first element of the array starts at subscript 8200, and the 50th
> element is ARRAY(8249)?  I could do it in PLI.  Is there a way to do it in
> IBM mainframe COBOL 370?
>

No, but you can modify the subscript easily.

IE -

COMPUTE SUB1 = OCCR - 8199.

MOVE ARRAY(SUB1) TO ....

where OCCR is your original number (8200-8249)....
```

##### ↳ ↳ Re: Syntax Question (arrays)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-31T21:20:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95akls$r32$1@slb7.atl.mindspring.net>`
- **References:** `<3a78b93b_2@spamkiller.newsfeeds.com> <95aeb0$gk1oi$1@ID-39920.news.dfncis.de>`

```
"DBuck" <dbuck@prairieinet.net> wrote in message
news:95aeb0$gk1oi$1@ID-39920.news.dfncis.de...
>
> Don <mengd@home.com> wrote in message
> news:3a78b93b_2@spamkiller.newsfeeds.com...
> > If I have an array of 50 elements in COBOL, the first element is
accessed
> as
> > ARRAY(1) and the 50th element is ARRAY(50).  Can I change the
subscripting
> > so the first element of the array starts at subscript 8200, and the 50th
> > element is ARRAY(8249)?  I could do it in PLI.  Is there a way to do it
in
> > IBM mainframe COBOL 370?
> >
…[11 more quoted lines elided]…
>

or possibly even more easily

   Move array (sub1 - 8199) to ...

(using "relative indexing" - which does work with both subscripts and
indexes)
```

#### ↳ Re: Syntax Question (arrays)

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-01T07:24:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A797196.3EB3B565@brazee.net>`
- **References:** `<3a78b93b_2@spamkiller.newsfeeds.com>`

```
Don wrote:

> If I have an array of 50 elements in COBOL, the first element is accessed as
> ARRAY(1) and the 50th element is ARRAY(50).  Can I change the subscripting
> so the first element of the array starts at subscript 8200, and the 50th
> element is ARRAY(8249)?  I could do it in PLI.  Is there a way to do it in
> IBM mainframe COBOL 370?

I've always wanted this ability.  There are times when it fits the business
model well.  The most common way around this is to modify the subscript e.g.
ARRAY(MY-INDEX - 8240).

A couple of times, I have simply wasted some space by starting at 1, but not
using the first x (in your case the first 8199) occurrences.  There is a trade
off here depending on how much space you're wasting, and how such wasted space
effects performance on your system.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
