[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RDUNX - read next on alternate index after Delete

_2 messages · 2 participants · 1998-02 → 1998-03_

---

### RDUNX - read next on alternate index after Delete

- **From:** "gregory" <ua-author-178382@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd44b0$6dab07e0$e94dcecd@gregory>`

```

Having a problem with Metacobol+ in a VS/CICS/Magec environment. Based on
the contents of the parameter card, this "file fix" program should add new
records and/or delete old records. The date of the record needs to be
changed, and it is part of the key, which is why delete/add is required.
The problem:

1) If the user chooses to add only, the processing logic should read next
through the file on alternate index (key 2), which begins with date. The
most recent dates are the problem, and this key positions me in the right
place really quickly - 5 minutes for the whole run compared to 30 minutes
for only about 1/8 of the file when key 1 was used.

2) If the user chooses to delete, the read next is causing an abend. My
interpretation is that it can't read next when it has just deleted the
record it was positioned at. In this case, read current record works.
Putting that in the processing loop is too dangerous, of course, since if
delete isn't chosen, the loop is never ending. Present approach is to
build the program with two discrete processing loops - do all the adds
first using read next, and then do all the deletes using read (current) -
(locky & redle to be precise).

Am certainly open to any other suggested approaches, but my real question
surrounds gaining a better understanding of alternate keys and deletes. An
existing program which deletes records, has a simple loop reading each
record, deleting whatever meets the criterion, then *reading next*. So how
can it work when mine won't? Obvious difference is that it is processing
on the primary key rather than an alternate. My only explanation as to why
my read next abends when the other one doesn't, is that an alternate key is
processed differently.

Any experience with alternate keys, or on the Metacobol rdunx/rdule/rduky
processing that you'd care to share? Have only worked in this environment
for 7 weeks, and have reviewed every Metacobol manual they have - but not a
one discusses these i/o verbs!

Regards, Pam··.@int··g.com
```

#### ↳ Re: RDUNX - read next on alternate index after Delete

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4f8b00cedb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd44b0$6dab07e0$e94dcecd@gregory>`
- **References:** `<01bd44b0$6dab07e0$e94dcecd@gregory>`

```

Gregory wrote in message <01bd44b0$6dab07e0$e94dcecd@gregory>...
› Having a problem with Metacobol+ in a VS/CICS/Magec environment.  Based on
› the contents of the parameter card, this "file fix" program should add new
…[34 more quoted lines elided]…
› 
I was hoping someone might have replied to this note by now. I want you to know that we aren't "ignoring you". It's just that
metacobol knowledge/experience is pretty limited these days. I few years ago, I had need to find some metacobol users and really
struggled to find any doing development with it. Maybe they are out there somewhere, but I wouldn't be surprised if you get limited
response to your question.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
