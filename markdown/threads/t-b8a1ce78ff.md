[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GPE in Fujitsu Power COBOL

_1 message · 1 participant · 1997-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### GPE in Fujitsu Power COBOL

- **From:** "laszlo=erdos%ew..." <ua-author-17071586@usenetarchives.gap>
- **Date:** 1997-07-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9707081715.aa01889@sco.stg.hu>`

```

Hello,

I found an interesting mistake in Fujitsu Power COBOL. I developed
a big application with this program. I have a little main EXE
and a lot of DLL, every window in different DLL-s. These are all
Power COBOL files with window handling. Moreover there are DLL-s
without handling of window (screen). These are not Power COBOL,
but COBOL85 (Programming Staff) DLL-s.


MAIN.EXE----|-----POWCOB_1.DLL-------|
| COB85_1.DLL
|-----POWCOB_2.DLL-------|
…[3 more quoted lines elided]…
|
.
.
.
.
|
|-----POWCOB_n.DLL-------|
| COB85_n.DLL


Usually some Power COBOL DLL call one COBOL85 DLL. For example
I handle the listing and printing functions in COBOL85 DLL.
This is very useful because I can call the same function from
different windows, and I needn't write same programs in
all Power COBOL DLL-s.

The mistake is follow:
1. If I don't handle file in COBOL85 DLL-s, then everything
work OK.

2. If I handle files (open, write, read etc.) then:

a.) the first call of COBOL85 DLL procedure works well.
For example I can print 4 copy of a list directly to
printer. Or I can generate a file. (The mistake independent
from printing!)

b.) the second time call of COBOL85 DLL procedure cause
the GENERAL PROTECTION ERROR in F1BCIO.DLL. Doesn't
matter you call the same COBOL85 DLL or another which
handles files. After it the program crashed!

c.) after the application was crashed, I ran the program
newly, without exiting from windows. Then I called
the COBOL85 DLL procedures many times without any
mistake! If I exit from windows then begin everything
from point a.) !

I tried this flow on different PCs, and always was the same!

Later I take my COBOL85 procedures code in Power COBOL DLLs.
This works well, but I have the same code in a lot of places,
and I got very big DLLs, and this is not a good result.

If you can, please help me,

with best regards

Laszlo Erdos

mail.: er··.@s··.hu
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
