[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Timer Routine?

_1 message · 1 participant · 2000-12_

---

### Timer Routine?

- **From:** "Kevin" <kksys@optonline.net>
- **Date:** 2000-12-08T16:13:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6N7Y5.410160$4d.52564617@news02.optonline.net>`

```
I have an application that uses a security key dongle. The key requires that
it be polled every 90 seconds to ensure that the application is still
active.

I am trying to determine the best method of accomplishing this without using
too many system resources.

I have thought about creating a thread that would check the time and after
90 seconds,  poll the key.
I also understand there is a Win API called "SLEEP" that would create a
pause that I could use in the thread that checks the key.

Has anyone ever done anything like this?
Does anyone know of the best way to do this without expending too many
resources?
Any ideas would be appreciated.

Thanks,
Kevin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
