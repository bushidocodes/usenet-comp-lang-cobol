[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TISAM the age old question

_3 messages · 3 participants · 1998-02_

---

### TISAM the age old question

- **From:** "rkri..." <ua-author-13460296@usenetarchives.gap>
- **Date:** 1998-02-19T19:46:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cijoc$b9j$1@nnrp1.dejanews.com>`

```

I am working on a cobol program which calls a c program. This program
works fine on our CISAM systems and we have created a rts which has the c
program statically linked to it which we use to run the cobol probram. We are
now interfacing with a system which although it uses the same operating
system, is using TISAM files. When we try to run our program with our
statically linked rts, the program incorrectly uses CISAM file types and can
not read and write data properly. If we re-compile the rts on that TISAM
system, there is an error message "114" indicating that we are attempting to
access an item beyond bounds of memory. This may be due to the TISAM compiler
being an earlier version MF 3.1 as opposed to MF 3.25.

When we run the rts compiled on the TISAM compiler, the file attempts
to open the file in CISAM mode. If we run another program, but initiate it
with the cobrun command, the file opens correctly in TISAM mode. It would
appear that the rts we compiled is not observing the file type. Is there a
way to configure our run-time to use TISAM file types?

Thanx in advance
Rajesh

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: TISAM the age old question

- **From:** "grj..." <ua-author-14608199@usenetarchives.gap>
- **Date:** 1998-02-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c8f5fbac2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6cijoc$b9j$1@nnrp1.dejanews.com>`
- **References:** `<6cijoc$b9j$1@nnrp1.dejanews.com>`

```

rkr··.@ik··n.com wrote:

: When we run the rts compiled on the TISAM compiler, the file attempts
: to open the file in CISAM mode. If we run another program, but initiate it
: with the cobrun command, the file opens correctly in TISAM mode. It would
: appear that the rts we compiled is not observing the file type. Is there a
: way to configure our run-time to use TISAM file types?

You must link the rts with TISAM. Look in the /usr/ti/README file for
instructions or call me.

Glen Johnson
CSI
512-343-6634
```

#### ↳ Re: TISAM the age old question

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-02-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c8f5fbac2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6cijoc$b9j$1@nnrp1.dejanews.com>`
- **References:** `<6cijoc$b9j$1@nnrp1.dejanews.com>`

```

Hi Rajesh,

rkr··.@ik··n.com wrote:
› 
›         I am working on a cobol program which calls a c program.  This program
…[5 more quoted lines elided]…
› not read and write data properly.
 
› OK, I'm with you so far ....
 
›  If we re-compile the rts on that TISAM
› system, there is an error message "114" indicating that we are attempting to
› access an item beyond bounds of memory.  This may be due to the TISAM compiler
› being an earlier version MF 3.1 as opposed to MF 3.25.

Now I'm lost. What do you mean by "re-compile" the RTS ? Do you mean
re-compile
your C program and re-link the RTS ? I'm not sure what you mean by TISAM
compiler, either, as TISAM is an ISAM library, not a compiler - the C
compiler
you are using should be the same, AFAIK. Can you clarify this, please.
You shouldn't need to recompile any of the COBOL programs.

› When we run the rts compiled on the TISAM compiler, the file attempts
› to open the file in CISAM mode.

I don't understand "the file attempts to open the file" - are you
referring to
your C program, or some COBOL program (or both) ?

› If we run another program, but initiate it
› with the cobrun command, the file opens correctly in TISAM mode.  It would
› appear that the rts we compiled is not observing the file type.  Is there a
› way to configure our run-time to use TISAM file types?

When you relink your RTS (using "cob" or "makerts"), try including the
following option on the command line:

-m ixfile=tixfile

(I *think* there should be a space after the -m, off the top of my
head).
If that doesn't work, then please try clarifying some of the points
above.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
