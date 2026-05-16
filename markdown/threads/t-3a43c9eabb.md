[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ATTN:>donald tees

_3 messages · 2 participants · 1998-10_

---

### ATTN:>donald tees

- **From:** SkidMike <skidmike@mindspring.com>
- **Date:** 1998-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36324841.E2657356@mindspring.com>`

```
thanks for the code you sent.  i have the .kbd file printed and taped to
my wall (i'll be doing some rewrites tomorrow <g>)
i see how you can get a small window now, but i have 2 questions:	
explain the phrase CONSOLE IS CRT 
and how come i still can't get MORE than 80x24.  i followed what you
did, but still have the same size.
can i use only certain values for row and column?  do they have to be a
certain value when multiplied?
```

#### ↳ Re: ATTN:>donald tees

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70ttjl$ff8$1@news.igs.net>`
- **References:** `<36324841.E2657356@mindspring.com>`

```

SkidMike wrote in message <36324841.E2657356@mindspring.com>...

>explain the phrase CONSOLE IS CRT

Well, to tell the truth, I do not have a clue what it does in Fujitsu.  That
bit of code was converted from DOS, different compiler, and that is
a leftover.  The norm is that display is directed to the screen for the
screen section, but statements like "display test" go to the console,
which is a totally different window.  It might just put everything onto
the console, and it might be a no-op.  Once I get the other 50,000 lines
of code on my plate converted, maybe I will have time to play and find out.

That program made a good test, and I wanted to use it, so once it worked
I just put it on my desktop and left it.  I sent it because is is small and
stand alone so it makes a good example.  It is probably also a good
example of use of the copy.  Those date routines are in use in dozens
of programs, and the program you have is the test routine. It should
probably be converted to a subroutine for Fujitsu code under Windows.

>and how come i still can't get MORE than 80x24.  i followed what you
>did, but still have the same size.
>can i use only certain values for row and column?  do they have to be a
>certain value when multiplied?

The docs only say that the total screen area cannot be more than 16K
characters.  I am converting DOS code, so have not tested screens
larger than 80*25, but have used that with no problem.  It may have to
do with your screen resolution. I am using a 19" screen cranked up pretty
high, and can get 4  80*24 screens on it. I'll test to-morrow on a different
screen/screen card, and get back to you.
```

#### ↳ Re: ATTN:>donald tees

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70tvj7$go6$1@news.igs.net>`
- **References:** `<36324841.E2657356@mindspring.com>`

```

SkidMike wrote in message <36324841.E2657356@mindspring.com>...
>thanks for the code you sent.  i have the .kbd file printed and taped to


As a PS to that last message.  That particular .KBD file was set up
to duplicate the scan codes picked up in assembler for a Microsoft
Cobol program running under DOS.  I did not want to change the programs
so I figured out how to get Fujitsu to give me the same numeric results
for the same keystrokes.

While the methodology is neat, personally I would choose different values
if I was going to set up a new system from scratch.  Probably the best
way to do it is to set up a new KBD file that is easy to remember, then
the values as a set of 88 level names that you copy from a file.  That will
keep your code logic separate from the keyboard keys that trigger it, and
make it easy to change if you ever have to.  If that does not make sense,
say so and I will type in an example.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
