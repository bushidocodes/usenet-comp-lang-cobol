[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pointers and Dynamic Allocation

_1 message · 1 participant · 1999-12_

---

### Pointers and Dynamic Allocation

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385D4317.DBA921C3@melbpc.org.au>`

```
The use of pointers requires an organised disciplined approach.
This applies with COBOL or C. I've seen COBOL programs using
pointers with memory leaks all over the place. 

One team replaced the individual getmains with a common memory
allocation routine and eliminated the leaks and storage overlays. 

The other team went with the "real programmers don't need
training wheels" approach and had endless problems, including
production downtime. It's funny, in a way programming is like
safe driving. It's not how good a driver you are, but whether you
are as good as you think you are - do you drive within your
ability and the conditions.

I use dynamic allocation when it adds value. 

One problem static programs have is fixed limits. 

Dynamic allocation allows you to have no fixed limits. "Sorry you
can only have 100 lines of transaction history because we had to
pick some number in the occurs and we chose 100". Sometimes this
is important.

That is one of the nice things about Java; you can have your cake
and eat it too (kind of).

The standards committee has added everything but the kitchen sink
to COBOL in the new standard CD1.7. 

They have made everything mandatory including report writer and
the OO extensions. COBOL is already a huge
language and this will make the problem worse.

In effect they have turned COBOL into C++ with three exceptions:

English like syntax. Although noone really believes PHBs can
actually read COBOL.
Decimal arithmetic.
Reserved words by the score.

Tim Josling


Rick Smith wrote:
> 
> Judson McClendon wrote in message ...
> [...]
> >One of the things in C/C++ and many other languages that contribute most
> >to broken code and horrible debugging problems is the use of pointers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
