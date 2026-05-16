[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# emptying a table <- What about this?

_1 message · 1 participant · 1999-10_

---

### Re: emptying a table <- What about this?

- **From:** Randall Bart <Barticus@usa.spam.net>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yD0OOKiiLzFtPEy1LDb4JSpbaIbN@4ax.com>`
- **References:** `<7u4ic4$544$1@news0.skynet.be> <LbkN3.2214$LW6.30493@news2.mia> <7u52mo$mcr@dfw-ixnews16.ix.netcom.com> <WroN3.43201$Ev4.39379@news3.mia> <7u8q08$19o@journal.concentric.net> <3807F4BD.AF9D5CFA@home.com> <7u9kaa$lf2$2@ssauraac-i-1.production.compuserve.com>`

```
The venerable "Russell Styles" <RWSTYLES@COMPUSERVE.COM> bestowed upon
comp.lang.cobol on Sat, 16 Oct 1999 06:06:31 -0400 these words:

>    Some compilers now complain about forward overlapping moves.  I assume
>that it impacts the algorythm used when copying from one area to another.
>Some compilers would drop back to byte at a time instead of 16 or 32 bits at
>a time.

It's not just a compiler issue, it's a hardware/microcode issue on
some systems.  This is where the compiler might produce code with
differing results on theoretically compatible computers.  The CPU
manuals always warn you of circumstances where overlapping moves are
undefined.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
