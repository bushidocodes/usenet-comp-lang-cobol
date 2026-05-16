[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data conversion on READ (why not?)

_1 message · 1 participant · 1999-11_

---

### Re: Data conversion on READ (why not?)

- **From:** roadraat@aol.com (RoadRaat)
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991120153441.08843.00000540@ng-xa1.aol.com>`
- **References:** `<38359E26.53A4FE3@bigfoot.com>`

```
>for the example that you've given us, not only is it an "elegant" way
>to accomplish what you are trying to accomplish, there is NO JUSTIFIABLE
>reason NOT to do it that way.

Thanks for the vote of confidence.  You mentioned abends.  My program never
abended.  The problem with tracing an abend was brought up by another who
responded to this thread.

My project assumed that the input data had already been edited.  Jeff Farkas
brought up the wisdom of NEVER taking this for granted in the real world.

My project works when I dummy the input file in my JCL, but one thing I never
checked out was what happens if I put alpha data on one of those fields that I
want to move to a comp-3 field.  I'll bet I'm toast when I do that.  Once
again, I'm okay according to the specs of my student project, but I was hoping
I could invent a way to perform conversions neatly out in the real world, too.

RoadRaat
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
