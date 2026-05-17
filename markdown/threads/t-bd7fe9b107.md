[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MFCOBOL profiler

_1 message · 1 participant · 1997-02_

---

### MFCOBOL profiler

- **From:** "bert duerinck" <ua-author-17072731@usenetarchives.gap>
- **Date:** 1997-02-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32F9FEA0.3BEB@denkart.be>`

```

Hi,

I want to use MFCOBOL profiling, so what i did was i compiled my
programs with -p and -C PROFILE.

I have a main program that is written in c. This main program is
compiled to an object file and then linked with the cob command together
with some cobol object programs. I have also some cobol programs that
are compiled to int file. All my cobol programs are compiled with the -p
and the -C PROFILE options

This is the sequence in which they are executed:

- the main program calls a cobol int program with the cobfunc
function. ( for this program there is made a profile file, a .ipf
file)
Then this cobol file does a call to a cobol program that was linked
into the main program executable. (but when we call this program
there is no .ipf file created for this program and the info isn't
in the other .ipf file)
Then this cobol program calls a cobol int program (But when we call
this program there is also no .ipf file created for this program and
the info isn't in the existing .ipf file)

Does anybody know how it comes that we don't have profile info for those
2 last cobol programs and only for the 1st program???

Does anybody know how we can get profile info for those 2 last cobol
programs???

Bert Duerinck

e-mail: b.··.@den··t.be
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
