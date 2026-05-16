[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Win32 and timers...

_2 messages · 2 participants · 2000-02_

---

### Win32 and timers...

- **From:** "tommy" <tommynilsen@yahoo.com>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tifq4.355$Po1.6596@news1.online.no>`

```

Hi.

Does anyone have a sample of a cobol-program that uses a timer , created by
api-calls
to WIN32 ??

I'm having trouble getting it to work properly..

Thanks,

Tommy Nilsen
tommynilsen@yahoo.ocm
```

#### ↳ Re: Win32 and timers...

- **From:** JohndeV <johndevNOjoSPAM@yahoo.com.invalid>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2c2e3ab8.a5d2ec29@usw-ex0101-006.remarq.com>`
- **References:** `<tifq4.355$Po1.6596@news1.online.no>`

```
Tommy

Try this in your program;

       working-storage section.

       01 sleep-time    pic 9(8) comp-5.
       01 sleep-ok      pic 9(8) comp-5.

       procedure division.
           move 5000 to sleep-time

           call WINAPI "SleepEx" using
               by value sleep-time
               by value isFALSE size 4
               returning sleep-ok
           end-call


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
