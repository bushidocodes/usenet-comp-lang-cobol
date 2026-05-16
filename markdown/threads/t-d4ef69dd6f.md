[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Message if record is kept ... II

_1 message · 1 participant · 1999-09_

---

### Message if record is kept ... II

- **From:** Vaclav Snajdr <snajdr.vaclav@t-online.de>
- **Date:** 1999-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37DCD01E.DC76097F@t-online.de>`

```
Thanks Russell, Thane and Michael for theit words .....

a) the version number is MF 4.0.5 on HP-UX or another Unixes

b) It is normally to minimize the time for locking records and the from
me described
     fall happens one or two times in the year. For your better
unterstanding I show you
     the follow picture

     Time 10.50 User A
     ..............................................................
     .  ArticleNo:    52135

..............................................................
Time 10.55 User B
     .   Name:
ABC
...........................................................
     .   price               <actual
entry                                        .  ArticleNo:  52135
     .   and so
on
............................................................

..............................................................
. Message:      Record Locked
      User A keeps the record to do
...........................................................
       same entries with rewrite after
      but he smokes now and read
The User B wish to change some data
      the
newspapers
of the same article too and try to read

with lock and receive the message:

Record Locked, but not from whom,

this is the point!!!!!!

       Also what I mean the rts gives out the information who is
occupied the record now.

        Servus - Vaclav
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
