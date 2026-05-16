[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Anyone moving their system to Linux from Microfocus Cobol on SCO Open Server ?

_2 messages · 2 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Anyone moving their system to Linux from Microfocus Cobol on SCO Open Server ?

- **From:** "Stephen B." <steveno@spamcfs.com.au>
- **Date:** 2001-04-02T17:17:13+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ac82b13@nexus.comcen.com.au>`

```
Anyone moving their system to Linux from Microfocus Cobol on SCO Open
Server?

What technical and licensing problems and solutions did you find ?

Have you any useful suggestions ?

PS. We are also interested if you moved from the older SCO 3.2.4.2.

Thanks,
Stephen
```

#### ↳ Re: Anyone moving their system to Linux from Microfocus Cobol on SCO Open Server ?

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-04-02T18:52:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mbehct48p9oj7drftarqd4ick5v3j4ge3h@4ax.com>`
- **References:** `<3ac82b13@nexus.comcen.com.au>`

```
ghItlh "Stephen B." <steveno@spamcfs.com.au> 

>Anyone moving their system to Linux from Microfocus Cobol on SCO Open
>Server?
…[9 more quoted lines elided]…
>

I have no idea about licensing as it's a commercial issue and that's
another department.

However, during an experiment in late 1999, [that was never taken
forward] I moved a very big product (around 30 million lines of COBOL,
I think) from OCDS 4.1 on mainstream unix (Dynix actually) to OCDS 4.1
on Linux with not one single COBOL platform issue [many many database
access issues but that's another story; the COBOL itself was fine].
The level of compatibility is very high. You should be aware of
endianess issues though if your SCO system is non intel (and if you
have any code which relies on this such as pointer manipulation or
reference modified or redefined access to binary storage).

There were issues with a whole bunch (around 15,000) lines of C code
that was linked into the runtime. The C code needed about 40 hours
work to move it from unix vendor specific C to something GCC was happy
with, and most of this was tinkering with the screen handling (which
uses curses/ncurses).

Not too shabby really. 

Really though, we need a good compatible open source COBOL on
GNU/Linux. Tiny Cobol is getting there but it's far from complete.
I'm trying marginally (i.e. not) successfully to contribute to Tims
GCC project (if only I could consistently get the EXISTING work to
build!!).

Of course, as usual, YMMV.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
